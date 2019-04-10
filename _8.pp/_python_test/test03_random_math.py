import random
import time

start = time.time()

for count in range(20):
    x = random.randrange(-10, 10)       #-10~9之間的整數
    y = random.randrange(-10, 10)       #-10~9之間的整數
    length = random.randrange(10)       #0~9之間的整數
    shape = random.randrange(3, 8)      #3~7之間的整數
    print(count, x, y, length, shape)


import math
for count in range(20):
    print("sin(" + str(count) + ") = " + str(math.sin(2*math.pi*count/360)) + ", cos(" + str(count) + ") = " + str(math.cos(2*math.pi*count/360)))


def randomAnimal():
    nouns = ["lion", "mouse", "cat", "dog"]
    noun = random.choice(nouns)     #在名詞字串中隨機選取一個字串
    return noun

for count in range(10):
    print(randomAnimal())

stop = time.time()

diff = stop - start

print("使用時間 " + str(diff) + " 秒")

time.clock()
