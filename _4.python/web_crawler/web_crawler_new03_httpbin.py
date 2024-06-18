"""
測試 httpbin

"""
import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個
#共用套件

import requests

print("------------------------------------------------------------")  # 60個


# 資料
my_data = {'key1': 'value1', 'key2': 'value2'}
# 將資料加入POST 請求中
r = requests.post('http://httpbin.org/post', data = my_data)
print(r.text)
print(r.status_code)

print('------------------------------------------------------------')	#60個

print('用 httpbin 測試 檔案的 POST')

# 要上傳的檔案
my_files = {'my_filename': open('bankRate.csv', 'rb')}
# 將檔案加入POST 請求中
r = requests.post('http://httpbin.org/post', files = my_files)
print(r.status_code)

print('------------------------------------------------------------')	#60個

print('requests 測試 7b')

print('將查詢參數加入 POST 請求中')
payload = {'key1': 'value1', 'key2': 'value2'}
url = 'http://httpbin.org/post'
html_data = requests.post(url, data=payload)
print(html_data.text)

print('------------------------------------------------------------')	#60個
print('requests 測試 7c')

print('將查詢參數定義為字典資料加入GET請求中')
url = 'http://httpbin.org/get'
params = {'key1': 'value1', 'key2': 'value2'}
html_data = get_html_data2(url, params)
if html_data:
    print(html_data.text)
else:
    print('無法取得網頁資料')

print("------------------------------------------------------------")  # 60個

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

print('------------------------------------------------------------')	#60個
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

print('------------------------------------------------------------')	#60個
print('requests 測試 10 很久 timeout')

print('將查詢參數加入 GET 請求中')

payload = {'key1': 'value1', 'key2': 'value2'}
html_data = requests.post("http://httpbin.org/post", data = payload)

print(html_data.url)
print(html_data.text)



print("------------------------------------------------------------")  # 60個


'''
import requests

url = 'https://httpbin.org/get'
headers = {'Content-Type': 'text/html'}

html_data = requests.get(url, headers=headers)

print(html_data.text)
'''



print("------------------------------------------------------------")  # 60個

url = 'https://httpbin.org/get'
hd = {'user-key': '7ADGS9S'}  # 標頭參數(以字典儲存)
pm = {'id': 1023, 'neme': 'joe'}   # 網址參數(以字典儲存)
r = requests.get(url, headers = hd, params = pm)   # 加入 headers 及 params 參數
print(r.text)   # 將回應的文字印出來

print('------------------------------------------------------------')	#60個

url = 'http://httpbin.org/post' # 使用測試服務網站, POST 方法網址要加 /post
r = requests.post(url, data = 'Hello')  # 送出字串資料
print(r.text)
r = requests.post(url, data = {'id':'123', 'name':'Joe'})
print(r.text)

print('------------------------------------------------------------')	#60個

r = requests.put('https://httpbin.org/put', data = {'key':'abc'})
print(r.text)
r = requests.patch('https://httpbin.org/patch', data = {'key':'xyz'})
print(r.text)
r = requests.delete('https://httpbin.org/delete')
print(r.text)

print('------------------------------------------------------------')	#60個

url_params = {'name': '陳會安', 'grade': 95}
r = requests.get("http://httpbin.org/get", params=url_params)
if r.status_code == 200:
    print(r.text)
else:
    print("錯誤! HTTP請求失敗...")

print('------------------------------------------------------------')	#60個

url = "http://httpbin.org/user-agent"
 
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
r = requests.get(url, headers=headers)
print(r.text)

print('------------------------------------------------------------')	#60個

url = "http://httpbin.org/user-agent"
 
r = requests.get(url)
print(r.text)

print('------------------------------------------------------------')	#60個

url = "http://httpbin.org/cookies"

cookies = dict(name='Joe Chen')
r = requests.get(url, cookies=cookies)
print(r.text)

print('------------------------------------------------------------')	#60個

post_data = {'name': '陳會安', 'grade': 95}
r = requests.post("http://httpbin.org/post", data=post_data)
print(r.text)

print('------------------------------------------------------------')	#60個

""" fail
proxy = {'http': 'http://109.161.48.141:3128',
         'https': 'https://109.161.48.141:3128'}
r = requests.get("http://httpbin.org/ip", proxies=proxy)
print(r.status_code)
print(r.text)
"""

print('------------------------------------------------------------')	#60個


""" fail
from fake_useragent import UserAgent
import random

ua = UserAgent()
def proxyGenerator():
   headers = {'user-agent': ua.random}
   res = requests.get('https://free-proxy-list.net/', headers=headers)
   soup = BeautifulSoup(res.text, 'lxml') 
   proxies_table = soup.find(id='proxylisttable')
   proxies = [] 
   for row in proxies_table.tbody.find_all('tr'):
     proxies.append({  
       'http': "http://" + row.find_all('td')[0].string + ":" +
               row.find_all('td')[1].string, 
       'https': "https://" + row.find_all('td')[0].string + ":" +
               row.find_all('td')[1].string        
     })   
   return random.choice(proxies)

while True:
   proxy = proxyGenerator()
   print("目前使用的代理伺服器: ", proxy)
   try:
      headers = {'user-agent': ua.random}
      url = "http://httpbin.org/ip"
      r = requests.get(url, headers=headers, proxies=proxy, verify=False)
      print(r.status_code)
      print(r.text)
      break
   except:
      print("連線錯誤! 搜尋其他的代理伺服器!")
      pass 
"""

print('------------------------------------------------------------')	#60個


import requests
# 將查詢參數定義為字典資料加入GET請求中
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.text)


import requests
# 將查詢參數加入 POST 請求中
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)


import requests
# 將查詢參數定義為字典資料加入GET請求中
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.text)


import requests
# 將查詢參數加入 POST請求中
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)



import requests

# 將查詢參數定義為字典資料加入GET請求中
payload = {'key1': 'value1', 'key2': 'value2'}
html = requests.get("http://httpbin.org/get", params=payload)

print(html.text)



import requests

# 將查詢參數加入 POST 請求中
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)

print(r.text)

print("------------------------------------------------------------")  # 60個

# get_params.py
import requests
# 將查詢參數定義為字典資料加入GET請求中
payload = {'key1': 'value1', 'key2': 'value2'}
html = requests.get("http://httpbin.org/get", params=payload)
print(html.text)




# post.py
import requests
# 將查詢參數加入 POST 請求中
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)




print("------------------------------------------------------------")  # 60個


url_params = {'name': '陳會安', 'score': 95}
r = requests.get("http://httpbin.org/get", params=url_params)
print(r.url)

print("------------------------------------------------------------")  # 60個

""" fail
from urlencode import urlencode 

url_params = {'name': '陳會安', 'score': 95}
print(urlencode(url_params))
"""
print("------------------------------------------------------------")  # 60個

data = {'name': '陳會安', 'score': 95}
r = requests.get("http://httpbin.org/get", params=data)
print(r.text)

print("------------------------------------------------------------")  # 60個

post_data = {'name': '陳會安', 'score': 95}
r = requests.post("http://httpbin.org/post", data=post_data)
print(r.text)

print("------------------------------------------------------------")  # 60個


import requests

url = "http://httpbin.org/cookies"

cookies = dict(name='Joe Chen')
r = requests.get(url, cookies=cookies)
print(r.text)

print("------------------------------------------------------------")  # 60個

import requests

url = "http://httpbin.org/user-agent"

r = requests.get(url)
print(r.text)
print("----------------------")

url_headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}
r = requests.get(url, headers=url_headers)
print(r.text)

print("------------------------------------------------------------")  # 60個

print('使用POST方式抓取數據')

import requests
params = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=params)
print(r.text)


print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



