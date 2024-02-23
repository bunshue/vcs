import requests
from bs4 import BeautifulSoup
#博客來寵物電子書
url='https://www.books.com.tw/web/sys_cebbotm/cebook/1003/?loc=P_0001_2_003' 
response=requests.get(url)#使用requests的get()方法傳回可擷取網頁資訊response物件
response.encoding = 'utf-8'    #設定編碼模式避免亂碼
#使用BeautifulSoup()函式取得解析網頁的BeautifulSoup物件bs
bs=BeautifulSoup(response.text,'lxml')
listAll=bs.find_all('div',class_='item')   #取得<div class="item">標籤的內容
for book in listAll:  				#將資料利用迴圈依序解析
    listClass=book.get('class')         #傳回目前標籤的類別資訊
    if len(listClass)==2:           	#['item', 'clearfix']總數為2，即目前有兩個類別
        if listClass[1]=='clearfix':  #遇到clearfix類別時，跳出本次迴圈
            continue  
    print((book.find('h4').find('a').text))  #搜尋第一個<h4>內的第一個<a>標籤，即書名
