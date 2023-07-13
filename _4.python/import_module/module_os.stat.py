'用 os.stat 讀出一個檔案的所有資訊'
import os
import stat
import time

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print(filename)

statinfo = os.stat(filename)
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





