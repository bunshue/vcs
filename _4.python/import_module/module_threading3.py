import threading
import time
import random

print("多執行緒")

print("------------------------------------------------------------")  # 60個


from threading import Thread
import time


# 模擬兔子賽跑的狀況
def rabbitRun():
    progress = 0
    while progress < 30:
        progress += 1
        print("兔子跑了", progress, "公尺")
        time.sleep(1)
        if progress % 7 == 0:
            time.sleep(10)
    print("兔子到達終點！")


# 模擬烏龜賽跑的狀況
def turtleRun():
    progress = 0
    while progress < 30:
        progress += 0.5
        print("烏龜跑了", progress, "公尺")
        time.sleep(1)
    print("烏龜到達終點！")


thr1 = Thread(target=rabbitRun)
thr2 = Thread(target=turtleRun)
# 龜兔賽跑開始！
thr1.start()
thr2.start()


print("------------------------------------------------------------")  # 60個

from threading import Thread
import random
import time


class RaceHorse(Thread):
    # 建構式
    def __init__(self, name, stepSizeMin, stepSizeMax, stepFreq):
        # 一定要注意要先執行Thread.__init()__!!
        Thread.__init__(self)
        self._name = name
        self._stepSizeMin = stepSizeMin
        self._stepSizeMax = stepSizeMax
        self._stepFreq = stepFreq

    # 覆寫Thread的run()方法
    def run(self):
        # 步伐的變異區間大小
        stepVar = self._stepSizeMax - self._stepSizeMin
        # 每次間隔時間，是步伐頻率的倒數
        intv = 1.0 / self._stepFreq
        progress = 0
        while progress < 100:
            # 用隨機數控制步伐的變異區間，縮放到實際步伐大小
            progress += self._stepSizeMin + random.random() * stepVar
            print(self._name, "跑了", progress, "公尺")
            time.sleep(intv)
        print(self._name, "到達終點！")


horse1 = RaceHorse("席爾巴斯雷利", 0.7, 0.75, 3)
horse2 = RaceHorse("波爾薩利諾", 0.6, 0.65, 3.5)
horse3 = RaceHorse("波雅漢考克", 0.8, 0.85, 2.8)

horse1.start()
horse2.start()
horse3.start()

print("------------------------------------------------------------")  # 60個

from threading import Thread
import time
import math
import random


# 模擬網路爬蟲執行的狀況
def run(name, minDelay, maxDelay):
    intv = maxDelay - minDelay
    delays = []
    for i in range(100):
        delay = minDelay + random.random() * intv
        delays.append(delay)
        # 計算平均值！
        mean = sum(delays) / len(delays)
        # 計算標準差！
        sqsum = sum([(d - mean) * (d - mean) for d in delays])
        stdev = math.sqrt(sqsum / len(delays))
        print((i + 1), "執行緒", name, "目前的平均值：", mean, ", 標準差：", stdev)
        time.sleep(delay)
    print("done!")


thr1 = Thread(target=run, args=("1號", 3.2, 5.5))
thr2 = Thread(target=run, args=("2號", 4.7, 6.2))
# 執行延遲觀察開始！
thr1.start()
thr2.start()


print("------------------------------------------------------------")  # 60個

import threading


def wakeUp(mytime, note, job):
    print(job, " 開始")
    starttime = int(time.time())
    while int(time.time()) - starttime < mytime:
        pass
    print(note)
    print(job, " 結束")


print("程式階段1")
threadObj1 = threading.Thread(target=wakeUp, args=[30, "買機票去北京", "threadJob1"])
threadObj1.start()  # threadObj1執行緒開始工作
time.sleep(1)  # 主執行緒休息1秒

threadObj2 = threading.Thread(target=wakeUp, args=[60, "送花給女友", "threadJob2"])
threadObj2.start()  # threadObj1執行緒開始工作
time.sleep(1)  # 主執行緒休息1秒

print("程式階段2,正常工作")

print("------------------------------------------------------------")  # 60個

import threading

a = input("按下任意鍵開始")
b = True
t = 0


def loop_a():
    global t  # 設定全域變數
    global b
    while b == True:
        t = t + 0.01
        time.sleep(0.01)


def loop_b():
    global b
    global t
    b = input("按下任意鍵停止")
    t = round(t * 100) / 100
    print(t)


# 跑多線程
thread1 = threading.Thread(target=loop_a)
thread1.start()
thread2 = threading.Thread(target=loop_b)
thread2.start()

print("------------------------------------------------------------")  # 60個

# LifoQueue - 可用於多執行緒的堆疊

import threading
import queue

# 要進行的工作
source = ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG"]
threads_num = 3

q = queue.LifoQueue()
for item in source:
    print("加入項目 :", item)
    q.put(item)


def worker():
    print("執行緒開始 ")
    while True:
        item = q.get()
        if item == "STOP":
            print("執行緒結束 ")
            break
        print("處理資料: ", item)
        time.sleep(0.01)
        q.task_done()


threads = []
for _ in range(threads_num):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

q.join()

for _ in range(threads_num):
    q.put("STOP")

for t in threads:
    t.join()

print("主程式結束")

sys.exit()

print("------------------------------------------------------------")  # 60個

# Queue - 可用於多執行緒的佇列

import threading
import queue

# 要進行的工作
source = ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG"]
threads_num = 3

q = queue.Queue()
for item in source:
    print("加入項目 :", item)
    q.put(item)


def worker():
    print("執行緒開始")
    while True:
        item = q.get()
        if item == "STOP":
            print("執行緒結束")
            break
        print("處理資料:", item)
        time.sleep(1)
        q.task_done()


threads = []
for _ in range(threads_num):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

q.join()

for _ in range(threads_num):
    q.put("STOP")

for t in threads:
    t.join()

print("主程式結束")

print("------------------------------------------------------------")  # 60個

# PriorityQueue - 可用於多執行緒的 heapq

import threading
import queue

# 要進行的工作
source = ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG"]

source = ["2-吃飯", "1-睡覺", "3-寫程式", "7-散步", "5-聽音樂", "6-打牌", "4-玩電動"]
threads_num = 3

q = queue.PriorityQueue()
for item in source:
    print("加入項目 :", item)
    q.put(item)


def worker():
    print("執行緒開始")
    while True:
        item = q.get()
        if item == "STOP":
            print("執行緒結束")
            break
        print("處理資料:", item)
        time.sleep(0.01)
        q.task_done()


threads = []
for _ in range(threads_num):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

q.join()

for _ in range(threads_num):
    q.put("STOP")

for t in threads:
    t.join()

print("主程式結束")

print("------------------------------------------------------------")  # 60個

import threading


def wakeUp():
    print("threadObj執行緒開始")
    time.sleep(10)  # threadObj執行緒休息10秒
    print("女朋友生日")
    print("threadObj執行緒結束")


print("程式階段1")
threadObj = threading.Thread(target=wakeUp)
threadObj.start()  # threadObj執行緒開始工作
time.sleep(1)  # 主執行緒休息1秒
print("程式階段2")

print("------------------------------------------------------------")  # 60個

import threading


def wakeUp(name, blessingWord):
    print("threadObj執行緒開始")
    time.sleep(10)  # threadObj執行緒休息10秒
    print(name, " ", blessingWord)
    print("threadObj執行緒結束")


print("程式階段1")
threadObj = threading.Thread(target=wakeUp, args=["NaNa", "生日快樂"])
threadObj.start()  # threadObj執行緒開始工作
time.sleep(1)  # 主執行緒休息1秒
print("程式階段2")

print("------------------------------------------------------------")  # 60個

import threading
import time


def worker():
    print(threading.current_thread().name, "Starting")
    time.sleep(2)
    print(threading.current_thread().name, "Exiting")


def manager():
    print(threading.current_thread().name, "Starting")
    time.sleep(3)
    print(threading.current_thread().name, "Exiting")


m = threading.Thread(target=manager)
w = threading.Thread(target=worker)
m.start()
w.start()

print("------------------------------------------------------------")  # 60個

import threading
import time


def worker():
    print(threading.current_thread().name, "Starting")
    time.sleep(2)
    print(threading.current_thread().name, "Exiting")


def manager():
    print(threading.current_thread().name, "Starting")
    time.sleep(3)
    print(threading.current_thread().name, "Exiting")


m = threading.Thread(target=manager)
w = threading.Thread(target=worker)
w2 = threading.Thread(name="Manager", target=worker)
m.start()
w.start()
w2.start()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
