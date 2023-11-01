import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個


import requests #滙入requests套件

addr = 'https://www.books.com.tw/'
res = requests.get(addr)

#檢查狀態碼
if res.status_code == 200:
    res.encoding='utf-8'
    print(res.text)
else:
    print(res.status_code)
    
print('------------------------------------------------------------')	#60個

import urllib.request
#設定欲請求的網址
addr = 'http://www.grandtech.info/'
#以with/as敘述來取得網址，離開之後也能釋放資源
with urllib.request.urlopen(addr) as response:
    print('網頁網址',response.geturl())
    print('伺服器狀態碼',response.getcode())
    print('網頁表頭',response.getheaders())
    zct_str = response.read().decode('UTF-8')
print('將網頁資料轉成字串格式',zct_str)

print('------------------------------------------------------------')	#60個

from urllib.parse import urlparse

addr = 'https://www.zct.com.tw/hot_sale.php?act=goods&hash=5717321f978f1'

result = urlparse(addr)
print('回傳的 ParseResult 物件:')
print(result)
print('通訊協定:'+result.scheme)
print('網站網址:', result.netloc)
print('路徑:', result.path)
print('查詢字串:', result.query)



print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個




#政府資料開放平臺 XML格式資料擷取與應用

url="https://apiservice.mol.gov.tw/OdService/download/A17000000J-000007-yrg"

import urllib.request as ur

with ur.urlopen(url) as response:
    get_xml=response.read()
    

from bs4 import BeautifulSoup

data = BeautifulSoup(get_xml,'xml')
HandlingUnit = data.find_all('辦理單位')
ContactPerson = data.find_all('聯絡人')
DuringTraining = data.find_all('訓練期間')
ContactNumber = data.find_all('聯絡電話')
CourseTitle = data.find_all('課程名稱')


csv_str = ""
for i in range(0, len(HandlingUnit)):
    csv_str += "{},{},{},{},{}\n".\
                format(HandlingUnit[i].get_text(),\
                       ContactPerson[i].get_text(),\
                       ContactNumber[i].get_text(),\
                       DuringTraining[i].get_text(),\
                       CourseTitle[i].get_text())

with open("course_xml.csv", "w") as f:
    story=f.write(csv_str)    #寫入檔案
    
print("XML格式資料擷取與應用,已將資料寫入course_xml.csv")



print('------------------------------------------------------------')	#60個

#以BeautifulSoup套件進行網頁解析
from bs4 import BeautifulSoup
content="""
<!DOCTYPE html>
<html lang="zh-TW">
<head>
<title>BeautifulSoup套件進行網頁解析</title>
<meta charset="utf-8">
</head>
<body>
<h1 style="background-color:red; color:white; font-family:Segoe Script; border:3px #000000 solid;">Python is funny</h1>
Python簡單易學又有趣
<h1 style="color:rgb(255, 99, 71);">程式設計網站推薦</h1>
<a href="https://www.python.org/">Python官方網站</a>
</body>
</html>
"""
bs = BeautifulSoup(content,'html.parser') 
print('網頁標題屬性：') #網頁標題屬性
print(bs.title) #網頁標題屬性
print('--------------------------------------------------------')
print('網頁html語法區塊：') 
print(bs.find('html')) #<html>標籤
print('--------------------------------------------------------')
print('網頁表頭範圍：') 
print(bs.find('head')) #<head>標籤
print('--------------------------------------------------------')
print('網頁身體範圍：') 
print(bs.find('body')) #<body>標籤
print('--------------------------------------------------------')
print('第1個超連結：')
print(bs.find("a",{"href":"https://www.python.org/"}))
print('--------------------------------------------------------')

print('------------------------------------------------------------')	#60個


from bs4 import BeautifulSoup
import requests

addr = 'https://tw.stock.yahoo.com/s/list.php?\
c=%A8%E4%A5%A6%B9q%A4l&rr=0.84235400%201556957344'

#取得網頁原始程式碼
res = requests.get(addr).text 
#以html.parser解析程式解析程式碼
bs = BeautifulSoup(res, 'html.parser')
#以<tr>並配合屬性取得表格中每列內容
rows = bs.find_all('tr', {'height':'30'})

#印出要查詢資料各欄位名稱
print('代號 名稱  時間  成交  買進   賣出  漲跌   張數   昨收   開盤  最高  最低')
#讀取每列的內容，找出<td>
for row in rows:
    if row.find('td'):
        #屬性stripped_strings去餘每欄中字串的空白符號
        cols =[item for item in row.stripped_strings]
        #讀取List物件的元素
        for item in range(0,len(cols)):
            print(cols[item], end = ' ')
        print() #換行
print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個

