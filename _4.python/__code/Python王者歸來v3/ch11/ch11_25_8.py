# ch11_25_8.py
def recur(i):    
    if (i < 1):            # 結束條件
        return 0
    else:
        recur(i-1)         # 每次呼叫讓自己減 1
    print(i, end='\t')
    
recur(5)

