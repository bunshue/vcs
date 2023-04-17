import requests

#無參數
def get_html_data1(url):
    print('取得網頁資料: ', url)
    resp = requests.get(url)
    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print('讀取網頁資料錯誤, url: ', resp.url)
        return None
    else:
        return resp

'''
#無參數
    
print('取得網頁資料 1')
url = 'https://tw.news.yahoo.com/most-popular/'
url = 'http://www.itwhy.org'
url = 'http://tw.yahoo.com'
html_data = get_html_data1(url)
if html_data:
    print(html_data.text)
else:
    print('無法取得網頁資料')


print('取得網頁資料 2')
import pprint
url = 'http://tw.yahoo.com'
html_data = get_html_data1(url)
if html_data:
    print('OK')
    #pprint.pprint(html_data.text)  #OK many
else:
    print('無法取得網頁資料')

'''

#有參數
def get_html_data2(api_url, api_params):
    print('取得網頁資料: ', api_url)
    print('參數: ', api_params)
    resp = requests.get(url = api_url, params = api_params) #带参数的GET请求
    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print('讀取網頁資料錯誤, url: ', resp.url)
        return None
    else:
        return resp

'''
#有參數
print('取得網頁資料 3')
api_url = 'http://dict.baidu.com/s'
api_params = {'wd':'python'}
html_data = get_html_data2(api_url, api_params)

print('111', html_data.url)
print('222', html_data.text) #打印解码后的返回数据
print('333', html_data)

print('取得網頁資料 4')
import pprint
api_url = 'https://zh.wikipedia.org/w/api.php'
api_params = {'format':'json', 'action':'query', 'titles':'椎名林檎', 'prop':'revisions', 'rvprop':'content'}
html_data = get_html_data2(api_url, api_params)
pprint.pprint(html_data)


print('取得網頁資料 5')
import codecs
api_url = 'https://zh.wikipedia.org/w/api.php'
api_params = {'format':'xmlfm', 'action':'query', 'titles':'椎名林檎', 'prop':'revisions', 'rvprop':'content'}
html_data = get_html_data2(api_url, api_params)
fo = codecs.open('wiki搜尋結果1.html', 'w', 'utf-8')
#fo = open('wiki搜尋結果222.html', 'w')
fo.write(html_data.text)
fo.close()


print('取得網頁資料 6')
import codecs
search_word = 'lion'
api_url = 'https://zh.wikipedia.org/w/api.php'
api_params = {'format':'xmlfm', 'action':'query', 'prop':'revisions', 'rvprop':'content'}
api_params['titles'] = search_word
html_data = get_html_data2(api_url, api_params)
fo = codecs.open('wiki搜尋結果2' + search_word + '.html', 'w', 'utf-8')
#fo = open('bbbbb'+ search_word + '.html', 'w')
fo.write(html_data.text)
fo.close()

import requests

url = 'http://www.ehappy.tw/demo.htm'
html_data = get_html_data1(url)
if html_data:
    print("擷取網頁資料 OK")
    print(html_data.text)
else:
    print('無法取得網頁資料')

print('將查詢參數加入 POST 請求中')
payload = {'key1': 'value1', 'key2': 'value2'}
url = 'http://httpbin.org/post'
html_data = requests.post(url, data=payload)
print(html_data.text)

print('將查詢參數定義為字典資料加入GET請求中')
api_url = 'http://httpbin.org/get'
api_params = {'key1': 'value1', 'key2': 'value2'}
html_data = get_html_data2(api_url, api_params)
if html_data:
    print(html_data.text)
else:
    print('無法取得網頁資料')

print('將自訂表頭加入 GET 請求中')

url = 'https://irs.thsrc.com.tw/IMINT/'
# 自訂表頭
headers={
   'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}
html_data = requests.get(url, headers = headers)
print(html_data)
'''

'''

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

print('BeautifulSoup 測試 2')

import requests
from bs4 import BeautifulSoup
url = 'http://www.e-happy.com.tw'
html_data = requests.get(url)
soup = BeautifulSoup(html_data.text, 'html.parser')
print(soup.prettify())

import pprint as pp
pp.pprint(html_data.text)


