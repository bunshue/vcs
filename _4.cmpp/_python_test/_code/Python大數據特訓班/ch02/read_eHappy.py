import requests
url = 'http://www.e-happy.com.tw'
html = requests.get(url)
html.encoding="utf-8"
if html.status_code == requests.codes.ok:
    print(html.text)