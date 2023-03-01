import random

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




