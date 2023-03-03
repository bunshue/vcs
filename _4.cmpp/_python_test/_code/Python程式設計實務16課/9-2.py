# _*_ coding: utf-8 _*_
# 程式 9-2  (Python 3 version)

import requests

url = 'http://udb.moe.edu.tw/Home/About'

html = requests.get(url).text.splitlines()
for i in range(0,15):
    print(html[i])