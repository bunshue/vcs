import requests 
 
url_params = {'name': '陳會安', 'grade': 95}
r = requests.get("http://httpbin.org/get", params=url_params)
if r.status_code == 200:
    print(r.text)
else:
    print("錯誤! HTTP請求失敗...")

