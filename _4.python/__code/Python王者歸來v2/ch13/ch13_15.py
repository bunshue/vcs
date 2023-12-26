# ch13_15.py
import random                       # 導入模組random

min, max = 1, 10
ans = random.randint(min, max)      # 隨機數產生答案
while True:
    yourNum = int(input("請猜1-10之間數字: "))
    if yourNum == ans:
        print("恭喜!答對了")
        break
    elif yourNum < ans:
        print("請猜大一些")
    else:
        print("請猜小一些")
        


