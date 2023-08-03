import time
import datetime


#>>> from time import gmtime, strftime


ttt = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())

print(ttt)

#'Thu, 28 Jun 2001 14:17:15 +0000'





import time

ddd = time.strptime("30 Nov 00", "%d %b %y")
print(ddd)

'''
time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0,
                 tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)
'''



print('量測時間 ST') 
# Start the stopwatch / counter
t1_start = time.perf_counter()
 
time.sleep(1.2345)   # 暫停 1.2345 秒
 
# Stop the stopwatch / counter
t1_stop = time.perf_counter()

print('量測時間 SP')  
print(t1_stop, t1_start)
print(t1_stop - t1_start, '秒')

from time import perf_counter_ns
 
print('量測時間 ST') 
# Start the stopwatch / counter
t1_start = time.perf_counter_ns()

time.sleep(1.2345)   # 暫停 1.2345 秒 
 
# Stop the stopwatch / counter
t1_stop = time.perf_counter_ns()

print('量測時間 SP')
print(t1_stop, 'ns', t1_start, 'ns')
 
print(t1_stop - t1_start, 'ns')


import time

start = time.time()

time.sleep(0.12345)

stop = time.time()

print(stop - start)


print('測試hasattr功能')
print('內建函數 (function) hasattr() ，判斷參數 (parameter) name 是否為 object 的屬性名稱')

class Demo:
    def __init__(self, i):
        self.i = i
        self.x = "xxx"
        self.y = "yyy"
        self.z = "zzz"
     
    def __str__(self):
        return str(self.i)
          
    def hello(self):
        print("hello " + self.__str__())
 
d = Demo(22)

print(hasattr(d, "t"))  #不是
print(hasattr(d, "u"))  #不是
print(hasattr(d, "v"))  #不是
print(hasattr(d, "w"))  #不是
print(hasattr(d, "x"))  #是
print(hasattr(d, "y"))  #是
print(hasattr(d, "z"))  #是




