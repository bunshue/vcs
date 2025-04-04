"""

thread 多執行緒

"""

import os
import sys
import time
import random
import threading

print("多執行緒")


"""
线程间通信（共享数据）非常简单因为可以共享同一个进程的内存
进程间通信（共享数据）比较麻烦因为操作系统会保护分配给进程的内存
要实现多进程间的通信通常可以用系统管道、套接字、三方服务来实现
multiprocessing.Queue
守护线程 - daemon thread
守护进程 - firewalld / httpd / mysqld
在系统停机的时候不保留的进程 - 不会因为进程还没有执行结束而阻碍系统停止
"""

print("有參數 thread")


def do_something(content):
    count = 0
    while True:
        print(content, end="")
        time.sleep(0.1)
        count += 1
        if count > 100:
            break
    print("\n", content, "已完成")


threading.Thread(target=do_something, args=("A",), daemon=True).start()
threading.Thread(target=do_something, args=("B",), daemon=True).start()

sys.exit()

print("------------------------------------------------------------")  # 60個

print("無參數 thread")


def run():
    print("啟動了！")
    for i in range(100):
        print(i, end=" ")
    print("完成了！")


thr1 = threading.Thread(target=run)
thr2 = threading.Thread(target=run)

thr1.start()
thr2.start()

print("------------------------------------------------------------")  # 60個

print("有參數 thread")


def run(which):
    print(which, "啟動了！")
    for i in range(100):
        print(which, i)
    print(which, "完成了！")


thr1 = threading.Thread(target=run, args=("1"))
thr2 = threading.Thread(target=run, args=("2"))
thr1.start()
thr2.start()

print("------------------------------------------------------------")  # 60個

print("有參數 thread")


def thread_ex0(name, num):
    print("啟動 thread :", name + str(num))
    i = 1
    while True:
        time.sleep(random.randint(1, 3))
        # time.sleep(1)
        print(name + str(num), " = ", i)
        i += 1
        if i > 10:
            break
    print(name + str(num), "已完成")


print("開兩個 thread, 分別進行")

# 建立新的執行緒
thread_ex0a = threading.Thread(target=thread_ex0, args=("執行緒", 1))
thread_ex0a.start()

# 建立新的執行緒
thread_ex0b = threading.Thread(target=thread_ex0, args=("執行緒", 2))
thread_ex0b.start()

print("------------------------------------------------------------")  # 60個


def t1():
    for i in range(10):
        print("A", end="")
        time.sleep(random.random())
    print(" t1 結束")


def t2():
    for i in range(10):
        print("B", end="")
        time.sleep(random.random())
    print(" t2 結束")


def t3(count, mark):
    for i in range(count):
        print(mark, end="")
        time.sleep(random.random())
    print(" t3 結束")


print("開三個 thread, 分別進行")

tt1 = threading.Thread(target=t1)
tt2 = threading.Thread(target=t2)
tt3 = threading.Thread(target=t3, kwargs={"count": 20, "mark": "C"})

tt1.start()
tt2.start()
tt3.start()

print("等待這三個 thread 分別做完工作")

tt1.join()
tt2.join()
tt3.join()

print("\n全部完成工作")

print("------------------------------------------------------------")  # 60個

print("有參數 thread")


def thread_ex5(name, num):
    print("啟動 thread :", name + str(num))
    i = 0
    while i < num:
        i = i + 1
        time.sleep(1.5)
        print(name + str(num), " = ", i)


thread_ex5a = threading.Thread(target=thread_ex5, args=("執行緒", 5))
thread_ex5b = threading.Thread(target=thread_ex5, args=("執行緒", 50))
thread_ex5c = threading.Thread(target=thread_ex5, args=("執行緒", 500))

thread_ex5a.start()
thread_ex5b.start()
thread_ex5a.join()  # 加入等待 aa() 完成的方法
thread_ex5b.join()  # 加入等待 bb() 完成的方法
thread_ex5c.start()  # 當 aa() 與 bb() 都完成後，才會開始執行 cc()

print("------------------------------------------------------------")  # 60個

thread_ex5a.start()
thread_ex5b.start()
thread_ex5a.join()  # 加入等待 aa() 完成的方法
thread_ex5c.start()  # 當 aa() 完成後，就會開始執行 cc()

print("------------------------------------------------------------")  # 60個

print("無參數 thread, 龜兔賽跑")

LENGTH = 10


# 模擬兔子賽跑的狀況
def rabbitRun():
    progress = 0
    while progress < LENGTH:
        progress += 1
        print("兔子跑了", progress, "公尺")
        time.sleep(1)
        if progress % 7 == 0:
            time.sleep(10)
    print("兔子到達終點！")


# 模擬烏龜賽跑的狀況
def turtleRun():
    progress = 0
    while progress < LENGTH:
        progress += 0.5
        print("烏龜跑了", progress, "公尺")
        time.sleep(1)
    print("烏龜到達終點！")


thr1 = threading.Thread(target=rabbitRun)
thr2 = threading.Thread(target=turtleRun)

print("龜兔賽跑開始！, 總長度 :", LENGTH, "公尺")
thr1.start()
thr2.start()

print("------------------------------------------------------------")  # 60個


class RaceHorse(threading.Thread):
    # 建構式
    def __init__(self, name, stepSizeMin, stepSizeMax, stepFreq):
        # 一定要注意要先執行Thread.__init()__!!
        threading.Thread.__init__(self)
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
        while progress < 20:
            # 用隨機數控制步伐的變異區間，縮放到實際步伐大小
            progress += self._stepSizeMin + random.random() * stepVar
            print(self._name, "跑了", progress, "公尺")
            time.sleep(intv)
        print(self._name, "到達終點！")


horse1 = RaceHorse("劉備", 0.7, 0.75, 3)
horse2 = RaceHorse("關公", 0.6, 0.65, 3.5)
horse3 = RaceHorse("張飛", 0.8, 0.85, 2.8)

horse1.start()
horse2.start()
horse3.start()

print("------------------------------------------------------------")  # 60個

import math

print("模擬網路爬蟲執行的狀況")


def run(name, minDelay, maxDelay):
    intv = maxDelay - minDelay
    delays = []
    for i in range(10):
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


thr1 = threading.Thread(target=run, args=("1號", 3.2, 5.5))
thr2 = threading.Thread(target=run, args=("2號", 4.7, 6.2))

# 執行延遲觀察開始！
thr1.start()
thr2.start()

print("------------------------------------------------------------")  # 60個


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

print("------------------------------------------------------------")  # 60個

# Queue - 可用於多執行緒的佇列

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


def worker():
    print(threading.current_thread().name, "Starting")
    time.sleep(2)
    print(threading.current_thread().name, "Exiting")


def manager():
    print(threading.current_thread().name, "Starting")
    time.sleep(3)
    print(threading.current_thread().name, "Exiting")


thread_ex6_manager = threading.Thread(target=manager)
thread_ex6_worker = threading.Thread(target=worker)

thread_ex6_manager.start()
thread_ex6_worker.start()

print("------------------------------------------------------------")  # 60個


def worker():
    print(threading.current_thread().name, "Starting")
    time.sleep(2)
    print(threading.current_thread().name, "Exiting")


def manager():
    print(threading.current_thread().name, "Starting")
    time.sleep(3)
    print(threading.current_thread().name, "Exiting")


thread_ex7_manager = threading.Thread(target=manager)
thread_ex7_worker = threading.Thread(target=worker)
thread_ex7_worker2 = threading.Thread(name="Manager", target=worker)

thread_ex7_manager.start()
thread_ex7_worker.start()
thread_ex7_worker2.start()

print("------------------------------------------------------------")  # 60個


def childThread(name):
    for i in range(7):
        print(name, i)
        time.sleep(1)


thr1 = threading.Thread(target=childThread, args=("1"))
thr1.start()

for i in range(3):
    print("main", i)
    time.sleep(1)

print("Wait for child thread...")
thr1.join()
print("Child thread stopped")

print("------------------------------------------------------------")  # 60個


class MyThread(threading.Thread):
    def __init__(self, idnum):
        # 必須先初始化Thread!
        threading.Thread.__init__(self)
        self.idnum = idnum

    def run(self):
        for i in range(7):
            print("Thread", self.idnum, i)
            time.sleep(1)


thr1 = MyThread(1)
thr2 = MyThread(2)
thr1.start()
thr2.start()

print("------------------------------------------------------------")  # 60個


def thread1(lock):
    global commonResource
    lock.acquire()
    for i in range(3):
        commonResource += 1
        print(i, "this is the thread1, resource value:", commonResource)
        time.sleep(1)
    lock.release()


def thread2(lock):
    global commonResource
    lock.acquire()
    for i in range(3):
        commonResource -= 1
        print(i, "this is the thread2, resource value:", commonResource)
        time.sleep(1)
    lock.release()


commonResource = 0
lock = threading.Lock()

thr1 = threading.Thread(target=thread1, args=(lock,))
thr2 = threading.Thread(target=thread2, args=(lock,))

print("Thread1 start")
thr1.start()
print("Thread2 start")
thr2.start()

thr1.join()
thr2.join()

print("All threads stop")


print("------------------------------------------------------------")  # 60個


class BankAccount:
    def __init__(self, deposit):
        self.balance = deposit

    def deposit(self, d):
        self.balance += d

    def getBalance(self):
        return self.balance

    def withdraw(self, d):
        # delay on bank electronic operation
        self.delay()
        if self.balance >= d:
            # delay on bank electronic operation
            self.delay()
            self.balance -= d
            # delay on bank electronic operation
            self.delay()
            return True
        # delay on bank electronic operation
        self.delay()
        return False  # unsuccessful withdrawal

    def delay(self):
        rnd = random.randint(1, 2)
        time.sleep(rnd)


class Withdrawer(Thread):
    def __init__(self, bankAccount, name):
        Thread.__init__(self)
        self.bankAccount = bankAccount
        self.moneyGot = 0
        self.name = name

    def run(self):
        while self.bankAccount.getBalance() >= 10:
            if self.bankAccount.withdraw(10):
                self.moneyGot += 10
            else:
                break
            print("This is", self.name, ", I got", self.moneyGot, "now")
            # delay on withdrawer operation
            self.delay()
        print("This is", self.name, ", I got", self.moneyGot, "totally")

    def delay(self):
        rnd = random.randint(1, 2)
        time.sleep(rnd)


acc = BankAccount(500.0)
print("Current bank balance:", acc.getBalance())
p1, p2, p3 = Withdrawer(acc, "John"), Withdrawer(acc, "Mary"), Withdrawer(acc, "Tom")

p1.start()
p2.start()
p3.start()

print("------------------------------------------------------------")  # 60個


class SafeBankAccount:
    def __init__(self, deposit, lock):
        self.balance = deposit
        self.lock = lock

    def deposit(self, d):
        self.balance += d

    def getBalance(self):
        return self.balance

    def withdraw(self, d):
        # lock on
        lock.acquire()  #!!!!!!!!!!!!!!!!!!
        # delay on bank electronic operation
        self.delay()
        if self.balance >= d:
            # delay on bank electronic operation
            self.delay()
            self.balance -= d
            # delay on bank electronic operation
            self.delay()
            # lock off
            lock.release()  #!!!!!!!!!!!!!!!!!!
            return True
        # delay on bank electronic operation
        self.delay()
        # lock off
        lock.release()  #!!!!!!!!!!!!!!!!!!
        return False  # unsuccessful withdrawal

    def delay(self):
        rnd = random.randint(1, 2)
        time.sleep(rnd)


# prepare lock
lock = threading.Lock()

acc = SafeBankAccount(500.0, lock)
print("Current bank balance:", acc.getBalance())
p1, p2, p3 = Withdrawer(acc, "John"), Withdrawer(acc, "Mary"), Withdrawer(acc, "Tom")

p1.start()
p2.start()
p3.start()

print("------------------------------------------------------------")  # 60個


# 消費者thread
def threadConsumer(cond):
    global commonResource

    for i in range(30):
        # 取得 lock
        cond.acquire()
        print("Acquire the condition lock")  # 執行緒進入等待狀況
        if commonResource == 0:
            print("wait")
            cond.wait()  # 喚醒執行緒
        print("notify to wake up")
        cond.notify()

        commonResource -= 1
        print("This is the consumer thread ", commonResource)

        # 釋放 lock
        cond.release()
        delay()


# 生產者thread
def threadProducer(cond):
    global commonResource

    for i in range(30):
        # 取得 lock
        cond.acquire()

        # 喚醒執行緒
        commonResource += 1
        print("This is the producer thread ", commonResource)
        cond.notify()

        # 釋放 lock
        cond.release()
        delay()


def delay():
    time.sleep(random.randint(0, 2))


commonResource = 0
condition = threading.Condition()

thr1 = threading.Thread(target=threadConsumer, args=(condition,))
thr2 = threading.Thread(target=threadProducer, args=(condition,))

print("Thread1 consumer start")
thr1.start()
print("Thread2 producer start")
thr2.start()

thr1.join()
thr2.join()

print("All threads stop")

print("------------------------------------------------------------")  # 60個


class Rabbit(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(10):
            print(self.name, "run", i)
            time.sleep(1)


class Turtle(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(10):
            print(self.name, "run", i)
            time.sleep(2)


rabbit1 = Rabbit("Bunny")
turtle1 = Turtle("Ted")
rabbit1.start()
turtle1.start()

print("------------------------------------------------------------")  # 60個


def job(num):
    print("子執行緒", num)


threads = []
for i in range(3):
    threads.append(threading.Thread(target=job, args=(i,)))
    threads[i].start()

for i in range(3):
    print("主程式", i)

for i in threads:
    i.join()

print("結束")

print("------------------------------------------------------------")  # 60個

from concurrent.futures import ThreadPoolExecutor

a = True  # 定義 a 為 True


def run():
    global a  # 定義 a 是全域變數
    while a:  # 如果 a 為 True
        print(123)  # 不斷顯示 123
        time.sleep(1)  # 每隔一秒


def keyin():
    global a  # 定義 a 是全域變數
    if input() == "a":
        a = False  # 如果輸入的是 a，就讓 a 為 False，停止 run 函式中的迴圈


executor = ThreadPoolExecutor()
e1 = executor.submit(run)
e2 = executor.submit(keyin)
executor.shutdown()

print("------------------------------------------------------------")  # 60個


class MyThreadTest(threading.Thread):
    def __init__(self, count=100):
        threading.Thread.__init__(self)
        self.my_count = 200
        self.flag_signal = True
        print("flag_signal = True")

    def run(self):
        while self.flag_signal:
            print("r", end=" ")

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
    print(_, end=" ")
    time.sleep(1)

t1.stop_my_thread()

now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print("現在時間 :", now)

record_time_elapsed = time.time() - record_time_st
print("作業時間 :", format(record_time_elapsed, ".2f"), "秒")

print("------------------------------------------------------------")  # 60個


# 定義下載漫畫的函數
def do_my_thread(idx, cnt):
    # print(text, cnt)
    # print(cnt)
    time.sleep(0.8)
    print(idx, end="")


# 建立並啟動多個執行緒
thread_count = 10  # 執行緒的數量

# 建立執行緒並將它們添加到執行緒串列表
threads = []
for i in range(10):
    # print('建立 thread :', i)
    cnt = random.randint(5, 10)
    thread = threading.Thread(target=do_my_thread, args=(i, cnt))
    threads.append(thread)
    thread.start()  # 啟動執行緒

# 等待所有執行緒完成
for thread in threads:
    thread.join()

print("\n完成")

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

"""

lock = threading.Lock()  # 建立 Lock

    #lock.acquire()  # 鎖定
            lock.acquire()  # 鎖定
            lock.release()  # 解除鎖定
    #lock.acquire()  # 鎖定
    #lock.release()


print("------------------------------------------------------------")  # 60個


"""
