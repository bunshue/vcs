# ch6_58.py
accounts = []                       # 建立空帳號串列
account = input("請輸入新帳號 = ")
accounts.append(account)            # 將輸入加入帳號串列

print("深智公司系統")
ac = input("請輸入帳號 = ")
if ac in accounts:
    print("歡迎進入深智系統")
else:
    print("帳號錯誤")


