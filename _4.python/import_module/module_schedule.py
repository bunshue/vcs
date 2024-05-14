"""
schedule：定時執行任務

Schedule—簡單實用的 Python 周期任務調度工具

周期性地執行某個 Python 腳本
1. Crontab
2. Celery
3. Schedule

1. 設定每隔多長時間 執行某個函數
2. 指定每天幾點幾分 執行某個函數

schedule.clear() 清空所有排程

schedule.every(N).HH_MM_SS.do(job1) 的用法

# 每星期一執行任務(單數)
schedule.every().monday.do(job1)

# 每3周執行任務
schedule.every(3).weeks.do(job1)

# 每3天執行任務
schedule.every(3).days.do(job1)

# 每1小時執行任務(單數)
schedule.every().hour.do(job1)

# 每3小時執行任務
schedule.every(3).hours.do(job1)

# 每3分鐘執行任務
schedule.every(3).minutes.do(job1)

# 每1秒執行任務(單數)
schedule.every().second.do(job1)

# 每3秒執行任務
schedule.every(3).seconds.do(job1)

# 每天的10:30執行任務
schedule.every().day.at("10:30").do(job1)

# 每個星期三的13:15分執行任務
schedule.every().wednesday.at("13:15").do(job1)

# 每小時的第53分執行任務
schedule.every().hour.at(":53").do(job1)

# 每分鐘的第17秒執行任務
schedule.every().minute.at(":17").do(job1)

#每隔5至10秒執行一次,亂數決定
schedule.every(5).to(10).seconds.do(job1)

"""

import sys
import time
import schedule

print("------------------------------------------------------------")  # 60個


# 無參數重複執行工作
def job1():
    print("無參數 執行工作, 時間 :", time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))


# 有參數重複執行工作
def job2(name):
    # print("Hello", name)
    print(name, "執行工作, 時間 :", time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))


# 只會執行一次工作
def job3_executes_once():
    print("此處編寫的任務只會執行一次... 後面有return CancelJob")
    return schedule.CancelJob


print("schedule：定時執行任務")
schedule.clear()

# schedule.cancel_job()

# 無參數重複執行工作
print("設定每1分鐘執行一次函數 job1()")
schedule.every(1).minutes.do(job1)

# 有參數重複執行工作
print("設定每15秒執行一次函數 job2() + 參數")
schedule.every(15).seconds.do(job2, name="Alice")

# 有參數重複執行工作
print("設定每20秒執行一次函數 job2() + 參數")
schedule.every(20).seconds.do(job2, name="David")

# 只會執行一次工作的
# schedule.every().day.at("11:45").do(job3_executes_once)
print("設定每20秒執行一次函數 job2() + 參數")
print("設定每5分鐘執行一次函數 job3_executes_once(), 但只會執行一次")
schedule.every(5).minutes.do(job3_executes_once)

"""
print("獲取目前所有的作業")
all_jobs = schedule.get_jobs()
print(all_jobs)
"""

print("\n開始檢測是否執行工作\n")

while True:
    schedule.run_pending()  # 檢測是否執行函數
    time.sleep(1)

sys.exit()

print("------------------------------------------------------------")  # 60個

"""
#自動備份檔案程式

import os
import shutil
import datetime

source_dir = "C:/dddddddddd111"
destination_dir = "C:/dddddddddd222"

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    
    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")


schedule.every().day.at("17:13").do(lambda: copy_folder_to_directory(source_dir, destination_dir))

while True:
    schedule.run_pending()  # 檢測是否執行函數
    time.sleep(60)
"""

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


"""
標簽功能

在設置作業的時候，為了后續方便管理作業，你可以給作業打個標簽，這樣你可以通過標簽過濾獲取作業或取消作業。

# Python 實用寶典
import schedule
def say_hello(name):
print("Hello {}".format(name))
# .tag 打標簽
schedule.every().day.do(say_hello, "Andrea").tag("daily-tasks", "friend")
schedule.every().hour.do(say_hello, "John").tag("hourly-tasks", "friend")
schedule.every().hour.do(say_hello, "Monica").tag("hourly-tasks", "customer")
schedule.every().day.do(say_hello, "Derek").tag("daily-tasks", "guest")


# get_jobs(標簽)：可以獲取所有該標簽的任務
friends = schedule.get_jobs("friend")
# 取消所有 daily-tasks 標簽的任務
schedule.clear("daily-tasks")


設定作業截止時間

如果你需要讓某個作業到某個時間截止，你可以通過這個方法：

# Python 實用寶典
import schedule
from datetime import datetime, timedelta, time
def job():
print("Boo")
# 每個小時運行作業，18:30后停止
schedule.every(1).hours.until("18:30").do(job)
# 每個小時運行作業，2030-01-01 18:33 today
schedule.every(1).hours.until("2030-01-01 18:33").do(job)
# 每個小時運行作業，8個小時后停止
schedule.every(1).hours.until(timedelta(hours=8)).do(job)
# 每個小時運行作業，11:32:42后停止
schedule.every(1).hours.until(time(11, 33, 42)).do(job)
# 每個小時運行作業，2020-5-17 11:36:20后停止
schedule.every(1).hours.until(datetime(2020, 5, 17, 11, 36, 20)).do(job)

截止日期之后，該作業將無法運行。

立即運行所有作業，而不管其安排如何

如果某個機制觸發了，你需要立即運行所有作業，可以調用 schedule.run_all() :

# Python 實用寶典
import schedule
def job_1():
print("Foo")
def job_2():
print("Bar")
schedule.every().monday.at("12:40").do(job_1)
schedule.every().tuesday.at("16:40").do(job_2)
schedule.run_all()
# 立即運行所有作業，每次作業間隔10秒
schedule.run_all(delay_seconds=10)

3.高級使用

裝飾器安排作業

如果你覺得設定作業這種形式太啰嗦了，也可以使用裝飾器模式：

# Python 實用寶典
from schedule import every, repeat, run_pending
import time
# 此裝飾器效果等同于 schedule.every(10).minutes.do(job)
@repeat(every(10).minutes)
def job():
print("I am a scheduled job")
while True:
run_pending()
time.sleep(1)

并行執行

默認情況下，Schedule 按順序執行所有作業。其背后的原因是，很難找到讓每個人都高興的并行執行模型。

不過你可以通過多線程的形式來運行每個作業以解決此限制：

# Python 實用寶典
import threading
import time
import schedule
def job1():
print("I"m running on thread %s" % threading.current_thread())
def job2():
print("I"m running on thread %s" % threading.current_thread())
def job3():
print("I"m running on thread %s" % threading.current_thread())
def run_threaded(job_func):
job_thread = threading.Thread(target=job_func)
job_thread.start()
schedule.every(10).seconds.do(run_threaded, job1)
schedule.every(10).seconds.do(run_threaded, job2)
schedule.every(10).seconds.do(run_threaded, job3)
while True:
schedule.run_pending()
time.sleep(1)

日志記錄

Schedule 模塊同時也支持 logging 日志記錄，這么使用：

# Python 實用寶典
import schedule
import logging
logging.basicConfig()
schedule_logger = logging.getLogger("schedule")
# 日志級別為DEBUG
schedule_logger.setLevel(level=logging.DEBUG)
def job():
print("Hello, Logs")
schedule.every().second.do(job)
schedule.run_all()
schedule.clear()

效果如下：

DEBUG:schedule:Running *all* 1 jobs with 0s delay in between
DEBUG:schedule:Running job Job(interval=1, unit=seconds, do=job, args=(), kwargs={})
Hello, Logs
DEBUG:schedule:Deleting *all* jobs

異常處理

Schedule 不會自動捕捉異常，它遇到異常會直接拋出，這會導致一個嚴重的問題：后續所有的作業都會被中斷執行，因此我們需要捕捉到這些異常。

你可以手動捕捉，但是某些你預料不到的情況需要程序進行自動捕獲，加一個裝飾器就能做到了：

# Python 實用寶典
import functools
def catch_exceptions(cancel_on_failure=False):
def catch_exceptions_decorator(job_func):
@functools.wraps(job_func)
def wrapper(*args, **kwargs):
try:
return job_func(*args, **kwargs)
except:
import traceback
print(traceback.format_exc())
if cancel_on_failure:
return schedule.CancelJob
return wrapper
return catch_exceptions_decorator
@catch_exceptions(cancel_on_failure=True)
def bad_task():
return 1 / 0
schedule.every(5).minutes.do(bad_task)

這樣，bad_task 在執行時遇到的任何錯誤，都會被 catch_exceptions 捕獲，這點在保證調度任務正常運轉的時候非常關鍵。



"""
