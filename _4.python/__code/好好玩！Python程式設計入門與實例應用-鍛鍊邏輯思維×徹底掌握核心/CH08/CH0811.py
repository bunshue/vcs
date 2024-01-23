from datetime import datetime, timedelta

# 設兩個時間
d1 = timedelta(days = 4, hours = 5)
d2 = timedelta(hours = 2.8)

#將兩個時間相加
dtAdd = d1 + d2    
print(f'共{dtAdd.days}天')
print(f'   7.8時 = {dtAdd.seconds:7,}')
print(f'4天7.8時 = {dtAdd.total_seconds():9,} 秒')
