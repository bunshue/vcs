#!/usr/bin/python

print("抓取網頁資料")
from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
#print(html.read())
print(html.read(), 'utf-8')

