# 引用相關套件
import requests ,csv   
from bs4 import BeautifulSoup
# 指定url變數為「博客來電子寵物書」網頁的網址
url='https://www.books.com.tw/web/sys_cebbotm/cebook/1003/?loc=P_0001_2_003' 
# 建立取得網頁資訊的Response物件，物件名稱為response
response=requests.get(url)
# 建立解析網頁的BeautifulSoup物件，物件名稱為bs
bs=BeautifulSoup(response.text,'lxml')
# 分別取的商品名稱以及價格標籤，並指定給對應串列
listName=bs.select('div.item>div.msg>h4>a')      
listPress=bs.select('li.info>span>a')
listPrice=bs.select('li.set2')
# 將listName與listPirce串列的資料依序存入booklist.csv檔中
f=open('booklist.csv','w',encoding="utf-8-sig",newline='')
write=csv.writer(f)
write.writerow(['書名','出版社','價格'])
for i in range(0,len(listName)):   
    #分析價格內容，只擷取數字部分
    Price=listPrice[i].text.split('：')[1].split('元')[0].split('折')[-1]
    # 使用text屬性，將標籤內的資料寫入csv檔中
    write.writerow([listName[i].text,listPress[i].text,Price])
    print(listName[i].text,listPress[i].text,Price)   
f.close()	
