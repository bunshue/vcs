# ch32_8.py
from matplotlib.animation import FuncAnimation 
import matplotlib.pyplot as plt  
import numpy as np  

# 輸出矩陣影像, 這個函數將被重複調用
def animate(i):
    pict = np.random.rand(8,8)
    ax.imshow(pict, cmap='jet')
# 建立動畫需要的 Figure 物件和軸物件       
fig, ax = plt.subplots()
# interval = 50, 相當於每隔 0.05 秒執行 animate()動畫
anim = FuncAnimation(fig,animate,frames=50,interval=50)
ax.set_axis_off()
plt.show()



