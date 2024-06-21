#看 thread
"""

"""

import os
import sys
import time
import random

import threading

print("------------------------------------------------------------")  # 60個

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


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




