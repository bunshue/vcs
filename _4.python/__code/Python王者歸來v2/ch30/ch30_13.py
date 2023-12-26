# ch30_13.py
import threading
import time

def daemonFun():                                                # 定義Daemon
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(5)
    print(threading.currentThread().getName(), 'Exiting')
def non_daemon():                                               # 定義非Daemon
    print(threading.currentThread().getName(), 'Starting')
    print(threading.currentThread().getName(), 'Exiting')

d = threading.Thread(name='daemon', target=daemonFun)           # 建立Daemon
d.setDaemon(True)                                               # 設為True
nd = threading.Thread(name='non-daemon', target=non_daemon)     # 建立非Daemon

d.start()
nd.start()
