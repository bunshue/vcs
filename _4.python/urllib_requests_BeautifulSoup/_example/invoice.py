import sys

import requests
from bs4 import BeautifulSoup
import urllib.parse
import html5lib

#無參數
def get_html_data1(url):
    print('取得網頁資料: ', url)
    resp = requests.get(url)
    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print('讀取網頁資料錯誤, url: ', resp.url)
        return None
    else:
        return resp

print('------------------------------------------------------------')	#60個

print("統一發票號碼 方法一")

import requests
import xml.etree.cElementTree as ET
#import xml.etree.ElementTree as ET  看起來一樣

url = 'http://invoice.etax.nat.gov.tw/invoice.xml'   #統一發票中獎號碼
html_data = get_html_data1(url)
if html_data:
    print("擷取網頁資料 OK")
    #print(html_data.text)
else:
    print('無法取得網頁資料')
    sys.exit()

#print(html_data.text)
tree = ET.fromstring(html_data.text)
print(tree)
print('根目錄標籤：' + tree.tag)
print('根目錄屬性：' + str(tree.attrib))
print('根目錄值：' + str(tree.text))

item = tree[0].find('item')
print('find 方法：' + item[0].text)

items = tree[0].findall('item')
print('findall 方法：' + items[0][0].text)

items = list(tree.iter(tag = 'item'))
print('iter 方法：' + items[0][0].text)

print('--------')


ret = {}
url = 'http://invoice.etax.nat.gov.tw/invoice.xml'   #統一發票中獎號碼
html_data = get_html_data1(url)
if html_data:
    print("擷取網頁資料 OK")
    #print(html_data.text)
else:
    print('無法取得網頁資料')
    sys.exit()

#print(html_data.text)
tree = ET.fromstring(html_data.text)  #解析XML
items = list(tree.iter(tag='item'))  #取得item標籤內容
title = items[0][0].text  #期別
ret['title'] = title + '月'
ptext = items[0][2].text  #中獎號碼
ptext = ptext.replace('<p>','')
plist = ptext.split('</p>')  
for i in range(len(plist)-1):
    tlist = plist[i].split('：')
    ret[tlist[0]] = tlist[1]
print(ret)





print('------------------------------------------------------------')	#60個

print("統一發票號碼 方法二")

import requests

url = 'https://invoice.etax.nat.gov.tw/index.html'
# 取得網頁html
web = get_html_data1(url)
# 設置編碼，避免中文亂碼
web.encoding='utf-8'       

from bs4 import BeautifulSoup
# 轉換成標籤樹
tree = BeautifulSoup(web.text, "html.parser")  
# 取出開獎月份
issue = tree.select(".carousel-item")[0].getText(); 
print(issue)
# 取出中獎號碼陣列
winlist = tree.select('.container-fluid')[0].select('.etw-tbiggest')  
#特別獎
nss = winlist[0].getText()  
#特獎
ns = winlist[1].getText() 
# 頭獎
n1 = [winlist[2].getText()[-8:], winlist[3].getText()[-8:], winlist[4].getText()[-8:]] 
print("特別獎:\n" + "　　"+nss + "\n")
print("特獎:\n"+"　　" + ns + "\n")
print("頭獎:")
for j in n1:
  print("　　"+j)
print("\n")






print('------------------------------------------------------------')	#60個


