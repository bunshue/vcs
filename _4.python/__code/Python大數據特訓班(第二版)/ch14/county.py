# 網址：http://www.ibon.com.tw/retail_inquiry.aspx#gsc.tab=0

import requests
url = 'http://www.ibon.com.tw/retail_inquiry_ajax.aspx'
payload = {'strTargetField': 'COUNTY', 'strKeyWords': '南投縣'}
html = requests.post(url, data=payload)
html.encoding='utf-8'

from bs4 import BeautifulSoup
soup = BeautifulSoup(html.text, 'html.parser')
datas = soup.find_all('tr')
print(datas[0:3]) # 顯示前 3 筆表格資料

del datas[0]  # 去掉表頭
for data in datas:
    items = data.find_all('td')
    for item in items:
        print(item.text.strip() , end=',')
    print()