import requests #滙入requests套件

addr = 'https://www.edu.tw/'
res = requests.get(addr)

#檢查狀態碼
if res.status_code == 200:
    print('status_code= ',res.status_code)
    res.encoding='utf-8'
    print(res.text)
else:
    print('網頁無法開啟, status_code= ',res.status_code)
