# Python 測試 urllib

print('------------------------------------------------------------')	#60個
print('準備工作')

import csv
import sys
import urllib
import urllib.request   #用來建立請求


print('下載圖片')
url = 'https://upload.wikimedia.org/wikipedia/commons/0/02/Festessen_Kaiser_Wilhelm_1898_%28front_page%29.jpg'

filename = 'cccc.jpg'
print('圖片寫出到本地檔案')
fp = open(filename, "wb")

response = urllib.request.urlopen(url)

#img = response.read()   #一次下載整個檔案, 改成分段下載
#fp.write(img)

size = 0
while True:
    info = response.read(100000)
    if len(info) < 1:
        break
    size = size + len(info)
    fp.write(info)
    print('已下載下載 ', size, '拜')

print(size, ' 拜下載')
fp.close()
response.close()

print('抓取圖片完成 並存檔成 : ' + filename)
print('OK')


