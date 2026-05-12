"""

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

h = 3 + 4j
print(type(h))
print(h)

print(abs(h))

print("------------------------------------------------------------")  # 60個

print("HEX: \x48\x45\x58")

print("------------------------------------------------------------")  # 60個

name = "david"
balance = 5000
print("姓名: %s 的帳戶餘額是 %d" % (name, balance))

print("------------------------------------------------------------")  # 60個

x, y = 10, 20
s = "Y= {} X= {}".format(x, y)
print(s)

print("------------------------------------------------------------")  # 60個

x, y = 10, 20
s = "Y= {1} X= {0}".format(x, y)
print(s)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 字串就是Unicode編碼成的串列
name1 = str("IMS群曜醫電")
for ch in name1:
    print(ch, ord(ch), hex(ord(ch)))  # ord()取出字串的Unicode的編碼值

unicode_array=[32676,26332,37291,38651]
for unicode in unicode_array:
    print(unicode, chr(unicode))  # chr()Unicode編碼值轉字串


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch04\ch4-1-3a.py

str1 = "Hello World!"
print("str1 = " + str1)
s = len(str1)
print("len(str1) = " + str(s))
s = max(str1)
print("max(str1) = " + s)
s = min(str1)
print("min(str1) = " + s)

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch04\ch4-1-3b.py

str1 = "welcome to python"
print("str1 = " + str1)
b = str1.isalnum()
print("str1.isalnum() = " + str(b))
b = str1.isalpha()
print("str1.isalpha() = " + str(b))
b = str1.isdigit()
print("str1.isdigit() = " + str(b))
b = "2022".isdigit()
print('"2022".isdigit() = ' + str(b))
b = str1.isidentifier()
print("str1.isidentifier() = " + str(b))
b = str1.islower()
print("str1.islower() = " + str(b))
b = str1.isupper()
print("str1.isupper() = " + str(b))
b = "   ".isspace()
print('"   ".isspace() = ' + str(b))

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch04\ch4-1-3c.py

str1 = "welcome to python"
print("str1 = " + str1)
b = str1.endswith("thon")
print("str1.endswith('thon') = " + str(b))
b = str1.startswith("hello")
print("str1.startswith('hello') = " + str(b))
b = str1.count("o")
print("str1.count('o') = " + str(b))
b = str1.find("come")
print("str1.find('come') = " + str(b))
b = str1.find("become")
print("str1.find('become') = " + str(b))
b = str1.find("o")
print("str1.find('o') = " + str(b))
b = str1.find("e")
print("str1.find('e') = " + str(b))
b = str1.rfind("o")
print("str1.rfind('o') = " + str(b))
b = str1.rfind("e")
print("str1.rfind('e') = " + str(b))

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch04\ch4-1-3d.py

str1 = "welcome to python"
print("str1 = " + str1)
str2 = "Welcome to Python"
print("str2 = " + str2)
str3 = "This is a test."
print("str3 = " + str3)
s = str1.capitalize()
print("str1.capitalize() = " + s)
s = str2.lower()
print("str2.lower() = " + s)
s = str1.upper()
print("str1.upper() = " + s)
s = str1.title()
print("str1.title() = " + s)
s = str2.swapcase()
print("str2.swapcase() = " + s)
s = str3.replace("is", "was")
print("str3.replace('is', 'was') = " + s)
str4 = "Tom,Bob,Mary,Joe,John"
lst1 = str4.split(",")
print(lst1)
str5 = "23\n52\n44\n78"
lst2 = str5.split("\n")
print(lst2)
lst3 = str5.splitlines()
print(lst3)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch04\ch4-2-1.py

lst1 = [1, 2, 3, 4, 5]
lst2 = [1, "Python", 5.5]
lst3 = list(["tom", "mary", "joe"])
lst4 = list("python")
lst5 = [1, ["tom", "mary", "joe"], [3, 4, 5]]
print(lst1)
print(lst2, lst3, lst4)
print("lst5:" + str(lst5))

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch04\ch4-2-2.py

lst1 = [1, 2, 3, 4, 5, 6]
print(lst1[0])
print(lst1[1])
print(lst1[-1])
print(lst1[-2])

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch04\ch4-2-2a.py

lst1 = [1, 2, 3, 4, 5, 6]
lst1[1] = 10
lst1[2] = "Python"
print(lst1)

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch04\ch4-2-2b.py

lst1 = [1, 2, 3, 4, 5, 6]
for e in lst1:
    print(e, end=" ")


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch04\ch4-2-2c.py

animals = ["cat", "dog", "bat"]
for index, animal in enumerate(animals):
    print(index, animal)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch04\ch4-2-2d.py

lst2 = [[2, 4], ["cat", "dog", "bat"], [1, 3, 5]]
print(lst2[1][0])
lst2[2][1] = 7
print(lst2)

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch04\ch4-2-2e.py

lst2 = [[2, 4], ["cat", "dog", "bat"], [1, 3, 5]]
for e1 in lst2:
    for e2 in e1:
        print(e2, end=" ")


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch04\ch4-2-3.py

lst1 = [1, 5]
lst1.append(7)
print(lst1)
lst1.extend([9, 11, 13])
print(lst1)

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch04\ch4-2-3a.py

lst1 = [1, 5]
lst1.insert(1, 3)
print(lst1)

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch04\ch4-2-3b.py

lst1 = [1, 3, 5, 7, 9, 11, 13]
del lst1[2]
print(lst1)
e1 = lst1.pop()
print(e1, lst1)
e2 = lst1.pop(1)
print(e2, lst1)
lst1.remove(9)
print(lst1)

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch04\ch4-2-4.py

lst1 = [4, 2, 8, 9, 1]
print("lst1 = " + str(lst1))
s = len(lst1)
print("len(lst1) = " + str(s))
s = max(lst1)
print("max(lst1) = " + str(s))
s = min(lst1)
print("min(lst1) = " + str(s))
str1 = "Hello"
lst2 = list(str1)
print("lst2 = " + str(lst2))
for i, v in enumerate(lst2, 0):
    print(i, ":", v, end=" ")
print()
s = sum(lst1)
print("sum(lst1) = " + str(s))
lst3 = sorted(lst1)
print("lst3 = sorted(lst1) = " + str(lst3))

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch04\ch4-2-4a.py

lst1 = [4, 2, 8, 9, 1, 8]
print("lst1 = " + str(lst1))
s = lst1.count(8)
print("lst1.count(8) = " + str(s))
s = lst1.index(8)
print("lst1.index(8) = " + str(s))
s = lst1.index(1)
print("lst1.index(1) = " + str(s))
lst1.sort()
print("lst1.sort() = " + str(lst1))
lst1.reverse()
print("lst1.reverse() = " + str(lst1))

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

d1 = {"chicken": 2, "dog": 4, "cat": 3}
d1["spider"] = 8
print(d1)

print("------------------------------------------------------------")  # 60個

d1 = {1: 1, 3: 9, 5: 24, 7: 47, 9: 83}
print("d1 = " + str(d1))
s = len(d1)
d2 = dict([(1, "tom"), (2, "mary"), (3, "joe")])
print("d2 = " + str(d2))
d3 = sorted(d1)
print("d3 = sorted(d1) = " + str(d3))

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch04\ch4-4-4a.py

d1 = {"tom": 2, "bob": 3, "mike": 4}
print("d1 = " + str(d1))
i = d1.get("tom")
print("d1.get('tom') = " + str(i))
i = d1.get("jerry", "不存在")
print("d1.get('jerry', '不存在') = " + str(i))
t1 = d1.keys()
print("d1.keys() = " + str(t1))
lst1 = list(t1)
for i in lst1:
    print(i, end=" ")
print()
t1 = d1.values()
print("d1.values() = " + str(t1))
lst1 = list(t1)
for i in lst1:
    print(i, end=" ")


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch04\ch4-5-1.py

str1, str2 = "Hello ", "World!"
str3 = str1 + str2
print(str3)
lst1, lst2 = [2, 4], [6, 8, 10]
lst3 = lst1 + lst2
print(lst3)
t1, t2 = (2, 4), (6, 8, 10)
t3 = t1 + t2
print(t3)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
'''
r = abs(-10)
print("abs(-10) = " + str(r))
r = abs(5)
print("abs(5) = " + str(r))
r = pow(8, 2)
print("pow(8, 2) = " + str(r))
r = pow(2, 3)
print("pow(2, 3) = " + str(r))
r = max(9, 3, 12, 32, 81, 92)
print("max(9, 3, 12, 32, 81, 92) = " + str(r))
r = min(9, 3, 12, 32, 81, 92)
print("min(9, 3, 12, 32, 81, 92) = " + str(r))
r = round(5.32)
print("round(5.32) = " + str(r))
r = round(5.52)
print("round(5.52) = " + str(r))
r = round(3.14568757, 3)
print("round(3.14568757, 3) = " + str(r))
r = round(3.14568757, 1)
print("round(3.14568757, 1) = " + str(r))
'''
print("------------------------------------------------------------")  # 60個

path = os.getcwd() + "/temp"
os.chdir(path)
print(path)
print(os.listdir(path))
os.mkdir("newDir")
print("mkdir(): ", os.listdir(path))
os.rename("newDir", "newDir2")
print("rename(): ", os.listdir(path))
os.rmdir("newDir2")
fp = open("aa.txt", "w")
fp.close()
print("rmdir(): ", os.listdir(path))
os.remove("aa.txt")
print("remove(): ", os.listdir(path))

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch05\ch5-3-2.py

import os.path as path

fname = path.realpath("ch5-3-2.py")
print(fname)
r = path.split(fname)
print("os.path.split() =", r)
r = path.splitext(fname)
print("os.path.splitext() =", r)
p = path.dirname(fname)
print("p = os.path.dirname() =", p)
f = path.basename(fname)
print("f = os.path.basename() =", f)
r = path.join(p, f)
print("os.path.join(p,f) =", r)

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch05\ch5-3-3.py

files = (os.getcwd(), "ch5-3-3.py")
for f in files:
    print("項目 = " + str(f))
    if os.path.exists(f):
        print("存在!")
    if os.path.isdir(f):
        print("是目錄!")
    if os.path.isfile(f):
        print("是檔案!")


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch05\ch5-4-1.py

fp = open("note.txt", "w")
if fp != None:
    print("檔案開啟成功!")
    fp.write("陳會安\n")
    fp.write("江小魚\n")
    print("已經寫入2個姓名到檔案note.txt!")
fp.close()

print("------------------------------------------------------------")  # 60個

fp = open("note.txt", "a")
fp.write("陳允傑\n")
print("已經新增1個姓名到檔案note.txt!")
fp.close()

print("------------------------------------------------------------")  # 60個

fp = open("note.txt", "r")
str1 = fp.read()
print(str1)
fp.close()

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch05\ch5-4-3a.py

fp = open("note.txt", "r")
lst1 = fp.readlines()
print(lst1)
for line in lst1:
    print(line, end="")
fp.close()

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch05\ch5-4-3b.py

with open("note.txt", "r") as fp:
    str1 = fp.read()
    print(str1)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch05\ch5-4-3c.py

fp = open("note.txt", "r")
str1 = fp.read(1)
str2 = fp.readline()
str3 = fp.readline()
str4 = fp.read(2)
print(str1)
print(str2)
print(str3)
print(str4)
fp.close()

print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch05\ch5-5.py

try:
    fp = open("myfile.txt", "r")
    print(fp.read())
    fp.close()
except FileNotFoundError:
    print("錯誤: myfile.txt檔案不存在!")


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\超簡單Python+MicroPython物聯網應用\ch05\ch5-5a.py

fp = open("myfile.txt", "r")
print(fp.read())
fp.close()

print("------------------------------------------------------------")  # 60個







print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



