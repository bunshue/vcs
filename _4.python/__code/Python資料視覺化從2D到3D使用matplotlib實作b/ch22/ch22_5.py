# ch22_5.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(10)
# 建立 1 組隨機數
data = np.random.normal(size=1000)     
fig, ax = plt.subplots(nrows=2, ncols=4)
# 建立小提琴圖
ax[0,0].violinplot(data)
ax[0,0].set_title('預設小提琴圖',color='m')
ax[0,1].violinplot(data, widths=[0.2])
ax[0,1].set_title('重新定義寬度',color='m')
ax[0,2].violinplot(data, vert=False)
ax[0,2].set_title('水平小提琴圖',color='m')
ax[0,3].violinplot(data, positions=[3])
ax[0,3].set_title('重新定義位置',color='m')
ax[1,0].violinplot(data,showextrema=False)
ax[1,0].set_title('隱藏極值',color='m')
ax[1,1].violinplot(data,showmeans=True)
ax[1,1].set_title('顯示均值',color='m')
ax[1,2].violinplot(data,showmedians=True)
ax[1,2].set_title('顯示中位數',color='m')
ax[1,3].violinplot(data,quantiles=[0.25,0.5,0.75])
ax[1,3].set_title('顯示分位數',color='m')
plt.suptitle('8 組均勻分布的小提琴圖',fontsize=16,color='b')
plt.tight_layout()
plt.show()


      
