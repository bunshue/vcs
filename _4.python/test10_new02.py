import os
import sys
import time
import random


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


#! /usr/bin/env python3
"""n2w: 數字轉英文模組, 包含一個num2words函式, 也能獨立執行
獨立執行用法: n2w num
              num: 0~999,999,999,999,999 之間的整數 (可用逗號分隔)
範例: n2w 10,003,103
輸入 10,003,103 後會輸出 ten million three thousand one hundred three
"""

import sys, string, argparse

# 數字與英文的對應字典
_1to9dict = {
    "0": "",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}
_10to19dict = {
    "0": "ten",
    "1": "eleven",
    "2": "twelve",
    "3": "thirteen",
    "4": "fourteen",
    "5": "fifteen",
    "6": "sixteen",
    "7": "seventeen",
    "8": "eighteen",
    "9": "nineteen",
}
_20to90dict = {
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety",
}

# 數字位數與數字英文單位的對應串列(list)
_magnitude_list = [
    (0, ""),
    (3, " thousand "),
    (6, " million "),
    (9, " billion "),
    (12, " trillion "),
    (15, ""),
]


# 數字轉英文的函式
def num2words(num_string):
    """num2words(num_string): convert number to English words"""
    if num_string == "0":
        return "zero"
    num_string = num_string.replace(",", "")
    num_length = len(num_string)
    max_digits = _magnitude_list[-1][0]
    if num_length > max_digits:
        return "Sorry, can't handle numbers with more than  " "{0} digits".format(
            max_digits
        )
    num_string = "00" + num_string
    word_string = ""

    # 用迴圈從數字最右邊逐次取三個數字來處理，亦即從右邊三個一組進行轉換
    for mag, name in _magnitude_list:
        if mag >= num_length:
            return word_string
        else:
            hundreds, tens, ones = (
                num_string[-mag - 3],
                num_string[-mag - 2],
                num_string[-mag - 1],
            )
            if not (hundreds == tens == ones == "0"):
                word_string = _handle1to999(hundreds, tens, ones) + name + word_string


# 處理1~999的函式
def _handle1to999(hundreds, tens, ones):
    if hundreds == "0":
        return _handle1to99(tens, ones)
    else:
        return _1to9dict[hundreds] + " hundred " + _handle1to99(tens, ones)


# 處理1~99的函式
def _handle1to99(tens, ones):
    if tens == "0":
        return _1to9dict[ones]
    elif tens == "1":
        return _10to19dict[ones]
    else:
        return _20to90dict[tens] + " " + _1to9dict[ones]


num = "12345678"
# 將第一個命令列參數值轉為英文，其餘命令列參數不處理
result = num2words(num)
print("{0} 的英文念法是: {1}".format(num, result))

print("------------------------------------------------------------")  # 60個

rawdata = """我
我的
眼睛
妳
妳的
心
溫柔
日子
雨
風
天空
雲
等待
哭泣
戀愛
相遇
分離
忘記
心醉
驀然
吹過
思念
靈魂
停止"""
words = rawdata.split("\n")


def poem():
    n = np.random.randint(2, 8)  # 2-8句, 決定有幾句

    for i in range(n):
        m = np.random.randint(1, 6)  # 決定每句的長度
        sentence = np.random.choice(words, m, replace=False)
        print(" ".join(sentence))


poem()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


word = "maintenance"
word.count("n")

len("thunderbolt")


animal = ["cat", "dog", "duck"]
len(animal)


max(100, 10, 50)
min(300, 30, 3000)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

import zipfile

files = zipfile.ZipFile("C:/workplace/test.zip")

files.namelist()

files.extract("d/c.txt")

files.extractall()

files.close()

print("------------------------------------------------------------")  # 60個

import requests

r = requests.get("https://tw.yahoo.com/")
print(r.text)

print("------------------------------------------------------------")  # 60個

import pprint

r = requests.get("https://tw.yahoo.com/")
pprint.pprint(r.text)


print("------------------------------------------------------------")  # 60個

import requests

base_url = "https://zipcloud.ibsnet.co.jp/api/search"

query_parameter = "?zipcode="

zipcode = "1600021"

request_url = base_url + query_parameter + zipcode

request_url

requests.get(request_url).json()


# 有這樣的 API 啊，網址是：https://zipcloud.ibsnet.co.jp/doc/api，請幫我寫出來


print("------------------------------------------------------------")  # 60個

import requests, pprint

api_url = "https://zh.wikipedia.org/w/api.php"

api_params = {
    "format": "json",
    "action": "query",
    "titles": "柔道",
    "prop": "revisions",
    "rvprop": "content",
}

wiki_data = requests.get(api_url, params=api_params).json()

pprint.pprint(wiki_data)


# pip install wikipedia


import wikipedia

wikipedia.set_lang("zh")
wikipedia.summary("柔道")


# python wiki_sample.py


# python try_sys.py 想查詢的關鍵字


# python wiki_sample_final.py 柔道


print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

soup = BeautifulSoup("<html> Lollipop </html>", "html.parser")

print("------------------------------------------------------------")  # 60個

import requests

from bs4 import BeautifulSoup

html_data = requests.get("http://tw.yahoo.com")

soup = BeautifulSoup(html_data.text, "html.parser")

soup.title


print("------------------------------------------------------------")  # 60個

import requests

from bs4 import BeautifulSoup

game_ranking_html = requests.get(
    "https://www.kamatari.org/blog/2021/best-games-of-2021/"
)

soup = BeautifulSoup(game_ranking_html.text, "html.parser")

for game in soup.findAll("h2"):
    print(game.text)


print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup

game_ranking_html = requests.get(
    "https://www.kamatari.org/blog/2021/best-games-of-2021/"
)
soup = BeautifulSoup(game_ranking_html.text, "html.parser")
for game in soup.findAll("h2"):
    print(game.text)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


'''
print('------------------------------------------------------------')	#60個

print(np.c_[np.array([1, 2, 3]), np.array([4, 5, 6])])
print(np.c_[np.array([[1, 2, 3]]), 0, 0, np.array([[4, 5, 6]])])

"""
array([[1, 4],
       [2, 5],
       [3, 6]])
"""

#array([[1, 2, 3, ..., 4, 5, 6]])

print('------------------------------------------------------------')	#60個

#numpy.c_() and numpy.r_()的用法


#####np.c_是按行连接两个矩阵，就是把两矩阵左右相加，要求行数相等，类似于pandas中的merge()。
#####np.r_是按列连接两个矩阵，就是把两矩阵上下相加，要求列数相等，类似于pandas中的concat()。

#np.c_是按行连接两个矩阵，就是把两矩阵左右相加，要求行数相等。
#np.r_是按列连接两个矩阵，就是把两矩阵上下相加，要求列数相等。


#1.numpy.c_:

import numpy as np

x = np.arange(12).reshape(3,4)
print('x:',x, x.shape)

y = np.arange(10,22).reshape(3,4)
print('y:',y, y.shape)

z = np.c_[x,y]
print('z:',z, z.shape)

#2.numpy.r_用法:

import numpy as np

x = np.arange(12).reshape(3,4)
print('x:',x, x.shape)

y = np.arange(10,22).reshape(3,4)
print('y:',y, y.shape)

z = np.r_[x,y]
print('z:',z, z.shape)
'''
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


import os
import sys
import time
import random

'''
print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

import requests

# 郵遞區號
zipcode = "1000001"

# API 端點
api_endpoint = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"

# 進行查詢
response = requests.get(api_endpoint)

# 檢查回應狀態
if response.status_code == 200:
    # 解析回應內容
    data = response.json()

    # 驗證 API 回應狀態
    if data['status'] == 200:
        # 取出第一筆地址資訊
        address_info = data['results'][0]

        # 印出完整郵遞區域
        print(f"{address_info['address1']} {address_info['address2']} {address_info['address3']}")
    else:
        print("API 回應錯誤，訊息：", data['message'])
else:
    print("API 查詢失敗，狀態碼：", response.status_code)



print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


""" fail
import requests

# 郵遞區號
zipcode = "100-0001"

# API 端點
api_endpoint = "http://your_api_endpoint"

# 你的 API 金鑰
api_key = "your_api_key"

# 設定查詢參數
params = {
    'apikey': api_key,
    'zipcode': zipcode,
}

# 進行查詢
response = requests.get(api_endpoint, params=params)

# 檢查回應狀態
if response.status_code == 200:
    # 解析回應內容
    data = response.json()

    # 印出郵遞區域
    print(data['area'])
else:
    print("API 查詢失敗，狀態碼：", response.status_code)
"""


print('------------------------------------------------------------')	#60個

from PIL import Image

def blue_to_red(image_path):
    img = Image.open(image_path)
    r, g, b = img.split() # 分離三個通道
    img = Image.merge("RGB",(b,g,r))# 將藍色通道和通道互換
    img.show()

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
#blue_to_red(filename)

print('------------------------------------------------------------')	#60個

"""
from PIL import Image

def blue_to_red2(image_path):
    img = Image.open(image_path)
    pixels = img.load()

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]

            #若該點的藍色成分明顯超過紅色及綠色,我們便將之視為藍色
            if b > r and b > g:
                #將藍色分轉為紅色
                pixels[x, y] = (b, g, r)
    img.show()
    
    
    
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
blue_to_red2(filename)
"""    

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

import tkinter.messagebox as msg

response = msg.askyesno('糟糕了!!!', '還好嗎？')

if (response == True):
	print('還 OK')
else:
	print('有點麻煩')


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


import calendar
print(calendar.month(2022, 7))


import calendar
print(calendar.__file__)

import calendar as cal
print(cal.month(2022, 8))

from calendar import month, isleap
print(month(2022, 9))

isleap(2024)

import calendar
calendar.isleap(2022)

from calendar import isleap
isleap(2022)


print('------------------------------------------------------------')	#60個

import tkinter as tk

window=tk.Tk()
tk.Label(window, text='紅', bg='red', width=20).pack()
tk.Label(window, text='藍', bg='green', width=20).pack()
tk.Label(window, text='綠', bg='blue', width=20).pack()
window.mainloop()



print('------------------------------------------------------------')	#60個



window = tk.Tk()

topping = {0:'海苔', 1:'糖心蛋', 2:'豆芽菜', 3:'叉燒'}

check_value={}

for i in range(len(topping)):
	check_value[i] = tk.BooleanVar()
	tk.Checkbutton(window, variable=check_value[i],

text = topping[i]).pack(anchor=tk.W)

def buy():
	for i in check_value:
		if check_value[i].get() == True:
			print(topping[i])

tk.Button(window, text='點餐', command=buy).pack()

window.mainloop()



print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個

import tkinter as tk
window=tk.Tk()
topping = {0:'海苔', 1:'糖心蛋', 2:'豆芽菜', 3:'叉燒'}
check_value={}
for i in range(len(topping)):
	check_value[i] = tk.BooleanVar()
	tk.Checkbutton(window, variable=check_value[i], text = topping[i]).pack(anchor=tk.W)
window.mainloop()

"""
請問迴圈裡面 check_value [i] = tk.BooleanVar() 這一行，能否舉個例子，假設第 0 個按鈕被勾選，check_value 長怎樣；假設第 0、1 個按鈕被勾選，check_value 長怎樣 ... 依此類推
"""

print('------------------------------------------------------------')	#60個

window = tk.Tk()
radio_value = tk.IntVar()
radio_value.set(1)
lunch = {0:'A 套餐',1:'B 套餐',2:'C 套餐'}
tk.Radiobutton(window, text = lunch[0], variable = radio_value, value = 0).pack()
tk.Radiobutton(window, text = lunch[1], variable = radio_value, value = 1).pack()
tk.Radiobutton(window, text = lunch[2], variable = radio_value, value = 2).pack()
def buy():
	value = radio_value.get()
	print(lunch[value])

tk.Button(window, text='點餐', command=buy).pack()
window.mainloop()


print('------------------------------------------------------------')	#60個

window = tk.Tk()
string = tk.StringVar()
entry = tk.Entry(window, textvariable=string).pack()
label = tk.Label(window, textvariable=string).pack()
window.mainloop()


print('------------------------------------------------------------')	#60個

window = tk.Tk()

def fileopen():
	print('進行開啟檔案的處理')

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar)

menubar.add_cascade(label=' 檔案', menu=filemenu)

filemenu.add_command(label='開啟檔案', command=fileopen)

window.config(menu=menubar)

window.mainloop()


print('------------------------------------------------------------')	#60個

import tkinter.filedialog as fd

window = tk.Tk()

def open(): 
	filename = fd.askopenfilename()
	print('open file => ' + filename)

def exit(): 
	window.destroy()

def find():
	print('find ! ')

menubar = tk.Menu(window)

filemenu = tk.Menu(menubar)

menubar.add_cascade(label='File', menu=filemenu)

filemenu.add_command(label='open', command=open)

filemenu.add_separator()

filemenu.add_command(label='exit', command=exit)

editmenu = tk.Menu(menubar)

menubar.add_cascade(label='Edit', menu=editmenu)

editmenu.add_command(label='find', command=find)

window.config(menu=menubar)


print('------------------------------------------------------------')	#60個

"""
請參考以下程式，幫我利用 tkinter 生成選單視窗，需要的檔案結構如下：

檔案：
	開啟新檔
	開啟舊檔
	另存為
	結束
編輯：
	剪下
	複製
	貼上
說明：
	關於本程式

----------- 以下是參考的程式架構 --------
"""
""" TBD
import tkinter as tk
import tkinter.filedialog as fd
window = tk.Tk()
def open():
	filename = fd.askopenfilename()
print('open file => ' + filename)
def exit():
	window.destroy()
def find():
	print('find !')
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='open', command=open)
filemenu.add_separator()
filemenu.add_command(label='exit', command=exit)
editmenu = tk.Menu(menubar)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='find', command=find)
window.config(menu=menubar)
window.mainloop()

"""

'''

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

import requests

api_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"

response = requests.get(api_url)

response_dict = response.json()


print("------------------------------------------------------------")  # 60個

response_dict.keys()
response_dict["total"]


import requests, pprint

search_api_url = "https://collectionapi.metmuseum.org/public/collection/v1/search?"
query_parameter = "q=python&hasImages=true"
search_url = search_api_url + query_parameter
print(search_url)
search_response = requests.get(search_url)
pprint.pprint(search_response.json())


print("------------------------------------------------------------")  # 60個

get_object_url = (
    "https://collectionapi.metmuseum.org/public/collection/v1/objects/435864"
)

object_response = requests.get(get_object_url)

object_response.json()["objectURL"]

object_response.json()["title"]

object_response.json()["primaryImageSmall"]

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

import datetime as dt

x = dt.datetime(2020, 10, 22)
print(x)

x = dt.datetime(year=2020, month=10, day=22)
print(x)

y = dt.datetime(2020, 10, 22, 10, 30, 45)  # 設定日期與時間
print(y)

print("------------------------------------------------------------")  # 60個

# 3-4-2 timedelta 物件

x = dt.timedelta(hours=1, minutes=30)  # 1 小時又 30 分

print(x)
y = dt.timedelta(days=1, seconds=30)  # 1 天又 30 秒
print(y)

# 3-4-3 用 timedelta 來增減 datetime 或 timedelta 的時間

import datetime as dt

x = dt.datetime(2020, 10, 22, 10, 30, 45)  # 原始時間

y = dt.timedelta(days=1, hours=2, minutes=5)

print(x)

print(x + y)  # 用 timedelta 來增減 datetime 的時間

print(x - y)

print(x + y * 2)


print("------------------------------------------------------------")  # 60個

# 3-4-4 將 datetime 時間以格式化方式輸出

import datetime as dt

x = dt.datetime(2020, 10, 22, 10, 30, 45)

s1 = x.strftime("%Y/%m/%d %H-%M-%S")

print(s1)

s2 = x.strftime("%Y 年 %m 月 %d 日 %H : %M : %S")

print(s2)


print("------------------------------------------------------------")  # 60個

# 3-4-5 用字串來建立 datetime 物件

import datetime as dt

s = "2020/10/22 10-30-45"  # 含有特定格式之日期時間字串

x = dt.datetime.strptime(s, "%Y/%m/%d %H-%M-%S")


print(x)

print(type(x))


print("------------------------------------------------------------")  # 60個

# 4-1-1 lambda 函式簡介

power = lambda x: x**2

print(power(10))


add = lambda a, b: a + b

print(add(5, 3))

print("------------------------------------------------------------")  # 60個

# 4-1-2 在 lambda 內使用一行 if 條件判斷式

absolute = lambda x: x if x >= 0 else -x

func = lambda x: (x**2 - 40 * x + 350) if 10 <= x < 30 else 50

# 4-2-1 str.split()：分割字串為 list 元素

sentence = "This is a test sentence"

print(sentence.split(" "))

["This", "is", "a", "test", "sentence"]

# 4-2-2 用字串正規化分割字串為 list

import re

sentence = "This,is a,test.sentence"
time_data = "2020/05/20_12:30:45"

print(re.split("[,. ]", sentence))  # 用逗點、句點和空格來分割字串

print(re.split("[/_:]", time_data))

print("------------------------------------------------------------")  # 60個

a = [1, -2, 3, -4, 5]

new = []

for x in a:
    new.append(abs(x))  # 走訪 a 的元素, 取絕對值後放入 new

print(new)

str_list = ["This", "is", "a", "test", "sentence"]

print(list(map(str.upper, str_list)))

print("------------------------------------------------------------")  # 60個

# 4-2-4 用 flter() 篩選容器元素

str_list = ["This", "is", "a", "test", "sentence"]

print(list(filter(lambda x: len(x) >= 3, str_list)))

["This", "test", "sentence"]

# 4-2-5 再探 sorted()：自訂目標容器的排序方式

str_list = ["This", "is", "a", "test", "sentence"]

print(sorted(str_list, key=len, reverse=True))

nest_list = [[0, 9], [1, 8], [2, 7], [3, 6], [4, 5]]

print(sorted(nest_list))

print(sorted(nest_list, key=lambda x: x[1]))

print(sorted(nest_list, key=lambda x: x[1], reverse=True))

print("------------------------------------------------------------")  # 60個

# 4-3-1 介紹 list 生成式

a = [1, -2, 3, -4, 5]

print([abs(x) for x in a])

print("------------------------------------------------------------")  # 60個

a = [1, -2, 3, -4, 5]

print([x**2 for x in a])

str_list = ["This", "is", "a", "test", "sentence"]

print([s.upper() for s in str_list])

# 4-3-2 在 list 生成式使用 if 過濾元素

a = [1, -2, 3, -4, 5]

print([x for x in a if x > 0])

str_list = ["This", "is", "a", "test", "sentence"]

print([x for x in str_list if len(x) >= 3])

print("------------------------------------------------------------")  # 60個


# 4-3-3 在 list 生成式用 zip() 同時走訪多個容器

a = [1, -2, 3, -4, 5]
b = [9, 8, -7, -6, -5]

print([[x, y] for x, y in zip(a, b)])
print([x + y for x, y in zip(a, b)])

print("------------------------------------------------------------")  # 60個

a = [1, -2, 3, -4, 5]

b = [9, 8, -7, -6, -5]

print([x + y for x, y in zip(a, b) if x + y >= 0])


# 4-3-4 以巢狀 list 生成式產生複合 list

a = [1, 2, 3]

b = ["A", "B"]

print([[x, y] for x in a for y in b])

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
