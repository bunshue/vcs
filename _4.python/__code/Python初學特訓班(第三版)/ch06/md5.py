import hashlib
import os
import requests

print('以md5檢查網站內容是否更新')

#環保署資料網址要修改
#url = "http://opendata.epa.gov.tw/ws/Data/REWXQA/?$orderby=SiteName&$skip=0&$top=1000&format=json"
url = 'https://data.epa.gov.tw/api/v2/aqx_p_488?format=csv&year_month=2023_04&offset=0&limit=100&api_key=9e273741-dad9-4c98-86cc-73e75137f66c&filters=SiteName,EQ,馬公'

# 讀取網頁原始碼
html = requests.get(url).text.encode('utf-8-sig')
print(html)

# 判斷網頁是否更新
md5 = hashlib.md5(html).hexdigest()
print('新md5 : ', md5)

if os.path.exists('old_md5.txt'):
    print('111')
    with open('old_md5.txt', 'r') as f:
        print('111a')
        old_md5 = f.read()
    with open('old_md5.txt', 'w') as f:
        print('111b')
        f.write(md5)
else:
    print('222')
    with open('old_md5.txt', 'w') as f:
        print('222a')
        f.write(md5)

print('舊md5 : ', old_md5)

if md5 != old_md5:
    print('資料已更新...') 
else:
    print('資料未更新，從資料庫讀取...')
