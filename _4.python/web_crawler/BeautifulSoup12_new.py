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


print('------------------------------------------------------------')	#60個

import bs4

htmlFile = requests.get('https://deepmind.com.tw')
objSoup = bs4.BeautifulSoup(htmlFile.text, 'lxml')
print("列印BeautifulSoup物件資料型態 ", type(objSoup))

print('------------------------------------------------------------')	#60個

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
print("列印BeautifulSoup物件資料型態 ", type(objSoup))

print('------------------------------------------------------------')	#60個

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
print("物件類型  = ", type(objSoup.title))
print("列印title = ", objSoup.title)

print('------------------------------------------------------------')	#60個

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
print("列印title = ", objSoup.title)
print("title內容 = ", objSoup.title.text)

print('------------------------------------------------------------')	#60個

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
objTag = objSoup.find('h1')
print("資料型態       = ", type(objTag))
print("列印Tag        = ", objTag)
print("Text屬性內容   = ", objTag.text)
print("String屬性內容 = ", objTag.string)

print('------------------------------------------------------------')	#60個

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
objTag = objSoup.find_all('h1')
print("資料型態    = ", type(objTag))     # 列印資料型態
print("列印Tag串列 = ", objTag)           # 列印串列
print("以下是列印串列元素 : ")
for data in objTag:                       # 列印串列元素內容
    print(data.text)

print('------------------------------------------------------------')	#60個

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
objTag = objSoup.find_all('h1', limit=2)
for data in objTag:                       # 列印串列元素內容
    print(data.text)

print('------------------------------------------------------------')	#60個

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
objTag = objSoup.find_all('h1')
print("資料型態    = ", type(objTag))     # 列印資料型態
print("列印Tag串列 = ", objTag)           # 列印串列
print("\n使用Text屬性列印串列元素 : ")
for data in objTag:                       # 列印串列元素內容
    print(data.text)
print("\n使用getText()方法列印串列元素 : ")
for data in objTag:
    print(data.getText())

print('------------------------------------------------------------')	#60個

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
objTag = objSoup.find(id='author')
print(objTag)
print(objTag.text)

print('------------------------------------------------------------')	#60個

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
objTag = objSoup.find_all(id='content')
for tag in objTag:
    print(tag)
    print(tag.text)

print('------------------------------------------------------------')	#60個

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
objTag = objSoup.select('#author')
print("資料型態     = ", type(objTag))          # 列印資料型態
print("串列長度     = ", len(objTag))           # 列印串列長度
print("元素資料型態 = ", type(objTag[0]))       # 列印元素資料型態
print("元素內容     = ", objTag[0].getText())   # 列印元素內容

print('------------------------------------------------------------')	#60個

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
objTag = objSoup.select('#author')
print("列出串列元素的資料型態    = ", type(objTag[0]))
print(objTag[0])
print("列出str()轉換過的資料型態 = ", type(str(objTag[0])))
print(str(objTag[0]))

print('------------------------------------------------------------')	#60個

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
objTag = objSoup.select('#author')
print(str(objTag[0].attrs))

print('------------------------------------------------------------')	#60個

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
pObjTag = objSoup.select('p')
print("含<p>標籤的串列長度 = ", len(pObjTag))
for pObj in pObjTag:
    print(str(pObjTag))         # 內部有子標籤<strong>字串
    print(pObj.getText())       # 沒有子標籤
    print(pObj.text)            # 沒有子標籤

print('------------------------------------------------------------')	#60個

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
imgTag = objSoup.select('img')
print("含<img>標籤的串列長度 = ", len(imgTag))
for img in imgTag:              
    print(img)   

print('------------------------------------------------------------')	#60個

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
imgTag = objSoup.select('img')
print("含<img>標籤的串列長度 = ", len(imgTag))
for img in imgTag:              
    print("列印標籤串列 = ", img)
    print("列印圖檔     = ", img.get('src'))
    print("列印圖檔     = ", img['src'])
print('------------------------------------------------------------')	#60個

url = 'http://www.xzw.com/fortune/'
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')      # 取得物件
constellation = objSoup.find('div', id='list')
cons = constellation.find('div', 'alb').find_all('div')

pict_url = 'http://www.xzw.com'
photos = []
for con in cons:
    pict = con.a.img['src']
    photos.append(pict_url+pict)

destDir = 'tmp_dir'
if os.path.exists(destDir) == False:            # 如果沒有此資料夾就建立
    os.mkdir(destDir)
print("搜尋到的圖片數量 = ", len(photos))       # 列出搜尋到的圖片數量
for photo in photos:                            # 迴圈下載圖片與儲存
    picture = requests.get(photo)               # 下載圖片
    picture.raise_for_status()                  # 驗證圖片是否下載成功
    print("%s 圖片下載成功" % photo)
# 先開啟檔案, 再儲存圖片
    pictFile = open(os.path.join(destDir, os.path.basename(photo)), 'wb')
    for diskStorage in picture.iter_content(10240):
        pictFile.write(diskStorage)
    pictFile.close()                            # 關閉檔案

print('------------------------------------------------------------')	#60個

url = 'http://www.taiwanlottery.com.tw'
html = requests.get(url)
print("網頁下載中 ...")
html.raise_for_status()                         # 驗證網頁是否下載成功                      
print("網頁下載完成")

objSoup = bs4.BeautifulSoup(html.text, 'lxml')  # 建立BeautifulSoup物件

dataTag = objSoup.select('.contents_box02')     # 尋找class是contents_box02
print("串列長度", len(dataTag))
for i in range(len(dataTag)):                   # 列出含contents_box02的串列                 
    print(dataTag[i])
        
# 找尋開出順序與大小順序的球
balls = dataTag[0].find_all('div', {'class':'ball_tx ball_green'})
print("開出順序 : ", end='')
for i in range(6):                              # 前6球是開出順序
    print(balls[i].text, end='   ')

print("\n大小順序 : ", end='')
for i in range(6,len(balls)):                   # 第7球以後是大小順序
    print(balls[i].text, end='   ')

# 找出第二區的紅球                   
redball = dataTag[0].find_all('div', {'class':'ball_red'})
print("\n第二區   :", redball[0].text)

print('------------------------------------------------------------')	#60個

url = 'http://www.taiwanlottery.com.tw'
html = requests.get(url)

objSoup = bs4.BeautifulSoup(html.text, 'lxml')      # 建立BeautifulSoup物件

dataTag = objSoup.select('.contents_box02')         # 尋找class是contents_box02
        
# 找尋開出順序與大小順序的球
balls = dataTag[2].find_all('div', {'class':'ball_tx ball_yellow'})
print("開出順序 : ", end='')
for i in range(6):                                  # 前6球是開出順序
    print(balls[i].text, end='   ')

print("\n大小順序 : ", end='')
for i in range(6,len(balls)):                       # 第7球以後是大小順序
    print(balls[i].text, end='   ')

# 找出第二區的紅球                   
redball = dataTag[2].find_all('div', {'class':'ball_red'})
print("\n特別號   :", redball[0].text)

print('------------------------------------------------------------')	#60個



from bs4 import BeautifulSoup

soup = BeautifulSoup("<html> Lollipop </html>", "html.parser")

print('------------------------------------------------------------')	#60個

import requests

from bs4 import BeautifulSoup

html_data = requests.get('http://tw.yahoo.com')

soup = BeautifulSoup(html_data.text, "html.parser")

print(soup.title)

print('------------------------------------------------------------')	#60個

import requests

from bs4 import BeautifulSoup

yahoo_news_xml = requests.get('https://tw.news.yahoo.com/rss/technology')

soup = BeautifulSoup(yahoo_news_xml.text, "html.parser")

type(soup)

soup.findAll('item')

print('------------------------------------------------------------')	#60個

for news in soup.findAll('item'):

	print(news.title)
	
print('------------------------------------------------------------')	#60個

import requests

from bs4 import BeautifulSoup

game_raking_html = requests.get('https://acg.gamer.com.tw/billboard.php?t=2&p=Android')

game_raking_html.encoding = 'UTF-8'

soup = BeautifulSoup(game_raking_html.text, "html.parser")

soup.find(class_='ACG-mainbox1').find(class_='ACG-maintitle').find('a').string

for game in soup.findAll(class_='ACG-mainbox1'):
	print(game.find(class_='ACG-mainumber').string + ' ' + game.find(class_='ACG-maintitle').find('a').string)

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個




print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

