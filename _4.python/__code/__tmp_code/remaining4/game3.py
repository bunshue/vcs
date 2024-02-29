import random

# 定義猜拳選項
options = ["rock", "paper", "scissors"]

# 提示用戶輸入猜拳選項
user_choice = input("Choose rock, paper, or scissors: ")

# 電腦隨機生成猜拳選項
computer_choice = random.choice(options)

# 比較用戶和電腦的猜拳選項，判斷輸贏
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")
else:
    print("You lose!")
