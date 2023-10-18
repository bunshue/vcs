"""

過度擬合


"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print('------------------------------------------------------------')	#60個


#過度擬合 (overfitting)
#

print('------------------------------------------------------------')	#60個
'''
X = np.random.rand(6)
Y = np.random.rand(6)

def myplot(n=1):
    plt.scatter(X, Y, c='r', s=100)
    x = np.linspace(0, 1, 1000)
    y = 0.5*np.sin(n*x) + 0.5
    plt.plot(x, y)

plt.plot(x,y)
plt.show()
'''

print('------------------------------------------------------------')	#60個

x = np.linspace(0, 1, 200)
y = -(x-1)**2+1
plt.plot(x,y)

X = np.linspace(0, 1, 20)
Y = -(X-1)**2+1 + 0.08*np.random.randn(20)
plt.scatter(X,Y, c='r',s=50)

xmin, xmax, ymin, ymax = 0, 1, 0, 1.5
plt.axis([xmin, xmax, ymin, ymax])  #設定各軸顯示範圍

plt.show()

print('------------------------------------------------------------')	#60個

#用拉格朗日 (Lagrange) 插值法學起來!

plt.plot(x,y)

z = np.polyfit(X, Y, 19)
p = np.poly1d(z)
plt.plot(x, p(x),'r')
plt.scatter(X,Y, c='r',s=50)

xmin, xmax, ymin, ymax = 0, 1, 0, 1.5
plt.axis([xmin, xmax, ymin, ymax])  #設定各軸顯示範圍

plt.show()



print('------------------------------------------------------------')	#60個



print('作業完成')

