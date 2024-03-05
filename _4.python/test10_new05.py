import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

print('enumerate 的用法')

print('字串轉串列')
animal_string = "鼠牛虎兔龍蛇馬羊猴雞狗豬"
animal_list = list(animal_string)

for i, ani in enumerate(animal_list):
    print(i, ani)

print("------------------------------------------------------------")  # 60個

print('字串轉串列')
animal_string = "鼠牛虎兔龍蛇馬羊猴雞狗豬"
animal_list = list(animal_string)

print(type(animal_list))

print('字串切片 slicing')

n = 3
m = 9

print('第n個')
cc = animal_list[n]
print(cc)
print('第n個 到 第m-1個')
cc = animal_list[n:m]
print(cc)
print('第n個 到 最後一個')
cc = animal_list[n:]
print(cc)
print('第0個 到 第m-1個')
cc = animal_list[:m]
print(cc)
print('全部')
cc = animal_list[:]
print(cc)
print('反相')
cc = animal_list[::-1]
print(cc)

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
