import os
import sys
import time
import random


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

#id的用法

fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25, '蘋果':18}
cfruits = fruits.copy( )
print("位址 = ", id(fruits), "  fruits元素 = ", fruits)
print("位址 = ", id(cfruits), "  fruits元素 = ", cfruits)


print('------------------------------------------------------------')	#60個


import random                       # 導入模組random

fruits = ['蘋果', '香蕉', '西瓜', '水蜜桃', '百香果']

count = [];
for _ in range(10):
    cc = random.choice(fruits)
    print(cc)





print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個



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
            print('|', end=' ')
        print('%02d' % ball, end=' ')
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
    n = int(input('机选几注: '))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()







print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


