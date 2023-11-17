"""

檔案操作_新進1

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

print('------------------------------------------------------------')	#60個

