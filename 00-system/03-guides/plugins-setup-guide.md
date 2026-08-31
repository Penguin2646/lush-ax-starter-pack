# 외부 플러그인 설치 가이드 (선택)

> 스타터팩에 내장된 스킬 34종 외에, 추가로 쓰면 좋은 외부 플러그인 13종.
> 플러그인은 저장소에 담기지 않으므로 각자 PC에서 1회 설치해야 합니다.

## 시작 전 확인

- **전제**: README의 설치 단계(Claude Code 설치 + 로그인 1회 성공)까지 끝난 상태여야 합니다.
- **VS Code는 필요 없습니다.** 파워셸(Windows) 또는 터미널(Mac)만 있으면 됩니다.
- **코워크(Cowork) 채팅창에서는 플러그인 설치 명령이 동작하지 않습니다.** 설치는 아래 방법 A 또는 B로 한 번만 하면, 이후 코워크·Code 어디서든 자동으로 사용됩니다.

## 방법 A — 파워셸/터미널에서 바로 복붙 (추천 · 가장 쉬움)

터미널을 열고 (Windows: `Win + X` → "터미널" 또는 "Windows PowerShell" / Mac: `Cmd + Space` → "터미널") 아래 두 블록을 **순서대로 통째로 복사 → 붙여넣기 → Enter** 하면 끝입니다.

### 1단계 — 마켓플레이스 등록 (블록 전체 복붙)

```
claude plugin marketplace add anthropics/claude-plugins-official
claude plugin marketplace add forrestchang/andrej-karpathy-skills
claude plugin marketplace add bradautomates/claude-video
claude plugin marketplace add Leonxlnx/taste-skill
claude plugin marketplace add phuryn/pm-skills
claude plugin marketplace add mvanhorn/last30days-skill
```

### 2단계 — 플러그인 설치 (블록 전체 복붙)

```
claude plugin install superpowers@claude-plugins-official
claude plugin install skill-creator@claude-plugins-official
claude plugin install hyperframes@claude-plugins-official
claude plugin install andrej-karpathy-skills@karpathy-skills
claude plugin install watch@claude-video
claude plugin install taste-skill@taste-skill
claude plugin install pm-product-strategy@pm-skills
claude plugin install pm-market-research@pm-skills
claude plugin install pm-data-analytics@pm-skills
claude plugin install pm-go-to-market@pm-skills
claude plugin install pm-marketing-growth@pm-skills
claude plugin install pm-execution@pm-skills
claude plugin install last30days@last30days-skill
```

### 3단계 — 설치 확인

```
claude plugin list
```

13종이 목록에 보이면 완료입니다.

## 방법 B — Claude Code 대화 안에서 설치

터미널에서 `claude`를 먼저 실행해 대화에 들어간 뒤, 슬래시 명령을 **한 줄씩** 입력합니다. (여러 줄 한번에 붙여넣기는 방법 A가 더 안전합니다)

### 1단계 — 마켓플레이스 등록

```
/plugin marketplace add anthropics/claude-plugins-official
/plugin marketplace add forrestchang/andrej-karpathy-skills
/plugin marketplace add bradautomates/claude-video
/plugin marketplace add Leonxlnx/taste-skill
/plugin marketplace add phuryn/pm-skills
/plugin marketplace add mvanhorn/last30days-skill
```

### 2단계 — 플러그인 설치

```
/plugin install superpowers@claude-plugins-official
/plugin install skill-creator@claude-plugins-official
/plugin install hyperframes@claude-plugins-official
/plugin install andrej-karpathy-skills@karpathy-skills
/plugin install watch@claude-video
/plugin install taste-skill@taste-skill
/plugin install pm-product-strategy@pm-skills
/plugin install pm-market-research@pm-skills
/plugin install pm-data-analytics@pm-skills
/plugin install pm-go-to-market@pm-skills
/plugin install pm-marketing-growth@pm-skills
/plugin install pm-execution@pm-skills
/plugin install last30days@last30days-skill
```

## 플러그인별 용도

| 플러그인 | 용도 |
|----------|------|
| **superpowers** | 작업 규율 세트 — 브레인스토밍, 계획 작성, 체계적 디버깅, 완료 전 검증 등 |
| **skill-creator** | 나만의 스킬을 직접 만들 때 |
| **hyperframes** | 영상 제작 (모션그래픽, 슬라이드쇼, 제품 런칭 영상 등) |
| **andrej-karpathy-skills** | 코딩 시 흔한 LLM 실수 방지 가이드라인 |
| **watch** | 영상(URL/로컬) 시청·분석 — 다운로드, 프레임 추출, 자막 전사 |
| **taste-skill** | 고급 프론트엔드 디자인 (안티-슬롭, 프리미엄 UI) |
| **pm-* 6종** | PM 도구 세트 — 제품 전략, 시장 조사, 데이터 분석, GTM, 그로스, 실행 |
| **last30days** | 최근 30일 트렌드 리서치 (Reddit, HN, X, YouTube, Polymarket) |

## 참고

- `graphify` 스킬(지식그래프)은 팩에 내장되어 있지만, 별도 Python 도구 설치가 필요할 수 있습니다.
  스킬 폴더 내 설치 안내(`.claude/skills/graphify/`)를 참조하세요.
- 플러그인 목록·버전은 2026-07 기준입니다.
