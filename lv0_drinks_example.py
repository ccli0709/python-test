import statistics # 匯入統計模組

# 飲料品項
drinks = ['珍珠奶茶', '紅茶拿鐵', '珍珠奶茶', '四季春', '珍珠奶茶', 
          '紅茶拿鐵', '四季春', '珍珠奶茶', '四季春', '紅茶拿鐵']

# 銷售價格 (對應上面的每一杯)
prices = [55, 60, 55, 35, 55, 60, 35, 55, 35, 60]

# 甜度選擇
sugars = ['半糖', '微糖', '全糖', '無糖', '半糖', 
          '半糖', '無糖', '微糖', '無糖', '微糖']

# 平日銷量(杯數)
weekday_sales = [40, 55, 60, 45, 50]

# 週末銷量(杯數)
weekend_sales = [70, 75]
        


prices_sum = statistics.fsum(prices)
print("總銷售額:", prices_sum)

# drinks_mode = statistics.mode(drinks)
drinks_mode = statistics.multimode(drinks)
print("賣最好的:", drinks_mode)


weekday_sales_mean = statistics.mean(weekday_sales)
print("平日每日平均售出杯數:", weekday_sales_mean)

weekend_sales_mean = statistics.mean(weekend_sales)
print("假日每日平均售出杯數:", weekend_sales_mean)
