import requests
from bs4 import BeautifulSoup

urlstr='http://www.drmaster.com.tw/Publish_Newbook.asp'

responseObj=requests.get(urlstr)
responseObj.encoding="utf-8"
bs=BeautifulSoup(responseObj.text, 'html.parser')

data=bs.select('td a img')

for book in data:
    if("http" in book.get('src')):
        print(book.get('src'))
