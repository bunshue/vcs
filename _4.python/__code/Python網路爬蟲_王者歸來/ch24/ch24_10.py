# ch24_10.py
from requests_html import HTMLSession

session = HTMLSession()
url = 'https://movie.douban.com/'
r = session.get(url)

movies = r.html.find('li.ui-slide-item')
count = 0
for m in movies:
    count += 1
    print('影片編號 : ', count)
    print('影片名稱 : ', m.attrs['data-title'])
    print('影片評分 : ', m.attrs['data-rate'])
    print('-'*70)
    if count == 20:
        break


    

