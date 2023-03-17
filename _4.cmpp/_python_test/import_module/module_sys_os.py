# python import module : sys, os

# 不包含 DDF 磁碟檔案資料夾操作

import sys
import os

print("列印參數")
print(sys.argv)
    
print("參數長度 = " + str(len(sys.argv)))
print("參數長度 = {}".format(len(sys.argv)))

#印出所有參數
i = 0
for arg in sys.argv:
    print("第{}個參數是:{}".format(i,arg))
    print(sys.argv[i])
    i += 1

print("目前路徑 : ", sys.path)
print("打印系統路徑")
print(sys.path)

print('系統命令');
os.system("cls")  # 清除螢幕
os.system("clear")
os.system("ls")
#os.system("pause") 暫停
os.system("mkdir dir2")  # 建立 dir2 目錄
os.system("copy ossystem.py dir2\copyfile.py") # 複製檔案 

print('系統命令, 開啟外部程式')

#getcwd()方法顯示當前的工作目錄。
cur_path = os.getcwd() # 取得目前路徑
print("現在路徑："+cur_path)

cur_path = os.getcwd() # 取得目前路徑
file=cur_path + "\dir2\copyfile.py" 
os.system("notepad " + file)  # 以記事本開啟 copyfile.py 檔

filename_r = '../data/article.txt'
os.system("notepad " + filename_r)
#os.system("svn checkout%s -q %s %s" % (creds, url, filename))











