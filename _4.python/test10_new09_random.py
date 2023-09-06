'''

random 專區

'''
import os
import sys
import time
import math
import random

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

'''
for ball in ballList:
    print(ball.color)
'''

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



for _ in range(1000):
    x = random.random() * math.exp(random.random()*200.0 - 100.0)


for _ in range(1000):
    e = random.randrange(300)
    n = random.randrange(-10**e, 10**e)



'''
def _random_getnode():
    """Get a random node ID, with eighth bit set as suggested by RFC 4122."""
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

'''



print('------------------------------------------------------------')	#60個


'''
一大堆random範例

'''

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

import time                         # 導入模組time

print(time.asctime())               # 列出目前系統時間 

print('------------------------------------------------------------')	#60個

import time                         # 導入模組time

xtime = time.localtime()
print(xtime)                        # 列出目前系統時間
print("年 ", xtime[0])
print("年 ", xtime.tm_year)         # 物件設定方式顯示
print("月 ", xtime[1])
print("日 ", xtime[2])
print("時 ", xtime[3])
print("分 ", xtime[4])
print("秒 ", xtime[5])
print("星期幾   ", xtime[6])
print("第幾天   ", xtime[7])
print("夏令時間 ", xtime[8])

print('------------------------------------------------------------')	#60個

import time                         # 導入模組time

print(time.ctime())

print('------------------------------------------------------------')	#60個

''' fail
import time

x = 1000000
pi = 0
time.clock()
for i in range(1,x+1):
    pi += 4*((-1)**(i+1) / (2*i-1))
    if i != 1 and i % 100000 == 0:      # 隔100000執行一次
        e_time = time.clock()
        print("當 i={:7d} 時 PI={:8.7f}, 所花時間={}".format(i, pi, e_time))
'''

print('------------------------------------------------------------')	#60個

import time
x = 1000000
pi = 0
time.process_time()
for i in range(1,x+1):
    pi += 4*((-1)**(i+1) / (2*i-1))
    if i != 1 and i % 100000 == 0:      # 隔100000執行一次
        e_time = time.process_time()
        print("當 i={:7d} 時 PI={:8.7f}, 所花時間={}".format(i, pi, e_time))

print('------------------------------------------------------------')	#60個

import calendar

print("2020年是否潤年", calendar.isleap(2020))    
print("2021年是否潤年", calendar.isleap(2021))

print('------------------------------------------------------------')	#60個

import calendar

print(calendar.month(2020,1))

print('------------------------------------------------------------')	#60個

import calendar

print(calendar.calendar(2023))

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

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




