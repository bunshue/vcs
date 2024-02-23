# 注意，本範例會隨著網站更新而導致無法爬文，若有問題可來信討論

# 引用相關套件
import requests
from bs4 import BeautifulSoup          
# 指定url變數為「Dcard熱門文章」網頁的網址    
url = 'https://www.dcard.tw/f'
response = requests.get(url)
bs=BeautifulSoup(response.text,'lxml')        # 取得物件
#取得所有文章程式碼
listItems = bs.find_all('article', 'sc-1v1d5rx-0 lmtfq')  

for item in listItems: 
    time = item.find_all('span', 'sc-6oxm01-2 hiTIMq')[2]   #發文時間
    print('發文時間:',time.text)
    print('文章標題:',item.h2.text)     #文章標題
    URl = item.find('a').get('href')    #文章網址
    print('文章網址: https://www.dcard.tw'+URl)
    print('='*70)
print('取得文章數量 =', len(listItems))
