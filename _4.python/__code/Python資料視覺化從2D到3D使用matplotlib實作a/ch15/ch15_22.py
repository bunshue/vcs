# ch15_22.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]  
fig, ax = plt.subplots(figsize=(6,3),subplot_kw=dict(aspect="equal"))
recipe = ["100 毫升純水",                   # 原料成分
          "90 公克黑糖",
          "120 毫升仙草",
          "100 毫升牛奶",
          "50 黑珍珠"]
data = [100, 90, 120, 100, 50]              # 原料份量
wedges, texts = ax.pie(data,wedgeprops=dict(width=0.5),startangle=15)
# 箭頭格式
kw = dict(arrowprops=dict(arrowstyle="->",color='b'),
          bbox=dict(boxstyle='square',
                    ec='w',
                    fc='yellow'),
          va="center")
# 建立箭頭和註解文字
for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1   # 箭頭指向角度
    x = np.cos(np.deg2rad(ang))                 # 箭頭 x 位置
    y = np.sin(np.deg2rad(ang))                 # 箭頭 y 位置
    horizontalalignment = {-1:"right",1:"left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(recipe[i],xy=(x,y),xytext=(1.35*np.sign(x),1.4*y),                               
                horizontalalignment=horizontalalignment,**kw)
ax.set_title("製作燒仙草環圈圖")
plt.show()


