# ch26_3.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.arange(-3, 3) 
y = np.arange(-3, 3) 
X, Y = np.meshgrid(x, y)                    # 建立 X, Y
U = -1 + X**2 - Y                           # 定義速度 U
V = 1 - X + Y**2                            # 定義速度 V
speed = np.sqrt(U**2 + V**2)
# 建立圖表網格物件
fig = plt.figure()
gs = gridspec.GridSpec(nrows=2, ncols=2)
# 使用預設環境建立流線圖
ax0 = fig.add_subplot(gs[0, 0])
ax0.streamplot(X, Y, U, V)
ax0.set_title('使用預設環境建立流線圖')
# 流線圖 1, 使用 cmap='spring' 色彩映射
ax1 = fig.add_subplot(gs[0, 1])
strobj = ax1.streamplot(X,Y,U,V,color=U,linewidth=2,cmap='spring')
fig.colorbar(strobj.lines)                  # 建立資料條
ax1.set_title("使用 cmap='spring' 色彩映射")
# 流線圖 2, x 和 y 軸密度不同, 使用黑色流線
ax2 = fig.add_subplot(gs[1, 0])
ax2.streamplot(X, Y, U, V, color='k', density=[0.5, 1])
ax2.set_title('使用黑色流線, x 和 y 軸密度不同')
# 流線圖 3, 沿著速度線變更線條寬度, 同時更改密度為 0.6
ax3 = fig.add_subplot(gs[1, 1])
lw = 5*speed / speed.max()
strobj = ax3.streamplot(X,Y,U,V,density=0.6,color=U,
                        cmap='summer',linewidth=lw)
fig.colorbar(strobj.lines)                  # 建立資料條
ax3.set_title('沿著速度線變更線條寬度')
plt.tight_layout()
plt.show()




