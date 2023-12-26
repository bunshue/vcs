# ch27_11.py

secretcode = 'DAY'                                              # 設定密碼
codeNotFound = True                                             # 尚未找到密碼為True
for i1 in range(1, 27):                                         # 第一位數
    if codeNotFound:            # 檢查是否找到沒有找到才會往下執行
        for i2 in range(1, 27):                                 # 第二位數
            if codeNotFound:    # 檢查是否找到沒有找到才會往下執行
                for i3 in range(1, 27):                         # 第三位數
                    code = chr(i1+64) + chr(i2+64) + chr(i3+64) # 組成密碼
                    if code == secretcode:                      # 比對密碼
                        print('Bingo!', code)
                        codeNotFound = False                    # 註明已經比對成功
                        break
                    else:
                        print(code, end=' ')                    # 列印無效碼


