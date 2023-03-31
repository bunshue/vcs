# Python 測試 BeautifulSoup

from bs4 import BeautifulSoup

'''
print('BeautifulSoup 測試 1')
import requests
from bs4 import BeautifulSoup

url = 'http://tw.yahoo.com'
html_data = requests.get(url)
soup = BeautifulSoup(html_data.text, "html.parser")
soup.title

print("取得網頁標題")
print(soup.title)


print('BeautifulSoup 測試 2')
import requests
from bs4 import BeautifulSoup

url = 'https://tw.news.yahoo.com/rss/technology'
html_data = requests.get(url)
soup = BeautifulSoup(html_data.text, "html.parser")
type(soup)
soup.findAll('item')

print("取得Yahoo奇摩新聞-科技新聞-標題")
for news in soup.findAll('item'):
	print(news.title)

print('BeautifulSoup 測試 3')
from bs4 import BeautifulSoup
import requests
import sys

url = 'https://www.google.com.tw/'
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, 'html.parser')
all_links = soup.find_all('a')

for link in all_links:
    href = link.get('href')
    if href != None and href.startswith('http://'):
        print('取得資料')
        print(href)


print('BeautifulSoup 測試 4')
import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/NBA/index.html" # PTT NBA 板
html_data = requests.get(url) # 用 requests 的 get 方法把網頁抓下來
html_doc = html_data.text # text 屬性就是 html 檔案
soup = BeautifulSoup(html_data.text, "lxml") # 指定 lxml 作為解析器
#print(soup.prettify()) # 把排版後的 html 印出來

# 一些屬性或方法
print(soup.title) # 把 tag 抓出來
print("---")
print(soup.title.name) # 把 title 的 tag 名稱抓出來
print("---")
print(soup.title.string) # 把 title tag 的內容欻出來
print("---")
print(soup.title.parent.name) # title tag 的上一層 tag
print("---")
print(soup.a) # 把第一個 <a></a> 抓出來
print("---")
print(soup.find_all('a')) # 把所有的 <a></a> 抓出來


'''

'''
print('BeautifulSoup 測試 5')
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        soup = BeautifulSoup(html, "html.parser")
        title = soup.body.h1
    except AttributeError as e:
        return None
    return title

url = 'http://www.pythonscraping.com/exercises/exercise1.html'
title = getTitle(url)
if title == None:
    print("找不到網頁標題")
else:
    print("取得網頁標題:")
    print(title)
'''



import requests
from bs4 import BeautifulSoup

url = 'http://ehappy.tw/bsdemo1.htm'
html_data = requests.get(url)
html_data.encoding = 'UTF-8'
soup = BeautifulSoup(html_data.text, 'html.parser')

print(soup.title)
print(soup.title.text)
print(soup.h1)
print(soup.p)




