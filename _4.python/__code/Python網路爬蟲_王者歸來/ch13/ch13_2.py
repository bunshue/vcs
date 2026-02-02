# ch13_2.py
import requests

url = 'http://www.taiwanrate.com/'
htmlfile = requests.get(url)
print("HTML編碼方式 : ", htmlfile.encoding)
htmlfile.encoding = 'utf-8'         # 編碼改為utf-8
print("更改編碼")
print("HTML編碼方式 : ", htmlfile.encoding)
print("列印網頁內容 \n", htmlfile.text)




