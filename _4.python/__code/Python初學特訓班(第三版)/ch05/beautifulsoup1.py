import requests
from bs4 import BeautifulSoup

#台灣彩券官網首頁
url = 'http://www.taiwanlottery.com.tw/'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

html_doc = """
<html><head><title>網頁標題</title></head>

<p class="title"><b>文件標題</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,'html.parser') 

print(soup.find('b')) # <b>文件標題</b>

print(soup.find_all('a'))

print(soup.find_all("a", {"class":"sister"}))

data1=soup.find("a", {"href":"http://example.com/elsie"})
print(data1.text) # Elsie

data2=soup.find("a", {"id":"link2"}) 
print(data2.text) # Lacie

data3 = soup.select("#link3") 
print(data3[0].text) # Tillie

print(soup.find_all(['title','a'])) 

data1=soup.find("a", {"id":"link1"}) 
print(data1.get("href")) # http://example.com/elsie
print(data1["href"])     # http://example.com/elsie




import requests
from bs4 import BeautifulSoup

#台灣彩券官網首頁
url = 'http://www.taiwanlottery.com.tw/'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

data1 = soup.select("#rightdown")
#print(data1)

data2 = data1[0].find('div', {'class':'contents_box02'})
#print(data2)

data3 = data2.find_all('div', {'class':'ball_tx'})
print(data3)

