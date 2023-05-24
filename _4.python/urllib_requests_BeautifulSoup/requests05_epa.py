import sys
import requests

def get_epa_key():
    filename = 'C:/_git/vcs/_1.data/______test_files1/_key/epa_key.txt'

    import os
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

DataID = 'aqx_p_488'
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
'''
條件查詢方式是使用filters參數加在API網址後：&filters='{資料字典英文欄位}',EQ,'{搜尋值}‘
ex：&filters=SiteName,EQ,馬公
'''
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

print('作業完成')






'''

import urllib.request   #用來建立請求
import zipfile
import csv

print('讀取遠端 json 檔案')

format = 'json'

url = 'https://data.epa.gov.tw/api/v2/%s?format=%s&offset=%s&limit=%s&api_key=%s' % (DataID, format, offset, limit, api_key)


filename = 'AQI.json'   #圖檔名稱

urllib.request.urlretrieve(url, filename) #下載遠端 csv 檔案

'''

'''
print()
print()

import pandas as pd


format = 'csv'
url = 'https://data.epa.gov.tw/api/v2/%s?format=%s&offset=%s&limit=%s&api_key=%s' % (DataID, format, offset, limit, api_key)

data = pd.read_csv(url)

print(data)
'''

'''
#JSON格式
def getAQI(key, filters):
    url = f'https://data.epa.gov.tw/api/v2/aqx_p_432?filters={filters}&api_key={key}&format=json'
    r = requests.get(url)
    jObj = r.json()['records']
    r.close()
    return jObj

#filters = 'sitename,EQ,桃園'
filters = 'siteid,EQ,17'
data = getAQI(api_key, filters)[0]
# 欄位都是小寫的
print(f'縣市: {data["county"]}')
print(f'測站名稱: {data["sitename"]}')
print(f'AQI: {data["aqi"]}')
print(f'PM2.5: {data["pm2.5"]}')


#CSV格式

def getAQI_csv(key, filters):
    url = f'https://data.epa.gov.tw/api/v2/aqx_p_432?filters={filters}&api_key={key}&format=csv'
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
'''

import tkinter as tk
import urllib3 #外部的packages
import certifi #https的連線方式

def downloadAQI():
    print("開始下載資料")

    DataID = 'aqx_p_432'
    format = 'csv'
    limit = '1000'
    api_key = epa_key

    url = 'https://data.epa.gov.tw/api/v2/%s?format=%s&limit=%s&api_key=%s' % (DataID, format, limit, api_key)
    print(url)
    
    #url = 'https://data.epa.gov.tw/api/v2/aqx_p_432?format=csv&limit=1000&api_key=xxxxxx'
    
    http=urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where()) #建立https連線
    #如下載網址為http://....則建立http連線為：http = urllib3.PoolManager()
    response = http.request('GET', url) #使用GET方法儲存
    if response.status == 200:
        print("下載成功")
        print(response.data)
        #儲存檔案，建立file實體
        file=open("空氣品質指標.csv","wb")
        file.write(response.data)
        print("存檔成功")
        file.close() #關閉檔案
        
    else:
        print("下載失敗")
        return #中斷，跳出downloadAQI

window = tk.Tk()
window.title("範例一")
window.geometry("500x300") #沒有設定寬x高，將依元件調整視窗大小
tk.Button(window, text = "下載資料", command = downloadAQI).pack(side = tk.LEFT, ipadx = 25, ipady = 25, expand = tk.YES)
window.mainloop()


 


