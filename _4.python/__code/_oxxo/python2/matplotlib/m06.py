import numpy as np
from matplotlib import pyplot as plt

n = 100
ax = np.random.normal(0,1,n)
ay = np.random.normal(0,1,n)
bx = np.random.normal(0,1,n)
by = np.random.normal(0,1,n)

plt.scatter(ax, ay, alpha=0.5, s=100, color='red')
plt.scatter(bx, by, alpha=0.5, s=100, color='blue')
plt.xlim = (0 , 1)
plt.ylim = (0 , 1)

plt.show()



