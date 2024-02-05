import sys
import calendar

print('------------------------------------------------------------')	#60個

#設定星期一為日曆的第一天
calendar.setfirstweekday(calendar.MONDAY) # 設定日曆的第一天

print(calendar.__file__)

print("2021年是否潤年", calendar.isleap(2021))
print("2024年是否潤年", calendar.isleap(2024))

print('------------------------------------------------------------')	#60個

print("年曆")
year = 2024
cc = calendar.calendar(year)
print(cc)

print("月曆")
year = 2024
month = 2
cc = calendar.month(year, month)
print(cc)

print("------------------------------------------------------------")  # 60個


"""
date = '%s %02d' % (calendar.month_abbr[0], dd)
print(date)
"""


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

print('------------------------------------------------------------')	#60個

import time

from email.utils import formatdate, parsedate, parsedate_tz

TIME_FMT = "%a, %d %b %Y %H:%M:%S GMT"

freshness_lifetime = max(0, min(5 / 10, 24 * 3600))
expires = freshness_lifetime

print("expires", time.strftime(TIME_FMT, time.gmtime(expires)))


print('------------------------------------------------------------')	#60個


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

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


import calendar

import time
import locale
import sys
import datetime
import os

print('------------------------------------------------------------')	#60個

TIMESTAMPS = [0, 10, 100, 1000, 10000, 100000, 1000000, 1234567890, 1262304000, 1275785153,]
def test_timegm():
    for secs in TIMESTAMPS:
        tuple = time.gmtime(secs)
        #assertEqual(secs, calendar.timegm(tuple))
        print(secs, calendar.timegm(tuple))

test_timegm()

lang, enc = locale.getdefaultlocale()
print(lang, enc)

print('------------------------------------------------------------')	#60個

"""
lang, enc = locale.getdefaultlocale()
oldlocale = locale.getlocale(locale.LC_TIME)
locale.setlocale(locale.LC_TIME, (lang, enc))
locale.setlocale(locale.LC_TIME, oldlocale)
"""

year = datetime.datetime.now().year

year = 2023
month = 8
cal = calendar.monthcalendar(year, month)
print(type(cal))
print(cal)

#calendar.setfirstweekday(1)
print('firstweekday = ', calendar.firstweekday())

#  list(calendar.Calendar().itermonthdates(datetime.MAXYEAR, 12))

print(calendar.Calendar().yeardatescalendar(2023))


print(calendar.TextCalendar().formatmonthname(2010, 10, 10))
print(calendar.LocaleHTMLCalendar(locale=''))
#print(cal.formatweekday(1))
#print(cal.formatmonthname(2010, 10))
print(calendar.TextCalendar().formatmonthname(2010, 10, 10))

print('------------------------------------------------------------')	#60個

print()
print()
print('1')
print(calendar.Calendar().yeardayscalendar(2004))
print('2 TextCalendar')
print(calendar.TextCalendar().formatweekheader(2))
print('3 TextCalendar')
print(calendar.TextCalendar().formatweekheader(9))
print('4 TextCalendar')
print(calendar.TextCalendar().formatmonth(2004, 1))

print('5 TextCalendar')
print(calendar.TextCalendar().formatyear(2004))
def shrink(cal):
    return [[[' '.join('{:02d}/{:02d}/{}'.format(
        d.month, d.day, str(d.year)[-2:]) for d in z)
              for z in y] for y in x] for x in cal]
print('6')
print(shrink(calendar.Calendar().yeardatescalendar(2004)))

print('------------------------------------------------------------')	#60個

"""
        orig = calendar.firstweekday()
        calendar.setfirstweekday(calendar.SUNDAY)
        self.assertEqual(calendar.firstweekday(), calendar.SUNDAY)
        calendar.setfirstweekday(calendar.MONDAY)
        self.assertEqual(calendar.firstweekday(), calendar.MONDAY)
        calendar.setfirstweekday(orig)


            calendar.setfirstweekday(123)

"""
print('------------------------------------------------------------')	#60個

import calendar

day_start, num_days = calendar.monthrange(2023, 10)
    
print('本月的第一天為星期 :', day_start)
print('本月的天數 :', num_days)

print('------------------------------------------------------------')	#60個

import calendar
year = 2022
month = 12
cal = calendar.Calendar()
for week in cal.monthdayscalendar(year, month):
    print(week)

print('------------------------------------------------------------')	#60個

import calendar
year = 2022
month = 12
print(str(year)+"年"+str(month)+"月")
dayname = ["日","一","二","三","四","五","六"]
print(dayname)
cal = calendar.Calendar(calendar.SUNDAY)
for week in cal.monthdayscalendar(year, month):
    print(week)

print('------------------------------------------------------------')	#60個

"""
import calendar
year = 2022
month = 12
cal = calendar.Calendar(calendar.SUNDAY)
for (row, week) in enumerate(cal.monthdayscalendar(year, month)):
    for (col, day) in enumerate(week):
        if day > 0 :
            print("第",row+1,"列","第",col+1,"欄=", day)
"""
print('------------------------------------------------------------')	#60個


