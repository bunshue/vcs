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
sp = BeautifulSoup(html_doc,'html.parser') 

print(sp.find('b')) # <b>文件標題</b>

print(sp.find_all('a'))

print(sp.find_all("a", {"class":"sister"}))

data1=sp.find("a", {"href":"http://example.com/elsie"})
print(data1.text) # Elsie

data2=sp.find("a", {"id":"link2"}) 
print(data2.text) # Lacie

data3 = sp.select("#link3") 
print(data3[0].text) # Tillie

print(sp.find_all(['title','a'])) 

data1=sp.find("a", {"id":"link1"}) 
print(data1.get("href")) # http://example.com/elsie
print(data1["href"])     # http://example.com/elsie
