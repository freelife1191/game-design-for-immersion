# 호스트별 사용

동일한 지식 스킬을 Codex·Claude Code·Antigravity에서 사용합니다. 설치 경로가 맞는 것, 앱이 발견한 것, 실제 요청을 수행한 것은 각각 다른 증거입니다.

| 호스트 | 프로젝트 경로 | 요청 예시 |
|---|---|---|
| Codex | `.agents/skills/game-design-for-immersion/` | `$game-design-for-immersion 원서 3장으로 감정 곡선을 검토해줘.` |
| Claude Code | `.claude/skills/game-design-for-immersion` | `/game-design-for-immersion 원서 3장으로 감정 곡선을 검토해줘.` |
| Antigravity | `.agents/skills/game-design-for-immersion/` | `game-design-for-immersion 스킬을 사용해 원서 3장으로 감정 곡선을 검토해줘.` |

Antigravity의 slash 호출은 설치 버전의 지원 여부를 확인합니다. 자연어로 스킬 이름과 목적을 명시하는 방식도 제공합니다. 스킬을 복사할 때는 `SKILL.md` 한 파일 대신 전체 폴더를 옮깁니다.

## 현재 연결과 이동

정본은 프로젝트의 `.agents/skills/game-design-for-immersion`입니다. 현재 개인 설치는 이 프로젝트를 가리키는 절대 링크, 프로젝트 Claude 별칭은 `../../.agents/skills/game-design-for-immersion` 상대 링크입니다. 원본 프로젝트를 이동하면 개인 링크의 대상도 확인합니다. 프로젝트 전체 이동 시 Claude 상대 링크는 같은 폴더 구조를 유지해야 합니다.

Codex 표시 메타데이터는 [openai.yaml](../.agents/skills/game-design-for-immersion/agents/openai.yaml)에 있습니다. 별도 역할 프로필 없이도 지식 스킬을 사용합니다.

## 인식 확인

1. 현재 열린 프로젝트와 `SKILL.md`의 `name`이 `game-design-for-immersion`인지 확인합니다.
2. 설치한 호스트의 스킬 목록 또는 새 세션에서 위의 짧은 요청을 실행합니다.
3. 답변이 요청에 맞게 선택한 자료를 실제 읽었는지 도구 로그에서 확인합니다.
4. 파일 연결 확인과 실제 호출 결과를 구분해 기록합니다.

제작 당시의 최종 호출 기록은 **Codex 1개**와 당시 버전의 검증 범위를 대상으로 합니다. Claude Code·Antigravity의 경로와 메타데이터 검사만으로 해당 호스트의 실제 실행을 통과했다고 판단하지 않습니다. CLI 시험은 GUI 메뉴에서의 발견까지 보증하지 않습니다.

## 공식 안내

공식 경로·호출 규칙의 확인 자료는 [Codex Skills](https://developers.openai.com/codex/skills/), [Claude Code Skills](https://code.claude.com/docs/en/skills), [Antigravity Skills](https://www.antigravity.google/docs/skills?tab=ide)입니다. 2026-10-14에 확인한 당시 공식 본문 기준으로 Codex·Claude Code의 심볼릭 링크 지원을 확인했으며, Antigravity의 링크 지원은 확인되지 않아 공통 원본 폴더를 직접 배치합니다. 버전별 지원이 다르면 설치된 버전의 도움말과 실제 발견·읽기 로그를 함께 확인합니다.
