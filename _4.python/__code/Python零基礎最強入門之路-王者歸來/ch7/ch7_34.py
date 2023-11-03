# ch7_34.py
index = 0
while index <= 10:
    index += 1
    if ( index % 2 != 0 ):  # 測試是否奇數
        continue            # 不往下執行
    print(index)            # 輸出偶數
        
