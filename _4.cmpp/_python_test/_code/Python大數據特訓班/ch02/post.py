import requests
payload = {'key1': 'value1', 'key2': 'value2'}
# 將查詢參數加入 POST 請求中
html = requests.post("http://httpbin.org/post", data=payload)
print(html.text)
