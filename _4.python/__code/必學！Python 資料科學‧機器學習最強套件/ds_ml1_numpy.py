"""

必學！Python 資料科學‧機器學習最強套件 numpy

"""

import os
import sys
import time
import random


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


#5-1 體驗 NumPy 的高速運算

import numpy as np

from numpy.random import rand

import time

​

​

N = 150

matA = np.array(rand(N, N))

matB = np.array(rand(N, N))

matC = np.array([[0] * N for _ in range(N)])

​

​

# 使用 Python 計算

start = time.time() 

for i in range(N):

    for j in range(N):

        for k in range(N):

            matC[i][j] = matA[i][k] * matB[k][j]

print("Python 的計算結果：%f[sec]" % float(time.time() - start))

​

# 使用 NumPy 計算

​

start = time.time()

matC = np.dot(matA, matB)

​

​

# 如果NumPy出現0.00[sec], 不代表真的是0, 而是小數點第2位後不表示的結果

print("NumPy 的計算結果：%f[sec]" % float(time.time() - start))

​

Python 的計算結果：4.585647[sec]

NumPy 的計算結果：0.008511[sec]

#5-2-1 建立陣列

np.array([1, 2, 3])

array([1, 2, 3])

print(np.arange(5))

print(np.arange(1,5))

print(np.arange(0,10,2))

[0 1 2 3 4]

[1 2 3 4]

[0 2 4 6 8]

print(np.linspace(0,1,5))

[0.   0.25 0.5  0.75 1.  ]

print(np.zeros(5))

print(np.ones(5))

[0. 0. 0. 0. 0.]

[1. 1. 1. 1. 1.]

import numpy as np

X = np.random.randn(5)

Y = np.random.randn(5)

print('X:', X)

print('Y:', Y)

np.random.seed(0)

X = np.random.randn(5)

np.random.seed(0)

Y = np.random.randn(5)

print('X (seed=0):', X)

print('Y (seed=0):', Y)

X: [-0.89002049  0.30911242 -0.69646098 -0.68680865  0.54940027]

Y: [-0.11053683  0.81934032 -1.48607749 -1.10757407  0.24476998]

X (seed=0): [1.76405235 0.40015721 0.97873798 2.2408932  1.86755799]

Y (seed=0): [1.76405235 0.40015721 0.97873798 2.2408932  1.86755799]

import numpy as np

# arr1

arr1 = np.random.randint(0, 11, (5, 2))

print('arr1:')

print(arr1)

# arr2

arr2 = np.random.rand(3)

print('arr2:')

print(arr2)

arr1:

[[ 4  7]

 [ 6  8]

 [ 8 10]

 [ 1  6]

 [ 7  7]]

arr2:

[0.47997717 0.3927848  0.83607876]

import numpy as np

np.random.seed(0)

x = ['蘋果', '橘子', '香蕉', '鳳梨', '奇異果', '草莓']

print(np.random.choice(x, 5))

['奇異果' '草莓' '蘋果' '鳳梨' '鳳梨']

import numpy as np

print('---------------↓不使用 copy()↓---------------')

arr1 = np.array([1, 2, 3, 4, 5])

print('arr1:'+str(arr1))

arr2 = arr1

arr2[0] = 100

print('arr2:'+str(arr1))

print('arr1:'+str(arr2))

---------------↓不使用 copy()↓---------------

arr1:[1 2 3 4 5]

arr2:[100   2   3   4   5]

arr1:[100   2   3   4   5]

print('---------------↓使用 copy()↓-----------------')

arr1 = np.array([1, 2, 3, 4, 5])

print(arr1)

arr2 = arr1.copy()

arr2[0] = 100

print('arr1:'+str(arr1))

print('arr2:'+str(arr2))

print('arr1:'+str(arr1))

---------------↓使用 copy()↓-----------------

[1 2 3 4 5]

arr1:[1 2 3 4 5]

arr2:[100   2   3   4   5]

arr1:[1 2 3 4 5]

#5-2-2 陣列的切片操作

import numpy as np

arr = np.arange(10)

print(arr)

arr[0:3] = 1

print(arr)

[0 1 2 3 4 5 6 7 8 9]

[1 1 1 3 4 5 6 7 8 9]

#5-2-3 使用布林陣列篩選值

import numpy as np

arr = np.arange(10)

new_arr = arr<5

print(arr)

print(new_arr)

[0 1 2 3 4 5 6 7 8 9]

[ True  True  True  True  True False False False False False]

print(arr[new_arr])

[0 1 2 3 4]

#5-2-4 陣列的四則計算

# 使用 Python 的 list

storages = [1, 2, 3, 4]

new_storages = []

for n in storages:

  n += n

  new_storages.append(n)

print(new_storages)

[2, 4, 6, 8]

# 使用 NumPy 陣列

import numpy as np

storages = np.array([1, 2, 3, 4])

storages += storages

print(storages)

[2 4 6 8]

import numpy as np

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

arr_1 + arr_2:

[ 3  7 11 15 19]

--------------------------

arr_1 - arr_2:

[1 1 1 1 1]

--------------------------

arr_1 ** 3:

[   8   64  216  512 1000]

--------------------------

arr_1 / arr_2:

[2.         1.33333333 1.2        1.14285714 1.11111111]


#5-2-5 體驗好用的 NumPy 函式

import numpy as np

arr = np.array([4, -9, 16, -4, 20])

print(arr)

arr_abs = np.abs(arr)

print('絕對值:',arr_abs)

print('e為底數:',np.exp(arr_abs))

print('平方根:',np.sqrt(arr_abs))

[ 4 -9 16 -4 20]

絕對值: [ 4  9 16  4 20]

e為底數: [5.45981500e+01 8.10308393e+03 8.88611052e+06 5.45981500e+01

 4.85165195e+08]

平方根: [2.         3.         4.         2.         4.47213595]

import numpy as np

arr1 = np.array([2, 5, 7, 9, 5, 2])

arr2 = np.array([2, 5, 8, 3, 1])

new_arr1 = np.unique(arr1)

print('剔除arr1重複元素:',new_arr1)

print('聯集:',np.union1d(new_arr1, arr2))

print('交集:',np.intersect1d(new_arr1, arr2))

print('差集:',np.setdiff1d(new_arr1, arr2))

剔除arr1重複元素: [2 5 7 9]

聯集: [1 2 3 5 7 8 9]

交集: [2 5]

差集: [7 9]

#5-3-1 陣列的軸 (axis)

arr = np.array([ [1, 2 ,3],

[4, 5, 6]])

print(arr.sum())

print(arr.sum(axis=0))

print(arr.sum(axis=1))

21

[5 7 9]

[ 6 15]

import numpy as np

arr = np.array([[[0,1,2],

[3,4,5]],

[[6,7,8],

[9,10,11]]])

print(arr.sum())

66

print(arr.sum(axis=0))

[[ 6  8 10]

 [12 14 16]]

print(arr.sum(axis=1))

[[ 3  5  7]

 [15 17 19]]

print(arr.sum(axis=2))

[[ 3 12]

 [21 30]]

#5-3-2 陣列的 shape

import numpy as np

arr = np.array([[1, 2, 3, 4],

[5, 6, 7, 8]])

print('原 shape 為:',arr.shape)

print(arr.reshape(4, 2))

原 shape 為: (2, 4)

[[1 2]

 [3 4]

 [5 6]

 [7 8]]

#5-3-3 多軸陣列的切片做法

arr = np.array([[1, 2 ,3],

[4, 5, 6]])

print(arr[1])

[4 5 6]

arr = np.array([[1, 2 ,3],

[4, 5, 6]])

print(arr[1][2])

6

import numpy as np

arr = np.array([[1, 2 ,3],

[4, 5, 6]])

print(arr[1,1:])

[5 6]

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])

print(arr[[3, 2, 0]])

[[7 8]

 [5 6]

 [1 2]]

#5-3-4 陣列轉置 (transpose)

import numpy as np

arr = np.arange(10).reshape(2, 5)

print(arr.T)

# print(arr.transpose(1,0))

[[0 5]

 [1 6]

 [2 7]

 [3 8]

 [4 9]]

#5-3-5 陣列排序

import numpy as np

arr = np.array([[8, 4, 2],

[3, 5, 1]])

print('---------------原陣列----------------')

print(arr)

print('----------對 arr 以軸 1 方向排序---------')

print(np.sort(arr))

print('----------對 arr 以軸 0 方向排序---------')

arr.sort(axis=0)

print(arr)

---------------原陣列----------------

[[8 4 2]

 [3 5 1]]

----------對 arr 以軸 1 方向排序---------

[[2 4 8]

 [1 3 5]]

----------對 arr 以軸 0 方向排序---------

[[3 4 1]

 [8 5 2]]

print('-------------argsort排序-------------')

print(arr.argsort())

-------------argsort排序-------------

[[2 0 1]

 [2 1 0]]

#5-3-6 陣列擴張 (Broadcasting)

import numpy as np

x = np.arange(15).reshape(3, 5)

y = np.array([np.arange(5)])

z = x - y

print(z)

[[ 0  0  0  0  0]

 [ 5  5  5  5  5]

 [10 10 10 10 10]]

#5-3-7 用 NumPy 函式計算矩陣乘積

import numpy as np

arr = np.arange(9).reshape(3, 3)

print(np.dot(arr, arr))

[[ 15  18  21]

 [ 42  54  66]

 [ 69  90 111]]

​



print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


