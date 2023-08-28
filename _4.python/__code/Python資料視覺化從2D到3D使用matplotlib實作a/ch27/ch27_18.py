# ch27_18.py  
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patch

circle = patch.Circle((2, 8), 1.5, fc='r')
square = patch.Rectangle((7, 6.5), 2.5, 3, fc='b')
triangle = patch.Polygon(((0.5,1),(4,1),(2.2, 3.8)),fc='m')
diamond = patch.Polygon(((5,2),(7,5.3),(5,8.5),(3,5.3)),fc='g')

fig = plt.figure()
ax = fig.add_subplot(fc='lightyellow', aspect='equal')
# for 迴圈加入外形物件
for shape in (square, circle, triangle, diamond):
    ax.add_artist(shape)                # 加入物件
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set(xlim=(0,10),ylim=(0,10))         # 設定顯示區間
plt.show()




