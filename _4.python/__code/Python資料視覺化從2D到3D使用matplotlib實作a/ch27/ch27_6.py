# ch27_6.py
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

# 建立軸單位長度相同的 axes 軸物件
figure, axes = plt.subplots(subplot_kw={'aspect':'equal'})     
center = (0,0)                      # 橢圓中心
width = 4                           # 橢圓水平軸直徑
height = 2                          # 橢圓垂直軸直徑
ellip = Ellipse(xy=center,
                width=width,
                height=height)      # 繪製橢圓
axes.add_artist(ellip)              # 將物件加入軸物件
axes.set_xlim(-3,3)
axes.set_ylim(-2,2)
plt.show()





