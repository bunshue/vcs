import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

'''
import datetime
today = datetime.date.today()
print('今天的日期 :', today)

print("------------------------------------------------------------")  # 60個

print("enumerate() 一個串列")

animals = ['鼠', '牛', '虎', '兔']

print('用 for')
for _ in enumerate(animals):
    print(_)

print('用 list')
print(list(enumerate(animals)))

print('用 unpacking 取出內容')

for index, ani in enumerate(animals):
    print(index, ani)

print("------------------------------------------------------------")  # 60個

print('字元相關的兩個內建函式')

print('字元轉數值')
cc = ord('豬')
print(cc)

print('數值轉字元')
nn = 35948 + 5
cc = chr(nn)
print(cc)

print("------------------------------------------------------------")  # 60個

#lambda匿名函數

# List 含有 Tuple
student = [
    ("Eugene", 1989, "Taipei"),
    ("Davie", 1993, "Kaohsiung"),
    ("Michelle", 1999, "Yilan"),
    ("Peter", 1988, "Hsinchu"),
    ("Connie", 1997, "Pingtung"),
]

# 定義sort()方法參數key
na = lambda item: item[0]
student.sort(key=na)
print("依名字排序：")
for name in student:
    print("{:6s},{}, {:10s}".format(*name))

# 直接在sort()方法帶入lamdba()函式
student.sort(key=lambda item: item[2], reverse=True)
print("依出生地遞減排序：")
for name in student:
    print("{:6s},{}, {:10s}".format(*name))

print("------------------------------------------------------------")  # 60個

print('內建函式dir()檢視目前的名稱空間')
print(dir())

print()

import qrcode
print(dir())

print()

#看單一模組的函式
import math
print(dir(math))
print()
'''
print("------------------------------------------------------------")  # 60個

import sys
print(sys.path) #查詢模組路徑

print('加入路徑')

foldername = 'C:/_git/vcs/_1.data/______test_files5'

sys.path.append(foldername)

print(sys.path) #查詢模組路徑

print("------------------------------------------------------------")  # 60個

print('使用自定義模組')
import sys

foldername = 'C:/_git/vcs/_4.python/import_module'
sys.path.append(foldername)

import module_my  #引用後, 出現 __pycache__

cc = module_my.numRand2(14, 52)
print(cc)

print(module_my.__name__)

print(__name__)



print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個






print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
