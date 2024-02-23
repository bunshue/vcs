print("==動物英文單字查詢==")
print("1. 獅子")
print("2. 老虎")
print("3. 大象")
print("4. 免子")
num = int(input("請輸入選項編號：")) # 輸入數字轉成整數並指定給num

if num >=1 and num <= 4:           # 判斷num是否介於1~4之間
    if num==1  :	
        show = "獅子：lion"         # num等於1，show指定 "獅子：lion"
    elif num==2  :
        show = "老虎：tiger"        # num等於2，show指定 "老虎：tiger""
    elif num==3  :	
        show = "大象：elephant"     # num等於3，show指定 "大象：elephant"
    elif num==4  :	
        show = "免子：rabbit"       # num等於4，show指定 "免子：rabbit"
else:
    show = "選項應介於1~4之間"   

print(show)  # 顯示show的結果
