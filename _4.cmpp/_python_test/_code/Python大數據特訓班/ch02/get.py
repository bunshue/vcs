import requests

payload = {'key1': 'value1', 'key2': 'value2'}
# 將查詢參數加入 GET 請求中
html_data = requests.get("http://httpbin.org/get", params = payload)

print(html_data.url)    # http://httpbin.org/get?key1=value1&key2=value2
print(html_data.text)   # http://httpbin.org/get?key1=value1&key2=value2


payload = {'title': '獅子'}
html_data = requests.get('https://zh.wikipedia.org/w/index.php', params = payload)

#相當於寫了 : https://zh.wikipedia.org/w/index.php?title=獅子

print(html_data.url)
print(html_data.text)



