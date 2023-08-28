# ch27_8.py
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np

np.random.seed(10)                          # 隨機數種子
num = 100                                   # 建立 100 個橢圓
ells = [Ellipse(xy=np.random.rand(2) * 10,  # 隨機數產生橢圓中心xy
                width=np.random.rand(),     # 隨機數產生水平軸直徑
                height=np.random.rand(),    # 隨機數產生垂直軸直徑
                angle=np.random.rand()*360) # 隨機數產生炫轉角度
                for i in range(num)]        # 執行 num 次

fig, axes = plt.subplots(subplot_kw={'aspect':'equal'})
# 將橢圓物件加入軸物件, 同時格式化所有橢圓物件
for e in ells:                              
    axes.add_artist(e)                      # 將橢圓物件加入軸物件
    e.set_clip_box(axes.bbox)               # 擷取橢圓
    e.set_alpha(np.random.rand())           # 隨機數產生透明度
    e.set_facecolor(np.random.rand(3))      # 建立隨機數顏色   
# 設定顯示空間
axes.set_xlim(0, 10)
axes.set_ylim(0, 10)
plt.show()






