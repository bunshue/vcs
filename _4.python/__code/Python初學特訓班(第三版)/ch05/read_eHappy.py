import requests
url = 'http://www.e-happy.com.tw'
html = requests.get(url)
html.encoding="utf-8"
print(html.text)