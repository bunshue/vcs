#看 thread
"""

"""

import os
import sys
import time
import random

import threading

print("------------------------------------------------------------")  # 60個
'''
class MyThreadTest(threading.Thread):

    def __init__(self, count=100):
        threading.Thread.__init__(self)
        self.my_count = 200
        self.flag_signal = True
        print("flag_signal = True")

    def run(self):
        while self.flag_signal:
            print('r', end = " ")
           
    def stop_my_thread(self):
        self.flag_signal = False
        print("flag_signal = False")

count = 123
t1 = MyThreadTest(count)
t1.start()

import datetime
now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print("現在時間 :", now)
record_time_st = time.time()

for _ in range(10):
    print(_, end = " ")
    time.sleep(1)
    
t1.stop_my_thread()

now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print("現在時間 :", now)

record_time_elapsed = time.time() - record_time_st
print('作業時間 :', format(record_time_elapsed, ".2f"), '秒')

print("------------------------------------------------------------")  # 60個
'''

print("------------------------------------------------------------")  # 60個

import time
import random
import threading

# 定義下載漫畫的函數
def do_my_thread(idx, cnt):
    #print(text, cnt)
    #print(cnt)
    time.sleep(0.8)
    print(idx, end = "")

# 建立並啟動多個執行緒
thread_count = 10                                       # 執行緒的數量

# 建立執行緒並將它們添加到執行緒串列表
threads = []
for i in range(10):
    #print('建立 thread :', i)
    cnt = random.randint(5, 10)
    thread = threading.Thread(target=do_my_thread, args=(i, cnt))
    threads.append(thread)
    thread.start()                                      # 啟動執行緒

# 等待所有執行緒完成
for thread in threads:
    thread.join()

print('\n完成')

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




