import requests
from bs4 import BeautifulSoup
url='http://www.dtc-tech.com.tw' #大才全資訊科技股有限公司首頁
response=requests.get(url)
bs=BeautifulSoup(response.text,'lxml')  	#傳回bs物件可解析網頁
print(bs.find('title'))                 	#傳回網頁含<title>~</title>
print(bs.find('title').text)            	#傳回網頁<title>標籤內的資料
print(bs.find('h1'))                    	#傳回第一個符合<h1>資料
					                          #若傳回None表示該網頁沒有<h1>標籤
