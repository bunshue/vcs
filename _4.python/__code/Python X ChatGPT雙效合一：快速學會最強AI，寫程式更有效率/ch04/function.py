print("功能選單") 
print(" 0.歡迎詞")
print(" 1.註冊會員資料" )
print(" 2.新增訂單")
print(" 3.查詢出貨明細")
print("請點選您要的項目:" )
Select=int(input()) 
if Select == 0: 
    print("歡迎光臨本系")
elif Select == 1: 
    print("呼叫註冊會員資料程式")
elif Select == 2: 
    print("呼叫新增訂單程式" )
elif Select == 3: 
    print("呼叫查詢出貨明細程式" )
else: #輸入錯誤的處理
    print("請重新選擇")
