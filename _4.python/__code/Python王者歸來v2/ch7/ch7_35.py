# ch7_35.py
i = 1                   # 設定i初始值
while i <= 9:           # 當i大於9跳出外層迴圈
    j = 1               # 設定j初始值
    while j <= 9:       # 當j大於9跳出內層迴圈
        result = i * j
        print(f"{i}*{j}={result:<3d}", end=" ")
        j += 1          # 內層迴圈加1
    print()             # 換行輸出
    i += 1              # 外層迴圈加1
    



