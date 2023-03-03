# _*_ coding: utf-8 *_*
# 程式 9-4 (Python 3 version)

import requests, re

regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
url = 'http://icho.chem.ntnu.edu.tw/pub/54con/54con.html'

html = requests.get(url).text

emails = re.findall(regex,html)
for email in emails:
    print(email)
