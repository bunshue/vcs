from apscheduler.schedulers.blocking import BlockingScheduler
import time, datetime 

def task(text):
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime, ": 執行任務...", text)
scheduler = BlockingScheduler() 
run_date = datetime.date(2020,9,4)
scheduler.add_job(task, "date", run_date=run_date, args=["工作1"])
run_date = datetime.datetime(2020,9,4,14,10,0)
scheduler.add_job(task, "date", run_date=run_date, args=["工作2"])
run_date = "2020-9-4 14:15:00"
scheduler.add_job(task, "date", run_date=run_date, args=["工作3"])
try:
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown() 
