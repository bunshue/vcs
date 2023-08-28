# ch27_9.py
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# 建立軸單位長度相同的 ax 軸物件
figure, ax = plt.subplots(subplot_kw={'aspect':'equal'})     
center = (1,1)                      # 橢圓中心
width = 4                           # 橢圓水平軸直徑
height = 2                          # 橢圓垂直軸直徑
rect = Rectangle(xy=center,
                 width=width,
                 height=height,
                 facecolor='lightyellow',
                 edgecolor='b')     # 繪製矩形
ax.add_artist(rect)                 # 將物件加入軸物件
ax.set_xlim(0,6)
ax.set_ylim(0,4)
plt.show() 





