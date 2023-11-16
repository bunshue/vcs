import requests
from bs4 import BeautifulSoup

req=requests.get("https://feebee.com.tw/s/?q=raspberry+pi+3")
soup=BeautifulSoup(req.text.encode('utf-8'), "html.parser")

for line in soup.select('.items'):
   print(line.select('.large')[0].text)
   print(line.select('.ellipsis')[0].text)
   print(line.select('a')[0].get("href"))



