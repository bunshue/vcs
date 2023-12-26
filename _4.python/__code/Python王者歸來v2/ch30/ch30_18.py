# ch30_18.py
import threading
import time

def worker():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(5)
    print(threading.currentThread().getName(), 'Exiting')
def manager():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(5)
    print(threading.currentThread().getName(), 'Exiting')
    
w = threading.Thread(name='worker',target=worker)
w.start()
print('worker start join')
w.join(1.5)             # 等待worker執行緒1.5秒工作完成才往下執行
print('worker end join')
m = threading.Thread(name='manager',target=worker)
m.start()
print('manager start join')
w.join(1.5)             # 等待manager執行緒1.5秒工作完成才往下執行
print('manager end join')
print(f"目前共有 {threading.active_count()} 執行緒在工作")
for thread in threading.enumerate():
    print("執行緒名稱 : ", thread.name)









