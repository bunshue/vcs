import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"] 
np.random.seed(20)                                       # 固定隨機數
x = np.random.rand(10)
y = np.random.rand(10)
colors = np.array(['b','c','g','k','m','r','y','pink','purple','orange'])
# 建立 2 x 3 的子圖
fig, axs = plt.subplots(nrows=2, ncols=3, sharex=True, sharey=True)
# 建立 aplha 標記
axs[0,0].scatter(x, y, s=100, c=colors, marker=r'$\alpha$')
axs[0,0].set_title(r'${alpha=}\alpha$'+'標記',c='b')
axs[0,0].axis('square')                                   # 建立矩形子圖
# 建立 beta 標記
axs[0,1].scatter(x, y, s=100, c=colors, marker=r'$\beta$')
axs[0,1].set_title(r'${beta=}\beta$'+'標記',c='b')
axs[0,1].axis('square')                                   # 建立矩形子圖
# 建立 gamma 標記
axs[0,2].scatter(x, y, s=100, c=colors, marker=r'$\gamma$')
axs[0,2].set_title(r'${gamma=}\gamma$'+'標記',c='b')
axs[0,2].axis('square')                                   # 建立矩形子圖
# 建立 clubsuit 標記
axs[1,0].scatter(x, y, s=100, c=colors, marker=r'$\clubsuit$')
axs[1,0].set_title(r'${clubsuit=}\clubsuit$'+'標記',c='b')
axs[1,0].axis('square')                                   # 建立矩形子圖
# 建立 spadesuit 標記
axs[1,1].scatter(x, y, s=100, c=colors, marker=r'$\spadesuit$')
axs[1,1].set_title(r'${spadesuit=}\spadesuit$'+'標記',c='b')
axs[1,1].axis('square')                                   # 建立矩形子圖
# 建立 heartsuit 標記
axs[1,2].scatter(x, y, s=100, c=colors, marker=r'$\heartsuit$')
axs[1,2].set_title(r'${heartsuit=}\heartsuit$'+'標記',c='b')
axs[1,2].axis('square')                                   # 建立矩形子圖
plt.tight_layout()

plt.show()



