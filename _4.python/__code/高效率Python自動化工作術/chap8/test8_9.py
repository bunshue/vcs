import calendar
year = 2022
month = 12
cal = calendar.Calendar(calendar.SUNDAY)
for (row, week) in enumerate(cal.monthdayscalendar(year, month)):
    for (col, day) in enumerate(week):
        if day > 0 :
            print("第",row+1,"列","第",col+1,"欄=", day)
