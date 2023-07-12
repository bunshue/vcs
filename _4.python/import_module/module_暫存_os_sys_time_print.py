import sys


print('---- os ------------------------------------------------------------------')	#70個

major, minor, micro, level, serial = sys.version_info

print('version_info')
print(sys.version_info)
print(major)
print(minor)
print(micro)
print(level)
print(serial)

import os

base_dir = os.path.dirname(os.path.abspath(__file__))

print(base_dir)

import os
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

size = os.stat(filename).st_size
print(size)



import os
user = os.getlogin()
print(user)

version = __version__ = "4.61.0.166 Unreleased"
print(version)

font_file = os.path.join(os.path.dirname(__file__), "OpenFlame.ttf")
print(font_file)

import os

print(os.listdir())
print(os.listdir('/'))



import sys, os

def lll(dirname):
    for name in os.listdir(dirname):
        print(name)
        if name not in (os.curdir, os.pardir):
            print(name)
            full = os.path.join(dirname, name)
            if os.path.islink(full):    #尋找link
                print('link')
                print(name, '->', os.readlink(full))
            else:
                print('f')
        else:
            print('x')

foldername = 'C:/_git/vcs/_1.data/______test_files1/_opencv'

#lll(foldername)


filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

from stat import *

mtime = None
atime = None
# First copy the file's mode to the temp file

statbuf = os.stat(filename)
mtime = statbuf.st_mtime
atime = statbuf.st_atime
print(type(mtime))
print(mtime)
print(type(atime))
print(atime)
print(statbuf[ST_MODE])
print(statbuf[ST_MODE] & 0o7777)

'''    
try:
    os.rename(filename, filename + '~')
except OSError as msg:
    err('%s: warning: backup failed (%r)\n' % (filename, msg))
'''

'''
#修改atime, mtime
try:
    os.utime(filename, (atime, mtime))
    except OSError as msg:
        err('%s: reset of timestamp failed (%r)\n' % (filename, msg))
'''


print('---- sys ------------------------------------------------------------------')	#70個

import sys
vi = sys.version_info
install_group = "Python %d.%d" % (vi[0], vi[1])
print(install_group)


print('---- time ------------------------------------------------------------------')	#70個
import datetime
print('datetime from lambda:', datetime.datetime.today())
today = datetime.datetime.today()
print('datetime from flex:', today)

today = str(datetime.datetime.today().date())
current = str(datetime.datetime.today())



print('---- print ------------------------------------------------------------------')	#70個

import time

print(time.localtime()) #獲取格式化的時間

localtime = time.asctime(time.localtime())
print (localtime)

#格式化日期成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))


import sys
import os
from stat import *

join = os.path.join

error = 'mkreal error'

BUFSIZE = 32*1024

def test_file(name):
    st = os.stat(name) # Get the mode
    mode = S_IMODE(st[ST_MODE])
    print(st)
    print(mode)

    files = os.listdir(name)
    
    for filename in files:
        print(filename)

sys.stdout = sys.stderr
progname = os.path.basename(sys.argv[0])

print(progname)

#name = 'cccc.dat'
name = 'dddd.pdf'
name = 'C:/_git/vcs/_4.python/__code/__tmp_code/scripts1/'

test_file(name)



print('---- 新進暫存 ------------------------------------------------------------------')	#70個




