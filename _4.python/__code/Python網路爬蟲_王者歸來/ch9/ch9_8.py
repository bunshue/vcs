# ch9_8.py
import requests, bs4

url = 'https://movies.yahoo.com.tw/chart.html'              # 本周排行榜的網址
moviehtml = requests.get(url)
objSoup = bs4.BeautifulSoup(moviehtml.text, 'lxml')         # 取得排行榜的HTML

itemsobj = objSoup.find('ul', 'ranking_list_r')             # 排行榜在此資料區間
items = itemsobj.find_all('li')
print("台北本週票房排行榜\n")
for item in items:
    name = item.span.text
    rank = item.find('div', 'num')
    print('片名 : ', name)
    print('名次 : ', rank.text)
    print()


    
    

    





















