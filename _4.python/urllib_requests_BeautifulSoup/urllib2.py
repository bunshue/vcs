# Python 測試 urllib

print('----------------------------------------------------------------------')	#70個
print('準備工作')


import urllib
import urllib.request   #用來建立請求
import zipfile
import csv

import requests
from urllib.parse import urlparse
from urllib.request import urlopen

print('----------------------------------------------------------------------')	#70個
print('urllib 測試 1')

'''
#新北市公共自行車即時資訊

print('讀取遠端zip檔')

# 公開資料檔案
url ='https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/csv/zip'
filename = 'ntpc_bicycle.zip'   #壓縮檔案名稱
file_dir = './'     #解壓縮目錄

urllib.request.urlretrieve(url, filename) #下載壓縮檔
f = zipfile.ZipFile(filename) #開啟壓縮檔
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
'''

'''
row[0]	sno：站點代號
row[1]	sna：場站名稱(中文)
row[2]	tot：場站總停車格
row[3]	sbi：場站目前車輛數量
row[4]	sarea：場站區域(中文)
row[5]	mday：資料更新時間
row[6]	lat：緯度
row[7]	lng：經度
row[8]	ar：地址(中文)
row[9]	sareaen：場站區域(英文)
row[10]	snaen：場站名稱(英文)
row[11]	aren：地址(英文)
row[12]	bemp：空位數量
row[13]	act：全站禁用狀態
'''



#全國環境輻射偵測即時資訊

print('讀取遠端zip檔')

# 公開資料檔案
url ='https://www.aec.gov.tw/dataopen/index.php?id=2'
filename = 'data.csv'   #壓縮檔案名稱

urllib.request.urlretrieve(url, filename) #下載csv檔

with open(filename, 'r', encoding = 'big5') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        print(row[0]+" "+row[2]+" "+row[3])


print('作業完成')


'''
row[0]	監測站
row[1]	監測站(英文)
row[2]	監測值(微西弗/時)
row[3]	時間
row[4]	GPS經度
row[5]	GPS緯度
'''


    
print('urllib 測試 作業完成')

