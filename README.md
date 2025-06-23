# Obsidian + Markdown暗記フィルター変換ツール

Obsidianで暗記用ノートを使いたくてCSSスニペットを試してみた記録です。  
JavaScriptが制限されるなどの理由で、最終的には外部アプリでHTMLに変換して使う形になりました。

Obsidian＋Markdown＋変換スクリプトで「答えを隠して表示」するノートが簡単に作れるようになります！

---

## ObsidianとCSSスニペット

Obsidian に出会って、シンプルで使いやすいことに感動！  
CSSスニペットという仕組みを使って、クリックで答えを表示する**暗記ノート**を試作しました。


## スニペット導入手順（ゼロから）

### ①snippetsフォルダを作る
1. Obsidian で使ってる **Vault**（ノートの入ってるフォルダ）を開く
2.  中にある `.obsidian` フォルダを開く
3. その中に新しく `snippets` という名前のフォルダを作る（手動でOK）
```sh
📁 Vault/
├─ .obsidian/
│  ├─ plugins/
│  ├─ themes/
│  └─ snippets/ ← これを新しく作る！
```

### ② .css ファイルを入れる
1. `snippets` フォルダの中に `my-cloze-style.css` など好きな名前で `.css` ファイルを作る
2. `.css` ファイルにコードを書く
```css
/* my-cloze-style.css */

.cloze {
    background-color: rgb(84, 223, 193);
    color: transparent;
    border-bottom: 1px solid rgb(17, 0, 255);
    border-radius: 3px;
    cursor: pointer;
    transition: color 0.3s ease;
  }

  .cloze:hover {
    color: black;
  }
```

### ③ 使い方

- Markdown（Obsidian）ではで囲む

```markdown
この果物は <span class="cloze">りんご</span> です。
```

→ 通常は「マーカーが引かれて文字が見えない」状態
→ ホバー（マウスを重ねる）と「りんご」が表示される<br>
※ ノートを書くときに毎回 spanタグ を書く手間はあるけど、Obsidianの「しおり」機能でノートの横にメモを置けるので、十分許容できると感じました💡

🚫 限界：クリックで表示させたかった…
クリック表示をしたい場合、JavaScriptが必要になりますが、
Obsidianではセキュリティ上、通常のノートにJavaScriptを組み込むことはできません。

## 💡 解決策：MarkdownをHTMLに変換する外部アプリを作成！
- MarkdownファイルをテンプレートHTMLに差し込んで、複数HTMLを自動生成

### 📁 フォルダ構成
```sh
md2html/
├─ input/             ← Markdownファイルをここに入れる
│   ├─ example1.md    # 変換したいファイルをここに持ってくる
│   └─ example2.md
├─ output/            ← HTMLが出力される
├─ template.html      ← 共通テンプレート
├─ style.css          ← デザイン
├─ script.js          ← 動作追加
└─ convert.py         ← 実行スクリプト
```

### template.html

```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <title>Flash_words</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <main>
    {content}
  </main>
  <script src="../script.js"></script>
</body>
</html>
```

### style.css / シンプル

```css
.cloze {
  background-color: #7ae0d6;
  padding: 0 1em;
  border-radius: 4px;
  cursor: pointer;
  display: inline-block;
  margin-bottom: 2px; /* マーカー同士の間隔を確保 */
}

.cloze.hidden {
  color: transparent;
  background-color: #ccc;
}

  /* オプション: ホバー時のスタイル */
.cloze:hover {
  background-color: #5fbdae;
}
.p {
  margin: 2px;
}
```

### style.css / ダークモード

```css
.cloze {
  background-color: #FFFF77;
  border-radius: 2px;
  cursor: pointer;
  padding: 0 1em;
  display: inline-block;
  margin-bottom: 2px; /* マーカー同士の間隔を確保 */
  margin-top: 2px;
  color: #000;
}
  
.cloze.hidden {
  color: transparent;
  background-color: #99CCFF;
  padding-top: 0;
}

.cloze:hover {
  background-color: #FFFF77;
}

main {
  max-width: 60%;
  margin: 0 auto;
  background-color: #333333;
  padding: 5px 0 8rem;
}

body {
  background-color: #222222;
  color: #99CCFF;
  font-family: "Segoe UI", sans-serif;
  margin: 0;   /* 要素の外側の余白 */
  padding: 0;  /* 要素の内側の余白 */
}

h1, h2, h3 {
  color: #CC99FF;  
  border-bottom: 2px solid #222222;
  margin: 35px auto 8px ;
  padding: 0 2.3em 0.2em;
}

strong {
  color: #FFFF77;
}

ul, li {
 padding-right: 4em;  /* 文字の折り返し位置の調整 */
}

li {
  line-height: 1.5;
  overflow-wrap: break-word;
  padding: 0 5px 0 2em;
  list-style: none;
}

ul {
  margin-top: 1em;
  margin-bottom: 2px;
  padding-left: 2em;
}

table {
  border-collapse:  collapse;     /* セルの線を重ねる */
  margin-right: 5em;
  margin-left: 5em;
}
th {
  background-color: #222222;
  font: bold;
  border: solid 1px #99CCFF;    /* 枠線指定 */
  padding: 4px;
}
td {
  background-color: #222222;
  border: solid 1px #99CCFF;    /* 枠線指定 */
  padding: 4px;
}

@media screen and (max-width:1120px) {
 main {
  max-width: 100%;
 }
}
```
### script.js

```javascript
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".cloze").forEach(function (el) {
	// 最初にhiddenクラスを追加して隠す
	el.classList.add("hidden");  // ←ブラウザに最初に表示される・単語が隠れている状態
    el.addEventListener("click", function () {
      el.classList.toggle("hidden");
    });
  });
});
```

### convert.py

```python
import os
import markdown

input_dir = "input"
output_dir = "output"
template_file = "template.html"

# 出力フォルダがなければ作成
os.makedirs(output_dir, exist_ok=True)

# テンプレート読み込み
with open(template_file, "r", encoding="utf-8") as f:
    template = f.read()

# inputフォルダ内の.mdファイルを処理
for filename in os.listdir(input_dir):
    if filename.endswith(".md"):
        md_path = os.path.join(input_dir, filename)
        with open(md_path, "r", encoding="utf-8") as f:
            md_content = f.read()
        # Markdown → HTML
        html_content = markdown.markdown(md_content, extensions=["extra"])
        # テンプレートに差し込み
        final_html = template.replace("{content}", html_content)
        # 出力
        out_path = os.path.join(output_dir, filename.replace(".md", ".html"))
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(final_html)

print("✅ すべてのMarkdownをHTMLに変換しました！")
```

### ✅ 使い方 

1. `input/` に `.md` ファイルを入れる
	- .mdファイル がコピペでフォーマットが崩れることあり。
	- VSコードで確認すると良！
2. ターミナルで `convert.py` を実行
```sh
python convert.py

# import markdownできない、モジュールが見つからないエラーが出たらインストール
pip install markdown

# インストールしてから
python convert.py
```
3. `output/` にHTMLが出力される
4. HTMLをブラウザで表示

ブラウザで開けば暗記フィルターつきHTML！

### GitHub Pages で自動生成されたWebページを公開しました！
https://yanagisawa-noriko.github.io/md-to-html-app/

GitHubで公開しているフォルダ構成には、公開ページ用のフォルダも含まれています。
```
md2html/
├─ docs/              ← ※公開ページ用※
├─ input/             ← Markdownファイルをここに入れる
│   ├─ example1.md    # 変換したいファイルをここに持ってくる
│   └─ example2.md
├─ output/            ← HTMLが出力される
├─ template.html      ← 共通テンプレート
├─ style.css          ← デザイン
├─ script.js          ← 動作追加
└─ convert.py         ← 実行スクリプト
```
