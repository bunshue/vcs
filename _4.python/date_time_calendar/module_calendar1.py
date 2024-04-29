import calendar

print('------------------------------------------------------------')	#60個

import os
import sys
import time
import locale
import datetime

print(calendar.__file__)

print('印出月的英文名')
for i in range(1,13):
    print(calendar.month_name[i])

year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day

print("日期 :", year, "年", month, "月", day,"日")

print('------------------------------------------------------------')	#60個

#簡單固定的用法

print("年曆")
cc = calendar.calendar(year)
print(cc)

"""
print(calendar.calendar(year, w=2, l=1, c=6, m=3)) #有無參數看不出差異
"""

print("年曆")
print('5 TextCalendar')
print(calendar.TextCalendar().formatyear(year))
def shrink(cal):
    return [[[' '.join('{:02d}/{:02d}/{}'.format(
        d.month, d.day, str(d.year)[-2:]) for d in z)
              for z in y] for y in x] for x in cal]

print("年曆")
print(calendar.Calendar().yeardayscalendar(year))

print("月曆")
cc = calendar.month(year, month)
print(cc)

print('4 TextCalendar')
print(calendar.TextCalendar().formatmonth(year, month))

print('------------------------------------------------------------')	#60個

#設定星期一為日曆的第一天
calendar.setfirstweekday(calendar.MONDAY) # 設定日曆的第一天

print(calendar.__file__)

print("2021年是否潤年", calendar.isleap(2021))
print("2024年是否潤年", calendar.isleap(2024))

print('------------------------------------------------------------')	#60個

"""
date = '%s %02d' % (calendar.month_abbr[0], dd)
print(date)
"""

dt = calendar.datetime.datetime
print(dt)
print(dt.now())
print(dt.now().year)
print(dt.now().month)
print(dt.now().day)
print(dt.now().hour)
print(dt.now().minute)
print(dt.now().second)
timedelta = calendar.datetime.timedelta
print(timedelta)

""" TBD
dt = calendar.datetime.datetime
print(calendar.timegm(time.strptime(dt, '%a %b %d %H:%M:%S %Y')))
print(calendar.timegm(time.strptime(dt, '%a %b %d %H:%M:%S %Y')))

#date = '%s %02d' % (calendar.month_abbr[mm], dd)

maybe_date = calendar.datetime.datetime
cc = calendar.timegm(time.strptime(maybe_date, '%a %b %d %H:%M:%S %Y'))
"""

print('------------------------------------------------------------')	#60個

print(calendar.firstweekday())

calendar.weekday(year, month, day)

calendar.monthrange(year, month)

print(calendar.monthcalendar(year, month))

weeks = calendar.monthcalendar(year, month)
#print(weeks)
#每一週的日期
for _ in weeks:
    print(_)

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

cal = calendar.monthcalendar(year, month)
print(type(cal))
print(cal)

#calendar.setfirstweekday(1)
print('firstweekday = ', calendar.firstweekday())

#  list(calendar.Calendar().itermonthdates(datetime.MAXYEAR, 12))

print("年曆")
print(calendar.Calendar().yeardatescalendar(year))

print(calendar.TextCalendar().formatmonthname(year, month, day))
print(calendar.LocaleHTMLCalendar(locale=''))
#print(cal.formatweekday(1))
#print(cal.formatmonthname(year, month))
print(calendar.TextCalendar().formatmonthname(year, month, day))

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

day_start, num_days = calendar.monthrange(year, month)
    
print('本月的第一天為星期 :', day_start)
print('本月的天數 :', num_days)

print('------------------------------------------------------------')	#60個

print("年曆")
cal = calendar.Calendar()
for week in cal.monthdayscalendar(year, month):
    print(week)

print('------------------------------------------------------------')	#60個

print("年曆")
print(str(year)+"年"+str(month)+"月")
dayname = ["日","一","二","三","四","五","六"]
print(dayname)
cal = calendar.Calendar(calendar.SUNDAY)
for week in cal.monthdayscalendar(year, month):
    print(week)

print('------------------------------------------------------------')	#60個

"""
print("年曆")
cal = calendar.Calendar(calendar.SUNDAY)
for (row, week) in enumerate(cal.monthdayscalendar(year, month)):
    for (col, day) in enumerate(week):
        if day > 0 :
            print("第",row+1,"列","第",col+1,"欄=", day)
"""
print('------------------------------------------------------------')	#60個

print('2 TextCalendar')
print(calendar.TextCalendar().formatweekheader(2))
print('3 TextCalendar')
print(calendar.TextCalendar().formatweekheader(9))
""" many
print('6')
print(shrink(calendar.Calendar().yeardatescalendar(year)))
"""

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個



"""

        a_weekday = [calendar.day_abbr[i].lower() for i in range(7)]
        f_weekday = [calendar.day_name[i].lower() for i in range(7)]


    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)
"""

print('--------------------')

print("年曆")
cal = calendar.Calendar(calendar.SUNDAY)
print(cal)

import datetime

today = datetime.date.today()
#birthday = input("輸入生日 ( YYYY/MM/DD )：")
birthday = '2006/03/11'
birthday_list = birthday.split("/")
year = today.year - int(birthday_list[0])
month = today.month - int(birthday_list[1])
if month < 0:
    year = year - 1
    month = 12 + month
day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if calendar.isleap(today.year):  # 判斷如果是閏年
    day_list[1] = 29  # 就將二月份的天數改成 29 天
day = today.day - int(birthday_list[2])
if day < 0:
    month = month - 1
    if month < 0:
        year = year - 1
        month = 12 + month
    day = day_list[month] + day

print(f"{year} 歲 {month} 個月 {day} 天")


print("------------------------------------------------------------")  # 60個


