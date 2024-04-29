"""
Schedule—簡單實用的 Python 周期任務調度工具

周期性地執行某個 Python 腳本
1. Crontab
2. Celery
3. Schedule

"""

import schedule
import time


def job():
    print("執行工作, 時間 :", time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))


def job_that_executes_once():
    print("此處編寫的任務只會執行一次... 後面有return CancelJob")
    return schedule.CancelJob


def say_hello(name):
    print("Hello", name)


print("設定每3分鐘執行一次函數")
schedule.every(1).minutes.do(job)

# 只會執行一次的
# schedule.every().day.at("11:45").do(job_that_executes_once)
schedule.every(5).minutes.do(job_that_executes_once)

# do() 將額外的參數傳遞給job函數
# 每幾秒呼叫一次 Alice
schedule.every(15).seconds.do(say_hello, name="Alice")

# 每幾秒呼叫一次 Bob
schedule.every(20).seconds.do(say_hello, name="Bob")


print("獲取目前所有的作業")
all_jobs = schedule.get_jobs()
print(all_jobs)

while True:
    schedule.run_pending()  # 檢測是否執行函數
    time.sleep(1)

"""
# 每十分鐘執行任務
schedule.every(10).minutes.do(job)
# 每個小時執行任務
schedule.every().hour.do(job)
# 每天的10:30執行任務
schedule.every().day.at("10:30").do(job)
# 每個月執行任務
schedule.every().monday.do(job)
# 每個星期三的13:15分執行任務
schedule.every().wednesday.at("13:15").do(job)
# 每分鐘的第17秒執行任務
schedule.every().minute.at(":17").do(job)
"""


"""
print('schedule：定時執行任務')

import schedule


schedule.clear()

cnt = 0

def job():
    global cnt
    print('工作示範, ', cnt)
    cnt += 1
    if cnt == 10:
        print('結束工作')#尚有問題
        schedule.clear()
        #schedule.cancel_job()


schedule.every(3).seconds.do(job)
# schedule.every(3).minutes.do(job)
# schedule.every(3).hours.do(job)
# schedule.every(3).days.do(job)
# schedule.every(3).weeks.do(job)

# schedule.every().minute.at(":43").do(job)
# schedule.every().hour.at(":53").do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().wednesday.at("13:15").do(job)

# schedule.every(5).to(10).seconds.do(job)  #每隔5至10秒執行一次,亂數決定

while True:
    schedule.run_pending()


print('kkkkkk')
"""


"""
#自動備份檔案程式

import os
import shutil
import datetime
import schedule
import time

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
    schedule.run_pending()
    time.sleep(60)
"""
