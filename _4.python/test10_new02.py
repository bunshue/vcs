import os
import sys
import time
import random


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


#! /usr/bin/env python3
"""n2w: 數字轉英文模組, 包含一個num2words函式, 也能獨立執行
獨立執行用法: n2w num
              num: 0~999,999,999,999,999 之間的整數 (可用逗號分隔)
範例: n2w 10,003,103
輸入 10,003,103 後會輸出 ten million three thousand one hundred three
"""

import sys, string, argparse

#數字與英文的對應字典
_1to9dict = {'0': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
             '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
             '9': 'nine'}
_10to19dict = {'0': 'ten', '1': 'eleven', '2': 'twelve',
               '3': 'thirteen', '4': 'fourteen', '5': 'fifteen',
               '6': 'sixteen', '7': 'seventeen', '8': 'eighteen', 
               '9': 'nineteen'}
_20to90dict = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty',
               '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'}

#數字位數與數字英文單位的對應串列(list)
_magnitude_list = [(0, ''), (3, ' thousand '), (6, ' million '), 
                  (9, ' billion '), (12, ' trillion '),(15, '')]

#數字轉英文的函式
def num2words(num_string):
    """num2words(num_string): convert number to English words"""
    if num_string == '0':                                             
        return 'zero'
    num_string = num_string.replace(",", "")
    num_length = len(num_string) 
    max_digits = _magnitude_list[-1][0]
    if num_length > max_digits:
        return "Sorry, can't handle numbers with more than  " \
               "{0} digits".format(max_digits)
    num_string = '00' + num_string 
    word_string = ''

    #用迴圈從數字最右邊逐次取三個數字來處理，亦即從右邊三個一組進行轉換
    for mag, name in _magnitude_list:
        if mag >= num_length:
            return word_string
        else:
            hundreds, tens, ones = num_string[-mag-3], \
                 num_string[-mag-2], num_string[-mag-1]               
            if not (hundreds == tens == ones == '0'):                 
                word_string = _handle1to999(hundreds, tens, ones) + \
                                            name + word_string        
                 
#處理1~999的函式
def _handle1to999(hundreds, tens, ones):
    if hundreds == '0':
        return _handle1to99(tens, ones)
    else:
        return _1to9dict[hundreds] + ' hundred ' + _handle1to99(tens, ones)

#處理1~99的函式
def _handle1to99(tens, ones):
    if tens == '0': 
        return _1to9dict[ones]
    elif tens == '1':
        return _10to19dict[ones]
    else:
        return _20to90dict[tens] + ' ' + _1to9dict[ones]

num = '12345678'
#將第一個命令列參數值轉為英文，其餘命令列參數不處理
result = num2words(num)
print("{0} 的英文念法是: {1}".format(num, result))

print('------------------------------------------------------------')	#60個

import numpy as np
import matplotlib.pyplot as plt
rawdata = '''我
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
停止'''
words = rawdata.split('\n')
def poem():
    n = np.random.randint(2, 8) # 2-8句, 決定有幾句

    for i in range(n):
        m = np.random.randint(1, 6) # 決定每句的長度
        sentence = np.random.choice(words, m, replace=False)
        print(" ".join(sentence))
poem()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print("global: ", list(globals().keys()))
print("進入 local:", locals())
print("離開 local:", locals().keys())




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


import os
import sys
import time
import random



print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


import calendar

print(calendar.month(2023, 10))

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


word = 'maintenance'
word.count('n')

len('thunderbolt')


animal = ['cat','dog','duck']
len(animal)


max(100,10,50)
min(300,30,3000)




print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個



import zipfile

files = zipfile.ZipFile('C:/workplace/test.zip')

files.namelist()

files.extract('d/c.txt')

files.extractall()

files.close()



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

import requests
r = requests.get('https://tw.yahoo.com/')
print(r.text)


print('------------------------------------------------------------')	#60個

import pprint
r = requests.get('https://tw.yahoo.com/')
pprint.pprint(r.text)


print('------------------------------------------------------------')	#60個

import requests

base_url = 'https://zipcloud.ibsnet.co.jp/api/search'

query_parameter = '?zipcode='

zipcode = '1600021'

request_url = base_url + query_parameter + zipcode

request_url

requests.get(request_url).json()



#有這樣的 API 啊，網址是：https://zipcloud.ibsnet.co.jp/doc/api，請幫我寫出來


print('------------------------------------------------------------')	#60個

import requests, pprint

api_url = 'https://zh.wikipedia.org/w/api.php'

api_params = {'format':'json', 'action':'query', 'titles':柔道', 'prop':'revisions', 'rvprop':'content'}

wiki_data = requests.get(api_url, params=api_params).json()

pprint.pprint(wiki_data)



#pip install wikipedia


import wikipedia
wikipedia.set_lang ('zh')
wikipedia.summary('柔道')



#python wiki_sample.py




#python try_sys.py 想查詢的關鍵字




#python wiki_sample_final.py 柔道





print('------------------------------------------------------------')	#60個

from bs4 import BeautifulSoup
soup = BeautifulSoup('<html> Lollipop </html>', 'html.parser')

print('------------------------------------------------------------')	#60個

import requests

from bs4 import BeautifulSoup

html_data = requests.get('http://tw.yahoo.com')

soup = BeautifulSoup(html_data.text,"html.parser")

soup.title


print('------------------------------------------------------------')	#60個

import requests

from bs4 import BeautifulSoup

game_ranking_html = requests.get('https://www.kamatari.org/blog/2021/best-games-of-2021/')

soup = BeautifulSoup(game_ranking_html.text, "html.parser")

for game in soup.findAll('h2'):
	print(game.text)


print('------------------------------------------------------------')	#60個

import requests
from bs4 import BeautifulSoup
game_ranking_html = requests.get ('https://www.kamatari.org/blog/2021/best-games-of-2021/')
soup = BeautifulSoup (game_ranking_html.text, "html.parser" )
for game in soup.findAll ('h2'):
	print (game.text)


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

print('------------------------------------------------------------')	#60個

'''
x0 = np.arange(-5, 5, 1)
y0 = np.arange(-5, 5, 1)
x, y = np.meshgrid(x0, y0)
z = np.c_[x.ravel(), y.ravel()]


print(len(x))
print(x.shape)
print(x)
print(len(y))
print(y.shape)
print(y)
print(len(z))
print(z.shape)
print(z)

print('x.ravel() = ', x.ravel())
print('y.ravel() = ', y.ravel())

plt.scatter(z[:, 0], z[:, 1], s = 100)
plt.grid()
plt.show()



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
print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



X, Y = np.meshgrid(np.linspace(-6,3,30), np.linspace(-8,5,30))

#ravel 拉平法

X = X.ravel()

Y = Y.ravel()

plt.scatter(X, Y)

plt.show()


print('------------------------------------------------------------')	#60個


#zip 高級組合法

xx = [1,2,3,4]

yy = [5,6,7,8]

list(zip(xx,yy))

Z = list(zip(X,Y))
print(Z)

#plt.scatter(X, Y, s=50, c=Z)
plt.show()

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個





