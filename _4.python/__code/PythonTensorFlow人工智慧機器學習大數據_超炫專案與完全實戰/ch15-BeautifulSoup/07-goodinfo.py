import requests
from bs4 import BeautifulSoup

req=requests.get("https://goodinfo.tw/StockInfo/StockDividendSchedule.asp?STOCK_ID=2892")
soup=BeautifulSoup(req.text.encode('utf-8'), "html.parser")

for listRight in soup.select('.focus-news'):
   for line in listRight.select('.title'):
     print(line.select('a')[0].text)
