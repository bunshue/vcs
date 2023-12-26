# ch30_15.py
import threading
import time

def worker():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(3)
    print(threading.currentThread().getName(), 'Exiting')

w = threading.Thread(name='worker',target=worker)
w.start()
print('start join')
w.join()                # worker執行緒工作完成才往下執行
print('end join')







