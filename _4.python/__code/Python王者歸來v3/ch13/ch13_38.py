# ch13_38.py
import time

def log_event(event):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"{timestamp} : {event}")

# 假設發生了一個事件
log_event("User login")


