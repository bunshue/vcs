# 各種import


import sys
print("打印系統路徑")
print(sys.path)


import os
os.system("ls")
os.system("pause")


import os
filenames = os.listdir('.')
print('all files:')
print(filenames)

zz = [name for name in filenames if name.endswith(('.jpg', '.h'))]
print('*.jpg *.h files:')
print(zz)


# Open a file
fo = open("foo.txt", "w")
fo.write("abcdefghijklmnopqrstuvwxyz");

# Close opend file
fo.close()

# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10);
print("read 10 string is : ", str)

# Check current position
position = fo.tell();
print("current file position : ", position)

print("seek to position 20")
fo.seek(20)

str = fo.read(10);
print("read 10 string is : ", str)

print("go to file head")
fo.seek(0)
str = fo.read(10);
print("read 10 string is : ", str)
# Close opend file
fo.close()

import os
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


import urllib
import urllib.request
 
data={}
data['word']='Jecvay Notes'
 
url_values=urllib.parse.urlencode(data)
url="http://www.baidu.com/s?"
full_url=url+url_values
 
data=urllib.request.urlopen(full_url).read()
data=data.decode('UTF-8')
print(data)



#字典(dictionary)的資料型態

mydict = {'a':3, 'b':2, 'c':5}

print(mydict['a'])

mydict['d'] = 7


print(mydict)

