# ch13_1.py
import requests

url = 'http://www.taiwanrate.com/'
htmlfile = requests.get(url)
print("HTML編碼方式 : ", htmlfile.encoding)
print("列印網頁內容 \n", htmlfile.text)




