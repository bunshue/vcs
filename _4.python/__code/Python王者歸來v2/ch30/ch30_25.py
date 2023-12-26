# ch30_25.py
import threading, time, random

def producer():                                         # 生產者狀況                      
    while True:
        condition.acquire()                             # 鎖定
        if len(data) >= 5:                              # 如果產品滿了
            print("生產線是 waiting ...")                   
            condition.wait()                            # 生產者等待
        else:
            data.append(random.randint(1, 100))         # 將產品放入庫存
            print("生產線庫存          ", data)         # 列印庫存
            time.sleep(1)
        condition.notify()                              # 通知
        condition.release()                             # 解鎖

def consumer():                                         # 消費者狀況
    while True:
        condition.acquire()                             # 鎖定
        if not data:                                    # 如果沒有產品
            print("消費者是 waiting ...")
            condition.wait()                            # 消費者等待
        else:
            print("消費者取走商品 : ", data.pop(0))
            print("目前庫存            ", data)         # 列印庫存       
            time.sleep(1)
        condition.notify()                              # 通知
        condition.release()                             # 解鎖

condition = threading.Condition()                       # 建立Condition物件
data = []                                               # 最初化庫存

p = threading.Thread(name='producer',target=producer)   # 建立producer執行緒   
c = threading.Thread(name='consumer',target=consumer)   # 建立consumer執行緒

p.start()
c.start()
p.join()
c.join()


        
