import random

# 生成一個隨機數
number = random.randint(1, 100)

# 提示用戶輸入數字
guess = int(input("Guess a number between 1 and 100: "))

# 比較用戶輸入的數字和隨機數的大小
while guess != number:
    if guess < number:
        guess = int(input("Too low. Guess again: "))
    else:
        guess = int(input("Too high. Guess again: "))

print("Congratulations! You guessed the number", number)
