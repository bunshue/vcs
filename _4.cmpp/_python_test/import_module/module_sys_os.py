# python import module : sys, os

# 不包含 DDF 磁碟檔案資料夾操作

import sys
print("列印參數")
print(sys.argv)
    
import sys

print("參數長度 = " + str(len(sys.argv)))
print("參數長度 = {}".format(len(sys.argv)))


#印出所有參數
i = 0
for arg in sys.argv:
    print("第{}個參數是:{}".format(i,arg))
    i += 1

#sys.argv[1]

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


print("系統命令")
filename_r = '../data/article.txt'
os.system("notepad " + filename_r)
#os.system("svn checkout%s -q %s %s" % (creds, url, filename))


import glob, os

allfiles = glob.glob('*.jpg') + glob.glob('*.png')
count = 1
for afile in allfiles:
	print(afile)
	ext = afile.split('.')[-1]
	newfilename = "{}.{}".format(str(count), ext)
	os.rename(afile, newfilename)
	count += 1
print("完成...")


import os, hashlib, glob

allfiles = glob.glob('*.jpg') + glob.glob('*.png')

allmd5s = dict()
for imagefile in allfiles:
	print(imagefile + " is processing...")
	img_md5 = hashlib.md5(open(imagefile,'rb').read()).digest()
	if img_md5 in allmd5s:
		print("---------------")
		print("以下為重覆的檔案：")
		os.system("open " + os.path.abspath(imagefile))
		os.system("open " + allmd5s[img_md5])
	else:
		allmd5s[img_md5] = 	os.path.abspath(imagefile) 



import os, hashlib, glob

allfiles = glob.glob('*.jpg') + glob.glob('*.png')

allmd5s = dict()
for imagefile in allfiles:
	print(imagefile + " is processing...")
	img_md5 = hashlib.md5(open(imagefile,'rb').read()).digest()
	if img_md5 in allmd5s:
		print("---------------")
		print("以下為重覆的檔案：")
		print(os.path.abspath(imagefile))
		print(allmd5s[img_md5])
	else:
		allmd5s[img_md5] = 	os.path.abspath(imagefile) 













