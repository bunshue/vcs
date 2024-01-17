# ch13_39.py
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


