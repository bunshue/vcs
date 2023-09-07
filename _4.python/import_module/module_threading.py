import threading
import time
import random

print('多執行緒')

'''
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

'''
print('------------------------------------------------------------')	#60個


def display(name, num):
    i = 1
    while True:
        time.sleep(random.randint(1, 3))
        #time.sleep(1)
        print(name + str(num), ' = ', i)
        i += 1

print('多執行緒')

thread1 = threading.Thread(target = display, args = ("執行緒", 1))
thread1.start()
#time.sleep(0.3)
thread2 = threading.Thread(target = display, args = ("執行緒", 2))
thread2.start()
                           





print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



