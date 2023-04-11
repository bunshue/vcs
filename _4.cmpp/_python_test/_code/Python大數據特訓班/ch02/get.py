import requests
payload = {'key1': 'value1', 'key2': 'value2'}
# 將查詢參數加入 GET 請求中
html_data = requests.get("http://httpbin.org/get", params=payload)
print(html_data.url) # http://httpbin.org/get?key1=value1&key2=value2
print(html_data.text) # http://httpbin.org/get?key1=value1&key2=value2
