# Python 測試 requests

print('----------------------------------------------------------------------')	#70個
print('準備工作')

import os
import sys
import csv
import json
import time
import requests
import pprint as pp
from datetime import datetime
from urllib import request
from bs4 import BeautifulSoup

def get_html_data1(url):
    print('取得網頁資料: ', url)
    resp = requests.get(url)
    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print('讀取網頁資料錯誤, url: ', resp.url)
        return None
    else:
        return resp

def get_html_data_from_url(url):
    html_data = get_html_data1(url)
    if html_data == None:
        print('無法取得網頁資料')
        sys.exit(1)	#立刻退出程式

    html_data.encoding = 'UTF-8' # 或是 unicode 也可, 指定編碼方式
    return html_data.text

print('----------------------------------------------------------------------')	#70個
print('requests 測試 1')

url = 'https://www.ptt.cc/bbs/hotboards.html'
html_data_text = get_html_data_from_url(url)

htmllist = html_data_text.splitlines()   #將網頁資料一行一行地分割成串列

n=0
for row in htmllist:
    if "音樂" in row:
        n+=1

print("找到 {} 次!".format(n))

print('----------------------------------------------------------------------')	#70個
print('requests 測試 2')


print('教育部統計處資料 很多')
url = 'http://stats.moe.gov.tw/files/detail/{}/{}_student.csv'
'''
for year in range(103, 109):
    print(url.format(year, year))
'''

print('----------------------------------------------------------------------')	#70個
print('requests 測試 3')

print('教育部統計處資料')
url = 'http://stats.moe.gov.tw/files/detail/111/111_student.csv'
html_data_text = get_html_data_from_url(url)

rows = html_data_text.split('\n')
print(rows[0])
print(rows[1])

print('----------------------------------------------------------------------')	#70個
print('requests 測試 4')

print('教育部統計處資料')
url = 'http://stats.moe.gov.tw/files/detail/108/108_student.csv'

html_data_text = get_html_data_from_url(url)
rows = html_data_text.split('\n')
data = list()
columns = rows[0].split(',')
for row in rows[1:]:
    try:
        row = row.split(',')
        item = list()
        for f_index in range(1, 5):
            item.append(row[f_index].replace('"', ''))
        data.append(item)
    except:
        pass
with open(os.path.basename(url), "w", encoding='utf-8', newline="") as fp:
    writer = csv.writer(fp)
    writer.writerow(columns[1:5])
    writer.writerows(data)
    
print("done")


print('----------------------------------------------------------------------')	#70個
print('requests 測試 5')

print('教育部統計處資料 很多')
url = 'http://stats.moe.gov.tw/files/detail/{0}/{0}_student.csv'

'''
for year in range(103, 109):
    csvdata = requests.get(url.format(year)).text
    rows = csvdata.split('\n')
    data = list()
    columns = rows[0].split(',')
    for row in rows[1:]:
        try:
            row = row.split(',')
            item = list()
            for f_index in range(1, 5):
                item.append(row[f_index].replace('"', ''))
            data.append(item)
        except:
            pass
    filename = os.path.basename(url.format(year))
    print(filename, "is writing...")
    with open(filename, "w", encoding='utf-8', newline="") as fp:
        writer = csv.writer(fp)
        writer.writerow(columns[1:5])
        writer.writerows(data)
    time.sleep(3)
'''
print("done")


print('----------------------------------------------------------------------')	#70個
print('requests 測試 6')

url = "https://www.nkust.edu.tw/p/403-1000-14-{}.php?Lang=zh-tw"

pages = list()
for pg in range(1, 4):
    pages.append(url.format(pg))

pp.pprint(pages)
print()
print(pages)

for page in pages:
    html = requests.get(page).text
    pp.pprint(html)
    time.sleep(3)
    print("=========================")


print('----------------------------------------------------------------------')	#70個
print('requests 測試 7')

url = "https://www.nkust.edu.tw/p/403-1000-14-{}.php?Lang=zh-tw"

pages = list()
for pg in range(1, 4):
    pages.append(url.format(pg))

pp.pprint(pages)
print()
print(pages)

for pg_no, page in enumerate(pages, 1):
    html = requests.get(page).text
    filename = "page-{}.txt".format(pg_no)
    with open(filename, "wt") as fp:
        fp.write(html)
    print(filename, "儲存完成！")
    time.sleep(3)
    print("=========================")

print('----------------------------------------------------------------------')	#70個
print('requests 測試 8')

#行政院農業委員會資料開放平台
url = 'https://data.coa.gov.tw/Service/OpenData/FromM/FarmTransData.aspx'

with request.urlopen(url) as res:
    data = json.loads(res.read().decode())

print(data)
print()
print(data[0])

filename = 'C:/_git/vcs/_1.data/______test_files2/products.csv'
print('將資料寫出到csv檔, 檔案 : ', filename)

with open(filename, 'w', encoding = 'big5', newline = '\n') as fp:
    writer = csv.writer(fp)
    writer.writerow(('作物名稱','平均價','交易量'))
    for item in data:
        writer.writerow((item['作物名稱'],item['平均價'],item['交易量']))

print('----------------------------------------------------------------------')	#70個

print('PC Home 電腦售價')
url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=mac%20Mini&page=1&sort=sale/dc'

html_data_text = get_html_data_from_url(url)

products = json.loads(html_data_text)['prods']
for product in products:
    if product['price'] > 20000:
        print("NT$:{}, {}".format(product['price'], product['name']))

print('----------------------------------------------------------------------')	#70個

url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=mac%20Mini&page=1&sort=sale/dc'

html_data_text = get_html_data_from_url(url)

products = json.loads(html_data_text)['prods']
message = ""
for product in products:
    if product['price'] > 20000:
        message = message + "NT$:{}, {}\n".format(product['price'], product['name'])
        
print("Mac Mini價格通知", message)


print('完成')




