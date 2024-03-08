## Bing
## 當然可以！以下是一個簡單的 Python 猜數字遊戲，讓你猜一個介於 0 到 100 之間的數字。請享受遊戲吧！🎮

import random

secret_number = random.randint(0, 100)  # 含頭尾
attempts = 1

print("歡迎來到猜數字遊戲！")
print("我已經選好一個數字，你來猜猜看吧！")

while True:
    ii = input("請輸入你的猜測（0 到 100）：")
    user_guess = int(ii)

    if user_guess < secret_number:
        print("太小了，再試試大一點的數字。")
    elif user_guess > secret_number:
        print("太大了，試試小一點的數字。")
    else:
        print("恭喜你猜對了！答案是 :", secret_number,"。你總共猜了", attempts, " 次。")
        break

    attempts += 1

