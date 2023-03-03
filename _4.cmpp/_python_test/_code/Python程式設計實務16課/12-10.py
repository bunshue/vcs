# _*_ coding: utf-8 _*_
# 程式 12-10 (Python 3 Version)

import requests
from bs4 import BeautifulSoup

url = 'http://www.appledaily.com.tw/appledaily/hotdaily/headline'

news_page = requests.get(url)
news = BeautifulSoup(news_page.text, 'html.parser')

news_title = news.find_all('div', {'class': 'aht_title'})

headlines = ''
for t in news_title:
	title = t.find_all('a')[0]
	headlines += title.text

print(headlines)
	
