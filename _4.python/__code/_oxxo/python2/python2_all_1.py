import os
import sys
import time
import random


print("------------------------------------------------------------")  # 60個
'''
# 猜數字：幾 A 幾 B

import random

""" 
arr = []
for i in range(9):
    arr.append(i+1)

answer = []
for i in range(4):
    arrLength = int(len(arr)) - 1
    answer.append(arr.pop(random.randint(0, arrLength)))


 """
answer = random.sample(range(1,10), k=4)  # 使用 random.sample
print(answer)

n = 0

while True:
    user = str(input('請輸入四個數字：'))
    a = 0
    b = 0
    n += 1
    result = [0, 0, 0, 0]
    for i in range(4):
        result[i] = int(user[i])
    for i in range(4):
        if (result[i] in answer):
            if(answer[i] == result[i]):
                a += 1
            else:
                b += 1

    print('第 ' + str(n) + ' 次：' + user + \
          ' ( ' + str(a) + ' A ' + str(b) + ' B )')
    if a == 4:
        print('猜中囉')
        break

print("------------------------------------------------------------")  # 60個

def inn():
    a = input('輸入文字並轉換為 ASCII：')
    print('{} 的 ASCII：{}'.format(a, ord(a)))
    inn()

inn()
'''

print("------------------------------------------------------------")  # 60個

# 九九乘法表

for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={} '.format(i, j, i*j), end='')
    print('')

print("------------------------------------------------------------")  # 60個

import requests
import json

url = "https://www.oxxostudio.tw/json/pageList.json"
r = requests.get(url)
j = json.loads(r.text)  # 轉換成 json 格式
print(j)

print("------------------------------------------------------------")  # 60個

import requests
import json

url = "https://www.oxxostudio.tw/json/pageList.json"
r = requests.get(url)
j = json.loads(r.text)  # 轉成 json 格式
print(j[0])

# 轉換成文字寫入，因為中文會變成編碼，所以後方要加上 ensure_ascii=False
jj = json.dumps(j[0], ensure_ascii=False)
print(jj)

with open('tmp_a06.txt', 'a+') as f:
    f.write(jj)

print("------------------------------------------------------------")  # 60個

import random

""" 
arr = []
for i in range(1, 50):
    arr.append(i)

lto = []
for i in range(6):
    arrLength = int(len(arr)) - 1
    lto.append(arr.pop(random.randint(0, arrLength))) 
"""

# 使用 random.sample 一行搞定
lto = random.sample(range(1,50), k = 6)
lto.sort()
print(lto)

print("------------------------------------------------------------")  # 60個

"""
while(True):
    a = input('請輸入簡單的數學式：')
    answer = '你輸入的不是數字呦～'
    if('+' in a):
        p = a.split('+')
        if(p[0].isdigit() and p[1].isdigit()):
            answer = int(p[0]) + int(p[1])
    elif('-' in a):
        p = a.split('-')
        if(p[0].isdigit() and p[1].isdigit()):
            answer = int(p[0]) - int(p[1])
    elif('/' in a):
        p = a.split('/')
        if(p[0].isdigit() and p[1].isdigit()):
            answer = int(p[0]) / int(p[1])
    elif('*' in a):
        p = a.split('*')
        if(p[0].isdigit() and p[1].isdigit()):
            answer = int(p[0]) * int(p[1])
    print(answer)
"""

print("------------------------------------------------------------")  # 60個

import time

#a = input('請輸入倒數的秒數：')
a = "3"

if(a.isdigit()):
    a = int(a)
    while(a > 0):
        print(a)
        a = a - 1
        time.sleep(1)
    print('時間到！')
else:
  print('你輸入的不是數字呦～')

print("------------------------------------------------------------")  # 60個

"""
import time
import math
import threading

a = input('按下任意鍵開始')
b = True
t = 0


def loop_a():
    global t  # 設定全域變數
    global b
    while (b == True):
        t = t + 0.01
        time.sleep(0.01)


def loop_b():
    global b
    global t
    b = input('按下任意鍵停止')
    t = round(t * 100)/100
    print(t)


# 跑多線程
thread1 = threading.Thread(target=loop_a)
thread1.start()
thread2 = threading.Thread(target=loop_b)
thread2.start()

"""
print("------------------------------------------------------------")  # 60個

# 參考：http://violin-tao.blogspot.com/2017/05/python3_26.html

import multiprocessing as p
import time
loc = p.Lock()  # 定義 Lock


def a1():
    global loc
    loc.acquire()  # 鎖住 Lock
    a = 0
    while (a <= 20):
        a = a + 1
        print('a' + str(a))
        time.sleep(0.01)
        if(a == 10):
            loc.release()  # 釋放 Lock


def a2():
    global loc
    a = 0
    while (a <= 20):
        a = a + 1
        print('b' + str(a))
        time.sleep(0.01)
        if(a == 5):
            loc.acquire()  # 鎖住 Lock


p1 = p.Process(target=a1)
p2 = p.Process(target=a2)
p1.start()
p2.start()

print("------------------------------------------------------------")  # 60個

from datetime import datetime

#a = input('請輸入你的出生年月日 ( yyyy/mm/dd )：')
a = "2006/03/11"
now = datetime.now()
ad = datetime.strptime(a, '%Y/%m/%d')
y = now.year - ad.year
m = now.month - ad.month
d = now.day - ad.day

print(f'你的生日是：{y} 歲 {m} 個月又 {d} 天')  # 使用 python3 語法

print("------------------------------------------------------------")  # 60個

import asyncio
import time
c = True


async def a():
    global c
    a = 0
    while (c == True):
        a = a + 1
        print(f'a{a}')
        await asyncio.sleep(0.1)


async def b():
    global c
    a = 0
    while (a <= 5):
        a = a + 1
        print(f'b{a}')
        await asyncio.sleep(0.1)
    c = False
    return a


loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(a()),
    asyncio.ensure_future(b()),
]
c = loop.run_until_complete(asyncio.gather(*tasks))
print(f'end:{c[1]}')

print("------------------------------------------------------------")  # 60個

class human():
    def __init__(self, name=None):
        if name:
            self.name = name
        else:
            self.name = '???'

    def talk(self, msg):
        print(f'{self.name}: {msg}')

class Taiwan(human):
    def __init__(self, name, age=None):
        super().__init__(name)   # 繼承 human 的 name
        if age:
            self.age = age
        else:
            self.age = '???'


a = human('oxxo')
b = human('tom')
c = human()     # 沒有輸入就採用預設值
print(a.name)   # oxxo
print(b.name)   # tom

a.talk('hello')      # oxxo: hello
b.talk('ya')         # tom: ya
c.talk('okok!!!!!')  # ???: okok!!!!!

c = Taiwan('qq', 18) 
print(c.name, c.age) # qq 18

print("------------------------------------------------------------")  # 60個

import csv
import requests
import json

url = "https://www.oxxostudio.tw/json/pageList.json"
r = requests.get(url)
j = json.loads(r.text)  # 轉成 json 格式

# 轉換成文字寫入，因為中文會變成編碼，所以後方要加上 ensure_ascii=False
# 此處不使用，因為發現出來變成純文字格式，非 json
jj = json.dumps(j[0], ensure_ascii=False)

with open('tmp_a15.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for i in j:
        writer.writerow([i['tag'], i['title'], i['site'], i['date']])
        # writer.writerows([[0, 1, 3], [1, 2, 3], [2, 3, 4]])
    print('寫入完成！')



print("------------------------------------------------------------")  # 60個

# 參考 https://zh.wikipedia.org/wiki/%E9%80%97%E5%8F%B7%E5%88%86%E9%9A%94%E5%80%BC
import csv
from collections import OrderedDict

with open('data/a16.csv') as csvFile:
    # r = csv.reader(csvFile)      # 無法和 DictReader 同時使用，不知道為什麼
    # for i in r:
    #   print(i)

    rows = csv.DictReader(csvFile)  # 轉成 OrderedDict
    o = []
    for row in rows:
        print(row)
        d = dict(OrderedDict(row))  # 轉成 Dict
        print(d)
        o.append(d)
        

    for i in o:
        print(f'姓名：{i["name"]}，年紀：{i["age"]} 歲。')

print("------------------------------------------------------------")  # 60個

""" fail
from lxml import html
import requests

url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
page = requests.get(url)
tree = html.fromstring(page.text)

print('美金：' + str(tree.xpath('//html/body/div[1]/main/div[3]/table/tbody/tr[1]/td[3]/text()')[0]))
print('日圓：' + str(tree.xpath('//html/body/div[1]/main/div[3]/table/tbody/tr[8]/td[3]/text()')[0]))
"""

print("------------------------------------------------------------")  # 60個

from lxml import html
import requests
import json

# https://mis.twse.com.tw/stock/fibest.jsp?stock=0050
url = 'https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_0050.tw'
page = requests.get(url)
j = json.loads(page.text)

print(j)


print("------------------------------------------------------------")  # 60個

import requests

rep = requests.get('https://www.oxxostudio.tw/img/articles/201803/css-animation-01.gif')

with open("tmp_test.gif", 'wb') as f:
  f.write(rep.content)

print("------------------------------------------------------------")  # 60個

''' 跳過 webdriver

from selenium import webdriver
import time
import requests

# pip3 install selenium
# 下載 chromedriver ( 注意要對應自己 chrome 版本 )
# https://chromedriver.chromium.org/downloads

driver = webdriver.Chrome(
    '/Users/oxxo/Documents/oxxo/practice/python/chromedriver')  # 設定 chromedriver 路徑
driver.get('http://oxxo.studio')  # 前往這個網址
print(driver.title)
time.sleep(1)
driver.execute_script(
    'window.scrollTo(0, document.body.scrollHeight);')  # 捲動到最下方
time.sleep(1)
for i in range(1, 7):
    img = driver.find_element_by_xpath(
        '//*[@id="content-grid"]/ul/li[' + str(i) + ']/a[1]/div/img')
    rep = requests.get(img.get_attribute('src'))
    with open('demo/test'+str(i)+'.jpg', 'wb') as f:
        f.write(rep.content)
driver.close()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
import time
import re

options = webdriver.ChromeOptions()
options.add_argument('headless')  # 不會開啟瀏覽器

driver = webdriver.Chrome(
    '/Users/oxxo/Documents/oxxo/practice/python/chromedriver', chrome_options=options)  # 設定 chromedriver 路徑
driver.get('https://www.dinbendon.net/do/login')  # 前往這個網址

# 輸入使用者 id
user = driver.find_element_by_xpath(
    '//*[@id="signInPanel_signInForm"]/table/tbody/tr[1]/td[2]/input')
user.send_keys('XXX')

# 輸入使用者密碼
pwd = driver.find_element_by_xpath(
    '//*[@id="signInPanel_signInForm"]/table/tbody/tr[2]/td[2]/input')
pwd.send_keys('XXX')

# 取得驗證碼訊息
checkquestion = driver.find_element_by_xpath(
    '//*[@id="signInPanel_signInForm"]/table/tbody/tr[3]/td[1]')
check = driver.find_element_by_xpath(
    '//*[@id="signInPanel_signInForm"]/table/tbody/tr[3]/td[2]/input')

# 計算驗證碼
checktext = checkquestion.text
print(checktext)
a = int(re.findall(r'\d+',checktext)[0])   # 使用正則表達式提取數字
b = int(re.findall(r'\d+',checktext)[1])
result = a+b
print(result)
check.send_keys(result)  # 輸入驗證碼

# 點擊按鈕
btn = driver.find_element_by_xpath(
    ' //*[@id="signInPanel_signInForm"]/table/tbody/tr[5]/td[2]/input[1]')
btn.click()

time.sleep(1)

# 抓取第一筆便當名稱，加入例外處理
try:
    menu = driver.find_element_by_xpath(
        '//*[@id="inProgressBox_inProgressOrders_0"]/td[2]/div[1]/a/span[2]')

    print(menu.text)
except:
    print('找不到便當名稱')

driver.close()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
import time
import requests

driver = webdriver.Chrome(
    '/Users/oxxo/Documents/oxxo/practice/python/chromedriver')  # 設定 chromedriver 路徑
driver.get('https://www.google.com.tw/imghp?hl=zh-TW&tab=wi&ogbl')  # 前往這個網址

search = driver.find_element_by_xpath(
    '//*[@id="sbtc"]/div/div[2]/input')
search.send_keys('林志玲')


btn = driver.find_element_by_xpath(
    '//*[@id="sbtc"]/button')
btn.click()

for i in range(1, 6):

    time.sleep(0.5)
    div = driver.find_element_by_xpath(
        '/html/body/div[6]/div[3]/div[3]/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div['+str(i)+']')
    div.click()

    time.sleep(0.5)
    img = driver.find_element_by_xpath(
        '//*[@id="irc-ss"]/div['+str(i)+']/div[1]/div[4]/div[1]/a/div/img')
    src = img.get_attribute('src')
    print(src)
    if(str(src) != 'None'):
      if('.jpg' in src):
          filename = src.split('/')[-1]
          rep = requests.get(src)
          with open('demo/'+str(filename), 'wb') as f:
              f.write(rep.content)
              closeBtn = driver.find_element_by_xpath('//*[@id="irc_ccbc"]')
              closeBtn.click()
      else:
          closeBtn = driver.find_element_by_xpath('//*[@id="irc_ccbc"]')
          closeBtn.click()
'''
print("------------------------------------------------------------")  # 60個

import re

# 取出一段文字中的阿拉伯數字
a = '123 + 456'
b = re.findall(r'\d+', a.replace(' ', ''))
print(b)

# 取出一段文字中的「非」阿拉伯數字
c = 'hello 123 !!!'
d = re.findall(r'\D+', c.replace(' ', ''))
print(d)

# 取出每個非空白字元
msg1 = 'hello world!!'
msg1r = re.findall(r'\S', msg1)
print(msg1r)


# 替換指定區間文字
msg2 = 'hello {name}, {age}'
msg2r = re.findall(r'\{.+?\}', msg2)
print(msg2r)
text = {
    'name': 'oxxo',
    'age': '18'
}
for i in range(0, len(msg2r)):
    o = re.sub(r'\{|\}', '', msg2r[i])
    msg2 = re.sub(msg2r[i], text[o], msg2)

print(msg2)

aa = 'abc'
aa = aa + 'def'
print(aa)

print("------------------------------------------------------------")  # 60個



#檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python2\numpy\np00.py

# encoding:UTF-8
# pip3 install numpy

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a[0], b[1])

a = np.append(a, b)
print(a)

d = a[1]
print(d)

a2 = np.delete(a, 1)
print(a2)
a3 = np.insert(a, 1, d)
print(a3)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python2\numpy\np01.py

import numpy as np

# 一維
a = np.array([1, 2, 3])
print(a)

# 二維
b = np.array([[1, 2, 3], [5, 6, 7]])
print(b)

# 二維，使用 dtype 定義數據類型
bb = np.array([[1, 2, 3], [5, 6, 7]], dtype=float)
print(bb)

# 最小維度
c = np.array([1,2,3], ndmin = 3)
print(c)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python2\numpy\np02.py

import numpy as np

a = np.array([[[1, 2, 3], [5, 6, 7]]])

# 取得陣列維度的深度
print(np.ndim(a))

# 依序取得每個維度的數量
print(np.shape(a))

# 修改維度 1,2,3 -> 1,3,2
a.shape = (1, 3, 2)
print(a)

# 也可以使用 reshape，不過不知道為什麼用了之後執行沒問題，但編輯器會報錯
# b = a.reshape(1,2,3)
# print(b)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python2\numpy\np03.py

import numpy as np

# 複製數據
a = [1, 2, 3]
b = np.asarray(a)
c = a
a = [4, 5, 6]
d = np.asarray(a, dtype=float)
print(a)   # [4, 5, 6]
print(b)   # [1 2 3]
print(c)   # [1, 2, 3]
print(d)   # [4. 5. 6.]

# 產生數據
x = np.arange(5, dtype=float)
print(x)  # [0. 1. 2. 3. 4.]
x2 = np.arange(0, 10, 2)
print(x2)  # [0 2 4 6 8]

# 使用 linspace 產生數據
y = np.linspace(1,10,10, dtype=int)
print(y) # [ 1  2  3  4  5  6  7  8  9 10]
y2 = np.linspace(1,2,10)
print(y2) 
# [1. 1.11111111 1.22222222 1.33333333 1.44444444 1.55555556 1.66666667 1.77777778 1.88888889 2.]

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python2\numpy\np04.py

import numpy as np

# 產生一個 0~1 的隨機數
r1 = np.random.random_sample()
print(r1)
r2 = np.random.random_sample((2,2))
print(r2)

# 產生一個多維陣列 0 ~ 1 的隨機數 ( 不包含 1 )
# 一樣有 seed 概念，seed 相同產生的隨機數就相同
a = np.random.rand(4, 3)
print(a)
b = np.random.rand(4, 3, 2)
print(b)

# 如果只是想返回一個隨機數，可使用 randn()
# randn 的用法和 rand 類似，也可從標準正態分佈中產生多維陣列隨機數
# https://wiki.mbalib.com/zh-tw/%E6%AD%A3%E6%80%81%E5%88%86%E5%B8%83
c = np.random.randn()
print(c)

# 產生隨機整數，也可用 size 產生多維陣列隨機數
d = np.random.randint(1, 100, 10)
print(d)
e = np.random.randint(1, 100, size=(2, 2, 3))
print(e)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python2\random\r01-seed.py

import random

# random.seed 
# random.seed 隨機數的「種子」，數值一樣則產生的隨機數相同，若不設定則使用系統提供隨機源
# random.random() 並不是真正的隨機數

random.seed(5)
a = random.random()
random.seed(5)
b = random.random()
c = random.random()   # 重複 print 出來的結果是相同的
d = random.random()
print(f'{a}\n{b}\n{c}\n{d}')


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python2\random\r02-randrange.py

import random

# random.randrange 和 random.randint 都可產生隨機整數

a = random.randrange(2, 500, 2) # randrange 可指定隨機數階層，一定偶數
print(a)
b = random.randrange(0, 1)   # randrange 不包含設定的最後一個數值，一定出現 0
print(b)
c = random.randint(0, 1)   # randint 包含設定的最後一個數值，0 和 1 隨機挑選
print(c)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python2\random\r03-choice.py

import random

# random.choices

a = random.choice([1, 2, 3, 4, 5])  # choice 從 list 中選擇一個隨機元素
print(a)

# choices 從 list 中選擇指定數量的隨機元素 ( 可能會重複 )
b = random.choices([1, 2, 3, 4, 5, 6, 7, 8], k=5)
print(b)

# choices 可透過 weight 定義權重，有相對和累績兩種選一種的設定
# weights 為相對，cum_weights 為累積，下面的例子出現 8 的機率是 1 的八倍
c = random.choices([1, 2, 3, 4, 5, 6, 7, 8], weights=[1, 2, 3, 4, 5, 6, 7, 8], k=5)
print(c)

# shuffle 可以把清單打散為隨機位置
d = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(d)
print(d)

# sample 可以從清單中隨機取出不重複的值
e = random.sample([1, 2, 3, 4, 5, 6, 7, 8], k=4)
print(e)
f = random.sample(range(1,50), k = 6) # 大樂透一行搞定？
print(f)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python2\random\r04-random.py

import random

# random.random() 並不是真正的隨機數，如果 seed 相同則結果相同
a = random.random()
print(a)

# uniform 返回兩個值中間的隨機浮點數
b = random.uniform(3,8)
print(b)

# triangular 返回兩個值中間的隨機浮點數
c = random.triangular(3,8)
print(c)

# beta 分佈，兩個值需都大於 0，返回 0~1 之間隨機浮點數
d = random.betavariate(3,8)
print(d)

# 指數分佈，不可為 0，若為負，則是小於零的福點數
e = random.expovariate(-5)
print(e)

# 其他還有
# random.gammavariate(alpha, beta)
# random.gauss(mu, sigma)
# random.lognormvariate(mu, sigma)
# random.normalvariate(mu, sigma)
# random.vonmisesvariate(mu, kappa)
# random.paretovariate(alpha)
# random.weibullvariate(alpha, beta)

# 參考：https://docs.python.org/zh-cn/3/library/random.html#random.random

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
