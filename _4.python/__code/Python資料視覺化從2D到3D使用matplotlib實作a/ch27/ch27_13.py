# ch27_13.py
import matplotlib.pyplot as plt
import matplotlib.patches as patch
  
fig = plt.figure()
ax = fig.subplots()
# 繪製橢圓
xy = (2, 1.5)                       # 定義 xy
arc0 = patch.Arc(xy,2,1)            # 使用 Arc 繪製橢圓
# 繪製圓弧
arc1 = patch.Arc(xy,3,1.5,          # xy, width, height
                 theta1=0,          # 圓弧起始角度
                 theta2=120,        # 圓弧結束角度
                 ec='g',            # 綠色線
                 lw=10)             # 線寬是 10
arc2 = patch.Arc(xy,3,1.5,          # xy, width, height
                 theta1=120,        # 圓弧起始角度
                 theta2=180,        # 圓弧結束角度
                 ec='r',            # 紅色線
                 linestyle = '--',  # 虛線
                 lw=5)              # 線寬是 5
arc3 = patch.Arc(xy,3,1.5,          # xy, width, height
                 theta1=180,        # 圓弧起始角度
                 theta2=300,        # 圓弧結束角度
                 color='b',         # 藍色線
                 lw=10)             # 線寬是 10
arc4 = patch.Arc(xy,3,1.5,          # xy, width, height
                 theta1=300,        # 圓弧起始角度
                 theta2=360,        # 圓弧結束角度
                 ec='m',            # 品紅色
                 linestyle = '-.',  # 虛點線
                 lw=5)              # 線寬是 5
for arc in (arc0, arc1, arc2, arc3, arc4):
    ax.add_patch(arc)
ax.axis([0,4,0,3])  
ax.set_aspect(1)                    # 1與'equal'效果相同  
plt.show()





