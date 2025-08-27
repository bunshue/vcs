"""
相關抽出

request

bs4

"""

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


""" wait long
print("requests 1")
import requests

r = requests.get("https://tw.yahoo.com/")
print(r.text)

print("------------------------------------------------------------")  # 60個

print("requests 2")
import requests

base_url = "https://zipcloud.ibsnet.co.jp/api/search"

query_parameter = "?zipcode="

zipcode = "1600021"

request_url = base_url + query_parameter + zipcode

request_url

requests.get(request_url).json()


# 有這樣的 API 啊，網址是：https://zipcloud.ibsnet.co.jp/doc/api，請幫我寫出來

print("------------------------------------------------------------")  # 60個

print("requests 3")
import requests

# 郵遞區號
zipcode = "1000001"

# API 端點
api_endpoint = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"

# 進行查詢
response = requests.get(api_endpoint)

# 檢查回應狀態
if response.status_code == 200:
    # 解析回應內容
    data = response.json()

    # 驗證 API 回應狀態
    if data['status'] == 200:
        # 取出第一筆地址資訊
        address_info = data['results'][0]

        # 印出完整郵遞區域
        print(f"{address_info['address1']} {address_info['address2']} {address_info['address3']}")
    else:
        print("API 回應錯誤，訊息：", data['message'])
else:
    print("API 查詢失敗，狀態碼：", response.status_code)


"""
print("------------------------------------------------------------")  # 60個

""" fail
import requests

# 郵遞區號
zipcode = "100-0001"

# API 端點
api_endpoint = "http://your_api_endpoint"

# 你的 API 金鑰
api_key = "your_api_key"

# 設定查詢參數
params = {
    'apikey': api_key,
    'zipcode': zipcode,
}

# 進行查詢
response = requests.get(api_endpoint, params=params)

# 檢查回應狀態
if response.status_code == 200:
    # 解析回應內容
    data = response.json()

    # 印出郵遞區域
    print(data['area'])
else:
    print("API 查詢失敗，狀態碼：", response.status_code)
"""

print("------------------------------------------------------------")  # 60個

"""
print("requests 4")
import requests
api_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
response = requests.get(api_url)
response_dict = response.json()

response_dict.keys()
response_dict["total"]

get_object_url = (
    "https://collectionapi.metmuseum.org/public/collection/v1/objects/435864"
)

object_response = requests.get(get_object_url)

object_response.json()["objectURL"]

object_response.json()["title"]

object_response.json()["primaryImageSmall"]
"""

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

html_str = "<p>Hello World!</p>"
soup = BeautifulSoup(html_str, "lxml")
print(soup)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

soup = BeautifulSoup("<html> Lollipop </html>", "html.parser")

print("------------------------------------------------------------")  # 60個

import requests

from bs4 import BeautifulSoup

html_data = requests.get("http://tw.yahoo.com")

soup = BeautifulSoup(html_data.text, "html.parser")

print(soup.title)

print("------------------------------------------------------------")  # 60個

import requests

from bs4 import BeautifulSoup

game_ranking_html = requests.get(
    "https://www.kamatari.org/blog/2021/best-games-of-2021/"
)

soup = BeautifulSoup(game_ranking_html.text, "html.parser")

for game in soup.findAll("h2"):
    print(game.text)

print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup

game_ranking_html = requests.get(
    "https://www.kamatari.org/blog/2021/best-games-of-2021/"
)
soup = BeautifulSoup(game_ranking_html.text, "html.parser")
for game in soup.findAll("h2"):
    print(game.text)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# htmlparse01

import sys
import requests

'''
print("------------------------------------------------------------")  # 60個

urlstr="http://www.drmaster.com.tw/Publish_Newbook.asp"
response=requests.get(urlstr)

print("網址：%s" %(response.url))
print("狀態：%s" %(response.status_code))
print("表頭：%s" %(response.headers))

"""
Response屬性
content 取得二進位資料 例如可以取得網路圖檔
encoding 取得或設定網頁的編碼模式
headers 取得網頁的表頭資訊
text 取得網頁的所有程式碼
status_code 取得網頁的連線狀態
    200: 請求成功
    400 伺服器無法理解請求
    404伺服器找不到請求資源, 可能是連接的url錯誤
url 取得網頁的網址
"""



print("------------------------------------------------------------")  # 60個

# htmlparse02.py

urlstr="http://www.drmaster.com.tw/Publish_Newbook.asp"
response=requests.get(urlstr)
response.encoding="utf-8"
print("網頁程式碼：%s" %(response.text))

print("------------------------------------------------------------")  # 60個

# htmlparse03.py

# 指定圖片網址
imgUrl='http://www.drmaster.com.tw/Cover/MP22030.png'
imgName=imgUrl.split('/')[-1]
response= requests.get(imgUrl) 
f=open(imgName,'wb')  	# 指定開啟檔案路徑
# 將response.content二進位內容寫入為MP22030.png
f.write(response.content)  			
print('%s 下載完畢' %(imgName))
f.close()


print("------------------------------------------------------------")  # 60個

# htmlparse04.py

from bs4 import BeautifulSoup
# 博碩文化新書網頁
urlstr='http://www.drmaster.com.tw/Publish_Newbook.asp'  
response=requests.get(urlstr)
response.encoding="utf-8"
bs=BeautifulSoup(response.text, 'html.parser')
print(bs.title.text)    # 顯示網頁title標題
listBookName=bs.select('.style2')
count=len(listBookName)
print("共 %d 筆新書記錄" %(count))  # 顯示 '共 20 筆新書記錄'

print('顯示網頁新書書名')
for book in listBookName:
    print(book.text)
    

print("------------------------------------------------------------")  # 60個

# htmlparse05.py

from bs4 import BeautifulSoup

urlstr='http://www.drmaster.com.tw/Publish_Newbook.asp'

response=requests.get(urlstr)
response.encoding="utf-8"
bs=BeautifulSoup(response.text,'html.parser')

listImageUrl=bs.select('td a img')

for link in listImageUrl:
    #if("http" in link.get('src')):
        print(link.get('src'))

'''
print("------------------------------------------------------------")  # 60個

# htmlparse06.py   http讀圖部分還沒好


import os, shutil
from bs4 import BeautifulSoup

# 若程式的路徑有images資料即刪除，否則即建立images
folder = "images"
if os.path.exists(folder):
    shutil.rmtree(folder)
os.mkdir(folder)

urlstr = "http://www.drmaster.com.tw/Publish_Newbook.asp"
response = requests.get(urlstr)
response.encoding = "utf-8"
bs = BeautifulSoup(response.text, "html.parser")
listImageUrl = bs.select("td a img")
# 逐一取得博碩新書圖檔並放入images資料夾下
n = 0
for link in listImageUrl:
    print(link.get("src"))
    imgUrl = link.get("src")
    if "http" in imgUrl:
        imgName = imgUrl.split("/")[-1]
        response = requests.get(imgUrl)
        f = open(folder + "/" + imgName, "wb")  # 指定開啟檔案路徑
        # 將response.content二進位內容寫入指定的圖檔名稱
        f.write(response.content)
        f.close()
        print("%s 下載完成" % (imgName))
        n += 1
print("共下載 %d 張圖檔" % (n))


print("------------------------------------------------------------")  # 60個

# htmlparse07.py

import os, shutil
from bs4 import BeautifulSoup

# 若程式的路徑有images資料即刪除，否則即建立images
folder = "images"
if os.path.exists(folder):
    shutil.rmtree(folder)
os.mkdir(folder)
pageName = "newbook.html"
if os.path.exists(pageName):
    os.remove(pageName)

urlstr = "http://www.drmaster.com.tw/Publish_Newbook.asp"
response = requests.get(urlstr)
response.encoding = "utf-8"
bs = BeautifulSoup(response.text, "html.parser")
listImageUrl = bs.select("td a img")
listImageUrlOk = []
listBookName = bs.select(".style2")
# 逐一取得博碩新書圖檔並放入images資料夾下
for link in listImageUrl:
    imgUrl = link.get("src")
    if "http" in imgUrl:
        imgName = imgUrl.split("/")[-1]
        listImageUrlOk.append(imgName)
        response = requests.get(imgUrl)
        f = open(folder + "/" + imgName, "wb")  # 指定開啟檔案路徑
        # 將response.content二進位內容寫入指定的圖檔名稱
        f.write(response.content)
        f.close()
        print("%s 下載完成" % (imgName))

f = open(pageName, "w", encoding="utf-8")
f.write("<html>\n")
f.write('<meta charset="utf-8">\n')
f.write("<body>\n")
f.write("<table border>\n")
f.write("<tr><td>書號</td><td>圖</td><td>書名</td></tr>\n")
for n in range(len(listBookName)):
    f.write("<tr>\n")
    f.write("<td>%s</td>\n" % (listImageUrlOk[n].split(".")[0]))
    f.write('<td><img src="images/%s" width="100"></td>\n' % (listImageUrlOk[n]))
    f.write("<td>%s</td>\n" % (listBookName[n].text))
    f.write("</tr>\n")
f.write("</table>\n")
f.write("</body>\n")
f.write("</html>\n")
f.close()

# 開啟 os.system(pageName)

print("%s 網頁建置成功" % (pageName))

print("------------------------------------------------------------")  # 60個


from bs4 import BeautifulSoup

htmlContent = """
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
"""
bs = BeautifulSoup(htmlContent, "html.parser")
print(bs.title)
print(bs.title.text)
print()
print(bs.find("h3"))
print(bs.find("h3").text)
print()
print(bs.find("a", {"target": "_blank"}))
print(bs.find("a", {"target": "_blank"}).text)
print()
print(bs.select(".blueText"))
print(bs.select(".blueText")[0].text)
print()
print(bs.select("#linkDtc"))
print(bs.select("#linkDtc")[0].text)
print()
link1 = bs.find_all("a")
for n in range(0, len(link1)):
    print(link1[n].text)
print()
data = bs.find("ul")
link2 = data.find_all("a")
for n in range(0, len(link2)):
    print(link2[n].text)


print("------------------------------------------------------------")  # 60個


# 檔案 : D:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch14\code\htmlparse03.py

import requests
from bs4 import BeautifulSoup

urlstr = "http://www.drmaster.com.tw/Publish_Newbook.asp"

responseObj = requests.get(urlstr)
responseObj.encoding = "utf-8"
bs = BeautifulSoup(responseObj.text, "html.parser")
print(bs.title.text)
data = bs.select(".style2")
count = len(data)
print("共 %d 筆新書記錄" % (count))

for book in data:
    print(book.text)


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch14\code\htmlparse04.py

import requests

# 指定圖片網址
img_url = "http://www.drmaster.com.tw/Cover/MP22030.png"
imgName = img_url.split("/")[-1]
response = requests.get(img_url)
f = open(imgName, "wb")  # 指定開啟檔案路徑
# 將response.content二進位內容寫入為MP22030.png
f.write(response.content)
print("%s 下載完畢" % (imgName))
f.close()


print("------------------------------------------------------------")  # 60個

# 檔案 : D:\_git\vcs\_4.python\__code\Python全面攻略_從程式新人到開發設計的快速學習\ch14\code\htmlparse05.py

import requests
from bs4 import BeautifulSoup

urlstr = "http://www.drmaster.com.tw/Publish_Newbook.asp"

responseObj = requests.get(urlstr)
responseObj.encoding = "utf-8"
bs = BeautifulSoup(responseObj.text, "html.parser")

data = bs.select("td a img")

for book in data:
    if "http" in book.get("src"):
        print(book.get("src"))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
