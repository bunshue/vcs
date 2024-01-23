import calendar
year = 2022
month = 12
cal = calendar.Calendar()
for week in cal.monthdayscalendar(year, month):
    print(week)
