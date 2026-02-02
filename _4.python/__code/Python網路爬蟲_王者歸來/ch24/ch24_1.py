# ch24_1.py
from requests_html import HTMLSession

session = HTMLSession()             # 定義Session
url = 'http://aaa.24ht.com.tw'
r = session.get(url)                # get()
print(type(r))
print(type(r.html))
print(r.html)
print(type(r.html.text))
print('-'*70)
print(r.html.text)



