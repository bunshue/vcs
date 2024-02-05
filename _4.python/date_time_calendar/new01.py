"""

新進
datetime
time
calendar


"""

import os
import sys
import time
import random
import datetime

print("------------------------------------------------------------")  # 60個

import datetime

dateObj = datetime.datetime.strptime('2025/1/1', '%Y/%m/%d')
print(dateObj)


print("------------------------------------------------------------")  # 60個


import time #匯入時間模組

print('現在時間：')
print() #輸出空白行
print(time.ctime())


print("------------------------------------------------------------")  # 60個


import time #滙入time模組

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

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH08\CH0807.py

import time    # 滙入time模組

current = time.localtime()    # 取得目前的日期和時間

print(time.strftime('%Y-%m-%d %H:%M:%S', current))
print(time.strftime('%Y-%m-%d 第%W週', current))   # 週數
print(time.strftime('%Y-%m-%d 第%j天', current))   # 天數

print(time.strftime('%c', current))      # 字串回傳
print(time.strftime('%c %p', current))   # 加入AM或PM

print(time.strftime('%x', current))      # 只有日期
print(time.strftime('%X', current))      # 只有時間值

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH08\CH0808.py

import datetime
work = datetime.date(2021, 10, 9)
print(work)
print(f'一週的第{work.weekday()}天')
num = work.isoweekday()
print('星期天' if num == 7 else '星期 '+ str(num))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH08\CH0809.py

from datetime import date, timedelta

# 某個日期區間，以1日為間隔值
begin = date(2021, 10, 1)
end = date(2021, 10, 15)
step = timedelta(days = 1)

result = []  #空的List，用來存放日期

# while迴圈 加入date物件
while begin < end:
    result.append(begin.strftime('%Y-%m-%d'))
    begin += step
    
width = 11 #欄寬   
# for/in 讀取並做格式化輸出
for item in result:
    print('{0:{width}}'.format(
        item, width = width), end = '')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH08\CH0810.py

from datetime import date, timedelta

tody = date.today() # 今天日期
yr, mt, dt = eval(input('請輸入出生的年、月、日->'))

# 某人生日
birth = date(yr, mt, dt)
ageDays = tody - birth


print(f'天數：{ageDays.days:,}天')
age = ageDays/timedelta(days = 365)   # 年齡
print(f'年齡 {age:.2f}')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH08\CH0811.py

from datetime import datetime, timedelta

# 設兩個時間
d1 = timedelta(days = 4, hours = 5)
d2 = timedelta(hours = 2.8)

#將兩個時間相加
dtAdd = d1 + d2    
print(f'共{dtAdd.days}天')
print(f'   7.8時 = {dtAdd.seconds:7,}')
print(f'4天7.8時 = {dtAdd.total_seconds():9,} 秒')

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH08\CH0812.py

from datetime import datetime, timedelta

d1 = datetime(2018, 9, 2)
print('日期：', d1 + (timedelta(days = 7)))

d2 = datetime(2020, 1, 22)
d3 = timedelta(days = 106)
dt = d2 - d3 # 將兩個日期相減
print('日期二：', dt.strftime('%Y-%m-%d'))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\好好玩！Python程式設計入門與實例應用-鍛鍊邏輯思維×徹底掌握核心\CH08\CH0813.py

from datetime import datetime, timedelta

#建立儲存星期的list物件
weeklst = ['Monday', 'Tuesday', 'Wednesday',
         'Thursday', 'Friday', 'Saturday', 'Sunday']

# 定義函式
def getWeeks(wkName, beginDay = None):
    #如果未傳入beginDay之日期，就以今天為主
    if beginDay is None:
        beginDay = datetime.today()
        
    #weekday()方法回傳取得星期的索引值，Monday索引值為0
    indexNum = beginDay.weekday()
    target = weeklst.index(wkName)
    lastWeek = ( 7 + indexNum - target) % 7
    if lastWeek == 0:
        lastWeek = 7
        
    #timedelta()建構式取得天數
    lastWeek_Day = beginDay - timedelta(
        days = lastWeek)
    return lastWeek_Day.strftime('%Y-%m-%d')

#呼叫函式，只傳入一個參數
print('今天的上週三：', getWeeks('Wednesday'))

#呼叫函式，傳入二個參數
dt = datetime(2017, 4, 11)
print('2017/4/11 的上週二：', getWeeks('Tuesday', dt))




print("------------------------------------------------------------")  # 60個



import sys


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

import time
x = 1000000
pi = 0
time.process_time()
for i in range(1,x+1):
    pi += 4*((-1)**(i+1) / (2*i-1))
    if i != 1 and i % 100000 == 0:      # 隔100000執行一次
        e_time = time.process_time()
        print(f"當 {i=:7d} 時 PI={pi:8.7f}, 所花時間={e_time}")

print("------------------------------------------------------------")  # 60個

import time
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(formatted_time)

print("------------------------------------------------------------")  # 60個

import time

def log_event(event):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"{timestamp} : {event}")

# 假設發生了一個事件
log_event("User login")

print("------------------------------------------------------------")  # 60個

import time

def database_backup():
    # 執行備份邏輯
    print("資料庫備份 ... ")

# 每天凌晨1點執行備份
while True:
    current_time = time.strftime("%H:%M", time.localtime())
    if current_time == "01:00":
        database_backup()
    time.sleep(60)              # 每分鐘檢查一次

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


