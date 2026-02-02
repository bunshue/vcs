# ch6_10.py
import requests
import hashlib
import json

url = 'http://opendata.epa.gov.tw/webapi/Data/REWIQA/?$orderby=SiteName&$\
skip=0&$top=1000&format=json'
try:
    aqijsons = requests.get(url)                # 將檔案下載至htmlfile
    print('下載成功')
except Exception as err:
    print('下載失敗')

data = hashlib.md5()
data.update(aqijsons.text.encode('utf-8'))
hashdata = data.hexdigest()
print('環保署PM2.5的哈希值 = ', hashdata)

fn = "out6_10.txt"
with open(fn, 'w') as fileobj:
    fileobj.write(hashdata)










    















