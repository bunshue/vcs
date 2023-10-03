'用 os.stat 讀出一個檔案的所有資訊'
import os
import stat
import time

#exists的原型
def exists(path):
    """Test whether a path exists.  Returns False for broken symbolic links"""
    try:
        os.stat(path)
    except OSError:
        return False
    return True

#isfile的原型
def isfile(path):
    try:
        st = os.stat(path)
    except OSError:
        return False
    return stat.S_ISREG(st.st_mode)

#isdir的原型
def isdir(s):
    try:
        st = os.stat(s)
    except OSError:
        return False
    return stat.S_ISDIR(st.st_mode)

#getsize的原型
def getsize(filename):
    """Return the size of a file, reported by os.stat()."""
    return os.stat(filename).st_size

#getmtime的原型
def getmtime(filename):
    """Return the last modification time of a file, reported by os.stat()."""
    return os.stat(filename).st_mtime

#getatime的原型
def getatime(filename):
    """Return the last access time of a file, reported by os.stat()."""
    return os.stat(filename).st_atime

#getctime的原型
def getctime(filename):
    """Return the metadata change time of a file, reported by os.stat()."""
    return os.stat(filename).st_ctime

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

status = exists(filename)
print('exists :', status)
status = isfile(filename)
print('isfile :', status)
status = isdir(filename)
print('isdir :', status)

size = getsize(filename)
print('size :', size)
mtime = getmtime(filename)
print('mtime :', mtime)
atime = getatime(filename)
print('atime :', atime)
ctime = getctime(filename)
print('ctime :', ctime)

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print(filename)

statinfo = os.stat(filename)

print(statinfo)

print('os.stat_result(', end = '')
print('st_mode=', statinfo.st_mode, end = ', ')
print('st_ino=', statinfo.st_ino, end = ', ')
print('st_dev=', statinfo.st_dev, end = ', ')
print('st_nlink=', statinfo.st_nlink, end = ', ')
print('st_uid=', statinfo.st_uid, end = ', ')
print('st_gid=', statinfo.st_gid, end = ', ')
print('st_size=', statinfo.st_size, end = ', ')
print('st_atime=', statinfo.st_atime, end = ', ')
print('st_mtime=', statinfo.st_mtime, end = ', ')
print('st_ctime=', statinfo.st_ctime, end = ')')    #使用檔案時間

print('\n使用檔案時間')
ttt = time.strftime('%Y:%m:%d', time.localtime(os.stat(filename).st_ctime))
print(ttt)



TB = 1024 * 1024 * 1024 * 1024  #定義TB的計算常量
GB = 1024 * 1024 * 1024         #定義GB的計算常量
MB = 1024 * 1024                #定義MB的計算常量
KB = 1024                       #定義KB的計算常量

def ByteConversionTBGBMBKB(size):
    if size < 0:
        return "不合法的數值"
    elif (size / TB >= 1024):    #如果目前Byte的值大於等於1024TB
        return "無法表示"
    elif (size / TB >= 1):   #如果目前Byte的值大於等於1TB
        return format(size / TB, ".2f") + " TB" #將其轉換成TB
    elif (size / GB >= 1):   #如果目前Byte的值大於等於1GB
        return format(size / GB, ".2f") + " GB" #將其轉換成GB
    elif (size / MB >= 1):   #如果目前Byte的值大於等於1MB
        return format(size / MB, ".2f") + " MB" #將其轉換成MB
    elif (size / KB >= 1):   #如果目前Byte的值大於等於1KB
        return format(size / KB, ".2f") + " KB" #將其轉換成KB
    else:
        return str(size) + " Byte"    #顯示Byte值

filesize = 123456
print('filesize = ', filesize , '\t檔案大小 : ', ByteConversionTBGBMBKB(filesize))




filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

'''
ST_SIZE: 普通文件以字節為單位的大小；包含等待某些特殊文件的數據。
ST_ATIME: 上次訪問的時間。
ST_MTIME: 最後一次修改的時間。
ST_CTIME: 由操作系統報告的"ctime"。在某些系統上（如Unix）是最新的元數據更改的時間，在其它系統上（如Windows）是創建時間（詳細信息參見平臺的文檔）。
'''

statinfo = os.stat(filename)
#print(statinfo)

filesize = statinfo[stat.ST_SIZE]
create_time = statinfo[stat.ST_CTIME]
modify_time = statinfo[stat.ST_MTIME]
access_time = statinfo[stat.ST_ATIME]

'''
print('檔案建立時間\t', create_time)
print('最後修改時間\t', modify_time)
print('最後存取時間\t', access_time)
'''

print('檔案大小:\t', filesize, ' 拜')
print('檔案大小:\t', ByteConversionTBGBMBKB(filesize))
print("建立日期:\t", time.ctime(create_time))
print("修改時間:\t", time.ctime(modify_time))
print("存取時間:\t", time.ctime(access_time))

'''
filesize = os.path.getsize(filename)
print("檔案大小\t" + str(filesize) + " 拜")
print("建立日期:\t", os.path.getmtime(filename))
print("建立日期:\t", time.ctime(os.path.getmtime(filename)))
'''

import os
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

size = os.stat(filename).st_size
print(size)



filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
import os
from stat import ST_MTIME
from stat import ST_CTIME

st = os.stat(filename)

print(st)

print(st[ST_MTIME])
print(st[ST_CTIME])







'''
stat 結構:

st_mode: inode 保護模式
st_ino: inode 節點號。
st_dev: inode 駐留的設備。
st_nlink: inode 的鏈接數。
st_uid: 所有者的用戶ID。
st_gid: 所有者的組ID。
st_size: 普通文件以字節為單位的大小；包含等待某些特殊文件的數據。
st_atime: 上次訪問的時間。
st_mtime: 最后一次修改的時間。
st_ctime: 由操作系統報告的"ctime"。在某些系統上（如Unix）是最新的元數據更改的時間，在其它系統上（如Windows）是創建時間（詳細信息參見平臺的文檔）。
'''


print('stat 結構:')

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

import os, sys
import stat
# 顯示文件 "a2.py" 信息
statinfo = os.stat(filename)
print(statinfo)

print('inode 保護模式\t', statinfo[stat.ST_MODE])
print('inode 節點號\t', statinfo[stat.ST_INO])
print('inode 駐留的設備\t', statinfo[stat.ST_DEV])
print('inode 的鏈接數\t', statinfo[stat.ST_NLINK])
print('所有者的用戶ID\t', statinfo[stat.ST_UID])
print('所有者的組ID\t', statinfo[stat.ST_GID])
print('檔案大小\t', statinfo[stat.ST_SIZE])
print('最後存取時間\t', statinfo[stat.ST_ATIME])
print('最後修改時間\t', statinfo[stat.ST_MTIME])
print('檔案建立時間\t', statinfo[stat.ST_CTIME])



import sys
import os

from stat import ST_ATIME, ST_MTIME # Really constants 7 and 8

'''
st_atime: 上次訪問的時間。
st_mtime: 最後一次修改的時間。
'''

print('將檔案1的時間拷貝到檔案2')
filename1 = 'C:/_git/vcs/_1.data/______test_files1/aaaaaaab.txt'
filename2 = 'C:/_git/vcs/_1.data/______test_files2/country_data_out1.xml'

''' TBD
try:
    stat1 = os.stat(filename1)
    print(stat1[ST_ATIME])
    print(stat1[ST_MTIME])
except OSError:
    sys.stderr.write(filename1 + ': cannot stat\n')
    sys.exit(1)
try:
    os.utime(filename2, (stat1[ST_ATIME], stat1[ST_MTIME]))
except OSError:
    sys.stderr.write(filename2 + ': cannot change time\n')
    sys.exit(2)
'''



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



filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
st = os.stat(filename) # Get the mode
mode = stat.S_IMODE(st[stat.ST_MODE])
print(st)
print(mode)



mode = os.stat(filename).st_mode
print(mode)
print(stat.S_IWOTH)
print(mode & stat.S_IWOTH)
print(mode)
print(stat.S_IWGRP)
print(mode & stat.S_IWGRP)


def msg(str):
    sys.stderr.write(str + '\n')

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

try:
    st = os.stat(filename)
except OSError:
    print('error')
if not S_ISREG(st[ST_MODE]):
    msg(filename + ': not a disk file')
else:
    mode = S_IMODE(st[ST_MODE])
    if mode & 0o111:
        if not ident:
            print(filename)
            ident = st[:3]
        else:
            if st[:3] == ident:
                s = 'same as: '
            else:
                s = 'also: '
            msg(s + filename)
    else:
        msg(filename + ': not executable')


print('------------------------------------------------------------')	#60個

foldername1 = 'C:/_git/vcs/_1.data/______test_files1'
foldername2 = 'C:/_git/vcs/_1.data/______test_files2'
foldername3 = 'C:/_git/vcs/_1.data/______test_files3'

if os.stat(foldername1).st_mtime < os.stat(foldername2).st_mtime:
    print('foldername1 較早')
else:
    print('foldername1 較晚')



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

file_stats = os.stat(filename)
mtime = time.ctime(file_stats.st_mtime)
print(mtime)

mtime = int(os.stat(filename).st_mtime)
print(mtime)



cc1 = os.stat(filename)
print(cc1)

cc2 = os.lstat(filename)
print(cc2)


# 获取元组
info = os.lstat(filename)

print('文件信息 :', info)

# 获取文件 uid
print('文件 UID  : %d' % info.st_uid)

# 获取文件 gid
print('文件 GID : %d' % info.st_gid)



size = os.stat(filename).st_size
print('檔案大小 :', size)



filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
stat = os.stat(filename)
print(stat.st_size)
print(stat.st_mtime)



foldername = 'C:/_git/vcs/_1.data/______test_files5'

nnnn = os.stat(foldername)
print(type(nnnn))
print(nnnn)



print('------------------------------------------------------------')	#60個





'''
# 新進未整理

            fileSize = os.stat(web+fileName)[6] #檔案大小
            if fileSize != None:
                f = open(web+fileName, 'r') #開啟檔案
                client.write(httpResponse)  #伺服器回應
                while True:
                    data = f.read(256) #次每次讀取 128 個字元
                    if len(data) == 0: #讀取完畢
                        break
                    client.write(data)   #伺服器回應
                f.close()
            else:
                err(client, "404", "Not Found")      

------------------------------------

    if httpMethod == 'GET': # 接受GET 請求
        fileName = path.strip('/')
        if fileName == '':
            fileName = 'index.html'
        print("傳送檔案",web+fileName)
        fileSize = os.stat(web+fileName)[6] #檔案大小
        if fileSize != None:
            f = open(web+fileName, 'r') #開啟檔案
            client.write(httpResponse)  #伺服器回應
            while True:
                data = f.read(128) #次每次讀取 128 個字元
                if len(data) == 0: #讀取完畢                        
                    break
                client.write(data)   #伺服器回應
            f.close()
        else:
            err(client, "404", "Not Found")      


------------------------------------


        statbuf = os.stat(filename)
        os.chmod(tempname, statbuf[ST_MODE] & 0o7777)

------------------------------------


import os
import time

print('touch的效果')

檔案touch前的時間
filename1 = 'aaa.py'

o_time = os.stat(filename1).st_mtime
print(o_time)

filename2 = 'nnnnn.txt'

n_time = os.stat(filename2).st_mtime
print(n_time)

print(n_time-o_time)

os.utime(filename1, (n_time, n_time))

now = time.time()

os.utime(filename1, (now, now))


檔案touch後的時間



------------------------------------

            mode = ((os.stat(tempname).st_mode) | 0o555) & 0o7777
            os.chmod(tempname, mode)



------------------------------------




# Copy one file's atime and mtime to another
import sys
import os
from stat import ST_ATIME, ST_MTIME # Really constants 7 and 8

        stat1 = os.stat(file1)

        os.utime(file2, (stat1[ST_ATIME], stat1[ST_MTIME]))





------------------------------------


import sys, os, time, difflib, optparse
from datetime import datetime, timezone

def file_mtime(path):
    t = datetime.fromtimestamp(os.stat(path).st_mtime,
                               timezone.utc)
    return t.astimezone().isoformat()

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
fromdate = file_mtime(filename)
print(fromdate)

string = 'aaaaaaa '
sys.stdout.writelines(string)
print(string)


    fromdate = file_mtime(fromfile)
      todate = file_mtime(tofile)
    with open(fromfile) as ff:
        fromlines = ff.readlines()
    with open(tofile) as tf:
        tolines = tf.readlines()




------------------------------------












'''
