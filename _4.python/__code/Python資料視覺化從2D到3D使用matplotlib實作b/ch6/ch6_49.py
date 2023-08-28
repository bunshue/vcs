# ch6_49.py
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["figure.facecolor"] = "lightyellow"
fig = plt.figure()
x = np.arange(1,11)
plt.plot(x, x)
plt.title('外圖表')
#新增子區域位置和大小
left, bottom, width, height = 0.2, 0.6, 0.2, 0.2
# 設定子座標物件
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(x,x, 'g')
ax2.set_title('內圖表')
plt.show() 



