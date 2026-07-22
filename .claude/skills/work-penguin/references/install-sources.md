# install-sources — 권장 스킬 설치 출처 (seed 디렉터리)

> 안 깔린 스킬을 추천·설치할 때 **사용자가 링크를 안 줘도** 펭귄이 올바른 출처로 설치하게 하는 디렉터리.
> - 이미 깔린 스킬은 **동적 스캔**으로 인식 → 링크 불필요.
> - **do-better 워크스페이스 기본 스킬은 링크 불필요.** 조직이 do-better를 기본으로 깔고 가므로 *이미 있다고 전제*. (예: daily-note·todo·todos·idea·progress·wiki-ingest/lint·md-to-pdf·pdf-to-md·csv-clean·excel-to-csv·decompose/execute/integrate·save·setup-workspace·thinking-partner·notion-handler + worker 에이전트 등 35+) → 이 목록은 **do-better 이후 추가한 외부 스킬만** 다룬다.
> - 이 목록은 **seed**다. 여기 없는 스킬은 펭귄이 출처를 **검색(WebSearch)으로 확인** 후 제시하고, **확실치 않으면 링크를 지어내지 말고** "출처를 같이 찾아볼게요"라고 한다. (검증 원칙 → `verification.md`)
> - 출처는 시점에 따라 바뀔 수 있으니, 설치 직전 한 번 확인.

## 설치 방법 3종

| 유형 | 방법 |
|------|------|
| 스킬 repo | `.claude/skills/`에서 `git clone <repo>` |
| 플러그인 | `claude plugin marketplace add <owner/repo>` → `claude plugin install <플러그인명>@<마켓플레이스명>` (CLI에서 바로 실행 가능. 예: `claude plugin marketplace add mvanhorn/last30days-skill` → `claude plugin install last30days@last30days-skill`. 2026-07 실검증) |
| PyPI 패키지 | `pip install <pkg>` 또는 `uv tool install <pkg>` (대개 스킬이 자동) |

## 알려진 출처 (2026-06 기준)

| 스킬 | 유형 | 출처 |
|------|------|------|
| **pm-skills** (product-strategy·market-research·data-analytics·go-to-market·marketing-growth·execution) | 스킬 | `github.com/phuryn/pm-skills` |
| **frontend-design** | 스킬 (Anthropic 공식, Apache-2.0) | `github.com/anthropics/skills` |
| **ui-ux-pro-max** | 스킬 | `github.com/nextlevelbuilder/ui-ux-pro-max-skill` |
| **taste-skill** (brutalist·minimalist·soft·image-to-code·redesign 등) | 플러그인 | `github.com/Leonxlnx/taste-skill` |
| **graphify** | PyPI + 스킬 | `pip install graphifyy` / `github.com/safishamsi/graphify` |
| **watch** (영상) | 플러그인 | `github.com/bradautomates/claude-video` |
| **superpowers** | 플러그인 | `github.com/obra/superpowers` |
| **karpathy-guidelines** | 플러그인 | `github.com/forrestchang/andrej-karpathy-skills` |
| **agent-skills** | 스킬 (MIT) | `github.com/addyosmani/agent-skills` |
| **work-penguin** (본인) | 스킬 | `github.com/Penguin2646/work-penguin` |
| **last30days** (최근 30일 소셜·커뮤니티 트렌드 리서치) | 플러그인 | `github.com/mvanhorn/last30days-skill` (2026-07 설치 검증) |

## 설치 안내 흐름 (모든 스킬 공통)

1. **이미 깔림?** → 동적 스캔으로 확인. 깔려 있으면 링크 없이 바로 사용법 안내.
2. **안 깔림** → 위 표(또는 검색)로 **올바른 출처** 제시 + **설치 전 가치 안내**("이거 깔면 [이 작업]이 이렇게 좋아져요"). → `skill-recommend.md §3.5`
3. **설치 실행** → 사용자가 링크를 안 줘도 펭귄이 위 출처로 설치 진행(동의 후).
4. **설치 직후** → "이제 ~할 수 있어요" 변화 확인.
5. 출처를 모르면 → **검색으로 확인**, 그래도 불명확하면 솔직히 말하고 함께 찾기. **링크 환각 금지.**

## 실사용 중 발굴해 누적된 출처 (학습·확장 기록)

> 펭귄이 대화 중 직무에 맞춰 **검색으로 발굴해 검증한** 외부 도구. 쓸수록 이 목록이 자란다(= 누적 학습). 모두 실제 검색으로 확인된 출처.

| 직무/업무 | 도구 | 출처 |
|-----------|------|------|
| 엑셀 자동화 (커머셜 플래닝·데이터) | Excel MCP | `github.com/negokaz/excel-mcp-server` · `github.com/sbroenne/mcp-server-excel` · `github.com/ivan-loh/mcp-excel`(SQL) |
| 디자인 (Figma) | Figma MCP | 공식 `claude plugin install figma@claude-plugins-official` · `github.com/arinspunk/claude-talk-to-figma-mcp` |
| 재무·회계 | QuickBooks / Ledger MCP | `github.com/intuit/quickbooks-online-mcp-server`(공식) · `github.com/minhyeoky/mcp-server-ledger` |
| 영업·CRM | HubSpot MCP | 공식 `developers.hubspot.com/mcp` · `github.com/baryhuang/mcp-hubspot` |

_(이 표는 고정이 아니다 — 펭귄이 새 직무·새 도구를 만날 때마다 검증 후 여기에 한 줄씩 추가한다.)_

## 확장 — 목록 밖 스킬도 발굴 (중요)

펭귄은 이 seed나 "사용자가 이미 깐 것"에 **갇히지 않는다.** 대화 중 사용자의 **직무·업무에 더 맞는 스킬/에이전트**가 있으면(여기 없어도) **적극 발굴**한다:
- 마켓플레이스/WebSearch로 후보를 찾고, **출처를 검증해** 제시 + (동의 시) 설치
- "이런 게 있는데 OO님 업무엔 이게 더 맞을 것 같아요" 식으로 **현재 설치 범위 이상**을 제안
- 단 링크·효능은 검증 후 — 환각 금지

→ 이게 펭귄을 *닫힌 추천기*가 아니라 **계속 더 좋은 도구를 데려오는 동료**로 만든다. 확장 범위를 여는 게 이 스킬이 의미 있어지는 핵심.
