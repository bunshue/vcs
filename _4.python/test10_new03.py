import os
import sys
import time
import random
import numpy as np
import pandas as pd

print('------------------------------------------------------------')	#60個

def show():
    person1={"name":"Amy","phone":"049-1234567","age":20}
    person2={"name":"Jack","phone":"02-4455666","age":25}
    person3={"name":"Nacy","phone":"04-9876543","age":17}
    persons=[person1,person2,person3]
    print(type(person1))
    print(type(person2))
    print(type(person3))
    print(type(persons))
    print(person1)
    print(person2)
    print(person3)
    print(persons)


show()

print('------------------------------------------------------------')	#60個

POSTGRES = {
    'user': 'admin',
    'password': '123456',
    'db': 'NTUHQA',
    'host': 'localhost',
    'port': '5432',
}

string = 'postgresql://%(user)s:%(password)s@%(host)s:%(port)s/%(db)s' % POSTGRES

print(string)

print('------------------------------------------------------------')	#60個

animals = ['cat', 'dog', 'bat'] 
for index, animal in enumerate(animals):
    print(index, animal)

animals = ['cat', 'dog', 'bat'] 
for animal in animals:
    print(animal)

d = {"chicken": 2, "dog": 4, "cat": 4, "spider": 8} 
for animal, legs in d.items():
    print("動物: %s 有 %d 隻腳" % (animal, legs))

d = {"chicken": 2, "dog": 4, "cat": 4, "spider": 8} 
for animal in d:
    legs = d[animal]
    print(animal, legs)




d = {"cat": "white", "dog": "black"}  # 建立字典 
print(d["cat"])       # 使用Key取得項目: 顯示 "white"
print("cat" in d)     # 是否有Key: 顯示 "True"
d["pig"] = "pink"     # 新增項目
print(d["pig"])       # 顯示 "pink"
print(d.get("monkey", "N/A"))  # 取出項目+預設值: 顯示 "N/A"
print(d.get("pig", "N/A"))     # 取出項目+預設值: 顯示 "pink"
del d["pig"]          # 使用Key刪除項目
print(d.get("pig", "N/A"))     # "pig"不存在: 顯示 "N/A"



from bs4 import BeautifulSoup

html_str = "<p>Hello World!</p>"
soup = BeautifulSoup(html_str, "lxml")
print(soup)




print('------------------------------------------------------------')	#60個


x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(type(x))

print('------------------------------------------------------------')	#60個

str1 = "Hello!\nPython"
print("不含r字元的輸出")
print(str1)
str2 = r"Hello!\nPython"
print("含r字元的輸出")
print(str2)

print('------------------------------------------------------------')	#60個

x1 = 97
x2 = chr(x1)      
print(x2)             # 輸出數值97的字元
x3 = ord(x2)
print(x3)             # 輸出字元x3的Unicode碼值
x4 = '魁'
print(ord(x4))        # 輸出字元'魁'的Unicode碼值

print('------------------------------------------------------------')	#60個

x = 0x5D            # 這是16進為整數
print(x)            # 列出10進位的結果
y = 93              # 這是10進為整數
print(hex(y))       # 列出轉換成16進位的結果

print('------------------------------------------------------------')	#60個

x = 0b1101          # 這是2進為整數
print(x)            # 列出10進位的結果
y = 13              # 這是10進為整數
print(bin(y))       # 列出轉換成2進位的結果

print('------------------------------------------------------------')	#60個

x = 100
print("100的16進位 = %x\n100的 8進位 = %o" % (x, x))

print('------------------------------------------------------------')	#60個

james = [23, 19, 22, 31, 18]                # 定義james串列
print("列印james第1-3場得分", james[0:3])
print("列印james第2-4場得分", james[1:4])
print("列印james第1,3,5場得分", james[0:6:2])


    


