"""

time 模組

"""

import sys
import time

print('---- time.sleep(秒) --------------------------------------------------------')	#60個

print("每0.3456秒打印一字")
a = 0;
while a < 3:
    a += 1;
    print("hello " + str(a))
    time.sleep(0.3456)  #過了一段時間

print('------------------------------------------------------------')	#60個

def countdown(n):
    while n > 0:
        print('數字 : ', n)
        n -= 1
        time.sleep(0.3456)  #過了一段時間

print("倒數計時")
countdown(5)

print('------------------------------------------------------------')	#60個

print('---- time.time() --------------------------------------------------------')	#60個

#time.time()#通常是用來作為時間戳記，可以傳回從 1970/1/1 00:00:00 算起至今的秒數

time_tick = time.time()
print('UNIX epoch 至今的時間 :', time_tick)

time_tick = int(time.time())
print('UNIX epoch 至今的時間 :', time_tick, '秒')

#取得tick數
ticks = time.time()
print("從1/1/1970 12:00:00至今的 tick數 : ", ticks)

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

print('---- 經歷時間 ST --------------------------------------------------------')	#60個

print("測試兩事件所經歷的時間 ST")
time_st = time.time()

time.sleep(0.3456)  #過了一段時間

time_sp = time.time()

time_elapsed = time_sp - time_st

print("測試兩事件所經歷的時間 SP, 經歷時間 : " + str(time_elapsed) + " 秒")
print("經歷時間 " + str(time_elapsed) + " 秒")
print("經歷時間", int(time_elapsed), " 秒")
print("經歷時間 %.2f", time_elapsed)
print("經歷時間 %.2f 秒" % (time_elapsed))

print('取整數秒')
time_elapsed = int(time_sp - time_st)
print("Test time is", time_elapsed, "seconds")

print('------------------------------------------------------------')	#60個

print('ccccccc')
ticks = time.time() #至今的tick數
print(ticks)

print('從ticks取得GMT時間')
time1 = time.gmtime(ticks)
print('GMT時間 :', time1)

time2 = time.gmtime()
print('目前的GMT時間 :', time2)

print('從ticks取得localtime時間')
time3 = time.localtime(ticks)
print('localtime時間 :', time3)

time4 = time.localtime()
print('目前的localtime時間 :', time4)


print('---- 現在時間 --------------------------------------------------------')	#60個

print("獲取當前時間");
localtime = time.localtime(time.time())
print("Local current time :", localtime)

print("獲取格式化的時間");
localtime = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime)

time5 = time.asctime()
print('time5 :', time5)

print(time.asctime())               # 列出目前系統時間 

print(time.ctime())

time6 = time.ctime()
print('time6 :', time6)

time7 = time.ctime(time.time())
print('time7 :', time7)

ufrom = 'From nobody ' + time.ctime(time.time())
print(ufrom)

# time.localtime() #可以輸出 struct_time 的時間格式
localtime = time.localtime() # 取得當前時間
print('當前時間 :', localtime)  # 列出目前系統時間
print('年 :', localtime.tm_year)
print('月 :', localtime.tm_mon)
print('日 :', localtime.tm_mday)
print('星 :' , localtime.tm_wday)
print('時 :', localtime.tm_hour)
print('分 :', localtime.tm_min)
print('秒 :', localtime.tm_sec)
print('星期(0為星期一) :', localtime.tm_wday)
print('今天為今年第幾天 :', localtime.tm_yday)
print('夏令時間(0為不是，1為是) :', localtime.tm_isdst)

print('------------------------------------------------------------')	#60個

print("年 ", localtime.tm_year)         # 物件設定方式顯示
print("年 ", localtime[0])
print("月 ", localtime[1])
print("日 ", localtime[2])
print("時 ", localtime[3])
print("分 ", localtime[4])
print("秒 ", localtime[5])
print("星期幾   ", localtime[6])
print("第幾天   ", localtime[7])
print("夏令時間 ", localtime[8])

print('------------------------------------------------------------')	#60個

print("獲取此時的時間");
print(time.localtime())

localtime = time.asctime(time.localtime())
print (localtime)

#格式化日期成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 格式化為 2020-09-26 21:14:30
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化為Sat Sep 26 21:14:30 2020
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

localtime = time.strftime("%Y/%m/%d %A %H:%M:%S", time.localtime(time.time()))
print('現在時間 :' + localtime)


print('------------------------------------------------------------')	#60個

print(time.strftime("%Y-%m-%d %H:%M:%S %a"))

timestamp = time.strftime('%Y-%m-%d %H:%M%z')
print(timestamp)

print('------------------------------------------------------------')	#60個

#獲取當前時間
localtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
print('當前時間 :', localtime)

print('------------------------------------------------------------')	#60個

print(time.strftime("%Y-%m-%d", time.localtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

version = time.strftime("-%Y%m%d")
print('version : ', version)

print('------------------------------------------------------------')	#60個

filename = '-%04d-%02d-%02d' % (time.localtime()[:3]) + '.jpg'
print(filename)

print('------------------------------------------------------------')	#60個

# Name of the benchmark
name = '%04i-%02i-%02i %02i:%02i:%02i' % (time.localtime(time.time())[:6])
print(name)

print('------------------------------------------------------------')	#60個

def DateFromTicks(ticks):
    return Date(*time.localtime(ticks)[:3])

def TimeFromTicks(ticks):
    return Time(*time.localtime(ticks)[3:6])

def TimestampFromTicks(ticks):
    return Timestamp(*time.localtime(ticks)[:6])

print('------------------------------------------------------------')	#60個

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



print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

"""
print(time.strptime(date, '%Y-%m-%d'))
print(time.strptime(time_, '%H:%M:%S'))
"""

print('------------------------------------------------------------')	#60個

dt = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())

print('現在時間 :', dt)

#Sat, 07 Oct 2023 19:15:16 +0000

print('------------------------------------------------------------')	#60個

dt = time.strptime("30 Sep 23", "%d %b %y")
print('time.struct_time 結構')
print(dt)
print('年 :', dt.tm_year)
print('月 :', dt.tm_mon)
print('日 :', dt.tm_mday)
print('時 :', dt.tm_hour)
print('分 :', dt.tm_min)
print('秒 :', dt.tm_sec)
print('星 :', dt.tm_wday)
print('第 :', dt.tm_yday, '天')

print('------------------------------------------------------------')	#60個

"""
print('量測時間 ST') 
# Start the stopwatch / counter
t1_start = time.perf_counter()
 
time.sleep(0.3456)  #過了一段時間
 
# Stop the stopwatch / counter
t1_stop = time.perf_counter()

print('量測時間 SP')  
print(t1_stop, t1_start)
print(t1_stop - t1_start, '秒')

from time import perf_counter_ns
 
print('量測時間 ST') 
# Start the stopwatch / counter
t1_start = time.perf_counter_ns()

time.sleep(0.3456)  #過了一段時間
 
# Stop the stopwatch / counter
t1_stop = time.perf_counter_ns()

print('量測時間 SP')
print(t1_stop, 'ns', t1_start, 'ns')
 
print(t1_stop - t1_start, 'ns')

start = time.time()

time.sleep(0.3456)  #過了一段時間

stop = time.time()

print(stop - start)
"""

print('------------------------------------------------------------')	#60個

print('存檔紀念')

fp = open('tmp_log.txt', 'w')
fp.write("# BUILD INFO\n")
fp.write("# Date: %s\n" % time.ctime())
fp.close()

print('------------------------------------------------------------')	#60個

print(time.localtime())
year, month, day, hour, minute, second, _, _, _ = time.localtime()
print("{}-{}-{} {}:{}:{}".format(year, month, day, hour, minute, second))

print('------------------------------------------------------------')	#60個

print(time.asctime())  # 列出目前系統時間

print("------------------------------------------------------------")  # 60個

xtime = time.localtime()
print(xtime)  # 列出目前系統時間
print("年 ", xtime[0])
print("月 ", xtime[1])
print("日 ", xtime[2])
print("時 ", xtime[3])
print("分 ", xtime[4])
print("秒 ", xtime[5])
print("星期幾   ", xtime[6])
print("第幾天   ", xtime[7])
print("夏令時間 ", xtime[8])

t = time.time()
tLocal = time.localtime(t)

print("轉換時間形式(年/月/日)：", time.strftime("%Y/%m/%d", tLocal))
print("轉換時間形式(年/月/日 時:分:秒)：", time.asctime (tLocal))

print("------------------------------------------------------------")  # 60個

print(time.time())
print(time.localtime())

field=time.localtime(time.time())#以元組資料的名稱去取得資料
print('tm_year= ',field.tm_year)
print('tm_mon= ',field.tm_mon)
print('tm_mday= ',field.tm_mday)
print('tm_hour= ',field.tm_hour)
print('tm_min= ',field.tm_min)
print('tm_mec= ',field.tm_sec)
print('tm_wday= ',field.tm_wday)
print('tm_yday= ',field.tm_yday)
print('tm_isdst= ',field.tm_isdst)

for j in range(9):#以元組的索引值取得的資料內容
    print('以元組的索引值取得資料= ',field[j])
            
print("我有一句話想對你說:")
time.sleep(1) #程式停1秒
print("學習Python的過程唯然漫長,但最終的果實是甜美的")
print("程式執行到目前的時間是"+str(time.process_time()))
time.sleep(2) #程式停2秒
print("程式執行到目前的時間是"+str(time.perf_counter()))

print('------------------------------------------------------------')	#60個

print('現在時間：')
print() #輸出空白行
print(time.ctime())

print("------------------------------------------------------------")  # 60個

#以秒數儲存epoch值, 以浮點數輸出
seconds = time.time() 
print('epoch:', seconds)

# 取得本地的當前的日期和時間，採struct_time型式以Tuple物件回傳
current = time.localtime(seconds)
print(f'當地時間：{current[0]}年 {current[1]}月',
      f'{current[2]}日 {current[3]}時',
      f'{current[4]}分 {current[5]}秒')

# 取得目當前的日期和時間，以字串回傳
current2 = time.ctime(seconds)
print('目前時間：', current2)

print("------------------------------------------------------------")  # 60個

current = time.localtime()    # 取得目前的日期和時間

print(time.strftime('%Y-%m-%d %H:%M:%S', current))
print(time.strftime('%Y-%m-%d 第%W週', current))   # 週數
print(time.strftime('%Y-%m-%d 第%j天', current))   # 天數

print(time.strftime('%c', current))      # 字串回傳
print(time.strftime('%c %p', current))   # 加入AM或PM

print(time.strftime('%x', current))      # 只有日期
print(time.strftime('%X', current))      # 只有時間值

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

x = 1000000
pi = 0
time.process_time()
for i in range(1,x+1):
    pi += 4*((-1)**(i+1) / (2*i-1))
    if i != 1 and i % 100000 == 0:      # 隔100000執行一次
        e_time = time.process_time()
        print(f"當 {i=:7d} 時 PI={pi:8.7f}, 所花時間={e_time}")

print("------------------------------------------------------------")  # 60個

formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(formatted_time)

print("------------------------------------------------------------")  # 60個

"""
def log_event(event):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"{timestamp} : {event}")

# 假設發生了一個事件
log_event("User login")
"""

print("------------------------------------------------------------")  # 60個

"""
def database_backup():
    # 執行備份邏輯
    print("資料庫備份 ... ")

# 每天凌晨1點執行備份
while True:
    current_time = time.strftime("%H:%M", time.localtime())
    if current_time == "01:00":
        database_backup()
    time.sleep(60)              # 每分鐘檢查一次
"""

print("------------------------------------------------------------")  # 60個

# 數位時鐘

class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = time.localtime(time.time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        # 走字
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        # 显示时间
        return "%02d:%02d:%02d" % (self._hour, self._minute, self._second)


"""
clock = Clock.now()
while True:
    print(clock.show())
    time.sleep(1)
    clock.run()
"""

print("------------------------------------------------------------")  # 60個

seconds = time.time()
print(seconds)
localtime = time.localtime(seconds)
print(localtime)
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)
asctime = time.asctime(localtime)
print(asctime)
strtime = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
print(strtime)
mydate = time.strptime("2018-1-1", "%Y-%m-%d")
print(mydate)

print("------------------------------------------------------------")  # 60個

print("開始計時")
starttime = int(time.time())  # 起始秒數

print("------------------------------------------------------------")  # 60個

print("計算1970年1月1日00:00:00至今的秒數 = ", int(time.time()))

print("------------------------------------------------------------")  # 60個

print(time.asctime())  # 列出目前系統時間

print("------------------------------------------------------------")  # 60個

xtime = time.localtime()
print(xtime)  # 列出目前系統時間
print("年 ", xtime[0])
print("月 ", xtime[1])
print("日 ", xtime[2])
print("時 ", xtime[3])
print("分 ", xtime[4])
print("秒 ", xtime[5])
print("星期幾   ", xtime[6])
print("第幾天   ", xtime[7])
print("夏令時間 ", xtime[8])

print("------------------------------------------------------------")  # 60個

endtime = int(time.time())  # 結束秒數
print("所花時間: ", endtime - starttime, " 秒")

print("------------------------------------------------------------")  # 60個

t = time.time()
tLocal = time.localtime(t)

print("轉換時間形式(年/月/日)：", time.strftime("%Y/%m/%d", tLocal))
print("轉換時間形式(年/月/日 時:分:秒)：", time.asctime(tLocal))

print("------------------------------------------------------------")  # 60個


print('------------------------------------------------------------')	#60個





print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

