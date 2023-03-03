# _*_ coding: utf-8 _*_
# 程式 9-3 (Python 3 version)

import requests

url = 'http://www.com.tw/exam/check_0001_NO_0_101_0_3.html'
name = input("請輸入要查詢的姓名:")
html = requests.get(url).text
if name in html:
    print("恭喜名列金榜")
else:
    print("不好意思，榜單中找不到{}".format(name))
