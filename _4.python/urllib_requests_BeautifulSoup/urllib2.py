'''
新北市公共自行車即時資訊
'''

import urllib.request   #用來建立請求
import zipfile
import csv

print('讀取遠端zip檔')

# 公開資料檔案
url ='https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/csv/zip'
zipName = 'F.zip'   #壓縮檔案名稱
file_dir = './'     #解壓縮目錄

urllib.request.urlretrieve(url, zipName) #下載壓縮檔
f = zipfile.ZipFile(zipName) #開啟壓縮檔
for fileName in f.namelist(): #壓縮檔案列表檔名
    f.extract(fileName, file_dir) #擷取壓縮檔案
    print(fileName) #印出解壓縮檔案名稱
f.close() #關檔

f = open(fileName, 'r',encoding = 'utf8') #開啟CSV檔案，，唯讀utf-8解碼
plots = csv.reader(f, delimiter=',') #讀取CSV檔案間隔逗號，設定給plots串列物件
for row in plots: #印出UBIKE資料
    print('%5s' %row[0], '%15s' %row[1], '%5s' %row[3], '%5s' %row[12])
f.close()

print('作業完成')
