# ch24_4.py
from requests_html import HTMLSession

session = HTMLSession()             # 定義Session
url = 'https://python.org/'
r = session.get(url)                # get()
about = r.html.find('#about', first=True)
print('about.attrs屬性')
print(about.attrs)
print('-'*70)
print('about.html屬性')
print(about.html)
print('-'*70)
print('about.absolute_links屬性')
print(about.attrs)
print('-'*70)
print("about.find('a')")
print(about.find('a'))

