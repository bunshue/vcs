import requests  # 匯入 requests 套件
r = requests.get('http://www.flag.com.tw') # 向旗標網站發出 GET 請求,並將回應物件儲存到 r

if r.status_code == 200:   # 回應的狀態碼若為 200 表示 OK
    print(r.text)          # 將回應的文字(網頁原始碼)印出來
else:
    print(r.status_code, r.reason) # 若發生錯誤(狀態碼不是 200), 則印出狀態碼及錯誤原因