#!/usr/bin/env python3
"""
YouTube metadata fetcher using yt-dlp.
Outputs structured JSON for the youtube-to-notion skill.
"""

import sys
import json
import subprocess
import re
from datetime import datetime


def format_duration(seconds):
    if not seconds:
        return "알 수 없음"
    seconds = int(seconds)
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    if h > 0:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"


def format_date(date_str):
    """YYYYMMDD → YYYY-MM-DD"""
    if not date_str or len(date_str) != 8:
        return None
    try:
        return f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:8]}"
    except Exception:
        return None


def extract_video_id(url):
    patterns = [
        r"(?:v=|youtu\.be/|embed/|shorts/)([A-Za-z0-9_-]{11})",
    ]
    for p in patterns:
        m = re.search(p, url)
        if m:
            return m.group(1)
    return None


def fetch_metadata(url):
    cmd = [
        sys.executable, "-m", "yt_dlp",
        "--dump-json",
        "--no-playlist",
        "--skip-download",
        url
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if result.returncode != 0:
        raise RuntimeError(f"yt-dlp 오류: {result.stderr[:300]}")
    return json.loads(result.stdout)


def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "YouTube URL을 인자로 전달하세요"}))
        sys.exit(1)

    url = sys.argv[1]
    try:
        meta = fetch_metadata(url)
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

    video_id = meta.get("id") or extract_video_id(url)
    thumbnail = (
        meta.get("thumbnail")
        or (f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg" if video_id else None)
    )

    tags = meta.get("tags") or []
    categories = meta.get("categories") or []

    output = {
        "title": meta.get("title", "제목 없음"),
        "channel": meta.get("uploader") or meta.get("channel", "알 수 없음"),
        "url": meta.get("webpage_url") or url,
        "video_id": video_id,
        "thumbnail": thumbnail,
        "duration": format_duration(meta.get("duration")),
        "upload_date": format_date(meta.get("upload_date")),
        "description": (meta.get("description") or "")[:2000],
        "view_count": meta.get("view_count"),
        "like_count": meta.get("like_count"),
        "tags": tags[:10],
        "categories": categories,
    }

    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
