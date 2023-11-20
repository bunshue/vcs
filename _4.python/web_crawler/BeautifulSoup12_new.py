import sys
import requests
from bs4 import BeautifulSoup

print('------------------------------------------------------------')	#60個

"""
req=requests.get('http://www.powenko.com/wordpress/')
print(req.text.encode('utf-8'))
soup=BeautifulSoup(req.text.encode('utf-8'), "html.parser")
print(soup.title)
print(soup.title.string)
print(soup.p)
print(soup.a)
print(soup.find_all('a'))
"""

print('------------------------------------------------------------')	#60個

text1="""
<head>
    <title>柯博文老師</title>
</head>
<body>
    <p class="title"><b>The test</b></p>
    <a class="redcolor" href="http://powenko.com/1.html" id="link1">test1</a>
    <a class="bluecolor" href="http://powenko.com/2.html" id="link2">test2</a>
    <a class="redcolor" id="link3" href="http://powenko.com/3.html" id="link3">test3</a>
</body>
"""
soup=BeautifulSoup(text1, "html.parser")
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p['class'])
print(soup.a)
print(soup.find_all('a'))
for link in soup.find_all('a'):
	print(link.get('href'))
print(soup.select('a'))
print(soup.select('.redcolor'))   # class="redcolor"
print(soup.select('#link3'))     # id="link3"
for link in soup.select('a'):
        print(link.string)

print('------------------------------------------------------------')	#60個

""" NG

req=requests.get("http://www.powenko.com/wordpress")
soup=BeautifulSoup(req.text.encode('utf-8'), "html.parser")
largefeaturepowenA2=soup.select('.largefeaturepowenA2')
largefeature0=largefeaturepowenA2[0]
for area in largefeature0.select('.area'):	
  # print(area.select('a')[1].text)
  t1=area.select('a')
  print(area.select('a')[1].contents[0])

print('------------------------------------------------------------')	#60個

"""

req=requests.get("http://news.baidu.com/tech")
soup=BeautifulSoup(req.text.encode('utf-8'), "html.parser")
largefeaturepowenA2=soup.select('.fb-list')
largefeature0=largefeaturepowenA2[0]
print(largefeature0)
for area in largefeature0.select('li'):
  t1=area.select('a')
  print(area.select('a')[0].contents[0])
  

print('------------------------------------------------------------')	#60個

req=requests.get("https://feebee.com.tw/s/?q=raspberry+pi+3")
soup=BeautifulSoup(req.text.encode('utf-8'), "html.parser")

for line in soup.select('.items'):
   print(line.select('.large')[0].text)
   print(line.select('.ellipsis')[0].text)
   print(line.select('a')[0].get("href"))

print('------------------------------------------------------------')	#60個

req=requests.get("https://www.chinatimes.com/?chdtv")
soup=BeautifulSoup(req.text.encode('utf-8'), "html.parser")

for listRight in soup.select('.focus-news'):
   for line in listRight.select('.title'):
     print(line.select('a')[0].text)

print('------------------------------------------------------------')	#60個

req=requests.get("https://goodinfo.tw/StockInfo/StockDividendSchedule.asp?STOCK_ID=2892")
soup=BeautifulSoup(req.text.encode('utf-8'), "html.parser")

for listRight in soup.select('.focus-news'):
   for line in listRight.select('.title'):
     print(line.select('a')[0].text)

print('------------------------------------------------------------')	#60個

