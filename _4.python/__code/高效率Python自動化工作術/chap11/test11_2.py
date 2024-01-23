import requests
from bs4 import BeautifulSoup

url = "https://www.shoeisha.co.jp/rss/book/index.xml"
tag = "title"
r = requests.get(url)                   #取得URL的資料
r.encoding = r.apparent_encoding        #自動辨識字元編碼
soup= BeautifulSoup(r.text, "lxml")     #剖析XML資料
for i, element in enumerate(soup.findAll(tag)):
    print(i, element.text)              #顯示編號與文字
