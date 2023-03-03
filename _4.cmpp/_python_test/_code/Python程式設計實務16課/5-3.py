# _*_ coding: utf-8 _*_

import random

game_count = 0
all_counts = []
while True:
  game_count += 1 
  guess_count = 0
  answer = random.randint(0,99)
  while True:
    guess = int(input("請猜一個數字(0-99)："))
    guess_count += 1
    if guess == answer:
      print("恭禧你，猜中了")
      print("你總共猜了" + str(guess_count) + "次")
      all_counts.append(guess_count)
      break;
    elif guess > answer:
      print("你猜的數字太大了")
    else:
      print("你猜的數字太小了")
  onemore = input("還要再玩一次嗎(Y/N)？")
  if onemore != 'Y' and onemore != 'y':
    print("歡迎下次再來玩！")
    print("您的成績如下：")
    print(all_counts)
    print("平均猜中次數" + str(sum(all_counts)/float(len(all_counts))))
    break;
 


