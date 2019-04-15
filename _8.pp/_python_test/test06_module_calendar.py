import calendar

# 獲取某個月的日曆，返回字串型別
cal = calendar.month(2019, 4)
print(cal)
calendar.setfirstweekday(calendar.SUNDAY) # 設定日曆的第一天
cal = calendar.month(2019, 4)
print(cal)
# 獲取一年的日曆
cal = calendar.calendar(2019)
print(cal)

