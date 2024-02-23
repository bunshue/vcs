# encoding:UTF-8
# 參考：http://violin-tao.blogspot.com/2017/05/python3_26.html

import multiprocessing as p
import time
loc = p.Lock()  # 定義 Lock


def a1():
    global loc
    loc.acquire()  # 鎖住 Lock
    a = 0
    while (a <= 20):
        a = a + 1
        print('a' + str(a))
        time.sleep(0.01)
        if(a == 10):
            loc.release()  # 釋放 Lock


def a2():
    global loc
    a = 0
    while (a <= 20):
        a = a + 1
        print('b' + str(a))
        time.sleep(0.01)
        if(a == 5):
            loc.acquire()  # 鎖住 Lock


p1 = p.Process(target=a1)
p2 = p.Process(target=a2)
p1.start()
p2.start()
