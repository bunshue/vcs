# ch7_28.py
num = int(input("請輸入大於1的整數做質數測試 = "))
if num == 2:                                # 2是質數所以直接輸出
    print(f"{num}是質數")
else:
    for n in range(2, num):                 # 用2 .. num-1當除數測試
        if num % n == 0:                    # 如果整除則不是質數
            print(f"{num}不是質數")
            break                           # 離開迴圈
    else:                                   # 否則是質數
        print(f"{num}是質數")


