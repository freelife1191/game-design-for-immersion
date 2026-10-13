#!/usr/bin/env python3
"""Validate this book skill's structure, references, source identity and tables."""
import argparse
import dataclasses
import hashlib
import importlib.util
import json
import re
import sys
from decimal import Decimal
from pathlib import Path

import yaml

sys.dont_write_bytecode = True


def validate(root, project_root, source_pdf=None):
    root = root.resolve()
    errors = []
    checks = {}

    def require(condition, message):
        if not condition:
            errors.append(message)

    required = ["SKILL.md", "agents/openai.yaml", "source.json",
                "references/index.md", "references/coverage.md",
                "references/figures-and-formulas.md", "references/glossary-extended.md",
                "references/review-history.json", "glossary.md", "patterns.md", "cheatsheet.md"]
    for name in required:
        require((root / name).is_file(), f"Missing: {name}")
    if errors:
        return {"status": "FAIL", "errors": errors}

    spec = importlib.util.spec_from_file_location(
        "bundle_security", project_root / ".agents/skills/book-to-skill/tools/scan_generated_skill.py")
    scanner = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = scanner
    spec.loader.exec_module(scanner)

    md_files = sorted(root.rglob("*.md"))
    findings, broken_links, placeholders, foreign_text = [], [], [], []
    link_count = 0
    for file in md_files:
        require(not file.is_symlink(), f"Nested Markdown symlink: {file}")
        require(file.stat().st_size <= 2 * 1024 * 1024, f"Oversized file: {file}")
        text = file.read_text(encoding="utf-8")
        findings.extend(dataclasses.asdict(x) for x in scanner._scan_text(str(file.relative_to(root)), text))
        if re.search(r"\[TODO:|\bTBD\b", text):
            placeholders.append(str(file.relative_to(root)))
        if re.search(r"[ぁ-ヿ]", text):
            foreign_text.append(str(file.relative_to(root)))
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if target.startswith(("https:", "http:", "#")):
                continue
            link_count += 1
            if not (file.parent / target.split("#")[0]).is_file():
                broken_links.append([str(file.relative_to(root)), target])
    require(not findings, "Security scan has findings requiring human review")
    require(not broken_links, "Broken relative file links")
    require(not placeholders, "Unfinished placeholders")
    require(not foreign_text, "Unexpected Japanese prose")
    checks.update(markdown_files_scanned=len(md_files), links_checked=link_count,
                  security_findings=findings, broken_links=broken_links,
                  placeholders=placeholders, unexpected_japanese_text=foreign_text)

    source = json.loads((root / "source.json").read_text())
    history = json.loads((root / "references/review-history.json").read_text())
    chapters = list((root / "chapters").glob("*.md"))
    sections = list((root / "references/sections").glob("*.md"))
    require(len(chapters) == len(source["chapters"]) == 4, "Original chapter count mismatch")
    require(len(sections) == len(source["sections"]) == 18, "Major section count mismatch")
    require(len(source["subsections"]) == 79, "Subsection coverage mismatch")
    for row in source["chapters"] + source["sections"] + source["subsections"]:
        require((root / row["file"]).is_file(), f"Missing mapped source file: {row['file']}")
        require(row["pdf_start"] == row["book_start"] + 16 and row["pdf_end"] == row["book_end"] + 16,
                f"Page convention mismatch: {row}")
    for row in source["sections"]:
        text = (root / row["file"]).read_text()
        match = re.search(r"목차 탐색 범위:\*\* 본문 (\d+)–(\d+)쪽 / PDF (\d+)–(\d+)쪽", text)
        require(match is not None, f"Section page metadata missing: {row['file']}")
        if match:
            actual = tuple(map(int, match.groups()))
            expected = (row["book_start"], row["book_end"], row["pdf_start"], row["pdf_end"])
            require(actual == expected, f"Section page metadata differs: {row['file']}")
    for row in source["subsections"]:
        parent = next(x for x in source["sections"] if x["section_id"] == row["section_id"].rsplit(".", 1)[0])
        require(parent["book_start"] <= row["book_start"] <= row["book_end"] <= parent["book_end"],
                f"Subsection outside parent range: {row['section_id']}")
    require(history["claims_checked"] == sum(len(a["claims_checked"]) for a in history["audits"]),
            "Claim evidence count mismatch")
    require(history["content_findings_resolved"] == sum(len(a["findings"]) for a in history["audits"]),
            "Correction evidence count mismatch")
    checks.update(chapter_files=len(chapters), section_files=len(sections),
                  subsections=len(source["subsections"]), source_claims_checked=history["claims_checked"],
                  section_header_ranges_checked=len(source["sections"]))

    frontmatter = (root / "SKILL.md").read_text().split("---", 2)[1]
    meta = yaml.safe_load(frontmatter)
    require(meta["name"] == "game-design-for-immersion", "Skill ID mismatch")
    require(isinstance(meta["description"], str) and len(meta["description"]) <= 1024, "Description invalid")
    ui = yaml.safe_load((root / "agents/openai.yaml").read_text())["interface"]
    require(25 <= len(ui["short_description"]) <= 64, "UI description length invalid")
    require("$game-design-for-immersion" in ui["default_prompt"], "Default prompt misses skill ID")

    sys.path.insert(0, str(project_root / ".agents/skills/book-to-skill"))
    from book_to_skill.utils import estimate_tokens
    budgets = {}
    for name, limit in [("SKILL.md", 4000), ("glossary.md", 1500), ("patterns.md", 2000), ("cheatsheet.md", 1200)]:
        text = (root / name).read_text()
        body = text.split("---", 2)[2] if name == "SKILL.md" else text
        budgets[name] = estimate_tokens(body)
        require(budgets[name] <= limit, f"Token estimate exceeds target: {name}")
    checks["token_estimates"] = budgets
    checks["total_markdown_token_estimate"] = sum(estimate_tokens(p.read_text()) for p in md_files)

    text = (root / "references/figures-and-formulas.md").read_text()
    progress_rows, allocation_rows, cycle_rows, growth_samples = [], [], {}, {}
    for line in text.splitlines():
        cells = [x.strip() for x in line.split("|")[1:-1]]
        if len(cells) == 5 and re.fullmatch(r"\d+", cells[1]) and all(re.fullmatch(r"\d+(?:\.\d+)?", x) for x in cells[2:]):
            progress_rows.append(tuple(Decimal(x) for x in cells[1:]))
        if len(cells) == 5 and cells[0] in {"장비", "스킬", "각성"}:
            cycle_rows[cells[0]] = (int(cells[1]), int(cells[2]), int(cells[3]),
                                    [int(x) for x in cells[4].split("·")])
        if len(cells) == 7 and re.fullmatch(r"\d+", cells[0]):
            values = [Decimal(x) for x in cells[1:6]]
            require(sum(values[:4]) == values[4], "Growth sample sum mismatch")
            growth_samples[int(cells[0])] = values
        if len(cells) == 4 and cells[0] in {"무료", "시간 소모", "유료", "특수"}:
            allocation_rows.append((cells[0], Decimal(cells[1].rstrip("%")),
                                    Decimal(cells[2].replace(",", "")), Decimal(cells[3].rstrip("%"))))
    require(len(progress_rows) == 7, "Production table row count mismatch")
    days, levels = Decimal(0), Decimal(0)
    for duration, per_day, reached, cumulative_days in progress_rows:
        days += duration
        levels += duration * per_day
        require(days == cumulative_days and levels == reached, "Production cumulative arithmetic mismatch")
    require(days == 55 and levels == 100, "Production totals mismatch")
    require(len(allocation_rows) == 4, "Allocation row count mismatch")
    require(sum(x[1] for x in allocation_rows) == 100, "Ability shares do not sum to 100")
    require(sum(x[2] for x in allocation_rows) == 500000, "RMB allocation does not sum to 500000")
    require(sum(x[3] for x in allocation_rows) == 100, "Cost shares do not sum to 100")
    for _, _, amount, percent in allocation_rows:
        require(amount / Decimal(500000) * 100 == percent, "Cost percentage calculation mismatch")
    checks["table_arithmetic"] = {"days": str(days), "cumulative_level_gain": str(levels),
                                 "cost_rmb": "500000", "ability_and_cost_percent": "100"}
    require(set(cycle_rows) == {"장비", "스킬", "각성"}, "Growth start/period rows missing")
    for name, expected in [("장비", (0, 3, 3)), ("스킬", (1, 5, 6)), ("각성", (0, 10, 10))]:
        if name in cycle_rows:
            initial, period, first, events = cycle_rows[name]
            require((initial, period, first) == expected, f"Growth initial/period/start mismatch: {name}")
            require(events[0] == first and all(b - a == period for a, b in zip(events, events[1:])),
                    f"Growth event sequence mismatch: {name}")
    require(set(growth_samples) == {1, 3, 5, 6, 10, 11, 30}, "Growth sample levels mismatch")
    if {5, 6, 10, 11, 30}.issubset(growth_samples):
        require([growth_samples[n][2] for n in [5, 6, 10, 11, 30]] == [1, 8, 8, 15, 36],
                "Skill sample offset mismatch")
    checks["growth_periods"] = {name: {"initial": values[0], "period": values[1], "first_additional": values[2]}
                              for name, values in cycle_rows.items()}

    terms = []
    for name in ["glossary.md", "references/glossary-extended.md"]:
        terms.extend(re.findall(r"^\*\*(.+?)\*\* —", (root / name).read_text(), re.M))
    require(len(terms) == len(set(terms)), "Duplicate glossary terms")
    checks["glossary_terms"] = len(terms)
    pdf = source_pdf or (root / source["source_file"]).resolve()
    require(pdf.is_file(), "Source PDF unavailable for fingerprint check")
    if pdf.is_file():
        digest = hashlib.sha256(pdf.read_bytes()).hexdigest()
        require(digest == source["source_sha256"], "Source fingerprint mismatch")
        checks["source_sha256"] = "matched" if digest == source["source_sha256"] else "mismatch"
    return {"status": "PASS" if not errors else "FAIL", "scope": "whole skill bundle", "checks": checks, "errors": errors}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("skill", type=Path)
    parser.add_argument("--project-root", type=Path, default=Path(__file__).resolve().parents[4])
    parser.add_argument("--source-pdf", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = validate(args.skill, args.project_root, args.source_pdf)
    serialized = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(serialized)
    print(serialized)
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
