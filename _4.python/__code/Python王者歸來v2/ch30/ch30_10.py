# ch30_10.py
import threading, time

def wakeUp(name, blessingWord):
    print("threadObj執行緒開始")
    time.sleep(10)              # threadObj執行緒休息10秒
    print(name, " ", blessingWord)
    print("threadObj執行緒結束")
    
print("程式階段1")
threadObj = threading.Thread(target=wakeUp, args=['NaNa','生日快樂'])
threadObj.start()               # threadObj執行緒開始工作
time.sleep(1)                   # 主執行緒休息1秒
print("程式階段2")


