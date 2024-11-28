"""
量測時間

"""

import os
import sys
import time
import random
import datetime

print("------------------------------------------------------------")  # 60個


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

print("量測時間 ST")
# Start the stopwatch / counter
t1_start = time.perf_counter()

time.sleep(0.3456)  # 過了一段時間

# Stop the stopwatch / counter
t1_stop = time.perf_counter()

print("量測時間 SP")
print(t1_stop, t1_start)
print(t1_stop - t1_start, "秒")

from time import perf_counter_ns

print("量測時間 ST")
# Start the stopwatch / counter
t1_start = time.perf_counter_ns()

time.sleep(0.3456)  # 過了一段時間

# Stop the stopwatch / counter
t1_stop = time.perf_counter_ns()

print("量測時間 SP")
print(t1_stop, "ns", t1_start, "ns")

print(t1_stop - t1_start, "ns")

start = time.time()

time.sleep(0.3456)  # 過了一段時間

stop = time.time()

print(stop - start)


print("------------------------------------------------------------")  # 60個

print("我有一句話想對你說:")
time.sleep(1)  # 程式停1秒
print("學習Python的過程唯然漫長,但最終的果實是甜美的")
print("程式執行到目前的時間是" + str(time.process_time()))
time.sleep(2)  # 程式停2秒
print("程式執行到目前的時間是" + str(time.perf_counter()))


print("我有一句話想對你說:")
t.sleep(0.1)  # 程式停0.1秒
print("學習Python的過程唯然漫長,但最終的果實是甜美的")
print("程式執行到目前的時間是" + str(t.process_time()))
t.sleep(0.2)  # 程式停0.2秒
print("程式執行到目前的時間是" + str(t.perf_counter()))


print("------------------------------------------------------------")  # 60個


print("開始執行到目前的時間:" + str(time.perf_counter()))
time.sleep(2)
print("程式執行時間經過:" + str(time.perf_counter()) + "秒")
time.sleep(3)
print("程式執行時間經過:" + str(time.perf_counter()) + "秒")

print("------------------------------------------------------------")  # 60個


# 模組與套件 clock() python3.8後改為perf_counter()
# print("開始執行到目前的時間:"+str(time.perf_counter()))
print("開始執行到目前的時間:" + str(time.perf_counter()))
time.sleep(2)
print("程式執行時間經過:" + str(time.perf_counter()) + "秒")
time.sleep(3)
print("程式執行時間經過:" + str(time.perf_counter()) + "秒")

print("------------------------------------------------------------")  # 60個

timestart = time.perf_counter()
for i in range(0, 5000):
    for j in range(0, 1000):
        n = i * j
timeend = time.perf_counter()
print("執行五百萬次整數運算的時間:" + str(timeend - timestart) + "秒")


print("------------------------------------------------------------")  # 60個

# 能計算時間長度的產生器


def elapsed_time_gen():
    last_time = time.perf_counter()
    while True:
        now = time.perf_counter()
        yield now - last_time
        last_time = now


elapsed_time = elapsed_time_gen()

for _ in range(5):
    time.sleep(random.randint(1, 10) / 10)
    print(next(elapsed_time))


print("------------------------------------------------------------")  # 60個


import re


def timefunc(n, func, *args, **kw):
    t0 = time.perf_counter()
    try:
        for i in range(n):
            result = func(*args, **kw)
        return result
    finally:
        t1 = time.perf_counter()
        if n > 1:
            print(n, "times", end=" ")
        print(func.__name__, "%.3f" % (t1 - t0), "CPU seconds")


s = "\13hello\14 \13world\14 " * 1000
p = re.compile(r"([\13\14])")
timefunc(10, p.sub, "", s)
timefunc(10, p.split, s)
timefunc(10, p.findall, s)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


"""
perf_counter()	取得程式執行的時間
t1 程式啟動 t1
t2 perf_counter() 取得t2-t1
t3 perf_counter() 取得t3-t2

t0 = time.perf_counter()
L.sort()
t1 = time.perf_counter()
print("%6.2f" % (t1-t0), end=' ')
flush()
"""
