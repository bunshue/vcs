# ch13_25.py
import random                       # 導入模組random
money = 300                         # 賭金總額
bet = 100                           # 賭注
min, max = 1, 100                   # 隨機數最小與最大值設定
winPercent = int(input("請輸入莊家贏的比率(0-100)之間 :"))

while True:
    print("歡迎光臨 : 目前籌碼金額 %d 美金 " % money)
    print("每次賭注 %d 美金 " % bet)
    print("猜大小遊戲: L或l表示大,  S或s表示小, Q或q則程式結束")
    customerNum = input("= ")       # 讀取玩家輸入
    if customerNum == 'Q' or customerNum == 'q':    # 若輸入Q或q
        break                                       # 程式結束
    num = random.randint(min, max)  # 產生是否讓玩家答對的隨機數
    if num > winPercent:            # 隨機數在此區間回應玩家猜對
        print("恭喜!答對了\n")
        money += bet                # 賭金總額增加
    else:                           # 隨機數在此區間回應玩家猜錯
        print("答錯了!請再試一次\n")
        money -= bet                # 賭金總額減少
    if money <= 0:
        break

print("歡迎下次再來")




