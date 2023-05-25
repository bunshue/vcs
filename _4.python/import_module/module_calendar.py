import calendar

print(calendar.__file__)

print("獲取某個月的日曆，返回字串型別")
cal = calendar.month(2023, 3)
print(cal)
calendar.setfirstweekday(calendar.SUNDAY) # 設定日曆的第一天

print("獲取日曆月份 2023/3");
cal = calendar.month(2023, 3)
print(cal)

print("獲取一年的日曆")
cal = calendar.calendar(2023)
print(cal)



'''
import calendar

date = '%s %02d' % (calendar.month_abbr[0], dd)

print(date)
'''


datetime = calendar.datetime.datetime
print(datetime)
print(datetime.now())
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)
print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.now().second)
timedelta = calendar.datetime.timedelta
print(timedelta)


import time

from email.utils import formatdate, parsedate, parsedate_tz

TIME_FMT = "%a, %d %b %Y %H:%M:%S GMT"

freshness_lifetime = max(0, min(5 / 10, 24 * 3600))
expires = freshness_lifetime

print("expires", time.strftime(TIME_FMT, time.gmtime(expires)))




import calendar
calendar.setfirstweekday(calendar.MONDAY)

print(calendar.isleap(2024))

print(calendar.firstweekday())

year = 2023
month = 5
day = 3
calendar.weekday(year, month, day)


calendar.monthrange(year, month)

print(calendar.monthcalendar(year, month))


print(calendar.calendar(year, w=2, l=1, c=6, m=3))

for i in range(1,13):
    print(calendar.month_name[i])


weeks = calendar.monthcalendar(year, month)
print(weeks)



