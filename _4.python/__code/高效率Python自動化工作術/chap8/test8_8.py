import calendar
year = 2022
month = 12
print(str(year)+"年"+str(month)+"月")
dayname = ["日","一","二","三","四","五","六"]
print(dayname)
cal = calendar.Calendar(calendar.SUNDAY)
for week in cal.monthdayscalendar(year, month):
    print(week)
    