# ch30_19.py
import threading  
  
class MyThread(threading.Thread):       # 這是threading.Thread的子類別
    def __init__(self):  
        threading.Thread.__init__(self) # 建立執行緒       
    def run(self):                      # 定義執行緒的工作
        print(threading.Thread.getName(self))
        print("Happy Python")
  
a = MyThread()                          # 建立執行緒物件a
a.run()                                 # 啟動執行緒a
a.run()                                 # 啟動執行緒a       
b = MyThread()                          # 建立執行緒物件b
b.start()                               # 啟動執行緒b
