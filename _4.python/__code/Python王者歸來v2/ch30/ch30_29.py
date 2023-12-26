# ch30_29.py
import random, time
import threading 

def waiter(event, loop):
    for i in range(loop):
        print(f"{i+1}. 等待flag被設定")
        event.wait()                        # 等待flag
        print("等待完成時間 : ", time.ctime())
        event.clear()                       # 重置flag.
        print()

def setter(event, loop):
    for i in range(loop):
        time.sleep(random.randint(2, 5))    # 休息一段時間再工作
        event.set()                         # 設定flag

event = threading.Event()                   # 建立Event物件
loop = random.randint(3, 6)                 # 迴圈次數

w = threading.Thread(target=waiter, args=(event,loop))
w.start()
s = threading.Thread(target=setter, args=(event,loop))    
s.start()
w.join()
s.join
print("工作完成!")


