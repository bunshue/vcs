import os
import sys
import time
import random

'''
print("------------------------------------------------------------")  # 60個

"""
#按 ctrl + c 離開程式

import random, shutil, sys, time

PAUSE = 0.1  # (!) Try changing this to 0.0 or 2.0.
STREAM_CHARS = ['0', '1']  # (!) Try changing this to other characters.

print('按 ctrl + c 離開程式')

try:
    while True:
        print(random.choice(STREAM_CHARS), end='')
        sys.stdout.flush()  # Make sure text appears on the screen.
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.

print("------------------------------------------------------------")  # 60個

try:
    while True:  # Main program loop.
        # Clear the screen by printing several newlines:
        print('\n' * 60)

        # Get the current time from the computer's clock:
        currentTime = time.localtime()
        # % 12 so we use a 12-hour clock, not 24:
        hours = str(currentTime.tm_hour % 12)
        if hours == '0':
            hours = '12'  # 12-hour clocks show 12:00, not 00:00.
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)

        print(hours, minutes, seconds)

        print('按 ctrl + c 離開程式')

        # Keep looping until the second changes:
        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break
except KeyboardInterrupt:
    print('Digital Clock, by Al Sweigart al@inventwithpython.com')
    sys.exit()  # When Ctrl-C is pressed, end the program.
"""


print("------------------------------------------------------------")  # 60個

import itertools

print('test itertools')
local_y_range = range(10)
local_x_range = range(10)
coords = list(itertools.product(local_x_range, local_y_range))
random.shuffle(coords)
print(coords)


print("------------------------------------------------------------")  # 60個

print('test random.triangular')

for _ in range(10):
    print(random.triangular(1, 5))

print('test random.uniform')
for _ in range(10):
    print(random.uniform(0.2, 0.9))

print("------------------------------------------------------------")  # 60個

cc = 'ABC' * 5
print(cc)

cc = ['A', 'B', 'C'] * 5
print(cc)

cc = [1,2,3] * 5
print(cc)


cc = 'A' * 5
print(cc)

print("------------------------------------------------------------")  # 60個

a = [i for i in range(10)]
print(a)

a = (i for i in range(10))
print(a)


print("------------------------------------------------------------")  # 60個

import numpy as np

x1 = np.linspace(-2.0, 2.0, 11) #包含頭尾共21點

# 移除 x1 > 0.55 的點, 就是保存 x1 <=0.6的點
x2 = x1[x1 <= 0.55]

# 遮罩 x1 > 0.7 的點, 會多了點線標記
x3 = np.ma.masked_where(x1 > 0.7, x1)

print(x1)
print(x2)
print(x3)


"""
x = np.random.normal(mu, sigma, size=N*10)  # 隨機數

# list 移除資料的寫法
x2 = x[x <= 100.0]
x2 = x2[ x2 >= 0]

"""

#過濾資料

"""
scores1 = np.random.normal(mu, sigma, size=N)  # 隨機數
print("資料個數1 :", len(scores1))
print("最高分 :", max(scores1))
print("最低分 :", min(scores1))

scores2 = scores1[scores1 <= 100.0]
scores3 = scores2[scores2 >= 0.0]
"""

'''
print("------------------------------------------------------------")  # 60個

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
print(type(portfolio))
print(portfolio)
print()



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

import re

s = ' hello world \n'
print("|"+s.strip()+"|")
print("|"+s.lstrip()+"|")
print("|"+s.rstrip()+"|")

# Character stripping
t = '-----hello====='
print(t.lstrip('-'))
print(t.strip('-='))

# 对中间不会影响
s = ' hello     world \n'
print(s.strip())

print(s.replace(' ', ''))
print(re.sub('\s+', ' ', s))



print("------------------------------------------------------------")  # 60個

text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

# 填充字符
print(text.rjust(20,'='))
print(text.center(20,'*'))

# format函数
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))
# 同时增加填充字符
print(format(text, '=>20s'))
print(format(text, '*^20s'))

# 格式化多个值
print('{:=>10s} {:*^10s}'.format('Hello', 'World'))

# 格式化数字
x = 1.2345
print(format(x, '=^10.2f'))

print("------------------------------------------------------------")  # 60個

"""
#plot 暫存
x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[16800,20000,21600,25400,12800,20000,25000,14600,32800,25400,18000,10600]
plt.plot(x, y, marker='d',ms=10, mfc='r', mec='b')
"""

print("------------------------------------------------------------")  # 60個

import sys
cc = sys.getdefaultencoding()

print(cc)

print("------------------------------------------------------------")  # 60個

import numpy as np

b = np.array([[1,2,3],[4,5,6]])
print(b[0, 0], b[0, 1], b[0, 2])
print(b[1, 0], b[1, 1], b[1, 2])

print("------------------------------------------------------------")  # 60個

import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a.dtype)
print(a.size)
print(a.shape)
print(a.itemsize)
print(a.ndim)
print(a.nbytes)

print("------------------------------------------------------------")  # 60個

import numpy as np

a = np.array([1,2,3,4,5,6])
print(a)
b = a.reshape((3, 2))
print(b)

print("------------------------------------------------------------")  # 60個

import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = a.reshape((3, 3))
print(b)
c = b.flatten()
print(c)

print("------------------------------------------------------------")  # 60個

import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
c = np.concatenate((a, b), axis=0)
print(c)
d = np.concatenate((a, b), axis=1)
print(d)

print("------------------------------------------------------------")  # 60個

import numpy as np

a = np.array([[1,2,3,4,5,6,7,8]])
b = a.reshape(2, 4)
print(b.shape)
c = np.expand_dims(b, axis=0)
d = np.expand_dims(b, axis=1)
print(c.shape, d.shape)
e = np.squeeze(c)
f = np.squeeze(d)
print(e.shape, f.shape)

print("------------------------------------------------------------")  # 60個

import numpy as np

a = np.array([[11,22,13,74,35,6,27,18]])

min_value = np.min(a)
max_value = np.max(a)
print(min_value, max_value)

min_idx = np.argmin(a)
max_idx = np.argmax(a)
print(min_idx, max_idx)

print("------------------------------------------------------------")  # 60個

import requests

r = requests.get('http://www.flag.com.tw') # 向旗標網站發出 GET 請求,並將回應物件儲存到 r

if r.status_code == 200:   # 回應的狀態碼若為 200 表示 OK
    print(r.text)          # 將回應的文字(網頁原始碼)印出來
else:
    print(r.status_code, r.reason) # 若發生錯誤(狀態碼不是 200), 則印出狀態碼及錯誤原因
    
print('------------------------------------------------------------')	#60個

url = 'https://httpbin.org/get'
hd = {'user-key': '7ADGS9S'}  # 標頭參數(以字典儲存)
pm = {'id': 1023, 'neme': 'joe'}   # 網址參數(以字典儲存)
r = requests.get(url, headers = hd, params = pm)   # 加入 headers 及 params 參數
print(r.text)   # 將回應的文字印出來

print('------------------------------------------------------------')	#60個

url = 'http://httpbin.org/post' # 使用測試服務網站, POST 方法網址要加 /post
r = requests.post(url, data = 'Hello')  # 送出字串資料
print(r.text)
r = requests.post(url, data = {'id':'123', 'name':'Joe'})
print(r.text)

print('------------------------------------------------------------')	#60個

r = requests.put('https://httpbin.org/put', data = {'key':'abc'})
print(r.text)
r = requests.patch('https://httpbin.org/patch', data = {'key':'xyz'})
print(r.text)
r = requests.delete('https://httpbin.org/delete')
print(r.text)

print('------------------------------------------------------------')	#60個

page = """
<html>
  <head><title>旗標科技</title></head>
  <body>
    <div class="section" id="main">
      <img alt="旗標圖示" src="https://zh.wikipedia.org/static/images/icons/wikdddipedia.png">
      <p>產品類別</p>
      <button id="books"><h4 class="bk">圖書</h4></button>
      <button id="maker"><h4 class="pk">創客</h4></button>
      <button id="teach"><h4 class="pk">教具</h4></button>
    </div>
    <div class="section" id="footer">
      <p>杭州南路一段15-1號19樓</p>
      <a href="http://flag.tw/contact">聯絡我們</a>
    </div>
  </body>
</html>
"""

from bs4 import BeautifulSoup
bs = BeautifulSoup(page, 'lxml')

print(bs.title)
print(bs.a)

print(bs.a.text)
print(bs.a.get('href'))
print(bs.a['href'])

print(bs.find('h4'))
print(bs.find('h4', {'class': 'pk'}))
print(bs.find('h4').text)

print(bs.find_all('h4'))
print(bs.find_all('h4', {'class': 'pk'}))

print(bs.find_all(['title', 'p']))
print(bs.find_all(['title', 'p'])[1].text)  #← 傳回第 1 個 (由 0 算起) 符合標籤中的文字

print('h4:', bs.select('h4'))         #←查詢所有 h4 標籤
print('#book:', bs.select('#books'))  #←查詢所有 id 為 'books' 的標籤
print('.pk:', bs.select('.pk'))       #←查詢所有 class 為 'pk' 的標籤
print('h4.bk', bs.select('h4.bk'))    #←查詢所有 class 為 'bk' 的 h4 標籤

print(bs.select('#main button .pk'))

print(bs.select('#main button .pk')[1].text)
print(bs.select('#footer a')[0]['href'])




print('------------------------------------------------------------')	#60個


import re # 使用前要先匯入 re 模組
print(re.match (r'pyt', 'python')) # pyt 由開頭即符合, 因此成功
print(re.match (r'yth', 'python')) # yth 與開頭不符合, 因此失敗
print(re.search(r'yth', 'python')) # seach( ) 不限開頭, 因此成功


print('------------------------------------------------------------')	#60個


import re

m = re.search(r'p[a-z]+e', 'apples')
print(m)   # 輸出 <_sre.SRE_Match object; span=(1, 5), match='pple'>
print(m.group())    # 輸出 pple
print(m.start())    # 輸出 1
print(m.end())    # 輸出 5 注意！pple 的位置是 1~4
print(m.span())    # 輸出 (1, 5)

print('------------------------------------------------------------')	#60個

print('1111 fail')
from selenium import webdriver    # 匯入 selenium 的 webdriver 子套件
from time import sleep         # 匯入內建 time 模組的 sleep() 函式 (計時用)
browser = webdriver.Chrome()   # 建立 Chrome 瀏覽器物件
browser.get('http://www.flag.com.tw')  # 開啟 Chrome 並連到旗標網站
sleep(5)                       # 暫停 5 秒
browser.close()                # 關閉網頁(目前分頁)A

print('------------------------------------------------------------')	#60個

print('2222')

from selenium import webdriver # 匯入 selenium 的 webdriver
from time import sleep         # 匯入內建 time 模組的 sleep() 函式

browser = webdriver.Chrome()            # 建立 Chrome 瀏覽器物件
browser.get('http://www.google.com')    # 開啟 Chrome 並連到 Google 網站
print('標題：' + browser.title)         # 輸出網頁標題
print('網址：' + browser.current_url)   # 輸出網頁網址
print('內容：' + browser.page_source[0:50]) # 輸出網頁原始碼的前 50 個字
print('視窗：', browser.get_window_rect())  # 輸出視窗的位置及寬高
browser.save_screenshot('d:/scrcap.png')   # 截取網頁畫面
sleep(3) # 暫停 3 秒
browser.set_window_rect(200, 100, 500, 250)   # 改變視窗位置及大小
sleep(3)
browser.fullscreen_window()     # 將視窗設為全螢幕
sleep(3)
browser.quit() # 關閉視窗結束驅動

print('------------------------------------------------------------')	#60個

print('333')

from selenium import webdriver # 匯入 selenium 的 webdriver

browser = webdriver.Chrome() # 建立 Chrome 瀏覽器物件
browser.get('http://www.google.com') # 開啟 Chrome 並連到旗標網站
e1 = browser.find_element_by_tag_name('head')  # 尋找 head 標籤
print(e1.tag_name)  # 輸出 head 確認已找到 (tag_name 屬性為標籤名稱, 詳見下表)
e2 = e1.find_element_by_tag_name('title')  # 在 head 元素中尋找 title 標籤
print(e2.tag_name)  # 輸出 tite 確認已找到
browser.quit()     # 關閉視窗結束驅動

print('------------------------------------------------------------')	#60個

from selenium import webdriver  # 匯入 selenium 的 webdriver

opt = webdriver.ChromeOptions()  # ←建立選項物件
opt.add_experimental_option('prefs',  # ←在選項物件中加入「禁止顯示訊息框」的選項
                            {'profile.default_content_setting_values': {'notifications': 2}})
browser = webdriver.Chrome(options=opt)  # ←以 options 指名參數來建立瀏覽器物件

browser.get('http://www.facebook.com')  # ←開啟 Chrome 並連到 fb 網站
browser.find_element_by_id('email').send_keys('您的帳號')  # }
browser.find_element_by_id('pass').send_keys('您的密碼')  # }輸入帳密並按登入鈕
browser.find_element_by_name('login').click()  # }

print('------------------------------------------------------------')	#60個

from selenium import webdriver  # 匯入 selenium 的 webdriver
from time import sleep          # 匯入內建的 time 模組的 sleep() 函式

opt =  webdriver.ChromeOptions()      #建立選項物件
opt.add_experimental_option('prefs',  #加入「禁止顯示訊息框」的選項
    {'profile.default_content_setting_values': {'notifications' : 2}})
browser = webdriver.Chrome(options = opt) #以 options 參數來建立瀏覽器物件

browser.get('http://www.google.com')    #←開啟 Chrome 並連到 Google 網站
browser.maximize_window()  #←將視窗最大化以避免最右邊的登入鈕沒顯示出來

browser.find_element_by_id('gb_70').click()   #←按登入鈕
sleep(3)       #←暫停 3 秒等待進入下一頁
browser.find_element_by_id('identifierId').send_keys('您的帳號') #}←輸入帳號
browser.find_element_by_id('identifierNext').click()   #←按繼續鈕
sleep(3)       #←暫停 3 秒等待進入下一頁
browser.find_element_by_name('password').send_keys('您的密碼')  #←輸入帳密
browser.find_element_by_id('passwordNext').click()   #←按繼續鈕

print('------------------------------------------------------------')	#60個

'''
datestr = "20210201"

# 下載股價
r = requests.get(
    'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALLBUT0999')

print(r.text)

print('------------------------------------------------------------')	#60個

import requests

datestr = "20210201"

# 下載股價
r = requests.get(
    'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALLBUT0999')

print(r.text)

print('------------------------------------------------------------')	#60個

import requests
from io import StringIO
import pandas as pd

datestr = "20210201"
stock_symbol = "2330"

# 下載股價
r = requests.get(
    'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALLBUT0999')

r_text = r.text.split('\n')

r_text = [i for i in r_text if len(
    i.split('",')) == 17 and i[0] != '=']

data = "\n".join(r_text)
df = pd.read_csv(StringIO(data), header=0)

df = df.drop(columns=['Unnamed: 16'])
filter_df = df[df["證券代號"] == stock_symbol]
print(filter_df)

print('------------------------------------------------------------')	#60個

import datetime

date = '20210311'
date = datetime.datetime.strptime(date, '%Y%m%d')
print(date.weekday())

print('------------------------------------------------------------')	#60個

import datetime

start_date_str = "20210125"
end_date_str = "20210201"

start_date = datetime.datetime.strptime(start_date_str, '%Y%m%d')
end_date = datetime.datetime.strptime(end_date_str, '%Y%m%d')

totaldays = (end_date - start_date).days + 1
dates = []
for daynumber in range(totaldays):
    date = (start_date + datetime.timedelta(days=daynumber))
    if date.weekday() < 6:
        dates.append(date.strftime('%Y%m%d'))
print(dates)

print('------------------------------------------------------------')	#60個

def get_setting():    #←將「讀取設定檔」寫成函式, 可讓程式易讀易用
	res = []     #←準備一個空串列來存放讀取及解析的結果
	try:              # 使用 try 來預防開檔或讀檔錯誤
		with open('stock.txt') as f:  # 用 with 以讀取模式開啟檔案
			slist = f.readlines()     # 以行為單位讀取所有資料
			print('讀入：', slist)    # 輸出讀到的資料以供確認
			a, b, c = slist[0].split(',')   #←將股票字串以逗號切割為串列
			res = [a, b, c]
	except:
		print('stock.txt 讀取錯誤')
	return res   #←傳回解析的結果, 但如果開檔或讀檔錯誤則會傳回 []

stock = get_setting()     # 呼叫上面的函式
print('傳回：', stock)    # 輸出傳回的結果

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import crawler_module as m
from time import sleep
import pandas as pd

all_list = []
stock_symbol, dates = m.get_data()

for date in dates:
    sleep(5)
    try:
        crawler_data = m.crawl_data(date, stock_symbol)
        all_list.append(crawler_data[0])
        df_columns = crawler_data[1]
        print("  OK!  date = " + date + " ,stock symbol = " + stock_symbol)
    except:
        print("error! date = " + date + " ,stock symbol = " + stock_symbol)

all_df = pd.DataFrame(all_list, columns=df_columns)
print(all_df)

# step 1 prepare data
day = all_df["日期"].astype(str)
close = all_df["收盤價"].astype(float)

# step 2 create plot
plt.figure(figsize=(12, 8), dpi=100)

# step 3 plot
plt.plot(day, close, 's-', color='r', label="Close Price")
plt.title("TSMC Line chart")
plt.xticks(fontsize=10, rotation=45)
plt.yticks(fontsize=10)
plt.legend(loc="best", fontsize=20)

plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import crawler_module as m
from time import sleep
import pandas as pd

all_list = []
stock_symbol, dates = m.get_data()

for date in dates:
    sleep(5)
    try:
        crawler_data = m.crawl_data(date, stock_symbol)
        all_list.append(crawler_data[0])
        df_columns = crawler_data[1]
        print("  OK!  date = " + date + " ,stock symbol = " + stock_symbol)
    except:
        print("error! date = " + date + " ,stock symbol = " + stock_symbol)

all_df = pd.DataFrame(all_list, columns=df_columns)

# step 1 prepare data
day = all_df["日期"].astype(str)
openprice = all_df["開盤價"].astype(float)
close = all_df["收盤價"].astype(float)

# step 2 create plot
fig, (ax, ax2) = plt.subplots(2, 1, sharex=True, figsize=(12, 8), dpi=100)
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
ax.set_title(stock_symbol+"  開盤價、收盤價 ( " +
             dates[0] + " ~ " + dates[-1] + " )")

# step 3 plot 子圖(ax)
ax.plot(day, openprice, 's-', color='r', label="Open Price")
ax.legend(loc="best", fontsize=10)

# step 3 plot 子圖(ax2)
ax2.plot(day, close, 'o-', color='b', label="Close Price")
ax2.legend(loc="best", fontsize=10)
ax2.set_xticks(range(0, len(day), 5))
ax2.set_xticklabels(day[::5])

# step 4 show plot
plt.show()

'''
print("------------------------------------------------------------")  # 60個


import requests

def download_pic(url, path):
    print(path)
    pic = requests.get(url)     #使用 GET 對圖片連結發出請求
    path += url[url.rfind('.'):]     #將路徑加上圖片的副檔名
    print(path)
    f = open(path,'wb')     #以指定的路徑建立一個檔案
    f.write(pic.content)     #將 HTTP Response 物件的 content寫入檔案中
    f.close()     #關閉檔案
    
url = "http://i.epochtimes.com/assets/uploads/2015/05/1502192113172483-600x400.jpg"  #貼上src屬性中的路徑
pic_path = "tmp_download_picture" #設定圖片的儲存名稱和路徑
download_pic(url, pic_path)

print('------------------------------------------------------------')	#60個

"""
import photo_module as m

while True:
    photo_name = input("請輸入要下載的圖片名稱: ")

    download_num = int(input("請輸入要下載的數量: "))

    photo_list = m.get_photolist(photo_name, download_num)

    if photo_list == None:
        print("找不到圖片, 請換關鍵字再試試看")
    else:
        if len(photo_list) < download_num:
            print("找到的相關圖片僅有", len(photo_list), "張")
        else:
            print("取得所有圖片連結")
        break

print("開始下載...")

for i in range(len(photo_list)):
    m.download_pic(photo_list[i], str(i+1))

print("\n下載完畢")

print('------------------------------------------------------------')	#60個

import photo_module as m
import os

while True:
    photo_name = input("請輸入要下載的圖片名稱: ")
        
    download_num = int(input("請輸入要下載的數量: "))
    
    photo_list = m.get_photolist(photo_name, download_num) 
    
    if photo_list == None:
        print("找不到圖片, 請換關鍵字再試試看")
    else:
        if len(photo_list) < download_num:
            print("找到的相關圖片僅有", len(photo_list), "張" )
        else:
            print("取得所有圖片連結") 
        break

folder_name = m.create_folder(photo_name)
    
print("開始下載...")
 
for i in range(len(photo_list)):
    m.download_pic(photo_list[i], folder_name + os.sep + photo_name + os.sep + str(i+1))
    
print("\n下載完畢")
"""

print('------------------------------------------------------------')	#60個

import threading

def job(num):
  print("子執行緒", num)

threads = []
for i in range(3):
  threads.append(threading.Thread(target = job, args = (i,)))
  threads[i].start()

for i in range(3):
  print("主程式", i)

for i in threads:
  i.join()

print("結束")

print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

