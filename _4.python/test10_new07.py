import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

#撈出一層
import os

print('Current dir:', os.getcwd())

count = 0
for item in os.listdir():
    count += 1
    print(count, item)
print('Total', count, 'items in', os.getcwd())
print("------------------------------------------------------------")  # 60個

import os

foldername = 'C:/_git/vcs/_1.data/______test_files5'

for item in os.walk(foldername):
    print('dir name:', item[0])
    print('sub-dir list:', item[1])
    print('file list:', item[2])
    print('='*80)
    
print("------------------------------------------------------------")  # 60個

import os
from datetime import datetime

foldername = 'C:/_git/vcs/_1.data/______test_files5'

for entry in os.scandir(foldername):
    info = entry.stat()
    # epoch timestamp轉換成日期字串
    da = datetime.utcfromtimestamp(info.st_mtime)
    dstr = da.strftime('%Y/%m/%d')
    if entry.is_dir():
        print('資料夾：', entry.name, '最後存取時間：', dstr)
    elif entry.is_file():
        print('檔案：', entry.name, '最後存取時間：', dstr)
        
print("------------------------------------------------------------")  # 60個

import os

def dirTree(path, level=0):
    if level>1:
        return
    for item in os.listdir(path):
        path2 = os.path.join(path, item)
        if os.path.isdir(path2):
            for i in range(level):
                print('   ', end='')
            print('+--'+item)
            try:
                dirTree(path2, level+1)
            except:
                pass

foldername = 'C:/_git/vcs/_1.data/______test_files5'

dirTree(foldername)

print("------------------------------------------------------------")  # 60個

import os
from datetime import datetime

#foldername = os.getcwd()
foldername = 'C:/_git/vcs/_1.data/______test_files5'

for entry in os.scandir(foldername):
    info = entry.stat()
    da = datetime.utcfromtimestamp(info.st_mtime)
    dstr = da.strftime('%d/%m/%Y')
    if entry.is_file():
        size = int(os.path.getsize(entry.name)/1024)
        ext = os.path.splitext(entry.name)
        print(entry.name, '\t'+str(size)+'KB\t', str(ext[-1].replace('.', ''))+'\t', dstr)
    elif entry.is_dir():
        print(entry.name, '\t\t\t<DIR>\t', dstr)
        
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
