"""

檔案操作_新進1

"""
"""

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
"""
print("------------------------------------------------------------")  # 60個

import os

for root, dirs, files in os.walk(os.curdir):
    print("{0} has {1} files".format(root, len(files)))
    if ".git" in dirs:
        dirs.remove(".git")

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python技術者們-練功！老手帶路教你精通正宗Python程式\中文版範例檔案\Ch12_習題與解答\Ch12_動手試一試.txt

### 12.2 ###

import os.path

old_path = os.path.abspath("test.log")
print(old_path)
new_path = "{}.{}".format(old_path, "old")
print(new_path)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
