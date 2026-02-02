# ch24_2.py
from requests_html import HTMLSession

session = HTMLSession()             # 定義Session
url = 'https://python.org/'
r = session.get(url)                # get()
url_links = r.html.links
count = 0
print('相對位址超連結數量 : ', len(url_links))
for link in url_links:
    count += 1
    print(link)
    if count >= 5:
        break
print('-'*70)
url_a_links = r.html.absolute_links
count = 0
print('絕對位址超連結數量 : ', len(url_a_links))
for link in url_a_links:
    count += 1
    print(link)
    if count >= 5:
        break

