﻿import urllib.request

url = 'http://www.grandtech.info/'

#以with/as敘述來取得網址，離開之後會自動釋放資源
with urllib.request.urlopen(url) as response:
    print('網頁網址',response.geturl())
    print('伺服器狀態碼',response.getcode())
    print('網頁表頭',response.getheaders())
    zct_str = response.read().decode('UTF-8')

print('將網頁資料轉成字串格式',zct_str)
#print('網頁程式碼如下: ',zct_str)

