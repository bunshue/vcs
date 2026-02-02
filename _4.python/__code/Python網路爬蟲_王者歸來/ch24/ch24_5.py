# ch24_5.py
from requests_html import HTMLSession

session = HTMLSession()             # 定義Session
url = 'http://python-requests.org/'
r = session.get(url)                # get()
a_element = r.html.find('a', containing='kenneth')
if a_element:
    for a in a_element:
        print(a)
