# 📈 Streamlit Stock Chart & News App / 株価チャート＆ニュースアプリ

A simple **Streamlit Web App** for learning and practicing web app development using Python.  
It includes a stock chart viewer, economic news feed, user login functionality, and is aimed at full deployment in the future.

PythonとStreamlitを使った**Webアプリ開発の学習用**プロジェクトです。  
株価チャート表示、経済ニュース取得、ログイン機能を実装し、最終的にはデプロイまでを目指します。

---

## 🚀 Features / 主な機能

- 📊 **Stock Price Chart** (with 25/75-day moving averages)  
  25日線・75日線付きの株価チャート表示

- 📰 **Economic News Feed** using RSS  
  経済ニュースをRSSで取得・表示

- 🔐 **Login System (Session-based)**  
  簡易ログイン機能（セッション管理）

- 🗂️ **Single File App (for now)**  
  単一ファイルで構成された簡易アプリ構成

- ☁️ **Future-ready for Deployment**  
  将来的にデプロイ可能な構成に

---

## 🛠️ Technologies / 技術スタック

- [Python 3.10+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [yfinance](https://pypi.org/project/yfinance/)
- [feedparser](https://pypi.org/project/feedparser/)
- [matplotlib](https://matplotlib.org/)
- [SQLite3 (for user auth)](https://www.sqlite.org/index.html)

---

## 📦 Setup / セットアップ方法

1. **Clone this repo / リポジトリをクローン**
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name```

2. Create virtual environment / 仮想環境の作成
```python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate```

3. Install dependencies / 必要なライブラリのインストール
```pip install -r requirements.txt```

4. Run the app / アプリを起動
```streamlit run main.py```


---

🌐 Deployment (coming soon) / デプロイ（今後予定）

This app is being prepared for deployment to platforms such as:

Streamlit Community Cloud

Render

Railway


このアプリは、上記のようなPaaS環境へのデプロイを予定しています。


---

📚 Learning Purpose / 学習目的

This project was created as a personal learning tool for building full-stack data apps with Python and Streamlit.

このプロジェクトは、PythonとStreamlitを使った個人学習用のWebアプリ開発教材として制作されました。


---

📄 License / ライセンス

MIT License


---

🙌 Author / 作者

Name: hisao


---