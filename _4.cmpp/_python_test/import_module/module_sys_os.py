# python import module : sys, os

import sys
print("列印參數")
print(sys.argv)

import sys

print("參數長度 = " + str(len(sys.argv)))
print("參數長度 = {}".format(len(sys.argv)))

i = 0
for arg in sys.argv:
    print("第{}個參數是:{}".format(i,arg))
    i += 1

import sys
print("目前路徑 : ", sys.path)
print("打印系統路徑")
print(sys.path)

import os
#getcwd()方法顯示當前的工作目錄。
print("current working directory : ", os.getcwd())

os.system("ls")
#os.system("pause") 暫停
os.system("clear")

import os
filenames = os.listdir('.')
print("列出所有檔案", filenames)

zz = [name for name in filenames if name.endswith(('.jpg', '.h'))]
print('*.jpg *.h files:')
print(zz)

#重新命名檔案
#os.rename("foo.txt", "foo2.txt")
#刪除檔案
#os.remove("foo2.txt");

print("mkdir")
#os.mkdir("test_python_dir")

print("chdir")
#os.chdir("test_python_dir")

filename_r = '../data/article.txt'
print("檔案名稱 : ", os.path.getmtime(filename_r))

import os.path
filesize = os.path.getsize(filename_r)
print("filesize : " , filesize)

print("檔案時間 : ", os.path.getmtime(filename_r))
import time
print("檔案時間 : ", time.ctime(os.path.getmtime(filename_r)))


print("檔案是否存在 : ", os.path.isfile(filename_r))


import os

cur_path = os.getcwd() # 取得目前路徑  

os.system("cls")  # 清除螢幕
os.system("mkdir dir2")  # 建立 dir2 目錄
os.system("copy ossystem.py dir2\copyfile.py") # 複製檔案 

file=cur_path + "\dir2\copyfile.py" 
os.system("notepad " + file)  # 以記事本開啟 copyfile.py 檔

import os
filename=os.path.abspath("test10_new10.py")
if os.path.exists(filename): #檢查檔案是否存在
    print("完整路徑名稱：" + filename)
    print("檔案大小：" , os.path.getsize(filename))

import os
cur_path=os.getcwd() # 取得目前路徑
print("現在路徑："+cur_path)


'''
print("測試mkdir")
import os
foldername = '__temp/tmpDir'
if os.path.exists(foldername):
    os.rmdir(foldername)
else:
    print(foldername + "目錄未建立, 建立之")
    os.mkdir(foldername)  # 建立目錄

foldername = "__temp/tmpDir"
if not os.path.exists(foldername):
    os.mkdir(foldername)
else:
    print(foldername + "已經存在!")   
'''

import os
filename = "myFile.txt"
if os.path.exists(filename):
    os.remove(filename)
else:
    print(filename + "檔案未建立!")   

import os
filename=os.path.abspath("ospath.py")
if os.path.exists(filename):   
    basename=os.path.basename(filename)
    print("最後的檔案或路徑名稱：" + basename)
    
    dirname=os.path.dirname(filename)
    print("目前檔案目錄路徑：" + dirname) 
    
    print("是否為目錄：",os.path.isdir(filename))
    
    fullpath,fname=os.path.split(filename)
    print("目錄路徑：" + fullpath)
    print("檔名：" + fname)
    
    Drive,fpath=os.path.splitdrive(filename)
    print("磁碟機：" + Drive)
    print("路徑名稱：" + fpath)   
    
    fullpath = os.path.join(fullpath + "\\" + fname)
    print("組合路徑= " + fullpath)


print("系統命令")
filename_r = '../data/article.txt'
os.system("notepad " + filename_r)
#os.system("svn checkout%s -q %s %s" % (creds, url, filename))









