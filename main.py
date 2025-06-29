import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

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
