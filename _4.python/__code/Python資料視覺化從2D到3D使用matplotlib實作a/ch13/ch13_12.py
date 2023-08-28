# ch13_12.py
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10)
N = 20                                      # 長條個數
theta = np.linspace(0.0, 2 * np.pi, N)      # 角度個數  
radius = 10 * np.random.rand(N)             # 半徑個數
width = np.pi / 4 * np.random.rand(N)       # 寬度個數
colors = plt.cm.hsv(radius / 10)            # 色彩個數
ax = plt.subplot(projection='polar')        # 建立子圖
# 繪製極座標長條圖
ax.bar(theta,radius,width,bottom=0.0,alpha=0.8,color=colors)
plt.show()

