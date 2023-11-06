import requests 
 
url = "https://fchart.github.io/test.html"
response = requests.get(url)
if response.status_code == 200:
    print("Text :\n", response.text)
    print("編碼: ", response.encoding)
    print("status_code : ", response.status_code)
else:
    print("錯誤! HTTP請求失敗...")


