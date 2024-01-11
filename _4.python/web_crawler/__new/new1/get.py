import requests #滙入requests套件

addr = 'https://www.books.com.tw/'
res = requests.get(addr)

#檢查狀態碼
if res.status_code == 200:
    res.encoding='utf-8'
    print(res.text)
else:
    print(res.status_code)
