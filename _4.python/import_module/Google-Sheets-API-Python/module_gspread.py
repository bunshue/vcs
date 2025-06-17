"""
gspread

"""


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" NG
# LinkGoogleSheet.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials as sac

# 設定金鑰檔路徑及驗證範圍
auth_json = "data/PythonConnectGsheet1-6a6086d149c5.json"
gs_scopes = ["https://spreadsheets.google.com/feeds"]
# 連線資料表
cr = sac.from_json_keyfile_name(auth_json, gs_scopes)
gc = gspread.authorize(cr)
# 開啟資料表
spreadsheet_key = "1OihpM657yWo1lc3RjskRfZ8m75dCPwL1IPwoDXSvyzI"
sheet = gc.open_by_key(spreadsheet_key)
# 開啟工作簿
wks = sheet.sheet1
# 清除所有內容
wks.clear()
# 新增列
listtitle = ["座號", "姓名", "國文", "英文", "數學"]
wks.append_row(listtitle)  # 標題
listdatas = [[1, "葉大雄", 65, 62, 40], [2, "陳靜香", 85, 90, 87], [3, "王聰明", 92, 90, 95]]
for listdata in listdatas:
    wks.append_row(listdata)  # 資料內容
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
"""
# LinkGoogleSheet.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials as sac

# 設定金鑰檔路徑及驗證範圍
auth_json = 'pythonconnectgsheet1-273500-e6ce04448957.json'
gs_scopes = ['https://spreadsheets.google.com/feeds']
# 連線資料表
cr = sac.from_json_keyfile_name(auth_json, gs_scopes)
gs_client = gspread.authorize(cr) 
# 開啟資料表
spreadsheet_key = '1lBlHPDYqwnQNiJrz-8nqPEd5H6Q4w0PaKasrrjojCNI' 
sheet = gs_client.open_by_key(spreadsheet_key)
# 開啟工作簿
wks = sheet.sheet1
# 清除所有內容
wks.clear() 
# 新增列
listtitle=["姓名","電話"]
wks.append_row(listtitle)  # 標題
listdata=["chiou","0937-1234567"]
wks.append_row(listdata)   # 資料內容

print("------------------------------------------------------------")  # 60個

# LinkGoogleSheet.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials as sac
# 設定金鑰檔路徑及驗證範圍
auth_json = 'PythonConnectGsheet1-6a6086d149c5.json'
gs_scopes = ['https://spreadsheets.google.com/feeds']
# 連線資料表
cr = sac.from_json_keyfile_name(auth_json, gs_scopes)
gs_client = gspread.authorize(cr) 
# 開啟資料表
spreadsheet_key = '1OihpM657yWo1lc3RjskRfZ8m75dCPwL1IPwoDXSvyzI' 
sheet = gs_client.open_by_key(spreadsheet_key)
# 開啟工作簿
wks = sheet.sheet1
# 清除所有內容
wks.clear() 
# 新增列
listtitle=["姓名","電話"]
wks.append_row(listtitle)  # 標題
listdata=["chiou","0937-1234567"]
wks.append_row(listdata)  # 資料內容
"""
print("------------------------------------------------------------")  # 60個

# Link Google Sheet

import gspread
from oauth2client.service_account import ServiceAccountCredentials

auth_json_path = 'gs_key/PythonUpload.json'
gss_scopes = ['https://spreadsheets.google.com/feeds']

#連線
credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_json_path,gss_scopes)
gss_client = gspread.authorize(credentials) 

#開啟 Google Sheet 資料表
spreadsheet_key = '1OihpM657yWo1lc3RjskRfZ8m75dCPwL1IPwoDXSvyzI' 
sheet = gss_client.open_by_key(spreadsheet_key).sheet1

# Google Sheet 資料表
sheet.clear() # 清除 Google Sheet 資料表內容
listtitle=["姓名","電話"]
sheet.append_row(listtitle)  # 標題
listdata=["chiou","0937-1234567"]
sheet.append_row(listdata)  # 資料內容



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# MiChiLin Taipei Link Google Sheet

def showsite(siteurl):
    html = requests.get(siteurl).text
    soup = BeautifulSoup(html,'html.parser')  
    kind=soup.select(".content-header-desc__detail")[1].text.strip() #分類
    area=soup.select(".content-header-desc__detail")[2].text.strip() #區
    item_desc=soup.select(".location-item .location-item__desc") #店名、地址
    name=item_desc[0].select("p")[0].text #店名    
    imgurl=soup.find('div',{'class':'images-featured-big-slider'}).get('style').split("'")[1] # 圖片名稱    
    lat=soup.select("#js-location-map")[0]["data-lat"] #緯度
    lng=soup.select("#js-location-map")[0]["data-lon"] #經度
    tel=soup.select(".location-item .location-item__desc")[2].text.strip()  #電話 
    addr=item_desc[0].select("p")[1].text.replace(" ","").replace("\n","").strip() #地址
    desc=soup.select(".restaurant-desc")[0].text.strip() #說明
    working_hours=soup.select(".location-item .location-item__desc")[1].text.strip()  #營業時間
    # 將資料加入 list1 串列中
    listdata=[kind,area,name,siteurl,imgurl,lat,lng,tel,addr,desc,working_hours]
    list1.append(listdata)

def getpageurl(page,url):
    global n,totpages
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser') 
    items = soup.select('.grid-restaurants__item__inner')
    print("第" + str(page)+"頁,共有"+ str(len(items)) + "間")
    for item in items:
        n+=1
        print("n=",n)
        itemurl=item.select('.resto-inner-title a')[0]['href'] #網址
        siteurl=rooturl + itemurl #組成完整網址
        showsite(siteurl) #顯示該店資訊
        if n==1:
            totpages=int(soup.find("input",{"class":"form-control"})['data-max_page']) # 總頁數
        
def auth_gss_client(path, scopes):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(path,scopes)
    return gspread.authorize(credentials)        

#主程式 
import time
import requests
from bs4 import BeautifulSoup 
import gspread
from oauth2client.service_account import ServiceAccountCredentials

list1=[]
n=0 #計算總共有多少家店
homeurl = 'https://guide.michelin.com/tw/taipei/restaurants?max=30&sort=relevance&order=desc'
rooturl='https://guide.michelin.com'
getpageurl(1,homeurl)  # 首頁

for page in range(2,totpages+1): #第 2~totpages頁
    html = requests.get(homeurl).text
    soup = BeautifulSoup(html,'html.parser') 
    path=soup.find("a",{"class":"page-arrow"}) # 「>」 下一頁按鈕
    fullurl = path["href"] #讀取 href 內容
    #以「?」分割，刪除前面字串中的最後一個字元，再加上 page 後，組成完整的路徑
    url = rooturl + fullurl.split("?")[0][:-1] + str(page)+ "?" + fullurl.split("?")[1]
    getpageurl(page,url)

auth_json_path = 'gs_key/PythonUpload.json'
gss_scopes = ['https://spreadsheets.google.com/feeds']
gss_client = auth_gss_client(auth_json_path, gss_scopes) #連線

spreadsheet_key = '1OihpM657yWo1lc3RjskRfZ8m75dCPwL1IPwoDXSvyzI' 
sheet = gss_client.open_by_key(spreadsheet_key).sheet1 #開啟工作表
sheet.clear() # 清除工作表內容

# Google Sheet 資料
listtitle=["分類","區","店名","網址","圖片名稱","經度","緯度","電話","地址","說明","營業時間"]
sheet.append_row(listtitle)  # 標題

for item1 in list1: #資料
    sheet.append_row(item1)
    time.sleep(1) # 必須加上適當的 delay
       
print("\n總共有",n,"間")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個







print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


