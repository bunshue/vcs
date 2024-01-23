import requests
from bs4 import BeautifulSoup

value1 = "https://www.shoeisha.co.jp/rss/book/index.xml"
value2 = "title"

#【函數: 取得RSS的標籤】
def readRSSitem(url, tag):
    msg = ""
    r = requests.get(url)                   #取得URL的資料
    r.encoding = r.apparent_encoding        #自動辨識字元編碼
    soup= BeautifulSoup(r.text, "lxml")     #剖析XML資料
    for i, element in enumerate(soup.findAll(tag)):
        msg += str(i) + ":" + element.text + "\n" #新增標籤的元素
    return msg

#【執行函數】
msg = readRSSitem(value1, value2)
print(msg)
