import os
import os, sys, stat, getopt

'''
import pydoc
if __name__ == '__main__':
    pydoc.cli()
'''

def mtime(f):
    st = os.fstat(f.fileno())
    return st[stat.ST_MTIME]


filename1 = 'C:/_git/vcs/_1.data/______test_files1/human1.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/human2.jpg'

try:
    sf = open(filename1, 'rb')
except IOError:
    sf = None
try:
    mf = open(filename2, 'r')
except IOError:
    mf = None


sft = mtime(sf)
mft = mtime(mf)
if mft > sft:
    # Master is newer -- copy master to slave
    sf.close()
    mf.close()
    print('1111111')
else:
    print('22222')

print('比較兩檔是否相同')

BUFSIZE = 16*1024

def identical(sf, mf):
    while 1:
        sd = sf.read(BUFSIZE)
        md = mf.read(BUFSIZE)
        if sd != md: return 0
        if not sd: break
    return 1

filename1 = 'C:/_git/vcs/_1.data/______test_files1/poetry2.txt'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/poetry2.txt'

try:
    sf = open(filename1, 'r')
except IOError:
    sf = None
try:
    mf = open(filename1, 'r')
except IOError:
    mf = None


if sf and mf:
    if identical(sf, mf):
        print('兩檔相同')
    else:
        print('兩檔不同')
        

err = sys.stderr.write
dbg = err
rep = sys.stdout.write

err('AAAAA')
dbg('BBBBB')
rep('CCCCC')

#err(str(msg) + '\n')

err('-i option or file-or-directory missing\n')

'''
import webbrowser
print('用預設的瀏覽器開啟網頁')
url = 'https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5'
print(url)
webbrowser.open(url)
'''

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

filename = 'C:/_git/vcs/_1.data/______test_files1/human2.jpg'

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
filename2 = 'C:/______test_files3/country_data_out1.xml'
   
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

