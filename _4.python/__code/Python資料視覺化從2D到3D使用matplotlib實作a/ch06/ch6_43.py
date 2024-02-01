# ch6_43.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
fig = plt.figure()
gs = fig.add_gridspec(2,2)          # 建立 2 x 2 網格

x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
gs_ax1 = fig.add_subplot(gs[0,0])   # 用網格物件索引0,0指定子圖
gs_ax1.plot(x, y,'b')               
gs_ax1.set_title('子圖[0, 0]')
gs_ax2 = fig.add_subplot(gs[0,1])   # 用網格物件索引0,1指定子圖
gs_ax2.plot(x, y,'g')               
gs_ax2.set_title('子圖[0, 1]')
gs_ax3 = fig.add_subplot(gs[1,0])   # 用網格物件索引1,0指定子圖
gs_ax3.plot(x, y,'m')               
gs_ax3.set_title('子圖[1, 0]')
gs_ax4 = fig.add_subplot(gs[1,1])   # 用網格物件索引1,1指定子圖
gs_ax4.plot(x, y,'r')               
gs_ax4.set_title('子圖[1, 1]')

plt.tight_layout()                  # 緊縮佈局
plt.show()



