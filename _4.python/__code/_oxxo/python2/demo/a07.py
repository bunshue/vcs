# encoding:UTF-8
import random

""" 
arr = []
for i in range(1, 50):
    arr.append(i)

lto = []
for i in range(6):
    arrLength = int(len(arr)) - 1
    lto.append(arr.pop(random.randint(0, arrLength))) 
"""

# 使用 random.sample 一行搞定
lto = random.sample(range(1,50), k = 6)
lto.sort()
print(lto)
