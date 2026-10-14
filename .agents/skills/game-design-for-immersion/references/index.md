# 참조 자료 색인

이 색인은 질문에 맞는 자료를 고르기 위한 편집 구성이다. 원서의 새로운 장이나 저자의 별도 프레임워크가 아니다. 원서 **4장**, 주요 절 **18개**, 세부 목차 **79개**를 구분한다.

## 필요한 자료 선택

| 목적 | 읽을 자료 | 사용 방식 |
|---|---|---|
| 전체 관점과 요청 분류 | [SKILL.md](../SKILL.md) | 먼저 원서 장과 상세 절을 고른다. |
| 장별 학습과 큰 판단 | `../chapters/`의 ch01–ch04 | 관련 장의 관점·프레임워크·사례를 읽는다. |
| 특정 조건·기법·사례 | 아래 `sections/`의 s01–s18 | 상세 내용과 적용 한계를 확인한다. |
| 세부 절 번호·제목·쪽 범위 | [coverage.md](coverage.md) | 목차 항목을 상세 파일로 연결한다. |
| 수치·표·공식·단위 | [figures-and-formulas.md](figures-and-formulas.md) → 연결 상세 절 | 예시 조건과 검산·미확인 항목을 본다. |
| 개념 정의 | [용어집](../glossary.md) | s 번호에서 상세 절로 이동한다. |
| 작성 절차·대안 비교 | [실무 패턴](../patterns.md) | 원문 프레임워크와 새 적용안을 구분한다. |
| 초안 누락·빠른 판단 | [판단표](../cheatsheet.md) | 조건과 실패 신호를 확인한다. |
| 제작·검수 기록 | `../source.json`, `review-history.json`, `revalidation-2026-10-14.json` | 스킬을 유지보수할 때만 읽는다. 답변 자료로 쓰지 않고 현재 버전의 통과로 소급하지 않는다. |

일상 설계·학습은 지식 Markdown을 먼저 선택한다. 큰 검수 JSON은 책의 개념 설명을 대신하는 자료가 아니라 제작·유지보수 기록이다.

## 상세 절 색인

| 참조 | 원서 절·제목 | 본문 시작 | 파일 |
|---|---|---:|---|
| s01 | 1.1 뜨거운 자극형 게임 | 2 | [조작·난이도](sections/s01-hot-challenge.md) |
| s02 | 1.2 차가운 전략형 게임 | 47 | [전략·수치·균형](sections/s02-cold-strategy.md) |
| s03 | 2.1 칠정육욕 | 101 | [기쁨·분노·슬픔·공포·감동](sections/s03-emotion.md) |
| s04 | 2.2 심리 기법 | 119 | [판단·기억·설득·협력](sections/s04-psychology.md) |
| s05 | 2.3 사회 교류 활동 촉진 | 165 | [공통 경험](sections/s05-social-interaction.md) |
| s06 | 3.1 변화의 중요성 | 170 | [감정 경로·감각 순응](sections/s06-change.md) |
| s07 | 3.2 감정 곡선 | 174 | [곡선 선택·중단](sections/s07-emotion-curves.md) |
| s08 | 3.3 기조 | 181 | [네 기조·스테이지 곡선](sections/s08-tone-stage.md) |
| s09 | 3.4 콘텐츠 설계 | 194 | [기대감·메인 루프·엔딩](sections/s09-content-loop.md) |
| s10 | 3.5 게임 스토리라인 설계의 몇 가지 방식 | 214 | [선형·분기·열린 세계](sections/s10-story-structure.md) |
| s11 | 4.1 플레이어의 성장 | 225 | [성장 유형·진전감](sections/s11-growth.md) |
| s12 | 4.2 가치체계 구축 | 235 | [가치의 네 요소](sections/s12-value-system.md) |
| s13 | 4.3 보상 배치 | 241 | [초·중·후반 보상](sections/s13-reward-placement.md) |
| s14 | 4.4 사회 교류, 유통 방식과 플레이어 간의 행위 | 246 | [거래·귀속·호혜](sections/s14-trade-social.md) |
| s15 | 4.5 과금 유도 | 255 | [계층·진행 곡선](sections/s15-spending-tiers.md) |
| s16 | 4.6 유료 콘텐츠 | 260 | [부족함·욕망·결제 사례](sections/s16-paid-content.md) |
| s17 | 4.7 프로젝트의 과금 방향 | 273 | [서버 회전·녹색 게임](sections/s17-business-direction.md) |
| s18 | 4.8 과금 곡선 수치 설계 | 276 | [성장·소비·생산·배분](sections/s18-economy-curves.md) |

## 사례·질문으로 찾기

| 질문·검색어 | 먼저 읽기 | 확인할 내용 |
|---|---|---|
| 장애물이 안 보인다, 점프가 늦다, 거리·시간 판단 | [1장](../chapters/ch01-game-difficulty.md) → [s01](sections/s01-hot-challenge.md) | 발견·거리 인식·도달 예측·입력의 병목 |
| RLD, 통과율, 발판·낭떠러지, 랜덤 스테이지 | [s01](sections/s01-hot-challenge.md) | 변수 조합·테스트·선험적 설계의 한계 |
| 대균열, 쉬운 구간 건너뛰기, 능력 한계·회복 | [s01](sections/s01-hot-challenge.md) | 한계 접근 속도와 주변 난이도 변동 |
| QTE, 기억형 조작, 공격 방식, 쾌감·대비 | [s01](sections/s01-hot-challenge.md) | 실제 효율과 조작 경험의 차이 |
| 보스전 설계, 다단계 보스 재도전, 보스 앞 저장 지점 | [s01](sections/s01-hot-challenge.md) → [s07](sections/s07-emotion-curves.md)·[s08](sections/s08-tone-stage.md) → [s13](sections/s13-reward-placement.md) | 보스의 기능, 플레이어 대응에서 거꾸로 짜는 협동 보스의 스킬 시퀀스, 반복 구간 길이와 고조점 복귀, 위험 예감, 메인·서브 난관의 구분 |
| 비전투 전략·경영·생산·거래 루프 | [s02](sections/s02-cold-strategy.md) | 우위 확보·조합·실행 중 대응, 템포를 바꾸는 조건 |
| 덱·유닛·행동 순서, 스펙·확률·상성 | [s02](sections/s02-cold-strategy.md) | 전투 외·전·중의 전략, 효용·대가·대응 |
| 대미지·방어식, 원탁 이론, 생존 시간 | [수치 참조](figures-and-formulas.md) → [s02](sections/s02-cold-strategy.md) | 변수의 역할·수식 범위·원문 기호, 생존 턴 수 모델(식 (1.1)–(1.3)) |
| 몬스터 공격 횟수 n, 긴장 유지, 생존 능력 향상 폭 | [s02](sections/s02-cold-strategy.md#strategy-monster-n) | 작은 n을 유지하는 방법, 장르별 참고치(대략적 예시), n이 클 때의 보완 |
| 전투 스타일(방어 상한선·제어형), 능력치 배분 | [s02](sections/s02-cold-strategy.md#strategy-prebattle) | 전투 전 최적 조합의 요소 |
| 시퀀스 트리, 게임 이론, 강자 독점·제어 균형 | [s02](sections/s02-cold-strategy.md) | 다단계·상호 의존 선택과 역전 조건 |
| 기쁨·도움·관계 변화, 분노·배신·복수 | [2장](../chapters/ch02-player-emotion.md) → [s03](sections/s03-emotion.md) | 감정 대상·기대·행동 원인 |
| 슬픔·공포·감동을 플레이로 만들기 | [s03](sections/s03-emotion.md) | 상실·예고·애정·신념과 상호작용 |
| 누명·소유물 침탈·가치관 침해 | [s03](sections/s03-emotion.md) | 제3자·해명 수단·실제 상실·사전 공감의 조건 |
| 가용성 편향·착각적 사고·통제의 환상 | [용어 범위](glossary-extended.md#term-scope) → [s04](sections/s04-psychology.md) | 원문 용법·일반 정의·정상 통제감의 구분 |
| 군중심리·역할·인지부조화·과잉정당화 | [s04](sections/s04-psychology.md) | 저자의 조건·한계와 편집자 적용안 |
| 공감·보호 스킬·협력, 사회적 촉진·태만 | [s04](sections/s04-psychology.md) → [s05](sections/s05-social-interaction.md) | 개인 기여와 공동 경험의 연결 |
| 프레이밍·미끼·서열 위치 효과·피크엔드 법칙·앵커링·매몰 비용·완결감 | [s04](sections/s04-psychology.md) | 정보·기준점·완료 지점, 효과의 비보편성 |
| 뽑기·가챠 확률 연출, 뽑기로 기대감 만들기 | [s04](sections/s04-psychology.md#evaluation) → [s09](sections/s09-content-loop.md) → [s07](sections/s07-emotion-curves.md) | 결과 공개 전 대기, 바로 추첨하지 않고 기대를 유지하는 조건, 룰렛이 절정이 되기 어려운 이유 |
| 10연속 뽑기 보정, 10연뽑 과금, 천장·확률 공시 | [s04](sections/s04-psychology.md#persuasion-psych) → [s16](sections/s16-paid-content.md) | 10연속 보정의 방식과 전체 확률, 10연뽑을 낀 소비 한도 돌파·<음양사> 사례. 천장·확률 공시 의무는 자료 밖 지식으로 밝힌다 |
| LTV·게임 수명·장기 지속 | [s05](sections/s05-social-interaction.md) | 책의 ‘게임의 수명(LTV)’ 표기와 사회 교류 맥락. 재무 지표 정의·계산식과 구분 |
| 친구 기능·길드가 있어도 교류가 없다 | [s05](sections/s05-social-interaction.md) | 같은 목표와 서로의 상황을 바꾸는 기여 |
| 같은 자극이 지루하다, 2–3분 경험도 곡선이 필요한가 | [3장](../chapters/ch03-game-experience.md) → [s06](sections/s06-change.md) | 감각 순응·변화·시간 단위 |
| 기본형·할리우드형·파동형 중 선택 | [s07](sections/s07-emotion-curves.md) | 형태·목표·반복 변화·성취와 절정의 구분 |
| 죽음·저장점·중단·복귀·이탈 | [s07](sections/s07-emotion-curves.md) | 경험의 단절과 실제 접속 중단의 차이 |
| 가벼움/무거움, 느림/빠름, 30분 법칙 | [s08](sections/s08-tone-stage.md) | 난이도·템포의 두 축과 고정 시간의 한계 |
| 오리와 눈먼숲, 추격·위험 예고·스테이지 끝 | [s08](sections/s08-tone-stage.md) | 플레이어 조절과 고조·해소·반복 길이 |
| 기대·암시물·목표·메인 루프·엔딩 | [s09](sections/s09-content-loop.md) | 참여·변화·보상 예측·강한 끝 |
| 서브 퀘스트·멀티 엔딩·오픈 월드·샌드박스·MMORPG | [s10](sections/s10-story-structure.md) | 자유도와 감정 흐름, 세계 변화의 조건 |
| 3장 전체 요약, 스릴과 쾌감의 구분, 경험 설계의 적용 범위 | [3장](../chapters/ch03-game-experience.md) | 장 요약 절(본문 224쪽/PDF 240쪽) |
| 성장 시스템이 많지만 강해진 느낌이 없다 | [4장](../chapters/ch04-rewards-growth-monetization.md) → [s11](sections/s11-growth.md) | 숙련·기능·수치, 합계·차이·주기 |
| 희귀 아이템이 가치 없다, 수요·효용·인정 | [s12](sections/s12-value-system.md) | 가치 네 요소의 결합 |
| 보상·메인 난관·서브 난관·후발 추격 | [s13](sections/s13-reward-placement.md) | 진행 단계·난관·후반 보상 기준 |
| 입장권·고레벨과 저레벨의 협력 | [s14](sections/s14-trade-social.md) | 고레벨이 유용한 보상을 얻을 수 있고 서버가 전반적으로 고레벨일 때 저레벨 입장권이 희소해지는 조건 |
| 완전 유통·반 유통·귀속·거래 불가·호혜 | [s14](sections/s14-trade-social.md) | 공급·가격·역할과 상호 도움 |
| 소·중·고과금, 부족함·욕망, VIP·결제 사례 | [s15](sections/s15-spending-tiers.md) → [s16](sections/s16-paid-content.md) | 계층별 능력·진행과 역사적 사례 조건 |
| 서버 회전·자원 독점·녹색 게임 | [s17](sections/s17-business-direction.md) | 사업 방향·경쟁·유료 효용의 의미 |
| 표 4.10, 100레벨·55일, 생산량 | [수치 참조](figures-and-formulas.md) → [s18](sections/s18-economy-curves.md) | 하루당 상승량·누적 검산·시작 조건 |
| 표 4.11, 능력 비중과 비용 비중, RMB | [수치 참조](figures-and-formulas.md) → [s18](sections/s18-economy-curves.md) | 두 종류의 비중과 전체 배분 |

## 여러 장을 연결하는 작업

| 작업 | 읽는 순서 | 산출물 |
|---|---|---|
| 짧은 액션 스테이지 개선 | ch01/s01 → ch03/s07–s08 | 실패 변수와 감정 타임라인 |
| 협력 기능의 실제 관계 만들기 | ch02/s03–s05 → ch04/s14 | 도움·역할·상호 기여·유통 조건 |
| 성장 체감과 루프 개선 | ch04/s11–s13 → ch03/s09 | 해금·증가량·보상·다음 목표 |
| 자유로운 세계의 감정 흐름 | ch03/s07–s10 → 필요한 전략은 ch01/s02 | 이동·트리거·스토리·중단 구성 |
| 전투 전략과 성장의 균형 | ch01/s02 → ch04/s11·s15–s16 | 상성·기능 변화·계층별 진행 |
| 수익 모델이 정해진 게임의 경제 | ch04/s14–s18 → ch03/s09 | 수요·유통·상품·시간·공급의 연결 |

## 이전 참조 번호와 범위

초기 버전은 18개 주요 절을 `ch01`–`ch18`로 불렀다. 현재 이 자료는 **같은 순서의 `s01`–`s18`**이다. 현재 `ch01`–`ch04`는 실제 원서 장을 뜻한다. 과거 절 번호를 요청한 경우 이 대응을 안내하고 적합한 상세 절을 읽는다. `ch07` 같은 과거 번호를 실제 원서의 7장으로 만들지 않는다.

세부 목차의 탐색 범위는 [목차 대응](coverage.md)에서 찾고, 인용할 쪽은 장·상세 절 문장 끝의 위치를 쓴다. 색인만 읽고 원문 조건을 단정하거나 아직 읽지 않은 파일을 답변 근거로 제시하지 않는다. 여기의 게임 이름·표·시장은 원서 사례이며 현재 제품·요금·정책을 설명하는 자료가 아니다.
