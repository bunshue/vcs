import random

# 產生介於1和100之間的亂數
target = random.randint(1, 100)

# 進入猜數字的迴圈
while True:
    # 要求使用者輸入猜測的數字
    guess = int(input("請輸入猜測的數字(1~100) : "))
    
    # 判斷使用者是否猜中數字
    if guess == target:
        print("猜中數字!")
        break
    # 判斷使用者猜的數字是否太大
    elif guess > target:
        print("數字太大")
    # 否則，顯示使用者猜的數字太小
    else:
        print("數字太小")
