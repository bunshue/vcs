# ch13_16.py
import random                       # 導入模組random

min, max = 1, 100                   # 隨機數最小與最大值設定
winPercent = int(input("請輸入莊家贏的比率(0-100)之間 :"))

while True:
    print("猜大小遊戲: L或l表示大,  S或s表示小, Q或q則程式結束")
    customerNum = input("= ")       # 讀取玩家輸入
    if customerNum == 'Q' or customerNum == 'q':    # 若輸入Q或q
        break                                       # 程式結束
    num = random.randint(min, max)  # 產生是否讓玩家答對的隨機數
    if num > winPercent:            # 隨機數在81-100間回應玩家猜對
        print("恭喜!答對了\n")
    else:                           # 隨機數在1-80間回應玩家猜錯
        print("答錯了!請再試一次\n")




