"""



"""

import multiprocessing

print(multiprocessing.current_process().name)

print("------------------------------------------------------------")  # 60個


# multiprocessing.Queue - 給多核運算用的佇列

import multiprocessing


def worker(queue):
    print("process 開始")
    while True:
        item = queue.get()
        if item == "STOP":
            print("process 結束")
            break
        print("處理資料:", item)
        time.sleep(0.01)


# 要進行的工作
source = ["AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG"]

process_num = 3

q = multiprocessing.Queue()
for item in source:
    print("加入項目 :", item)
    q.put(item)

processes = []
for _ in range(process_num):
    p = multiprocessing.Process(target=worker, args=(q,))
    p.start()
    processes.append(p)

for _ in range(process_num):
    q.put("STOP")

for p in processes:
    p.join()

print("主程式結束")

print("------------------------------------------------------------")  # 60個


# 參考：http://violin-tao.blogspot.com/2017/05/python3_26.html

import multiprocessing as p

loc = p.Lock()  # 定義 Lock


def a1():
    global loc
    loc.acquire()  # 鎖住 Lock
    a = 0
    while a <= 20:
        a = a + 1
        print("a" + str(a))
        time.sleep(0.01)
        if a == 10:
            loc.release()  # 釋放 Lock


def a2():
    global loc
    a = 0
    while a <= 20:
        a = a + 1
        print("b" + str(a))
        time.sleep(0.01)
        if a == 5:
            loc.acquire()  # 鎖住 Lock


p1 = p.Process(target=a1)
p2 = p.Process(target=a2)
p1.start()
p2.start()

print("------------------------------------------------------------")  # 60個


"""
使用Process类创建多个进程

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""

# 通过下面程序的执行结果可以证实 父进程在创建子进程时复制了进程及其数据结构
# 每个进程都有自己独立的内存空间 所以进程之间共享数据只能通过IPC的方式


from multiprocessing import Process, Queue
from time import sleep


def sub_task(string, q):
    number = q.get()
    while number:
        print("%d: %s" % (number, string))
        sleep(0.001)
        number = q.get()


def main():
    q = Queue(10)
    for number in range(1, 11):
        q.put(number)
    Process(target=sub_task, args=("Ping", q)).start()
    Process(target=sub_task, args=("Pong", q)).start()


if __name__ == "__main__":
    main()


print("------------------------------------------------------------")  # 60個

"""
实现进程间的通信

Version: 0.1
Author: 骆昊
Date: 2018-03-20
"""
import multiprocessing
import os


def sub_task(queue):
    print("子进程进程号:", os.getpid())
    counter = 0
    while counter < 1000:
        queue.put("Pong")
        counter += 1


if __name__ == "__main__":
    print("当前进程号:", os.getpid())
    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=sub_task, args=(queue,))
    p.start()
    counter = 0
    while counter < 1000:
        queue.put("Ping")
        counter += 1
    p.join()
    print("子任务已经完成.")
    for _ in range(2000):
        print(queue.get(), end="")


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
