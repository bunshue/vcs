import requests
from bs4 import BeautifulSoup
# 博碩文化新書網頁
urlstr='http://www.drmaster.com.tw/Publish_Newbook.asp'  
response=requests.get(urlstr)
response.encoding="utf-8"
bs=BeautifulSoup(response.text, 'html.parser')
print(bs.title.text)    # 顯示網頁title標題
listBookName=bs.select('.style2')
count=len(listBookName)
print("共 %d 筆新書記錄" %(count))  # 顯示 '共 20 筆新書記錄'

# 顯示網頁新書書名
for book in listBookName:
    print(book.text)
    
    
    
