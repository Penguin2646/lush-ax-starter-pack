# LUSH AX 스타터팩 — 워크스페이스 가이드

> Claude Code + Johnny Decimal 기반 PKM 워크스페이스.
> 이 파일은 Claude Code가 매 세션 시작 시 자동으로 읽는 프로젝트 지침입니다.
> 본인 프로필(이름, 역할, 관심사)은 이 파일 하단의 "내 프로필" 섹션을 직접 작성하거나 `/setup-workspace` 스킬로 채우세요.

## 폴더 구조 (Johnny Decimal)

```
00-inbox/      # 임시 캡처 (20개 미만 유지, 주간 처리)
00-system/     # 시스템 설정, 템플릿, 가이드
10-projects/   # 활성 프로젝트 (시한부)
20-operations/ # 지속적 운영 (종료일 없음)
30-knowledge/  # 지식 (00-wiki + 도메인 아카이브)
40-personal/   # 개인 노트 (daily, weekly, ideas, reflections, todos)
50-resources/  # 외부 자료, 첨부파일
90-archive/    # 완료/중단 항목
```

### 주요 하위 폴더

| 번호 | 폴더 | 용도 |
|------|------|------|
| **00-wiki** | 30-knowledge/ | **지식 위키 (복리 축적). 아래 Wiki Schema 참조** |
| 41-daily | 40-personal/ | Daily Notes (월별: 41-daily/YYYY-MM/) |
| 42-weekly | 40-personal/ | Weekly Review |
| 43-ideas | 40-personal/ | 아이디어 캡처 |
| 44-reflections | 40-personal/ | 회고 및 학습 |
| 46-todos | 40-personal/ | active-todos.md |
| 37-claude-code | 30-knowledge/ | Claude Code 관련 지식 |

## Wiki (30-knowledge/00-wiki/)

지식이 복리로 축적되는 위키. 주제에 대해 물으면 **00-wiki/index.md를 먼저 확인**.

@30-knowledge/00-wiki/SCHEMA.md

## 파일 명명 규칙

| 유형 | 형식 | 예시 |
|------|------|------|
| Daily Note | `YYYY-MM-DD.md` | 2026-04-24.md |
| 주제 노트 | `주제명.md` | thinking-partner.md |
| JD 폴더 | `XX-name` 또는 `XX.YY-name` | 37-claude-code, 37.01-learning |
| 중복 파일명 | JD prefix 필수 | 18-progress-tracker.md |

## Inbox 관리 (00-inbox)

- **목적**: 임시 캡처, 영구 저장소 아님
- **규칙**: 20개 미만 유지
- **주기**: 주간 처리 (Capture → Process → Organize)

## 첨부파일 (50-resources/attachments/)

- 모든 비텍스트 파일 저장
- 명명: `[관련노트]_[설명].[ext]`

## Skills 사용

이 워크스페이스의 `.claude/skills/`에 프로젝트 전용 스킬이 있습니다.
스킬은 키워드 기반으로 **자동 트리거**됩니다. (수동 슬래시 커맨드 아님)

예: "오늘 daily note 만들어줘" → `daily-note` 스킬 자동 실행
예: "할 일 추가해줘" → `todo` 스킬 자동 실행

## Agents 사용

`.claude/agents/`에 서브에이전트가 있습니다. 복잡한 작업을 Claude가 자동으로 위임하거나, 명시적으로 "research-worker로 조사해줘" 같이 호출할 수 있습니다.

## 외부 연동

연동한 외부 서비스가 있으면 아래 표에 기록하세요. (예: Google Workspace `gws` CLI, Notion MCP 등)

| 서비스 | 도구 | 계정 | 연동일 |
|--------|------|------|--------|
| (없음) | - | - | - |

---

## Superpowers 스킬 추천 규칙

작업 시작 전, 아래 상황에 해당하면 해당 스킬을 먼저 실행하거나 사용자에게 추천한다:

| 상황 | 스킬 |
|------|------|
| 새 기능/컴포넌트 구현 시작 | `superpowers:brainstorming` |
| 멀티스텝 구현 작업 (3단계 이상) | `superpowers:writing-plans` |
| 독립적인 작업 2개 이상 동시 진행 | `superpowers:dispatching-parallel-agents` |
| 버그/에러/예상치 못한 동작 발생 | `superpowers:systematic-debugging` |
| "완료"라고 말하기 직전 | `superpowers:verification-before-completion` |
| 브랜치 작업 완료 후 머지/PR 필요 | `superpowers:finishing-a-development-branch` |

---

## 코딩 원칙 (Karpathy Guidelines)

> 모든 코딩 작업에 자동 적용. 출처: [Andrej Karpathy](https://x.com/karpathy/status/2015883857489522876)

1. **코딩 전 생각** — 가정을 먼저 말하고, 해석이 여러 개면 제시하고 선택 유도. 불확실하면 묻기.
2. **단순함 우선** — 요청한 것만 구현. 추가 기능·추상화·에러핸들링 자체 추가 금지.
3. **외과적 변경** — 건드린 코드만 수정. 관련 없는 코드 "개선" 금지. 내가 만든 orphan만 정리.
4. **목표 기반 실행** — 성공 기준을 먼저 정의하고, 검증될 때까지 루프.

---

## 내 프로필

> 아래 항목을 직접 작성하거나, Claude에게 "워크스페이스 세팅해줘"라고 말해 `setup-workspace` 스킬로 채우세요.

**이름**: (작성해 주세요)
**역할**: (작성해 주세요 — 예: 마케팅 팀, 캠페인 기획·성과 분석)
**관심사**: (작성해 주세요)
**이 워크스페이스 용도**: (작성해 주세요)

_작성일: YYYY-MM-DD_

---

**Last Updated**: 2026-07-22 (스타터 팩 배포판)
