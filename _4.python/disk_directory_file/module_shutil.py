import sys
import shutil

filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2 = 'picture1b.jpg'
filename3 = 'picture1c.jpg'

foldername1 = 'C:/_git/vcs/_1.data/______test_files5'
foldername2 = 'C:/_git/vcs/_1.data/______test_files6'

print("------------------------------------------------------------")  # 60個

print('顯示終端機設定')

WIDTH = shutil.get_terminal_size()[0]

print('WIDTH = ', WIDTH)
print(shutil.get_terminal_size())
print(shutil.get_terminal_size()[0])
print(shutil.get_terminal_size()[1])

print("------------------------------------------------------------")  # 60個

sys.exit()

print("複製 檔案 -> 檔案")
shutil.copy(filename1, filename2)
shutil.copy(filename1, filename3)

print("複製 檔案 -> 資料夾")
shutil.copy(filename1, foldername1)

print("------------------------------------------------------------")  # 60個

print("複製 資料夾 -> 資料夾")
shutil.copytree(foldername1, foldername2)

print("------------------------------------------------------------")  # 60個

print("移動 檔案 -> 資料夾")
shutil.move(filename2, foldername2)

print("------------------------------------------------------------")  # 60個

filename3 = 'picture1c.jpg'
filename4 = 'picture1d.jpg'

print("更改檔案名稱")
shutil.move(filename3, filename4)

print("------------------------------------------------------------")  # 60個

print("移動 資料夾 -> 資料夾")

foldername2 = 'C:/_git/vcs/_1.data/______test_files6'
foldername3 = 'C:/_git/vcs/_1.data/______test_files6b'

shutil.move(foldername2, foldername3)

print("------------------------------------------------------------")  # 60個

print("刪除 資料夾")
shutil.rmtree(foldername3)

print("------------------------------------------------------------")  # 60個



""" 新進
import os
import shutil
cur_path = os.path.dirname(__file__) # 取得目前路徑
destfile = cur_path + "\\" + "newfile.py"
print(cur_path)
print(destfile)
#shutil.copy("shutil.py", destfile )  # 檔案複製


print("------------------------------------------------------------")  # 60個


shutil.copyfile(KEYWORD_FILE, TEST_PY_FILE)


bak = file + ".bak"
shutil.copyfile(file, bak)
print("backed up", file, "to", bak)


print("------------------------------------------------------------")  # 60個

#shutil.move() 重命名或移動文件的功能。

import shutil
shutil.move('/path/to/dir/filename.txt', '/path/to/dir/new_filename.txt')
 

import shutil
print(srcfile, ' -> ', destfile)
shutil.copy(srcfile,destfile); # 複製檔案

print('------------------------------------------------------------')	#60個


import sys

import shutil, pathlib

filename1 =  'temp.txt'
filename2 =  'temp_cpd.txt'

print(pathlib.Path.cwd())

path = pathlib.Path.cwd() / filename2

print('cccc : ', path)

if path.exists() == True:
    print("\n該檔名已存在")
else:
    is_Success = shutil.copyfile(filename1, filename2)
    print("已複製完成檔案{}：".format(is_Success))

    is_Move = shutil.move(filename2, "C:\\dddddddddd")
    print("並移動至該路徑：{}".format(is_Move))

print('------------------------------------------------------------')	#60個

import shutil, pathlib

file = str(input("請輸入欲要複製的檔名(可含副檔名)："))
copyFile = str(input("請輸入複製檔案的名稱(可含副檔名):"))

path = pathlib.Path.cwd() / copyFile

if path.exists() == True:
    print("\n該檔名已存在")
else:
    is_Success = shutil.copyfile(file, copyFile)
    print("已複製完成檔案{}：".format(is_Success))

    is_Move = shutil.move(copyFile, "D:\\")
    print("並移動至該路徑：{}".format(is_Move))


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個




"""


