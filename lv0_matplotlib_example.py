import statistics # 匯入統計模組
import matplotlib.pyplot as plt

# 設定中文字體，解決中文顯示問題
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial Unicode MS']  # 設定字體
plt.rcParams['axes.unicode_minus'] = False  # 解決負號顯示問題

scores = [40, 55, 60, 65, 70, 70, 75, 75, 80, 80, 
          85, 85, 90, 95, 95, 100, 60, 45, 80, 75]

# 指定我們想要的邊界：從 40 到 100，每 10 分切一刀
my_bins = [40, 50, 60, 70, 80, 90, 100]

# 畫直方圖的主角：hist
plt.hist(scores, bins=my_bins, edgecolor='black')
plt.show()