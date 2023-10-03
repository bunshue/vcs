import matplotlib.pyplot as plt
import numpy as np

N = 1000                        # 數據數量
np.random.seed(10)              # 設定隨機數種子值
x = np.random.normal(0, 1, N)   # 均值是 0, 標準差是 1
y = np.random.normal(0, 1, N)   # 均值是 0, 標準差是 1
color = x + y                   # 設定顏色串列是 x + y 數列結果
norm = plt.Normalize(vmin=-3, vmax=3)
plt.scatter(x,y,s=60,alpha=0.5,c=color,cmap='jet',norm=norm)
plt.xlim(-3, 3)
plt.xticks(())                  # 不顯示 x 刻度
plt.ylim(-3, 3)
plt.yticks(())                  # 不顯示 y 刻度
plt.colorbar()                  # 建立色彩條

plt.show()

