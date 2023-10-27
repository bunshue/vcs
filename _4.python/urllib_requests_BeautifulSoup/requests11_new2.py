import os
import sys
import time
import random

import requests
import re
import bs4


print('------------------------------------------------------------')	#60個

url = 'http://www.mcut.edu.tw'
htmlfile = requests.get(url)
print(type(htmlfile))
if htmlfile.status_code == requests.codes.ok:
    print("取得網頁內容成功")
    print("網頁內容大小 = ", len(htmlfile.text))
    print(htmlfile.text)            # 列印網頁內容
else:
    print("取得網頁內容失敗")


print('------------------------------------------------------------')	#60個

url = 'http://www.mcut.edu.tw'
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    pattern = input("請輸入欲搜尋的字串 : ")    # 讀取字串
# 使用方法1
    if pattern in htmlfile.text:              # 方法1
        print(f"搜尋 {pattern} 成功")
    else:
        print(f"搜尋 {pattern} 失敗")
    # 使用方法2, 如果找到放在串列name內
    name = re.findall(pattern, htmlfile.text)  # 方法2
    if name:
        print(f"{pattern} 出現 {len(name)} 次")
    else:
        print(f"{pattern} 出現 0 次")
else:
    print("網頁下載失敗")

print('------------------------------------------------------------')	#60個

url = 'http://mcut.edu.tw/file_not_existed' # 不存在的內容
try:
    htmlfile = requests.get(url)
    htmlfile.raise_for_status()             # 異常處理
    print("下載成功")
except Exception as err:                    # err是系統內建的錯誤訊息
    print(f"網頁下載失敗: {err}")
print("程式繼續執行 ... ")

print('------------------------------------------------------------')	#60個

url = 'https://www.kingstone.com.tw/' 
htmlfile = requests.get(url)
htmlfile.raise_for_status()

print('------------------------------------------------------------')	#60個

headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }
url = 'https://www.kingstone.com.tw/'
htmlfile = requests.get(url, headers=headers)
htmlfile.raise_for_status()
print("偽裝瀏覽器擷取網路資料成功")

print('------------------------------------------------------------')	#60個

url = 'http://www.tenlong.com.tw'                    # 天瓏書局網址
try:
    htmlfile = requests.get(url)
    print("下載成功")
except Exception as err:                                
    print("網頁下載失敗: %s" % err)
# 儲存網頁內容
fn = 'out21_8.txt'
with open(fn, 'wb') as file_Obj:                     # 以二進位儲存
    for diskStorage in htmlfile.iter_content(10240): # Response物件處理
        size = file_Obj.write(diskStorage)           # Response物件寫入
        print(size)                                  # 列出每次寫入大小
    print("以 %s 儲存網頁HTML檔案成功" % fn)

print('------------------------------------------------------------')	#60個

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

destDir = 'out21_25'
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




print('------------------------------------------------------------')	#60個





