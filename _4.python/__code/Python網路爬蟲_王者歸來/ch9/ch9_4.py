# ch9_4.py
import requests, bs4

url = 'https://movies.yahoo.com.tw/movie_thisweek.html'     # 本周新片的網址
moviehtml = requests.get(url)
objSoup = bs4.BeautifulSoup(moviehtml.text, 'lxml')         # 取得新片網址的HTML

movieNum = 0
items = objSoup.find_all('div', 'release_info')             # 新片在此資料區間
for item in items:
    cName = item.find('div', 'release_movie_name').a.text.strip()   # 中文片名
    eName = item.find('div', 'en').a.text.strip()                   # 英文片名
    rTime = item.find('div', 'release_movie_time')          # 上映日期
    level = item.find('div', 'leveltext').span.text.strip() # 期待度
    txt = item.find('div', 'release_text').text.strip()     # 內容摘要
    movieNum += 1
    print('新片編號 : ', movieNum)
    print('中文片名 : ', cName)
    print('英文片名 : ', eName)
    print(rTime.text)                                       # 列印上映日期
    print('期待度   : ', level)
    print('內容摘要 : ', txt)
    print()




    
    

    





















