# ch20_49_1.py
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
# 取得測試資料
X, Y, Z = axes3d.get_test_data(0.05)
# 建立 2 個子圖
fig,ax = plt.subplots(1,2,figsize=(8,4),subplot_kw={'projection':'3d'})
# 繪製曲線表面圖
ax[0].plot_surface(X, Y, Z, cmap="bwr")
ax[0].set_title('繪製曲線表面圖',fontsize=16,color='b')

# 繪製曲線框面圖
#ax = fig.add_subplot(111, projection='3d')
ax[1].plot_wireframe(X, Y, Z, color='g')
ax[1].set_title('繪製曲線框線圖',fontsize=16,color='b')
plt.show()



      
