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

