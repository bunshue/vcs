import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個
#共用套件

import requests

print("------------------------------------------------------------")  # 60個

print("查詢台銀牌告匯率")


from bs4 import BeautifulSoup #解析網頁
import csv #處理CSV檔案
from time import localtime, strftime #處理時間
from os.path import exists #台銀匯率網站

html = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW") #回傳HTML檔案，轉存html物件
bsObj = BeautifulSoup(html.content, "lxml") #解析網頁，建立bs物件
for single_tr in bsObj.find("table", {"title":"牌告匯率"}).find("tbody").findAll("tr"): #針對匯率表格分析
    cell = single_tr.findAll("td") #找到每一個表格
    currency_name = cell[0].find("div", {"class":"visible-phone"}).contents[0] #找到表格中幣別
    currency_name = currency_name.replace("\r","") #取代不需要的字元
    currency_name = currency_name.replace("\n","")
    currency_name = currency_name.replace(" ","")
    currency_rate = cell[2].contents[0] #找到幣別匯率
    print(currency_name, currency_rate)
    filename = "bankRate" + currency_name + ".csv" #每種幣別存一個檔案
    now_time = strftime("%Y-%m-%d %H:%M:%S", localtime()) #記錄目前時間
    if not exists(filename):
        data = [['時間', '匯率'], [now_time, currency_rate]] #準備寫入檔案資料
    else:
        data = [[now_time, currency_rate]]

    f = open(filename, "a") #開啟檔案
    w = csv.writer(f) #建立寫入CSV物件
    print('寫入資料 :', data)
    w.writerows(data) #寫入資料
    f.close()
    
print('------------------------------------------------------------')	#60個

# 資料
my_data = {'key1': 'value1', 'key2': 'value2'}
# 將資料加入POST 請求中
r = requests.post('http://httpbin.org/post', data = my_data)
print(r.text)
print(r.status_code)

print('------------------------------------------------------------')	#60個

# 要上傳的檔案
my_files = {'my_filename': open('bankRate.csv', 'rb')}
# 將檔案加入POST 請求中
r = requests.post('http://httpbin.org/post', files = my_files)
print(r.status_code)

print('------------------------------------------------------------')	#60個

from bs4 import BeautifulSoup

""" fail?
print("臺灣證交所本國上市證券")
#查詢台灣證交所本國上市證券國際證券辨識號碼一覽表

import pandas as pd #匯入pandas套件

df = pd.read_html('http://isin.twse.com.tw/isin/C_public.jsp?strMode=2', encoding = 'big5hkscs', header = 0)
newdf = df[0][df[0]['產業別'] > '0'] #產業別資料大於0
#del newdf['國際證券辨識號碼(ISIN Code)'],newdf['CFICode'],newdf['備註']
del newdf['CFICode'],newdf['備註'] #刪除兩個不需要欄位
df2 = newdf['有價證券代號及名稱'].str.split(' ', expand = True) #分成兩個欄位回存
df2 = df2.reset_index(drop = True) #重設索引值
newdf = newdf.reset_index(drop = True) #重設索引值
for i in df2.index:
    if ' ' in df2.iat[i,0]: #將有價證券代號及名稱
        df2.iat[i,1] = df2.iat[i,0].split(' ')[1] #欄位資料內容分割為2，回存df2物件中。
        df2.iat[i,0] = df2.iat[i,0].split(' ')[0] #回存df2物件中。
newdf = df2.join(newdf) #將df2合併到newdf物件
newdf = newdf.rename(columns = {0:'股票代號', 1:'股票名稱'}) #修改欄位名稱
del newdf['有價證券代號及名稱'] #將"有價證券代號及名稱"欄位刪除

filename = 'stock_.xlsx'
newdf.to_excel(filename, sheet_name = 'Sheet1', index = False) #存入excel

print('已存檔到 : ', filename)
"""

print("------------------------------------------------------------")  # 60個

import json
import urllib.parse

url = "https://udn.com/api/more?page=2&id=&channelId=1&cate_id=0&type=breaknews&totalRecNo=6561"
html = requests.get(url).text
data = json.loads(html)


titles = data['lists']
for title in titles:
    print(title['title'])
    print(urllib.parse.urljoin("https://udn.com", title['titleLink']))

url = "https://ck101.com/forum-3590-1.html?ref=nav"
res = requests.get(url)
print(res)
print(res.text)

url = "https://ck101.com/forum-3590-1.html?ref=nav"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}
res = requests.get(url, headers=headers)
print(res)
print(res.text)

print("------------------------------------------------------------")  # 60個

print("新北市不動產仲介經紀商業同業公會網站")

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

file_name = "tmp_新北市仲介.csv" #設定csv寫入檔名

f = open(file_name, "w", encoding = 'utf8')
w = csv.writer(f)
httphead = 'http://www.tcr.org.tw/a/table_blogs/index/21654'

# 根據新北市不動產仲介經紀商業同業公會網站會員介紹首頁
# 與其後各頁差異，根據頁面規則涵蓋需要抓取頁面
for i in range(1,17):
    if i==1:
        htmlname=httphead
    else:
        htmlname=httphead+"?page="+str(i)
    html = urlopen(htmlname)
    # 以BeautifulSoup的"lxml"模式解析網頁，設定為bsObj物件
    bsObj = BeautifulSoup(html, "lxml")
    count=0

    for single_tr in bsObj.find("table").find("table").findAll("tr"): #抓取網頁資料
        if count==0:
            cell = single_tr.findAll("th") # 處理表頭
            F0 = cell[0].contents
            F1 = cell[1].contents
            F2 = cell[2].contents
            F3 = cell[3].contents
            F4 = cell[4].contents
        else:
            cell = single_tr.findAll("td") # 處理表格中資料
            # print(cell)
            F0 = cell[0].a.string
            F1 = cell[1].a.string
            F2 = cell[2].a.string
            F3 = cell[3].a.string
            F4 = cell[4].a.string
        print(F0,F1,F2,F3,F4)
        data = [[F0,F1,F2,F3,F4]]
        if i>1 and count>0:
            w.writerows(data) # 逐行寫入csv檔案
        count=count+1

f.close()

print("------------------------------------------------------------")  # 60個

print("各國GDP資料")

# 讀入csv 文字檔
import pandas as pd
csv_file = "https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv"
gdp = pd.read_csv(csv_file)
print('------------------------------------------------')
print(type(gdp))
print('------------------------------------------------')
print(gdp.head())
print('------------------------------------------------')

# 讀入excel 試算表
xlsx_file = "https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.xlsx"
gapminder = pd.read_excel(xlsx_file)
print('------------------------------------------------')
print(type(gapminder))
print('------------------------------------------------')
print(gapminder.head())
print('------------------------------------------------')

print('用list 標註變數名稱從DataFrame選出country 與continent 欄位：')
print(gapminder[['country', 'continent']])

print('------------------------------------------------')
print('選一個變數且沒有以list 標註，選出欄位資料，型別為Series')
country = gapminder['country']
print(type(country))
print('------------------------------------------------')
print('聚合函數計算sum，計算2007 年全球人口總數：')
aa = gapminder[gapminder['year'] == 2007][['pop']].sum()
print(aa)
print('------------------------------------------------')
print('計算2007 年全球的平均壽命、平均財富：')
bb = gapminder[gapminder['year'] == 2007][['lifeExp', 'gdpPercap']].mean()
print(bb)
print('------------------------------------------------')
print('groupby群組計算2007 年各洲人口總數：')
cc = gapminder[gapminder['year'] == 2007].groupby(by = 'continent')['pop'].sum()
print(cc)

print('------------------------------------------------')

import re
import bs4

print("------------------------------------------------------------")  # 60個

print("webbrowser")
import webbrowser
webbrowser.open('http://www.mcut.edu.tw')

print("------------------------------------------------------------")  # 60個

print("webbrowser")
#address = input("請輸入地址 : ")
address = "新竹市東區榮光里中華路二段445號"
webbrowser.open('http://www.google.com.tw/maps/place/' + address)

print('------------------------------------------------------------')	#60個

print("status_code")
url = 'http://www.mcut.edu.tw'
htmlfile = requests.get(url)
print(type(htmlfile))
if htmlfile.status_code == requests.codes.ok:
    print("取得網頁內容成功")
    print("網頁內容大小 = ", len(htmlfile.text))
else:
    print("取得網頁內容失敗")

print("------------------------------------------------------------")  # 60個

print("aaaa")
url = 'http://www.mcut.edu.tw'
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    print("取得網頁內容成功")
    print(htmlfile.text)            # 列印網頁內容
else:
    print("取得網頁內容失敗")

print('------------------------------------------------------------')	#60個

print("bbbb")
url = 'http://www.mcut.edu.tw'
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    print('欲搜尋的字串')
    pattern = "英文"

    # 使用方法1
    if pattern in htmlfile.text:              # 方法1
        print(f"搜尋 {pattern} 成功")
    else:
        print(f"搜尋 {pattern} 失敗")

    # 使用方法2, 如果找到放在串列name內
    name = re.findall(pattern, htmlfile.text)  # 方法2
    if name:
        print(f"{pattern} 出現 {len(name)} 次")
    else:
        print(f"{pattern} 出現 0 次")
else:
    print("網頁下載失敗")

print('------------------------------------------------------------')	#60個

print("cccc")
url = 'http://mcut.edu.tw/file_not_existed' # 不存在的內容
try:
    htmlfile = requests.get(url)
    htmlfile.raise_for_status()             # 異常處理
    print("下載成功")
except Exception as err:                    # err是系統內建的錯誤訊息
    print(f"網頁下載失敗: {err}")
print("程式繼續執行 ... ")

print('------------------------------------------------------------')	#60個

""" fail
print("金石堂官網")

url = 'https://www.kingstone.com.tw/'
htmlfile = requests.get(url)
htmlfile.raise_for_status()
"""

print('------------------------------------------------------------')	#60個

print("eeee")
headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }
url = 'https://www.kingstone.com.tw/'
htmlfile = requests.get(url, headers=headers)
htmlfile.raise_for_status()
print("偽裝瀏覽器擷取網路資料成功")

print('------------------------------------------------------------')	#60個

print("天瓏書局")
url = 'http://www.tenlong.com.tw'                    # 天瓏書局網址
try:
    htmlfile = requests.get(url)
    print("下載成功")
except Exception as err:                                
    print("網頁下載失敗: %s" % err)
# 儲存網頁內容
fn = 'tmp_html_text1.txt'
with open(fn, 'wb') as file_Obj:                     # 以二進位儲存
    for diskStorage in htmlfile.iter_content(10240): # Response物件處理
        size = file_Obj.write(diskStorage)           # Response物件寫入
        print(size)                                  # 列出每次寫入大小
    print("以 %s 儲存網頁HTML檔案成功" % fn)

print('------------------------------------------------------------')	#60個

""" many
r = requests.get('http://tw.yahoo.com')
print(r.text)

print('------------------------------------------------------------')	#60個

import pprint

r = requests.get('http://tw.yahoo.com')
pprint.pprint(r.text)
"""

print('------------------------------------------------------------')	#60個

""" fail
import pprint

api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'

weather_data = requests.get(api_url).json()

pprint.pprint(weather_data)
"""
print('------------------------------------------------------------')	#60個

""" fail
url = 'http://weather.livedoor.com/forecast/webservice/json/v1'

paload = {'city':'130010'}

weather_data = requests.get(url, params = paload).json()

pprint.pprint(weather_data['forecasts'][0]) 
"""

print('------------------------------------------------------------')	#60個

import pprint

api_url = 'https://zh.wikipedia.org/w/api.php'

api_params = {'format':'json', 'action':'query', 'titles':'椎名林檎', 'prop':'revisions', 'rvprop':'content'}

wiki_data = requests.get(api_url, params = api_params)

pprint.pprint(wiki_data)

print('------------------------------------------------------------')	#60個

addr = 'https://www.edu.tw/'    #教育部
addr = 'https://www.books.com.tw/'

res = requests.get(addr)

#檢查狀態碼
if res.status_code == 200:
    print('status_code= ',res.status_code)
    res.encoding='utf-8'
    print(res.text)
else:
    print('網頁無法開啟, status_code= ',res.status_code)


import base64
from io import BytesIO
from PIL import Image

url = 'https://upload.wikimedia.org/wikipedia/commons/3/3d/Uranus2.jpg'
resp = requests.get(url)
img3 = Image.open(BytesIO(resp.content))
img3.save('tmp_Uranus2.jpg')

#print(base64.b64encode(resp.content))



print('------------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



