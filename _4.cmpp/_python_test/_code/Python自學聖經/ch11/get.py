import requests

url = 'http://www.ehappy.tw/demo.htm'
r = requests.get(url)
# 檢查HTTP回應碼是否為200(requests.code.ok)
if r.status_code == requests.codes.ok:
    print("擷取網頁資料 OK")
    print(r.text)
else:
    print("擷取網頁資料 NG")
