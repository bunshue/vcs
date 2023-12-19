import os
import sys
import time
import random

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
