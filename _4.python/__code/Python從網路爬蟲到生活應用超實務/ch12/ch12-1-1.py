from apscheduler.schedulers.blocking import BlockingScheduler
import time 

def task():
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime, ": 執行任務...")
scheduler = BlockingScheduler() 
scheduler.add_job(task, "interval", seconds=3)
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown() 
