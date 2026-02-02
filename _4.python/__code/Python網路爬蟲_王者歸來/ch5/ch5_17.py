# ch5_17.py
import requests
import bs4
import re

htmlFile = requests.get('https://tw.yahoo.com/')
objSoup = bs4.BeautifulSoup(htmlFile.text, 'lxml')
headline_news = objSoup.find_all('a', class_='story-title')
for h in headline_news:
    print("焦點新聞 : " + h.text)
    print("新聞網址 : " + h.get('href'))














