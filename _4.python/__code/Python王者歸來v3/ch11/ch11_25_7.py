# ch11_25_7.py
import time
def recur(i):
    print(i, end='\t')
    time.sleep(1)           # 休息 1 秒
    if (i <= 1):            # 結束條件
        return 0
    else:
        return recur(i-1)   # 每次呼叫讓自己減 1

recur(5)

