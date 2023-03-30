import requests

'''
#讀取html檔
from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())



import urllib.request
input = urllib.request.urlopen('http://www.yahoo.com/index.html')
print(input.read())
'''


import requests

response = requests.get("https://www.ptt.cc/bbs/C_Chat/index.html")    # 以ptt C_Chat版為例
print(response.text)
print(response.status_code)



    



