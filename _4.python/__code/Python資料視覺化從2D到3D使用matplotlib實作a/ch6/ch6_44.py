# ch6_44.py
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.facecolor"] = "lightyellow"

fig = plt.figure()
gs = fig.add_gridspec(3, 3)         # 建立 3 x 3 子圖
x = np.arange(1,11) 
gs_ax1 = fig.add_subplot(gs[0,:])   # 使用切片觀念
gs_ax1.plot(x, x)
gs_ax1.set_title('gs[0,:]')
gs_ax2 = fig.add_subplot(gs[1,:-1]) # 使用切片觀念
gs_ax2.plot(x, x)
gs_ax2.set_title('gs[1,:-1]')
gs_ax3 = fig.add_subplot(gs[1:,-1]) # 使用切片觀念
gs_ax3.plot(x, x)
gs_ax3.set_title('gs[1:,-1]')
gs_ax4 = fig.add_subplot(gs[-1,0])  # 使用切片觀念
gs_ax4.plot(x, x)
gs_ax4.set_title('gs[-1,0]')
gs_ax5 = fig.add_subplot(gs[-1,-2]) # 使用切片觀念
gs_ax5.plot(x, x)
gs_ax5.set_title('gs[-1,-2]')

plt.tight_layout()                  # 緊湊佈局
plt.show()


