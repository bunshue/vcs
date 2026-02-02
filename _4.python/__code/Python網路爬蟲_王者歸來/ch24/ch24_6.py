# ch24_6.py
from requests_html import HTMLSession

session = HTMLSession()             # 定義Session
url = 'https://github.com/'
r = session.get(url)                # get()
a_element = r.html.xpath('a')
if a_element:
    for a in a_element:
        print(a)
        print('-'*70)
