import calendar

import time
import locale
import sys
import datetime
import os


TIMESTAMPS = [0, 10, 100, 1000, 10000, 100000, 1000000, 1234567890, 1262304000, 1275785153,]
def test_timegm():
    for secs in TIMESTAMPS:
        tuple = time.gmtime(secs)
        #assertEqual(secs, calendar.timegm(tuple))
        print(secs, calendar.timegm(tuple))

test_timegm()

lang, enc = locale.getdefaultlocale()
print(lang, enc)

'''
lang, enc = locale.getdefaultlocale()
oldlocale = locale.getlocale(locale.LC_TIME)
locale.setlocale(locale.LC_TIME, (lang, enc))
locale.setlocale(locale.LC_TIME, oldlocale)
'''

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


'''
        orig = calendar.firstweekday()
        calendar.setfirstweekday(calendar.SUNDAY)
        self.assertEqual(calendar.firstweekday(), calendar.SUNDAY)
        calendar.setfirstweekday(calendar.MONDAY)
        self.assertEqual(calendar.firstweekday(), calendar.MONDAY)
        calendar.setfirstweekday(orig)


            calendar.setfirstweekday(123)

'''

