# ch30_10.py
import threading
import time

def worker():
    print(threading.current_thread().name, 'Starting')
    time.sleep(2)
    print(threading.current_thread().name, 'Exiting')
def manager():
    print(threading.current_thread().name, 'Starting')
    time.sleep(3)
    print(threading.current_thread().name, 'Exiting')

m = threading.Thread(target=manager)
w = threading.Thread(target=worker)
w2 = threading.Thread(name='Manager',target=worker)
m.start()
w.start()
w2.start()



