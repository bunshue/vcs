# ch24_1.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
x = range(5)
y = range(5)
X, Y = np.meshgrid(x, y)
Z = [[0,0,0,0,0],
     [0,1,1,1,0],
     [0,1,2,2,0],
     [0,1,1,1,0],
     [0,0,0,0,0]]
fig = plt.figure(figsize=(10,4.5))
fig.add_subplot(121)
plt.contour(X, Y, Z)
plt.title('使用contour函數',fontsize=16,color='b')

fig.add_subplot(122)
plt.contourf(X, Y, Z)
plt.title('使用contourf函數',fontsize=16,color='b')
plt.show()


      
