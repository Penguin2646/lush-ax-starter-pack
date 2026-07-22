# LUSH AX 스타터팩

> LUSH 임직원을 위한 Claude Code + Johnny Decimal 기반 **AI 워크스페이스 스타터팩**
> 비개발자도 clone 한 번으로 바로 시작할 수 있는 배포판입니다.

**핵심 특징:**
- 폴더 구조(Johnny Decimal) + 스킬 34종 + 에이전트 5종이 **미리 세팅된 상태**로 제공
- **Skills 기반** — 자연어로 호출 ("오늘 daily note 만들어줘" → 자동 실행)
- **Wiki 복리 시스템** — 지식이 쌓일수록 가치가 증가 (Karpathy LLM Wiki 아이디어)
- 개인 기록·데이터는 비어 있는 **깨끗한 초기 상태**

📊 **포함된 스킬·에이전트 전체 목록**: [docs/skills-catalog.pdf](docs/skills-catalog.pdf) 참조

---

# 설치 가이드

> 새 PC에 처음 세팅할 때 위에서부터 순서대로 따라 하면 됩니다. 소요 시간 약 15~20분.

## Step 0. 준비물

| 항목 | 설명 |
|------|------|
| Claude 계정 | [claude.ai](https://claude.ai) 가입 + **Pro 또는 Max 구독** (Claude Code 사용 조건) |
| GitHub 계정 | 아래 Step 1에서 가입 |
| 터미널 | Mac: 기본 `터미널` 앱 / Windows: `PowerShell` (기본 내장) |

## Step 1. GitHub 가입 & Git 설정

### 1-1. GitHub 가입

1. [github.com/signup](https://github.com/signup) 접속
2. 이메일 → 비밀번호 → 사용자 이름(영문) 입력 후 가입
3. 이메일 인증 완료

### 1-2. Git 설치

**Mac** — 터미널에서:
```bash
git --version
```
버전이 나오면 이미 설치된 것. 안 나오면 자동으로 설치 팝업이 뜹니다 (또는 `xcode-select --install`).

**Windows** — PowerShell에서:
```powershell
winget install --id Git.Git -e
```
또는 [git-scm.com/download/win](https://git-scm.com/download/win) 에서 설치 파일 다운로드 → 전부 기본값으로 Next.
설치 후 **PowerShell을 껐다 다시 켜야** `git` 명령이 인식됩니다.

### 1-3. Git 사용자 설정 (최초 1회)

Mac/Windows 공통:
```bash
git config --global user.name "내이름"
git config --global user.email "GitHub가입이메일@example.com"
```

확인:
```bash
git config --global user.name
git config --global user.email
```

## Step 2. Claude Code 설치

**Mac** — 터미널에서:
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows** — PowerShell에서:
```powershell
irm https://claude.ai/install.ps1 | iex
```

설치 확인 (터미널/PowerShell 재시작 후):
```bash
claude --version
```

> 💡 npm이 익숙하다면 `npm install -g @anthropic-ai/claude-code` 로도 설치할 수 있습니다 (Node.js 18+ 필요).

## Step 3. 워크스페이스 다운로드

### 방법 A — git clone (권장: 이후 업데이트 받기 쉬움)

원하는 위치(예: 바탕화면)에서:
```bash
git clone https://github.com/Penguin2646/lush-ax-starter-pack.git
cd lush-ax-starter-pack
```

### 방법 B — ZIP 다운로드 (git 없이)

1. 이 GitHub 페이지 상단의 **초록색 `<> Code` 버튼** 클릭
2. **Download ZIP** 클릭
3. 압축 해제 후 폴더를 원하는 위치로 이동

## Step 4. 첫 실행 & 초기 설정

워크스페이스 폴더 안에서 Claude Code 실행:
```bash
claude
```

- 최초 실행 시 브라우저가 열리며 **Claude 계정 로그인**을 요청합니다 → 로그인하면 끝
- 폴더 신뢰 여부를 물으면 **Yes** 선택

로그인이 끝나면 Claude에게 이렇게 말하세요:
```
워크스페이스 세팅해줘
```

`setup-workspace` 스킬이 대화형으로 진행합니다:
1. **프로필 작성** — CLAUDE.md의 "내 프로필"을 4개 질문으로 채움
2. **Python 환경** — 데이터 스킬(csv-clean, excel-to-csv 등)용 `.venv` 생성 (원할 때만)
3. **선택 도구 체크** — git, gws(Google Workspace CLI) 상태 확인
4. **첫 Daily Note** — 오늘의 기록 시작

## Step 5. (선택) 외부 플러그인 설치

superpowers, last30days 등 추가 플러그인 13종은 각자 PC에서 1회 설치가 필요합니다.
Claude Code 안에서 `/plugin` 명령으로 설치 — 명령어 전체 목록은
[00-system/03-guides/plugins-setup-guide.md](00-system/03-guides/plugins-setup-guide.md) 참조.

## Step 6. (선택) 내 GitHub 저장소로 백업 연결

작업 내용을 본인 GitHub에 백업하려면:

1. GitHub에서 **New repository** 클릭 → 이름 입력(예: `my-workspace`) → **Private** 선택 → Create
2. 터미널에서 워크스페이스 폴더로 이동 후:
```bash
git remote set-url origin https://github.com/내아이디/my-workspace.git
git push -u origin main
```
3. 이후에는 Claude에게 **"저장해줘"** 라고만 하면 `save` 스킬이 커밋+푸시를 알아서 합니다.

> ⚠️ 업무 내용을 담는 저장소는 반드시 **Private**으로 만드세요.

---

# 일상 루틴

```
오늘 daily note 만들어줘        # daily-note — 하루 기록 시작
할 일 추가해줘: 이메일 답장     # todo — 할 일 캡처
이 아이디어 기록해줘            # idea — 아이디어 저장
위키에 반영해줘                 # wiki-ingest — 지식 축적
저장해줘                        # save — GitHub 백업
이번 주 회고해줘                # weekly-synthesis — 주간 정리
```

# 폴더 구조 (Johnny Decimal)

```
00-inbox/      # 임시 캡처 (20개 미만 유지, 주간 처리)
00-system/     # 시스템 설정, 템플릿, 가이드
10-projects/   # 활성 프로젝트 (시한부)
20-operations/ # 지속적 운영 (종료일 없음)
30-knowledge/  # 지식 (00-wiki + 도메인 아카이브)
40-personal/   # 개인 노트 (daily, weekly, ideas, todos)
50-resources/  # 외부 자료, 첨부파일
90-archive/    # 완료/중단 항목
```

# 포함된 스킬 (34종) & 에이전트 (5종)

| 분류 | 스킬 |
|------|------|
| 📝 데일리·기록 | daily-note, daily-review, weekly-synthesis, idea, todo, todos, progress, save |
| 🧠 지식·위키 | wiki-ingest, wiki-lint, graphify(지식그래프) |
| 📄 문서 변환 | csv-clean, excel-to-csv, pdf-to-md, md-to-pdf, hwpxskill, transcript-organizer |
| 🎨 기획·제작 | dashboard-prd, webapp-prd, frontend-design, ui-ux-pro-max, thinking-partner, decompose, execute, integrate |
| 📈 세일즈·업무 자동화 | sales-analysis, product-forecast, product-sales-analysis, work-penguin(업무 동료 AI) |
| 🔗 외부 연동 | notion-handler, youtube-to-notion, web-crawler-ocr, doc-updater, setup-workspace |

추가로 쓰면 좋은 **외부 플러그인 13종**(superpowers, last30days, hyperframes, pm-skills 등)은
[00-system/03-guides/plugins-setup-guide.md](00-system/03-guides/plugins-setup-guide.md) 를 보고 각자 설치하세요.

| 에이전트 | 용도 |
|----------|------|
| research-worker | 다중 소스 웹 리서치 (3개 이상 교차검증) |
| analysis-worker | 데이터 분석·패턴 인식·전략 평가 |
| content-worker | 글쓰기·문서 생성·콘텐츠 구조화 |
| development-worker | 코드 작성·자동화·API 연동 |
| zettelkasten-linker | 노트 품질 분석·양방향 링크 제안 |

상세 설명은 [docs/skills-catalog.pdf](docs/skills-catalog.pdf) 참조.

---

# Credits

- 원본 템플릿: [Rhim80/do-better-workspace](https://github.com/Rhim80/do-better-workspace)
- 스타터 팩 구성: [@Penguin2646](https://github.com/Penguin2646)

**License**: 개인·팀 학습/업무용으로 자유롭게 사용하세요.
