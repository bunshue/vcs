"""
各種 python 檔案格式相關資料

一般檔案資訊

用 os.stat 讀出一個檔案的所有資訊
os.stat 和 os.lstat 一樣

stat 結構:

st_mode: inode 保護模式
st_ino: inode 節點號。
st_dev: inode 駐留的設備。
st_nlink: inode 的鏈接數。
st_uid: 所有者的用戶ID。
st_gid: 所有者的組ID。

st_size: 普通文件以字節為單位的大小；包含等待某些特殊文件的數據。
st_ctime: 由操作系統報告的"ctime"。在某些系統上（如Unix）是最新的元數據更改的時間，在其它系統上（如Windows）是創建時間（詳細信息參見平臺的文檔）。
st_mtime: 最后一次修改的時間。
st_atime: 上次訪問的時間。

ST_SIZE: 普通文件以字節為單位的大小；包含等待某些特殊文件的數據。
ST_CTIME: 由操作系統報告的"ctime"。在某些系統上（如Unix）是最新的元數據更改的時間，在其它系統上（如Windows）是創建時間（詳細信息參見平臺的文檔）。
ST_MTIME: 最後一次修改的時間。
ST_ATIME: 上次訪問的時間。

"""


import os
import sys
import math
import random
import stat
import time

print("------------------------------------------------------------")  # 60個

TB = 1024 * 1024 * 1024 * 1024  # 定義TB的計算常量
GB = 1024 * 1024 * 1024  # 定義GB的計算常量
MB = 1024 * 1024  # 定義MB的計算常量
KB = 1024  # 定義KB的計算常量


def ByteConversionTBGBMBKB(size):
    if size < 0:
        return "不合法的數值"
    elif size / TB >= 1024:  # 如果目前Byte的值大於等於1024TB
        return "無法表示"
    elif size / TB >= 1:  # 如果目前Byte的值大於等於1TB
        return format(size / TB, ".2f") + " TB"  # 將其轉換成TB
    elif size / GB >= 1:  # 如果目前Byte的值大於等於1GB
        return format(size / GB, ".2f") + " GB"  # 將其轉換成GB
    elif size / MB >= 1:  # 如果目前Byte的值大於等於1MB
        return format(size / MB, ".2f") + " MB"  # 將其轉換成MB
    elif size / KB >= 1:  # 如果目前Byte的值大於等於1KB
        return format(size / KB, ".2f") + " KB"  # 將其轉換成KB
    else:
        return str(size) + " Byte"  # 顯示Byte值


filesize = 123456
print("filesize = ", filesize, "\t檔案大小 : ", ByteConversionTBGBMBKB(filesize))

print("------------------------------------------------------------")  # 60個


def get_cma_times(filename):
    cc = os.stat(filename)
    ctime = cc[stat.ST_CTIME]
    mtime = cc[stat.ST_MTIME]
    atime = cc[stat.ST_ATIME]

    print("建立日期:\t", time.ctime(ctime))
    print("修改日期:\t", time.ctime(mtime))
    print("存取日期:\t", time.ctime(atime))


print("------------------------------------------------------------")  # 60個

print("使用 os.stat 取得檔案資訊")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

print("使用os.stat")
cc = os.stat(filename)
print(type(cc))
print(cc)

print("使用macro")
size = cc[stat.ST_SIZE]
ctime = cc[stat.ST_CTIME]
mtime = cc[stat.ST_MTIME]
atime = cc[stat.ST_ATIME]

# print('建立日期:\t', ctime)  # 秒
# print('修改日期:\t', mtime)  # 秒
# print('存取日期:\t', atime)  # 秒

print("大小:\t", size, " 拜")
print("大小:\t", ByteConversionTBGBMBKB(size))
print("建立日期:\t", time.ctime(ctime))
print("修改日期:\t", time.ctime(mtime))
print("存取日期:\t", time.ctime(atime))

ctime = cc.st_ctime
mtime = cc.st_mtime
atime = cc.st_atime

mtime = time.ctime(cc.st_mtime)
print(mtime)
mtime = int(cc.st_mtime)
print(mtime)

mtime = cc.st_mtime

atime = cc.st_atime
print(type(mtime))
print(mtime)
print(type(atime))
print(atime)

filesize = os.path.getsize(filename)
print("大小\t" + str(filesize) + " 拜")
print("建立日期:\t", os.path.getmtime(filename))
print("建立日期:\t", time.ctime(os.path.getmtime(filename)))

print("使用結構內的項目")
print("mode  :", cc.st_mode)
print("ino   :", cc.st_ino)
print("dev   :", cc.st_dev)
print("nlink :", cc.st_nlink)
print("uid   :", cc.st_uid)
print("gid   :", cc.st_gid)
print("size  :", cc.st_size)
print("ctime :", cc.st_ctime)
print("mtime :", cc.st_mtime)
print("atime :", cc.st_atime)

print("文件 UID  : %d" % cc.st_uid)
print("文件 GID : %d" % cc.st_gid)

print("mode")

print("old_mode", cc.st_mode)
mode = ((cc.st_mode) | 0o555) & 0o7777
print("new_mode", mode)
mode = cc[stat.ST_MODE] & 0o7777
print("new_mode", mode)

print(cc[stat.ST_MODE])
print(cc[stat.ST_MODE] & 0o7777)

mode = stat.S_IMODE(cc[stat.ST_MODE])
print(mode)

# st_mode用以判斷是不是檔案/資料夾/...
mode = cc.st_mode
print(mode)
print(stat.S_IWOTH)
print(mode & stat.S_IWOTH)
print(mode)
print(stat.S_IWGRP)
print(mode & stat.S_IWGRP)

print(stat.S_ISREG(cc.st_mode))
print(stat.S_ISDIR(cc.st_mode))

"""
if not stat.S_ISREG(st[stat.ST_MODE]):
    msg(filename + ': not a disk file')

"""
print("inode 保護模式\t", cc[stat.ST_MODE])
print("inode 節點號\t", cc[stat.ST_INO])
print("inode 駐留的設備\t", cc[stat.ST_DEV])
print("inode 的鏈接數\t", cc[stat.ST_NLINK])
print("所有者的用戶ID\t", cc[stat.ST_UID])
print("所有者的組ID\t", cc[stat.ST_GID])

print("\n使用檔案時間")
ttt = time.strftime("%Y:%m:%d", time.localtime(cc.st_ctime))
print(ttt)

print("------------------------------------------------------------")  # 60個

print("讀取mtime, 比較兩個檔案的 修改日期 的 早晚")
foldername1 = "C:/_git/vcs/_1.data/______test_files1"
foldername2 = "C:/_git/vcs/_1.data/______test_files2"
foldername3 = "C:/_git/vcs/_1.data/______test_files3"

if os.stat(foldername1).st_mtime < os.stat(foldername2).st_mtime:
    print("foldername1 較早")
else:
    print("foldername1 較晚")

print("------------------------------------------------------------")  # 60個


def msg(str):
    sys.stderr.write(str + "\n")


filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

try:
    cc = os.stat(filename)
except OSError:
    print("error")
if not stat.S_ISREG(cc[stat.ST_MODE]):
    msg(filename + ": not a disk file")
else:
    mode = stat.S_IMODE(cc[stat.ST_MODE])
    if mode & 0o111:
        if not ident:
            print(filename)
            ident = cc[:3]
        else:
            if cc[:3] == ident:
                s = "same as: "
            else:
                s = "also: "
            msg(s + filename)
    else:
        msg(filename + ": not executable")

print("------------------------------------------------------------")  # 60個

print("修改檔案的 修改/存取 日期, 將檔案2的 修改/存取 日期設定給檔案1")

filename1 = "python03_algorithm.py"
cc = os.stat(filename1)
mtime1 = cc[stat.ST_MTIME]  # 修改日期
atime1 = cc[stat.ST_ATIME]  # 存取日期
get_cma_times(filename1)
print("檔案1的修改日期:(舊)\t", time.ctime(mtime1))
print("檔案1的存取日期:(舊)\t", time.ctime(atime1))

filename2 = "python05_file_info.py"
cc = os.stat(filename2)
mtime2 = cc[stat.ST_MTIME]  # 修改日期
atime2 = cc[stat.ST_ATIME]  # 存取日期

get_cma_times(filename2)
print("檔案2的修改日期:\t", time.ctime(mtime2))
print("檔案2的存取日期:\t", time.ctime(atime2))

print("兩個檔案的修改日期的時間差:\t", mtime2 - mtime1, "秒")
print("兩個檔案的存取日期的時間差:\t", atime2 - atime1, "秒")

print("將檔案2的 修改/存取 日期設定給檔案1")
# 修改atime, mtime
try:
    # os.utime(filename1, (atime2, mtime2))
    os.utime(filename1, times=(atime2, mtime2))
except OSError as msg:
    err("%s: reset of timestamp failed (%r)\n" % (filename1, msg))
    sys.stderr.write(filename1 + ": cannot change time\n")

get_cma_times(filename1)
print("檔案1的修改日期:(新)\t", time.ctime(mtime1))
print("檔案1的存取日期:(新)\t", time.ctime(atime1))

print("------------------------------------------------------------")  # 60個

filename = "python04_str_DSLT1.py"

print("touch 一個檔案")

print("touch 前 :")
get_cma_times(filename)

os.utime(filename, (time.time(), time.time()))

print("touch 後 :")
get_cma_times(filename)

filename = "python04_string.py"

print("touch 前 :")
get_cma_times(filename)

os.utime(filename, (0, 0))  # 將兩時間改成1970-01-01
# os.utime(filename, None)  # 改成最新時間
# os.utime(filename)  # 改成最新時間

print("touch 後 :")
get_cma_times(filename)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


"""
# 新進未整理

try:
    os.rename(filename, filename + '~')
except OSError as msg:
    err('%s: warning: backup failed (%r)\n' % (filename, msg))

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

import difflib, optparse
from datetime import datetime, timezone

def file_mtime(path):
    t = datetime.fromtimestamp(os.stat(path).st_mtime,
                               timezone.utc)
    return t.astimezone().isoformat()

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
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


filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

show = "不存在，可能檔案或路徑有誤"
if os.path.exists(filename):  # 判斷檔案或路徑是否存在
    show = "存在"
print("%s %s" % (filename, show))

print("------------------------------------------------------------")  # 60個

show = "不存在，可能檔案或路徑有誤"
if os.path.exists(filename):
    show = "存在"
    if os.path.isfile(filename):
        show += "，為檔案路徑"
    if os.path.isdir(filename):
        show += "，為目錄路徑"
print("%s %s" % (filename, show))

print("------------------------------------------------------------")  # 60個

dirPath = "tmp_PythonHw"
if os.path.exists(dirPath):
    print("目錄已存在或路徑有誤，無法建立")
else:
    os.mkdir(dirPath)
    pathname = os.path.split(dirPath)[0]  # 取得路徑
    filename = os.path.split(dirPath)[1]  # 取得目錄名稱
    print("於 %s 建立 %s 目錄" % (pathname, filename))

print("------------------------------------------------------------")  # 60個

dirPath = "tmp_PythonHw"
if os.path.exists(dirPath):
    os.rmdir(dirPath)
    pathname = os.path.split(dirPath)[0]  # 取得路徑
    filename = os.path.split(dirPath)[1]  # 取得目錄名稱
    print("刪除 %s 下的 %s 目錄" % (pathname, filename))
else:
    print("目錄不存在或路徑有誤，無法刪除")

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
