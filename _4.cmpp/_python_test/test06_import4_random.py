import random

member = ["���", "���l", "��c�l", "�᪨"]
housework = ["���a", "��a", "�~��A", "������"]
random.shuffle(housework)
for i in range(4):
    print("%s���ѭt�d%s" % (member[i], housework[i]))
    
for count in range(20):
    x = random.randrange(-10, 10)       #-10~9���������
    y = random.randrange(-10, 10)       #-10~9���������
    length = random.randrange(10)       #0~9���������
    shape = random.randrange(3, 8)      #3~7���������
    print(count, x, y, length, shape)



def randomAnimal():
    nouns = ["lion", "mouse", "cat", "dog"]
    noun = random.choice(nouns)     #�b�W���r�ꤤ�H������@�Ӧr��
    return noun

for count in range(10):
    print(randomAnimal())

from random import randint
print("1��6��@��")
for count in range(10):
    print(randint(1, 6))


import random as R
print("1��6��@��")
for count in range(10):
    print(R.randint(1, 6))

print("����@��")
for count in range(10):
    print(random.choice(['a', 'b', 'c']))


