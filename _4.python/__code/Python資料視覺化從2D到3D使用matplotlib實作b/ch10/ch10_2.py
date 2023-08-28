# ch10_2.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.linspace(0.0, 2*np.pi, 50)               # 建立 50 個點
y1 = np.sin(x)
plt.scatter(x,y1,c=x,cmap='rainbow',marker='*') # 繪製 sin 
y2 = np.cos(x)
plt.scatter(x,y2,c=x,cmap='rainbow',marker='s') # 繪製 cos 
plt.xlabel('角度')
plt.ylabel('正弦波值')
plt.title('Sin 和 Cos Wave', fontsize=16)
plt.show()



