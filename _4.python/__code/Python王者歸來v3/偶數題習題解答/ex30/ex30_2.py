# ex30_2.py
import threading, time

def wakeUp(mytime,note,job):
    print(job," 開始")
    starttime = int(time.time())
    while int(time.time()) - starttime < mytime:
        pass
    print(note)
    print(job," 結束")
    
print("程式階段1")
threadObj1 = threading.Thread(target=wakeUp,
                args=[30,'買機票去北京','threadJob1'])
threadObj1.start()              # threadObj1執行緒開始工作
time.sleep(1)                   # 主執行緒休息1秒

threadObj2 = threading.Thread(target=wakeUp,
                args=[60,'送花給女友', 'threadJob2'])
threadObj2.start()              # threadObj1執行緒開始工作
time.sleep(1)                   # 主執行緒休息1秒

print("程式階段2,正常工作")


