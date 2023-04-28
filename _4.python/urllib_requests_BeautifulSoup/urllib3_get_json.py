import urllib.request   #用來建立請求
import zipfile
import csv

print('讀取遠端 json 檔案')

url ='https://data.epa.gov.tw/api/v2/aqx_p_432?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=ImportDate%20desc&format=JSON'
filename = 'AQI.'   #圖檔名稱

urllib.request.urlretrieve(url, filename) #下載遠端 json 檔案




print('作業完成')

