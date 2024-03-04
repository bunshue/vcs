"""
相關抽出

網頁抓取處理相關


"""

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


import requests

addr = "https://www.books.com.tw/"
res = requests.get(addr)

# 檢查狀態碼
if res.status_code == 200:
    res.encoding = "utf-8"
    print(res.text)
else:
    print(res.status_code)

print("------------------------------------------------------------")  # 60個

import urllib.request

# 設定欲請求的網址
addr = "http://www.grandtech.info/"
# 以with/as敘述來取得網址，離開之後也能釋放資源
with urllib.request.urlopen(addr) as response:
    print("網頁網址", response.geturl())
    print("伺服器狀態碼", response.getcode())
    print("網頁表頭", response.getheaders())
    zct_str = response.read().decode("UTF-8")
print("將網頁資料轉成字串格式", zct_str)

print("------------------------------------------------------------")  # 60個

from urllib.parse import urlparse

addr = "https://www.zct.com.tw/hot_sale.php?act=goods&hash=5717321f978f1"

result = urlparse(addr)
print("回傳的 ParseResult 物件:")
print(result)
print("通訊協定:" + result.scheme)
print("網站網址:", result.netloc)
print("路徑:", result.path)
print("查詢字串:", result.query)

print("------------------------------------------------------------")  # 60個

# 政府資料開放平臺 XML格式資料擷取與應用

url = "https://apiservice.mol.gov.tw/OdService/download/A17000000J-000007-yrg"

import urllib.request as ur

with ur.urlopen(url) as response:
    get_xml = response.read()

from bs4 import BeautifulSoup

data = BeautifulSoup(get_xml, "xml")
HandlingUnit = data.find_all("辦理單位")
ContactPerson = data.find_all("聯絡人")
DuringTraining = data.find_all("訓練期間")
ContactNumber = data.find_all("聯絡電話")
CourseTitle = data.find_all("課程名稱")

csv_str = ""
for i in range(0, len(HandlingUnit)):
    csv_str += "{},{},{},{},{}\n".format(
        HandlingUnit[i].get_text(),
        ContactPerson[i].get_text(),
        ContactNumber[i].get_text(),
        DuringTraining[i].get_text(),
        CourseTitle[i].get_text(),
    )

with open("course_xml.csv", "w") as f:
    story = f.write(csv_str)  # 寫入檔案

print("XML格式資料擷取與應用,已將資料寫入course_xml.csv")

print("------------------------------------------------------------")  # 60個

# 以BeautifulSoup套件進行網頁解析
from bs4 import BeautifulSoup

content = """
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
bs = BeautifulSoup(content, "html.parser")
print("網頁標題屬性：")  # 網頁標題屬性
print(bs.title)  # 網頁標題屬性
print("--------------------------------------------------------")
print("網頁html語法區塊：")
print(bs.find("html"))  # <html>標籤
print("--------------------------------------------------------")
print("網頁表頭範圍：")
print(bs.find("head"))  # <head>標籤
print("--------------------------------------------------------")
print("網頁身體範圍：")
print(bs.find("body"))  # <body>標籤
print("--------------------------------------------------------")
print("第1個超連結：")
print(bs.find("a", {"href": "https://www.python.org/"}))
print("--------------------------------------------------------")

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup
import requests

addr = "https://tw.stock.yahoo.com/s/list.php?\
c=%A8%E4%A5%A6%B9q%A4l&rr=0.84235400%201556957344"

# 取得網頁原始程式碼
res = requests.get(addr).text
# 以html.parser解析程式解析程式碼
bs = BeautifulSoup(res, "html.parser")
# 以<tr>並配合屬性取得表格中每列內容
rows = bs.find_all("tr", {"height": "30"})

# 印出要查詢資料各欄位名稱
print("代號 名稱  時間  成交  買進   賣出  漲跌   張數   昨收   開盤  最高  最低")
# 讀取每列的內容，找出<td>
for row in rows:
    if row.find("td"):
        # 屬性stripped_strings去餘每欄中字串的空白符號
        cols = [item for item in row.stripped_strings]
        # 讀取List物件的元素
        for item in range(0, len(cols)):
            print(cols[item], end=" ")
        print()  # 換行

print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup

# 獲取網頁內容
game_ranking_html = requests.get("https://acg.gamer.com.tw/billboard.php?t=2&p=iOS")

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(game_ranking_html.text, "html.parser")

# 找到所有遊戲排名標題的標籤
games = soup.find_all("div", {"class": "APP-LI-NAME"})

# 顯示遊戲排名標題
for i, game in enumerate(games, 1):
    print(f"{i}. {game.text.strip()}")

print("------------------------------------------------------------")  # 60個


""" many
import requests
import os
import threading

# XKCD 漫畫的基本 URL
base_url = 'https://xkcd.com/'

# 定義下載漫畫的函數
def download_xkcd(start_comic, end_comic):
    for comic_number in range(start_comic, end_comic):
        # 跳過編號為 0 的漫畫，因為它不存在
        if comic_number == 0:
            continue

        url = f'{base_url}{comic_number}/info.0.json'   # 建立API URL來獲取漫畫資訊
        try:
            response = requests.get(url)
            response.raise_for_status()                 # 確保請求成功

            comic_json = response.json()
            comic_url = comic_json['img']               # 從JSON響應中提取圖片 URL
            print(f'\n圖片下載中 : {comic_url}...')

            # 向圖片 URL 發送請求並下載圖片
            res = requests.get(comic_url)
            res.raise_for_status()

            # 保存圖片到本地資料夾
            with open(os.path.join('xkcd_comics', os.path.basename(comic_url)), 'wb') as image_file:
                for chunk in res.iter_content(100000):
                    image_file.write(chunk)             # 寫入圖片數據
        except requests.exceptions.HTTPError as err:
            print(f'Failed to download comic {comic_number}: {err}')  # 輸出錯誤訊息

# 建立並啟動多個執行緒
thread_count = 10                                       # 執行緒的數量
comic_range = 10                                        # 每個執行緒負責下載的漫畫數量

# 如果不存在, 建立一個目錄來存儲下載的漫畫
if not os.path.exists('xkcd_comics'):
    os.makedirs('xkcd_comics')

# 建立執行緒並將它們添加到執行緒串列表
threads = []
for i in range(1, thread_count * comic_range, comic_range):         # 漫畫編號從 1 開始
    start = i
    end = i + comic_range
    thread = threading.Thread(target=download_xkcd, args=(start, end))
    threads.append(thread)
    thread.start()                                      # 啟動執行緒

# 等待所有執行緒完成
for thread in threads:
    thread.join()

print('漫畫圖片下載完成')

"""

print("------------------------------------------------------------")  # 60個


import requests

url = "https://www.books.com.tw/web/sys_cebbotm/cebook/1003/?loc=P_0001_2_003"  # 博客來網址
response = requests.get(url)
# 印出<class 'requests.models.Response'>，表示response為Response物件
print("物件型別：", type(response))
print("網址：", response.url)
print("表頭資訊：", response.headers)
print("連線狀態：", response.status_code)
print("網頁編碼模式：", response.encoding)

print("------------------------------------------------------------")  # 60個

import requests

# 指定圖片網址
img_url = "http://www.gotop.com.tw/Waweb2004/WawebImages/BookXL/AEL022200.jpg"
response = requests.get(img_url)
f = open("tmp_bootstrap.jpg", "wb")  # 指定開啟檔案路徑
# 將response.content二進位內容寫入檔案
f.write(response.content)
print("下載完畢")
f.close()

print("------------------------------------------------------------")  # 60個

"""
import requests
from bs4 import BeautifulSoup
url='http://www.dtc-tech.com.tw' #大才全資訊科技股有限公司首頁
response=requests.get(url)
bs=BeautifulSoup(response.text,'lxml')  	#傳回bs物件可解析網頁
print(bs.find('title'))                 	#傳回網頁含<title>~</title>
print(bs.find('title').text)            	#傳回網頁<title>標籤內的資料
print(bs.find('h1'))                    	#傳回第一個符合<h1>資料
					                          #若傳回None表示該網頁沒有<h1>標籤
"""

print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup

# 博客來寵物電子書
url = "https://www.books.com.tw/web/sys_cebbotm/cebook/1003/?loc=P_0001_2_003"
response = requests.get(url)  # 使用requests的get()方法傳回可擷取網頁資訊response物件
response.encoding = "utf-8"  # 設定編碼模式避免亂碼
# 使用BeautifulSoup()函式取得解析網頁的BeautifulSoup物件bs
bs = BeautifulSoup(response.text, "lxml")
listAll = bs.find_all("div", class_="item")  # 取得<div class="item">標籤的內容
for book in listAll:  # 將資料利用迴圈依序解析
    listClass = book.get("class")  # 傳回目前標籤的類別資訊
    if len(listClass) == 2:  # ['item', 'clearfix']總數為2，即目前有兩個類別
        if listClass[1] == "clearfix":  # 遇到clearfix類別時，跳出本次迴圈
            continue
    print((book.find("h4").find("a").text))  # 搜尋第一個<h4>內的第一個<a>標籤，即書名


print("------------------------------------------------------------")  # 60個


import requests
from bs4 import BeautifulSoup

# 博客來寵物電子書
url = "https://www.books.com.tw/web/sys_cebbotm/cebook/1003/?loc=P_0001_2_003"
response = requests.get(url)  # 使用requests的get()方法傳回可擷取網頁資訊response物件
response.encoding = "utf-8"  # 設定編碼模式避免亂碼
# 使用BeautifulSoup()函式取得解析網頁的BeautifulSoup物件bs
bs = BeautifulSoup(response.text, "lxml")
listName = bs.select("div.item>div.msg>h4>a")  # 根據路徑擷取<a>標籤，並指定給listName串列
listPrice = bs.select("li.set2")  # 取得套用set2類別的<li>標籤，並指定給listPrice串列
for i in range(0, len(listName)):  # 使用迴圈逐一印出書名與書價
    print("%s  %s" % (listName[i].text, listPrice[i].text))


print("------------------------------------------------------------")  # 60個


# html to csv

# 引用相關套件
import requests
import csv
from bs4 import BeautifulSoup

# 指定url變數為「博客來電子寵物書」網頁的網址
url = "https://www.books.com.tw/web/sys_cebbotm/cebook/1003/?loc=P_0001_2_003"
# 建立取得網頁資訊的Response物件，物件名稱為response
response = requests.get(url)
# 建立解析網頁的BeautifulSoup物件，物件名稱為bs
bs = BeautifulSoup(response.text, "lxml")
# 分別取的商品名稱以及價格標籤，並指定給對應串列
listName = bs.select("div.item>div.msg>h4>a")
listPress = bs.select("li.info>span>a")
listPrice = bs.select("li.set2")
# 將listName與listPirce串列的資料依序存入booklist.csv檔中
f = open("tmp_booklist.csv", "w", encoding="utf-8-sig", newline="")
write = csv.writer(f)
write.writerow(["書名", "出版社", "價格"])
for i in range(0, len(listName)):
    # 分析價格內容，只擷取數字部分
    Price = listPrice[i].text.split("：")[1].split("元")[0].split("折")[-1]
    # 使用text屬性，將標籤內的資料寫入csv檔中
    write.writerow([listName[i].text, listPress[i].text, Price])
    print(listName[i].text, listPress[i].text, Price)
f.close()


print("------------------------------------------------------------")  # 60個

""" OK many
#抓 博客來電子寵物書 圖片 OK

# 引用相關套件
import requests
from bs4 import BeautifulSoup

# 指定url變數為「博客來電子寵物書」網頁的網址
url='https://www.books.com.tw/web/sys_cebbotm/cebook/1003/?loc=P_0001_2_003'
response=requests.get(url)# 建立取得網頁資訊的Response物件，物件名稱為response
response.encoding = 'utf-8'    #設定編碼模式避免亂碼
#使用BeautifulSoup()函式取得解析網頁的BeautifulSoup物件bs
bs=BeautifulSoup(response.text,'lxml')
Img=bs.select('div.item>a>img')  #擷取有圖片網址的<img>標籤
for link in Img:     
    #使用split()方法解析網址
    src=link.get('src') 
    ImgUrl=src.split('=')[1].split('&')[0]
    #網址用'/'分隔取最後一筆資料 => *.jpg
    ImgName=ImgUrl.split('/')[-1]
    print('圖片網址:', ImgUrl)
    print('圖片檔名:', ImgName)

    try:  #下載圖片
        Rpimg=requests.get(ImgUrl) #建立下載圖片的Response物件Rpimg
        f=open((ImgName),'wb')    #開啟圖片檔案                    
        f.write(Rpimg.content)     #下載圖片
        f.close()
        print(ImgName,'下載完畢')
    except:
        print('下載失敗')
        f.close()

print('執行完畢')
"""

print("------------------------------------------------------------")  # 60個

print("口罩資料")

import requests, csv, os


def fnDownloadCsv():  # 下載CSV檔
    print("口罩資料下載中...")
    # 健保特約機構口罩剩餘數量明細清單資料來源的Url
    maskdataUrl = "https://data.nhi.gov.tw/resource/mask/maskdata.csv"
    # 下載健保特約機構口罩剩餘數量明細清單資料並儲存成Masks.csv
    r = requests.get(maskdataUrl)
    f = open("tmp_Masks.csv", "wb")
    f.write(r.content)
    f.close()
    print("口罩資料下載完成...")


def fnShowResult():
    # 將輸入地址有 '台' 的字換成 '臺'
    # search=str(input('請搜尋藥局地址:'))
    search = "深坑區"
    search = search.replace("台", "臺")
    print("=" * 50)
    # 開啟Masks.csv資料檔，並將口罩資料轉成data字典物件
    f = open("tmp_Masks.csv", encoding="utf-8")
    data = csv.DictReader(f)
    # 若有 tmp_Masks.html 網頁即刪除
    if os.path.exists("tmp_Masks.html"):
        os.remove("tmp_Masks.html")
    # 使用附加模式建立tmp_Masks.html網頁
    fH = open("tmp_Masks.html", "a", encoding="utf-8")
    # 寫入網頁表格標題
    fH.write('<meta charset="utf-8" /><table border="1">')
    fH.write(
        "<tr>\
                 <th>醫事機構名稱</th>\
                 <th>醫事機構地址</th>\
                 <th>醫事機構電話</th>\
                 <th>成人口罩剩餘數</th>\
                 <th>兒童口罩剩餘數</th>\
                 <th>路線規劃</th>\
              </tr>"
    )
    # 印出查詢的健保特約機構口罩剩餘數量明細資料
    for row in data:
        address = row["醫事機構地址"]
        # 判斷地址與搜尋地址是否吻合
        if search in address:
            # 不顯示成人以及兒童口罩賣完的診所
            if row["成人口罩剩餘數"] != 0 and row["兒童口罩剩餘數"] != 0:
                print("藥局名稱:", row["醫事機構名稱"])
                print("藥局地址:", row["醫事機構地址"])
                print("藥局電話:", row["醫事機構電話"])
                print("成人口罩剩餘數:", row["成人口罩剩餘數"])
                print("兒童口罩剩餘數:", row["兒童口罩剩餘數"])
                print("=" * 50)
                # 將資料寫入 tmp_Masks.html
                fH.write("<tr>")
                fH.write("<td>" + row["醫事機構名稱"] + "</td>")
                fH.write("<td>" + row["醫事機構地址"] + "</td>")
                fH.write("<td>" + row["醫事機構電話"] + "</td>")
                fH.write("<td>" + row["成人口罩剩餘數"] + "</td>")
                fH.write("<td>" + row["兒童口罩剩餘數"] + "</td>")
                fH.write(
                    '<td><a href="https://www.google.com/'
                    + "maps/search/"
                    + row["醫事機構地址"]
                    + '">路線規劃</a></td>'
                )
                fH.write("</tr>")
    fH.write("</table>")
    # 關閉檔案
    fH.close()
    f.close()
    # os.system('tmp_Masks.html')    # 開啟網頁


fnDownloadCsv()  # 呼叫fnDownLoadCsv()函式下載健保特約機構口罩剩餘數量明細清單
fnShowResult()  # 印出查詢的健保特約機構口罩剩餘數量明細資料並建立成網頁檔


print("------------------------------------------------------------")  # 60個

''' OKmany

#下載很多圖檔  OK many

import requests, json, os, shutil, sys  # 引用相關套件

# 將農村地方美食小吃特色料理的JSON資料集網址指定給url變數
url='https://data.coa.gov.tw/Service/OpenData/ODwsv/ODwsvTravelFood.aspx'
# 建立取得網頁資訊的Response物件，物件名稱為rp
rp=requests.get(url)
# 設定編碼模式避免亂碼
rp.encoding="utf_8_sig"
# 使用json套件的loads()方法將擷取到的資料集轉成all_list串列
all_list=json.loads(rp.text)

print(type(all_list))

print(len(all_list))

print(all_list)

print("------------------------------------------------------------")  # 60個
for i in range(5):
    #print(all_list[i])
    
    #print('ID :',all_list[i]['ID'])
    print('Name :',all_list[i]['Name'])
    print('Address :',all_list[i]['Address'])
    print('Tel :',all_list[i]['Tel'])
    #print('HostWords :',all_list[i]['HostWords'])
    print('City :',all_list[i]['City'])
    print('Town :',all_list[i]['Town'])
    print('PicURL :',all_list[i]['PicURL'])
    print('Latitude :',all_list[i]['Latitude'])
    print('Longitude :',all_list[i]['Longitude'])
    print("------------------------------------------------------------")  # 60個
    
image_foldername = 'tmp_images'
html_filename = 'tmp_countryfood2222.html'
if os.path.exists(html_filename):  
    os.remove(html_filename)     # 若有 tmp_countryfood.html 網頁即刪除
if os.path.exists(image_foldername): 
    shutil.rmtree(image_foldername)    # 若有images目錄即刪除
else:
    os.mkdir(image_foldername)        # 若無images目錄即刪除

#下載圖片
cnt = 0
for col in all_list:  
    imgUrl=col['PicURL']
    print(cnt)
    #網址用'/'分隔取最後一筆資料 => *.jpg
    imgName = imgUrl.split('/')[-1] #擷取圖片名稱
    print('圖片網址：', imgUrl)
    print('圖片檔名：', imgName)
    
    print("------------------------------------------------------------")  # 60個
    cnt += 1
    try:
        #建立取得圖片的Rpimg物件
        Rpimg=requests.get(imgUrl) 
        f=open((image_foldername+'/'+imgName),'wb')    #開啟圖片檔案                    
        f.write(Rpimg.content)     #下載圖片
        print(imgName,'下載完畢')
        print("------------------------------------------------------------")  # 60個
        f.close()
        if cnt >= 10:
            break
    except:
        print('下載失敗')
        print("------------------------------------------------------------")  # 60個
        sys.exit(1)

print('製作html檔案')
fw=open(html_filename,'w',encoding='UTF-8')
fw.write('<!DOCTYPE html>\n')
fw.write('<html>\n')
fw.write('<head><meta charset="utf-8" />\n')
fw.write('<title>農村地方美食小吃特色料理</title>\n')
fw.write('</head>\n')
fw.write('<body>\n')

#網頁CSS樣式設定
style="""
<style> 
img { 
   border-radius: 4px 4px 0 0; height:180px; 
   width:100%; 
} 
.card { 
   box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); 
   width: 280px ; 
   border-radius: 5px; 
   border:1px #FFF2C1 solid; float: left; 
   margin:13px; 
} 
.card:hover { 
   box-shadow: 0 8px 16px 0 #FCC592; 
} 
.txt { 
   padding: 2px 16px; 
   height:110px;
   background-color:#FEE3AD; 
} 
</style>       
"""
fw.write('\n'+style+'\n')

#HTML標籤與開放資料整合成網頁內容
cnt = 0
for row in all_list:
    print("cnt = ", cnt)
    #網址用'/'分隔取最後一筆資料 => *.jpg
    picName=row['PicURL'].split('/')[-1]
    print('圖片網址：', row['PicURL'])
    print('圖片檔名：', picName)
    
    fw.write('<div class="card">\n') #設定外層div以及屬性
    # 設置圖片的相對路徑，路徑為 'images/檔名'
    fw.write('  <img src="'+ image_foldername +'/'+ picName + '">\n') 
    fw.write('  <div class="txt">\n') #設定文字div以及屬性
    fw.write('     <h4><b>'+row['Name']+'</b></h4>\n') #寫入店家名稱
    fw.write('     <p>'+row['Address']+'</p>\n') #寫入店家地址
    fw.write('  </div>\n') 
    fw.write('</div>\n\n')
    cnt += 1
    if cnt >= 10:
        break

fw.write('</body>\n') 
fw.write('</html>\n') 
fw.close()

#os.system(html_filename)  # 開啟網頁
print("%s 網頁建置完成" % (html_filename))

'''

print("------------------------------------------------------------")  # 60個

# 引用相關套件
import requests, json

# 指定url變數為全國休閒農業區旅遊資訊所提供的json檔資料網址
url = "https://data.coa.gov.tw/Service/OpenData/ODwsv/ODwsvAttractions.aspx"
# 建立取得網頁資訊的Response物件，物件名稱為rp
rp = requests.get(url)
# 設定編碼模式避免亂碼
rp.encoding = "utf_8_sig"
# 使用json套件的loads()方法將擷取到的資料集轉成串列
all_list = json.loads(rp.text)
# 建立Inquire變數來存放欲查詢資料中的縣市名稱

# Inquire=str(input('輸入縣市查詢當地的農場：'))
Inquire = "雲林"

# 當輸入的字元有 '台' 字時，將該字轉換成 '臺' 字
Inquire = Inquire.replace("台", "臺")
print("------------------------------------------------------------")  # 60個

list_result = []  # 建立list_result串列用來存放符合的農業休閒區項目
for col in all_list:
    if Inquire in col["City"]:  # 判斷查詢的縣市使否存在
        print("名稱：", col["Name"], "電話：", col["Tel"], "\n地址：", col["Address"])
        print("------------------------------------------------------------")  # 60個
        list_result += [col["City"]]  # 將符合的農業休閒區項目放入list_result串列

# 使用len()函式取得list_result串列的數量並放入變數count
count = len(list_result)
# 判斷農業休閒區數量是否不等於0
if count != 0:
    print(list_result[0], "總計", count, "處旅遊區")
else:
    # 其餘狀況則顯示錯誤或無農業休閒區
    print("輸出錯誤或是此地沒有旅遊區")

print("------------------------------------------------------------")  # 60個

import requests, json

# 指定url變數為全國休閒農業區旅遊資訊所提供的json檔資料網址
url = "https://data.coa.gov.tw/Service/OpenData/ODwsv/ODwsvAttractions.aspx"
# 建立取得網頁資訊的Response物件，物件名稱為rp
rp = requests.get(url)
# 設定編碼模式避免亂碼
rp.encoding = "utf_8_sig"
# 使用json套件的loads()方法將JSON資料集轉成串列
all_list = json.loads(rp.text)
# 資料整理
listAllCity = []  # 存放每筆記錄的縣市名稱，此處串列存放重複的縣市名稱
for col in all_list:
    listAllCity += [col["City"]]

listCity = []  # 存放所有縣市名稱，此串列存放不重複的縣市名稱
listCount = []  # 存放各縣市對應的農業區數量
for city in set(listAllCity):  # 使用set()移除listAllCity串列中重複的縣市
    print(city, "地區有", listAllCity.count(city), "個農業區")
    listCity += [city]
    listCount += [listAllCity.count(city)]

print("縣市 :", listCity)
print()
print("數量 :", listCount)
print()

print("------------------------------------------------------------")  # 60個

sys.exit()

# 注意，本範例會隨著網站更新而導致無法爬文，若有問題可來信討論

# 引用相關套件
import requests
from bs4 import BeautifulSoup

# 指定url變數為「Dcard熱門文章」網頁的網址
url = "https://www.dcard.tw/f"
response = requests.get(url)
bs = BeautifulSoup(response.text, "lxml")  # 取得物件
# 取得所有文章程式碼
listItems = bs.find_all("article", "sc-1v1d5rx-0 lmtfq")

for item in listItems:
    time = item.find_all("span", "sc-6oxm01-2 hiTIMq")[2]  # 發文時間
    print("發文時間:", time.text)
    print("文章標題:", item.h2.text)  # 文章標題
    URl = item.find("a").get("href")  # 文章網址
    print("文章網址: https://www.dcard.tw" + URl)
    print("=" * 70)
print("取得文章數量 =", len(listItems))


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
