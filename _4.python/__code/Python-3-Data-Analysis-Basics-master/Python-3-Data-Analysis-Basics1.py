"""

Python-3-Data-Analysis-Basics 1


"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print('------------------------------------------------------------')	#60個

'''
x = np.linspace(0, 1, 200)
y = -(x - 1) ** 2 + 1

X = np.random.rand(6)
Y = np.random.rand(6)

def myplot(n = 1):
    plt.scatter(X, Y, c = 'r', s = 100)
    x = np.linspace(0, 1, 1000)
    y = 0.5*np.sin(n*x) + 0.5
    plt.plot(x, y)

myplot(5)
plt.show()

print('------------------------------------------------------------')	#60個

#過度擬合 (overfitting)

#用拉格朗日 (Lagrange) 插值法學起來!

x = np.linspace(0, 1, 200)
y = -(x - 1) ** 2 + 1
plt.plot(x, y, 'lime')

X = np.linspace(0, 1, 20)
Y = -(X-1) ** 2 + 1 + 0.08 * np.random.randn(20)
plt.scatter(X,Y, c = 'b', s = 50)

z = np.polyfit(X, Y, 19)
p = np.poly1d(z)
plt.plot(x, p(x),'r')

xmin, xmax, ymin, ymax = 0, 1, 0, 1.5
plt.axis([xmin, xmax, ymin, ymax])  #設定各軸顯示範圍

plt.show()

'''
print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

print('作業完成')

