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
    print('AAAAAAAAAAAAA')

print('每3分鐘執行一次函數')          
schedule.every(3).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


