# ch24_7.py
from requests_html import HTMLSession

session = HTMLSession()             # 定義Session
url = 'https://python.org/'
r = session.get(url)                # get()
txt = r.html.search('Python is a {} language')[0]
print(txt)




