target, guess = 38, 1
while True:
    guess = int(input("請輸入猜測數字(1~100): "))
    if target == guess:
        print("猜中數字 = ", target)
        break      # 跳出迴圈
    elif guess > target:
        print("數字太大!")
    else:
        print("數字太小!")



