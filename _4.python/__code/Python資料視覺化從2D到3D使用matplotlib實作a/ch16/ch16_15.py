# ch16_15.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
np.random.seed(10)
# 建立 3 組數據
data = [np.random.randn(1000) for x in range(1,4)]
labels = ['x1','x2','x3']
# 建立子圖
fig, ax = plt.subplots(nrows=1,ncols=2,figsize=(9,5))
# 建立正常的箱形圖盒子
box1 = ax[0].boxplot(data,
                     patch_artist=True, # 含顏色
                     labels=labels)     # x 軸標記
ax[0].set_title('預設箱線圖盒子')
# 建立缺口箱線圖盒子
box2 = ax[1].boxplot(data,
                     notch=True,        # 缺口
                     patch_artist=True, # 含顏色
                     labels=labels)     # x 軸標記
ax[1].set_title('缺口箱線圖盒子')
# 箱線盒填上顏色
colors = ['lightgreen', 'yellow', 'aqua']
for box in (box1,box2):
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)
# 建立水平軸線
for ax in [ax[0], ax[1]]:
    ax.yaxis.grid(True)
    ax.set_xlabel('3 組數據')
    ax.set_ylabel('觀察值')
plt.show() 


      
