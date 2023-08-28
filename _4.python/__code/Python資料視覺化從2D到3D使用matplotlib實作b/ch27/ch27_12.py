# ch27_12.py
import matplotlib.pyplot as plt
import matplotlib.patches as patch
  
fig = plt.figure()
ax = fig.add_subplot(111)
  
rect1 = patch.Rectangle((-150, -200),   # 矩形 xy
                        400, 150,       # width, height
                        color ='g')     # 矩形是綠色 
rect2 = patch.Rectangle((-100, 10),     # 矩形 xy
                        400, 200,       # width, height
                        color ='m')     # 矩形是品紅色
rect3 = patch.Rectangle((-300, -50),    # 矩形 xy
                        100, 200,       # width, height
                        color ='y')     # 矩形是淺黃色
ax.add_patch(rect1)                     # 將 rect1 加入軸物件
ax.add_patch(rect2)                     # 將 rect2 加入軸物件
ax.add_patch(rect3)                     # 將 rect3 加入軸物件
plt.xlim([-400, 400])
plt.ylim([-300, 300]) 
plt.show()





