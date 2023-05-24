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

import sys
print(sys.version_info)
print(sys.version_info[0])
if sys.version_info[0] >= 3:
    print('python 新版')
else:
    print('python 舊版')
    
if sys.version < '3':
    print('python 舊版')
else:
    print('python 新版')


import os

print(__file__)

print(os.path.abspath(__file__))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

DIRS = os.path.join(BASE_DIR, 'templates')
NAME = os.path.join(BASE_DIR, 'db.sqlite3')
AAAA = os.path.join(BASE_DIR, 'static')

print(DIRS)
print(NAME)
print(AAAA)


import os

PATH = "/".join(os.path.abspath(__file__).split("/")[:-2])

#sys.path.append(PATH)
print(PATH)

import os

print(os.environ.get("CI_COMMIT_TAG", "0.0.0"))
_version = os.environ.get("CI_COMMIT_TAG", "0.0.1.dev2")


'''here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()
'''

print(sys.platform)

if sys.platform.startswith("win"):
    print('你用的作業系統是Windows')
else:
    print('你用的作業系統不是Windows')

import sys
if sys.platform == 'win32':
    print('Windows')
else:
    print('Non-Windows')

print("Python:", sys.version)
print(sys.version)
print(sys.version)

import sys
print(sys.path)
sys.exit(1)	#立刻退出程式

#強制離開程式, 並說明原因
sys.exit('強制離開程式, 並說明原因')




