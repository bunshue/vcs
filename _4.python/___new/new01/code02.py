# Bing
# 當然可以！以下是一個簡單的 Python 猜數字遊戲，讓你猜一個介於 0 到 100 之間的數字。請享受遊戲吧！🎮

import random

secret_number = random.randint(0, 100)  # 含頭尾之整數
attempts = 1

print("歡迎來到猜數字遊戲！")
print("我已經選好一個數字，你來猜猜看吧！")

while True:
    # print(attempts)
    ii = input("請輸入你的猜測（0 到 100）：")
    if ii == "q":
        print("你要離開了")
        break

    user_guess = int(ii)

    if user_guess < secret_number:
        print("太小了，再試試大一點的數字。")
    elif user_guess > secret_number:
        print("太大了，試試小一點的數字。")
    else:
        print("恭喜你猜對了！答案是 :", secret_number, "。你總共猜了", attempts, " 次。")
        break

    attempts += 1
    if attempts > 10:
        print("你太笨了，離開")
        break

print("------------------------------------------------------------")  # 60個

# 修改猜數字遊戲程式，只允許使用者最多猜10次
# 修改猜數字遊戲程式，允許使用者按q離開遊戲

print("------------------------------------------------------------")  # 60個

import random

# 使用 random.randint(m, n) 生成兩整數，對此兩整數做多則運算並輸出 0 <= a <= 100  1 <= b <= 10 (加減乘除整數除求餘冪次方)
a = random.randint(0, 100)
b = random.randint(1, 10)
print(a)
print(b)
c = a + b
print(c)
c = a - b
print(c)
c = a * b
print(c)
c = a / b
print(c)
c = a % b
print(c)
c = a // b
print(c)
c = a**b
print(c)

print("------------------------------------------------------------")  # 60個

# 使用sleep() 每1秒印出一個字 印10次

import time

for i in range(10):
    print(i)
    print("A")
    time.sleep(1)

print("------------------")

i = 0
while i < 10:
    print(i)
    print("A")
    time.sleep(1)
    i += 1

print("------------------------------------------------------------")  # 60個
