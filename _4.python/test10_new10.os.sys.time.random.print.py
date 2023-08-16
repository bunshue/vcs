import os
import sys
import time
import datetime
import random

foldername = 'C:/_git/vcs/_1.data/______test_files5'
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('------------------------------------------------------------')	#60個


print('---- os --------------------------------------------------------')	#60個

import test
packagedir = os.path.dirname(test.__file__)

import email
packagedir = os.path.dirname(email.__file__)
print(packagedir)

'''
print(time.strptime(date, '%Y-%m-%d'))
print(time.strptime(time_, '%H:%M:%S'))
'''

print('------------------------------------------------------------')	#60個








print(sys.maxsize)
print(2 ** 32)

import stat

print(os.name)
print(os.sep)

print('------------------------------------------------------------')	#60個


#>>> from time import gmtime, strftime


ttt = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())

print(ttt)

#'Thu, 28 Jun 2001 14:17:15 +0000'


print('------------------------------------------------------------')	#60個



ddd = time.strptime("30 Nov 00", "%d %b %y")
print(ddd)

'''
time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0,
                 tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)
'''


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

start = time.time()

time.sleep(0.12345)

stop = time.time()

print(stop - start)
'''



print('------------------------------------------------------------')	#60個

print(os.getpid())



import os

def getuser():
    for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
        print(name)
        user = os.environ.get(name)
        if user:
            print(user)
            return user

print('get user name')
ccc = getuser()
print(ccc)



print('------------------------------------------------------------')	#60個


import sys, os, time, difflib, argparse
from datetime import datetime, timezone

path = 'C:/_git/vcs/_4.python'
t1 = datetime.fromtimestamp(os.stat(path).st_mtime, timezone.utc)
print(t1)

t2 = t1.astimezone().isoformat()
print(t2)


print('------------------------------------------------------------')	#60個



import os
import sys
m = sys.modules.get('__main__')

print(m)



foldername = 'C:/_git/vcs/_1.data/______test_files5'
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

name = os.path.basename(filename)

print(name)


globs = {}
globs = globs.copy()
print(globs)

print()

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

if filename.endswith(".jpg"):
    # It is a module -- insert its dir into sys.path and try to
    # import it. If it is part of a package, that possibly
    # won't work because of package imports.
    dirname, filename = os.path.split(filename)
    print(filename[:-3])




print('------------------------------------------------------------')	#60個

import datetime
seconds = datetime.datetime(2004, 10, 26, 10, 33, 33, tzinfo = datetime.timezone(datetime.timedelta(0))).timestamp()
print(seconds)


import time
print('存檔紀念')

fp = open('Build.txt', 'w')
fp.write("# BUILD INFO\n")
fp.write("# Date: %s\n" % time.ctime())
fp.close()


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個








filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
print(filename)
filename = os.path.normcase(filename)
print(filename)




print('------------------------------------------------------------')	#60個







print('------------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個



print('---- sys --------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個







print('------------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個


print('---- time datetime --------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('---- random --------------------------------------------------------')	#60個




print('---- 新進 --------------------------------------------------------')	#60個

