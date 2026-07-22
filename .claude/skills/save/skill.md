---
name: save
description: 변경사항을 GitHub에 저장하고 데일리 노트에도 기록. "저장해줘", "깃허브에 올려줘", "save", "푸시해줘", "커밋해줘", "업로드해줘" 등을 언급하면 자동 실행.
argument-hint: "[커밋 메시지] (생략 시 자동 생성)"
allowed-tools:
  - Bash
  - Read
  - Edit
  - Write
  - Glob
---

# save - Git Add + Commit + Push + Progress + Daily Note

변경된 파일을 GitHub에 한 번에 저장하고, progress.md(있는 경우)와 오늘 데일리 노트에 기록.

## 사용 예시

```
저장해줘
save 오늘 작업 내용 정리
깃허브에 올려줘
```

## 실행 단계

1. **변경사항 확인**: `git status` 로 변경된 파일 목록 출력
2. **변경사항 없으면 종료**: "저장할 변경사항이 없어요" 출력 후 종료
3. **커밋 메시지 결정**:
   - 인수로 메시지가 주어지면 그대로 사용
   - 없으면 변경된 파일 목록을 보고 간결하게 자동 생성 (한국어, 50자 이내)
4. **progress.md 조건부 업데이트** (커밋 전):
   - 변경된 파일들의 상위 폴더를 보고 프로젝트 폴더 감지
   - 해당 폴더에 `progress.md`가 존재하면:
     - `## 작업 이력` 섹션에 오늘 날짜 블록 추가 (기존 이력 유지)
     - `## 현재 상태` 완료 항목 ✅ 갱신
     - `## 다음 작업 목록` 신규 항목 추가
     - `_Last updated_` 날짜 갱신
     - progress.md도 `git add`에 포함
   - `progress.md`가 없으면 이 단계 건너뜀 (기존 save와 동일하게 동작)
5. **실행**:
   ```bash
   git add .
   git commit -m "[메시지]"
   git push
   ```
6. **데일리 노트 업데이트** (없으면 자동 생성 — 사용자 합의 2026-06-26):
   - 오늘 날짜(`YYYY-MM-DD`) 기준으로 `40-personal/41-daily/YYYY-MM/YYYY-MM-DD.md` 파일 찾기
   - **파일이 없으면 자동 생성**: 월별 폴더 `mkdir -p` → `00-system/01-templates/daily-note-template.md`를 복사해 `YYYY-MM-DD`·`(요일)` 치환(daily-note 스킬 로직). 그 위에 아래 A·B 기록. (안내만 하고 건너뛰지 말 것)
   - 파일이 있으면 아래 두 가지를 처리:

   **A. `## 오늘 한 일` 섹션 업데이트** (작업 내용 요약):
   - 이번 커밋에서 변경된 파일과 progress.md(있는 경우)를 참고해 작업 내용을 요약
   - `## 오늘 한 일` 섹션이 이미 있으면 아래에 이어 붙임, 없으면 파일 상단(Git 저장 기록 위)에 새로 추가
   - 형식: 프로젝트/파일 기준으로 그룹핑, 글머리 불렛으로 핵심만 요약
   - 예시:
     ```
     ## 오늘 한 일

     ### Monthly Sales League — 2026-04 리포트
     - 전체 디자인 시스템 IBM Carbon → Apple 전환 (Inter, 18px radius, pill badges)
     - §4 Top 20: 메달 컬러 배지, YoY 바 제거
     - §5 한국 vs 글로벌: ₩ 매출 추가, 요약 박스 리라이트
     ```

   **B. `## Git 저장 기록` 섹션에 커밋 항목 추가**:
   - 형식: `- HH:MM — [커밋 메시지] (변경 N개 파일)`
   - 해당 섹션이 없으면 파일 맨 아래에 새로 추가
7. **결과 출력**:

```
✅ GitHub에 저장됐어요
   커밋: [메시지]
   변경 파일: N개
   브랜치: master → origin/master
   progress.md: 10-projects/[프로젝트명]/progress.md 업데이트됨  ← progress.md 있을 때만 표시
   데일리 노트: YYYY-MM-DD.md — 오늘 한 일 + Git 저장 기록 업데이트됨
```

## 에러 처리

- push 실패 시 에러 메시지를 그대로 출력하고 원인 설명
- 인증 오류 시: "터미널에서 `git push` 를 직접 실행해 인증을 확인해보세요" 안내
- progress.md 업데이트 실패 시: 경고만 출력하고 전체 흐름은 중단하지 않음
- 데일리 노트 업데이트 실패 시: 경고만 출력하고 전체 흐름은 중단하지 않음

## 참고

- `git add .` 로 **모든 변경사항**을 포함합니다 (신규 파일 포함)
- `.gitignore`에 등록된 파일은 자동 제외됩니다
- progress.md, 데일리 노트는 git 커밋 **성공 후**에만 기록합니다
- progress.md가 없는 폴더 작업 시 기존 save와 완전히 동일하게 동작합니다
