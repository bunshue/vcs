import requests 

r = requests.get("http://www.google.com")
if r.status_code == 200:
    print("請求成功...")
else:
    print("請求失敗...")
     