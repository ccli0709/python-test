import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


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
df = pd.DataFrame(
    {
        "Market_Ret": market_returns,  # 大盤
        "Stock_Ret": stock_returns,  # 個股
    }
)

print("--- 前 5 天的每日報酬率 (%) ---")
print(df.head())
print(df.std())

# X 是大盤 (自變數)，Y 是個股 (應變數)
x = df["Market_Ret"]
y = df["Stock_Ret"]

# 執行線性迴歸
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

print(f"Beta (斜率): {slope:.4f}")
print(f"Alpha (截距): {intercept:.4f}")
print(f"R-squared (解釋力): {r_value**2:.4f}")

# 繪圖
plt.figure(figsize=(8, 6))
plt.scatter(market_returns, stock_returns, alpha=0.6, label="Daily Returns")


# 畫出迴歸線 (SCL)
x_seq = np.linspace(min(market_returns), max(market_returns), 100)
y_seq = intercept + slope * x_seq
plt.plot(x_seq, y_seq, color="red", linewidth=2, label=f"SCL (Beta={slope:.2f})")

plt.axhline(0, color="gray", linestyle="--", alpha=0.5)
plt.axvline(0, color="gray", linestyle="--", alpha=0.5)
plt.title(
    f"Security Characteristic Line (Beta = {slope:.2f})(R-squared: {r_value**2:.4f})"
)
plt.xlabel("Market Return (%)")
plt.ylabel("Stock Return (%)")
plt.legend()
plt.grid(True, alpha=0.3)

plt.show()
