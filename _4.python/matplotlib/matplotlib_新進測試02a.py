import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


'''
print('------------------------------------------------------------')	#60個
                                
x = [x for x in range(0, 11)]                   
y = [(3 * y -18) for y in x]
plt.plot(x, y, '-*')   

plt.xticks(x)                           # 標記每個單一x數字
plt.axis([0, 10, -20, 15])              # 標記刻度範圍
plt.xlabel("children")
plt.ylabel("Apple")
plt.grid()                              # 加格線
plt.show()

print('------------------------------------------------------------')	#60個

x = [x for x in range(0, 11)]
y1 = [2 * y for y in x]
y2 = [3 * y for y in x]
y3 = [4 * y for y in x]
plt.xticks(x)
plt.plot(x, y1, label='L1')
plt.plot(x, y2, label='L2')
plt.plot(x, y3, label='L3')
plt.legend(loc='best')
plt.grid()                              # 加格線
plt.show()
'''

print('------------------------------------------------------------')	#60個

x = np.linspace(0, 10, 200)
y1 = np.sin(x)
y2 = np.sin(x) + 0.3*np.random.randn(200)

plt.subplot(121)
plt.plot(x, y1)

plt.subplot(122)
plt.scatter(x, y2)

plt.show()


print('------------------------------------------------------------')	#60個


x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])

X, Y = np.meshgrid(x, y)


print('------------------------------------------------------------')	#60個
from mpl_toolkits.mplot3d import Axes3D

π = np.pi
θ = np.linspace(-5*π, 5*π, 200)

x = np.cos(θ)
y = np.sin(θ)
z = θ/(5*π)

#ax = fig.add_subplot(231, projection='3d')  #第一張圖
ax = plt.gca(projection='3d')
plt.plot(x, y, z)

plt.show()

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

