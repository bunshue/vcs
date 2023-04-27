print('抓取網頁中的e-mail地址')

import requests, re

regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+)"
url = 'http://csharphelper.com/blog/'

html = requests.get(url, verify = False).text
    
emails = re.findall(regex, html)
for email in emails:
    print(email)
