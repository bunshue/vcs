import requests
url = 'http://www.e-happy.com.tw'
html = requests.get(url)
html.encoding="utf-8"
if html.status_code == requests.codes.ok:
    print(html.text)


import requests
from bs4 import BeautifulSoup
url = 'http://www.e-happy.com.tw'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')


import requests
from bs4 import BeautifulSoup
payload = {
   'from': 'https://www.ptt.cc/bbs/Gossiping/index.html',
	'yes': 'yes'
}
headers = {
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
rs = requests.Session()
rs.post('https://www.ptt.cc/ask/over18', data=payload, headers=headers)
res = rs.get('https://www.ptt.cc/bbs/Gossiping/index.html', headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')
items = soup.select('.r-ent')
for item in items:
    print(item.select('.date')[0].text, item.select('.author')[0].text, item.select('.title')[0].text)
