from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', minute='*/20')
def scheduled_job():
    url = "https://for-dr-master.herokuapp.com/"
    conn = urllib.request.urlopen(url)
        
    for key, value in conn.getheaders():
        print(key, value)

sched.start()