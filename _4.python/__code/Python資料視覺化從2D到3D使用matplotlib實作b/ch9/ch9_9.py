# ch9_9.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"] 
np.random.seed(5)                                       # 固定隨機數
x = np.random.rand(10)
y = np.random.rand(10)
colors = np.array(['b','c','g','k','m','r','y','pink','purple','orange'])
# 建立 1 x 3 的子圖
fig, axs = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True)
# 建立多邊形標記
axs[0].scatter(x, y, s=75, c=colors, marker=(5, 0))
axs[0].set_title("多邊形marker=(5, 0)")
axs[0].axis('square')                                   # 建立矩形子圖
# 建立星形標記
axs[1].scatter(x, y, s=75, c=colors, marker=(5, 1))
axs[1].set_title("星狀形marker=(5, 1)")
axs[1].axis('square')                                   # 建立矩形子圖
# 建立鑽石標記
axs[2].scatter(x, y, s=75, c=colors, marker=(5, 2))
axs[2].set_title("鑽石形marker=(5, 2)")
axs[2].axis('square')                                   # 建立矩形子圖
plt.tight_layout()
plt.show()



