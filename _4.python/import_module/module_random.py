import sys
import random

'''
random.seed()

random.random()

random.randint(num1, num2)

random.choice

random.randrange

random.uniform(num1, num2)

----

還沒整理好的
random.sample.....

'''

print('隨機變數')

print('---- random.seed() --------------------------------------------------------')	#60個

"""
random.seed(5)  #固定亂數種子
for i in range(10):
    print(random.random(), end = ', ')

import time
randseed = int(time.time())
random.seed(randseed) #打亂亂數種子
for i in range(10):
    print(random.random(), end = ', ')
""" 

print('---- random.random() --------------------------------------------------------')	#60個

print('random.random(), 隨機分布, 產生 0.00 ~ 1.00 之間的一個浮點數')
for i in range(5):
    print(random.random())

print('------------------------------------------------------------')	#60個

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
R = random.randint(num1, num2) #產生 num1 ~ num2 之間的亂數整數 包含邊界
G = random.randint(num1, num2) #產生 num1 ~ num2 之間的亂數整數 包含邊界
B = random.randint(num1, num2) #產生 num1 ~ num2 之間的亂數整數 包含邊界
print("取得亂數: ", R, G, B)
print("取得亂數1: {} 亂數2: {} 亂數3: {}".format(R, G, B))
print("取得亂數: (%d, %d, %d)" % (R, G, B))

print('取出 1 ~ 6 之間的整數')

num = random.randint(1, 6)
print("你擲的骰子點數為：" + str(num))

print('---- random.choice --------------------------------------------------------')	#60個

import random                   # 導入模組random

ANIMALS = '鼠牛虎兔龍蛇馬'
animalList = list(ANIMALS) #字串 轉 串列
print(type(animalList))
print(animalList)

for i in range(10):
    print(random.choice(animalList), end = ', ')
print()

print('------------------------------------------------------------')	#60個

#animals = [1,2,3,4,5,6]
animals = ['鼠', '牛', '虎', '兔', '龍']
for i in range(10):
    animal = random.choice(animals)     #在名詞字串中隨機選取一個字串
    print(animal, end = ', ')
print()

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

NUMBER = 11
numberList = list(range(NUMBER))
print(type(numberList))
print(numberList)

for i in range(10):
    print(random.choice(numberList), end = ', ')
print()

print('------------------------------------------------------------')	#60個

for i in range(10):
    print(random.choice([1,2,3,4,5,6]), end = ', ')
print()

print('------------------------------------------------------------')	#60個

for i in range(10):
    t = random.choice(range(80, 180))
    print(t, end = ', ')
print()

print('------------------------------------------------------------')	#60個

pretty_note = '♫♪♬'
pretty_text = ''

string_message = 'abcdefg'
for i in string_message:
    pretty_text += i
    pretty_text += random.choice(pretty_note)
    
print(pretty_text)

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



print('---- random.randrange --------------------------------------------------------')	#60個

maxNo = 10
result = random.randrange(1, 10)
print("取得亂數 : " + str(result))

print('------------------------------------------------------------')	#60個

for count in range(20):
    x = random.randrange(-10, 10)       #-10~9之間的整數
    y = random.randrange(-10, 10)       #-10~9之間的整數
    length = random.randrange(10)       #0~9之間的整數
    shape = random.randrange(3, 8)      #3~7之間的整數
    print(count, x, y, length, shape)

print('------------------------------------------------------------')	#60個


print('randrange(300), 取出0~300間之整數')

for _ in range(10):
    x = random.randrange(300)
    print(x)


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


print('------------------------------------------------------------')	#60個


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


print('常態分布 1 ~ 10')
for i in range(5):
    print("uniform(1,10) : ", random.uniform(1, 10))

print('------------------------------------------------------------')	#60個


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

lotterys = random.sample(range(1,50), 7)    # 7組號碼
specialNum = lotterys.pop()                 # 特別號

print("第xxx期大樂透號碼 ", end="")
for lottery in sorted(lotterys):            # 排序列印大樂透號碼
    print(lottery, end=" ")
print("\n特別號:%d" % specialNum)           # 列印特別號




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

animals = ['鼠', '牛', '虎', '兔', '龍']
for i in range(3):
    random.shuffle(animals)              # 將次序打亂重新排列
    print(animals)

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




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


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


print('------------------------------------------------------------')	#60個


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



print('random 之 dir')
import random
print(dir(random))


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('---- 用 numpy 做的 random --------------------------------------------------------')	#60個

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



import numpy as np

print("回傳值是10(含)至20(不含)的單一隨機數")
x1 = np.random.randint(10, 20)
print(x1)

print("回傳一維陣列10個元素, 值是1(含)至5(不含)的隨機數")
x2 = np.random.randint(1, 5, 10)
print(x2)

print("回傳單3*5陣列, 值是0(含)至10(不含)的隨機數")
x3 = np.random.randint(10, size=(3, 5))     
print(x3)



A = np.random.rand(50)

mydata = np.random.randn(4,3)
df3 = pd.DataFrame(np.random.randn(3,3), columns=list("ABC"))


"""

插播一下, 平常我們要從一個平均值是 0, 標準差是 1 的常態分布中, 隨機取幾個數出來似乎有點困難。但我們打開封印後, 這件事很簡單!

我們可以取整數亂數

np.random.randint(a,b)
樣取出的數字 k 會介於:
a <= k < b

k = np.random.randint(1,101)
1~100





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


print('---- 新進 --------------------------------------------------------')	#60個


import random                       # 導入模組random

num = []
for i in range(600):
    num.append(random.choice([1,2,3,4,5,6]))
    
numCount = {i:num.count(i) for i in num}
for num in sorted(numCount.keys()):
    print(num, ':', numCount[num])


print('------------------------------------------------------------')	#60個



for i in range(10):
    #time.sleep(random.randint(0,2))
    print(random.randint(0,2))



print('------------------------------------------------------------')	#60個

import random
for i in range(10):
    print(random.uniform(1,100), " ", end="")

print()

print('------------------------------------------------------------')	#60個

import random 
lst = [random.randint(1,100) for i in range(100)]
print(lst)
print("Average of the list is", sum(lst)/float(len(lst)))

print('------------------------------------------------------------')	#60個

import random
fruit = ['Apple', 'Cherry', 'Banana', 'Strawberry']
print("Before:", fruit)
random.shuffle(fruit)
print("After:", fruit)
print("Today's lucky fruit is:", random.choice(fruit))

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個
import random

def random_num():
    values = [1, 2, 3, 4, 5, 6]
    print(random.choice(values))
    print(random.choice(values))
    print(random.choice(values))
    print(random.choice(values))
    print(random.choice(values))

    # 抽取样本
    print(random.sample(values, 2))
    print(random.sample(values, 2))
    print(random.sample(values, 3))

    # 打算顺序
    random.shuffle(values)
    print(values)

    # 随机整数
    print(random.randint(0,10))
    print(random.randint(0,10))
    print(random.randint(0,10))
    print(random.randint(0,10))

    # 随机二进制数的整数返回
    print(random.getrandbits(200))

    # 修改随机数生成的种子
    random.seed() # Seed based on system time or os.urandom()
    random.seed(12345) # Seed based on integer given
    random.seed(b'bytedata') # Seed based on byte data

if __name__ == '__main__':
    random_num()



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



