# ch27_10.py
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

fig = plt.figure()  
ax = fig.add_subplot(111)
img = np.arange(25).reshape(5, 5)       # 建立影像 
ax.imshow(img, cmap='Blues')
ax.add_patch(Rectangle((0.5,0.5),       # 矩形 xy
                       3, 3,            # 寬與高
                       fc ='none',      # 內部顏色
                       ec = 'g',        # 矩形框的顏色
                       linestyle='--',  # 線條樣式
                       lw = 8) )        # 矩形線寬
plt.show()





