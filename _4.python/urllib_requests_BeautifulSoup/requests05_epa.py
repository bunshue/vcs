import requests

DataID = 'aqx_p_488'
format = 'csv'
year_month = '2023_04'
offset = '0'
limit = '100'
api_key = 'xxxxxxxx'


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

print()
print()

import pandas as pd


format = 'csv'
url = 'https://data.epa.gov.tw/api/v2/%s?format=%s&offset=%s&limit=%s&api_key=%s' % (DataID, format, offset, limit, api_key)

data = pd.read_csv(url)

print(data)
