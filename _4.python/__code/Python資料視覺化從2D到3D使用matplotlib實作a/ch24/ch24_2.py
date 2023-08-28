# ch24_2.py
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
plt.contourf(X, Y, Z, cmap='PuRd')
plt.title('contourf函數, cmap=PuRd',fontsize=16,color='b')

fig.add_subplot(122)
plt.contourf(X, Y, Z, cmap='YlOrBr')
plt.title('contourf函數, cmap=YlOrBr',fontsize=16,color='b')
plt.show()


      
