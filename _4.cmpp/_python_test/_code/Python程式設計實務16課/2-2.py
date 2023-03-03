import datetime

today = datetime.date.today()
month = int(input("請問你是在哪一個月份出生："))
day = int(input("請問你是出生日是幾號："))
birthday = datetime.date(today.year, month, day)

if birthday < today:
  birthday = datetime.date(today.year+1, month, day)

diff = birthday - today
if diff.days == 0:
  print("不會吧！今天是你的生日，祝你生日快樂！")
else:
  print("哇！再過 " + str(diff.days) + " 天就是你的生日了！")
