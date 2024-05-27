from bs4 import BeautifulSoup

htmlContent='''
<html>
<head>
<title>碁峰暢銷書籍</title>
<style>
  .blueText{
    color:blue;
  }
</style>
</head>
<body>
<h3 class="blueText">優質好書</h3>
<ul>
  <li><a href="http://books.gotop.com.tw/v_AEL022500">JAVA SE 12基礎必修課</a></li>
  <li><a href="http://books.gotop.com.tw/v_AEL019900">C語言基礎必修課(涵蓋「APCS大學程式設計先修檢測」試題詳解)</a></li>
  <li><a href="http://books.gotop.com.tw/v_AEL022600">Visual C# 2019基礎必修課</a></li>
</ul>
<p><a href="https://www.facebook.com/dtcbook" id="linkDtc" target="_blank">DTC粉專</a></p>
</body>
</html>
'''
bs=BeautifulSoup(htmlContent, 'html.parser')
print(bs.title)
print(bs.title.text)
print()
print(bs.find('h3'))
print(bs.find('h3').text)
print()
print(bs.find('a', {'target':'_blank'}))
print(bs.find('a', {'target':'_blank'}).text)
print()
print(bs.select('.blueText'))
print(bs.select('.blueText')[0].text)
print()
print(bs.select('#linkDtc'))
print(bs.select('#linkDtc')[0].text)
print()               
link1=bs.find_all('a')
for n in range(0, len(link1)):
    print(link1[n].text)
print()    
data=bs.find('ul')
link2=data.find_all('a')
for n in range(0, len(link2)):
    print(link2[n].text)