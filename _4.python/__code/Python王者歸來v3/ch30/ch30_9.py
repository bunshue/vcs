# ch30_9.py
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
m.start()
w.start()



