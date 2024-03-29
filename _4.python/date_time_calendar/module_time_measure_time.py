"""
量測時間

"""

import os
import sys
import time
import random
import datetime

print("------------------------------------------------------------")  # 60個

import time

def do_something():
    T = 0.345
    time.sleep(T)

print("量測時間的方法1\t使用time")

time_st = time.time()

do_something()

timeElapsed = time.time() - time_st

timeElapsed = round(timeElapsed, 4)

print("所花時間={}".format(timeElapsed))

print("------------------------------------------------------------")  # 60個

print("量測時間的方法2\t使用perf_counter")

time.perf_counter()

do_something()

timeElapsed = time.perf_counter()
print("所花時間={}".format(timeElapsed))

print("------------------------------------------------------------")  # 60個

print("量測時間的方法3\t使用process_time")
time.process_time()

do_something()

timeElapsed = time.process_time()
print("所花時間={}".format(timeElapsed))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


