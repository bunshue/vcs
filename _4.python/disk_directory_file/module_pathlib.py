"""

pathlib --- 物件導向檔案系統路徑


"""

import os
import sys
import time
import random


from pathlib import Path

print("列出子目錄：")
p = Path('.')
print(p)

print("在當前目錄樹下列出 Python 原始碼檔案：")
cc = list(p.glob('**/*.py'))
print(cc)

print("瀏覽目錄樹內部：")

foldername = 'C:/_git/vcs/_1.data'
p = Path(foldername)
q = p / '______test_files3' / '_excel'
print(q)

q.resolve()

print("查詢路徑屬性：")

print("q.exists()", q.exists())

print("q.is_dir()", q.is_dir())


foldername = 'C:/_git/vcs/_4.python/_data/'
p = Path(foldername)
q = p / 'article2.txt'
print(q)

#q.resolve()

#filename = 'C:/_git/vcs/_4.python/_data/article2.txt'

#開啟檔案：

with q.open() as f:
    cc = f.readline()
    print(cc)


import pathlib
foldername = 'C:/_git/vcs/_4.python/_data/'

cc = pathlib.PureWindowsPath(foldername).drive

print("所在的磁碟機 : ", cc)

cc = pathlib.PureWindowsPath(foldername).root

print("所在的root : ", cc)


p = pathlib.PureWindowsPath('C:/AA/BB/CC/DD/EE/FF/GG/HH/II/JJ/kk.py')
print(p.parents[0])
print(p.parents[1])
print(p.parents[2])
print(p.parents[3])
print(p.parents[4])
print(p.parents[5])

p = pathlib.PurePath('C:/AA/BB/CC/DD/EE/FF/GG/HH/II/JJ/kk.py')
#邏輯上的父路徑：
print(p.parent)


print("CWD :", pathlib.Path.cwd())
print("HOME :", pathlib.Path.home())


filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

p = pathlib.Path(filename)

print(p.stat().st_mode)

print(p.chmod(0o444))

print(p.stat().st_mode)

"""
Path.is_dir()
Path.is_file()
"""

print('------------------------------------------------------------')	#60個

'''
import pathlib
path = pathlib.Path('test10_new06.py')
abs_path = path.resolve()
print(abs_path)
new_path = str(abs_path) + ".old"
print(new_path)

print('------------------------------------------------------------')	#60個


from pathlib import Path

filepath = "檔案操作_新進1.py"
p = Path(filepath)
print("檔案路徑　　　 = " + str(p))
print("檔案名稱　　　　 = " + p.name)
print("檔案副檔名　　 = " + p.suffix)
print("檔案副檔名以外 = " + p.stem)
print("資料夾名稱　　　　 = " + p.parent.name)
print("檔案大小　　 = " + str(p.stat().st_size) + "位元組")

print("------------------------------------------------------------")  # 60個

from pathlib import Path

p = Path(".")
p = p.joinpath("newfolder")
p.mkdir(exist_ok=True)

print("------------------------------------------------------------")  # 60個

from pathlib import Path

infolder = "testfolder"
ext = "*.txt"
filelist = []
for p in Path(infolder).glob(ext):  #將這個資料夾的檔案
    filelist.append(str(p))         #新增至列表
for filename in sorted(filelist):   #再替每個檔案排序
    print(filename)

print("------------------------------------------------------------")  # 60個

from pathlib import Path

infolder = "testfolder"
ext = "*.txt"
filelist = []
for p in Path(infolder).rglob(ext): #將這個資料夾以及子資料夾的所有檔案
    filelist.append(str(p))         #新增至列表
for filename in sorted(filelist):   #再替每個檔案排序
    print(filename)

print("------------------------------------------------------------")  # 60個

from pathlib import Path

infolder = "testfolder"
ext = "*.txt"
allsize = 0
filelist = []
for p in Path(infolder).rglob(ext): #將這個資料夾以及子資料夾的所有檔案
    filelist.append(str(p))         #新增至列表
for filename in sorted(filelist):   #再替每個檔案排序
    size = Path(filename).stat().st_size
    print(filename + " = " + str(size) + "位元組")
    allsize += size
print("allsize = " + str(allsize) + "位元組")

print("------------------------------------------------------------")  # 60個



import pathlib

test_path = pathlib.Path(os.pardir)
print(test_path)
test_path.resolve()


print('------------------------------------------------------------')	#60個


import pathlib
cur_path = pathlib.Path(".")
size = 0
for text_path in cur_path.glob("*.txt"):
    if not text_path.is_symlink():
        size += text_path.stat().st_size
        
print(size)

print('------------------------------------------------------------')	#60個

import pathlib
cur_path = pathlib.Path(".")
new_path = cur_path.joinpath("backup")
size = 0
for text_path in cur_path.glob("*.txt"):
    if not text_path.is_symlink():
        size += text_path.stat().st_size
        text_path.rename(new_path.joinpath(text_path.name))
        
print(size)






print('------------------------------------------------------------')	#60個


import pathlib
cur_path = pathlib.Path(".")
FILE_PATTERN = "*.txt"
path_list = cur_path.glob(FILE_PATTERN)
print(list(path_list))
[PosixPath('item_attributes.txt'), PosixPath('related_items.txt'), PosixPath('item_info.txt')]

print("------------------------------------------------------------")  # 60個

import datetime
import pathlib
FILE_PATTERN = "*.txt"
ARCHIVE = "archive"
if __name__ == '__main__':
    
    date_string = datetime.date.today().strftime("%Y-%m-%d")
    cur_path = pathlib.Path(".")
    new_path = cur_path.joinpath(ARCHIVE, date_string)
    new_path.mkdir()                                    
    paths = cur_path.glob(FILE_PATTERN)
    for path in paths:
        path.rename(new_path.joinpath(path.name))




'''

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個




