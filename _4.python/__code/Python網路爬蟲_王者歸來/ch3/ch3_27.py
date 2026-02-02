# ch3_27.py
from urllib import request, error

headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }
# 錯誤網址
url_error = 'http://aaa.24t.com.tw/'            # 錯誤網址
try:
    htmlfile = request.urlopen(url_error)
except error.URLError as e:
    print('錯誤原因 : ', e.reason)
else:
    print("擷取網路資料成功")
# 正確網址
url = 'http://aaa.24ht.com.tw/'                 # 網址正確
try:
    req = request.Request(url, headers=headers)
    htmlfile = request.urlopen(req)
except error.URLError as e:
    print('錯誤原因 : ', e.reason)
else:
    print("擷取網路資料成功")
