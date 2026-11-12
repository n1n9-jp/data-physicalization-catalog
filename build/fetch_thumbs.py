"""dataphys.org の一覧ページから、各事例のサムネイル画像のパスを集めて data/thumbs.json に書き出す。

画像そのものは保存しない。公開ページは dataphys.org 上の画像を参照して表示する。
使い方: python3 build/fetch_thumbs.py            （一覧ページを取得）
        python3 build/fetch_thumbs.py gallery.html  （保存済みのHTMLを使う）
"""
import json, os, re, sys, urllib.request
SRC = 'https://dataphys.org/list/gallery'
here = os.path.dirname(os.path.abspath(__file__))
if len(sys.argv) > 1:
    html = open(sys.argv[1], encoding='utf-8', errors='replace').read()
else:
    req = urllib.request.Request(SRC, headers={'User-Agent': 'data-physicalization-catalog (thumbnail index)'})
    html = urllib.request.urlopen(req, timeout=60).read().decode('utf-8', errors='replace')
pairs = re.findall(r'<a href="https://dataphys\.org/list/([^/"]+)/">\s*<img class="list-view"[^>]*src="([^"]+)"', html)
thumbs = {slug: src for slug, src in pairs if src.startswith('/list/')}
out = os.path.join(here, '..', 'data', 'thumbs.json')
json.dump(dict(source=SRC, base='https://dataphys.org', thumbs=dict(sorted(thumbs.items()))), open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print('thumbnails', len(thumbs))
