import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

print('------------------------------------------------------------')	#60個

'''
x0 = np.arange(-5, 5, 1)
y0 = np.arange(-5, 5, 1)
x, y = np.meshgrid(x0, y0)
z = np.c_[x.ravel(), y.ravel()]


print(len(x))
print(x.shape)
print(x)
print(len(y))
print(y.shape)
print(y)
print(len(z))
print(z.shape)
print(z)

print('x.ravel() = ', x.ravel())
print('y.ravel() = ', y.ravel())

plt.scatter(z[:, 0], z[:, 1], s = 100)
plt.grid()
plt.show()



print('------------------------------------------------------------')	#60個

print(np.c_[np.array([1, 2, 3]), np.array([4, 5, 6])])
print(np.c_[np.array([[1, 2, 3]]), 0, 0, np.array([[4, 5, 6]])])


"""
array([[1, 4],
       [2, 5],
       [3, 6]])
"""

#array([[1, 2, 3, ..., 4, 5, 6]])




print('------------------------------------------------------------')	#60個

#numpy.c_() and numpy.r_()的用法


#####np.c_是按行连接两个矩阵，就是把两矩阵左右相加，要求行数相等，类似于pandas中的merge()。
#####np.r_是按列连接两个矩阵，就是把两矩阵上下相加，要求列数相等，类似于pandas中的concat()。

#np.c_是按行连接两个矩阵，就是把两矩阵左右相加，要求行数相等。
#np.r_是按列连接两个矩阵，就是把两矩阵上下相加，要求列数相等。


#1.numpy.c_:

import numpy as np

x = np.arange(12).reshape(3,4)
print('x:',x, x.shape)

y = np.arange(10,22).reshape(3,4)
print('y:',y, y.shape)

z = np.c_[x,y]
print('z:',z, z.shape)

#2.numpy.r_用法:

import numpy as np

x = np.arange(12).reshape(3,4)
print('x:',x, x.shape)

y = np.arange(10,22).reshape(3,4)
print('y:',y, y.shape)

z = np.r_[x,y]
print('z:',z, z.shape)
'''
print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



X, Y = np.meshgrid(np.linspace(-6,3,30), np.linspace(-8,5,30))

#ravel 拉平法

X = X.ravel()

Y = Y.ravel()

plt.scatter(X, Y)

plt.show()


print('------------------------------------------------------------')	#60個


#zip 高級組合法

xx = [1,2,3,4]

yy = [5,6,7,8]

list(zip(xx,yy))

Z = list(zip(X,Y))
print(Z)

#plt.scatter(X, Y, s=50, c=Z)
plt.show()

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



