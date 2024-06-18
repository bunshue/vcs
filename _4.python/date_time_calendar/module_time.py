"""
time 模組
"""

import sys
import time

"""
1. 單獨使用
2. 轉換使用
3. 格式化使用

1. time.time()
2. time.localtime()
3. time.ctime()
   time.gmtime()
   time.asctime()

"""
print("---- 單獨使用 --------------------------------------------------------")  # 60個
print('---- time.time() --------------------------------------------------------')	#60個

print('time.time()\t', time.time())

#time.time()#通常是用來作為時間戳記，可以傳回從 1970/1/1 00:00:00 算起至今的總秒數

total_seconds = time.time()
print('UNIX epoch 至今的時間 :', total_seconds, '秒 (百奈秒)')

total_seconds = int(time.time())
print('UNIX epoch 至今的時間 :', total_seconds, '秒 (整數秒)')

print('------------------------------------------------------------')	#60個

total_seconds = time.time() # Get current time

# Obtain the total seconds since midnight, Jan 1, 1970
totalSeconds = int(total_seconds)

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

print('---- time.localtime() --------------------------------------------------------')	#60個

#而如果要輸出此時準確的時間的話則
print(time.localtime())

print('time.localtime()\t', time.localtime())

year, month, day, hour, minute, second, _, _, _ = time.localtime()
print("{}-{}-{} {}:{}:{}".format(year, month, day, hour, minute, second))

print('從 total_seconds 取得localtime時間')
print('現在時間 轉 localtime')
localtime = time.localtime(time.time())
print('localtime時間 :', localtime)


print("獲取當前時間");
localtime = time.localtime(time.time())
print("Local current time :", localtime)

    
print('123456秒後')
localtime = time.localtime(time.time() + 123456)
print('localtime時間 :', localtime)

print('現在時間 轉 localtime')
localtime = time.localtime(time.time())   #傳回時間元組
print(type(localtime))
print(localtime)
print('年 :', localtime[0], end = " ")
print('月 :', localtime[1], end = " ")
print('日 :', localtime[2], end = " ")
print('時 :', localtime[3], end = " ")
print('分 :', localtime[4], end = " ")
print('秒 :', localtime[5])

# time.localtime() #可以輸出 struct_time 的時間格式
localtime = time.localtime() # 取得當前時間
print('當前時間 :', localtime)  # 列出目前系統時間
print('年 :', localtime.tm_year, end = " ")
print('月 :', localtime.tm_mon, end = " ")
print('日 :', localtime.tm_mday, end = " ")
print('星 :' , localtime.tm_wday, end = " ")
print('時 :', localtime.tm_hour, end = " ")
print('分 :', localtime.tm_min, end = " ")
print('秒 :', localtime.tm_sec)
print('星期(0為星期一) :', localtime.tm_wday)
print('今天為今年第幾天 :', localtime.tm_yday)
print('夏令時間(0為不是，1為是) :', localtime.tm_isdst)

print('------------------------------------------------------------')	#60個

localtime = time.localtime()
print(localtime)                        # 列出目前系統時間
print("年 ", localtime.tm_year)         # 物件設定方式顯示
print("年 ", localtime[0], end = " ")
print("月 ", localtime[1], end = " ")
print("日 ", localtime[2], end = " ")
print("時 ", localtime[3], end = " ")
print("分 ", localtime[4], end = " ")
print("秒 ", localtime[5])
print("星期幾   ", localtime[6], end = " ")
print("第幾天   ", localtime[7], end = " ")
print("夏令時間 ", localtime[8])

print('------------------------------------------------------------')	#60個

localtime = time.localtime()
print("西元%d年%d月%d日%d點%d分"%(localtime[0],localtime[1],localtime[2],localtime[3],localtime[4]))

print("------------------------------------------------------------")  # 60個

week = ["一","二","三","四","五","六","日"]
dst = ["無日光節約時間","有日光節約時間"]
localtime = time.localtime()
show = "現在時刻:"+"\n"
show += "民國"+str(int(localtime.tm_year)-1911)+"年"
show += str(localtime.tm_mon)+"月"+str(localtime.tm_mday)+"日"
show += str(localtime.tm_hour)+"時"+str(localtime.tm_min)+"分"
show += str(localtime.tm_sec)+"秒 星期"+week[localtime.tm_wday]+"\n"
show += "今天是今年的第"+str(localtime.tm_yday)+"天，此地"+dst[localtime.tm_isdst]
print(show)

print("------------------------------------------------------------")  # 60個

print("---- 其他 --------------------------------------------------------")  # 60個

print('time.ctime()\t', time.ctime())
print('time.gmtime()\t', time.gmtime())
print('time.asctime()\t', time.asctime())

print(time.ctime(time.time()))

print('從 total_seconds 取得GMT時間')
gmtime = time.gmtime(total_seconds)
print('GMT時間 :', gmtime)

#asctime() #傳回時間元組的日期時間字串
formattime = time.asctime(time.localtime(total_seconds))
print(formattime)

print("---- 轉換使用 --------------------------------------------------------")  # 60個

print("獲取格式化的時間");
localtime = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime)

#cccc轉換
time7 = time.ctime(time.time())
print('time7 :', time7)



print("---- 格式化使用 --------------------------------------------------------")  # 60個


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

print('現在時間 轉 localtime')
localtime = time.localtime(time.time())
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

# 做一件事, 量測時間

endtime = int(time.time())  # 結束秒數
print("所花時間: ", endtime - starttime, " 秒")

print("------------------------------------------------------------")  # 60個

from email.utils import formatdate, parsedate, parsedate_tz

TIME_FMT = "%a, %d %b %Y %H:%M:%S GMT"

freshness_lifetime = max(0, min(5 / 10, 24 * 3600))
expires = freshness_lifetime

print("expires", time.strftime(TIME_FMT, time.gmtime(expires)))

print('------------------------------------------------------------')	#60個

#顯示系統當前時間
now = time.strftime("%Y-%m-%d %I:%M:%S %p", time.localtime())
print(now)

"""
定义和使用时钟类

Version: 0.1
Author: 骆昊
Date: 2018-03-08
"""
""" no cloc
import os


class Clock(object):

    # Python中的函数是没有重载的概念的
    # 因为Python中函数的参数没有类型而且支持缺省参数和可变参数
    # 用关键字参数让构造器可以传入任意多个参数来实现其他语言中的构造器重载
    def __init__(self, **kw):
        if 'hour' in kw and 'minute' in kw and 'second' in kw:
            self._hour = kw['hour']
            self._minute = kw['minute']
            self._second = kw['second']
        else:
            tm = time.localtime(time.time())
            self._hour = tm.tm_hour
            self._minute = tm.tm_min
            self._second = tm.tm_sec

    def run(self):
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
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


if __name__ == '__main__':
    # clock = Clock(hour=10, minute=5, second=58)
    clock = Clock()
    while True:
        os.system('clear')
        print(clock.show())
        time.sleep(1)
        clock.run()

"""

print('---- time.sleep(秒) --------------------------------------------------------')	#60個

print("每0.3456秒打印一字")
a = 0;
while a < 3:
    a += 1;
    print("hello " + str(a), end = '\t')
    time.sleep(0.3456)  #過了一段時間
print()

print('------------------------------------------------------------')	#60個

def countdown(n):
    while n > 0:
        print('數字 : ', n, end = '\t')
        n -= 1
        time.sleep(0.3456)  #過了一段時間

print("倒數計時")
countdown(5)
print()

print('------------------------------------------------------------')	#60個

print("程式暫停0.2秒鐘")
time.sleep(0.2)
print("程式繼續執行")

print("------------------------------------------------------------")  # 60個

print('格式化使用------------------------------------------------------------')	#60個

localtime = time.localtime()    # 取得目前的日期和時間

print(time.strftime('%Y-%m-%d %H:%M:%S', localtime))
print(time.strftime('%Y-%m-%d 第%W週', localtime))   # 週數
print(time.strftime('%Y-%m-%d 第%j天', localtime))   # 天數

print(time.strftime('%c', localtime))      # 字串回傳
print(time.strftime('%c %p', localtime))   # 加入AM或PM

print(time.strftime('%x', localtime))      # 只有日期
print(time.strftime('%X', localtime))      # 只有時間值

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

name = '%04i-%02i-%02i %02i:%02i:%02i' % (time.localtime(time.time())[:6])
print(name)

print('------------------------------------------------------------')	#60個

print('轉換使用------------------------------------------------------------')	#60個

localtime = time.asctime(time.localtime())
print (localtime)

print('------------------------------------------------------------')	#60個

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

for i in range(9):#以元組的索引值取得的資料內容
    print(field[i], end = " ")

print()

print('------------------------------------------------------------')	#60個

# 取得本地的當前的日期和時間，採struct_time型式以Tuple物件回傳
current = time.localtime(time.time())
print(f'當地時間：{current[0]}年 {current[1]}月',
      f'{current[2]}日 {current[3]}時',
      f'{current[4]}分 {current[5]}秒')

# 取得目當前的日期和時間，以字串回傳
current2 = time.ctime(time.time())
print('目前時間：', current2)

print("------------------------------------------------------------")  # 60個

localtime = time.localtime(time.time())

print("轉換時間形式(年/月/日)：", time.strftime("%Y/%m/%d", localtime))
print("轉換時間形式(年/月/日 時:分:秒)：", time.asctime(localtime))

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


def DateFromTicks(ticks):
    return Date(*time.localtime(ticks)[:3])

def TimeFromTicks(ticks):
    return Time(*time.localtime(ticks)[3:6])

def TimestampFromTicks(ticks):
    return Timestamp(*time.localtime(ticks)[:6])

print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個

"""
localtime()返回元組的日期與時間資料結構 用索引方式獲得個別內容
索引	名稱	說明
0	tm_year	年 	2020
1	tm_mon	月 	1-12
2	tm_mday 日	1-31
3	tm_hour	時	0-23
4	tm_min	分	0-59
5	tm_sec	秒	0-59
6	tm_wday	星期	0:一, 1:二...
7	tm_yday	年第幾天
8	tm_isdst 夏令時間 0:不是, 1:是
"""

xtime = time.localtime()            #使用localtime()方法列出目前時間的結構
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

print('range(5)', range(5))
print('list(range(5))', list(range(5)))

# range
tStart = time.time()
for i in range(10000000):
    pass
tEnd = time.time()
print('range time:', tEnd - tStart)

print("------------------------------------------------------------")  # 60個






print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個



"""

        start_time = time.perf_counter()  # 獲取函數開始執行的時間
        result = func(*args, **kwargs)  # 調用原始函數
        end_time = time.perf_counter()  # 獲取函數結束執行的時間
        duration = end_time - start_time  # 計算函數執行時間
        print(f"{func.__name__} 執行需 : {duration:.7f} 秒")
        


"""

