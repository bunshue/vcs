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

print("range(5)", range(5))
print("list(range(5))", list(range(5)))

# range
tStart = time.time()

for i in range(10000000):
    pass
tEnd = time.time()

print("range time:", tEnd - tStart)

print("------------------------------------------------------------")  # 60個

# 量測時間
start = time.time()

# do something

end = time.time()

print("經過時間 :", str((end - start) / 60)[0:6] + "分")

print("------------------------------------------------------------")  # 60個

# 量測時間
start = time.time()

# do something

print("elaspe: {0:.6f}".format(time.time() - start))

print("------------------------------------------------------------")  # 60個

# print("time: %fs\n" % (time.time()-start))

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

startTime = time.time()

elapsedTime = time.time() - startTime
print("Time for LinkedList is", elapsedTime, "seconds")

startTime = time.time()

elapsedTime = time.time() - startTime
print("Time for list is", elapsedTime, "seconds")

print("------------------------------------------------------------")  # 60個

import time

startTime = time.time()  # Get start time

endTime = time.time()  # Get end time
runTime = int((endTime - startTime) * 1000)  # Get test time
print(
    "To test if",
    NUMBER_OF_ELEMENTS,
    "elements are in the set\n",
    "The runtime is",
    runTime,
    "milliseconds",
)

startTime = time.time()  # Get start time

endTime = time.time()  # Get end time
runTime = int((endTime - startTime) * 1000)  # Get test time
print(
    "\nTo test if",
    NUMBER_OF_ELEMENTS,
    "elements are in the list\n",
    "The runtime is",
    runTime,
    "milliseconds",
)

startTime = time.time()  # Get start time
endTime = time.time()  # Get end time
runTime = int((endTime - startTime) * 1000)  # Get test time
print(
    "\nTo remove",
    NUMBER_OF_ELEMENTS,
    "elements from the set\n",
    "The runtime is",
    runTime,
    "milliseconds",
)

startTime = time.time()  # Get start time

endTime = time.time()  # Get end time
runTime = int((endTime - startTime) * 1000)  # Get test time
print(
    "\nTo remove",
    NUMBER_OF_ELEMENTS,
    "elements from the list\n",
    "The runtime is",
    runTime,
    "milliseconds",
)

print("------------------------------------------------------------")  # 60個

startTime = time.time()  # Get start time


endTime = time.time()  # Get end time
testTime = int(endTime - startTime)  # Get test time
print(
    "Correct count is",
    correctCount,
    "out of",
    NUMBER_OF_QUESTIONS,
    "\nTest time is",
    testTime,
    "seconds",
)


print("------------------------------------------------------------")  # 60個


import time


def bark(duration):
    _time = time.time
    _sleep = time.sleep

    # We give the parent some time to be ready.
    _sleep(1.0)

    start_time = _time()
    end_time = start_time + duration * 2.0
    i = 0
    while _time() < end_time:
        print("b", end=" ")
        i += 1


bark(0.2)

print("------------------------------------------------------------")  # 60個

print("測試兩事件所經歷的時間 ST")
time_st = time.time()

time.sleep(0.3456)  # 過了一段時間

time_sp = time.time()

time_elapsed = time_sp - time_st

print("耗時 : {0:.6f}".format(time_sp - time_st))

print("測試兩事件所經歷的時間 SP, 經歷時間 : " + str(time_elapsed) + " 秒")
print("經歷時間 " + str(time_elapsed) + " 秒")
print("經歷時間", int(time_elapsed), " 秒")
print("經歷時間 %.2f", time_elapsed)
print("經歷時間 %.2f 秒" % (time_elapsed))

print("取整數秒")
time_elapsed = int(time_sp - time_st)
print("Test time is", time_elapsed, "seconds")

print("------------------------------------------------------------")  # 60個

print("開始計時")
starttime = int(time.time())  # 起始秒數

# 做一件事, 量測時間

endtime = int(time.time())  # 結束秒數
print("所花時間: ", endtime - starttime, " 秒")

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

        start_time = time.time()
        func()
        times = time.time() - start_time
        print('execution time: {}'.format(datetime.timedelta(seconds=times)))



    global_start_time = time.time()
    train_cnn()
    print('训练耗时 (s) : ', time.time() - global_start_time)
    global_start_time = time.time()
    train_cnn()
    print('训练耗时 (s) : ', time.time() - global_start_time)

print("經過時間 : e ", time.time() - startime)

    time_elapsed = time.time() - since
    print('Training complete in {:.0f}m {:.0f}s'.format(
        time_elapsed // 60, time_elapsed % 60))

print(time.time(), " 秒")



start = time.time()

print("耗時 : {0:.6f}".format(time.time() - start))


    begin_time = time.time()
    ret, frame = cap.read()
    
    classes, confs, boxes = nnProcess(frame, model)
    frame = drawBox(frame, classes, confs, boxes, names, colors)

    fps = 'fps: {:.2f}'.format(1 / (time.time() - begin_time))


"""


