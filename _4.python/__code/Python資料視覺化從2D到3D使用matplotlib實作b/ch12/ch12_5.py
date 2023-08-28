# ch12_5.py
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

top = mpl.cm.get_cmap('OrRd_r', 128)        # OrRd_r色彩反轉
bottom = mpl.cm.get_cmap('Blues', 128)      # Blues色彩
# 組合OrRd_r和Blues色彩
newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))
OrRdBlue = mpl.colors.ListedColormap(newcolors)

np.random.seed(10)
plt.subplot(211)                            # 上方子圖
data1 = np.random.random((80, 80))
plt.imshow(data1, cmap=OrRdBlue)

plt.subplot(212)                            # 下方子圖
data2 = np.random.random((80, 80))
plt.imshow(data2, cmap=OrRdBlue)
plt.subplots_adjust(left=0.2, right=0.6, bottom=0.1, top=0.9)
# 建立子圖表axes物件
ax = plt.axes([0.7, 0.1, 0.05, 0.8])        # 設定色彩條大小和位置
plt.colorbar(mpl.cm.ScalarMappable(cmap=OrRdBlue),cax=ax)
plt.show()


