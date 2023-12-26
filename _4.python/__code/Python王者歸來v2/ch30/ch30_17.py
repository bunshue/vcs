# ch30_17.py
import threading
import time

def worker():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(3)
    print(threading.currentThread().getName(), 'Exiting')

w = threading.Thread(name='worker',target=worker)
w.start()
print('start join')
w.join(1.5)             # 等待worker執行緒1.5秒工作完成才往下執行
print("是否working執行緒仍在工作 ? ", w.isAlive())
time.sleep(2)           # 主執行緒休息2秒
print("是否working執行緒仍在工作 ? ", w.isAlive())
print('end join')







