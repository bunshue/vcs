
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

