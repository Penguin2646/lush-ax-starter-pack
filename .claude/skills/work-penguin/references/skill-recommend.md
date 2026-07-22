# skill-recommend — 설치 스킬 동적 스캔 & 추천

> 원칙: **하드코딩 금지.** 추천 직전 항상 현재 설치된 스킬을 새로 읽는다. 도구가 늘수록 펭귄이 똑똑해진다.

## 1. 스캔 (매번)

1. 대화에 제공된 **available skills 목록**(시스템 컨텍스트)을 우선 사용.
2. 필요하면 `.claude/skills/` 디렉터리와 플러그인 스킬을 직접 확인.
3. 사용자가 *안 깐* 스킬은 추천하되 "이건 설치가 필요해요"라고 표시. (do-better 기본 스킬은 전제 → 링크 불필요)
4. **확장 (중요)**: 사용자의 직무·업무에 더 맞는 스킬/에이전트가 설치본·seed에 **없으면 목록 밖에서도 발굴**(WebSearch/마켓플레이스)해 추천·설치(출처 검증). 펭귄은 깔린 것에 갇히지 않는다. → `install-sources.md` 확장 섹션.

## 2. 업무 → 스킬 매핑 (가이드, 고정 아님)

| 업무 신호 | 추천 후보 (설치돼 있으면) | 한 줄 사용법 |
|-----------|--------------------------|--------------|
| 디자인/UI/자료 미관 (InDesign·Figma 포함) | frontend-design, ui-ux-pro-max, taste-skill(image-to-code) | "이 3개를 같이 쓰면 AI 티 안 나는 고퀄. frontend-design으로 톤→ui-ux-pro-max로 팔레트·폰트→taste-skill로 마감. **레퍼런스(이미지/링크)를 주면 image-to-code/taste-skill로 그 톤을 재현** — 레퍼런스 제공이 퀄리티의 핵심. Figma/InDesign 작업도 '이런 느낌' 레퍼런스를 코드/시안으로 빠르게 뽑아 출발점으로." |
| 보고서/문서화 | md-to-pdf, hwpxskill, content-worker | "초안은 content-worker, 배포본은 md-to-pdf로 A4 PDF." |
| 엑셀/데이터 정리 | excel-to-csv, csv-clean | "xlsx → CSV 변환 후 정리, 그 다음 분석." |
| 매출/판매 분석·예측 | sales-analysis, product-forecast | "예측 vs 실적은 product-forecast, 트렌드·수요는 sales-analysis." |
| 기획/PRD/전략 | pm-skills, dashboard-prd, webapp-prd, thinking-partner | "전략 프레임워크는 pm-skills, 화면 기획은 dashboard-prd." |
| 마케팅/그로스 | pm-skills(market-research·go-to-market·marketing-growth), last30days, research-worker, web-crawler-ocr, watch | "감으로 하던 마케팅을 **데이터 기반 리서치 루프**로. 시장·경쟁은 pm-skills market-research, 경쟁사 페이지는 web-crawler-ocr, 영상 트렌드는 watch, 깊은 조사는 research-worker로 3소스 교차검증. GTM·그로스 루프 설계까지." |
| 자료조사/리서치 | research-worker, web-crawler-ocr | "다중 소스 검증은 research-worker, URL 분석은 web-crawler-ocr." |
| 트렌드·소셜 반응 (최근 30일) | last30days, NaverSearch(MCP), research-worker | "글로벌 소셜 트렌드(Reddit·X·YouTube 등 15+ 소스, 실제 참여도 순위)는 last30days, 국내 검색·쇼핑 트렌드는 NaverSearch datalab — 둘을 합치면 국내+글로벌 트렌드 스냅샷. 깊은 검증은 research-worker." |
| 영상/녹취 | watch, transcript-organizer | "영상 분석은 watch, 긴 녹음 정리는 transcript-organizer." |
| 지식 정리/연결 | graphify, wiki-ingest | "폴더를 지식그래프로는 graphify, 위키 축적은 wiki-ingest." |
| 노션/외부 저장 | notion-handler, youtube-to-notion | — |
| 반복작업 분해·병렬 | decompose, execute, integrate | "큰 일은 decompose로 쪼개 execute로 병렬 실행." |

## 3. 추천 방식

- **묶어서** 추천 (단품 나열 X): "디자인이면 이 3개 조합이 좋아요."
- 각 추천에 **왜 + 어떻게 + 기대 효과** 한 줄씩.
- 사용자가 안 깐 도구면 설치 한 줄도 곁들임(부담 안 주게).
- 모르는 새 업무 유형이면 가장 가까운 카테고리로 유추 후 제안.

## 3.5 설치 권장·설치 시 안내 (필수)

스킬을 권하거나 설치할 때 **항상** 가치를 말로 안내한다 (graphify 포함 **모든 스킬**):
- **설치 전 (왜)**: "이거 깔면 **[지금 이 작업]이 이렇게 좋아져요**" — 쉬운 말 한 줄. 기능 나열이 아니라 *이 사람의 현재 작업이 어떻게 바뀌는지*.
- **설치 직후 (확인)**: "이제 ~할 수 있어요" 한 줄로 변화 확인.
- **부담 줄이기**: "설치는 처음 한 번, 자동이에요."
- **올바른 링크로 설치 (사용자가 링크 안 줘도)**: 안 깔린 스킬은 `install-sources.md`의 출처로 펭귄이 직접 설치한다. 목록에 없으면 WebSearch로 출처 확인, **불명확하면 링크를 지어내지 말 것.** (→ `install-sources.md`)
- **graphify 예시 문구**: "설치되면 그 폴더 문서들이 **연결 그래프 → graph.html 시각화**로 바뀌어요. 텍스트로만 보던 게 그림이 되니 구조가 한눈에 들어와요." (→ `graphify-diagnosis.md`)
- **다른 스킬 예시 문구**: PM 스킬 → "전략·리서치를 프레임워크로 구조화돼요." / 디자인 스킬 → "레퍼런스만 주면 그 톤으로 고퀄 시안이 나와요." — graphify만이 아니라 **추천하는 스킬마다** 그 작업이 어떻게 좋아지는지 말한다.

## 4. 자가 진화

추천이 잘 먹힌 조합은 스코어보드 "After(+도구)" 칸에 남는다. 다음에 비슷한 업무가 오면 그 기록을 근거로 더 정확히 추천한다.
