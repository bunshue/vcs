import requests
from bs4 import BeautifulSoup

urlstr='http://www.drmaster.com.tw/Publish_Newbook.asp'

response=requests.get(urlstr)
response.encoding="utf-8"
bs=BeautifulSoup(response.text,'html.parser')

listImageUrl=bs.select('td a img')

for link in listImageUrl:
    #if("http" in link.get('src')):
        print(link.get('src'))
