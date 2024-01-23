from datetime import date, timedelta

tody = date.today() # 今天日期
yr, mt, dt = eval(input('請輸入出生的年、月、日->'))

# 某人生日
birth = date(yr, mt, dt)
ageDays = tody - birth


print(f'天數：{ageDays.days:,}天')
age = ageDays/timedelta(days = 365)   # 年齡
print(f'年齡 {age:.2f}')
