# encoding:UTF-8
import time
import math
import threading

a = input('按下任意鍵開始')
b = True
t = 0


def loop_a():
    global t  # 設定全域變數
    global b
    while (b == True):
        t = t + 0.01
        time.sleep(0.01)


def loop_b():
    global b
    global t
    b = input('按下任意鍵停止')
    t = round(t * 100)/100
    print(t)


# 跑多線程
thread1 = threading.Thread(target=loop_a)
thread1.start()
thread2 = threading.Thread(target=loop_b)
thread2.start()
