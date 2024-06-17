
"""


"""

import os
import sys
import time
import random
import numpy as np
import pandas as pd

print("------------------------------------------------------------")  # 60個
'''
#各種建立資料的寫法
print("range")

N1 = 3
N2 = 9
STEP = 2

a = range(N1)
print(a)
for _ in a:
    print(_, end=" ")
print()

a = range(N1, N2)
print(a)
for _ in a:
    print(_, end=" ")
print()

a = range(N1, N2, STEP)
print(a)
for _ in a:
    print(_, end=" ")
print()

"""
    range(101)可以產生一個0到100的整數序列。
    range(1, 100)可以產生一個1到99的整數序列。
    range(1, 100, 2)可以產生一個1到99的奇數序列，其中的2是步長，即數值序列的增量。
"""


print("使用np.linspace, 和range一樣")

a = np.arange(N1)
print(a)
for _ in a:
    print(_, end=" ")
print()

a = np.arange(N1, N2)
print(a)
for _ in a:
    print(_, end=" ")
print()

a = np.arange(N1, N2, STEP)
print(a)
for _ in a:
    print(_, end=" ")
print()


# 二維

W = 640
H = 480
w = 160
h = 160

for y in range(0, H, h):
    for x in range(0, W, w):
        print(x, y, end="    ")
print()

print("------------------------------------------------------------")  # 60個

print("使用np.linspace")

N1 = 3
N2 = 9
N = 2

x = np.linspace(N1, N2, N)  # 從N1到N2, 分成N個, 包含頭尾
print(x)

x = np.linspace(N1, N2)  # 若沒有給定N值, 則分成 50 個, 包含頭尾
print(x)

# np.linspace 若只給a b 則代表分成50點
x = np.linspace(0, 2 * np.pi)
print(x.shape)


import numpy as np

# 含頭尾共N個元素的陣列
N = 11
x = np.linspace(0, 10, 11)  # 建立含11個元素的陣列

print("包含頭尾之linespace :", x)


print("------------------------------------------------------------")  # 60個

n = list(range(100))
r = list(range(25))
n = list(range(10)) * 10

print("------------------------------------------------------------")  # 60個

for _ in range(10):
    a = random.randint(3, 8)  # 唯一包含頭尾
    print(a)

print("------------------------------------------------------------")  # 60個

W = 5
H = 5
nextCells = {}  # 字典
for x in range(H):
    for y in range(W):
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = "Y"
        else:
            nextCells[(x, y)] = "N"
print(type(nextCells))
print(nextCells)

print("------------------------------------------------------------")  # 60個


print("20位 靠右對齊")

string = "abcdefg"
print(string.rjust(20))

number = 1234567
print(repr(int(number)).rjust(20))

print("4位 不對齊")
for _ in range(20):
    a = random.randint(0, 200)
    print(repr(int(a)), end=" ")
print()

print("4位 靠左對齊")
for _ in range(20):
    a = random.randint(0, 200)
    print(repr(int(a)).ljust(4), end="")
print()

print("------------------------------------------------------------")  # 60個

year = 2023
month = 3
day = 11
total = 123
print(f"{year}年{month}月{day}日是{year}年的第{total}天")

print("------------------------------------------------------------")  # 60個

import os

#用預設程式開啟檔案
#os.system('cccc.mp3')

#用預設程式wav檔案
#os.startfile('harumi99.wav')

#用系統預設程式開啟檔案
#os.system('cv03.png')

print("------------------------------------------------------------")  # 60個

import random
import time

N = 10
lst = list(range(N))
print(lst)
random.shuffle(lst)
print(lst)

lst.sort()
print(lst)

print("------------------------------------------------------------")  # 60個

import random

animals1 = ['鼠', '牛', '虎']
animals2 = ['兔', '龍', '蛇']
animals3 = ['馬', '羊', '猴']
animals4 = ['雞', '狗', '豬']

print('本次選出人員')
print(random.choice(animals1) + " " + random.choice(animals2) + " " + random.choice(animals3) + " "+ random.choice(animals4))

print("------------------------------------------------------------")  # 60個

import random

passlen = 3
s = "ABCDEFG"
p =  "".join(random.sample(s,passlen ))
print (p)

print("------------------------------------------------------------")  # 60個

number = 1234.5678
print("Number :", format(number, ".2f"))

print("------------------------------------------------------------")  # 60個

"""
import sys, time

PAUSE = 0.02

print('無限迴圈進行中..... 按 Ctrl+C離開 ')

try:
    while True:
        print("A", end = " ")
        time.sleep(PAUSE)  # Pause for PAUSE number of seconds.

    print('XXXXXXXXXXXXXXXXXXXXXXXXXX')
   
except KeyboardInterrupt:
    print('你按了 Ctrl+C 離開')
    sys.exit()  # When Ctrl-C is pressed, end the program.
"""

print("------------------------------------------------------------")  # 60個
"""
import time
for i in range(5, 0, -1):
    print("\r", "倒计时{}秒！".format(i), end="", flush=True)
    time.sleep(1)
"""

print("------------------------------------------------------------")  # 60個
"""
print('目前的全螢幕截圖')

from PIL import ImageGrab

image = ImageGrab.grab()
filename = 'Image_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.jpg'
image.save(filename)

image = ImageGrab.grab().convert('L')  
data = image.load()
print(type(data))
#print(data.size)
if data[260, 300] > 150:
    #isCollision_day(data)
    print("aaaaaaa")
else:
    #isCollision_night(data)
    print("bbbbbbb")
"""
print("------------------------------------------------------------")  # 60個


import datetime
now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print("現在時間 :", now)

print("------------------------------------------------------------")  # 60個

#字串轉數值,10進位整數
print(int('13',10))
#字串轉數值,2進位整數
print(int('1001',2))
#字串轉數值,浮點數
print(float('3.14'))

#ord()是將字元轉成ASCII碼
#chr()是將ASCII碼轉成字元
#ord()和chr()互為反函數
print(chr(ord('A')))
print(ord(chr(65)))


#i的初始值為A字元的ASCII碼(65)，終止值小於Z字元的ASCII碼(90)+1，遞增值為1
for i in range(ord("A"),ord("Z")+1,1):
    print(chr(i), end = '')
  
#bin()回傳參數的二進位值
##輸出結果數字前面0b代表二進位(binary)
print(bin(10))
#oct()回傳參數的八進位值
##輸出結果數字前面0o代表八進位(octal)
print(oct(10))
#hex()回傳參數的十六進位值
##輸出結果數字前面0x代表十六進位(hexdecimal)
print(hex(10))


##預設是取到整數位，根據小數第一位(如果是5要看個位數，奇進偶捨)判別
print("==Test2==")
print(round(3.5))
print(round(3.6))
print(round(4.5))
print(round(4.6))
##指定取到小數第一位，根據小數第二位(如果是5要看小數第一位，奇進偶捨)判別
print("==Test3==")
print(round(1.35,1))
print(round(1.36,1))
print(round(1.45,1))
print(round(1.46,1))



#ord()回傳參數字元對應的的編碼位置
print("==Test1==")
print(ord("H"))
print(ord("你"))
print(ord("好"))
#chr()回傳參數編碼位置對應的字元
print("==Test2==")
print(chr(72))
print(chr(20320))
print(chr(22909))
##輸出'A'之後的10個英文字母
print("==Test3==")
for i in range(65,75):
    print(chr(i),end='')
print()
##輸出'你'之後的10個中文字
for i in range(20320,20330):
    print(chr(i),end='')
print()
#str()回傳參數為字串
print("==Test4==")
print(str(123)+"456")
#ascii()回傳參數的字串表達形式
##如果字串含有非ASCII字元，所有非ASCII字元會以Unicode跳脫字元的方式呈現
print(ascii("Ab123"))
print(ascii("hello你好".encode('utf-8')))

'''

print('字串的對齊 justify')

print("01234567890123456789")
print("==Test1==")
string1=str(153)
print(string1)
#center()指定寬度置中對齊
print(string1.center(20))
#ljust()指定寬度靠左對齊
print(string1.ljust(20))
#rjust()指定寬度靠右對齊
print(string1.rjust(20))
print("==Test2==")
#center()指定寬度置中對齊，指定補齊填補字元
print(string1.center(20,"-"))
#ljust()指定寬度靠左對齊，指定補齊填補字元
print(string1.ljust(20,"-"))
#rjust()指定寬度靠右對齊，指定補齊填補字元
print(string1.rjust(20,"-"))
print("==Test3==")
#zfill()指定寬度靠右對齊，以'0'補齊
print(string1.zfill(20))
  

sys.exit()


import math
help(math.sqrt)
help(math.pow)

print('help 的用法')
import random
print(dir(random))
help(random.randint)
help(random.choice)

print("------------------------------------------------------------")  # 60個

#chap6-02a
import pandas as pd
#建立一個pandas dataframe
df = pd.DataFrame({
   "姓名": ["約翰", "瑪莉", "麥可", "大衛"],
   "年齡": [16, 17, 16, 18],
   "性別": ["男", "女", "男", "男"],
  })
print("==Test1==")
print(df)
#取出dataframe其中一欄就是series
print(df['姓名'])
print(df['年齡'])
print("==Test2==")
#自行建立一個pandas series
score = pd.Series([78, 67, 90, 81], name="成績")
print(score)
#將series加入dataframe導致增加一欄(column)
print("==Test3==")
df['成績'] = score
print(df)



#chap6-02b
from pandas import DataFrame as pdDF
from pandas import Series as pdSer
#建立一個pandas dataframe
df = pdDF({
   "姓名": ["約翰", "瑪莉", "麥可", "大衛"],
   "年齡": [16, 17, 16, 18],
   "性別": ["男", "女", "男", "男"],
  })
print("==Test1==")
print(df)
#取出dataframe其中一欄就是series
print(df['姓名'])
print(df['年齡'])
print("==Test2==")
#自行建立一個pandas series
score = pdSer([78, 67, 90, 81], name="成績")
print(score)
#將series加入dataframe導致增加一欄(column)
print("==Test3==")
df['成績'] = score
print(df)



#chap6-02c
import pandas as pd
#建立一個pandas dataframe
df = pd.DataFrame({
   "姓名": ["約翰", "瑪莉", "麥可", "大衛"],
   "年齡": [16, 17, 16, 18],
   "性別": ["男", "女", "男", "男"],
  })
print("==Test1==")
print(df)
print(df.shape)
#列出所有欄索引標籤(欄位名稱)
for col in range(df.shape[1]):
  print(df.columns.values[col],' ',end='')
print()
print("==Test2==")
#列出各列的列索引標籤、表格內容
for row in range(df.shape[0]):
  print(df.index.values[row],' ',end='')
  for col in range(df.shape[1]):
    print(df.iloc[row][col],' ',end='')
  print()
print("==Test3==")
#比較loc(彈性較大)和iloc顯示表格內容
#loc使用行索引標籤(column index label)和列索引標籤(row index label)
print(df.loc[1]["姓名"])
#iloc使用行索引(column index)和列索引(row index)
print(df.iloc[1][0])





#chap6-02d
import pandas as pd
#建立一個pandas dataframe
df = pd.DataFrame({
   "姓名": ["約翰", "瑪莉", "麥可", "大衛"],
   "年齡": [16, 17, 16, 18],
   "性別": ["男", "女", "男", "男"],
  })
print("==Test1==")
#將dataframe轉成清單list
alldata=df.to_dict('split')
#會有3個list構成: columns, index, data
print(alldata)
print(alldata["columns"])  
print(alldata["index"])
print(alldata["data"])  
print("==Test2==")
#列出所有欄索引標籤(欄位名稱)
for col in range(len(alldata["columns"])):
  print(alldata["columns"][col],' ',end='')
print()
print("==Test3==")
#列出各列的列索引標籤、欄位內容
for row in range(len(alldata["index"])):
  print(alldata["index"][row],' ',end='')
  for col in range(len(alldata["columns"])):
    print(alldata["data"][row][col],' ',end='')
  print()
  
  

#chap6-02e
from pandas import DataFrame as pdDF
#建立一個pandas dataframe
df = pdDF({
   "姓名": ["約翰", "瑪莉", "麥可", "大衛"],
   "年齡": [16, 17, 16, 18],
   "性別": ["男", "女", "男", "男"],
   "成績": [78, 67, 90, 81]
  })
print(df)
#指定顯示dataframe中是數值型態的欄位的最大max()或最小min()數據
print("最小年齡:", df['年齡'].min())
print("最高分:", df['成績'].max())
#describe()可以顯示dataframe中是數值型態的欄位的統計資料
df.describe()


#chap6-02f
from pandas import DataFrame as pdDF
#建立一個pandas dataframe
df = pdDF({
   "姓名": ["約翰", "瑪莉", "麥可", "大衛"],
   "年齡": [16, 17, 16, 18],
   "性別": ["男", "女", "男", "男"],
   "成績": [78, 67, 90, 81]
  })
print(df)
newrow={"姓名":"珍妮","年齡":17,"性別":"女","成績":87}
df=df.append(newrow, ignore_index = True)
print(df)



#chap6-02g
from pandas import DataFrame as pdDF
#建立一個pandas dataframe
df = pdDF({
   "姓名": ["約翰", "瑪莉", "麥可", "大衛"],
   "年齡": [16, 17, 16, 18],
   "性別": ["男", "女", "男", "男"],
   "成績": [78, 67, 90, 81]
  })
print("==Test1==")
print(df)
#刪除指定的欄
df.drop(['年齡'],inplace=True,axis=1)
print(df)
#刪除指定的列
indexNames=df[df['成績']<80].index
df.drop(indexNames,inplace=True)
print(df.shape)
print("==Test2==")
#列出所有欄索引(欄位名稱)
for col in range(df.shape[1]):
  print(df.columns.values[col],' ',end='')
print()
print("==Test3==")
#使用iloc列出各列的列索引、欄位內容
for row in range(df.shape[0]):
  print(df.index.values[row],' ',end='')
  for col in range(df.shape[1]):
    print(df.iloc[row][col],' ',end='')
  print()
print("==Test4==")
#列出所有欄索引(欄位名稱)
for col in range(df.shape[1]):
  print(df.columns.values[col],' ',end='')
print()
print("==Test5==")
#使用loc列出各列的列索引、欄位內容
for row in range(df.shape[0]):
  print(df.index.values[row],' ',end='')
  for col in range(df.shape[1]):
    print(df.loc[df.index.values[row]][df.columns.values[col]],' ',end='')
  print()  
  
  
#chap6-02h
import pandas as pd
#建立一個pandas dataframe
df = pd.DataFrame({
   "姓名": ["約翰", "瑪莉", "麥可", "大衛"],
   "年齡": [16, 17, 16, 18],
   "性別": ["男", "女", "男", "男"],
   "成績": [78, 67, 90, 81]
  })
print("==Test1==")
print(df)
print("==Test2==")
#建立樞紐分析表
#aggfunc: mean是求平均, sum是求總和
table=pd.pivot_table(data=df,index=['性別'],columns=['年齡'],values=['成績'],aggfunc={'成績':'mean'})
print(table)
#查看欄索引標籤
#發現是元組tuple型態
print(table.columns.values)
#查看列索引標籤
print(table.index.values)
print("==Test3==")
#建立樞紐分析表
#aggfunc: mean是求平均, sum是求總和
table=pd.pivot_table(data=df,index=['性別'],values=['成績'],aggfunc={'成績':'sum'})
print(table)
#查看欄索引標籤
print(table.columns.values)
#查看列索引標籤
print(table.index.values)

'''



print("------------------------------------------------------------")  # 60個



'''




#chap7-01b
import requests
url ='http://jigsaw.w3.org/HTTP/connection.html'
res = requests.get(url)
#print(res.text)

#在<HEAD></HEAD>區塊中取得包圍網頁標題的指定字串<TITLE></TITLE>所在的位置
#stripe()去除字串頭尾的'\n'(換行)、'\t'(跳格)、' '(空白)
datapos1=res.text.find("<TITLE>")
datapos2=res.text.find("</TITLE>")
data=res.text[datapos1+7:datapos2]
data=data.strip()
print(data)
#在<BODY></BODY>區塊中取得包圍內容標題的指定字串<H1></H1>所在的位置
datapos1=res.text.find("<H1>")
datapos2=res.text.find("</H1>")
data=res.text[datapos1+4:datapos2]
#將設定斜體的HTML語法<I></I>移除
data=data.replace("<I>","")
data=data.replace("</I>","")
data=data.strip()
print(data)



print("------------------------------------------------------------")  # 60個


import requests
from bs4 import BeautifulSoup
url ='http://jigsaw.w3.org/HTTP/connection.html'
res = requests.get(url)
#指定html.parser作為解析器
soup = BeautifulSoup(res.text, 'html.parser') 
#把排版後的html印出來，因為未排版前有很多網頁語法缺乏換行符號，不易閱讀
#必須借助於Beautiful Shop套件
print(soup.prettify()) 
#find_all()回傳的格式是串列list
#而且contens的內容也是串列list
a_tags = soup.find_all('title')
for a_tag in a_tags:
  for b in a_tag.contents:
    print(str(b).strip())
a_tags = soup.find_all('h1')
for a_tag in a_tags:
  cc=""
  for b in a_tag.contents:        
    b=str(b).replace('<i>','').replace('</i>','').replace('\n','').replace('\r','')
    cc=cc+b
  print(cc.strip())
'''

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
import requests
url ='https://www.dcard.tw/f/stock/p/237123381'
res = requests.get(url)
print(res.text)

print("------------------------------------------------------------")  # 60個

#chap7-02b
import requests
from bs4 import BeautifulSoup
url ='https://www.dcard.tw/f/stock/p/237123381'
res = requests.get(url)
#指定html.parser作為解析器
soup = BeautifulSoup(res.text, 'html.parser') 
#把排版後的html印出來，因為未排版前有很多網頁語法缺乏換行符號，不易閱讀
#必須借助於Beautiful Shop套件
print(soup.prettify())

print("------------------------------------------------------------")  # 60個

#chap7-02c
import requests
from bs4 import BeautifulSoup
url = 'https://www.dcard.tw/f/stock/p/237123381'


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-TW,zh;q=0.9",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36" #使用者代理
    }

#response = requests.get(url="https://example.com", headers=headers)
res = requests.get(url, headers=headers)
#指定html.parser作為解析器
soup = BeautifulSoup(res.text, 'html.parser') 
#把排版後的html印出來
print(soup.prettify()) 
a_tags = soup.find_all('h1')
print(">>>>>文章標題")
print(a_tags[0].contents[0])
print("\n")

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




