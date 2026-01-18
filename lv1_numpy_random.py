import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 設定中文字體，解決中文顯示問題
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']  # 設定字體
plt.rcParams['axes.unicode_minus'] = False  # 解決負號顯示問題

# 設定隨機亂數種子 (讓每次跑出來結果一樣，方便教學)
np.random.seed(42)

# 模擬 100 天的數據
days = 100

# 1. 模擬「大盤」每日報酬率 (平均 0%，波動 1%)
market_returns = np.random.normal(0, 1, days)

# 2. 模擬「台積電」每日報酬率
# 假設台積電跟大盤連動性很高 (Beta 設為 1.2)，再加上一些個股特有的波動 (Noise)
stock_returns = 1.2 * market_returns + np.random.normal(0, 0.5, days)

# 把它整理成漂亮的 Pandas 表格
df = pd.DataFrame({
    'Market_Ret': market_returns, # 大盤
    'Stock_Ret': stock_returns    # 個股
})

print("--- 前 5 天的每日報酬率 (%) ---")
print(df.head())
print(df.std())



# 畫直方圖的主角：hist
plt.title('大盤每日報酬率 vs 個股每日報酬率')
plt.plot(market_returns, label='大盤每日報酬率')
plt.plot(stock_returns, label='個股每日報酬率')
plt.legend()
plt.show()