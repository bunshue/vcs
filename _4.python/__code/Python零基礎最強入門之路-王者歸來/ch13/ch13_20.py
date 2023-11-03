# ch13_20.py
import random                       # 導入模組random
import time                         # 導入模組time

min, max = 1, 10
ans = random.randint(min, max)      # 隨機數產生答案
yourNum = int(input("請猜1-10之間數字: "))
starttime = int(time.time())    # 起始秒數
while True:    
    if yourNum == ans:
        print("恭喜!答對了")
        endtime = int(time.time())  # 結束秒數
        print("所花時間: ", endtime - starttime, " 秒")
        break
    elif yourNum < ans:
        print("請猜大一些")
    else:
        print("請猜小一些")
    yourNum = int(input("請猜1-10之間數字: "))
        


