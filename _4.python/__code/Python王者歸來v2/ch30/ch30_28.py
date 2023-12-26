# ch30_28.py
import random, time
import threading
                                            
def player():
    name = threading.current_thread().getName()
    time.sleep(random.randint(2,5))
    print(f"{name} 抵達柵欄時間 : {time.ctime()}")
    b.wait()

b = threading.Barrier(4)                # 等待的執行緒數量    
print("比賽開始 …")
for i in range(4):
    t = threading.Thread(target=player)
    t.start()
for i in range(4):                      # 等待執行緒結束
    t.join()
print("比賽結束!")

