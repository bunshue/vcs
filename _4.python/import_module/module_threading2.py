import threading
import time
import random

print("多執行緒")

print("------------------------------------------------------------")  # 60個


import threading


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


import threading


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

import threading
import time


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

import threading
import time


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


import threading
import time


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

import random
import time


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


from threading import Thread


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

import threading
import random
import time


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

import threading
from threading import Thread
import random
import time


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

thr1 = Thread(target=threadConsumer, args=(condition,))
thr2 = Thread(target=threadProducer, args=(condition,))

print("Thread1 consumer start")
thr1.start()
print("Thread2 producer start")
thr2.start()

thr1.join()
thr2.join()

print("All threads stop")


print("------------------------------------------------------------")  # 60個

from threading import Thread
import time


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


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
