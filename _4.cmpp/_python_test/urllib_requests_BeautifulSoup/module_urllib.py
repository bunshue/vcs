# python import module : urllib





print("讀取遠端純文字檔1")
from urllib.request import urlopen
textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
print(textPage.read())






print("讀取遠端純文字檔2")
#encoding:Big5

#Perl的基本語法
#http://ind.ntou.edu.tw/~dada/cgi/Perlsynx.htm

import urllib.request   #用來建立請求

url = "http://ind.ntou.edu.tw/~dada/cgi/Perlsynx.htm"
data = urllib.request.urlopen(url).read()
data = data.decode('Big5')      #將bytes轉成str
print(data)

fd = open("__temp\perl.html", "w")
fd.write(data)
fd.close()






"""
import urllib.request   #用來建立請求

url = "http://ind.ntou.edu.tw/~dada/cgi/Perlsynx.htm"
a = urllib.request.urlopen(url)
print("type : ")
print(type(a))
print("info : ")
print(a.info())

print("geturl : ")
print(a.geturl())
print("getcode : ")
print(a.getcode())
print("getheaders : ")
print(a.getheaders())
print("length : ")
print(a.length)
print("version : ")
print(a.version)

data = a.read()
#data = data.decode('UTF-8')
#print(data)

fd = open("tmp.html", "wb")
fd.write(data)
fd.close()
"""

print("抓取網頁資料, 並存檔")
import urllib
import urllib.request
 
data={}
data['word']='明仁天皇'
 
url_values=urllib.parse.urlencode(data)
url="http://www.baidu.com/s?"
full_url=url+url_values
 
data=urllib.request.urlopen(full_url).read()
#data=data.decode('UTF-8')
print(data)

filename = "__temp\b2.html"
print("抓取網頁資料 並存檔成 : "+filename)
fd = open(filename, "wb")
fd.write(data)
fd.close()



#!/usr/bin/python

print("抓取網頁資料")
from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
#print(html.read())
print(html.read(), 'utf-8')



print("抓取網頁資料222")
#encoding:UTF-8

#百度
#http://ind.ntou.edu.tw/~dada/cgi/Perlsynx.htm

import urllib.request   #用來建立請求

url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
print(data)

fd = open("__temp\bbb.html", "wb")
fd.write(data)
fd.close()

print("讀取遠端純文字檔")
from urllib.request import urlopen

textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
print(textPage.read())





print("讀取遠端純文字檔3333")

import urllib
import urllib.request
 
data={}
data['word']='Jecvay Notes'
 
url_values=urllib.parse.urlencode(data)
url="http://www.baidu.com/s?"
full_url=url+url_values
 
data=urllib.request.urlopen(full_url).read()
data=data.decode('UTF-8')
print(data)


from urllib import parse

url = 'https://www.cnblogs.com/angelyan/'

result = parse.urlparse(url=url,scheme='http',allow_fragments=True)

print(result)
print(result.scheme)






from urllib.parse import urlparse

url = 'https://www.most.gov.tw/folksonomy/list?menu_id=ba3d22f3-96fd-4adf-a078-91a05b8f0166&filter_uid=none&listKeyword=&pageNum=2&pageSize=18&view_mode=listView&subSite=main&l=ch&tagUid='

uc = urlparse(url)
print("NetLoc:", uc.netloc)
print("Path:", uc.path)

q_cmds = uc.query.split('&')
print("Query Commands:")
for cmd in q_cmds:
    print(cmd)


#web = input("請輸入網址：")
web = 'https://www.google.com.tw/'

if web.startswith("http://") or web.startswith("https://"):
    print("輸入的網址格式正確！")
else:
    print("輸入的網址格式錯誤！")


