# ch10_12.py
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
np.random.seed(10)                      # 設定種子值
N = 100
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 150 * r**2
colors = theta
plt.subplot(projection='polar')
plt.scatter(theta,r,c=colors,s=area,cmap='rainbow',alpha=0.8)
plt.show()


