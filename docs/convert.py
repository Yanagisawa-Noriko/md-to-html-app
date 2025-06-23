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