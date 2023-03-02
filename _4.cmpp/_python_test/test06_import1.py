# 各種import

import sys
print("目前路徑 : ", sys.path)
print("打印系統路徑")
print(sys.path)


import os
path = os.getcwd()
print("current path is ", path)

os.system("ls")
os.system("pause")

filenames = os.listdir('.')
print('all files:')
print(filenames)

zz = [name for name in filenames if name.endswith(('.jpg', '.h'))]
print('*.jpg *.h files:')
print(zz)

#重新命名檔案
#os.rename("foo.txt", "foo2.txt")
#刪除檔案
#os.remove("foo2.txt");

#建立目錄
#os.mkdir("test_python_dir")

os.chdir("test_python_dir")

#getcwd()方法顯示當前的工作目錄。
print("current working directory : ", os.getcwd())


#異常處理
#刪除目錄
try:
    os.rmdir("aaaaa");
    print("remove directory aaaaa OK")
except IOError:
   print("Error: can't find file or read data")
else:
    print("remove directory aaaaa fail")




