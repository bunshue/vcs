year = int(input("請輸入西元年份："))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("%d 是閏年" %year)
else :
    print("%d 是平年" %year)
