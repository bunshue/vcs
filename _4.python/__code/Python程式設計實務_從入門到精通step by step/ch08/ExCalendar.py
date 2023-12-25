import calendar

y = int(input("請輸入年份:"))
m = int(input("請輸入月份:"))
ys = int(input("列印n年內為閏年的月曆:"))
notLeap = []

calendar.setfirstweekday(calendar.SUNDAY)

for i in range(ys):
    if calendar.isleap(y+i) == True:
        print("\n")
        calendar.prmonth(y+i, m)
    else:
        notLeap.append(y+i)

print("\n以下非閏年:", notLeap)
print("{}到{}期間有幾個閏年:{}".format(y, y+ys, calendar.leapdays(y, y+ys)))
