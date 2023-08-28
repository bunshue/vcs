# ch12_6.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
N = 5
data = np.reshape(np.linspace(0,1,N**2), (N,N)) # 建立 N x N 陣列
plt.figure()
# 使用預設顏色繪製
plt.subplot(131)
plt.imshow(data)
plt.xticks(range(N))                            # 繪製 x 軸刻度
plt.yticks(range(N))                            # 繪製 y 軸刻度
plt.title('使用預設插值',fontsize=12,color='b')
# 相同陣列使用不同的插值法
plt.subplot(132)
plt.imshow(data,interpolation='bicubic')
plt.xticks(range(N))                            # 繪製 x 軸刻度
plt.yticks([])                                  # 隱藏繪製 y 軸刻度
plt.title('使用 bicubic 插值',fontsize=12,color='b')
plt.subplot(133)
plt.imshow(data,interpolation='hamming')
plt.xticks(range(N))                            # 繪製 x 軸刻度
plt.yticks([])                                  # 隱藏繪製 y 軸刻度
plt.title('使用 hamming 插值',fontsize=12,color='b')
plt.show()


