#以BeautifulSoup套件進行網頁解析
from bs4 import BeautifulSoup

content="""
<!DOCTYPE html>
<html lang="zh-TW">
<head>
<title>BeautifulSoup套件進行網頁解析</title>
<meta charset="utf-8">
</head>
<body>
<h1 style="background-color:red; color:white; font-family:Segoe Script; border:3px #000000 solid;">Python is funny</h1>
Python簡單易學又有趣
<h1 style="color:rgb(255, 99, 71);">程式設計網站推薦</h1>
<a href="https://www.python.org/">Python官方網站</a>
</body>
</html>
"""

bs = BeautifulSoup(content,'html.parser') 
print('網頁標題屬性：') #網頁標題屬性
print(bs.title) #網頁標題屬性
print('--------------------------------------------------------')
print('網頁html語法區塊：') 
print(bs.find('html')) #<html>標籤
print('--------------------------------------------------------')
print('網頁表頭範圍：') 
print(bs.find('head')) #<head>標籤
print('--------------------------------------------------------')
print('網頁身體範圍：') 
print(bs.find('body')) #<body>標籤
print('--------------------------------------------------------')
print('第1個超連結：')
print(bs.find("a",{"href":"https://www.python.org/"}))
print('--------------------------------------------------------')

