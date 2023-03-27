import requests

print('檢查HTTP回應碼是否為200(requests.code.ok)')
url = 'http://www.ehappy.tw/demo.htm'
html_data = requests.get(url)
if html_data.status_code == requests.codes.ok:
    print("擷取網頁資料 OK")
    print(html_data.text)
else:
    print("擷取網頁資料 NG")


print('將查詢參數加入 POST 請求中')
payload = {'key1': 'value1', 'key2': 'value2'}
url = 'http://httpbin.org/post'
html_data = requests.post(url, data=payload)
print(html_data.text)

print('將查詢參數定義為字典資料加入GET請求中')
payload = {'key1': 'value1', 'key2': 'value2'}
url = 'http://httpbin.org/get'
html_data = requests.get(url, params=payload)
print(html_data.text)



print('設定查詢目前IP的api網址')
url = 'https://api.ipify.org'
html_data = requests.get(url)
print('我目前的IP是：', html_data.text)


print('設定cookies的值')

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
cookies = {'over18':'1'}
html_data = requests.get(url, cookies=cookies)
print(html_data.text)


'''
print('將自訂表頭加入 GET 請求中')

url = 'https://irs.thsrc.com.tw/IMINT/'
# 自訂表頭
headers={
   'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}
html_data = requests.get(url, headers=headers)
print(html_data)
'''

print("抓取網頁資料 2")
#url = 'https://httpbin.org/get?value1=1&value2=2'
url = 'https://tw.dictionary.search.yahoo.com/?value1=lion'
#url = 'https://www.google.com.tw/'
html_data = requests.get(url)
print(html_data.text)
print(html_data.status_code)
if html_data.status_code == requests.codes.ok:
    print("抓取網頁OK")
else:
    print("抓取網頁NG")


print("抓取網頁資料 3")

url = 'http://udb.moe.edu.tw/Home/About'
#html = requests.get(url).text.splitlines()
for i in range(0,15):
    print(i)
    #print(html[i])






