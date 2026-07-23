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

> 처음이라도 괜찮습니다. 천천히 따라오세요.
> **자기 컴퓨터(Mac / Windows)에 해당하는 섹션만** 처음부터 끝까지 따라가면 됩니다. 소요 시간 약 20~30분.

## Step 0. 준비물

| 항목 | 설명 |
|------|------|
| Claude 계정 | [claude.ai](https://claude.ai) 가입 + **Pro 또는 Max 구독** (Claude Code 사용 조건) |
| GitHub 계정 | 아래 Step 1에서 가입 |
| 터미널 | Mac: 기본 `터미널` 앱 (Cmd + Space → "터미널") / Windows: `PowerShell` (Win + X → "Windows PowerShell" 또는 "터미널") |

## Step 1. GitHub 가입

1. [github.com/signup](https://github.com/signup) 접속
2. 이메일 → 비밀번호 → 사용자 이름(영문) 입력 후 가입
3. 이메일 인증 완료

---

## 🍎 Mac 설치

### 1단계: Xcode Command Line Tools 설치

Mac에서 개발 도구를 쓰려면 Apple의 기본 도구가 필요합니다.
설치 프로그램이 자동으로 뜨니까 걱정하지 마세요.

터미널을 열고 (Cmd + Space → "터미널" 입력 → Enter) 아래를 붙여넣으세요:

```bash
xcode-select --install
```

Enter를 누르면 설치 팝업 창이 뜹니다.

- **"설치" 버튼을 클릭**하세요
- 팝업이 안 보이면 Cmd + Tab으로 찾거나, Dock(화면 하단 바)을 확인하세요
- 설치 완료까지 **5~10분** 정도 걸립니다
- "이미 설치되어 있습니다" 메시지가 나오면 이 단계는 건너뛰세요

이건 한 번만 하면 됩니다. 나중에 다시 할 필요 없어요.

### 2단계: Node.js 설치

Claude Code를 실행하려면 Node.js가 필요합니다.

1. https://nodejs.org 에 접속
2. **"LTS" 버전** 클릭해서 다운로드
3. 다운로드된 파일(.pkg) 실행 → Continue 계속 클릭 → 완료

설치 확인 (터미널에서):

```bash
node --version
```

**v18 이상** 숫자가 나오면 성공!

### 3단계: Claude Code 설치

터미널에서 아래를 복사해서 붙여넣기:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Enter 누르면 설치가 시작됩니다. (1~2분 걸림)

### 4단계: 확인

```bash
claude
```

대화 화면이 뜨면 성공!

### Mac — 잘 안 될 때

**"claude를 찾을 수 없습니다"**

터미널을 껐다가 다시 여세요. 그래도 안 되면:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/."$(basename "$SHELL")rc" && source ~/."$(basename "$SHELL")rc"
```

**Xcode 설치 팝업이 안 뜸**

Dock(화면 하단 바)을 확인하세요. 설치 창이 뒤에 숨어있을 수 있습니다.
Cmd + Tab으로 "소프트웨어 업데이트" 또는 "Install" 창을 찾아보세요.

### Mac 설치 체크리스트

- [ ] Xcode Command Line Tools 설치함 (팝업에서 "설치" 클릭)
- [ ] Node.js 설치함 (nodejs.org에서 LTS 버전)
- [ ] Claude Code 설치함
- [ ] `claude` 실행해서 대화 화면 확인함

---

## 🪟 Windows 설치

### 1단계: Git for Windows 설치 (Claude Code보다 먼저!)

Claude Code는 내부적으로 이런 명령어를 씁니다:

```
ls    (파일 목록 보기)
cat   (파일 내용 보기)
grep  (텍스트 찾기)
```

이건 Mac/Linux 명령어인데, Windows는 원래 못 알아듣습니다.
Git for Windows를 설치하면 "Git Bash"라는 게 같이 깔리는데, 이게 통역사 역할을 해서 Windows도 이 명령어를 이해하게 됩니다.

1. https://git-scm.com/downloads/win 에 접속
2. **"64-bit Git for Windows Setup"** 클릭해서 다운로드
3. 다운로드된 파일 실행 → 그냥 "Next" 계속 누르면 됩니다 (기본값이 좋음)

### 2단계: Node.js 설치

Claude Code를 실행하려면 Node.js가 필요합니다.

1. https://nodejs.org 에 접속
2. **"LTS" 버전** 클릭해서 다운로드
3. 다운로드된 파일(.msi) 실행 → Next 계속 클릭 → 완료

설치 확인 (PowerShell에서):

```powershell
node --version
```

**v18 이상** 숫자가 나오면 성공!

### 3단계: Claude Code 설치

PowerShell을 열고 (Win + X → "Windows PowerShell" 또는 "터미널" 클릭) 아래를 붙여넣기:

```powershell
irm https://claude.ai/install.ps1 | iex
```

Enter 누르면 설치가 시작됩니다.

### 4단계: PowerShell 재시작 (중요!)

설치가 끝나면 **PowerShell을 완전히 닫고 새로 여세요.**
환경변수가 업데이트되려면 이게 꼭 필요합니다.

### 5단계: 확인

```powershell
claude
```

대화 화면이 뜨면 성공!

### Windows — 잘 안 될 때

**"claude를 찾을 수 없습니다"**

1. PowerShell을 껐다가 다시 여세요.
2. 그래도 안 되면 PATH 직접 추가:

```powershell
[Environment]::SetEnvironmentVariable("PATH", "$env:PATH;$env:USERPROFILE\.local\bin", "User")
```

3. PowerShell 다시 껐다가 열기
4. 이제 `claude` 입력

**Git for Windows 설치했는데 claude 안 됨**

1. Git for Windows 설치 완료 확인
2. PowerShell 새로 열기
3. 다시 Claude Code 설치 명령어 실행

### Windows 설치 체크리스트

- [ ] Git for Windows 설치함 (Claude Code보다 먼저!)
- [ ] Node.js 설치함 (nodejs.org에서 LTS 버전)
- [ ] Claude Code 설치함
- [ ] PowerShell 껐다가 다시 열었음 (중요!)
- [ ] `claude` 실행해서 대화 화면 확인함

---

## VS Code 설치 (Mac / Windows 공통, 권장)

Claude Code가 만든 코드를 눈으로 보고 수정할 수 있는 편집기입니다.
터미널 화면만 보는 것보다 훨씬 편해요. (코드에 색깔도 입혀주고, 에러도 알려줌)

1. https://code.visualstudio.com/ 에서 다운로드
2. 다운로드된 파일 실행 → Next 계속 → 완료 (Mac도 Windows도 똑같습니다)

---

## Step 2. Git 사용자 설정 (최초 1회)

Mac은 터미널, Windows는 PowerShell에서:

```bash
git config --global user.name "내이름"
git config --global user.email "GitHub가입이메일@example.com"
```

확인:

```bash
git config --global user.name
git config --global user.email
```

## Step 3. 스타터팩 다운로드

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

작업 내용을 본인 GitHub에 백업(push)하려면, 먼저 **내 GitHub 계정 인증**이 필요합니다.
GitHub CLI(`gh`)라는 도구가 로그인/인증을 대신 처리해 줘요. 이게 있어야 Claude Code가 여러분 계정 권한으로 pull/push를 실행할 수 있습니다.

### 6-1. GitHub CLI(gh) 설치

**Windows (PowerShell):**

```powershell
winget install --id GitHub.cli
```

> 💡 `winget`이 없다고 나오면: https://github.com/cli/cli/releases/latest 에서 `gh_..._windows_amd64.msi` 다운로드 → 실행 → Next 계속 클릭

**Mac:**

1. https://github.com/cli/cli/releases/latest 접속
2. `gh_..._macOS_universal.pkg` 다운로드 (Apple Silicon/Intel 구분 없이 이 파일 하나면 됩니다)
3. 다운로드된 파일 실행 → 계속 클릭 → 완료

> 💡 Homebrew를 이미 쓰고 있다면 `brew install gh` 한 줄로도 됩니다. (이 가이드에서는 Homebrew 설치를 요구하지 않으므로, 없다면 위 .pkg 방식을 쓰세요)

### 6-2. 터미널 껐다 켜고 설치 확인

방금 설치한 `gh`가 터미널에 인식되려면 재시작이 필요합니다. 터미널(PowerShell)을 완전히 닫고 새로 연 뒤:

```bash
gh --version
```

버전 숫자가 나오면 정상 설치! (안 나오면 PC 재부팅 후 다시 시도)

### 6-3. GitHub 로그인 인증

```bash
gh auth login
```

이 과정에서 내 GitHub 계정과 터미널이 실제로 연결됩니다. 화면에 질문이 순서대로 뜨는데, 이렇게 답하세요 (방향키 + Enter):

| 질문 | 선택 |
|------|------|
| Where do you use GitHub? | **GitHub.com** |
| What is your preferred protocol for Git operations on this host? | **HTTPS** |
| Authenticate Git with your GitHub credentials? | **Yes** (Y 입력) |
| How would you like to authenticate GitHub CLI? | **Login with a web browser** |

> 질문 문구는 gh 버전에 따라 조금 다를 수 있지만, 답 순서는 같습니다: **GitHub.com → HTTPS → Yes → 웹 브라우저 로그인**

마지막에 **일회용 코드**(예: `XXXX-XXXX`)가 뜹니다 → 그대로 Enter → 브라우저가 열리면 GitHub 로그인 후 그 코드를 입력하고 승인하면 끝!

확인:

```bash
gh auth status
```

`Logged in to github.com` 이 보이면 인증 성공입니다.

### 6-4. 내 저장소 만들고 연결

1. GitHub에서 **New repository** 클릭 → 이름 입력(예: `my-workspace`) → **Private** 선택 → Create
2. 터미널에서 워크스페이스 폴더로 이동 후, **다운로드 방법에 따라** 아래 중 하나 실행:

**Step 3에서 방법 A(git clone)로 받은 경우:**

```bash
git remote set-url origin https://github.com/내아이디/my-workspace.git
git push -u origin main
```

**Step 3에서 방법 B(ZIP)로 받은 경우** (폴더가 아직 git 저장소가 아니므로 먼저 만들어야 합니다):

```bash
git init -b main
git add .
git commit -m "start"
git remote add origin https://github.com/내아이디/my-workspace.git
git push -u origin main
```

> 💡 명령어가 부담스러우면 워크스페이스 폴더에서 `claude` 실행 후 이렇게 말해도 됩니다:
> "이 폴더를 https://github.com/내아이디/my-workspace 에 백업 연결하고 푸시해줘"

> ⚠️ 업무 내용을 담는 저장소는 반드시 **Private**으로 만드세요.

### 6-5. 이후에는 말로 시키면 됩니다

인증이 끝났으니, 워크스페이스 폴더에서 `claude`를 실행하고 자연어로 부탁하면 됩니다:

```
저장해줘                          # save 스킬 — 커밋 + 푸시 자동 처리
다른 PC에서 작업한 것 풀해줘       # git pull 실행
```

### GitHub 연동 — 잘 안 될 때

**push할 때 인증 오류가 남**
→ `gh auth status`로 로그인 상태 확인. `You are not logged in`이면 6-3부터 다시.

**`gh`를 찾을 수 없다고 나옴**
→ 터미널을 완전히 닫고 새로 열기. 그래도 안 되면 재부팅.

**Mac인데 git이 없다고 나옴**
→ Mac 설치 1단계(Xcode Command Line Tools)를 하면 git이 함께 설치됩니다. `git --version`으로 확인하세요.

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
