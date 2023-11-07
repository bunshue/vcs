import requests

url = 'http://httpbin.org/post' # 使用測試服務網站, POST 方法網址要加 /post
r = requests.post(url, data = 'Hello')  # 送出字串資料
print(r.text)
r = requests.post(url, data = {'id':'123', 'name':'Joe'})
print(r.text)