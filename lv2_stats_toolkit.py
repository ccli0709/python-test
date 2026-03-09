import numpy as np
import pandas as pd
import scipy.stats as stats

# 設定亂數種子
np.random.seed(42)

# 1. 產生模擬資料 (假設這是某基金 1000 天的報酬率 %)
# 我們故意混入一些 "極端值" (outliers)，讓資料稍微 "歪" 一點
normal_data = np.random.normal(0, 1, 1000)   # 常態分佈
outliers = np.random.uniform(0, 1, 20)      # 加入 20 個大賺的極端值
data = np.concatenate([normal_data, outliers])

# 轉成 DataFrame 比較好處理
df = pd.DataFrame(data, columns=['Returns'])
print(df)

# --- 實作開始 ---

# A. 集中趨勢 (Central Tendency)
mean_val = df['Returns'].mean()   # 平均數
median_val = df['Returns'].median()  # 中位數
mode_val = stats.mode(data, keepdims=True)[0][0]  # 眾數 (數值型資料通常較少用，除非有重複)

# B. 離散程度 (Dispersion)
std_val = df['Returns'].std()       # 標準差 (波動率)
var_val = df['Returns'].var()       # 變異數
range_val = df['Returns'].max() - df['Returns'].min()  # 全距

# C. 分佈形狀 (Shape) - 財務分析超重要！
# 偏態 (Skewness): >0 代表右偏(這組資料大賺的日子比較多)，<0 代表左偏
skew_val = df['Returns'].skew()
# 峰態 (Kurtosis): >3 代表 "肥尾" (Fat Tail)，極端事件發生的機率比常態分佈高
kurt_val = df['Returns'].kurtosis() 

# D. 假設檢定 (Hypothesis Testing) - T檢定
# 假設我們要檢定：這檔基金的平均報酬率是否 "顯著大於 0"？
# H0: 平均數 = 0
# H1: 平均數 != 0
t_stat, p_value = stats.ttest_1samp(df['Returns'], 0)


# --- 輸出報告 ---
print(f"--- A. 集中趨勢 ---")
print(f"平均數 (Mean): {mean_val:.4f}")
print(f"中位數 (Median): {median_val:.4f}")
print(f"差異: {mean_val - median_val:.4f} (平均數被極端值拉高了)")

print(f"\n--- B. 離散程度 ---")
print(f"標準差 (Std Dev): {std_val:.4f}")
print(f"全距 (Range): {range_val:.4f}")

print(f"\n--- C. 分佈形狀 ---")
print(f"偏態 (Skewness): {skew_val:.4f} (正值代表右尾比較長，有大賺的極端值)")
print(f"峰態 (Kurtosis): {kurt_val:.4f} (越高代表極端值越多)")

print(f"\n--- D. 假設檢定 (T-test) ---")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4e}")
if p_value < 0.05:
    print("結論: 拒絕虛無假設 (顯著！平均報酬率真的不等於 0)")
else:
    print("結論: 無法拒絕虛無假設 (結果可能是運氣)")