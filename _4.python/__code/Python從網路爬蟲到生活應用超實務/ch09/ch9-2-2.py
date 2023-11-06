import requests 
 
token = "<存取權杖>"
headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/x-www-form-urlencoded"
}
params = {"message": "Python程式送出測試通知訊息"}
r = requests.post("https://notify-api.line.me/api/notify",
                   headers=headers, params=params)  
if r.status_code == 200:
    print("已經送出通知訊息...")
else:
    print("錯誤! 寄送通知訊息失敗...")

