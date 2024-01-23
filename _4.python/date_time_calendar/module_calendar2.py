import calendar

print('------------------------------------------------------------')	#60個


import calendar
print(calendar.month(2022, 12))

print('------------------------------------------------------------')	#60個


import calendar
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(2022, 12))

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

import calendar
year = 2022
month = 12
cal = calendar.Calendar(calendar.SUNDAY)
for (row, week) in enumerate(cal.monthdayscalendar(year, month)):
    for (col, day) in enumerate(week):
        if day > 0 :
            print("第",row+1,"列","第",col+1,"欄=", day)

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個
