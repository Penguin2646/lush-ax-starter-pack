---
name: youtube-to-notion
description: YouTube URL을 주면 영상 정보를 자동으로 파싱해 노션 데이터베이스에 저장. "유튜브 저장", "유튜브 노션에 저장", "youtube notion", "이 유튜브 정리해줘", "영상 저장" 등을 언급하거나 youtube.com 또는 youtu.be URL을 제공하면 자동 실행.
context: fork
allowed-tools:
  - Bash
  - Read
---

# youtube-to-notion Skill

YouTube URL을 받아 영상 메타데이터를 추출하고, 노션 DB에 정리해서 저장한다.

## 설정값 (고정)

- **Notion DB ID**: `35d4b75477c781e0bc3de863eef7cb7f`
- **스크립트 경로**: `.claude/skills/youtube-to-notion/scripts/youtube_fetch.py`
- **Notion API 스크립트**: `.claude/skills/notion-handler/scripts/notion_api.py`

## 실행 절차

### 1단계: YouTube 메타데이터 수집

```bash
python3 .claude/skills/youtube-to-notion/scripts/youtube_fetch.py "YOUTUBE_URL"
```

반환 필드: `title`, `channel`, `url`, `video_id`, `thumbnail`, `duration`, `upload_date`, `description`, `tags`, `categories`

### 2단계: 카테고리 자동 분류

`tags`, `categories`, `title`, `description`을 분석해 아래 중 가장 적합한 것을 1~3개 선택:
- `마케팅` — 브랜드, 광고, 콘텐츠, 소셜미디어
- `세일즈` — 영업, 판매 전략, 고객 확보
- `데이터` — 분석, 통계, 예측, 대시보드
- `AI·테크` — AI, 머신러닝, 개발, 자동화
- `비즈니스` — 경영, 전략, 트렌드, 사례
- `기타` — 위에 해당 없음

### 3단계: 핵심 요약 생성

`description` (최대 2000자)을 읽고 **한국어로 3~5줄** 핵심 요약 작성.
description이 없거나 너무 짧으면 title에서 유추해서 작성.

### 4단계: Notion DB에 페이지 생성

```bash
python3 .claude/skills/notion-handler/scripts/notion_api.py create-page \
  --parent "35d4b75477c781e0bc3de863eef7cb7f" \
  --properties '{
    "제목": "TITLE",
    "URL": "YOUTUBE_URL",
    "섬네일": "THUMBNAIL_URL",
    "채널명": "CHANNEL",
    "카테고리": ["카테고리1", "카테고리2"],
    "시청 상태": "미시청",
    "영상 길이": "DURATION",
    "업로드일": "YYYY-MM-DD",
    "저장일": "TODAY_DATE",
    "핵심 요약": "SUMMARY_TEXT",
    "플레이리스트": "미분류",
    "공유 여부": false
  }'
```

> `저장일`은 오늘 날짜(YYYY-MM-DD), `upload_date`가 없으면 해당 필드 생략.

### 5단계: 페이지 본문 블록 추가

create-page 응답에서 `page_id`를 추출한 후 블록을 추가:

```bash
python3 .claude/skills/notion-handler/scripts/notion_api.py append-blocks \
  --id "PAGE_ID" \
  --blocks '[
    {"type": "image", "url": "THUMBNAIL_URL"},
    {"type": "divider"},
    {"type": "heading_2", "text": "핵심 요약"},
    {"type": "callout", "text": "SUMMARY_TEXT", "emoji": "📌"},
    {"type": "heading_2", "text": "영상 설명"},
    {"type": "paragraph", "text": "DESCRIPTION_FIRST_500"},
    {"type": "divider"},
    {"type": "bookmark", "url": "YOUTUBE_URL"}
  ]'
```

> `DESCRIPTION_FIRST_500`: description의 첫 500자. 없으면 해당 블록 생략.

## 완료 후 출력

저장 완료 후 사용자에게 다음을 출력:

```
✅ 노션에 저장됐어요!

📺 **[영상 제목]**
📡 채널: [채널명]
⏱ 길이: [영상 길이]  |  📅 업로드: [업로드일]
🏷 카테고리: [카테고리1, 카테고리2]

📝 핵심 요약:
[요약 내용]

🔗 노션 페이지: https://www.notion.so/[PAGE_ID without hyphens]
```

## 오류 처리

- yt-dlp 실패 시: "영상 정보를 가져오지 못했어요. URL을 확인해주세요." 출력
- 비공개/삭제된 영상: 해당 사실 안내
- Notion 저장 실패 시: API 오류 메시지 그대로 출력
