# ch29_5.py
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
x = np.random.random(150)*10            # 建立150個0 - 10的隨機數
y = np.random.random(150)*15            # 建立150個0 - 15的隨機數
z = np.random.random(150)*20            # 建立150個0 - 20的隨機數
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('x',fontsize=14,color='b')
ax.set_ylabel('y',fontsize=14,color='b')
ax.set_zlabel('z',fontsize=14,color='b')
ax.scatter(x, y, z, marker='*', color='m')
plt.show()


 

