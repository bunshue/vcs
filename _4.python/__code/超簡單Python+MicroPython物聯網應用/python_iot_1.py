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

fp = open("note.txt", "r")
lst1 = fp.readlines()
print(lst1)
for line in lst1:
    print(line, end="")
fp.close()

print("------------------------------------------------------------")  # 60個

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



