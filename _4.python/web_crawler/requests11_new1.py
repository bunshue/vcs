import sys

import os
import time
import random

import requests
import re
import bs4

print("------------------------------------------------------------")  # 60個

import webbrowser
webbrowser.open('http://www.mcut.edu.tw')

print("------------------------------------------------------------")  # 60個

#address = input("請輸入地址 : ")
address = "新竹市東區榮光里中華路二段445號"
webbrowser.open('http://www.google.com.tw/maps/place/' + address)

print('------------------------------------------------------------')	#60個

url = 'http://www.mcut.edu.tw'
htmlfile = requests.get(url)
print(type(htmlfile))
if htmlfile.status_code == requests.codes.ok:
    print("取得網頁內容成功")
    print("網頁內容大小 = ", len(htmlfile.text))
else:
    print("取得網頁內容失敗")

print("------------------------------------------------------------")  # 60個

url = 'http://www.mcut.edu.tw'
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    print("取得網頁內容成功")
    print(htmlfile.text)            # 列印網頁內容
else:
    print("取得網頁內容失敗")

print('------------------------------------------------------------')	#60個

url = 'http://www.mcut.edu.tw'
htmlfile = requests.get(url)
if htmlfile.status_code == requests.codes.ok:
    pattern = input("請輸入欲搜尋的字串 : ")    # 讀取字串
# 使用方法1
    if pattern in htmlfile.text:              # 方法1
        print(f"搜尋 {pattern} 成功")
    else:
        print(f"搜尋 {pattern} 失敗")
    # 使用方法2, 如果找到放在串列name內
    name = re.findall(pattern, htmlfile.text)  # 方法2
    if name:
        print(f"{pattern} 出現 {len(name)} 次")
    else:
        print(f"{pattern} 出現 0 次")
else:
    print("網頁下載失敗")

print('------------------------------------------------------------')	#60個

url = 'http://mcut.edu.tw/file_not_existed' # 不存在的內容
try:
    htmlfile = requests.get(url)
    htmlfile.raise_for_status()             # 異常處理
    print("下載成功")
except Exception as err:                    # err是系統內建的錯誤訊息
    print(f"網頁下載失敗: {err}")
print("程式繼續執行 ... ")

print('------------------------------------------------------------')	#60個

url = 'https://www.kingstone.com.tw/' 
htmlfile = requests.get(url)
htmlfile.raise_for_status()

print('------------------------------------------------------------')	#60個

headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }
url = 'https://www.kingstone.com.tw/'
htmlfile = requests.get(url, headers=headers)
htmlfile.raise_for_status()
print("偽裝瀏覽器擷取網路資料成功")

print('------------------------------------------------------------')	#60個

url = 'http://www.tenlong.com.tw'                    # 天瓏書局網址
try:
    htmlfile = requests.get(url)
    print("下載成功")
except Exception as err:                                
    print("網頁下載失敗: %s" % err)
# 儲存網頁內容
fn = 'tmp_html_text1.txt'
with open(fn, 'wb') as file_Obj:                     # 以二進位儲存
    for diskStorage in htmlfile.iter_content(10240): # Response物件處理
        size = file_Obj.write(diskStorage)           # Response物件寫入
        print(size)                                  # 列出每次寫入大小
    print("以 %s 儲存網頁HTML檔案成功" % fn)

print('------------------------------------------------------------')	#60個

import requests

r = requests.get('http://tw.yahoo.com')

print(r.text)

print('------------------------------------------------------------')	#60個

import requests

import pprint

r = requests.get('http://tw.yahoo.com')

pprint.pprint(r.text)


print('------------------------------------------------------------')	#60個

import requests

import pprint

api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'

weather_data = requests.get(api_url).json()

pprint.pprint(weather_data)

print('------------------------------------------------------------')	#60個


url = 'http://weather.livedoor.com/forecast/webservice/json/v1'

paload = {'city':'130010'}

weather_data = requests.get(url, params = paload).json()


print('------------------------------------------------------------')	#60個


pprint.pprint(weather_data['forecasts'][0]) 


print('------------------------------------------------------------')	#60個

import requests, pprint

api_url = 'https://zh.wikipedia.org/w/api.php'

api_params = {'format':'json', 'action':'query', 'titles':'椎名林檎', 'prop':'revisions', 'rvprop':'content'}

wiki_data = requests.get(api_url, params = api_params)

pprint.pprint(wiki_data)

print('------------------------------------------------------------')	#60個

import requests

addr = 'https://www.edu.tw/'    #教育部
addr = 'https://www.books.com.tw/'

res = requests.get(addr)

#檢查狀態碼
if res.status_code == 200:
    print('status_code= ',res.status_code)
    res.encoding='utf-8'
    print(res.text)
else:
    print('網頁無法開啟, status_code= ',res.status_code)


import base64
from io import BytesIO
from PIL import Image

url = 'https://upload.wikimedia.org/wikipedia/commons/3/3d/Uranus2.jpg'
resp = requests.get(url)
img3 = Image.open(BytesIO(resp.content))
img3.save('tmp_Uranus2.jpg')

print(base64.b64encode(resp.content))



print('------------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個








