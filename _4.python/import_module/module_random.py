import sys
import random

print('隨機變數')

print('------------------------------------------------------------')	#60個
'''
import random

#random.seed(5)  #固定亂數種子
for i in range(10):
    print(random.random(), end = ',')



print('---- random.random() --------------------------------------------------------')	#60個


#print('random.random() 測試, 0.00 ~ 1.00 之間的浮點數')
#for i in range(10):
#    print(random.random(), end = '\n')
#print()

print('蒙地卡羅模擬')

import random

trials = 1000000
Hits = 0
for i in range(trials):
    x = random.random() * 2 - 1     # x軸座標
    y = random.random() * 2 - 1     # y軸座標
    if x * x + y * y <= 1:          # 判斷是否在圓內
        Hits += 1
PI = 4 * Hits / trials

print("PI = ", PI)




print('---- random.randint(num1, num2) --------------------------------------------------------')	#60個

num1, num2 = 0, 255
R = random.randint(num1, num2) #產生 0~255 之間的亂數整數 包含邊界
G = random.randint(num1, num2) #產生 0~255 之間的亂數整數 包含邊界
B = random.randint(num1, num2) #產生 0~255 之間的亂數整數 包含邊界
print("取得亂數: ", R, G, B)
print("取得亂數1: {} 亂數2: {} 亂數3: {}".format(R, G, B))
print("取得亂數: (%d, %d, %d)" % (R, G, B))

num = random.randint(1, 6)
print(num)

num = random.randint(1, 6)
print("你擲的骰子點數為：" + str(num))


print('---- random.choice --------------------------------------------------------')	#60個

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


maxNo=10
result = random.randrange(1, 10)
print("取得亂數 : " + str(result))

print('------------------------------------------------------------')	#60個


print('---- random.uniform(num1, num2) --------------------------------------------------------')	#60個

import random                       # 導入模組random

print('random.uniform(num1, num2) 測試, num1 ~ num2 之間的浮點數')

num1, num2 = 2.34, 4.56
for i in range(30):
    print(random.uniform(num1, num2), end = '\n')
print()

print('建立一個隨機串列')
N = 5
data = [random.uniform(num1, num2) for _ in range(N)]
print(type(data))
print(len(data))
print(data)


print('------------------------------------------------------------')	#60個

import random                   # 導入模組random

ANIMALS = '鼠牛虎兔龍蛇馬'
animalList = list(ANIMALS) #字串 轉 串列
print(type(animalList))
print(animalList)

for i in range(10):
    print(random.choice(animalList), end = ',')
print()


print('------------------------------------------------------------')	#60個

import random                               # 導入模組random

N = 7   #7組號碼
for i in range(10):
    numbers = random.sample(range(1, 50), N)   #結果為 1, 2, 3....49 不包含50之整數
    #print(type(numbers))
    print(numbers)

specialNum = numbers.pop()                 # 特別號, 最後一個數字是特別號, pop出後, numbers剩下6個號碼

print("第xxx期大樂透號碼 :", end = '')
for num in sorted(numbers):            # 排序列印大樂透號碼
    print(num, end = ' ')
print(f"\n特別號:{specialNum}")             # 列印特別號

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


print('--- random.shuffle(list) ---------------------------------------------------------')	#60個

ANIMALS = '鼠牛虎兔龍蛇馬'
animalList = list(ANIMALS) #字串 轉 串列
print(type(animalList))
print(animalList)

for i in range(5):
    random.shuffle(animalList)    # 將次序打亂重新排列
    print(animalList)


print('------------------------------------------------------------')	#60個

ANIMALS = '鼠牛虎兔龍蛇馬'
animalList = list(ANIMALS) #字串 轉 串列
print('原串列')
print(animalList)
print('次序打散')
random.shuffle(animalList)
print(animalList)
print('排序')
animalList.sort()
print(animalList)

print('------------------------------------------------------------')	#60個



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

"""index = []
ran = random.sample(range(0, 10),2)
for i in ran:
    index.append(i)
index.sort()
"""

print('------------------------------------------------------------')	#60個


sys.exit()

s = ''
for i in range(0, 10):
    s += random.choice('<>=^')
    s += random.choice('+- ')
    s += str(random.randrange(1, 100))
    s += str(random.randrange(100))
    s += random.choice(('', 'E', 'e', 'G', 'g', 'F', 'f', '%'))

print(s)


print('------------------------------------------------------------')	#60個

import time
randseed = int(time.time())
random.seed(randseed)


print('------------------------------------------------------------')	#60個

tttt = hex(random.getrandbits(64))  # 64 bits randomness
print(tttt)


print('------------------------------------------------------------')	#60個

    
print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


import random

_FMT = '[Non-text (%(type)s) part of message omitted, filename %(filename)s]'
print(_FMT)

_width = len(repr(sys.maxsize-1))
_fmt = '%%0%dd' % _width

print(_width)
print(_fmt)

token = random.randrange(sys.maxsize)
print(token)
boundary = ('=' * 15) + (_fmt % token) + '=='
print(boundary)

'''
print('------------------------------------------------------------')	#60個





"""
import random

print('在0 <= output < 1之間產生一個浮點數')
random.random()

print('在low<= output <=hight之間產生一個整數')
random.randint(low, hight)


#由一個平均為0，變異數為1的高斯分布中隨機取點，並以list儲存。
np.random.randn(size)
#由low到high中產生一個size大小的list。 dtype，一般來說我們不會動到
np.random.randint(low, high, size, dtype='l')

print(np.random.randn(6))
#output:[ 1.3265288  -0.15050998 -0.59429709  0.6356734  -0.89041176  0.2790698]
print(np.random.randn(2,3))
#output:[[-0.51469048 -0.82356942  0.80310762]
#        [ 0.21914897 -0.04437828 -0.41106366]]
print(np.random.randint(1,10,6))
#output: [[4 6 7],[4 2 9]]


"""



print('------------------------------------------------------------')	#60個


from random import randint

# Return a random color string in the form #RRGGBB
def getRandomColor():
    color = "#"
    for j in range(6):
        color += toHexChar(randint(0, 15)) # Add a random digit
    return color

# Convert an integer to a single hex digit in a character 
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:  # 10 <= hexValue <= 15
        return chr(hexValue - 10 + ord('A'))

class Ball:
    def __init__(self):
        self.x = 0 # Starting center position
        self.y = 0 
        self.dx = 2 # Move right by default
        self.dy = 2 # Move down by default
        self.radius = 3 # The radius is fixed
        self.color = getRandomColor() # Get random color

ballList = [] # Create a list for balls

length = len(ballList)
print('length = ', length)

for i in range(6):
    ballList.append(Ball())

length = len(ballList)
print('length = ', length)

for i in range(length):
    print('第', i, '個 : ', ballList[i].color)

for ball in ballList:
    print(ball.color)

b = ballList.pop()
print(b.color)

b = ballList.pop()
print(b.color)

b = ballList.pop()
print(b.color)

print('------------------------------------------------------------')	#60個




from random import randint, random, getrandbits

def getrandbytes(size):
    return getrandbits(8 * size).to_bytes(size, 'little')


ccc = b'111' + getrandbytes(100)

print(type(ccc))
print(ccc)

datacount = randint(16, 64) * 1024 + randint(1, 1024)

ddd = random() * randint(-1000, 1000)
print(ddd)





print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




import random
print(dir(random))


import random
t = random.randint(1, 100)
print(t)

import random as R
t = R.randint(1, 100)
print(t)


import random
r1 = random.randint(1, 6)
r2 = random.randint(1, 6)
print(r1 + r2)
lst1 = list(range(11))
print(lst1)
r3 = random.choice(lst1)
print(r3)


import math
for _ in range(1000):
    x = random.random() * math.exp(random.random()*200.0 - 100.0)


for _ in range(1000):
    e = random.randrange(300)
    n = random.randrange(-10**e, 10**e)



"""
def _random_getnode():
    #Get a random node ID, with eighth bit set as suggested by RFC 4122.
    import random
    return random.randrange(0, 1<<48) | 0x010000000000


        return UUID(bytes=os.urandom(16), version=4)
    except:
        import random
        bytes = bytes_(random.randrange(256) for i in range(16))
        return UUID(bytes=bytes, version=4)


        import os
        if int(os.uname().release.split('.')[0]) >= 9:

        import random
        clock_seq = random.randrange(1<<14) # instead of stable storage

"""

print('------------------------------------------------------------')	#60個

import random   # 導入模組random

print('------------------------------------------------------------')	#60個

print('隨機分布 0 ~ 1')
for i in range(5):
    print(random.random())
    
print('------------------------------------------------------------')	#60個

random.seed(5)  #固定亂數種子
for i in range(5):
    print(random.random())
    
print('------------------------------------------------------------')	#60個

print('常態分布 1 ~ 10')
for i in range(5):
    print("uniform(1,10) : ", random.uniform(1, 10))

print('------------------------------------------------------------')	#60個

fruits = ['蘋果', '香蕉', '西瓜', '水蜜桃', '百香果']
for i in range(5):
    print(random.choice(fruits))

print('------------------------------------------------------------')	#60個

for i in range(10):
    print(random.choice([1,2,3,4,5,6]), end=",")

print('------------------------------------------------------------')	#60個

porker = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
for i in range(3):
    random.shuffle(porker)              # 將次序打亂重新排列
    print(porker)

print('------------------------------------------------------------')	#60個

lotterys = random.sample(range(1,50), 7)    # 7組號碼
specialNum = lotterys.pop()                 # 特別號

print("第xxx期大樂透號碼 ", end="")
for lottery in sorted(lotterys):            # 排序列印大樂透號碼
    print(lottery, end=" ")
print("\n特別號:%d" % specialNum)           # 列印特別號


print('------------------------------------------------------------')	#60個


trials = 1000000
Hits = 0
for i in range(trials):
    x = random.random() * 2 - 1     # x軸座標
    y = random.random() * 2 - 1     # y軸座標
    if x * x + y * y <= 1:          # 判斷是否在圓內
        Hits += 1
PI = 4 * Hits / trials

print("PI = ", PI)



