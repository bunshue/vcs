# ch11_25_6.py
import time
def recur(i):
    print(i, end='\t')
    time.sleep(1)       # 休息 1 秒
    return recur(i-1)

recur(5)


