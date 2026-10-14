# 몰입을 설계하는 게임 기획 스킬

쉬웨이훙의 『몰입을 설계하는 게임 기획』 제2판을 바탕으로 **난이도·전략·감정·경험·성장·경제**를 학습하고 설계·검토하는 지식 스킬입니다. 실제 호출 이름은 **`game-design-for-immersion`**입니다.

플레이어에게 남길 경험을 정하고, 그 경험을 만드는 행동과 규칙을 검토합니다. 기본 활용에는 원문 PDF나 변환 도구가 필요하지 않습니다.

---

## 설치 <a id="installation"></a>

현재 프로젝트에는 설치되어 있습니다. 다른 프로젝트에 사용할 때는 **지식 스킬 폴더 전체**를 복사합니다. 개인 설치 `/Users/freelife/.agents/skills/game-design-for-immersion`과 이 프로젝트의 Claude Code 별칭은 현재 프로젝트 원본을 가리킵니다.

### 프롬프트로 설치

아래는 에이전트 대화창에 입력할 요청입니다. 원본·대상 경로는 실제 경로로 바꿉니다.

```text
/absolute/source-project/.agents/skills/game-design-for-immersion 폴더 전체를
/absolute/target-project/.agents/skills/game-design-for-immersion에 설치해줘.
Claude Code용 .claude/skills/game-design-for-immersion 상대 링크도 만들어줘.
기존 대상이나 별칭이 있으면 보존하고 차이를 알려줘.
```

### CLI로 설치

대상 프로젝트 루트에서 실행합니다. `SKILL_SOURCE`는 복사할 원본의 절대 경로입니다. 기존 파일·끊어진 링크도 덮어쓰지 않습니다.

```bash
SKILL_SOURCE='/absolute/source-project/.agents/skills/game-design-for-immersion'
SKILL_TARGET="$PWD/.agents/skills/game-design-for-immersion"
CLAUDE_TARGET="$PWD/.claude/skills/game-design-for-immersion"

test -f "$SKILL_SOURCE/SKILL.md" || { printf '%s\n' '스킬 원본을 찾을 수 없습니다.' >&2; exit 1; }
if [ -e "$SKILL_TARGET" ] || [ -L "$SKILL_TARGET" ] || [ -e "$CLAUDE_TARGET" ] || [ -L "$CLAUDE_TARGET" ]; then
  printf '%s\n' '기존 스킬 또는 별칭을 보존합니다.' >&2
  exit 1
fi
mkdir -p "$(dirname "$SKILL_TARGET")" "$(dirname "$CLAUDE_TARGET")"
cp -R "$SKILL_SOURCE" "$SKILL_TARGET"
ln -s '../../.agents/skills/game-design-for-immersion' "$CLAUDE_TARGET"
```

새 설치는 새 세션에서 확인합니다. Codex·Antigravity는 `.agents/skills/`, Claude Code는 `.claude/skills/`에서 연결된 같은 지식 자료를 읽습니다. [호스트별 안내](docs/agents.md)를 참고합니다.

## 시작하기 <a id="quick-start"></a>

Codex에서 아래 요청을 입력합니다. 시간·정책은 **연습용 가상 입력**입니다.

```text
$game-design-for-immersion 원서 3장으로 3분 액션 스테이지의 감정 곡선을 설계해줘.
대상: 처음 플레이하는 사람. 목표: 위험을 이해하고 마지막 돌파에 성취감을 느끼기.
확정: 전투력 판매 없음. 미정: 실패 뒤 재시도 위치와 회복 구간 길이.
관련 장과 상세 절을 읽고 곡선 선택 이유, 구간별 행동·기조·피드백을 작성해줘.
책의 설명과 새 적용안을 구분하고 미정 정책은 선택지와 영향으로 남겨줘.
```

기대 결과는 곡선 선택 근거, 구간별 경험표, 재시도 대안, 플레이테스트 항목입니다. 실제 플레이 결과는 게임에서 별도로 확인합니다.

---

## 목차 <a id="toc"></a>

- [설치](#installation)
- [시작하기](#quick-start)
- [간단 사용과 요청문](#usage)
- [보강된 조건을 내 기획에 적용하기](#refined-usage)
- [스킬 구성과 전체 4장](#structure)
- [상세 가이드](#guides)
- [출처와 검증 범위](#evidence)

## 간단 사용과 요청문 <a id="usage"></a>

| 목적 | 대화창 요청 예시 | 기대 결과 |
|---|---|---|
| 개념 학습 | `$game-design-for-immersion RLD와 난이도 곡선의 차이를 설명하고 이해 확인 문제를 내줘.` | 정의·조건·예시·이해 확인 |
| 자료 선택 | `$game-design-for-immersion 친구 기능은 있지만 교류가 없는 문제에 필요한 장과 절을 골라줘.` | 읽을 자료·선택 이유·검토 기준 |
| 경험 설계 | `$game-design-for-immersion 2분 퍼즐의 긴장과 회복을 설계해줘. 힌트 정책은 미정이야.` | 곡선·행동·실패/복귀 대안 |
| 전략 검토 | `$game-design-for-immersion 공격·방어·회복 중 공격만 선택되는 메모를 검토해줘.` | 효용·대가·대응·반례 |
| 성장 검토 | `$game-design-for-immersion 원서 4.1절로 성장선의 합계·증가량·해금 주기를 검토해줘.` | 성장 구분·표·체감 가설 |
| 경제 비교 | `$game-design-for-immersion 외형만 유료인 게임의 유통 세 안을 같은 기준으로 비교해줘.` | 확정 정책 유지·효용·교류·운영 영향 |
| 수치 조회 | `$game-design-for-immersion 표 4.1의 초기값·반복 주기·첫 추가 상승을 나눠 설명해줘.` | 원문 값·단위·계산·한계 |
| 문서 검토 | `$game-design-for-immersion "./기획서.md"를 문제→영향→최소 수정안으로 검토해줘. 파일은 수정하지 마.` | 문장 근거·관련 절·확인할 정책 |

> [!NOTE]
> 예시는 Codex 형식(`$game-design-for-immersion`)입니다. Claude Code에서는 `/game-design-for-immersion`으로 바꾸거나 `game-design-for-immersion 스킬을 사용해서 …`처럼 요청합니다. 다른 호스트는 [호스트별 사용](docs/agents.md)을 봅니다.

### 내 상황에 맞게 요청하기

```text
$game-design-for-immersion [기능/문서/경험]을 [학습/설계/비교/검토]해줘.
맥락: [장르·대상·세션 길이·현재 문제·관측 자료]
확정: [유지할 정책] / 미정: [결정하지 않은 정책]
산출물: [개념표/경험 타임라인/성장표/대안 비교/검토표]
관련 자료를 읽고 책의 근거·사례 재구성·새 제안을 구분해줘.
미정 사항은 선택지·영향·검증할 질문으로 남겨줘.
```

같은 대화에서는 “방금 결과의 재시도 부분만 보완해줘”로 이어갑니다. 새 대화에는 이전 답변이나 문서를 함께 제공합니다. 고급 활용에는 **상세 18절별 예시 36개·후속 요청 18개·공통 예시 8개·공통 후속 요청 4개·연계 시나리오 3개**가 있습니다.

## 보강된 조건을 내 기획에 적용하기 <a id="refined-usage"></a>

스킬은 특정 기법·사례를 상세 절에서 먼저 확인하고, 큰 설계 관점이 더 필요할 때 장 자료로 확장합니다. [참조 색인](.agents/skills/game-design-for-immersion/references/index.md)과 전략·심리 참조의 절별 바로가기를 이용합니다. 후속에는 선택한 결과뿐 아니라 **적용 조건·예외의 판정, 확인 근거, 미확인 항목**도 넘깁니다.

| 내 문제 | 확인할 조건·예외 | 바로 사용할 요청 |
|---|---|---|
| 전투 없는 경영 게임의 선택이 단조롭다 | 우위 확보·조합·실행 중 대응, 단기 미션의 템포 비용 | [경영 예시와 후속](docs/advanced-usage.md#common-05) |
| 심리 효과 이름만으로 기획을 설명하고 있다 | 책/일반 용어의 차이, 누명·요청 순서의 성립 조건 | [심리 조건 학습과 후속](docs/advanced-usage.md#common-06) |
| 고정 퀘스트에서 장기 복귀를 개선한다 | 경험 유형과 중단 시간, 실제 조절 가능한 상태, 새 시스템이 필요한 범위, 하나의 복귀 표지 | [복귀 예시와 후속](docs/advanced-usage.md#common-07) |
| 목표 없는 짧은 경험에 시연을 넣을지 고민한다 | 빠른 템포는 목표 부재를 상쇄하는 유일한 방법이지만 목표가 있을 때 집중이 더 쉬움, 시연 생략은 기획자의 확신과 즉시 충분한 플레이가 함께 있을 때 | [자유 조작 예시와 후속](docs/advanced-usage.md#common-08) |
| 느린 획득 경로를 삭제하거나 유통·상품을 바꾼다 | 영구·대체 불가 보상, 시스템 재유통, 상호 필요, 진행·가격의 다른 축 | [조건별 활용 표](docs/advanced-usage.md#refined-conditions) |
| 성장 곡선이 겹치거나 해금 간격이 일정하지 않다 | 책의 ‘성장 곡선’은 수치 성장만 가리킴, 새 능력·챕터 해금(큰 파동)과 수치 상승(작은 파동), 능력 성장·수치 성장 비중형의 차이, 시작 레벨 차이와 의도적 겹침 | [A. 6개 성장 경로의 체감을 실력·해금·증가량으로 진단하기](docs/advanced-usage.md#s11-a)<br>[B. 표 4.1의 초기값·주기·첫 상승을 따로 검산하기](docs/advanced-usage.md#s11-b) |
| 외형 상품을 설계하며 책의 과시용 장비 사례를 참고한다 | 책은 과시용 장비에 일정 수준의 수치 능력을 권하고, 채택하지 않으면 일부 수익을 포기하는 대신 긍정적 평가를 얻는다고 씀, 외형만 유료와의 충돌, 한정성·획득 루트 설계 | [A. 재료 부족과 외형 욕망의 상품 동기·정책 충돌 구분하기](docs/advanced-usage.md#s16-a) |
| 서버 회전이나 녹색 게임 같은 사업 방향을 비교한다 | AFK·서버 통합은 자원 독점형의 서술, 녹색은 PVE 자원 획득과 추가 유료 아이템 가격 상향, 외형 가격은 미정 | [A. 서버 회전 두 유형과 녹색 게임의 사업 조건 비교하기](docs/advanced-usage.md#s17-a)<br>[B. 외형 유료 모델과 녹색 게임의 공통점·차이 검토하기](docs/advanced-usage.md#s17-b) |

**정책의 적용 범위도 구분합니다.** ‘외형만 유료’는 성능·진행 우위 판매를 배제하는 조건입니다. 아직 미정인 외형 가격·전시 등급·외형 전용 할인까지 자동 금지하는 뜻으로 넓히지 않습니다. 책의 소비 집단·VIP·가격 사례는 현재 정책의 정답이 아니라 비교할 조건입니다.

## 스킬 구성과 전체 4장 <a id="structure"></a>

**관련 자료 선택 → 실제 내용 읽기 → 근거와 프로젝트 조건 구분 → 학습·설계·검토 → 반례 확인** 순으로 활용합니다. 이 순서는 이 가이드의 활용 흐름입니다.

```text
.agents/skills/game-design-for-immersion/
├── SKILL.md                   # 사용 원칙·요청 분류·원서 장 색인
├── agents/openai.yaml         # Codex 표시·호출 메타데이터
├── chapters/                  # 실제 원서 4장
├── references/
│   ├── index.md               # 질문·사례·연계 작업으로 자료 선택
│   ├── coverage.md            # 18절·79개 세부 목차와 원문 위치
│   ├── figures-and-formulas.md # 표·수식·단위·검산
│   ├── glossary-extended.md   # 확장 용어
│   ├── review-history.json    # 기존 원문 재대조 기록
│   ├── revalidation-2026-10-14.json # 2026-10-14 재검수 기록
│   └── sections/              # 상세 18절
├── glossary.md                # 핵심 용어
├── patterns.md                # 실무 적용 절차
├── cheatsheet.md              # 빠른 판단표
└── source.json                # 서지·원문 식별·목차·검수 범위
```

| 장 | 원서 제목 | 본문 / PDF | 주요 활용 |
|---|---|---|---|
| [01](.agents/skills/game-design-for-immersion/chapters/ch01-game-difficulty.md) | 게임 난이도 설계 | 1–98 / 17–114 | 조작 병목·전략 선택·밸런스 |
| [02](.agents/skills/game-design-for-immersion/chapters/ch02-player-emotion.md) | 플레이어 감정 설계 | 99–168 / 115–184 | 감정 원인·심리 기법·공통 경험 |
| [03](.agents/skills/game-design-for-immersion/chapters/ch03-game-experience.md) | 게임 경험 설계 | 169–224 / 185–240 | 변화·곡선·기조·루프·스토리 |
| [04](.agents/skills/game-design-for-immersion/chapters/ch04-rewards-growth-monetization.md) | 보상, 성장, 과금 설계 | 225–284 / 241–300 | 성장·가치·보상·유통·과금 |

> [!IMPORTANT]
> **원서 장 `ch01`–`ch04`와 상세 참조 `s01`–`s18`을 구분합니다.** 초기 버전의 `ch07`은 현재 `s07`(감정 곡선)입니다. 현재 원서 3장은 게임 경험 설계입니다.

장 전체의 관점은 `chapters/`, 특정 조건과 사례는 `references/sections/`에서 읽습니다. [참조 색인](.agents/skills/game-design-for-immersion/references/index.md)은 파일 선택용이며, 그 표만 읽고 상세 조건을 단정하지 않습니다. [전체 목차 대응](.agents/skills/game-design-for-immersion/references/coverage.md)과 [고급 활용](docs/advanced-usage.md)에서 18절을 찾아봅니다.

## 상세 가이드 <a id="guides"></a>

| 필요한 내용 | 문서 |
|---|---|
| 읽는 순서·자료 선택 | [가이드 홈](docs/index.md) |
| 첫 요청·입력·결과 확인 | [시작하기](docs/getting-started.md) |
| Codex·Claude Code·Antigravity | [호스트별 사용](docs/agents.md) |
| 학습·설계·검토·반복 보완 | [작업 흐름](docs/workflow.md) |
| 4장 전략·18절 예시·연계 시나리오 | [고급 활용](docs/advanced-usage.md) |
| 근거·수치·답변·실제 호출 검사 | [검수와 테스트](docs/validation.md) |
| 인식·경로·누락·OCR·수치 문제 | [문제 해결](docs/troubleshooting.md) |

## 출처와 검증 범위 <a id="evidence"></a>

참고 도서: 쉬웨이훙, 권유라 옮김, 『몰입을 설계하는 게임 기획』 제2판, 제이펍(2026). 제공된 한국어판 PDF는 308쪽입니다. 서지와 원본 해시는 [source.json](.agents/skills/game-design-for-immersion/source.json)에 있습니다.

책의 설명, 책 사례의 압축 재구성, 프로젝트를 위한 새 적용안을 구분합니다. **PDF 쪽 = 인쇄 본문 쪽 + 16**이며 앞부분 로마숫자 쪽에는 적용하지 않습니다. 예시 비율·가격·일수는 서비스 기본값이 아닙니다.

2026-10-13의 [구조·내용 검토](output/skill-review/2026-10-13/structure-review/report.md)는 보존했습니다. 제작 당시의 입력·원문 대조·독립 시험·호스트 결과는 로컬 검수 기록으로 보존하며 기본 설치에 포함하지 않습니다. 증거 종류와 완료 판정 방법은 [검수 가이드](docs/validation.md#evidence-levels)에 있습니다.

2026-10-14에는 원문·문서·한국어를 다시 검수해 근거 없는 시간 기준과 귀속·용어 혼용을 보정했습니다. 이후 [skill-creator 심층 검토](_workspace/skill-creator-review/2026-10-14/reference-depth/report.md)에서 19개 세부 절의 조건·예외를 보강하고 자료 선택·정책 해석을 다듬었습니다. 이번 README와 고급 가이드 반영 내용은 [문서 검토 기록](_workspace/documentation-review/2026-10-14/reference-depth-sync/report.md)에 따로 남깁니다. [최근 재검수와 한국어 검수](docs/validation.md#latest-review)에서 범위와 보완 내용을 확인할 수 있습니다.

> [!NOTE]
> 이 자료는 학습·적용을 위해 합성한 지식이며 원문 전체·긴 인용·원본 도판의 복제본이 아닙니다. 일부 OCR 수식·VIP 표의 한계는 출처 기록과 상세 자료에서 확인합니다. 원문이나 전체 추출 텍스트는 공유할 스킬에 포함하지 않습니다.

스킬은 원문 없이 포함된 자료만으로 답하고, 원문 확인이 필요한 곳은 쪽을 안내합니다. 원문 PDF와 직접 대조하는 방법은 [문제 해결](docs/troubleshooting.md#source-check)에 있습니다. 심리 연구의 외부 재현성, 현재 시장·가격·정책, 실제 게임 성과는 이 책 기반 검수만으로 확인되지 않습니다.
