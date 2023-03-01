import time
import datetime

print("每05秒打印一字")

import time
a = 0;
while a < 3:
    a += 1;
    print("hello " + str(a))
    time.sleep(0.5)


print("打印現在時間")
from datetime import datetime
now = datetime.today()
print(now)


import time
start = time.time()

time1 = time.gmtime(28800)
time2 = time.gmtime()

print(time1)
print(time2)

time3 = time.localtime(1234)
time4 = time.localtime()

print(time3)
print(time4)

time5 = time.asctime()

print(time5)

time6 = time.ctime()
time7 = time.ctime(time.time())

print(time6)
print(time7)

print("打印現在時間")
localtime = time.strftime("%Y/%m/%d %A %H:%M:%S", time.localtime(time.time()))
print("現在是: ", localtime)


stop = time.time()

diff = stop - start

print("使用時間 " + str(diff) + " 秒")


import calendar

print("獲取某個月的日曆，返回字串型別")
cal = calendar.month(2023, 3)
print(cal)
calendar.setfirstweekday(calendar.SUNDAY) # 設定日曆的第一天
cal = calendar.month(2023, 3)
print(cal)

print("獲取一年的日曆")
cal = calendar.calendar(2023)
print(cal)


print("獲取此時的時間");
print(time.localtime())


#取得tick數
ticks = time.time()
print("從1/1/1970 12:00:00至今的 tick數 : ", ticks)


#!/usr/bin/python
import time;  # This is required to include time module.



print("獲取當前時間");
localtime = time.localtime(time.time())
print("Local current time :", localtime)


print("獲取格式化的時間");
localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)

print("獲取日曆月份 2023/3");
import calendar
cal = calendar.month(2023, 3)
print(cal)


#import datetime
from datetime import *
#from dateutil.relativedelta import *

NOW = datetime.now()
TODAY = date.today()

print(NOW)
print(TODAY)

#how old is john
johnbirthday = datetime(1978, 4, 5, 12, 0)
#relativedelta(NOW, johnbirthday)

#print(relativedelta(NOW, johnbirthday))


#python template
import time
import datetime

a = datetime.datetime(2012,3,1)
b = datetime.datetime(2012,2,28)

print(a - b)
print("兩者時間差" , a - b)

a = datetime.datetime(2012,3,1,10,5,30)
b = datetime.datetime(2012,2,28,12,34,56)

print(a - b)
print("兩者時間差" , a - b)


a = datetime.datetime(2006,3,11,9,15,30)
b = datetime.datetime.now

#print(a - b)
#print("兩者時間差" , a - b)

print(datetime.datetime.now())

d = datetime.datetime.now()
#print("現在時間" , d)
#print("過去時間" , a)









