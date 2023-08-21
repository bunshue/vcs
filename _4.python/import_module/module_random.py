# python import module : random

import random

print('--- random.randint ---------------------------------------------------------')	#60個


R = random.randint(0, 255) #產生 0~255 之間的亂數整數 包含邊界
G = random.randint(0, 255) #產生 0~255 之間的亂數整數 包含邊界
B = random.randint(0, 255) #產生 0~255 之間的亂數整數 包含邊界
print("取得亂數: ", R, G, B)
print("取得亂數1: {} 亂數2: {} 亂數3: {}".format(R, G, B))
print("取得亂數: (%d, %d, %d)" % (R, G, B))

maxNo=10
result = random.randrange(1, 10)
print("取得亂數 : " + str(result))

while True:
    x = random.randint(1,6)
    print(x)
    if x == 6:
        break

num = random.randint(1,6)
print("你擲的骰子點數為：" + str(num))

print("1到6選一個")
for count in range(10):
    print(random.randint(1, 6))



print('--- random.choice ---------------------------------------------------------')	#60個

for i in range(10):
    timeout = random.choice(range(80,180))
    print('timeout', timeout)

print('------------------------------------------------------------')	#60個




pretty_note = '♫♪♬'
pretty_text = ''

string_message = 'abcdefg'
for i in string_message:
    pretty_text += i
    pretty_text += random.choice(pretty_note)
    
print(pretty_text)



def randomAnimal():
    nouns = ["lion", "mouse", "cat", "dog"]
    noun = random.choice(nouns)     #在名詞字串中隨機選取一個字串
    return noun

for count in range(10):
    print(randomAnimal())


print("任選一個")
for count in range(10):
    print(random.choice(['a', 'b', 'c']))


#values = [1,2,3,4,5,6]
values = ['alpha','bravo','charlie','delta','echo','foxtrot']

print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))



first_names = ['Bob', 'Maria', 'Alex', 'James', 'Susan', 'Henry', 'Lisa', 'Anna', 'Lisa']
last_names = ['Smith', 'Brown', 'Wilson', 'Thomson', 'Cook', 'Taylor', 'Walker', 'Clark']

for i in range(10):
    first = random.choice(first_names)
    last = random.choice(last_names)
    print(first, last)




print('------------------------------------------------------------')	#60個

def randomNoun():
    nouns = ["cats", "hippos", "cakes"]
    noun = random.choice(nouns)
    return noun

def randomVerb():
    verbs = ["eats", "likes", "hates", "has"]
    verb = random.choice(verbs)
    return verb

for i in range(4):
  verb = randomVerb()
  noun = randomNoun()
  sentence = "david " + verb + " " + noun
  print(sentence)


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('--- random.sample ---------------------------------------------------------')	#60個

list1 = random.sample(range(1,50), 7)
special = list1.pop()
list1.sort()
print("本期大樂透中獎號碼為：", end="")
for i in range(0,6):
    if i == 5:    print(str(list1[i]))
    else:    print(str(list1[i]), end=", ")
print("本期大樂透特別號為：" + str(special))

print('------------------------------------------------------------')	#60個


print('--- random.shuffle ---------------------------------------------------------')	#60個


print("亂數分配工作")
member = ["花媽", "花橘子", "花柚子", "花爸"]
housework = ["掃地", "拖地", "洗衣服", "擦窗戶"]
random.shuffle(housework)
for i in range(4):
    print("%s今天負責%s" % (member[i], housework[i]))

print('------------------------------------------------------------')	#60個

for count in range(20):
    x = random.randrange(-10, 10)       #-10~9之間的整數
    y = random.randrange(-10, 10)       #-10~9之間的整數
    length = random.randrange(10)       #0~9之間的整數
    shape = random.randrange(3, 8)      #3~7之間的整數
    print(count, x, y, length, shape)

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

#發牌遊戲

# Create a deck of cards
deck = [x for x in range(0, 52)]

# Create suits and ranks lists
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9",
      "10", "Jack", "Queen", "King"]
        
# Shuffle the cards
random.shuffle(deck)

# Display the first four cards
for i in range(4):
    suit = suits[deck[i] // 13]
    rank = ranks[deck[i] % 13]
    print("Card number", deck[i], "is", rank, "of", suit)

print('------------------------------------------------------------')	#60個

import pandas as pd
import numpy as np

my_array = np.arange(10)  # [0 1 2 3 4]

print('原list')
print(my_array)

print('shuffle list')
np.random.shuffle(my_array)
print(my_array)

print('shuffle list')
np.random.shuffle(my_array)
print(my_array)

print('shuffle list')
np.random.shuffle(my_array)
print(my_array)

sum_my_array = sum(my_array)
print('和')
print(sum_my_array)

'''
index = []
ran = random.sample(range(0, 10),2)
for i in ran:
    index.append(i)
index.sort()
'''

print('------------------------------------------------------------')	#60個

import time

n = 10
lst = list(range(n))
print(lst)
random.shuffle(lst)
print(lst)
startTime = time.time()
lst.sort()
print("Sort time in Python is", int(time.time() - startTime), "seconds")

print(lst)

print('------------------------------------------------------------')	#60個


s = ''
for i in range(0, 10):
    s += random.choice('<>=^')
    s += random.choice('+- ')
    s += str(random.randrange(1, 100))
    s += str(random.randrange(100))
    s += random.choice(('', 'E', 'e', 'G', 'g', 'F', 'f', '%'))

print(s)


print('------------------------------------------------------------')	#60個


randseed = int(time.time())
random.seed(randseed)


print('------------------------------------------------------------')	#60個

tttt = hex(random.getrandbits(64))  # 64 bits randomness
print(tttt)


print('------------------------------------------------------------')	#60個

    
print('------------------------------------------------------------')	#60個

data = [random.uniform(-2, 9) for _ in range(10)]

print(len(data))
print(type(data))
print(data)

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print("猜數字遊戲")
'''
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
'''



print('------------------------------------------------------------')	#60個

