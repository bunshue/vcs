

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

fd = open("perl.html", "w")
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

filename = "b2.html"
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

fd = open("bbb.html", "wb")
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






