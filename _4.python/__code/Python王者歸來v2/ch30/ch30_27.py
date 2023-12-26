# ch30_27.py
import time
import threading
 
semaphore = threading.BoundedSemaphore(3)                       # 限制計數器最大值
 
def func():
    if semaphore.acquire():                                     # 如果取得鎖
        print (threading.currentThread().getName() + ' 取得鎖')
        print("Working ...")
        time.sleep(2)
        semaphore.release()
        print (threading.currentThread().getName() + ' 釋出鎖')
  
for i in range(5):
    t = threading.Thread(target=func)
    t.start()

