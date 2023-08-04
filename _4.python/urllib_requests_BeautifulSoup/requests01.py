# Python 測試 requests

print('----------------------------------------------------------------------')	#70個
print('準備工作')

import re
import os
import sys
import csv
import json
import time
import codecs
import pprint
import requests
from datetime import datetime

#無參數
def get_html_data1(url):
    print('無參數取得網頁資料: ', url)
    resp = requests.get(url)
    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print('讀取網頁資料錯誤, url: ', resp.url)
        return None
    else:
        return resp

#有參數
def get_html_data2(url, params):
    print('有參數取得網頁資料: ', url)
    print('參數: ', params)
    resp = requests.get(url = url, params = params) #有參數的GET請求
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
print('requests 測試 1 無參數 取得網頁資料 只是把網頁抓下來')

url = 'https://tw.news.yahoo.com/most-popular/'
url = 'http://www.itwhy.org'
url = 'http://www.ehappy.tw/demo.htm'
url = 'http://tw.yahoo.com'

html_data = get_html_data1(url)
if html_data:
    print("擷取網頁資料 OK")
    #print(html_data.text)  #OK many
    #pprint.pprint(html_data.text)  #OK many
else:
    print('無法取得網頁資料')

print('----------------------------------------------------------------------')	#70個
print('requests 測試 2 有參數 取得網頁資料 只是把網頁抓下來')

print('有參數 取得網頁資料 a')
url = 'http://dict.baidu.com/s'
params = {'wd':'python'}

html_data = get_html_data2(url, params)

print('111', html_data.url)
print('222', html_data.text) #打印解码后的返回数据
print('333', html_data)


print('有參數 取得網頁資料 b')
url = 'https://zh.wikipedia.org/w/api.php'
params = {'format':'json', 'action':'query', 'titles':'椎名林檎', 'prop':'revisions', 'rvprop':'content'}
html_data = get_html_data2(url, params)
pprint.pprint(html_data)


print('有參數 取得網頁資料 c')
url = 'https://zh.wikipedia.org/w/api.php'
params = {'format':'xmlfm', 'action':'query', 'titles':'椎名林檎', 'prop':'revisions', 'rvprop':'content'}
html_data = get_html_data2(url, params)
fo = codecs.open('wiki搜尋結果1.html', 'w', 'utf-8')
#fo = open('wiki搜尋結果222.html', 'w')
fo.write(html_data.text)
fo.close()

print('有參數 取得網頁資料 d')
search_word = 'lion'
url = 'https://zh.wikipedia.org/w/api.php'
params = {'format':'xmlfm', 'action':'query', 'prop':'revisions', 'rvprop':'content'}
params['titles'] = search_word
html_data = get_html_data2(url, params)
fo = codecs.open('wiki搜尋結果2' + search_word + '.html', 'w', 'utf-8')
#fo = open('bbbbb'+ search_word + '.html', 'w')
fo.write(html_data.text)
fo.close()

print('----------------------------------------------------------------------')	#70個

'''
print('----------------------------------------------------------------------')	#70個
print('requests 測試 7b')

print('將查詢參數加入 POST 請求中')
payload = {'key1': 'value1', 'key2': 'value2'}
url = 'http://httpbin.org/post'
html_data = requests.post(url, data=payload)
print(html_data.text)

print('----------------------------------------------------------------------')	#70個
print('requests 測試 7c')

print('將查詢參數定義為字典資料加入GET請求中')
url = 'http://httpbin.org/get'
params = {'key1': 'value1', 'key2': 'value2'}
html_data = get_html_data2(url, params)
if html_data:
    print(html_data.text)
else:
    print('無法取得網頁資料')

'''

'''
print('將自訂表頭加入 GET 請求中')

url = 'https://irs.thsrc.com.tw/IMINT'		#台灣高鐵訂票系統

# 自訂表頭
headers={
   'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}
html_data = requests.get(url, headers = headers)
print(html_data)

print("抓取網頁資料 2")
#url = 'https://httpbin.org/get?value1=1&value2=2'
url = 'https://tw.dictionary.search.yahoo.com/?value1=lion'
#url = 'https://www.google.com.tw/'
html_data = get_html_data1(url)
if html_data:
    print("抓取網頁OK")
    #print(html_data.text)
else:
    print("抓取網頁NG")

'''

print('----------------------------------------------------------------------')	#70個
print('requests 測試 9')

print('將查詢參數加入 GET 請求中')

payload = {'key1': 'value1', 'key2': 'value2'}
html_data = requests.get("http://httpbin.org/get", params = payload)

print(html_data.url)    # http://httpbin.org/get?key1=value1&key2=value2
print(html_data.text)   # http://httpbin.org/get?key1=value1&key2=value2


payload = {'title': '獅子'}
html_data = requests.get('https://zh.wikipedia.org/w/index.php', params = payload)

#相當於寫了 : https://zh.wikipedia.org/w/index.php?title=獅子

print(html_data.url)
print(html_data.text)

print('----------------------------------------------------------------------')	#70個
print('requests 測試 10 很久 timeout')
'''

print('將查詢參數加入 GET 請求中')

payload = {'key1': 'value1', 'key2': 'value2'}
html_data = requests.post("http://httpbin.org/post", data = payload)

print(html_data.url)
print(html_data.text)
'''

print('----------------------------------------------------------------------')	#70個
print('requests 測試 11')

url = 'https://www.ptt.cc/bbs/hotboards.html'
html_data_text = get_html_data_from_url(url)

htmllist = html_data_text.splitlines()   #將網頁資料一行一行地分割成串列

n=0
for row in htmllist:
    if "音樂" in row:
        n+=1

print("找到 {} 次!".format(n))

print('----------------------------------------------------------------------')	#70個
print('requests 測試 12')

print('教育部統計處資料 很多')
url = 'http://stats.moe.gov.tw/files/detail/{}/{}_student.csv'
'''
for year in range(103, 109):
    print(url.format(year, year))
'''

print('----------------------------------------------------------------------')	#70個
print('requests 測試 13')

print('教育部統計處資料')
url = 'http://stats.moe.gov.tw/files/detail/111/111_student.csv'
html_data_text = get_html_data_from_url(url)

rows = html_data_text.split('\n')
print(rows[0])
print(rows[1])

print('----------------------------------------------------------------------')	#70個
print('requests 測試 14')

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
print('requests 測試 15')

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
print('requests 測試 16')

url = "https://www.nkust.edu.tw/p/403-1000-14-{}.php?Lang=zh-tw"

'''many
pages = list()
for pg in range(1, 4):
    pages.append(url.format(pg))

pprint.pprint(pages)
print()
print(pages)

for page in pages:
    html = requests.get(page).text
    pprint.pprint(html)
    time.sleep(3)
    print("=========================")
'''

print('----------------------------------------------------------------------')	#70個
print('requests 測試 17')

url = "https://www.nkust.edu.tw/p/403-1000-14-{}.php?Lang=zh-tw"

pages = list()
for pg in range(1, 4):
    pages.append(url.format(pg))

pprint.pprint(pages)
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
print('requests 測試 19')

print('PC Home 電腦售價')
url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=mac%20Mini&page=1&sort=sale/dc'

html_data_text = get_html_data_from_url(url)

products = json.loads(html_data_text)['prods']
for product in products:
    if product['price'] > 20000:
        print("NT$:{}, {}".format(product['price'], product['name']))

print('----------------------------------------------------------------------')	#70個
print('requests 測試 20')

url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=mac%20Mini&page=1&sort=sale/dc'

html_data_text = get_html_data_from_url(url)

products = json.loads(html_data_text)['prods']
message = ""
for product in products:
    if product['price'] > 20000:
        message = message + "NT$:{}, {}\n".format(product['price'], product['name'])
        
print("Mac Mini價格通知", message)

print('----------------------------------------------------------------------')	#70個
print('requests 測試 21 中油油價')

url = "https://www.cpc.com.tw/historyprice.aspx?n=2890"
html_data = requests.get(url)

m = re.search("var pieSeries = (.*);", html_data.text)
jsonstr = m.group(0).strip('var pieSeries = ').strip(";")
j = json.loads(jsonstr)
#print(j)
cnt = 1
for item in reversed(j):    #反向排序, 利用 reversed 反轉了排序(原內容由舊到新, 利用這個改為由新到舊)
    new_line = 0
    for data in item['data']:
        if(data['name'] == '超級/高級柴油'):
            new_line = 0
            continue
        else:
            new_line = 1
        print("date:" + item['name'])   #第一層的 name 為日期
        print(data['name'] + ":" + str(data['y']))  #後面再接一層 array data 其中的 name 為產品名, 而 y 為單價
    if (new_line == 1):
        print("================")

    cnt += 1
    if cnt == 10:
        break

print('----------------------------------------------------------------------')	#70個
print('requests 測試 22')

import requests

url = "https://udn.com/api/more?page=2&id=&channelId=1&cate_id=0&type=breaknews&totalRecNo=6561"

'''many
data = requests.get(url).text
print(data)
'''

print('----------------------------------------------------------------------')	#70個
print('requests 測試 22')

import requests
import re

print('抓取網頁中的電話號碼')

url = 'https://www.taichung.gov.tw/10179/12034/'

html = requests.get(url).text

regex04a = r'\(\d{2}\)\d{4}-?\d{4}'
regex04b = r'\d{2}-\d{4}-?\d{4}'
regex0800 = r'0800-\d{6}'
matches = re.findall(regex04a, html)
matches += re.findall(regex04b, html)
matches += re.findall(regex0800, html)

for match in matches:
    print('抓到符合條件的 : ', match)
    
print('全部資料')
print(matches)




print('----------------------------------------------------------------------')	#70個

import requests

print('查詢一個網頁有出現的詞的次數')

url = 'https://udn.com/news/breaknews/1/99#breaknews'

resp = requests.get(url)
html = resp.text
print(resp.status_code)

q = input("請輸入你要查詢的詞：")
while q != "":
    print('出現次數 : ', html.count(q))
    q = input("請輸入你要查詢的詞：")








print('----------------------------------------------------------------------')	#70個

print('抓取網頁中的e-mail地址')

import requests, re

regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+)"
url = 'http://csharphelper.com/blog/'

html = requests.get(url, verify = False).text
    
emails = re.findall(regex, html)
for email in emails:
    print(email)




print('----------------------------------------------------------------------')	#70個


import requests
import re

print('抓取網頁內的所有圖片連結')

url = 'https://www.bagong.cn/dog/'

html = requests.get(url).text

regex = r'https?://.+.jpg'
photos = re.findall(regex, html)
for photo in photos:
    print(photo)



print('----------------------------------------------------------------------')	#70個





print('----------------------------------------------------------------------')	#70個








print('完成')










