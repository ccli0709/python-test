import statistics # 匯入統計模組

money = [100, 100, 100, 200, 9500]

# 算平均數 (Mean)
mean_val = statistics.mean(money)
print("平均數:", mean_val)

# 算中位數 (Median)
median_val = statistics.median(money)
print("中位數:", median_val)


money2 = [100, 100, 100, 150, 200, 9500]

# 算中位數2 (Median)
median_val2 = statistics.median(money2)
print("中位數2:", median_val2)

# 計算標準差
stdev_val = statistics.stdev(money)

# 為了方便閱讀，我們通常會取小數點後兩位
print(f"標準差: {stdev_val:.2f}")
