# python import module : time, datetime, calendar

import time
import datetime

print("測試兩事件所經歷的時間 ST")
time_start = time.time()

print("每0.3秒打印一字")
a = 0;
while a < 3:
    a += 1;
    print("hello " + str(a))
    time.sleep(0.3)

def countdown(n):
    while n > 0:
        print('數字 : ', n)
        n -= 1
        time.sleep(0.3)

print("倒數計時")
countdown(5)
 


print("打印現在時間")
from datetime import datetime
now = datetime.today()
print(now)

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

import datetime

today = datetime.date.today()
month = int(input("請問你是在哪一個月份出生："))
day = int(input("請問你是出生日是幾號："))
birthday = datetime.date(today.year, month, day)

if birthday < today:
  birthday = datetime.date(today.year+1, month, day)

diff = birthday - today
if diff.days == 0:
  print("不會吧！今天是你的生日，祝你生日快樂！")
else:
  print("哇！再過 " + str(diff.days) + " 天就是你的生日了！")


age = int(input("你的年紀是："))
if age >= 20:
  print("請記得今年要去投票")
else:
  diff = str(20 - age)
  print("要年滿20歲才能夠投票，你還差 " + diff + " 歲")

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


# 字串轉換為時間
def strTodatetime(datestr, format):
    return datetime.datetime.strptime(datestr, format)
print(time.strftime("%Y-%m-%d", time.localtime()))
print(strTodatetime("2014-3-1","%Y-%m-%d"))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(strTodatetime("2019-4-15","%Y-%m-%d")-strTodatetime("2006-03-11","%Y-%m-%d"))




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
print(str(d3) )
print(d3.ctime())
#print(time.ctime([sec]))#把秒數轉換成日期格式，如果不帶引數，則顯示當前的時間。
#time.ctime([ sec ])
print("time.ctime() : %s" % time.ctime())




import calendar
print(calendar.__file__)

print("獲取某個月的日曆，返回字串型別")
cal = calendar.month(2023, 3)
print(cal)
calendar.setfirstweekday(calendar.SUNDAY) # 設定日曆的第一天

print("獲取日曆月份 2023/3");
cal = calendar.month(2023, 3)
print(cal)

print("獲取一年的日曆")
cal = calendar.calendar(2023)
print(cal)

time_stop = time.time() - time_start
print("測試兩事件所經歷的時間 SP, 經歷時間 : "+str(time_stop) + " 秒")
















