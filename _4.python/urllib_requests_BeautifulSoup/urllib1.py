import urllib
import urllib.request   #用來建立請求

print('讀取遠端html檔或純文字檔')
url = 'http://pythonscraping.com/pages/page1.html'
#url = 'http://www.pythonscraping.com/pages/warandpeace/chapter1.txt'
html = urllib.request.urlopen(url)
html_data = html.read()
print(html_data)
print('OK')

print('讀取遠端純文字檔2')
#encoding:Big5
#Perl的基本語法
#http://ind.ntou.edu.tw/~dada/cgi/Perlsynx.htm

print('讀取遠端html檔1')
url = 'http://ind.ntou.edu.tw/~dada/cgi/Perlsynx.htm'
html = urllib.request.urlopen(url).read()
html_data = html.decode('Big5')      #將bytes轉成str
print(html_data)
print('OK')

print('資料寫出到本地檔案')
filename = 'C:/______test_files3/perl.html'
fd = open(filename, "w")
fd.write(html_data)
fd.close()
print('抓取網頁資料 並存檔成 : ' + filename)
print('OK')

print("抓取網頁資料, 並存檔")
data={}
data['word']='明仁天皇'
 
url_values = urllib.parse.urlencode(data)
url = 'http://www.baidu.com/s?'
full_url = url + url_values
 
data = urllib.request.urlopen(full_url).read()
#data=data.decode('UTF-8')
print(data)
print('OK')

print('資料寫出到本地檔案')
filename = 'C:/______test_files3/b2.html'
fd = open(filename, "wb")
fd.write(data)
fd.close()
print('抓取網頁資料 並存檔成 : ' + filename)
print('OK')

print('抓取網頁資料 1')
url = 'http://pythonscraping.com/pages/page1.html'
html = urllib.request.urlopen(url)
html_data = html.read()
print(html_data, 'utf-8')
print('OK')

print('抓取網頁資料 2')
#encoding:UTF-8

#百度
#http://ind.ntou.edu.tw/~dada/cgi/Perlsynx.htm
url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
print(data)

print('資料寫出到本地檔案')
filename = 'C:/______test_files3/bbb.html'
fd = open(filename, "wb")
fd.write(data)
fd.close()
print('抓取網頁資料 並存檔成 : ' + filename)
print('OK')

print('讀取遠端純文字檔3')
data={}
data['word']='Jecvay Notes'
 
url_values=urllib.parse.urlencode(data)
url="http://www.baidu.com/s?"
full_url=url+url_values
 
data=urllib.request.urlopen(full_url).read()
data=data.decode('UTF-8')
print(data)
print('OK')

print('抓取網頁資料 4')

url = 'https://www.cnblogs.com/angelyan/'
result = urllib.parse.urlparse(url = url, scheme = 'http', allow_fragments = True)
print(result)
print(result.scheme)
print('OK')

print('抓取網頁資料 5')
url = 'https://www.most.gov.tw/folksonomy/list?menu_id=ba3d22f3-96fd-4adf-a078-91a05b8f0166&filter_uid=none&listKeyword=&pageNum=2&pageSize=18&view_mode=listView&subSite=main&l=ch&tagUid='
uc = urllib.parse.urlparse(url)
print("NetLoc:", uc.netloc)
print("Path:", uc.path)

q_cmds = uc.query.split('&')
print("Query Commands:")
for cmd in q_cmds:
    print(cmd)

print('抓取網頁資料 OK')

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
print('資料寫出到本地檔案')
filename = 'C:/______test_files3/tmp.html'
fd = open(filename, "wb")
fd.write(data)
fd.close()
print('抓取網頁資料 並存檔成 : ' + filename)


'''
import requests

url = 'https://httpbin.org/get'
headers = {'Content-Type': 'text/html'}

html_data = requests.get(url, headers=headers)

print(html_data.text)
'''

import ssl
import requests
from urllib.request import urlopen
import urllib.request   #用來建立請求
from bs4 import BeautifulSoup

context = ssl._create_unverified_context()
url = 'https://movies.yahoo.com.tw/chart.html'
html_data = urllib.request.urlopen(url).read()
html_data = html_data.decode('utf-8')
print(html_data)
soup = BeautifulSoup(html_data, 'html.parser')
print(soup.prettify())






print('作業完成')


