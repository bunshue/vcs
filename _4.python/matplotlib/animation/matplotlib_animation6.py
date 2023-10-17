from matplotlib.animation import FuncAnimation 
import matplotlib.pyplot as plt  
import numpy as np  

# 輸出矩陣影像, 這個函數將被重複調用
def animate(i):
    pict = np.random.rand(8,8)
    ax.imshow(pict, cmap='jet')

# 建立動畫需要的 Figure 物件和軸物件       
fig, ax = plt.subplots()

interval = 100   #每隔 interval msec 執行 animate()動畫
anim = FuncAnimation(fig,
                     animate,
                     frames = 50,
                     interval = interval)

ax.set_axis_off()

plt.show()



