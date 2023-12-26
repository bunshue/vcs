# ch30_26.py
import threading, time, random, queue

bufSize = 10
q = queue.Queue(bufSize)                                # 建立queue,最多10筆

def producer():                                         # 生產者狀況                      
    while True:
        if not q.full():                                # 如果queue有空間
            item = random.randint(1,100)                # 生產產品
            q.put(item)                                 # 將產品放入庫存
            print(f"生產者Putting存入 {str(item):2s} : queue數量 {str(q.qsize())}")
            time.sleep(2)                               # 休息2秒
            
def consumer():                                         # 消費者狀況
    while True:
        if not q.empty():                               # 如果queue不是空的
            item = q.get()                              # 消欸產品
            print(f"消費者Getting取得 {str(item):2s} : queue數量 {str(q.qsize())}")      
            time.sleep(2)                               # 休息2秒

p = threading.Thread(name='producer',target=producer)   # 建立producer執行緒   
c = threading.Thread(name='consumer',target=consumer)   # 建立consumer執行緒
p.start()
time.sleep(2)
c.start()
time.sleep(2)



        
