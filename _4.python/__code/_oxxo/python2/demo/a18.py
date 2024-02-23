# encoding:UTF-8
from lxml import html
import requests
import json

# https://mis.twse.com.tw/stock/fibest.jsp?stock=0050
url = 'https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch=tse_0050.tw'
page = requests.get(url)
j = json.loads(page.text)

print(j)

