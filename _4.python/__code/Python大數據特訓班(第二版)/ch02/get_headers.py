import requests
url = 'https://irs.thsrc.com.tw/IMINT/'
# 自訂表頭
headers={
   'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}
# 將自訂表頭加入 GET 請求中
html = requests.get(url, headers=headers)
print(html)