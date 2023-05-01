import tkinter as tk
from datetime import datetime


# メインウィンドウの作成
root = tk.Tk()
root.geometry('500x300')
root.title('日記アプリ')

# テキストエリアの作成
text = tk.Text(root, height=5)
text.pack()

# 保存ボタンのクリック時の処理
def save_text():
    diary = text.get('1.0', 'end-1c')  # 入力されたテキストの取得
    today = datetime.today().strftime('%Y年%m月')
    file_name = today + '.txt'
    with open(file_name, 'a', encoding='utf-8') as f:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # タイムスタンプの取得
        f.write(timestamp + '\n')  # タイムスタンプの書き込み
        f.write(diary + '\n\n')  # ファイルにテキストを書き込む
    text.delete('1.0', 'end')  # テキストエリアの内容を初期化する
    tk.messagebox.showinfo('更新完了！', '日記を更新しました。')  # アラートメッセージの表示

# 保存ボタンの作成
save_button = tk.Button(root, text='保存', command=save_text)
save_button.pack()

# メインループの開始
root.mainloop()