# matplotlib_新進測試14_其他

import os
import time
import random
import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("matplotlib 01 ------------------------------------------------------------")  # 60個

x = np.linspace(0.0, np.pi, 500)
y = np.cos(2 * np.pi * x)
plt.plot(x, y, "m", lw=2)
plt.annotate(
    "局部極大值",
    xy=(2, 1),
    xytext=(2.5, 1.2),
    arrowprops=dict(arrowstyle="->", facecolor="black"),
)
plt.annotate(
    "局部極小值", xy=(1.5, -1), xytext=(2.0, -1.25), arrowprops=dict(arrowstyle="-")
)
plt.text(0.8, 1.2, "Annotate的應用", fontsize=20, color="b")
plt.ylim(-1.5, 1.5)

plt.show()

print("matplotlib 02 ------------------------------------------------------------")  # 60個

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False 
x = np.linspace(0.0, np.pi, 500)
y = np.cos(2 * np.pi * x)
plt.plot(x, y, 'm', lw=2)
plt.annotate('局部極大值',
            xy=(2, 1),
            xytext=(2.5, 1.2),           
            arrowprops=dict(facecolor='black',shrink=0.05)) 
plt.ylim(-1.5, 1.5)

plt.show()

print("matplotlib 03 ------------------------------------------------------------")  # 60個

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False 
x = np.linspace(0.0, np.pi, 500)
y = np.cos(2 * np.pi * x)
plt.plot(x, y, 'm', lw=2)
plt.annotate('局部極大值',
            xy=(2, 1),
            xytext=(2.5, 1.2),           
            arrowprops=dict(facecolor='y',shrink=0.05)) 
plt.ylim(-1.5, 1.5)

plt.show()

print("matplotlib 04 ------------------------------------------------------------")  # 60個

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False 
x = np.linspace(0.0, np.pi, 500)
y = np.cos(2 * np.pi * x)
plt.plot(x, y, 'm', lw=2)
plt.annotate('局部極大值',
            xy=(2, 1),
            xytext=(2.5, 1.2),           
            arrowprops=dict(shrink=0.05)) 
plt.ylim(-1.5, 1.5)

plt.show()

print("matplotlib 05 ------------------------------------------------------------")  # 60個

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False 
x = np.linspace(0.0, np.pi, 500)
y = np.cos(2 * np.pi * x)
plt.plot(x, y, 'm', lw=2)
plt.annotate('局部極大值',
            xy=(2, 1),
            xytext=(2.5, 1.2),           
            arrowprops = dict(ec = 'g', fc = 'g', shrink = 0.05)) 
            #arrowprops = dict(color = 'g', shrink = 0.05))
plt.ylim(-1.5, 1.5)
plt.show()

print("matplotlib 06 ------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(figsize=(4,4))
ax.annotate("Annotate",
            xy = (0.2, 0.2),
            xytext = (0.7, 0.8),
            arrowprops = dict(arrowstyle="->",
                              connectionstyle="arc"),
            )
plt.show()

print("matplotlib 07 ------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(figsize=(4,4))
ax.annotate("Annotate",
            xy = (0.2, 0.2),
            xytext = (0.7, 0.8),
            arrowprops = dict(arrowstyle="->",
                              connectionstyle="angle"),
            )
plt.show()

print("matplotlib 08 ------------------------------------------------------------")  # 60個

def demo(ax, connectionstyle):
    # 繪製子圖與箭頭樣式說明
    x1, y1 = 0.3, 0.2
    x2, y2 = 0.8, 0.6
    ax.plot([x1, x2], [y1, y2], "g.")
    ax.annotate("",
                xy=(x1, y1),
                xytext=(x2, y2),
                arrowprops=dict(arrowstyle="->", color="m",
                                shrinkA=5,
                                shrinkB=5,
                                connectionstyle=connectionstyle,
                                ),
                )
    ax.text(0.1, 0.96, connectionstyle.replace(",", ",\n"),
            transform=ax.transAxes, ha="left", va="top", c='b')
# 主程式開始
fig, axs = plt.subplots(3, 5, figsize=(7, 6.2))
demo(axs[0, 0], "angle3,angleA=90,angleB=0")
demo(axs[1, 0], "angle3,angleA=0,angleB=90")
demo(axs[0, 1], "angle,angleA=-90,angleB=180,rad=0")
demo(axs[1, 1], "angle,angleA=-90,angleB=180,rad=5")
demo(axs[2, 1], "angle,angleA=-90,angleB=10,rad=5")
demo(axs[0, 2], "arc3,rad=0.")
demo(axs[1, 2], "arc3,rad=0.3")
demo(axs[2, 2], "arc3,rad=-0.3")
demo(axs[0, 3], "arc,angleA=-90,angleB=0,armA=30,armB=30,rad=0")
demo(axs[1, 3], "arc,angleA=-90,angleB=0,armA=30,armB=30,rad=5")
demo(axs[2, 3], "arc,angleA=-90,angleB=0,armA=0,armB=40,rad=0")
demo(axs[0, 4], "bar,fraction=0.3")
demo(axs[1, 4], "bar,fraction=-0.3")
demo(axs[2, 4], "bar,angle=180,fraction=-0.3")
# 取消刻度標記與標籤
for ax in axs.flat:
    ax.set(xlim=(0, 1), ylim=(0, 1.25), xticks=[], yticks=[])
plt.tight_layout()          # 緊縮佈局

plt.show()

print("matplotlib 09 ------------------------------------------------------------")  # 60個

plt.subplots(figsize=(4,4))
plt.annotate("Simple",
             xy=(0.2, 0.2),
             xytext=(0.7, 0.8),
             size=20, va="center", ha="center",
             color='b',
             arrowprops=dict(arrowstyle="simple",
                             color='g',
                             connectionstyle="arc3,rad=-0.3"),
             )
plt.show()

print("matplotlib 10 ------------------------------------------------------------")  # 60個

plt.subplots(figsize=(4,4))
plt.annotate("fancy",
             xy=(0.2, 0.2),
             xytext=(0.7, 0.8),
             size=20, va="center", ha="center",
             color='b',
             bbox=dict(boxstyle="round4",fc="lightyellow"),
             arrowprops=dict(arrowstyle="fancy",
                             color='g',
                             connectionstyle="arc3,rad=-0.3"),
             )
plt.show()

print("matplotlib 11 ------------------------------------------------------------")  # 60個

plt.subplots(figsize=(4,4))
plt.annotate("wedge",
             xy=(0.2, 0.2),
             xytext=(0.7, 0.8),
             size=20, va="center", ha="center",
             color='b',
             bbox=dict(boxstyle="round4",fc="lightyellow"),
             arrowprops=dict(arrowstyle="wedge",
                             color='g',
                             connectionstyle="arc3,rad=-0.3"),
             )
plt.annotate("wedge",
             xy=(0.2, 0.2),
             xytext=(0.7, 0.8),
             size=20, va="center", ha="center",
             color='b',
             bbox=dict(boxstyle="round4",fc="lightyellow"),
             arrowprops=dict(arrowstyle="wedge",
                             color='m',
                             connectionstyle="arc3,rad=0.3"),
             )
plt.show()

print("matplotlib 12 ------------------------------------------------------------")  # 60個

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fig = plt.figure()
ax = fig.add_subplot(projection='polar')
r = np.linspace(0, 1, 1000)
theta = 2 * 2*np.pi * r
ax.plot(theta, r, color='g', lw=3)

i = 500
radius, thistheta = r[i], theta[i]
ax.plot([thistheta], [radius], 'o')         # 指定位置繪點
ax.annotate('極座標文字註解',
            xy=(thistheta, radius),         # theta, radius
            xytext=(0.8, 0.2),              # 百分比
            color='b',                      # 藍色
            textcoords='figure fraction',   # 座標格式是百分比
            arrowprops=dict(arrowstyle="->",
                            color='m'),
            horizontalalignment='left',
            verticalalignment='bottom',
            )
plt.show()

print("matplotlib 13 ------------------------------------------------------------")  # 60個

plt.figure(figsize=(18, 4))
plt.subplot(2, 2, 1)
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'subplot(2,2,1)', ha='center', va='center',
        size=20, alpha=.5)

plt.subplot(2, 2, 2)
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'subplot(2,2,2)', ha='center', va='center',
        size=20, alpha=.5)

plt.subplot(2, 2, 3)
plt.xticks(())
plt.yticks(())

plt.text(0.5, 0.5, 'subplot(2,2,3)', ha='center', va='center',
        size=20, alpha=.5)

plt.subplot(2, 2, 4)
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'subplot(2,2,4)', ha='center', va='center',
        size=20, alpha=.5)

plt.tight_layout()
plt.show()

print("matplotlib 14 ------------------------------------------------------------")  # 60個

import matplotlib.gridspec as gridspec

plt.figure(figsize=(18, 4))
G = gridspec.GridSpec(3, 3)

axes_1 = plt.subplot(G[0, :])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 1', ha='center', va='center', size=24, alpha=.5)

axes_2 = plt.subplot(G[1:, 0])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 2', ha='center', va='center', size=24, alpha=.5)

axes_3 = plt.subplot(G[1:, -1])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 3', ha='center', va='center', size=24, alpha=.5)

axes_4 = plt.subplot(G[1, -2])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 4', ha='center', va='center', size=24, alpha=.5)

axes_5 = plt.subplot(G[-1, -2])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 5', ha='center', va='center', size=24, alpha=.5)

plt.tight_layout()
plt.show()

print("matplotlib 15 ------------------------------------------------------------")  # 60個

plt.figure(figsize=(18, 4))

plt.axes([.1, .1, .8, .8])
plt.xticks(())
plt.yticks(())
plt.text(.2, .5, 'axes([0.1, 0.1, .8, .8])', ha='center', va='center',
        size=20, alpha=.5)

plt.axes([.5, .5, .3, .3])
plt.xticks(())
plt.yticks(())
plt.text(.5, .5, 'axes([.5, .5, .3, .3])', ha='center', va='center',
        size=16, alpha=.5)

plt.show()

print("matplotlib 16 ------------------------------------------------------------")  # 60個

# 箱線圖

data = np.random.rand(20, 5) # 生成5個維度數據，每組20個
plt.boxplot(data)

plt.show()

print("matplotlib 17 ------------------------------------------------------------")  # 60個

# 小提琴圖
data = np.random.rand(20, 5)
plt.violinplot(data,showmeans=False,showmedians=True)

plt.show()

print("matplotlib 18 ------------------------------------------------------------")  # 60個

# Matplotlib技巧

import matplotlib

fig = plt.figure(figsize = (6,4), dpi=120) # 設置繪製對象大小
plt.style.use('ggplot') # 設置顯示風格

plt.plot([12,13,45,15,16], label='label1') # 繪圖及設置圖例文字
plt.annotate('local max', xy=(2, 45), xytext=(3, 45),arrowprops=dict(facecolor='black',
    shrink=0.05))  # 繪製帶箭頭的標註
x = np.arange(0, 6)
y = x * x
plt.plot(x, y, marker='o', label='label2') # 繪圖及設置圖例文字
for xy in zip(x, y):
    plt.annotate("(%s,%s)" % xy, xy=xy, xytext=(-20, 10), # 繪製標註
                 textcoords='offset points')
plt.text(4.5, 10, 'Draw text', fontsize=20) # 在位置0,20繪製文字

plt.legend(loc='upper left')  # 在左上角顯示圖例
plt.xlabel("x value")  # 設置x軸上的標籤
plt.ylabel("y value")  # 設置y軸上的標籤
plt.xlim(-0.5,7)  # 設置x軸範圍
plt.ylim(-5,50) # 設置y軸範圍
plt.show()

print(matplotlib.artist.getp(fig.patch))  # 顯示繪製對象的各個屬性值

print("matplotlib 19 箱圖------------------------------------------------------------")  # 60個

# Creating dataset
np.random.seed(10)
data_1 = np.random.normal(100, 10, 200)
data_2 = np.random.normal(90, 20, 200)
data_3 = np.random.normal(80, 30, 200)
data_4 = np.random.normal(70, 40, 200)
data = [data_1, data_2, data_3, data_4]

fig = plt.figure(figsize=(10, 7))

# 圖加軸
ax = fig.add_axes([0, 0, 1, 1])

bp = ax.boxplot(data, labels=["mu = 100", "mu = 90", "mu = 80", "mu = 70"])
ax.set_title("Box plot")

plt.show()

print("matplotlib 20 導出圖表 ------------------------------------------------------------")  # 60個

from io import BytesIO
from lxml import etree
import base64
import webbrowser

data = pd.DataFrame({'id':['1','2','3','4','5'], # 構造數據
                     'math':[90,89,99,78,63],
                     'english':[89,94,80,81,94]})
plt.plot(data['math']) # matplotlib做圖
plt.plot(data['english'])

# 保存圖片（與網頁顯示無關）
plt.savefig('導出圖表.jpg',dpi=300)

# 保存網頁
buffer = BytesIO()
plt.savefig(buffer)  
plot_data = buffer.getvalue()

imb = base64.b64encode(plot_data)  # 生成網頁內容
ims = imb.decode()
imd = "data:image/png;base64,"+ims
data_im = """<h1>Figure</h1>  """ + """<img src="%s">""" % imd   
data_des = """<h1>Describe</h1>"""+data.describe().T.to_html()
root = "<title>Dataset</title>"
root = root + data_des + data_im

html = etree.HTML(root)
tree = etree.ElementTree(html)
tree.write('導出圖表.html')
#使用默認瀏覽器打開 html 文件
webbrowser.open('導出圖表.html',new = 1)

print("matplotlib 21 ------------------------------------------------------------")  # 60個



print("matplotlib 22 ------------------------------------------------------------")  # 60個


print("matplotlib 23 ------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



'''

#文字顯示問題

from os import path
from matplotlib.font_manager import fontManager

"""
print('顯示所有字型')
for i in fontManager.ttflist:
    print(i.fname, i.name)
"""

print("matplotlib 14 ------------------------------------------------------------")  # 60個



'''

