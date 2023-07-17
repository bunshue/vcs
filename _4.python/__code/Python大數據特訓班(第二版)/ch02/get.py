import requests
url = 'http://www.ehappy.tw/demo.htm'
html = requests.get(url)
# 檢查HTTP回應碼是否為200(requests.code.ok)
if html.status_code == requests.codes.ok:
    print(html.text)