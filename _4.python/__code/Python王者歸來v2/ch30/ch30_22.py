# ch30_21.py
import threading
  
class MyThread(threading.Thread):       # 這是threading.Thread的子類別
    def __init__(self):  
        threading.Thread.__init__(self) # 建立執行緒       
    def run(self):
        global data                     # 定義全域資料
#        datalock.acquire()              # 鎖定
        data += 5
        print("data = ", data)
#        datalock.release()              # 解鎖

data = 10                               # 全域最初值
datalock = threading.Lock()             # 建立物件
ts = []                                 # 建立執行緒串列
for t in range(10):
    t = MyThread()
    ts.append(t)                        # 將持行緒加入執行緒串列

for t in ts:                            # 啟動所有執行緒
    t.start()

for t in ts:                            # 等待所有執行緒退出
    t.join()


