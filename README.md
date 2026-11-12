# データ物質化 事例カタログ

データを物の形・素材・動きに置き換えた事例（data physicalization）を、年代・素材・感覚・データの種類・用途で絞り込める一覧です。

公開ページ: https://n1n9-jp.github.io/data-physicalization-catalog/

## 収録内容

- 444件（データを伴う事例417件、データを伴わない関連技術27件）
- 432件は [List of Physical Visualizations and Related Artifacts](https://dataphys.org/list/gallery)（Pierre Dragicevic, Yvonne Jansen 編）に基づきます
- 12件は、この一覧にない事例を一次情報から加えたものです（藁算、大津浪記念碑、まるごとまちごとハザードマップ、桜ライン311 など）
- 説明文はこのカタログで書き起こしたものです
- もとの一覧は「CC-BY-SA」で公開され、再利用する場合は一覧ページを参照するよう求めています

## 写真について

一覧の各カードには、dataphys.org の一覧ページにあるサムネイル画像を表示しています。画像はこのリポジトリに複製せず、dataphys.org から読み込んでいます。写真の権利は、それぞれの作者・提供者にあります。出典は各事例の該当ページで確認できます。

- 対象は dataphys.org の一覧に基づく432件です。独自に追加した12件には写真がありません
- 画像のパスは `data/thumbs.json` にあり、`build/fetch_thumbs.py` で一覧ページから作り直せます
- dataphys.org 側で画像の場所が変わると表示されなくなります。その場合は「写真を読み込めませんでした」と表示されます

## 分類について

素材・感覚・データの種類・用途・動きの5軸は、このカタログのために付けた試案です。各事例の公開情報から1件ずつ判断していますが、元ページと1件ずつ照合したものではありません。授業や研究で使う際は、元の出典で確かめてください。

## 構成

| パス | 内容 |
|---|---|
| `index.html` | 公開ページ（データを埋め込んだ単一ファイル） |
| `data/*.txt` | 事例データ。1行1件、`\|` 区切り |
| `data/thumbs.json` | 事例ごとのサムネイル画像のパス（dataphys.org 上） |
| `build/fetch_thumbs.py` | 一覧ページから `data/thumbs.json` を作る |
| `build/parse.py` | データの検査と `build/data.json` の生成 |
| `build/make.py` | `build/template.html` にデータを埋め込み `index.html` を生成 |

`data/*.txt` の列は次の順です。

```
年|dataphys.orgのスラッグまたは出典URL|名称|作者|説明|素材|感覚|データの種類|用途|動き|フラグ
```

各コードの意味は `build/parse.py` の先頭にあります。フラグは `x`＝データを伴わない関連技術、`j`＝日本に関わる事例、`n`＝独自に追加した事例です。

## 更新のしかた

```bash
python3 build/fetch_thumbs.py   # 写真のパスを取り直すときだけ
python3 build/parse.py   # コードの検査。errors 0 を確認
python3 build/make.py    # index.html を再生成
```

## 分類の参考にした文献

- Jansen ほか (2015) [Opportunities and Challenges for Data Physicalization](https://doi.org/10.1145/2702123.2702180), CHI '15
- Bae ほか (2022) [Making Data Tangible](https://arxiv.org/abs/2202.10520v1), CHI '22
- Hogan, Hornecker (2017) [Towards a Design Space for Multisensory Data Representation](https://doi.org/10.1093/iwc/iww015)
