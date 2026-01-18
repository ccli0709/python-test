import pandas as pd
import numpy as np

# 建立一個有缺漏的銷售表
data = {
    'drink': ['珍珠奶茶', '紅茶拿鐵', '四季春', '珍珠奶茶', '水果茶'],
    'sugar': ['半糖', '微糖', None, '全糖', np.nan],
    'price': [55, 60, 35, 55, None]
}
# 轉成 Pandas 的表格 (DataFrame)
df = pd.DataFrame(data)


print("--- 原始資料 (有 NaN) ---")
print(df)
print("-" * 30)


# 2. 處理甜度：用「半糖」填補漏洞
df['sugar'] = df['sugar'].fillna('半糖')

# 3. 處理價格：先算出平均值，再填進去
mean_price = df['price'].mean()
print(f"計算出的平均價格: {mean_price}")

# 關鍵步驟：把平均價格填入 price 欄位的空缺中
df['price'] = df['price'].fillna(mean_price)

print("-" * 30)
print("--- 清洗後資料 (乾淨！) ---")
print(df)