# F1750 練習 01

import random

def guessing_game():
    answer = random.randint(0, 100)
 
    while True:
        user_guess = int(input('請猜數字 (0~99): '))
 
        if user_guess == answer:
            print('答對了! 答案是', answer)
            break
        elif user_guess > answer:
            print('猜得太高, 再試一次')
        else:
            print('猜得太低, 再試一次')

guessing_game()
