# python import module : time, datetime, calendar

import time
from time import sleep
#from time import sleep_ms

print("測試兩事件所經歷的時間 ST")
time_start = time.time()

print("每0.3秒打印一字")
a = 0;
while a < 3:
    a += 1;
    print("hello " + str(a))
    time.sleep(0.3)
    sleep(0.1)
    #sleep_ms(100)

def countdown(n):
    while n > 0:
        print('數字 : ', n)
        n -= 1
        time.sleep(0.3)

print("倒數計時")
countdown(5)
 

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


print('----- localtime -----------------------------------------------------------------')	#70個

print("打印現在時間")
localtime = time.strftime("%Y/%m/%d %A %H:%M:%S", time.localtime(time.time()))
print("現在是: ", localtime)

print("獲取此時的時間");
print(time.localtime())

print("獲取當前時間");
localtime = time.localtime(time.time())
print("Local current time :", localtime)


print("獲取格式化的時間");
localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)



import time
import datetime

# 字串轉換為時間
def strTodatetime(datestr, format):
    return datetime.datetime.strptime(datestr, format)
print(time.strftime("%Y-%m-%d", time.localtime()))
print(strTodatetime("2014-3-1", "%Y-%m-%d"))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(strTodatetime("2019-4-15","%Y-%m-%d") - strTodatetime("2006-03-11","%Y-%m-%d"))



stop = time.time()
diff = stop - start
print("使用時間 " + str(diff) + " 秒")


#取得tick數
ticks = time.time()
print("從1/1/1970 12:00:00至今的 tick數 : ", ticks)


#!/usr/bin/python
import time;  # This is required to include time module.



import time
t = time.localtime()
print(t)
print("年" , t.tm_year)
print("月" , t.tm_mon)
print("日" , t.tm_mday)
print("星" , t.tm_wday)
print("時" , t.tm_hour)
print("分" , t.tm_min)
print("秒" , t.tm_sec)

#age = int(input("你的年紀是："))
age = 25
if age >= 20:
  print("請記得今年要去投票")
else:
  diff = str(20 - age)
  print("要年滿20歲才能夠投票，你還差 " + diff + " 歲")



time.localtime() #可以輸出 struct_time 的時間格式

import time  # 引入 time 模組

localtime = time.localtime() # 取得當前時間
print(localtime)


import time  # 引入 time 模組

localtime = time.localtime() # 取得當前時間
print("年:", localtime.tm_year)
print("月:", localtime.tm_mon)
print("日:", localtime.tm_mday)
print("時:", localtime.tm_hour)
print("分:", localtime.tm_min)
print("秒:", localtime.tm_sec)
print("星期(0為星期一):", localtime.tm_wday)
print("今天為今年第幾天:", localtime.tm_yday)
print("夏令時間(0為不是，1為是):", localtime.tm_isdst)


#strftime() 可以將時間格式化


import time

# 格式化為 2020-09-26 21:14:30
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化為Sat Sep 26 21:14:30 2020
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))






import time
def get_time():
    return time.strftime("%Y/%m/%d %A %H:%M:%S", time.localtime(time.time()))

localtime = get_time()
print('現在時間 : ' + localtime)


import time
print("現在時間")
localtime = time.strftime("%Y/%m/%d %A %H:%M:%S", time.localtime(time.time()))
print('現在時間 : ' + localtime)



time_stop = time.time() - time_start
print("測試兩事件所經歷的時間 SP, 經歷時間 : "+str(time_stop) + " 秒")

import time

currentTime = time.time() # Get current time

# Obtain the total seconds since midnight, Jan 1, 1970
totalSeconds = int(currentTime)

# Get the current second 
currentSecond = totalSeconds % 60 

# Obtain the total minutes
totalMinutes = totalSeconds // 60 

# Compute the current minute in the hour
currentMinute = totalMinutes % 60

# Obtain the total hours
totalHours = totalMinutes // 60

# Compute the current hour
currentHour = totalHours % 24

# Display results
print("Current time is " + str(currentHour) + ":"
    + str(currentMinute) + ":" + str(currentSecond) + " GMT")
    




# python import module : datetime

import datetime

#取得查詢當年年份及上個月月份
now_date = datetime.datetime.now() # 取得查詢當下的時間
now_year = now_date.year # 取得查詢當下當年年份

# 取得查詢當下上個月月份
if(now_date.month != 1):
    last_month = now_date.month - 1
else:
    last_month = 12

print("now_year = " + str(now_year))
print("last_month = " + str(last_month))



print("打印現在時間")
from datetime import datetime
now = datetime.today()
print(now)

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




print('----- timediff -----------------------------------------------------------------')	#70個

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

import datetime

today = datetime.date.today()
#month = int(input("請問你是在哪一個月份出生："))
month = 3
#day = int(input("請問你是出生日是幾號："))
day = 11
birthday = datetime.date(today.year, month, day)

if birthday < today:
  birthday = datetime.date(today.year+1, month, day)

diff = birthday - today
if diff.days == 0:
  print("不會吧！今天是你的生日，祝你生日快樂！")
else:
  print("哇！再過 " + str(diff.days) + " 天就是你的生日了！")


print("獲取昨天的日期");
def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    #print(type(today))  # 檢視獲取到時間的型別
    #print(type(yesterday))
    return yesterday
yesterday = getYesterday()
print("昨天的時間：", yesterday)

print("獲取當天的日期");
#print(datetime.datetime.now()) fail
#print(datetime.date.today())   fail

#兩日期相減 
d1 = datetime.datetime(2005, 2, 16)
d2 = datetime.datetime(2004, 12, 31)
print((d1 - d2).days)
#執行時間： 
starttime = datetime.datetime.now()
endtime = datetime.datetime.now()
print((endtime - starttime).seconds)
#計算當前時間向後10天的時間。
# 如果是小時 days 換成 hours
d1 = datetime.datetime.now()
d3 = d1 - datetime.timedelta(days =10)
print(str(d3))
print(d3.ctime())
#print(time.ctime([sec]))#把秒數轉換成日期格式，如果不帶引數，則顯示當前的時間。
#time.ctime([ sec ])
print("time.ctime() : %s" % time.ctime())




print('----- datetime.now() -----------------------------------------------------------------')	#70個

import datetime as dt

now = dt.datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%Y-%m-%d, %H:%M:%S")
print("date and time:",date_time)


from datetime import datetime

tt = datetime.strptime("2018-01-31", "%Y-%m-%d")
print(tt)


from datetime import datetime

dateString = "7-May-2018"
dateFormatter = "%u-%b-%Y"
tt = datetime.strptime(dateString, dateFormatter)
print(tt)


from datetime import datetime

dateString = "31/12/2013"
dateFormatter = "%d/%m/%Y"
tt = datetime.strptime(dateString, dateFormatter)
print(tt)


from datetime import datetime

dateString = "31/12/2013"
dateFormatter = "%d/%m/%Y"
tt = datetime.strptime(dateString, dateFormatter)
print(tt)

from datetime import datetime

dateString = "Monday, July 16, 2018 20:01:56"
dateFormatter = "%A, %B %d, %Y %H:%M:%S"
tt = datetime.strptime(dateString, dateFormatter)
print(tt)



# 日期時間操作 

import time  # 導入 time 模組

time.time()#通常是用來作為時間戳記，可以傳回從 1970/1/1 00:00:00 算起至今的秒數

import time # 引入 time 模組

seconds = time.time()
print(seconds)




import datetime

now1 = datetime.datetime.now()
now2 = datetime.datetime.now().date()

new_date = now2 + datetime.timedelta(-1)    #昨天

print(now1)
print(now2)
print(new_date)
print(now2.year)
print(now2.month)
print(now2.day)

print('字串轉日期格式')
date1 = '2023-03-11'
print(date1)
date2 = datetime.datetime.strptime(date1, "%Y-%m-%d").date()
print(date2)
print(date2.year)
print(date2.month)
print(date2.day)

date3 = datetime.datetime.now()
mesg = "{} {}:{}:{}".format(date3, date3.hour, date3.minute, date3.second)
print(mesg)

print('字串轉日期格式')
date4 = '2023-04-07 15:41:26'
date5 = datetime.datetime.strptime(date4, "%Y-%m-%d %H:%M:%S")
print(date5)


import time

startTime = time.time() # Get start time

#do something
#do something
#do something

endTime = time.time() # Get end time
testTime = int(endTime - startTime) # Get test time
print("Test time is", testTime, "seconds")


import time
version = time.strftime("-%Y%m%d")
print(version)






import datetime

def transform_date(date): #轉換日期
    y, m, d, h = date[:4],date[5:7],date[8:10],date[11:13]
    return y + '/' + m  + '/' + d  + '/' + h  

old_date = datetime.datetime.now() # 取得現在時間

old_date = str(old_date)    #先轉成字串

#old_date = '2023/05/24 13:00:00' ex

print(old_date)

new_date = transform_date(old_date)

print(new_date)

print('----- new -----------------------------------------------------------------')	#70個


string = ("%d" % datetime.datetime.now().year)
print(string)

now = datetime.datetime.now()
filename = now.strftime("news-%y-%m-%d-%H-%M-%S.json")
print(filename)

string = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(string)







