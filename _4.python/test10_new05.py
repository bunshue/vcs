import os
import sys
import time
import random


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

# id的用法

fruits = {"西瓜": 15, "香蕉": 20, "水蜜桃": 25, "蘋果": 18}
cfruits = fruits.copy()
print("位址 = ", id(fruits), "  fruits元素 = ", fruits)
print("位址 = ", id(cfruits), "  fruits元素 = ", cfruits)


print("------------------------------------------------------------")  # 60個


import random  # 導入模組random

fruits = ["蘋果", "香蕉", "西瓜", "水蜜桃", "百香果"]

count = []
for _ in range(10):
    cc = random.choice(fruits)
    print(cc)


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


"""
双色球随机选号程序
"""

from random import randrange, randint, sample


def display(balls):
    """
    输出列表中的双色球号码
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print("|", end=" ")
        print("%02d" % ball, end=" ")
    print()


def random_select():
    """
    随机选择一组号码
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    for _ in range(6):
        index = randrange(len(red_balls))
        selected_balls.append(red_balls[index])
        del red_balls[index]
    # 上面的for循环也可以写成下面这行代码
    # sample函数是random模块下的函数
    # selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input("机选几注: "))
    for _ in range(n):
        display(random_select())


if __name__ == "__main__":
    main()


print("------------------------------------------------------------")  # 60個


"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low**3 + mid**3 + high**3:
        print(num)


print("------------------------------------------------------------")  # 60個

# 函数的定义和使用 - 求最大公约数和最小公倍数


def gcd(x, y):
    if x > y:
        (x, y) = (y, x)
    for factor in range(x, 1, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
    return 1


def lcm(x, y):
    return x * y // gcd(x, y)


print(gcd(15, 27))
print(lcm(15, 27))


print("------------------------------------------------------------")  # 60個

import time
import shutil
import os

seconds = time.time()
print(seconds)
localtime = time.localtime(seconds)
print(localtime)
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)
asctime = time.asctime(localtime)
print(asctime)
strtime = time.strftime("%Y-%m-%d %H:%M:%S", localtime)
print(strtime)
mydate = time.strptime("2018-1-1", "%Y-%m-%d")
print(mydate)

# shutil.copy('/Users/Hao/hello.py', '/Users/Hao/Desktop/first.py')
os.system("ls -l")
# os.chdir('/Users/Hao')
os.system("ls -l")
# os.mkdir('test')

print("------------------------------------------------------------")  # 60個

# 用range创建数值列表
list1 = list(range(1, 11))  # 不含尾
print(list1)


print("------------------------------------------------------------")  # 60個
