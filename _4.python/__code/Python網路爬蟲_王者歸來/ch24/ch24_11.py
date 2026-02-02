# ch24_11.py
from requests_html import HTMLSession

session = HTMLSession()             # 定義Session
url = 'http://python-requests.org/'
r = session.get(url)                # get()
r.html.render()
txt =  r.html.search('Python 2 will retire in only {months} months!')['months']
print(txt)






