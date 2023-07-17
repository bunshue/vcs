import requests
from bs4 import BeautifulSoup
url = 'http://www.ehappy.tw/bsdemo1.htm'
html = requests.get(url)
html.encoding = 'UTF-8'
sp = BeautifulSoup(html.text, 'html.parser')

print(sp.title)
print(sp.title.text)
print(sp.h1)
print(sp.p)