"""

檔案操作_新進1

"""
'''

import os
import os.path
import shutil

FileName1='workfile.txt'
FileName2='workfileCopy.txt'
FileName3='workfileRename.txt'

def FunListAllFiles():
    allFiles = os.listdir('.')
    print('allfiles :', allFiles)

print('-----------')
FunListAllFiles()
if os.path.isfile(FileName1) and os.access(FileName1, os.R_OK):
    shutil.copy(FileName1, FileName2)   

print('-----------')
FunListAllFiles()
if os.path.isfile(FileName2) and os.access(FileName2, os.R_OK):
    os.rename(FileName2, FileName3)   

print('-----------')
FunListAllFiles()
if os.path.isfile(FileName3) and os.access(FileName3, os.R_OK): 
    os.remove(FileName3)
    print('%s deleted' %(FileName3))   

print('-----------')
FunListAllFiles()
print('-----------')


print('------------------------------------------------------------')	#60個

import os
import os.path

if os.path.exists('./folder'):
    os.rmdir('./folder')
    print(os.getcwd())    
else: 
    os.mkdir('./folder')  
    os.chdir('./folder')
    print(os.getcwd())    
'''
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

print('------------------------------------------------------------')	#60個




import os
for root, dirs, files in os.walk(os.curdir):
    print("{0} has {1} files".format(root, len(files)))
    if ".git" in dirs:
        dirs.remove(".git")    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python技術者們-練功！老手帶路教你精通正宗Python程式\中文版範例檔案\Ch12_習題與解答\Ch12_動手試一試.txt

### 12.2 ###

import os.path
old_path = os.path.abspath('test.log')
print(old_path)
new_path = '{}.{}'.format(old_path, "old")
print(new_path)


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





print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個

