# ch27_7.py
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np

angle = 30                              # 炫轉角度
angles = np.arange(0, 180, angle)       # 建立角度陣列
# 建立軸單位長度相同的 axes 軸物件
fig, axes = plt.subplots(subplot_kw={'aspect': 'equal'})
center = (0,0)                          # 橢圓中心
width = 4                               # 橢圓水平軸直徑
height = 2                              # 橢圓垂直軸直徑
for angle in angles:                    # 繪製系列橢圓
    ellip = Ellipse(center,width,height,angle,
                    facecolor='g',alpha=0.2)
    axes.add_artist(ellip)              # 加入ellip物件
axes.set_xlim(-2.2, 2.2)
axes.set_ylim(-2.2, 2.2)
plt.show()







