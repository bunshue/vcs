# ch12_7.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
N = 5
np.random.seed(10)                  # 設定種子顏色值
src = np.random.random((N,N,3))     # 隨機產生影像圖陣列資料
plt.figure()

plt.subplot(141)
plt.xticks(range(N))    # 繪製 x 軸刻度
plt.yticks(range(N))    # 繪製 y 軸刻度
plt.title('RGB色彩')
plt.imshow(src)

plt.subplot(142)
r = src.copy()          # 複製影像色彩陣列
r[:,:,[1,2]] = 0        # 保留紅色元素, 設定綠色和藍色元素是 0
plt.xticks(range(N))    # 繪製 x 軸刻度
plt.yticks([])          # 隱藏繪製 y 軸刻度
plt.title('Red元素')
plt.imshow(r)

plt.subplot(143)
g = src.copy()          # 複製影像色彩陣列
g[:,:,[0,2]] = 0        # 保留綠色元素, 設定紅色和藍色元素是 0
plt.xticks(range(N))    # 繪製 x 軸刻度
plt.yticks([])          # 隱藏繪製 y 軸刻度
plt.title('Green元素')
plt.imshow(g)

plt.subplot(144)
b = src.copy()          # 複製影像色彩陣列
b[:,:,[0,1]] = 0        # 保留藍色元素, 設定紅色和綠色元素是 0
plt.xticks(range(N))    # 繪製 x 軸刻度
plt.yticks([])          # 隱藏繪製 y 軸刻度
plt.title('Blue元素')
plt.imshow(b)
plt.show()


