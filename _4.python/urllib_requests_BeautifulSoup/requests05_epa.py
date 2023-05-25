'''
AQI綜合指標（Air Quality Index 空氣品質指標）

空氣品質指標值(AQI)

細懸浮微粒(PM2.5)
懸浮微粒(PM10)

空氣品質指標(AQI)
資料集代碼 	AQX_P_432

空氣品質指標(AQI)(歷史資料)
資料集代碼 	AQX_P_488
'''

import requests

import urllib.request   #用來建立請求
import zipfile
import csv

import os
import sys
import time

import pandas as pd

import urllib3 #外部的packages
import certifi #https的連線方式
import hashlib
import sqlite3
import ast
from bs4 import BeautifulSoup

def get_epa_key():
    filename = 'C:/_git/vcs/_1.data/______test_files1/_key/epa_key.txt'

    filename = os.path.abspath(filename)
    if not os.path.exists(filename): #檢查檔案是否存在
        print('EPA_KEY 檔案不存在, 離開, 檔案 : ' + filename)
        return ""

    print("讀取檔案 : " + filename)
    fo = open(filename, 'r')
    epa_key = fo.read()
    fo.close()

    length = len(epa_key)
    if length != 36:
        print('EPA_KEY 錯誤, 離開')
        return ""
    return epa_key


epa_key = get_epa_key()
length = len(epa_key)
if length != 36:
    print('EPA_KEY 錯誤, 離開')
    sys.exit(1)	#立刻退出程式

DataID = 'AQX_P_432'
format = 'csv'
year_month = '2023_04'
offset = '0'
limit = '100'
api_key = epa_key

'''
#無查詢條件
url = 'https://data.epa.gov.tw/api/v2/%s?format=%s&offset=%s&limit=%s&api_key=%s' % (DataID, format, offset, limit, api_key)
print(url)
r = requests.get(url)
print(r.text)
'''

'''
#無查詢條件
url = 'https://data.epa.gov.tw/api/v2/%s?format=%s&year_month=%s&offset=%s&limit=%s&api_key=%s' % (DataID, format, year_month, offset, limit, api_key)
print(url)
r = requests.get(url)
print(r.text)
'''

#有查詢條件
#條件查詢方式是使用filters參數加在API網址後：&filters='{資料字典英文欄位}',EQ,'{搜尋值}‘
#ex：&filters=SiteName,EQ,馬公
filters1 = 'SiteName,EQ,馬公'
filters2 = 'SiteName,EQ,馬公,金門'
filters3 = 'SiteName,EQ,馬公,金門|status,EQ,普通'

url = 'https://data.epa.gov.tw/api/v2/%s?format=%s&year_month=%s&offset=%s&limit=%s&api_key=%s&filters=%s' % (DataID, format, year_month, offset, limit, api_key, filters1)
print(url)

url = 'https://data.epa.gov.tw/api/v2/%s?format=%s&year_month=%s&offset=%s&limit=%s&api_key=%s&filters=%s' % (DataID, format, year_month, offset, limit, api_key, filters2)
print(url)

url = 'https://data.epa.gov.tw/api/v2/%s?format=%s&year_month=%s&offset=%s&limit=%s&api_key=%s&filters=%s' % (DataID, format, year_month, offset, limit, api_key, filters3)
print(url)

'''
r = requests.get(url)
print(r.text)
'''

print('----------------------------------------------------------------------')	#70個
time.sleep(3)

print('讀取遠端 json 檔案')
format = 'json'
url = 'https://data.epa.gov.tw/api/v2/%s?format=%s&offset=%s&limit=%s&api_key=%s' % (DataID, format, offset, limit, api_key)
filename = 'C:/_git/vcs/_1.data/______test_files2/AQI_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.json';   #json檔案名稱
urllib.request.urlretrieve(url, filename) #下載遠端 json 檔案

print('----------------------------------------------------------------------')	#70個
time.sleep(3)

format = 'csv'
url = 'https://data.epa.gov.tw/api/v2/%s?format=%s&offset=%s&limit=%s&api_key=%s' % (DataID, format, offset, limit, api_key)

data = pd.read_csv(url)

print(data)

print('----------------------------------------------------------------------')	#70個
time.sleep(3)

#JSON格式
def getAQI(key, filters):
    url = f'https://data.epa.gov.tw/api/v2/{DataID}?filters={filters}&api_key={key}&format=json'
    print(url)
    r = requests.get(url)
    jObj = r.json()['records']
    r.close()
    return jObj

#filters = 'sitename,EQ,桃園'
filters = 'siteid,EQ,17'
data = getAQI(api_key, filters)[0]  #只看第1筆資料, index = 0
# 欄位都是小寫的
print(f'縣市: {data["county"]}')
print(f'測站名稱: {data["sitename"]}')
print(f'AQI: {data["aqi"]}')
print(f'PM2.5: {data["pm2.5"]}')

print('----------------------------------------------------------------------')	#70個
time.sleep(3)

#CSV格式

def getAQI_csv(key, filters):
    url = f'https://data.epa.gov.tw/api/v2/{DataID}?filters={filters}&api_key={key}&format=csv'
    r = requests.get(url)
    csv = r.text
    r.close()
    return csv


#filters = 'sitename,EQ,桃園'
filters = 'siteid,EQ,17'
lines = getAQI_csv(api_key, filters).split('\n')
fields = lines[0].split(',')
row = lines[1].split(',')
data = {}
for idx in range(len(fields)):
    data[fields[idx]] = row[idx]
# 欄位都是小寫的
print(f'縣市: {data["county"]}')
print(f'測站名稱: {data["sitename"]}')
print(f'AQI: {data["aqi"]}')
print(f'PM2.5: {data["pm2.5"]}')

print('----------------------------------------------------------------------')	#70個
time.sleep(3)

def downloadAQI():
    print("開始下載資料")

    DataID = 'AQX_P_432'
    format = 'csv'
    limit = '1000'
    api_key = epa_key

    url = 'https://data.epa.gov.tw/api/v2/%s?format=%s&limit=%s&api_key=%s' % (DataID, format, limit, api_key)
    print(url)
    
    #url = 'https://data.epa.gov.tw/api/v2/AQX_P_432?format=csv&limit=1000&api_key=xxxxxx'
    
    http = urllib3.PoolManager(cert_reqs = 'CERT_REQUIRED', ca_certs = certifi.where()) #建立https連線
    #如下載網址為http://....則建立http連線為：http = urllib3.PoolManager()
    response = http.request('GET', url) #使用GET方法儲存
    if response.status == 200:
        print("下載成功")
        print(response.data)
        #儲存檔案，建立file實體
        filename = 'C:/_git/vcs/_1.data/______test_files2/AQI_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.csv';
        file = open(filename, "wb")
        file.write(response.data)
        print("存檔成功")
        file.close() #關閉檔案
        
    else:
        print("下載失敗")
        return #中斷，跳出downloadAQI

downloadAQI()

print('----------------------------------------------------------------------')	#70個
time.sleep(3)


db_filename = 'C:/_git/vcs/_1.data/______test_files1/_db/DataBasePM25.sqlite'
md5_filename = 'C:/_git/vcs/_1.data/______test_files2/old_md5.txt'

conn = sqlite3.connect(db_filename) # 建立資料庫連線
cursor = conn.cursor() # 建立 cursor 物件

# 建立一個資料表
sqlstr='''
CREATE TABLE IF NOT EXISTS TablePM25 ("no" INTEGER PRIMARY KEY AUTOINCREMENT 
NOT NULL UNIQUE ,"SiteName" TEXT NOT NULL ,"PM25" INTEGER)
'''
cursor.execute(sqlstr)

print('以md5檢查網站內容是否更新')

DataID = 'AQX_P_432'
format = 'json'
limit = '10'
api_key = epa_key

#fail
url = 'https://data.epa.gov.tw/api/v2/%s?format=%s&year_month=%s&offset=%s&limit=%s&api_key=%s&filters=%s' % (DataID, format, year_month, offset, limit, api_key, filters1)
print(url)
#fail same
url = f'https://data.epa.gov.tw/api/v2/{DataID}?format={format}&year_month={year_month}&offset={offset}&limit={limit}&api_key={api_key}&filters={filters1}'
print(url)

#filters = 'sitename,EQ,桃園'
filters = 'siteid,EQ,17'

DataID = 'AQX_P_432'
#ok  AQX_P_432
url = f'https://data.epa.gov.tw/api/v2/{DataID}?filters={filters}&api_key={api_key}&format=json'
print(url)
url = f'https://data.epa.gov.tw/api/v2/{DataID}?format=json&api_key={api_key}&filters={filters1}'
print(url)

url = f'https://data.epa.gov.tw/api/v2/{DataID}?format=json&api_key={api_key}'
print(url)

# 讀取網頁原始碼
#html = requests.get(url).text.encode('utf-8-sig')
html = requests.get(url)
#print(html)

# 判斷網頁是否更新
md5 = hashlib.md5(html.text.encode('utf-8-sig')).hexdigest()
print('新md5 : ', md5)

old_md5 = ""
if os.path.exists(md5_filename):
    print('111')
    with open(md5_filename, 'r') as f:
        print('111a')
        old_md5 = f.read()
        
with open(md5_filename, 'w') as f:
    print('222')
    f.write(md5)

print('舊md5 : ', old_md5)

if md5 != old_md5:
    print('資料已更新...')

    # 刪除資料表內容
    conn.execute("delete from TablePM25")
    conn.commit()
    

    # 欄位都是小寫的
    jsondata = html.json()['records']

    '''
    # debug
    #print(jsondata)
    print(len(jsondata))
    n = 1
    for site in jsondata:
        print(f'縣市: {site["county"]}')
        print(f'測站名稱: {site["sitename"]}')
        print(f'AQI: {site["aqi"]}')
        print(f'PM2.5: {site["pm2.5"]}')
        n += 1
        if n == 10:
            break;
    '''
    
    n = 1
    for site in jsondata:
        SiteName=site["sitename"]
        if site["pm2.5"] == "ND":
            continue
        PM25 = 0 if site["pm2.5"] == "" else int(site["pm2.5"])
        print("站名:{}   PM2.5={}".format(SiteName, PM25))
        # 新增一筆記錄
        sqlstr="insert into TablePM25 values({},'{}',{})" .format(n, SiteName, PM25)
        cursor.execute(sqlstr)
        n += 1
        conn.commit() # 主動更新

else:
    print('資料未更新，從資料庫讀取...') 
    cursor=conn.execute("select *  from TablePM25")
    rows=cursor.fetchall()
    for row in rows:
        print("站名:{}   PM2.5={}".format(row[1],row[2]))    

conn.close()  # 關閉資料庫連線

print('作業完成')

