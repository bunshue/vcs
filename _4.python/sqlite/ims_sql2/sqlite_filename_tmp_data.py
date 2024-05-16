#檔案資料庫 之 暫存資料

print('------------------------------------------------------------')	#60個
print('準備工作')

import os
import sys
import csv
import time
import cv2
import sqlite3
import tkinter as tk
import tkinter as tk
from tkinter.filedialog import askopenfile #tk之openFileDialog
from tkinter.filedialog import asksaveasfile #tk之saveFileDialog
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

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



filename = 'C:/aaa/bbb/ccc/ddd/eee.jpg'

name = filename.split('/')
print(type(name))
print(len(name))
print(name)


print('------------------------------------------------------------')	#60個


from os.path import abspath

def _basename(path):
    # A basename() variant which first strips the trailing slash, if present.
    # Thus we always get the last component of the path, even for directories.
    sep = os.path.sep + (os.path.altsep or '')
    return os.path.basename(path.rstrip(sep))

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
base_name = _basename(filename)
print(base_name)

src = abspath(base_name)
print(src)

zip_filename = base_name + ".zip"
print(zip_filename)

print('------------------------------------------------------------')	#60個

foldername = 'C:/_git/vcs/_1.data/______test_files2'

normdir = os.path.normcase(foldername)
print(normdir)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('尋找python程式碼的所在地')

module_name = 'pytube'
code_place = os.path.dirname(__import__(module_name).__file__)
print(code_place)


print('取得相對路徑')
foldername = 'C:/_git/vcs/_1.data/______test_files1/'
fn = os.path.relpath(foldername, code_place)

print(fn)

print('------------------------------------------------------------')	#60個


foldername = 'C:/_git/vcs/_1.data/______test_files5'
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

name = os.path.basename(filename)

print(name)


print('------------------------------------------------------------')	#60個


filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

if filename.endswith(".jpg"):
    # It is a module -- insert its dir into sys.path and try to
    # import it. If it is part of a package, that possibly
    # won't work because of package imports.
    dirname, filename = os.path.split(filename)
    print(filename[:-3])



print('------------------------------------------------------------')	#60個

print('將主檔名中不合法的字元去除')

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

m_filename = ""
for c in filename:
   #print(c)
   if c == " " or c == "." or c == "," or c == "、" or c == "，" or c == "(" or c == ")":
      m_filename += ""  # 去除不合法字元
   else:
      m_filename += c

print(filename)
print(m_filename)


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



