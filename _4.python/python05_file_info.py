"""
各種 python 檔案格式相關資料

一般檔案資訊

用 os.stat 讀出一個檔案的所有資訊

"""

import os
import sys
import math
import random
import stat
import time

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

"""
st_atime: 上次訪問的時間。
st_mtime: 最後一次修改的時間。
"""

print('將檔案1的時間拷貝到檔案2')
filename1 = 'C:/_git/vcs/_1.data/______test_files1/aaaaaaab.txt'
filename2 = 'C:/_git/vcs/_1.data/______test_files2/country_data_out1.xml'

""" TBD
try:
    st = os.stat(filename1)
    print(st[stat.ST_ATIME])
    print(st[stat.ST_MTIME])
except OSError:
    sys.stderr.write(filename1 + ': cannot stat\n')
    sys.exit(1)
try:
    os.utime(filename2, (st[stat.ST_ATIME], st[stat.ST_MTIME]))
except OSError:
    sys.stderr.write(filename2 + ': cannot change time\n')
    sys.exit(2)
"""

print('------------------------------------------------------------')	#60個

"""    
try:
    os.rename(filename, filename + '~')
except OSError as msg:
    err('%s: warning: backup failed (%r)\n' % (filename, msg))
"""

"""
#修改atime, mtime
try:
    os.utime(filename, (atime, mtime))
    except OSError as msg:
        err('%s: reset of timestamp failed (%r)\n' % (filename, msg))
"""

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
st = os.stat(filename) # Get the mode
mode = stat.S_IMODE(st[stat.ST_MODE])
print(st)
print(mode)

print('------------------------------------------------------------')	#60個

def msg(str):
    sys.stderr.write(str + '\n')

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

try:
    st = os.stat(filename)
except OSError:
    print('error')
if not stat.S_ISREG(st[stat.ST_MODE]):
    msg(filename + ': not a disk file')
else:
    mode = stat.S_IMODE(st[stat.ST_MODE])
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

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

cc = os.stat(filename)

mtime = time.ctime(cc.st_mtime)
print(mtime)

mtime = int(os.stat(filename).st_mtime)
print(mtime)

print('文件信息 :', cc)
print('文件 UID  : %d' % cc.st_uid)
print('文件 GID : %d' % cc.st_gid)

print('------------------------------------------------------------')	#60個

"""
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

print('touch的效果')

檔案touch前的時間
filename1 = 'aaa.py'

old_time = os.stat(filename1).st_mtime
print(old_time)

filename2 = 'nnnnn.txt'

new_time = os.stat(filename2).st_mtime
print(new_time)

print(new_time - old_time)

os.utime(filename1, (new_time, new_time))

now = time.time()

os.utime(filename1, (now, now))


檔案touch後的時間



------------------------------------

            mode = ((os.stat(tempname).st_mode) | 0o555) & 0o7777
            os.chmod(tempname, mode)

        st = os.stat(filename)
        os.chmod(tempname, st[ST_MODE] & 0o7777)



------------------------------------

# Copy one file's atime and mtime to another

        st = os.stat(file1)

        os.utime(file2, (st[stat.ST_ATIME], st[stat.ST_MTIME]))

------------------------------------


import difflib, optparse
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

"""

print("os.stat 和 os.lstat 一樣")

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

print('使用os.stat')
cc = os.stat(filename)
print(type(cc))
print(cc)

print('使用macro')
atime = cc[stat.ST_ATIME]
mtime = cc[stat.ST_MTIME]
ctime = cc[stat.ST_CTIME]
size = cc[stat.ST_SIZE]

print('ST_ATIME :', cc[stat.ST_ATIME])
print('ST_MTIME :', cc[stat.ST_MTIME])
print('ST_CTIME :', cc[stat.ST_CTIME])
print("檔案大小 :", size, "拜")

print('使用結構內的項目')
size = cc.st_size
print("檔案大小 :", size, "拜")
print("mode  :", cc.st_mode)
print("ino   :", cc.st_ino)
print("dev   :", cc.st_dev)
print("nlink :", cc.st_nlink)
print("uid   :", cc.st_uid)
print("gid   :", cc.st_gid)
print("size  :", cc.st_size)
print("atime :", cc.st_atime)
print("mtime :", cc.st_mtime)
print("ctime :", cc.st_ctime) #使用檔案時間

print('inode 保護模式\t', cc[stat.ST_MODE])
print('inode 節點號\t', cc[stat.ST_INO])
print('inode 駐留的設備\t', cc[stat.ST_DEV])
print('inode 的鏈接數\t', cc[stat.ST_NLINK])
print('所有者的用戶ID\t', cc[stat.ST_UID])
print('所有者的組ID\t', cc[stat.ST_GID])
print('檔案大小\t', cc[stat.ST_SIZE])
print('最後存取時間\t', cc[stat.ST_ATIME])
print('最後修改時間\t', cc[stat.ST_MTIME])
print('檔案建立時間\t', cc[stat.ST_CTIME])


print('\n使用檔案時間')
ttt = time.strftime('%Y:%m:%d', time.localtime(os.stat(filename).st_ctime))
print(ttt)

filesize = os.stat(filename).st_size

print('檔案大小:\t', filesize, ' 拜')
print('檔案大小:\t', ByteConversionTBGBMBKB(filesize))

print('------------------------------------------------------------')	#60個

print('mode')

#st_mode用以判斷是不是檔案/資料夾/...
mode = os.stat(filename).st_mode
print(mode)
print(stat.S_IWOTH)
print(mode & stat.S_IWOTH)
print(mode)
print(stat.S_IWGRP)
print(mode & stat.S_IWGRP)

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



"""
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
"""




filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

"""
ST_SIZE: 普通文件以字節為單位的大小；包含等待某些特殊文件的數據。
ST_ATIME: 上次訪問的時間。
ST_MTIME: 最後一次修改的時間。
ST_CTIME: 由操作系統報告的"ctime"。在某些系統上（如Unix）是最新的元數據更改的時間，在其它系統上（如Windows）是創建時間（詳細信息參見平臺的文檔）。
"""

st = os.stat(filename)
#print(st)

filesize = st[stat.ST_SIZE]
create_time = st[stat.ST_CTIME]
modify_time = st[stat.ST_MTIME]
access_time = st[stat.ST_ATIME]

"""
print('檔案建立時間\t', create_time)
print('最後修改時間\t', modify_time)
print('最後存取時間\t', access_time)
"""

print('檔案大小:\t', filesize, ' 拜')
print('檔案大小:\t', ByteConversionTBGBMBKB(filesize))
print("建立日期:\t", time.ctime(create_time))
print("修改時間:\t", time.ctime(modify_time))
print("存取時間:\t", time.ctime(access_time))

"""
filesize = os.path.getsize(filename)
print("檔案大小\t" + str(filesize) + " 拜")
print("建立日期:\t", os.path.getmtime(filename))
print("建立日期:\t", time.ctime(os.path.getmtime(filename)))
"""

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

mtime = None
atime = None

# First copy the file's mode to the temp file

cc = os.stat(filename)

mtime = cc.st_mtime
atime = cc.st_atime
print(type(mtime))
print(mtime)
print(type(atime))
print(atime)
print(st[stat.ST_MODE])
print(st[stat.ST_MODE] & 0o7777)

print('------------------------------------------------------------')	#60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


#資料夾
filename = 'C:/_git/vcs/_1.data/______test_files3'

#檔案
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

cc = os.stat(filename)

print(stat.S_ISREG(cc.st_mode))
print(stat.S_ISDIR(cc.st_mode))

"""
if not stat.S_ISREG(st[stat.ST_MODE]):
    msg(filename + ': not a disk file')

size = os.stat(filename).st_size
mtime = os.stat(filename).st_mtime
atime = os.stat(filename).st_atime
ctime = os.stat(filename).st_ctime

"""

