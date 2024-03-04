"""
相關抽出

檔案處理
檔名處理

"""

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

import os

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

if os.path.exists(filename):
    print(filename, ":", os.path.getsize(filename))
else:
    print(filename, "檔案不存在")

print("------------------------------------------------------------")  # 60個

import shutil

srcfilename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
dstfilename = "tmp_pic.jpg"

shutil.copy(srcfilename, dstfilename)  # 檔案複製

print("------------------------------------------------------------")  # 60個
"""
srcfilename = input("請輸入來源檔案 : ")
dstfilename = input("請輸入目的檔案 : ")        
with open(srcfilename) as src_Obj:        # 用預設mode=r開啟檔案,傳回檔案物件src_Obj
    data = src_Obj.read()           # 讀取檔案到變數data

with open(dstfilename, 'w') as dst_Obj:   # 開啟檔案mode=w
    dst_Obj.write(data)             # 將data輸出到檔案

"""

print("------------------------------------------------------------")  # 60個
"""
import zipfile
import glob, os
zipdir = input("請輸入欲壓縮的目錄 : ")
zipdir = zipdir + '/*'
zipfilename = input("請輸入保存壓縮檔案的名稱 : ")

fileZip = zipfile.ZipFile(zipfilename, 'w')
for name in glob.glob(zipdir):        # 遍歷zipdir目錄
    fileZip.write(name, os.path.basename(name), zipfile.ZIP_DEFLATED)
    
fileZip.close()
"""


print("------------------------------------------------------------")  # 60個


"""


import os

print(os.path.relpath('D:\\'))              # 目前目錄至D:\的相對路徑
print(os.path.relpath('D:\\Python\\ch13'))  # 目前目錄至特定path的相對路徑
print(os.path.relpath('D:\\', 'ch14_5.py')) # 目前檔案至D:\的相對路徑


import os

print(os.path.abspath('.'))             # 列出目前目錄的絕對路徑
print(os.path.abspath('..'))            # 列出上一層目錄的絕對路徑
print(os.path.abspath('ch14_4.py'))     # 列出檔案的絕對路徑




import os

print(os.path.join('D:\\','Python','ch14','ch14_8.py')) # 4個參數
print(os.path.join('D:\\Python','ch14','ch14_8.py'))    # 3個參數
print(os.path.join('D:\\Python\\ch14','ch14_8.py'))     # 2個參數



import os
import glob

print("方法1:列出\\Python\\ch14工作目錄的所有檔案與大小")
for file in glob.glob('D:\\Python\\ch14\\*.*'):
    print(f"{file} : {os.path.getsize(file)} bytes")
    
print("方法2:列出目前工作目錄的特定檔案")
for file in glob.glob('ch14_1*.py'):
    print(file)
    
print("方法3:列出目前工作目錄的特定檔案")
for file in glob.glob('ch14_2*.*'):
    print(file)

import os

mydir = 'test'
# 如果mydir不存在就建立此資料夾
if os.path.exists(mydir):
    print(f"{mydir} 已經存在")
else:
    os.mkdir(mydir)
    print(f"建立 {mydir} 資料夾成功")

print("------------------------------------------------------------")  # 60個

import os

mydir = 'test'
# 如果mydir存在就刪除此資料夾
if os.path.exists(mydir):
    os.rmdir(mydir)
    print(f"刪除 {mydir} 資料夾成功")
else:
    print(f"{mydir} 資料夾不存在")

print("------------------------------------------------------------")  # 60個

import os

print(os.getcwd())              # 列出目前工作目錄


import shutil
shutil.rmtree('dir27')  


import os

for dirName, sub_dirNames, fileNames in os.walk('oswalk'):
    print("目前工作目錄名稱:   ", dirName)
    print("目前子目錄名稱串列: ", sub_dirNames)
    print("目前檔案名稱串列:   ", fileNames, "\n")
    

print("------------------------------------------------------------")  # 60個

with open('app.log', 'a') as log_file:
    log_file.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - 工作項目 1\n')

print("------------------------------------------------------------")  # 60個

import shutil
import glob

log_files = glob.glob('/path/to/logs/*.log')
backup_path = '/path/to/backup/'

for log_file in log_files:
    shutil.copy(log_file, backup_path + time.strftime("%Y%m%d_%H%M%S_") + log_file.split('/')[-1])

print("------------------------------------------------------------")  # 60個




import os

print(os.listdir("D:\\Python\\ch14"))
print(os.listdir("."))      # 這代表目前工作目錄





"""


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
