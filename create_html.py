from datetime import datetime
import os
import re

# 数字を含むファイル名を数値でソートする関数
def sort_by_number(filename):
    # 正規表現でファイル名から数字を抽出
    match = re.search(r'(\d+)', filename)
    # 数字が見つかればそれを返し、見つからなければ0を返す
    return int(match.group(1)) if match else 0

# 画像が入っているフォルダのパスを指定
root_folder = "downloads"

# HTMLのヘッダー部分　home.html
#  リファラが違う
html_header_home = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Gallery</title>
    <script>
        // リファラ（参照元）をチェックする関数
        window.onload = function() {
            const referrer = document.referrer;
            //  リファラが空または認証ページ以外なら、認証ページにリダイレクト
            if (!referrer || !referrer.includes("https://dannyso16.github.io/KyuyoMeisaiKaitoriyasanViewer/")) {
                window.location.href = "https://dannyso16.github.io/KyuyoMeisaiKaitoriyasanViewer/";
            }
        };
    </script>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 20px;
        }
        img {
            display: block;
            margin: 10px auto;
            max-width: 100%;
            height: auto;
        }
        .folder-title {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            margin: 20px 0;
        }
        a {
            display: block;
            text-align: center;
            font-size: 20px;
            color: #333;
            text-decoration: none;
            margin: 10px;
        }
        a:hover {
            color: #007BFF;
        }
        .folder-list {
            max-width: 600px;
            margin: 0 auto;
            text-align: center;
        }
    </style>
</head>
<body>
"""

# HTMLのヘッダー部分　サブページ
#  リファラが違う
html_header_sub = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Gallery</title>
    <script>
        // リファラ（参照元）をチェックする関数
        window.onload = function() {
            const referrer = document.referrer;
            //  リファラが空またはhomeページ以外なら、認証ページにリダイレクト
            if (!referrer || !referrer.includes("https://dannyso16.github.io/KyuyoMeisaiKaitoriyasanViewer/home.html")) {
                window.location.href = "https://dannyso16.github.io/KyuyoMeisaiKaitoriyasanViewer/";
            }
        };
    </script>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 20px;
        }
        img {
            display: block;
            margin: 10px auto;
            max-width: 100%;
            height: auto;
        }
        .folder-title {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            margin: 20px 0;
        }
        a {
            display: block;
            text-align: center;
            font-size: 20px;
            color: #333;
            text-decoration: none;
            margin: 10px;
        }
        a:hover {
            color: #007BFF;
        }
        .folder-list {
            max-width: 600px;
            margin: 0 auto;
            text-align: center;
        }
    </style>
</head>
<body>
"""

# HTMLのフッター部分（共通）
html_footer = """
</body>
</html>
"""

# メインインデックスページ用のHTMLコンテンツ
index_content = """
<div class="folder-list">
<h1>給与明細買取屋さん　まとめのまとめ</h1>
"""

# サブフォルダ情報をリストに保存（フォルダ名と更新日時）
folders_info = []

# ルートフォルダ内のサブフォルダを探索
for subdir, _, files in os.walk(root_folder):
    png_files = [f for f in files if f.endswith(".png") or f.endswith(".jpeg")]
    png_files = sorted(png_files, key=sort_by_number)
    
    if png_files:
        # サブフォルダ名と最終更新日時を取得
        folder_name = os.path.basename(subdir)
        folder_mod_time = os.path.getmtime(subdir)
        formatted_time = datetime.fromtimestamp(folder_mod_time).strftime('%Y-%m-%d')
        
        # サブフォルダ情報をリストに追加
        folders_info.append((folder_name, folder_mod_time, formatted_time, png_files))

# 更新日時が遅い順にソート（新しい順）
folders_info.sort(key=lambda x: x[1], reverse=True)

# ソートしたフォルダ情報からインデックスページとサブページを作成
for folder_name, folder_mod_time, formatted_time, png_files in folders_info:
    folder_page = f"{folder_name}.html"
    
    # サブフォルダ名と更新日時をインデックスページに追加
    index_content += f'<a href="{folder_page}">{folder_name}({formatted_time})</a>\n'
    
    # サブフォルダ専用のページを作成
    folder_content = f'<div class="folder-title">{folder_name}</div>\n'
    for file in png_files:
        file_path = os.path.join(root_folder, folder_name, file)
        folder_content += f'<img src="{file_path}" alt="{file}">\n'
    
    # サブフォルダ専用ページを書き出す
    folder_html = html_header_sub + folder_content + html_footer
    with open(folder_page, "w", encoding="utf-8") as f:
        f.write(folder_html)


# メインインデックスページを書き出す
index_content += "</div>\n"  # folder-listクラスの閉じタグ
index_html = html_header_home + index_content + html_footer

output_index = "home.html"
with open(output_index, "w", encoding="utf-8") as f:
    f.write(index_html)

print(f"インデックスページが生成されました: {output_index}")
