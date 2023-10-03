import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 2*np.pi, 50)                   # 建立 50 個點
y1 = np.sin(x)
plt.scatter(x,y1,c=y1,cmap='rainbow',marker='*')    # 繪製 sin 
y2 = np.cos(x)
plt.scatter(x,y2,c=y2,cmap='rainbow',marker='s')    # 繪製 cos 

plt.show()
