# 릴리스 노트

이 디렉터리는 GitHub Release에 넣을 **검토 가능한 노트 원본**을 보관합니다. 파일을 추가하거나 커밋하는 일만으로 공개 릴리스가 만들어지지는 않습니다.

## 파일 규칙

| 항목 | 규칙 | 예시 |
|---|---|---|
| 파일명 | `yyyy-mm-dd-title.md` | `2026-10-15-documentation-and-release-guide.md` |
| 날짜 | KST 작성일 | `2026-10-15` |
| 제목 | 소문자 kebab-case | `documentation-and-release-guide` |
| 버전 | 날짜와 별도로 관리 | 태그가 필요할 때만 지정 |

새 노트는 [_template.md](_template.md)를 복사해 작성합니다. 독자가 알아야 할 변경, 영향, 검증 범위와 한계를 적고 내부 작업 로그나 검증하지 않은 실행 결과는 넣지 않습니다.

## GitHub Release 만들기 <a id="github-release"></a>

1. 릴리스할 커밋의 전체 SHA를 확인하고, 태그와 제목을 정합니다.
2. 해당 노트의 내용과 대상 커밋을 검토합니다.
3. 아래 명령의 대문자 자리를 실제 값으로 바꿔 **초안**을 만듭니다.

```bash
gh release create TAG \
  --repo freelife1191/game-design-for-immersion \
  --target FULL_COMMIT_SHA \
  --title "TITLE" \
  --notes-file release/FILE \
  --draft
```

> [!IMPORTANT]
> `TAG`, `FULL_COMMIT_SHA`, `TITLE`, `FILE`은 모두 실제 릴리스 값으로 바꿉니다. 날짜 기반 파일명은 버전이나 태그를 대신하지 않습니다.

`--target`은 아직 없는 태그를 만들 때 그 태그가 가리킬 전체 커밋 SHA입니다. 이미 만든 태그를 대상으로 할 때는 태그가 의도한 커밋을 가리키는지 먼저 확인하고 `--verify-tag`을 사용하며, `--target`을 함께 쓰지 않습니다.

## 초안 검토와 공개

GitHub에서 초안의 제목·노트·대상 커밋을 검토한 뒤, 공개할 때만 다음을 실행합니다.

```bash
gh release edit TAG \
  --repo freelife1191/game-design-for-immersion \
  --draft=false
```

자세한 옵션은 GitHub CLI 공식 문서인 [`gh release create`](https://cli.github.com/manual/gh_release_create), [`gh release edit`](https://cli.github.com/manual/gh_release_edit)를 따릅니다.

## 현재 노트

- [2026-10-15 — 문서·릴리스 가이드](2026-10-15-documentation-and-release-guide.md)

## 기존 Release 본문에 적용하기

기존 릴리스의 태그·대상 커밋·공개 상태와 현재 본문을 확인한 뒤 적용합니다. 다음 명령은 본문 전체를 교체하므로 보존할 내용을 먼저 노트에 반영합니다.

```bash
gh release edit TAG \
  --repo freelife1191/game-design-for-immersion \
  --notes-file release/FILE
```

> [!TIP]
> GitHub Release에 붙일 노트의 문서 링크는 전체 GitHub URL로 작성합니다. 특정 배포본에 고정하려면 태그나 커밋 URL을 사용하세요. 노트와 배포 파일에 원문·PDF·인증 파일·로컬 작업 로그를 포함하지 않습니다.

[← 프로젝트 소개](../README.md) · [문서 지도](../docs/index.md) · [노트 템플릿](_template.md) · [GitHub Releases](https://github.com/freelife1191/game-design-for-immersion/releases)
