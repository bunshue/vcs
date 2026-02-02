# ch3_18.py
import urllib.request

url = 'https://www.mcut.edu.tw'
htmlfile = urllib.request.urlopen(url)
print('版本 : ', htmlfile.version)
print('網址 : ', htmlfile.geturl())
print('下載 : ', htmlfile.status)
print('表頭 : ')
for header in htmlfile.getheaders():
    print(header)










