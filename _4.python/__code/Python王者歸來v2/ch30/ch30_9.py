# ch30_9.py
import threading, time

def wakeUp():
    print("threadObj執行緒開始")
    time.sleep(10)              # threadObj執行緒休息10秒
    print("女朋友生日")
    print("threadObj執行緒結束")
    
print("程式階段1")
threadObj = threading.Thread(target=wakeUp)
threadObj.start()               # threadObj執行緒開始工作
time.sleep(1)                   # 主執行緒休息1秒
print("程式階段2")










