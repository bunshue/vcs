import requests
# 將查詢參數定義為字典資料加入GET請求中
payload = {'key1': 'value1', 'key2': 'value2'}
html = requests.get("http://httpbin.org/get", params=payload)
print(html.text)