import streamlit as st
import sqlite3

# データベースに接続
conn = sqlite3.connect('members.db')
cursor = conn.cursor()

# テーブルの作成
cursor.execute('''
    CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')
conn.commit()

# ユーザー情報の入力フォームを作成
username = st.text_input("ユーザー名")
password = st.text_input("パスワード", type="password")
email = st.text_input("メールアドレス")

# ログイン状態を保持する変数
logged_in = False

# フォームの送信ボタンがクリックされた場合の処理
if st.button("登録"):
    if username and password and email:
        # データの挿入
        cursor.execute('''
            INSERT INTO members (username, password, email)
            VALUES (?, ?, ?)
        ''', (username, password, email))
        conn.commit()

        st.success("登録が完了しました！")
    else:
        st.warning("全ての情報を入力してください。")

# フォームの送信ボタンがクリックされた場合の処理
if st.button("ログイン"):
    # ユーザー名とパスワードが入力されているかをチェック
    if username and password:
        # データベースからユーザー情報を取得
        cursor.execute("SELECT * FROM members WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()

        if user:
            # ユーザーが見つかった場合、ログイン状態を更新
            logged_in = True
            st.success("ログインに成功しました！")
        else:
            st.warning("ユーザー名またはパスワードが正しくありません。")
    else:
        st.warning("ユーザー名とパスワードを入力してください。")

# ログイン状態を表示
if logged_in:
    st.write("ログイン済みです。")

# データベースとの接続を閉じる
conn.close()

