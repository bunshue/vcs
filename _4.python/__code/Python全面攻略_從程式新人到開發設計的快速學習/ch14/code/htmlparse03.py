import requests
from bs4 import BeautifulSoup

urlstr='http://www.drmaster.com.tw/Publish_Newbook.asp'

responseObj=requests.get(urlstr)
responseObj.encoding="utf-8"
bs=BeautifulSoup(responseObj.text, 'html.parser')
print(bs.title.text)
data=bs.select('.style2')
count=len(data)
print("共 %d 筆新書記錄" %(count))

for book in data:
    print(book.text)
    
    
    
