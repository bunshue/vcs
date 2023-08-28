# ch9_16.py
import matplotlib.pyplot as plt
import numpy as np

trials = 2000
Hits = 0
radius = 50
for i in range(trials):
    x = np.random.randint(1, 100)               # x軸座標
    y = np.random.randint(1, 100)               # y軸座標
    if np.sqrt((x-50)**2 + (y-50)**2) < radius: # 在圓內
        plt.scatter(x, y, marker='.', c='y')
        Hits += 1
    else:
        plt.scatter(x, y, marker='.', c='g')    
plt.axis('equal')
plt.show()











