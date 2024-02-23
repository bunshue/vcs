i = 1 # i起始值為1
# 執行三次
while (i<=3) :
    print("第 %d 次帳密驗證：" %i, end="")
    uid = input(" 帳號：")  #將帳號指定給uid
    pw = input(" 密碼：")  #將密碼指定給pw
    if uid=="dtc" and pw=="168":	
        print("帳密正確，歡迎進入系統")  
        break
    i+=1
else :
    print()
    print("3 次帳密錯誤，無法使用系統")

