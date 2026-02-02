# ch24_9.py
from requests_html import HTMLSession

session = HTMLSession()
url = 'https://movie.douban.com/'
r = session.get(url)

movies = r.html.find('li.ui-slide-item')
print('影片數量 : ', len(movies))
print('數據型態 : ', type(movies[0]))
print(movies[0])
print('-'*70)
print(movies[0].attrs['data-title'])
print(movies[0].attrs['data-rate'])
