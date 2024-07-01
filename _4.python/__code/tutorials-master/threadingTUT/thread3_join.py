import time
import threading

def job_thread1():
    print('T1 start\n')
    time.sleep(0.3)
    print('T1 finish\n')

def job_thread2():
    print('T2 start\n')
    time.sleep(0.4)
    print('T2 finish\n')

thread1 = threading.Thread(target=job_thread1, name='T1')
thread2 = threading.Thread(target=job_thread2, name='T2')
thread1.start()
thread2.start()

time.sleep(5)

thread2.join()
thread1.join()

print('all done\n')
