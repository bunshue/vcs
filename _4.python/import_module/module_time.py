# python import module : time, datetime
"""
python的日期當中分成
1. date(日期)
2. time(時間)
3. datetime(混合date跟time)
4. timedelta(計算歷時期間的型態)
5. timezone(處理時區資訊的型態)

"""
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
    time.sleep(0.1)

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

print('---- 現在時間 --------------------------------------------------------')	#60個

print("現在時間")
now = datetime.datetime.today()
print(now)

print("獲取此時的時間");
print(time.localtime())

print("獲取當前時間");
localtime = time.localtime(time.time())
print("Local current time :", localtime)

print("獲取格式化的時間");
localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)

time5 = time.asctime()
print('time5 :', time5)

time6 = time.ctime()
print('time6 :', time6)

time7 = time.ctime(time.time())
print('time7 :', time7)

stop = time.time()
diff = stop - start
print("使用時間 " + str(diff) + " 秒")

#取得tick數
ticks = time.time()
print("從1/1/1970 12:00:00至今的 tick數 : ", ticks)

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

localtime = time.localtime() # 取得當前時間
print(localtime)

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

time_stop = time.time() - time_start
print("測試兩事件所經歷的時間 SP, 經歷時間 : "+str(time_stop) + " 秒")

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

NOW = datetime.datetime.now()
print(NOW)
TODAY = datetime.date.today()
print(TODAY)

#how old is john
johnbirthday = datetime.datetime(1978, 4, 5, 12, 0)
#relativedelta(NOW, johnbirthday)

#print(relativedelta(NOW, johnbirthday))

print('---- timediff --------------------------------------------------------')	#60個

a = datetime.datetime(2012, 3, 1)
b = datetime.datetime(2012, 2, 28)

print(a - b)
print("兩者時間差" , a - b)

a = datetime.datetime(2012, 3, 1, 10, 5, 30)
b = datetime.datetime(2012, 2, 28, 12, 34, 56)

print(a - b)
print("兩者時間差" , a - b)

a = datetime.datetime(2006, 3, 11, 9, 15, 30)
b = datetime.datetime.now

#print(a - b)
#print("兩者時間差" , a - b)

print(datetime.datetime.now())

d = datetime.datetime.now()
#print("現在時間" , d)
#print("過去時間" , a)

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
    oneday = datetime.timedelta(days = 1)
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
d3 = d1 - datetime.timedelta(days = 10)
print(str(d3))
print(d3.ctime())
#print(time.ctime([sec]))#把秒數轉換成日期格式，如果不帶引數，則顯示當前的時間。
#time.ctime([ sec ])
print("time.ctime() : %s" % time.ctime())


print('---- datetime.now() --------------------------------------------------------')	#60個

tt = datetime.datetime.strptime("2018-01-31", "%Y-%m-%d")
print(tt)

dateString = "7-May-2018"
dateFormatter = "%u-%b-%Y"
tt = datetime.datetime.strptime(dateString, dateFormatter)
print(tt)

dateString = "31/12/2013"
dateFormatter = "%d/%m/%Y"
tt = datetime.datetime.strptime(dateString, dateFormatter)
print(tt)

dateString = "31/12/2013"
dateFormatter = "%d/%m/%Y"
tt = datetime.datetime.strptime(dateString, dateFormatter)
print(tt)

dateString = "Monday, July 16, 2018 20:01:56"
dateFormatter = "%A, %B %d, %Y %H:%M:%S"
tt = datetime.datetime.strptime(dateString, dateFormatter)
print(tt)

#time.time()#通常是用來作為時間戳記，可以傳回從 1970/1/1 00:00:00 算起至今的秒數
seconds = time.time()
print(seconds)

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

def transform_date(date): #轉換日期
    y, m, d, h = date[:4],date[5:7],date[8:10],date[11:13]
    return y + '/' + m  + '/' + d  + '/' + h  

old_date = datetime.datetime.now() # 取得現在時間

old_date = str(old_date)    #先轉成字串

#old_date = '2023/05/24 13:00:00' ex

print(old_date)

new_date = transform_date(old_date)

print(new_date)

print('---- strftime() 可以將時間格式化 --------------------------------------------------------')	#60個

# 格式化為 2020-09-26 21:14:30
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化為Sat Sep 26 21:14:30 2020
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

localtime = time.strftime("%Y/%m/%d %A %H:%M:%S", time.localtime(time.time()))
print('現在時間 : ' + localtime)

# 字串轉換為時間
def strTodatetime(datestr, format):
    return datetime.datetime.strptime(datestr, format)
print(time.strftime("%Y-%m-%d", time.localtime()))
print(strTodatetime("2014-3-1", "%Y-%m-%d"))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(strTodatetime("2019-4-15","%Y-%m-%d") - strTodatetime("2006-03-11","%Y-%m-%d"))

version = time.strftime("-%Y%m%d")
print('version : ', version)

now = datetime.datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

current_time = now.strftime("%H:%M:%S")
print("time:", current_time)

date_time = now.strftime("%Y-%m-%d, %H:%M:%S")
print("date and time:", date_time)

now = datetime.datetime.now()
filename = now.strftime("news-%y-%m-%d-%H-%M-%S.json")
print(filename)

string = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(string)

print('---- new --------------------------------------------------------')	#60個

string = ("%d" % datetime.datetime.now().year)
print(string)

datetime_format = '%Y/%m/%d %H:%M:%S'
now = datetime.datetime.now()
current_time = 'DateTime_{:{}}'.format(now, datetime_format)
print(current_time)

  


import time

ttt = time.time()
#returns the seconds with millisecond precision since the UNIX epoch.
print(ttt)

ttt = int(time.time())
print(ttt)



import datetime
print('datetime from lambda:', datetime.datetime.today())
today = datetime.datetime.today()
print('datetime from flex:', today)

today = str(datetime.datetime.today().date())
current = str(datetime.datetime.today())



import time

print(time.localtime()) #獲取格式化的時間

localtime = time.asctime(time.localtime())
print (localtime)

#格式化日期成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

print('------------------------------------------------------------')	#60個

timestamp = time.strftime('%Y-%m-%d %H:%M%z')

print(timestamp)


print('------------------------------------------------------------')	#60個

now = datetime.datetime.now()
filename = now.strftime("%y-%m-%d-%H-%M-%S.json")
print(filename)

now = datetime.datetime.now()
filename = now.strftime("news-%y-%m-%d-%H-%M-%S.json")
print(filename)


import time

imagepath = '-%04d-%02d-%02d'%(time.localtime()[:3])
imagepath = imagepath + '.dmg'

print(imagepath)



filename = '-%04d-%02d-%02d'%(time.localtime()[:3])
print(filename)


print('------------------------------------------------------------')	#60個

#獲取當前時間
def get_current_time():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return current_time

current_time = get_current_time()
print('當前時間 :', current_time)

print('------------------------------------------------------------')	#60個

import datetime
import time


def DateFromTicks(ticks):
    return Date(*time.localtime(ticks)[:3])

def TimeFromTicks(ticks):
    return Time(*time.localtime(ticks)[3:6])

def TimestampFromTicks(ticks):
    return Timestamp(*time.localtime(ticks)[:6])

print(datetime.datetime)
print(datetime.date)
print(datetime.time)


"""
datetime(2016, 7, 20, 15, 45),
"timestamp": "2016-07-20 15:45",



"timestamp": self.event.timestamp.strftime("%Y-%m-%d %H:%M"),

#timestamp = time.strftime('%Y-%m-%d %H:%M+%Z')
"""


print('------------------------------------------------------------')	#60個


def format_time(field_timestamp: datetime) -> str:
    return field_timestamp.strftime("%Y-%m-%d %H:%M")



print('------------------------------------------------------------')	#60個


start_time = time.time()

time.sleep(0.3456)  #過了一段時間

latency = time.time() - start_time
print("it took %.2f", latency)


print('------------------------------------------------------------')	#60個

t1 = time.time()

t2 = time.time()

t3 = time.time()

print("_safe_repr:", t2 - t1)
print("pformat:", t3 - t2)

print('------------------------------------------------------------')	#60個


print(datetime.datetime.now())

print('------------------------------------------------------------')	#60個

start_date = datetime.datetime(2016, 7, 17)
print(start_date)
end_date = datetime.datetime(2016, 7, 24)
print(end_date)
expected = [datetime.datetime(2016, 7, i) for i in range(17, 24)]
print(expected)

print('------------------------------------------------------------')	#60個

ufrom = 'From nobody ' + time.ctime(time.time())
print(ufrom)



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



import datetime

#輸出當前的日期及時間

print(datetime.datetime.now())

print(datetime.datetime.today())

#而如果只想要輸出現在的日期的話則用
print(datetime.date.today())


#而如果要輸出此時準確的時間的話則
print(time.localtime())

#而我們也可以一一拆解

tonow = datetime.datetime.now()
print(tonow.year)
print(tonow.month)
print(tonow.day)

#而我們也可以算今天是今年的第幾天

dts = '20201007'
dt = datetime.datetime.strptime(dts,"%Y%m%d")
another_dts = dts[:4]+"0101"
another_dt = datetime.datetime.strptime(another_dts,"%Y%m%d")
print(int((dt-another_dt).days)+1)

#由上可得知datetime.datetime.strptime()這個是將所輸入的dts轉換成日期的格式則格式為後面的年月日，再來取出輸入的西元年加上"0101"後一樣轉換成日期的格式最後將輸入日期減掉設定日期後+1輸出成今天為今年的第幾天

loc_dt = datetime.datetime.today() 
time_del = datetime.timedelta(hours=3) 
new_dt = loc_dt + time_del 
datetime_format = new_dt.strftime("%Y/%m/%d %H:%M:%S")
loc_dt_format = loc_dt.strftime("%Y/%m/%d %H:%M:%S")
print(loc_dt_format)
print(datetime_format)


#由上可得知我們也可以調整時差，將我們現在的時間加上3小時的時差並將其輸出出來，一開始我們將抓出本地的時間並且將變數time_del宣告為時差差三個小時，最後將其相加就變成有時差三個小時最後將其指定格式後輸出，而以此類推我們也可以將時差晚三個小時


loc_dt = datetime.datetime.today() 
time_del = datetime.timedelta(hours=3) 
new_dt = loc_dt - time_del 
datetime_format = new_dt.strftime("%Y/%m/%d %H:%M:%S")
loc_dt_format = loc_dt.strftime("%Y/%m/%d %H:%M:%S")
print(loc_dt_format)
print(datetime_format)



print('------------------------------------------------------------')	#60個

from datetime import date, timedelta

d0 = date(1993, 12, 15)
d1 = date(2020, 12, 15)

delta = timedelta(days = 1)
print('日期 :', d0 + delta)

delta = timedelta(days = 10000)
print('日期 :', d0 + delta)

print('相距日期 :', d1 - d0, '天')


d0 = date(2021, 5, 24)
d1 = date(2023, 8, 21)
print('相距日期 :', d1 - d0, '天')

print('------------------------------------------------------------')	#60個

import datetime

def _format_time(hh, mm, ss, us):
    # Skip trailing microseconds when us==0.
    result = "%02d:%02d:%02d" % (hh, mm, ss)
    if us:
        result += ".%06d" % us
    return result

year = 2023
month = 8
day = 11
sep = 'W'
hour = 12
minute = 34
second = 56
microsecond = 123456
s = _format_time(hour, minute, second, microsecond)
print(s)


s = ("%04d-%02d-%02d%c" % (year, month, day, sep) +
     _format_time(hour, minute, second,microsecond))
print(s)


hh = 12
mm = 34
ss = 56
s = "%d:%02d:%02d" % (hh, mm, ss)
print(s)


print('------------------------------------------------------------')	#60個
import time
print(time.time())
print(time.localtime())
year, month, day, hour, minute, second, _, _, _ = time.localtime()
print("{}-{}-{} {}:{}:{}".format(year, month, day, hour, minute, second))
print(time.asctime())
print(time.strftime("%Y-%m-%d %H:%M:%S %a"))

import datetime
#當前的日期及時間
print(datetime.datetime.now())

import datetime
today = datetime.datetime.today()
birthday = datetime.datetime(2018,10,27, 17, 0, 0)
print(today - birthday)

"""
from datetime import datetime
now = datetime.now()
print("今天是{}".format(datetime.strftime(now, "%Y-%m-%d")))

#date = input("請輸入一個日期（yyyy-mm-dd):")
print('請輸入一個日期')
date = '2006-03-11'
print(date)
target = datetime.strptime(date, "%Y-%m-%d")
diff = now-target
print("到今天共經過了{}天。".format(diff.days))
"""

print('------------------------------------------------------------')	#60個


# Name of the benchmark
name = '%04i-%02i-%02i %02i:%02i:%02i' % \
       (time.localtime(time.time())[:6])

print(name)



print('------------------------------------------------------------')	#60個

xtime = time.localtime()
print(xtime)                        # 列出目前系統時間
print("年 ", xtime[0])
print("年 ", xtime.tm_year)         # 物件設定方式顯示
print("月 ", xtime[1])
print("日 ", xtime[2])
print("時 ", xtime[3])
print("分 ", xtime[4])
print("秒 ", xtime[5])
print("星期幾   ", xtime[6])
print("第幾天   ", xtime[7])
print("夏令時間 ", xtime[8])

print('------------------------------------------------------------')	#60個

ticks = time.time() #至今的tick數
print(ticks)

localtime = time.localtime(ticks)   #傳回時間元組
print(type(localtime))
print(localtime)

print('年 :', localtime[0])
print('月 :', localtime[1])
print('日 :', localtime[2])
print('時 :', localtime[3])
print('分 :', localtime[4])
print('秒 :', localtime[5])

#asctime() #傳回時間元組的日期時間字串
formattime = time.asctime(time.localtime(ticks))
print(formattime)



print('------------------------------------------------------------')	#60個


import time                         # 導入模組time

print(time.asctime())               # 列出目前系統時間 

print('------------------------------------------------------------')	#60個

import time                         # 導入模組time

xtime = time.localtime()
print(xtime)                        # 列出目前系統時間
print("年 ", xtime[0])
print("年 ", xtime.tm_year)         # 物件設定方式顯示
print("月 ", xtime[1])
print("日 ", xtime[2])
print("時 ", xtime[3])
print("分 ", xtime[4])
print("秒 ", xtime[5])
print("星期幾   ", xtime[6])
print("第幾天   ", xtime[7])
print("夏令時間 ", xtime[8])

print('------------------------------------------------------------')	#60個

import time                         # 導入模組time

print(time.ctime())


print('------------------------------------------------------------')	#60個

year, month, day, hours, minutes, seconds = 2023, 9, 22, 12, 34, 56
cc = datetime.datetime(year, month, day, hours, minutes, seconds)
print(cc)

NOW = datetime.datetime.now()
print(NOW)

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


startTime = time.time() # Get start time

#do something

endTime = time.time() # Get end time
testTime = int(endTime - startTime) # Get test time
print("Test time is", testTime, "seconds")

print('------------------------------------------------------------')	#60個

startTime_seconds = time.time()

time.sleep(0.3456)  #過了一段時間

elapsedTime_seconds = time.time() - startTime_seconds
print("Time for LinkedList is", elapsedTime_seconds, "seconds")

start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2017, 1, 1)

print('------------------------------------------------------------')	#60個
t0 = time.time()

#do something

t1 = time.time()

print("Open took %.2f seconds" % (t1 - t0))
print("\ncommand took %.2f seconds\n" % (t1 - t0))

print('------------------------------------------------------------')	#60個

startTime = time.time()

#do something

elapsedTime = time.time() - startTime
print("Time for LinkedList is", elapsedTime, "seconds")

startTime = time.time()

elapsedTime = time.time() - startTime
print("Time for list is", elapsedTime, "seconds")


print('------------------------------------------------------------')	#60個

import time

startTime = time.time()

# do something

print("Sort time in Python is", int(time.time() - startTime), "seconds")

print('------------------------------------------------------------')	#60個

import time                         # 導入模組time

starttime = int(time.time())        # 起始秒數

# do something

endtime = int(time.time())  # 結束秒數
print("所花時間: ", endtime - starttime, " 秒")


print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

