# TkinterDiary
## 紹介
このアプリケーションはTkinterを使った日記アプリです。  
初めてTkinterを利用したこともあり、仕様の理解を深めるためにテストコードを書きました。  
そしてその後実装をChatGPTで賄いました。
- test1.py,test2.pyは動作確認にご活用ください。
    - これらが動作しない場合はpythonの導入がされているか再度確認をしてください。 

## 使い方

1. このリポジトリをローカルにクローンします。

   ```
   git clone https://github.com/ms3nd3r/TkinterDiary.git
   ```

2. `diary.py`ファイルを開きます。

3. プログラムを実行します。

4. テキストエリアに日記の内容を入力します。

5. 保存ボタンをクリックします。

6. 日記が保存され、テキストエリアの内容が初期化されます。

7. アラートメッセージが表示されます。

日記のデータは、`diaryData`ディレクトリに`yyyy年mm月.txt`という名前のファイルとして保存されます。日記を記録する際には、タイムスタンプが付与されます。ファイルが存在する場合は、そのファイルの最下部に日記の内容が追記されます。ファイルが存在しない場合は、新規作成されます。

## コードの作り方と修正
(後ほどブログにまとめます。)