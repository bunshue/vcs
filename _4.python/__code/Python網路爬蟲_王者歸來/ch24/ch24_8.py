# ch24_8.py
from requests_html import HTMLSession

session = HTMLSession()
url = 'https://movie.douban.com/'
r = session.get(url)

print('影片名稱 : ', r.html.find('li.title', first=True).text)
print('影片評分 : ', r.html.find('li.rating', first=True).text)

