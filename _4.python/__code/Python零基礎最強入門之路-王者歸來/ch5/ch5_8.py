# ch5_8.py
print("判斷輸入年份是否潤年")
year = input("請輸入年分: ")
rem4 = int(year) % 4
rem100 = int(year) % 100
rem400 = int(year) % 400
if rem4 == 0:
    if rem100 != 0 or rem400 == 0:
        print("%s 是潤年" % year)
    else:
        print("%s 不是潤年" % year)
else:
    print("%s 不是潤年" % year)
