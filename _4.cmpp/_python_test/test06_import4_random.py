# python import module : random


import random
x = random.randint(1,6)
print(x)
while x != 6:
  x = random.randint(1,6)
  print(x)


member = ["花媽", "花橘子", "花柚子", "花爸"]
housework = ["掃地", "拖地", "洗衣服", "擦窗戶"]
random.shuffle(housework)
for i in range(4):
    print("%s今天負責%s" % (member[i], housework[i]))
    
for count in range(20):
    x = random.randrange(-10, 10)       #-10~9之間的整數
    y = random.randrange(-10, 10)       #-10~9之間的整數
    length = random.randrange(10)       #0~9之間的整數
    shape = random.randrange(3, 8)      #3~7之間的整數
    print(count, x, y, length, shape)



def randomAnimal():
    nouns = ["lion", "mouse", "cat", "dog"]
    noun = random.choice(nouns)     #在名詞字串中隨機選取一個字串
    return noun

for count in range(10):
    print(randomAnimal())

from random import randint
print("1到6選一個")
for count in range(10):
    print(randint(1, 6))


import random as R
print("1到6選一個")
for count in range(10):
    print(R.randint(1, 6))

print("任選一個")
for count in range(10):
    print(random.choice(['a', 'b', 'c']))


import random
#values = [1,2,3,4,5,6]
values = ['alpha','bravo','charlie','delta','echo','foxtrot']

print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))

print("猜數字遊戲")


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
 





