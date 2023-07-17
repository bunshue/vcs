import requests
# 設定查詢目前IP的api網址
url = 'https://api.ipify.org'
r = requests.get(url)

print('我目前的IP是：', r.text)