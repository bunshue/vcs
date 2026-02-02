# ch9_6.py
import requests, bs4

url = 'https://movies.yahoo.com.tw/movie_thisweek.html'     # 本周新片的網址
moviehtml = requests.get(url)
objSoup = bs4.BeautifulSoup(moviehtml.text, 'lxml')         # 取得新片網址的HTML

movieNum = 0
items = objSoup.find_all('div', 'release_info')             # 新片在此資料區間
for item in items:
    cName = item.find('div', 'release_movie_name').a.text.strip()   # 中文片名
    eName = item.find('div', 'en').a.text.strip()                   # 英文片名
    photo = item.find_previous_sibling('div', 'release_foto').a.img['src']
    movieNum += 1
    print('新片編號 : ', movieNum)
    print('中文片名 : ', cName)
    print('英文片名 : ', eName)
    print('海報網址 : ', photo)
    print()




    
    

    





















