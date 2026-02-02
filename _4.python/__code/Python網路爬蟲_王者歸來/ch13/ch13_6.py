# ch13_6.py
import requests, bs4

url = 'https://www.moneydj.com/funddj/ya/YP401000.djhtm'
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')          # 取得物件
fundtable = objSoup.find('table', id='oMainTable')
# 抓標題
objhead = fundtable.find('tr', id='oScrollMenu')
heads = objhead.find_all('th')
for head in heads:
    print(head.text.strip())

















