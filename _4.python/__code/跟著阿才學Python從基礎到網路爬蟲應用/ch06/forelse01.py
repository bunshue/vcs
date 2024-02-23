# 執行三次
for i in range(3):
    print("第 %d 次帳密驗證：" %(i+1), end="")
    uid = input(" 帳號：")  #將帳號指定給uid
    pw = input(" 密碼：")  #將密碼指定給pw
    if uid=="dtc" and pw=="168":	
        print("帳密正確，歡迎進入系統")  
        break
else :
    print()
    print("3 次帳密錯誤，無法使用系統")

