# ch9_14.py
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)                          # 固定隨機數
N = 50                                      # 散點的數量
r = 0.5                                     # 邊界線boundary半徑
x = np.random.rand(N)                       # 隨機的 x 座標點
y = np.random.rand(N)                       # 隨機的 y 座標點
area = np.random.randint(20,100,N)          # 散點大小
colorused = ['b','c','g','k','m','r','y']   # 定義顏色
colors = []
for i in range(N):                          # 隨機設定 N 個顏色
    colors.append(np.random.choice(colorused))

r1 = np.sqrt(x ** 2 + y ** 2)               # 計算距離
area1 = np.ma.masked_where(r1 < r, area)    # 邊界線 0.5 內區域遮罩
area2 = np.ma.masked_where(r1 >= r, area)   # 邊界線 0.5 (含)外區域遮罩
# 大於或等於 0.5 繪製星形, 小於 0.5 繪製圓形
plt.scatter(x, y, s=area1, marker='*', c=colors)
plt.scatter(x, y, s=area2, marker='o', c=colors)
# 計算 0.5Pi 之弧度, 依據弧度產生的座標點繪製邊界線
radian = np.arange(0, np.pi / 2, 0.01)
plt.plot(r * np.cos(radian), r * np.sin(radian))    # 繪製邊界線
plt.xticks(np.arange(0,1.1,step=0.1))
plt.yticks(np.arange(0,1.1,step=0.1))
plt.show()



