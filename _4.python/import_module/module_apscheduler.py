import sys
import apscheduler

"""
定時任務、自動化執行

APScheduler全名為Advanced Python Schedule，
是一個輕量級的Python任務定時執行模組。
它可以讓你安排需要定時執行的任務，
只要是可以呼叫的對象（函式、方法等等）都可以指定給定時器來執行。


add_job()方法你的時間指定參數

interval模式

代表指定以間隔的方式來執行：
參數名稱 	說明
weeks 	間隔幾週
days 	間隔幾天
hours 	間隔幾小時
minutes 	間隔幾分鐘
seconds 	幾格幾秒

cron模式

指定某個時段執行：
參數名稱 	說明
year 	西元年，四位數字
month 	月份（1-12）
day 	日（1-31）
hour 	時（0-23）
minute 	分（0-59）
second 	秒（0-59）
day_of_week 	指定星期，0=星期一…6=星期日

"""

print("------------------------------------------------------------")  # 60個


"""
阻塞式
阻塞式定時器在啟動後程式會停止繼續執行
"""

import time
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


def job1():
    print(f'工作１啟動: 目前時間{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')


def job2():
    print(f'工作２啟動: 目前時間{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')


def job3():
    print(f'工作３啟動: 目前時間{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')


def job4():
    print(f'工作４啟動: 目前時間{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')


# 指定時區（一定要指定，否則會失敗）
scheduler = BlockingScheduler(timezone="Asia/Shanghai")

# 每１分鐘執行job1函式
scheduler.add_job(job1, "interval", minutes=1)

# 每５秒執行job2函式
scheduler.add_job(job2, "interval", seconds=5)

# 每１秒執行job3函式
scheduler.add_job(job3, "interval", seconds=1)

# 每週二到日的下午6點30分執行job4函式
scheduler.add_job(job4, "cron", day_of_week="1-6", hour=18, minute=30)

scheduler.start()

print("Schedule started ...")  # 這行不會被執行

"""
非阻塞式
非阻塞式在啟動後，程式會繼續執行，需注意不能讓程式結束，否則定時器就會跟著結束了。
"""

import time
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime


def job1():
    print(f'工作１啟動: 目前時間{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')


def job2():
    print(f'工作２啟動: 目前時間{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')


def job3():
    print(f'工作３啟動: 目前時間{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')


def job4():
    print(f'工作４啟動: 目前時間{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')


# 指定時區（一定要指定，否則會失敗）
scheduler = BackgroundScheduler(timezone="Asia/Shanghai")

# 每１分鐘執行job1函式
scheduler.add_job(job1, "interval", minutes=1)

# 每５秒執行job2函式
scheduler.add_job(job2, "interval", seconds=5)

# 每１秒執行job3函式
scheduler.add_job(job3, "interval", seconds=1)

# 每週二到日的下午6點30分執行job4函式
scheduler.add_job(job4, "cron", day_of_week="1-6", hour=18, minute=30)

scheduler.start()

print("Schedule started ...")

while True:
    time.sleep(10)  # 暫停10秒鐘
    print("程式執行中.....")


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
