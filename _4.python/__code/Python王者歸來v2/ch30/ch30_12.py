# ch30_12.py
import threading
import time

def worker():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    print(threading.currentThread().getName(), 'Exiting')
def manager():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(3)
    print(threading.currentThread().getName(), 'Exiting')

m = threading.Thread(target=manager)
w = threading.Thread(target=worker)
w2 = threading.Thread(name='Manager',target=worker)
m.start()
w.start()
w2.start()



