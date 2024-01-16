# 新進測試06

import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

th = np.arange(0,360,10)
#print(th)

x = np.cos(np.radians(th))
y = np.sin(np.radians(th))

plt.plot(x,y)


plt.show()

print("求arctan 3.4的角度")
rad = np.arctan(3.4)
print(rad)
th = np.degrees(rad)
print(th)

print("------------------------------------------------------------")  # 60個

# 時序圖
import pandas as pd
import matplotlib.dates as mdates

x = ['20170808210000' ,'20170808210100' ,'20170808210200' ,'20170808210300'
     ,'20170808210400' ,'20170808210500' ,'20170808210600' ,'20170808210700'
     ,'20170808210800' ,'20170808210900']

x = pd.to_datetime(x)
y = [3900.0,  3903.0,  3891.0,  3888.0,  3893.0,
     3899.0,  3906.0,  3914.0,  3911.0,  3912.0]

plt.plot(x, y)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M')) # 設置時間顯示格式
plt.gcf().autofmt_xdate() # 自動旋轉角度，以避免重疊
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

#派圖
data = {'apples': 10, 'oranges': 15, 'lemons': 5, 'limes': 20}
explode = (0, 0.1, 0, 0)  # 向外擴展顯示的區域
plt.pie(data.values(), explode=explode, labels=data.keys(), autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal') # 設置餅圖爲正圓形
plt.show()



print("------------------------------------------------------------")  # 60個


# 箱線圖

data = np.random.rand(20, 5) # 生成5個維度數據，每組20個
plt.boxplot(data)

plt.show()

print("------------------------------------------------------------")  # 60個

# 小提琴圖
data = np.random.rand(20, 5)
plt.violinplot(data,showmeans=False,showmedians=True)

plt.show()

print("------------------------------------------------------------")  # 60個

#fail

# 三維散點圖
from mpl_toolkits.mplot3d import Axes3D

data = np.random.rand(50, 3) # 生成三維數據，每維50個
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(data[:, 0], data[:, 1], data[:, 2])
ax.set_zlabel('Z')
ax.set_ylabel('Y')
ax.set_xlabel('X')
plt.show()

print("------------------------------------------------------------")  # 60個

#fail

# 三維柱圖

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y) # 生成網格點座標矩陣
x, y = _xx.ravel(), _yy.ravel() # 展開爲一維數組

top = x + y
bottom = np.zeros_like(top) # 與top數組形狀一樣，內容全部爲0
width = depth = 1

ax.bar3d(x, y, bottom, width, depth, top, shade=True)
plt.show()



print("------------------------------------------------------------")  # 60個

#fail

# 三維曲面圖和等高線圖

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)
ax.contourf(X,Y,Z,zdir='z',offset=-2) # 把等高線向z軸投射
ax.set_zlim(-2,2) # 設置z軸範圍
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

print("------------------------------------------------------------")  # 60個

# 繪圖區域

fig = plt.figure(figsize = (8,6))  # 8x6英寸
fig.suptitle("Title 1") # 主標題
ax1 = plt.subplot(221) # 整體爲兩行兩列，創建其中的第一個子圖
ax1.set_title('Title 2',fontsize=12,color='y')  # 子標題
ax1.plot([1,2,3,4,5])
ax2 = plt.subplot(222)
ax2.plot([5,4,3,2,1])
ax3 = plt.subplot(223)
ax3.plot([1,2,3,3,3])
ax4 = plt.subplot(224)
ax4.plot([5,4,3,3,3])

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure(figsize = (9,6))
ax1 = plt.subplot2grid((3,3), (0,0), colspan = 2)
ax2 = plt.subplot2grid((3,3), (0,2), rowspan = 2) 
ax3 = plt.subplot2grid((3,3), (1,0), rowspan = 2) 
ax4 = plt.subplot2grid((3,3), (1,1)) # rowspan/colspan默認爲1 
ax5 = plt.subplot2grid((3,3), (2,1), colspan = 2) 
ax5.plot([1,2,3,4,1])

plt.show()

print("------------------------------------------------------------")  # 60個

#文字顯示問題

from os import path
from matplotlib.font_manager import fontManager

"""
print('顯示所有字型')
for i in fontManager.ttflist:
    print(i.fname, i.name)
"""

print("------------------------------------------------------------")  # 60個

print("從windows字型中找出可以顯示的中文字型")
import matplotlib as mpl
zhfont = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/mingliu.ttc')
plt.text(0, 0, u'測試一下 ', fontsize=20, fontproperties=zhfont)

plt.show()

print("------------------------------------------------------------")  # 60個

plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
plt.rcParams['axes.unicode_minus'] = False

plt.text(0.5, 0.5, u'測試一下')

plt.show()

print("------------------------------------------------------------")  # 60個

# 導出圖表

import pandas as pd
import matplotlib.pyplot as plt
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

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

