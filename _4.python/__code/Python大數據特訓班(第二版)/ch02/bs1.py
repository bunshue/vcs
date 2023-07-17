import requests
from bs4 import BeautifulSoup
url = 'http://ehappy.tw/bsdemo1.htm'
html = requests.get(url)
html.encoding = 'UTF-8'
sp = BeautifulSoup(html.text, 'lxml')

print(sp.title)
print(sp.title.text)
print(sp.h1)
print(sp.p)