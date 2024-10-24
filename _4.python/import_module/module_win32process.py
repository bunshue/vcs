import sys
import time

SYSTIMES_IMPLEMENTATION = None
USE_WIN32PROCESS_GETPROCESSTIMES = 'win32process.GetProcessTimes()'

import win32process
SYSTIMES_IMPLEMENTATION = USE_WIN32PROCESS_GETPROCESSTIMES

WIN32_PROCESS_TIMES_TICKS_PER_SECOND = 1e7
def win32process_getprocesstimes_systimes():
    d = win32process.GetProcessTimes(win32process.GetCurrentProcess())
    return (d['UserTime'] / WIN32_PROCESS_TIMES_TICKS_PER_SECOND,
            d['KernelTime'] / WIN32_PROCESS_TIMES_TICKS_PER_SECOND)

systimes = win32process_getprocesstimes_systimes

def processtime():
    user, system = systimes()
    return user + system

def some_workload1():
    x = 0
    for i in range(10000000):
        x = x + 1
    print(x)

def some_workload2():
    x = 0.0
    for i in range(10000000):
        x += i
    print(x)

if __name__ == '__main__':
    print('Using %s as timer' % SYSTIMES_IMPLEMENTATION)
    print()
    
    print('Testing systimes() under load conditions')
    t0 = systimes()
    some_workload1()
    t1 = systimes()
    print('before:', t0)
    print('after:', t1)
    print('differences:', (t1[0] - t0[0], t1[1] - t0[1]))


    print('Testing systimes() under load conditions')
    t0 = systimes()
    some_workload1()
    t1 = systimes()
    print('before:', t0)
    print('after:', t1)
    print('differences:', (t1[0] - t0[0], t1[1] - t0[1]))
    

    print('Testing systimes() under load conditions 2222')
    t0 = systimes()
    some_workload2()
    t1 = systimes()
    print('before:', t0)
    print('after:', t1)
    print('differences:', (t1[0] - t0[0], t1[1] - t0[1]))


    print('Testing systimes() under idle conditions')
    t0 = systimes()
    time.sleep(1)
    t1 = systimes()
    print('before:', t0)
    print('after:', t1)
    print('differences:', (t1[0] - t0[0], t1[1] - t0[1]))
    print()

    print(processtime())

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

