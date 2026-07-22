#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
build-deck-pdf.py — 발표 덱 HTML → '모바일에서 안 깨지는' PDF (세팅 완료, 항상 이걸로 뽑을 것)

자동 적용 3종 (카카오톡/iOS PDF 뷰어 깨짐 방지):
  1) glow 제거   : box-shadow/text-shadow 전부 삭제 → iOS 뷰어가 흐림 그림자를
                   '꽉 찬 초록/골드 사각형'으로 잘못 렌더하는 문제 차단. (디자인은 테두리·색·
                   그라데이션으로 유지됨 — glow만 사라짐)
  2) 폰트 임베드 : --virtual-time-budget로 CDN 웹폰트(Pretendard·IBM Plex Mono) 로드 후 인쇄
                   → 한글 □ 두부 방지. 이모지는 본래색 그대로 Image/Type3로 임베드.
  3) 경로 우회   : OneDrive 폴더로 직접 --print-to-pdf 하면 '액세스 거부(0x5)' → 시스템 temp에
                   렌더 후 목표 위치로 복사.
끝에 폰트 임베드/glow 잔존을 자동 검증한다.

Usage:
  python build-deck-pdf.py <input.html> [output.pdf]
  # output 생략 시 input과 같은 이름의 .pdf
"""
import sys, re, os, subprocess, tempfile, shutil, urllib.parse

CHROME_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
]

def find_browser():
    for p in CHROME_CANDIDATES:
        if os.path.exists(p):
            return p
    sys.exit("[build-deck-pdf] Chrome/Edge를 찾지 못함. CHROME_CANDIDATES 경로 확인.")

def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: python build-deck-pdf.py <input.html> [output.pdf]")
    src = os.path.abspath(sys.argv[1])
    if not os.path.exists(src):
        sys.exit(f"[build-deck-pdf] 입력 없음: {src}")
    out = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else os.path.splitext(src)[0] + ".pdf"
    browser = find_browser()

    html = open(src, encoding="utf-8").read()

    # 1) glow 전부 제거
    n_box = html.count("box-shadow"); n_txt = html.count("text-shadow")
    html2 = re.sub(r'(?:box|text)-shadow\s*:[^;}"\']*;?', '', html)

    # 입력과 같은 폴더에 임시 HTML (상대경로·로컬 자산 보존)
    tmp_html = os.path.join(os.path.dirname(src), ".deck_render_tmp.html")
    open(tmp_html, "w", encoding="utf-8").write(html2)

    # 2)+3) 시스템 temp에 렌더 (OneDrive 출력 거부 우회)
    tmp_pdf = os.path.join(tempfile.gettempdir(), "deck_render_tmp.pdf")
    url = "file:///" + urllib.parse.quote(tmp_html.replace("\\", "/"))
    try:
        subprocess.run([
            browser, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
            "--virtual-time-budget=20000", "--run-all-compositor-stages-before-draw",
            f"--print-to-pdf={tmp_pdf}", url,
        ], check=True, capture_output=True)
        shutil.copyfile(tmp_pdf, out)
    finally:
        for f in (tmp_html, tmp_pdf):
            try: os.remove(f)
            except OSError: pass

    # 검증
    data = open(out, "rb").read()
    fonts = sorted(set(re.findall(rb"/BaseFont */([A-Za-z0-9+,\-]+)", data)))
    fontfile = data.count(b"FontFile")
    has_pretendard = b"Pretendard" in data
    glow_left = html2.count("box-shadow") + html2.count("text-shadow")
    passed = has_pretendard and fontfile > 0 and glow_left == 0

    print(f"[build-deck-pdf] OK -> {out}  ({len(data)//1024} KB)")
    print(f"  glow 제거: box-shadow {n_box}→0, text-shadow {n_txt}→0 (잔존 {glow_left})")
    print(f"  임베드 폰트({fontfile} FontFile): " + b", ".join(fonts).decode("ascii", "replace"))
    print(f"  모바일 안전: {'PASS ✅' if passed else 'FAIL ⚠️  — 재확인 필요'}")
    if not passed:
        sys.exit(1)

if __name__ == "__main__":
    main()
