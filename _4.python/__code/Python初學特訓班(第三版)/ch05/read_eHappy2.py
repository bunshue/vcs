import requests
url = 'http://www.e-happy.com.tw'
html = requests.get(url)
html.encoding="utf-8"

htmllist = html.text.splitlines()
for row in htmllist:
   print(row)