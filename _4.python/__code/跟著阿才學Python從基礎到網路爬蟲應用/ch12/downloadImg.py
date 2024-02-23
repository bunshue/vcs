# 引用相關套件
import requests
from bs4 import BeautifulSoup
# 指定url變數為「博客來電子寵物書」網頁的網址
url='https://www.books.com.tw/web/sys_cebbotm/cebook/1003/?loc=P_0001_2_003' 
response=requests.get(url)# 建立取得網頁資訊的Response物件，物件名稱為response
response.encoding = 'utf-8'    #設定編碼模式避免亂碼
#使用BeautifulSoup()函式取得解析網頁的BeautifulSoup物件bs
bs=BeautifulSoup(response.text,'lxml')
Img=bs.select('div.item>a>img')  #擷取有圖片網址的<img>標籤
for link in Img:     
    #使用split()方法解析網址
    src=link.get('src') 
    ImgUrl=src.split('=')[1].split('&')[0]
    print('圖片網址:',ImgUrl)
    ImgName=ImgUrl.split('/')[-1]
    print('圖片名稱:',ImgName)
    try:  #下載圖片
        Rpimg=requests.get(ImgUrl) #建立下載圖片的Response物件Rpimg
        f=open((ImgName),'wb')    #開啟圖片檔案                    
        f.write(Rpimg.content)     #下載圖片
        f.close()
        print(ImgName,'下載完畢')
    except:
        print('下載失敗')
        f.close() 
print('執行完畢')
