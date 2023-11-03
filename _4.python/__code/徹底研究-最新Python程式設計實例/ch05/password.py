"""
讓使用者輸入密碼，並且進行密碼驗證,
輸入次數以三次為限，超過三次則不准登入，
假如目前密碼為3388。
"""
password=3388 #利用變數來儲存密碼以供驗證
i=1

while i<=3: #輸入次數以三次為限
    new_pw=int(input("請輸入密碼:"))
    if new_pw != password:  #如果輸入的密碼與預設密碼不同
        print("密碼發生錯誤!!")
        i=i+1
        continue #跳回while開始處
    else:
        print("密碼正確!!")
        break
if i>3:
        print("密碼錯誤三次，取消登入!!\n"); #密碼錯誤處理
