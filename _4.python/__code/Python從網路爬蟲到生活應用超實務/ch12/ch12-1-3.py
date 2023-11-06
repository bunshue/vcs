from apscheduler.schedulers.blocking import BlockingScheduler
import time 

def task(text):
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime, ": 執行任務...", text)
scheduler = BlockingScheduler() 
scheduler.add_job(task, "interval", minutes=1, args=["工作1"])
start_date = '2020-09-04 14:25:00'
end_date = '2020-09-04 14:28:00'
scheduler.add_job(task, "interval", minutes=1, seconds = 30, 
    start_date=start_date, end_date=end_date, args=["工作2"])
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown() 
