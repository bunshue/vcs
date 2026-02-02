# ch3_19.py
import urllib.request

headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }
url = 'http://aaa.24ht.com.tw/'
req = urllib.request.Request(url, headers=headers)
htmlfile = urllib.request.urlopen(req)
print(htmlfile.read().decode('utf-8'))





