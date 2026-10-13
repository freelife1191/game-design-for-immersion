# README와 고급 활용 가이드 독립 문서 재검토 r2

검토일: 2026-10-14  
범위: `README.md`, `docs/advanced-usage.md`의 r2 현재본과 전 스냅샷·정준 스킬 참조 대조. 문서 계약과 정적 연결만 판정했다. 행동 시험, 호스트 호출, 게임 플레이테스트와 시장 검증은 수행하지 않았고 판정에 소급하지 않았다.

## 판정

**승인: 문서 검토 범위에서 차단·major·minor 없음.** 이전 검토의 조건 인계 결함과 한국어 조사 오류는 현재본에서 해소됐다. 이 승인은 실제 모델이 프롬프트를 따르거나 게임 효과가 성립함을 뜻하지 않는다.

## 실제로 읽은 자료

- 현재·전 스냅샷: `README.md`, `docs/advanced-usage.md`, `_workspace/documentation-review/2026-10-14/reference-depth-sync/before/README.md`, `_workspace/documentation-review/2026-10-14/reference-depth-sync/before/docs/advanced-usage.md`
- 작업 근거: `before-prompts.json`, `prompts.json`, `plan.json`, `change-plan-applied.json`, `condition-audit/review.json`, `condition-audit/review.md`, `candidate-manifest-r2.json`, 기존 reviewer 기록
- 정준 스킬·참조: `.agents/skills/game-design-for-immersion/SKILL.md`, `references/index.md`, `references/coverage.md`, `references/revalidation-2026-10-14.json`, `s01`, `s02`, `s03`, `s04`, `s07`, `s09`, `s10`, `s12`, `s14`, `s16` 상세 참조
- 선행 기록: `_workspace/skill-creator-review/2026-10-14/reference-depth/report.md`, `final-review/final-review.md`

## 이전 지적의 해소 확인

각 새 부모·후속 쌍에서 조건 계약이 끝까지 이어진다.

| 부모/후속 | 부모 산출물 | 후속 입력 | 후속 산출물 |
|---|---|---|---|
| `common-05` | 2082행: 성립·불성립·미확인·해당 없음 판정, 원서 쪽·입력·관측 근거, 다음 확인 자료 | 2106행: `이어받을 조건·예외` | 2110행: 판정의 유지·변경 여부와 근거 |
| `common-06` | 2136행 | 2160행 | 2164행 |
| `common-07` | 2190행 | 2214행 | 2218행 |
| `common-08` | 2244행 | 2268행 | 2272행 |

따라서 공통 안내의 “적용 조건·예외의 판정과 근거 위치를 함께 제공”이라는 요구(45·49행)와 새 대화용 후속 프롬프트가 일치한다. 부모가 특정 장르나 시스템을 강제하지 않는 제한, 후속이 미정 정책을 결정하지 않는 제한도 유지한다.

## 정적 검증

- `candidate-manifest-r2.json`의 SHA-256과 현재 파일이 일치했다. `README.md`: `41a9f7ae…`, `docs/advanced-usage.md`: `10d82bda…`.
- 기존 61개 요청 ID가 모두 남고, 현재 ID는 69개이며 중복이 없다. 추가 ID는 `common-05`~`common-08` 및 각각의 후속뿐이다.
- 기존 85개 명시 앵커가 모두 남고, 현재 고급 가이드의 앵커는 94개이며 중복이 없다. README·고급 가이드에서 참조한 내부 앵커와 상대 파일 링크의 미해결 건은 0건이다.
- 후속 요청 22개의 parent가 모두 실제 부모 ID와 일치한다.
- 전 스냅샷의 가상 입력·확정·미정 필드 82개가 현재 문서에 모두 남았다. 새 12분·15분·2주·2분은 가상 입력으로 한정되고, 20분·0.1%·RMB/VIP는 원서 사례를 현재 기본값으로 만들지 않도록 제한한다.
- 조건 감사의 19개 세부 절은 기존 보강 11건, 새 공통 예시 7건, 기존 충분 1건으로 모두 처분되어 있다. selective 읽기, 책/일반 심리 용어 경계, 동적 재개의 조절 가능 상태, 표지 개수 비강제, 영구 보상 반례, 시스템 재유통, 호혜의 양쪽 필요, 가격·효과 축 및 소비 집단 조건도 각 요청·산출물·확인 문장에 남아 있다.
- 새 문구에서 이전 조사 오류(`조건를`, `관측를`, `목록를`, `질문를`)는 발견되지 않았다.

## 행동 시험과 별도인 한계

`trials/noncombat`, `trials/reentry`, `trials/reciprocity`의 기존 결과는 수정 전 문구로 실행된 기록이므로 이 r2 문서 판정의 근거로 쓰지 않았다. 이후 실제 행동 시험에서는 네 새 부모·후속 쌍을 새 대화로 복사해 조건 판정·근거·미확인 자료가 실제로 보존되는지만 별도로 확인하면 된다.
