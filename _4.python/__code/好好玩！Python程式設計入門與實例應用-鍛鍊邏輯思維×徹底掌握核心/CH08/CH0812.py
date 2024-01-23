from datetime import datetime, timedelta

d1 = datetime(2018, 9, 2)
print('日期：', d1 + (timedelta(days = 7)))

d2 = datetime(2020, 1, 22)
d3 = timedelta(days = 106)
dt = d2 - d3 # 將兩個日期相減
print('日期二：', dt.strftime('%Y-%m-%d'))

