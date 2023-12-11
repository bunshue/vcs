# 新進測試05

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

import pandas as pd

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

X, Y = np.meshgrid(np.linspace(-6, 3, 30), np.linspace(-8, 5, 30))

#ravel 拉平法

X = X.ravel()

Y = Y.ravel()

plt.scatter(X, Y)

plt.show()

print('------------------------------------------------------------')	#60個

""" fail
#zip 高級組合法

xx = [1, 2, 3, 4]
yy = [5, 6, 7, 8]
list(zip(xx, yy))

Z = list(zip(X, Y))
print(Z)

plt.scatter(X, Y, s = 50, c = Z)
plt.show()
"""

print('------------------------------------------------------------')	#60個

N = 100

sinc2d = np.zeros((N, N))
for x, x1 in enumerate(np.linspace(-10, 10, N)):
     for y, x2 in enumerate(np.linspace(-10, 10, N)):
         sinc2d[x,y] = np.sin(x1) * np.sin(x2) / (x1 * x2)
#print(sinc2d)

# same
x1 = np.linspace(-10, 10, N)
x2 = np.linspace(-10, 10, N)
sinc2d = np.outer(np.sin(x1), np.sin(x2)) / np.outer(x1, x2)
#print(sinc2d)

plt.imshow(sinc2d)
plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

