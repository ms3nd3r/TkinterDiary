import os
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# diaryDataディレクトリがない場合は作成する
if not os.path.exists('diaryData'):
    os.makedirs('diaryData')

# メインウィンドウの作成
root = tk.Tk()
root.geometry('500x300')
root.title('日記アプリ')


# ウィンドウの背景色を黒に設定
root.configure(bg='#1C1C1C')

# テキストエリアの作成
text = tk.Text(root, height=5, bg='black', fg='white', insertbackground='white')
text.pack()

# 保存ボタンのクリック時の処理
def save_text():
    diary = text.get('1.0', 'end-1c')  # 入力されたテキストの取得
    today = datetime.today().strftime('%Y年%m月')
    file_name = os.path.join('diaryData', today + '.txt')  # ファイルのパスを指定する
    with open(file_name, 'a', encoding='utf-8') as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # タイムスタンプの取得
        f.write(timestamp + '\n')  # タイムスタンプの書き込み
        f.write(diary + '\n\n')  # ファイルにテキストを書き込む
    text.delete('1.0', 'end')  # テキストエリアの内容を初期化する
    messagebox.showinfo('更新完了！', '日記を更新しました。')  # アラートメッセージの表示

# # 保存ボタンの作成
# save_button = tk.Button(root, text='保存', command=save_text)
# save_button.pack()
# 保存ボタンの作成
save_button = tk.Button(root, text='保存', command=save_text, font=('Helvetica', 22), bg='white', fg='black')
save_button.pack(pady=10)

# メインループの開始
root.mainloop()
