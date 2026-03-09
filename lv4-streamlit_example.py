import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

# --- 1. 網頁設定 ---
st.set_page_config(page_title="超級投資戰情室", layout="wide")

st.title("📈 我的 AI 投資戰情室 (Interactive Dashboard)")
st.markdown("這是你的畢業專案：結合 **Python 資料抓取** 與 **互動式網頁** 的強大工具！")

# --- 2. 側邊欄：參數控制區 (Sidebar) ---
st.sidebar.header("⚙️ 參數設定")

# 輸入股票代號
stock_id = st.sidebar.text_input("輸入股票代號 (台股請加 .TW)", value="2330.TW")

# 選擇時間範圍
days_back = st.sidebar.slider("回測天數", min_value=30, max_value=1000, value=365, step=30)

# 設定均線參數 (這就是互動的精髓！)
st.sidebar.subheader("技術指標設定")
ma_short = st.sidebar.number_input("短期均線 (MA_Fast)", min_value=3, max_value=50, value=5)
ma_long = st.sidebar.number_input("長期均線 (MA_Slow)", min_value=10, max_value=200, value=20)

# --- 3. 抓取資料 (使用快取裝飾器，讓網頁跑得飛快) ---

@st.cache_data
def get_data(ticker, days):
    start_date = datetime.now() - timedelta(days=days)
    df = yf.Ticker(ticker).history(start=start_date)
    return df

# 當使用者改參數時，這裡會自動重跑
try:
    df = get_data(stock_id, days_back)
    
    # 計算均線
    df[f'MA_{ma_short}'] = df['Close'].rolling(window=ma_short).mean()
    df[f'MA_{ma_long}'] = df['Close'].rolling(window=ma_long).mean()

    # --- 4. 關鍵數據指標 (Metric) ---
    # 算出最近一天的漲跌幅
    last_close = df['Close'].iloc[-1]
    prev_close = df['Close'].iloc[-2]
    change = last_close - prev_close
    pct_change = (change / prev_close) * 100

    # 顯示漂亮的數字看板
    col1, col2, col3 = st.columns(3)
    col1.metric("目前股價", f"{last_close:.2f}", f"{pct_change:.2f}%")
    col1.markdown(f"**日期**: {df.index[-1].strftime('%Y-%m-%d')}")
    
    # --- 5. 繪製互動式 K 線圖 (Plotly) ---
    st.subheader(f"{stock_id} 股價走勢圖")
    
    fig = go.Figure()

    # 畫 K 線 (蠟燭圖)
    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df['Open'], high=df['High'],
        low=df['Low'], close=df['Close'],
        name='K線'
    ))

    # 畫均線
    fig.add_trace(go.Scatter(x=df.index, y=df[f'MA_{ma_short}'], 
                             line=dict(color='orange', width=1.5), name=f'MA {ma_short}'))
    fig.add_trace(go.Scatter(x=df.index, y=df[f'MA_{ma_long}'], 
                             line=dict(color='blue', width=1.5), name=f'MA {ma_long}'))

    # 設定圖表版面
    fig.update_layout(height=600, xaxis_rangeslider_visible=False)
    
    # 將圖表顯示在網頁上
    st.plotly_chart(fig, width=True)

    # --- 6. 顯示原始資料 (可勾選是否顯示) ---
    if st.checkbox("顯示原始數據表格"):
        st.dataframe(df.sort_index(ascending=False))

except Exception as e:
    st.error(f"發生錯誤，請檢查股票代號是否正確。錯誤訊息: {e}")