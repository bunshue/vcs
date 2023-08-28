# ch12_11.py
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4])
y = np.array([8,7,6])
xx, yy = np.meshgrid(x,y)
plt.scatter(xx,yy,marker='o',c='m')
plt.show()





