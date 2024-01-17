# ch20_50.py
import matplotlib.pyplot as plt
import numpy as np

z = np.linspace(0,1,300)        # z 軸值
x = z * np.sin(30*z)            # x 軸值
y = z * np.cos(30*z)            # y 軸值
colors = x + y                  # 色彩是沿 x + y 累增

# 建立 2 個子圖
fig,ax = plt.subplots(1,2,figsize=(8,4),subplot_kw={'projection':'3d'})
ax[0].scatter(x, y, z, c = colors)                  # 繪製左子圖
ax[1].scatter(x, y, z, c = colors, cmap='hsv')      # 繪製右子圖
ax[1].set_axis_off()            # 關閉軸
plt.show()



      
