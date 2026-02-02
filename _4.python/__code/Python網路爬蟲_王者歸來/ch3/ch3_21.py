# ch3_21.py
from urllib import parse

s = '台灣積體電路製造'
url_code = parse.quote(s)
print('URL編碼  : ', url_code)
code = parse.unquote(url_code)
print('中文編碼 : ', code)


    












