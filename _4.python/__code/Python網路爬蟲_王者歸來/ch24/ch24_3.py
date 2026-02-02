# ch24_3.py
from requests_html import HTMLSession

session = HTMLSession()             # 定義Session
url = 'https://python.org/'
r = session.get(url)                # get()
about = r.html.find('#about', first=True)
print(about.text)



