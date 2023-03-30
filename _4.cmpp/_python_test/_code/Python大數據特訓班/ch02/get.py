import requests
payload = {'key1': 'value1', 'key2': 'value2'}
# 將查詢參數加入 GET 請求中
html = requests.get("http://httpbin.org/get", params=payload)
print(html.url) # http://httpbin.org/get?key1=value1&key2=value2
