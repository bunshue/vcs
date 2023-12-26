# ch23_10.py
import requests, bs4

htmlFile = requests.get('https://deepwisdom.com.tw')
objSoup = bs4.BeautifulSoup(htmlFile.text, 'lxml')
print(f"列印BeautifulSoup物件資料型態 {type(objSoup)}")











