import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

import random

print(dir(random))

print("------------------------------------------------------------")  # 60個


import os
 
path = os.getcwd() + "\\temp"
os.chdir(path)
print(path)
print(os.listdir(path))

print("------------------------------------------------------------")  # 60個

import os
 
path = os.getcwd()
new_path = os.getcwd() + "\\temp"
print("目前工作路徑: ", path)
print(new_path)
os.chdir(new_path)
print("chdir(): ", new_path)
os.mkdir('newDir')
print("mkdir(): ", os.listdir(new_path))

print("------------------------------------------------------------")  # 60個

import os
 
new_path = os.getcwd() + "\\temp"
print(new_path)
os.chdir(new_path)
os.rename('newDir','newDir2')
print("rename(): ", os.listdir(new_path))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-2-1c.py

import os
 
new_path = os.getcwd() + "\\temp"
print(new_path)
os.chdir(new_path)
os.rmdir('newDir2')
fp = open("aa.txt", "w")
fp.close()
print("rmdir(): ", os.listdir(new_path))
os.remove("aa.txt")
print("remove(): ", os.listdir(new_path))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-2-2.py

import os.path as path
 
fname = path.realpath("ch11-2-2.py")
print(fname)
r = path.split(fname)
print("os.path.split() =", r)
r = path.splitext(fname)
print("os.path.splitext() =", r)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-2-2a.py

import os.path as path
 
fname = path.realpath("ch11-2-2.py")
print(fname)
p = path.dirname(fname)
print("p = os.path.dirname() =", p)
f = path.basename(fname)
print("f = os.path.basename() =", f)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-2-2b.py

import os.path as path
 
p = "D:\PythonChatGPT\ch11"
f = "ch11-2-2.py"
print(p, f)
r = path.join(p, f)
print("os.path.join(p,f) =", r)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-3-1.py

import math
 
# 顯示數學常數
print("math.e = ", math.e)
print("math.pi = ", math.pi)

print("------------------------------------------------------------")  # 60個

import math
 
# 數學函數
no = -19.536
print("測試值no = ", no)
print("math.fabs(no) =  ", math.fabs(no))
print("math.ceil(no) = ", math.ceil(no))
print("math.floor(no) = ", math.floor(no))
# 指數和對數函數
x, y = 13.536, 3.57
print("測試值x / y = ", x, "/", y)
print("math.exp(x) = ", math.exp(x))
print("math.log(x) = ", math.log(x))
print("math.pow(x,y) = ", math.pow(x,y))
print("math.sqrt(x) = ", math.sqrt(x))
# 三角函數
deg = 60.0
rad = math.radians(deg)
print("測試值deg / rad = ", deg, "/", rad)
print("math.sin(rad) = ", math.sin(rad))
print("math.cos(rad) = ", math.cos(rad))
print("math.tan(rad) = ", math.tan(rad)) 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-3-2.py

import random

r1 = random.randint(1, 6)
r2 = random.randint(1, 6)
print(r1 + r2)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-3-2a.py

import random

lst1 = list(range(11))
print(lst1)
r3 = random.choice(lst1)
print(r3)


print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-4-1.py

fp = open("note.txt", "w")
if fp != None:
    print("檔案開啟成功!")
fp.close()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-4-1a.py

fp = open("temp\\note.txt", "w")
if fp != None:
    print("檔案開啟成功!")
fp.close()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-4-1b.py

fp = open("temp/note.txt", "w")
if fp != None:
    print("檔案開啟成功!")
fp.close()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-4-2.py

fp = open("note.txt", "w")
fp.write("陳會安\n")
fp.write("江小魚\n")
print("已經寫入2個姓名到檔案note.txt!")
fp.close()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-4-2a.py

fp = open("temp/note.txt", "w")
fp.write("陳會安")
fp.write("江小魚")
print("已經寫入2個姓名到檔案note.txt!")
fp.close()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-4-3.py

fp = open("note.txt", "a")
fp.write("陳允傑\n")
print("已經新增1個姓名到檔案note.txt!")
fp.close()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-4-3a.py

fp = open("temp/note.txt", "a")
fp.write("陳允傑")
print("已經新增1個姓名到檔案note.txt!")
fp.close()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-4-4.py

fp = open("note.txt", "r")
str1 = fp.read()
print("檔案內容:")
print(str1)
fp.close()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-4-4a.py

fp = open("note.txt", "r")
list1 = fp.readlines()
print("檔案內容:")
print(list1)
for line in list1:
    print(line, end="")    
fp.close()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-4-5.py

fp = open("note.txt", "r")
str1 = fp.read(1)
str2 = fp.read(2)
print("檔案內容:")
print(str1)
print(str2)
fp.close()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-4-5a.py

fp = open("note.txt", "r")
str1 = fp.readline()
str2 = fp.readline()
print("檔案內容:")
print(str1)
print(str2)
fp.close()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-4-6.py

with open("note.txt", "r") as fp:
    str1 = fp.read()
    print("檔案內容:")
    print(str1)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-4-6a.py

fp = open("note.txt", "r")
print("檔案內容(有換行):")
for line in fp:
    print(line)
fp.close() 
fp = open("note.txt", "r")   
print("檔案內容(沒換行):")
for line in fp:
    print(line, end="")    
fp.close()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-4-7.py

from check_file import check_txt_file

result = check_txt_file('note.txt')
print(result)  # 如果檔案存在，輸出True；否則輸出False

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-5-1.py

try:
    fp = open("myfile.txt", "r")
    print(fp.read())
    fp.close()
except FileNotFoundError:
    print("錯誤! myfile.txt檔案不存在!")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-5-2.py

try:
    n1, n2 = eval(input("輸入2個整數n1,n2: "))
    r = n1 / n2
    print("r=", r)
except ZeroDivisionError:
    print("錯誤! 除以0")
except SyntaxError:
    print("錯誤! 數字需逗號分隔")
except:
    print("錯誤! 輸入錯誤!")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-5-2a.py

m = 10
eval("print('Python')")
eval("print(50 + 10)")
eval("print(55 / 7)")
eval("print(m + 5)")
eval("print('m' * 5)")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\ch11-5-3.py

try:
    n1, n2 = eval(input("輸入2個整數n1,n2: "))
    r = n1 / n2
    print("r=", r)
except:
    print("錯誤: 輸入或運算錯誤!")
else:
    print("Else: 資料輸入正確!")
finally:
    print("Finally: 有輸入資料!")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\check_file.py

import os

def check_txt_file(file_path):
    """
    檢查指定路徑的檔案是否存在，如果存在就回傳True；不存在就回傳False。
    """
    if os.path.isfile(file_path) and file_path.endswith(".txt"):
        return True
    else:
        return False


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\convert_temp.py

def convert_to_f(c):
    f = (9.0 * c) / 5.0 + 32.0
    return f

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\hello.py

# hello.py
def say_hello():
    print("Hello, world!")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\main.py

# main.py
import hello

hello.say_hello()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python X ChatGPT：零基礎AI聊天用流程圖學Python程式設計\ch11\mybmi.py

name = None

def bmi(h, w):
    r = w/h/h
    return r

print("------------------------------------------------------------")  # 60個







print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


