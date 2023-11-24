"""

必學！Python 資料科學‧機器學習最強套件 numpy

"""

import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

import numpy as np


print('------------------------------------------------------------')	#60個

#NumPy 的高速運算

from numpy.random import rand

N = 300

print('建立NXN之隨機矩陣A')
matA = np.array(rand(N, N))

print('建立NXN之隨機矩陣B')
matB = np.array(rand(N, N))

print('建立NXN之矩陣C 元素全為3')
matC = np.array([[3] * N for _ in range(N)])

print(matA.shape)
#print(matA)
print(matB.shape)
#print(matB)
print(matC.shape)
#print(matC)

print('------------------------------------------------------------')	#60個

print('使用 Python 計算')
start = time.time() 

for i in range(N):
    for j in range(N):
        for k in range(N):
            matC[i][j] = matA[i][k] * matB[k][j]

time1 = time.time() - start
print("Python 的計算結果：%f[sec]" % float(time1))


print('使用 NumPy 計算')
start = time.time()

matC = np.dot(matA, matB)

time2 = time.time() - start
print("NumPy 的計算結果：%f[sec]" % float(time2))

if time2 < 0.000001:
    time2 = 0.000001
print('使用numpy快了 ', time1/time2, ' 倍')

print('------------------------------------------------------------')	#60個

#建立陣列

cc = np.array([1, 2, 3])
print(cc)

print(np.arange(5))
print(np.arange(1, 5))
print(np.arange(0, 10, 2))
print(np.linspace(0, 1, 5)) #0~1共分5個, 包含頭尾
print(np.zeros(5))#零陣列
print(np.ones(5))#壹陣列

print('不固定亂數種子')
X = np.random.randn(5)
Y = np.random.randn(5)

print('X:', X)
print('Y:', Y)


print('固定亂數種子')
np.random.seed(0)
X = np.random.randn(5)

np.random.seed(0)
Y = np.random.randn(5)

print('X (seed=0):', X)
print('Y (seed=0):', Y)

#X: [-0.89002049  0.30911242 -0.69646098 -0.68680865  0.54940027]
#Y: [-0.11053683  0.81934032 -1.48607749 -1.10757407  0.24476998]

#X (seed=0): [1.76405235 0.40015721 0.97873798 2.2408932  1.86755799]
#Y (seed=0): [1.76405235 0.40015721 0.97873798 2.2408932  1.86755799]

print('------------------------------------------------------------')	#60個

# arr1
arr1 = np.random.randint(0, 11, (5, 2))
print('arr1:')
print(arr1)

# arr2
arr2 = np.random.rand(3)
print('arr2:')
print(arr2)

print('------------------------------------------------------------')	#60個

np.random.seed(0)
x = ['蘋果', '橘子', '香蕉', '鳳梨', '奇異果', '草莓']
print(np.random.choice(x, 5))

#['奇異果' '草莓' '蘋果' '鳳梨' '鳳梨']

print('------------------------------------------------------------')	#60個

print('---------------↓不使用 copy()↓---------------')

arr1 = np.array([1, 2, 3, 4, 5])

print('arr1:'+str(arr1))

arr2 = arr1

arr2[0] = 100

print('arr2:'+str(arr1))

print('arr1:'+str(arr2))

print('---------------↓使用 copy()↓-----------------')

arr1 = np.array([1, 2, 3, 4, 5])

print(arr1)

arr2 = arr1.copy()

arr2[0] = 100

print('arr1:'+str(arr1))

print('arr2:'+str(arr2))

print('arr1:'+str(arr1))

print('------------------------------------------------------------')	#60個

#陣列的切片操作
arr = np.arange(10)
print(arr)

arr[0:3] = 1
print(arr)

print('------------------------------------------------------------')	#60個

#使用布林陣列篩選值

arr = np.arange(10)

new_arr = arr < 5

print(arr)

print(new_arr)

print(arr[new_arr])

print('------------------------------------------------------------')	#60個

#陣列的四則計算

# 使用 Python 的 list

storages = [1, 2, 3, 4]

new_storages = []

for n in storages:
    n += n
    new_storages.append(n)

print(new_storages)

#[2, 4, 6, 8]

print('------------------------------------------------------------')	#60個

# 使用 NumPy 陣列

storages = np.array([1, 2, 3, 4])

storages += storages

print(storages)

#[2 4 6 8]

arr_1 = np.array([2, 4, 6, 8, 10])

arr_2 = np.array([1, 3, 5, 7, 9])

# arr + arr (相加)

print('arr_1 + arr_2:')

print(arr_1 + arr_2)

print('--------------------------')

# arr - arr (相減)

print('arr_1 - arr_2:')

print(arr_1 - arr_2)

print('--------------------------')

# arr ** 3 (三次方)

print('arr_1 ** 3:')

print(arr_1 ** 3)

print('--------------------------')

# arr_1 / arr_2(相除)

print('arr_1 / arr_2:')

print(arr_1 / arr_2)

print()

print('------------------------------------------------------------')	#60個

#體驗好用的 NumPy 函式

arr = np.array([4, -9, 16, -4, 20])

print(arr)

arr_abs = np.abs(arr)

print('絕對值:',arr_abs)

print('e為底數:',np.exp(arr_abs))

print('平方根:',np.sqrt(arr_abs))

arr1 = np.array([2, 5, 7, 9, 5, 2])

arr2 = np.array([2, 5, 8, 3, 1])

new_arr1 = np.unique(arr1)

print('剔除arr1重複元素:',new_arr1)

print('聯集:',np.union1d(new_arr1, arr2))

print('交集:',np.intersect1d(new_arr1, arr2))

print('差集:',np.setdiff1d(new_arr1, arr2))

print('------------------------------------------------------------')	#60個

#陣列的軸 (axis)

arr = np.array([ [1, 2 ,3],
                 [4, 5, 6]])

print(arr.sum())

print(arr.sum(axis=0))

print(arr.sum(axis=1))

arr = np.array([[[0, 1, 2],
                 [3, 4, 5]],
                [[6, 7, 8],
                 [9, 10, 11]]])
print(arr.sum())
print(arr.sum(axis=0))
print(arr.sum(axis=1))
print(arr.sum(axis=2))

print('------------------------------------------------------------')	#60個

#陣列的 shape 與 reshape

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])

print('原 shape 為:',arr.shape)

print(arr.reshape(4, 2))

print('------------------------------------------------------------')	#60個

#多軸陣列的切片做法

arr = np.array([[1, 2 ,3],
                [4, 5, 6]])
print(arr[1])

arr = np.array([[1, 2 ,3],
                [4, 5, 6]])
print(arr[1][2])

arr = np.array([[1, 2 ,3],
                [4, 5, 6]])
print(arr[1,1:])

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
print(arr[[3, 2, 0]])

print('------------------------------------------------------------')	#60個

#陣列轉置 (transpose)

arr = np.arange(10).reshape(2, 5)
print(arr.T)

# print(arr.transpose(1,0))

print('------------------------------------------------------------')	#60個

#陣列排序

arr = np.array([[8, 4, 2],
                [3, 5, 1]])

print('---------------原陣列----------------')

print(arr)

print('----------對 arr 以軸 1 方向排序---------')

print(np.sort(arr))

print('----------對 arr 以軸 0 方向排序---------')

arr.sort(axis = 0)

print(arr)

print('-------------argsort排序-------------')

print(arr.argsort())

print('------------------------------------------------------------')	#60個

#陣列擴張 (Broadcasting)

x = np.arange(15).reshape(3, 5)
y = np.array([np.arange(5)])
z = x - y
print(z)

print('------------------------------------------------------------')	#60個

#用 NumPy 函式計算矩陣乘積

arr = np.arange(9).reshape(3, 3)

print(np.dot(arr, arr))

print('------------------------------------------------------------')	#60個


