import threading
import time
import random

print("多執行緒")

"""
def t1():
    for i in range(10):
        print('A', end = '')
        time.sleep(random.random())
    print(' t1 結束')

def t2():
    for i in range(10):
        print('B', end = '')
        time.sleep(random.random())
    print(' t2 結束')

def t3(count, mark):
    for i in range(count):
        print(mark, end = '')
        time.sleep(random.random())
    print(' t3 結束')

threading.Thread(target = t1).start()
threading.Thread(target = t2).start()

print('主執行緒結束')

tt1 = threading.Thread(target = t1)
tt2 = threading.Thread(target = t2)
tt3 = threading.Thread(target = t3, kwargs={'count' : 20, 'mark' : 'X'})

tt1.start()
tt2.start()
tt3.start()

tt1.join()
tt2.join()
tt3.join()

print('主執行緒結束')

"""
print("------------------------------------------------------------")  # 60個


def display(name, num):
    i = 1
    while True:
        time.sleep(random.randint(1, 3))
        # time.sleep(1)
        print(name + str(num), " = ", i)
        i += 1


print("多執行緒")

thread1 = threading.Thread(target=display, args=("執行緒", 1))
thread1.start()
# time.sleep(0.3)
thread2 = threading.Thread(target=display, args=("執行緒", 2))
thread2.start()


print("------------------------------------------------------------")  # 60個


import threading
import time


def aa():
    i = 0
    while i < 5:
        i = i + 1
        time.sleep(0.5)
        print("A:", i)


def bb():
    i = 0
    while i < 50:
        i = i + 10
        time.sleep(0.5)
        print("B:", i)


a = threading.Thread(target=aa)  # 建立新的執行緒
b = threading.Thread(target=bb)  # 建立新的執行緒

a.start()  # 啟用執行緒
b.start()  # 啟用執行緒

"""
A: 1
B: 10
A: 2
B: 20
A: 3
B: 30
A: 4
B: 40
A: 5
"""


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch09\code003.py

import threading
import time


def aa():
    i = 0
    while i < 5:
        i = i + 1
        time.sleep(0.5)
        print("A:", i)


def bb():
    i = 0
    while i < 50:
        i = i + 10
        time.sleep(0.5)
        print("B:", i)


def cc():
    i = 0
    while i < 500:
        i = i + 100
        time.sleep(0.5)
        print("C:", i)


a = threading.Thread(target=aa)
b = threading.Thread(target=bb)
c = threading.Thread(target=cc)

a.start()
b.start()
a.join()  # 加入等待 aa() 完成的方法
b.join()  # 加入等待 bb() 完成的方法
c.start()  # 當 aa() 與 bb() 都完成後，才會開始執行 cc()

"""
A: 1
B: 10
A: 2
B: 20
A: 3
B: 30
A: 4
B: 40
A: 5
B: 50
C: 100 <--- A B 都結束後才開始
C: 200
C: 300
C: 400
C: 500
"""


print("------------------------------------------------------------")  # 60個

import time


def aa():
    i = 0
    while i < 5:
        i = i + 1
        time.sleep(0.5)
        print("A:", i)


def bb():
    i = 0
    while i < 100:
        i = i + 10
        time.sleep(0.5)
        print("B:", i)


def cc():
    i = 0
    while i < 500:
        i = i + 100
        time.sleep(0.5)
        print("C:", i)


a = threading.Thread(target=aa)
b = threading.Thread(target=bb)
c = threading.Thread(target=cc)

a.start()
b.start()
a.join()  # 加入等待 aa() 完成的方法
c.start()  # 當 aa() 完成後，就會開始執行 cc()

"""
A: 1
B: 10
A: 2
B: 20
A: 3
B: 30
A: 4
B: 40
A: 5
B: 50
C: 100 <--- A 結束就開始
B: 60
C: 200
B: 70
C: 300
B: 80
C: 400
B: 90
C: 500
B: 100
"""


print("------------------------------------------------------------")  # 60個

import threading
import time


def aa():
    lock.acquire()  # 鎖定
    i = 0
    while i < 5:
        i = i + 1
        time.sleep(0.5)
        print("A:", i)
        if i == 2:
            lock.release()  # i 等於 2 時解除鎖定


def bb():
    lock.acquire()  # 鎖定
    i = 0
    while i < 50:
        i = i + 10
        time.sleep(0.5)
        print("B:", i)
    lock.release()


lock = threading.Lock()  # 建立 Lock
a = threading.Thread(target=aa)
b = threading.Thread(target=bb)

a.start()
b.start()

"""
A: 1
A: 2
B: 10
A: 3
B: 20
A: 4
B: 30
A: 5
B: 40
B: 50
"""

print("------------------------------------------------------------")  # 60個


import threading
import time


def aa():
    event.wait()  # 等待事件被觸發
    event.clear()  # 觸發後將事件回歸原本狀態
    for i in range(1, 6):
        print("A:", i)
        time.sleep(0.5)


def bb():
    for i in range(10, 60, 10):
        if i == 30:
            event.set()  # 觸發事件
        print("B:", i)
        time.sleep(0.5)


event = threading.Event()  # 註冊事件
a = threading.Thread(target=aa)
b = threading.Thread(target=bb)

a.start()
b.start()

"""
B: 10
B: 20
B: 30
A: 1
B: 40
A: 2
B: 50
A: 3
A: 4
A: 5
"""


print("------------------------------------------------------------")  # 60個


import threading
import time


def aa():
    i = 0
    while True:
        event_a.wait()  # 等待 event_a 被觸發
        event_a.clear()  # 還原 event_a 狀態
        for i in range(1, 6):
            print(i)
            time.sleep(0.5)
        event_b.set()  # 觸發 event_b


def bb():
    while True:
        input("輸入任意內容")
        event_a.set()  # 觸發 event_a
        event_b.wait()  # 等待 event_b 被觸發
        event_b.clear()  # 還原 event_b 狀態


event_a = threading.Event()  # 註冊 event_a
event_b = threading.Event()  # 註冊 event_b
a = threading.Thread(target=aa)
b = threading.Thread(target=bb)

a.start()
b.start()

"""
輸入任意內容a
1
2
3
4
5
輸入任意內容b
1
2
3
4
5
輸入任意內容
"""


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
