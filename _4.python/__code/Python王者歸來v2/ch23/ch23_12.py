# ch23_12.py
import requests, bs4

htmlFile = requests.get('http://www.deepmind.com.tw')
objSoup = bs4.BeautifulSoup(htmlFile.text, 'lxml')
print("列印BeautifulSoup物件資料型態 ", type(objSoup))











