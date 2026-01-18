import matplotlib.pyplot as plt
import numpy as np

# 設定中文字體，解決中文顯示問題
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']  # 設定字體
plt.rcParams['axes.unicode_minus'] = False  # 解決負號顯示問題

hours = [1, 2, 2.5, 3, 5, 6, 7.5, 8]
scores = [40, 50, 55, 60, 75, 80, 85, 95]

# 計算迴歸線 (Linear Regression)
# polyfit(x, y, 1) 代表我們要找一次方程式 (y = ax + b)
coefficients = np.polyfit(hours, scores, 1)
polynomial = np.poly1d(coefficients)
y_trend = polynomial(hours)

# 預測 4 小時的分數
predicted_score_4h = polynomial(4)

plt.figure(figsize=(8, 5))
plt.scatter(hours, scores, color='royalblue', s=100, label='實際資料')
plt.plot(hours, y_trend, color='red', linewidth=2, linestyle='--', label='趨勢線 (迴歸)')

# 標記預測點
plt.scatter([4], [predicted_score_4h], color='orange', s=150, zorder=5, marker='*', label=f'預測 (4小時): {predicted_score_4h:.1f}')

plt.title('讀書時數 vs 考試分數 with 趨勢線')
plt.xlabel('讀書時數')
plt.ylabel('考試分數')
plt.legend()
plt.grid(True, alpha=0.6)
plt.show()
plt.savefig('regression_study_scores.png')


print(f"預測 4 小時的分數: {predicted_score_4h}")
print(f"方程式: y = {coefficients[0]:.2f}x + {coefficients[1]:.2f}")

