# encoding:UTF-8
from datetime import datetime

a = input('請輸入你的出生年月日 ( yyyy/mm/dd )：')
now = datetime.now()
ad = datetime.strptime(a, '%Y/%m/%d')
y = now.year - ad.year
m = now.month - ad.month
d = now.day - ad.day

print(f'你的生日是：{y} 歲 {m} 個月又 {d} 天')  # 使用 python3 語法
