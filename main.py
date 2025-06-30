import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import sqlite3
import hashlib

# --- パスワードハッシュ化関数 ---
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# --- DBに接続しユーザー登録 ---
def create_usertable():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users(username TEXT PRIMARY KEY, password TEXT)')
    conn.commit()
    conn.close()

def add_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users(username, password) VALUES (?, ?)', (username, hash_password(password)))
        conn.commit()
    except sqlite3.IntegrityError:
        st.error("そのユーザー名は既に使われています")
    conn.close()

def login_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, hash_password(password)))
    data = c.fetchone()
    conn.close()
    return data

# --- Streamlit アプリ本体 ---
def main():
    st.title("ログイン機能付き Streamlit アプリ")
    menu = st.sidebar.selectbox("メニュー", ["ログイン", "新規登録"])

    create_usertable()

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        st.success("ログイン済みです")
        
        # 日本語フォントを指定
        matplotlib.rcParams['font.family'] = 'MS Gothic'

        st.title("📈 株価チャート表示アプリ")

        # 銘柄入力
        ticker = st.text_input("ティッカーシンボルを入力してください（例：AAPL、GOOG、7203.T）", "AAPL")

        # 日付範囲
        start_date = st.date_input("開始日", pd.to_datetime("2024-01-01"))
        end_date = st.date_input("終了日", pd.to_datetime("today"))

        if start_date >= end_date:
            st.error("開始日は終了日より前にしてください。")
        else:
            # 株価データ取得
            data = yf.download(ticker, start=start_date, end=end_date)

            if data.empty:
                st.warning("データが取得できませんでした。")
            else:
                # 移動平均線を計算
                data["MA25"] = data["Close"].rolling(window=25).mean()
                data["MA75"] = data["Close"].rolling(window=75).mean()

                # プロット
                fig, ax = plt.subplots()
                ax.plot(data.index, data["Close"], label="終値", color="blue")
                ax.plot(data.index, data["MA25"], label="25日移動平均", color="orange")
                ax.plot(data.index, data["MA75"], label="75日移動平均", color="green")
                ax.set_title(f"{ticker} の株価")
                ax.set_xlabel("日付")
                ax.set_ylabel("価格")
                ax.legend()
                ax.grid(True)
                st.pyplot(fig)

        if st.button("ログアウト"):
            st.session_state.logged_in = False
            st.rerun()

    elif menu == "ログイン":
        st.subheader("ログイン画面")
        username = st.text_input("ユーザー名")
        password = st.text_input("パスワード", type="password")
        if st.button("ログイン"):
            user = login_user(username, password)
            if user:
                st.session_state.logged_in = True
                st.success(f"{username} さん、ようこそ！")
                st.rerun()
            else:
                st.error("ユーザー名またはパスワードが違います")

    elif menu == "新規登録":
        st.subheader("新規登録画面")
        new_user = st.text_input("新しいユーザー名")
        new_pass = st.text_input("新しいパスワード", type="password")
        if st.button("登録"):
            if new_user and new_pass:
                add_user(new_user, new_pass)
                st.success("登録が完了しました。ログインしてください。")
            else:
                st.warning("ユーザー名とパスワードを入力してください。")

if __name__ == "__main__":
    main()