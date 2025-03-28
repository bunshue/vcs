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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("量測時間的方法1\t使用time")

time_st = time.time()

do_something()

time_sp = time.time()

time_diff = time_sp - time_st

print(f"經歷時間: {time_diff}秒")

print("經歷時間 : {}".format(datetime.timedelta(seconds=time_diff)))
print("經歷時間 : {}".format(time_diff))
print("經歷時間 : {0:.6f}".format(time_diff))
print("經歷時間 :", str(time_diff), "秒")
print("經歷時間 :", int(time_diff), "秒")
print("經歷時間 %.2f 秒", time_diff)
print("經歷時間 %.2f 秒" % (time_diff))
print("經歷時間 :", time_diff, "秒")
print("經歷時間 :", str((time_diff) / 60)[0:6] + "分")

print("time {:.0f}m {:.0f}s".format(time_diff // 60, time_diff % 60))
print("time: %f s\n" % (time.time() - time_st))

time_diff = round(time_diff, 4)

print("取整數秒")
time_diff = int(time_diff)
print("經歷時間 :", time_diff, "秒")

time_diff = int(time_sp - time_st)
time_diff = int((time_diff) * 1000)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("量測時間的方法2\t使用perf_counter")

time.perf_counter()

do_something()

time_diff = time.perf_counter()
print("所花時間={}".format(time_diff))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("量測時間的方法3\t使用process_time")
time.process_time()

do_something()

time_diff = time.process_time()
print("所花時間={}".format(time_diff))

print("------------------------------------------------------------")  # 60個

print("量測時間 ST")
# Start the stopwatch / counter
t1_start = time.perf_counter()

do_something()

# Stop the stopwatch / counter
t1_stop = time.perf_counter()

print("量測時間 SP")
print(t1_stop, t1_start)
print(t1_stop - t1_start, "秒")

from time import perf_counter_ns

print("量測時間 ST")
# Start the stopwatch / counter
t1_start = time.perf_counter_ns()

do_something()

# Stop the stopwatch / counter
t1_stop = time.perf_counter_ns()

print("量測時間 SP")
print(t1_stop, "ns", t1_start, "ns")

print(t1_stop - t1_start, "ns")

print("------------------------------------------------------------")  # 60個

print("我有一句話想對你說:")
do_something()
print("學習Python的過程唯然漫長,但最終的果實是甜美的")
print("程式執行到目前的時間是" + str(time.process_time()))
do_something()
print("程式執行到目前的時間是" + str(time.perf_counter()))

print("我有一句話想對你說:")
do_something()
print("學習Python的過程唯然漫長,但最終的果實是甜美的")
print("程式執行到目前的時間是" + str(t.process_time()))
do_something()
print("程式執行到目前的時間是" + str(t.perf_counter()))

print("------------------------------------------------------------")  # 60個

print("開始執行到目前的時間:" + str(time.perf_counter()))
do_something()
print("程式執行時間經過:" + str(time.perf_counter()) + "秒")
do_something()
print("程式執行時間經過:" + str(time.perf_counter()) + "秒")

print("------------------------------------------------------------")  # 60個

# 模組與套件 clock() python3.8後改為perf_counter()
# print("開始執行到目前的時間:"+str(time.perf_counter()))
print("開始執行到目前的時間:" + str(time.perf_counter()))
do_something()
print("程式執行時間經過:" + str(time.perf_counter()) + "秒")
do_something()
print("程式執行時間經過:" + str(time.perf_counter()) + "秒")

print("------------------------------------------------------------")  # 60個

time_st = time.perf_counter()

do_something()

time_sp = time.perf_counter()

time_diff = time_sp - time_st

print("時間:" + str(time_diff) + "秒")

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

start_calc = time.time()
x = factorial(C.Decimal(n), 0)
end_calc = time.time()


start_conv = time.time()
sx = str(x)
end_conv = time.time()

print("cdecimal:")
print("calculation time: %fs" % (end_calc - start_calc))
print("conversion time: %fs\n" % (end_conv - start_conv))

# Python integers
start_calc = time.time()
y = factorial(n, 0)
end_calc = time.time()
start_conv = time.time()
sy = str(y)
end_conv = time.time()

print("int:")
print("calculation time: %fs" % (end_calc - start_calc))
print("conversion time: %fs\n\n" % (end_conv - start_conv))

print("------------------------------------------------------------")  # 60個


def bark(duration):
    _time = time.time
    _sleep = time.sleep

    # We give the parent some time to be ready.
    _sleep(1.0)

    time_st = _time()
    end_time = time_st + duration * 2.0
    i = 0
    while _time() < end_time:
        print("b", end=" ")
        i += 1


bark(0.2)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


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


"""

    begin_time = time.time()
    ret, frame = cap.read()
    
    classes, confs, boxes = nnProcess(frame, model)
    frame = drawBox(frame, classes, confs, boxes, names, colors)

    fps = 'fps: {:.2f}'.format(1 / (time.time() - begin_time))


"""


start = time.time()

# .....
time1 = time.time() - start
print("Python 的計算結果：%f[sec]" % float(time1))

start = time.time()

# ......
time2 = time.time() - start
print("NumPy 的計算結果：%f[sec]" % float(time2))

if time2 < 0.000001:
    time2 = 0.000001
print("使用numpy快了 ", time1 / time2, " 倍")
