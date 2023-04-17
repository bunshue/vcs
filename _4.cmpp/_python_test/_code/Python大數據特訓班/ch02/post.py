import requests

payload = {'key1': 'value1', 'key2': 'value2'}
# 將查詢參數加入 POST 請求中
html_data = requests.post("http://httpbin.org/post", data = payload)

print(html_data.url)
print(html_data.text)




