#!/usr/bin/python
import time;  # This is required to include time module.

#取得tick數
ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)


#獲取當前時間
localtime = time.localtime(time.time())
print("Local current time :", localtime)


#獲取格式化的時間
localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)

#獲取日曆月份
import calendar

cal = calendar.month(2019, 4)
print("Here is the calendar:")
print(cal)


#import datetime
from datetime import *; from dateutil.relativedelta import *

NOW = datetime.now()
TODAY = date.today()

print(NOW)
print(TODAY)

#how old is john
johnbirthday = datetime(1978, 4, 5, 12, 0)
#relativedelta(NOW, johnbirthday)

print(relativedelta(NOW, johnbirthday))


#使用dir()內置函數返回一個包含一個模塊中定義名稱的字符串的排序列表。
#該列表包含在一個模塊中定義的所有模塊，變量和函數的名稱。

import math
content = dir(math)
print(content)


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

