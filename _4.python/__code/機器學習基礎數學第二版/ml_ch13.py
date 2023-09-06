import sys

import numpy as np
import matplotlib.pyplot as plt

import random

print('------------------------------------------------------------')	#60個

min = 1
max = 6
for i in range(10):
    print(random.randint(min, max), end = ' ')
print()

print('------------------------------------------------------------')	#60個

from random import randint

min = 1
max = 6                                         # 骰子有幾面
times = 10000                                   # 擲骰子次數

dice = [0] * 7                                  # 建立擲骰子的串列
for i in range(times):
    data = randint(min, max)
    dice[data] += 1
print(dice)    
del dice[0]                                     # 刪除索引0資料
    
for i, c in enumerate(dice, 1):
    print('{} = {} 次'.format(i, c))
print(dice)
x = [i for i in range(1, max+1)]                # 長條圖x軸座標
width = 0.35                                    # 長條圖寬度
plt.bar(x, dice, width, color='g')              # 繪製長條圖
plt.ylabel('Frequency')
plt.title('Test 10000 times')

plt.show()

print('------------------------------------------------------------')	#60個

print('建立 1 個隨機數')
x = np.random.rand()
print(x)

print('建立 3 個隨機數')
x = np.random.rand(3)
print(x)
    
print('建立 3x2 個隨機數')
x = np.random.rand(3, 2)
print(x)

print('------------------------------------------------------------')	#60個

print('建立 1 個 0-4(含) 的整數隨機數')
x = np.random.randint(5)
print(x)

print('建立 3 個 0-9(含) 的整數隨機數')
x = np.random.randint(10,size=3)
print(x)

print('建立 3x2 個0-9(含) 的整數隨機數')
x = np.random.randint(0, 10, size=(3,2))
print(x)

print('------------------------------------------------------------')	#60個

sides = 6
# 建立 10000 個 1-6(含) 的整數隨機數
dice = np.random.randint(1,sides+1,size=10000)  # 建立隨機數
    
h = plt.hist(dice, sides)                       # 繪製hist圖
print("bins的y軸 ",h[0])
print("bins的x軸 ",h[1])
plt.ylabel('Frequency')
plt.title('Test 10000 times')

plt.show()

print('------------------------------------------------------------')	#60個

print('固定random seed')
np.random.seed(5)
x = np.random.randint(10, size=10)
print(x)

print('------------------------------------------------------------')	#60個

# 一維陣列
arr1 = np.arange(9)
print("一維陣列")
print(arr1)
np.random.shuffle(arr1)         # 重新排列
print("重新排列")
print(arr1)

# 二維陣列
arr2 = np.arange(9).reshape((3,3))
print("二維陣列")
print(arr2)
np.random.shuffle(arr2)         # 重新排列
print("重新排列")
print(arr2)

print('------------------------------------------------------------')	#60個

fruits = ["Apple", "Orange", "Grapes", "Banana", "Mango"]
fruit1 = np.random.choice(fruits,3)
print("隨機挑選 3 種水果")
print(fruit1)

fruit2 = np.random.choice(fruits,5)
print("隨機挑選 5 種水果 -- 可以重複")
print(fruit2)
    
fruit3 = np.random.choice(fruits,5,replace=False)
print("隨機挑選 5 種水果 -- 不可以重複")
print(fruit3)

print('------------------------------------------------------------')	#60個

fruits = ["Apple", "Orange", "Grapes", "Banana", "Mango"]
fruit1 = np.random.choice(fruits,5,p=[0.8,0.05,0.05,0.05,0.05])
print("依權重挑選 5 種水果")
print(fruit1)

fruit2 = np.random.choice(fruits,5,p=[0.05,0.05,0.05,0.05,0.8])
print("依權重挑選 5 種水果")
print(fruit2)


print('------------------------------------------------------------')	#60個

