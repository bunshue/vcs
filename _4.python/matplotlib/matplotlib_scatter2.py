# scatter 集合
# 散布圖 Scatter Chart

import sys
import numpy as np
import matplotlib.pyplot as plt
import random
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

'''
"""
額外設定 s、c 和 cmap，就能根據資料點的數據，對應出指定的顏色，
假設資料的範圍是 0～100，顏色地圖是紅橙黃綠藍，
則 0～20 對應紅色，21～40 對應橙色，
41～60 對應黃色，61～80 對應綠色，81～100 對應藍色。
"""

x = range(1, 11) # 1 2 3 ... 10
y = range(1, 11) # 1 2 3 ... 10
X, Y = np.meshgrid(x, y)
size = [i * 80 for i in Y]         # 放大資料點數據 N 倍，比較容易觀察尺寸
plt.scatter(X, Y, s = size, c = size, cmap = 'Set1')  # 使用 Set1 的 colormap
plt.colorbar()
plt.show()

print('------------------------------------------------------------')	#60個

#加上 vmin 和 vmax 的設定，能設定顏色的最大值與最小值
#當數值小於 vmin 時，只會顯示紅色，當數值大於 vmax 時，只會顯示灰色。

x = range(1, 11) # 1 2 3 ... 10
y = range(1, 11) # 1 2 3 ... 10
X, Y = np.meshgrid(x, y)
size = [i * 80 for i in Y]         # 放大資料點數據 N 倍，比較容易觀察尺寸
plt.scatter(X, Y, s = size, c = size, cmap = 'Set1', vmin = 200, vmax = 650)
plt.colorbar()
plt.show()

print('------------------------------------------------------------')	#60個


xpt = np.linspace(0, 5, 50)   # 建立含50個元素的陣列
ypt = xpt                     # y陣列的變化
plt.scatter(xpt, ypt, s=50, c=ypt, cmap='hsv')          # 色彩隨y軸值變化
plt.show()

print('------------------------------------------------------------')	#60個

listx = [31,15,20,25,12,18,45,21,33,5,18,22,37,42,10]
listy = [68,20,61,32,45,56,10,18,70,64,43,66,19,77,21]
scale = [x ** 3 for x in [5,4,2,6,7,1,8,9,2,3,2,4,5,7,2]]

plt.xlim(0, 50)
plt.ylim(0, 80)
plt.scatter(listx, listy, c = 'r', s = scale, marker = 'o', alpha = 0.5)

plt.show()

print('------------------------------------------------------------')	#60個

# Generate 100 random data points along 3 dimensions
x, y, scale = np.random.randn(3, 100)

# Map each onto a scatterplot we'll create with Matplotlib
plt.scatter(x=x, y=y, c=scale, s=np.abs(scale)*500)

plt.show()

print('------------------------------------------------------------')	#60個

x = np.linspace(0, 5, 50)                # 含50個元素的陣列
y = x                   # y陣列的變化
plt.scatter(x,y,s=50,c=y,cmap='rainbow')  # 色彩隨 y 軸值變化
plt.colorbar()                            # 色彩條

plt.show()

print('------------------------------------------------------------')	#60個

x = np.arange(50)
y = np.arange(50)
plt.scatter(x, y, c = y, cmap = 'rainbow')

plt.show()
'''
print('------------------------------------------------------------')	#60個
#常態分佈
X = np.random.randn(600)
Y = np.random.randn(600)

plt.scatter(X, Y, c='r', s=100)
plt.show()

print('------------------------------------------------------------')	#60個

# Fixing random state for reproducibility
np.random.seed(19680801)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt 

#x，y，大小，颜色
plt.scatter([1,2,3,4],[2,4,6,8],[10,20,30,400],['r', 'b','y','k'])   
plt.scatter([1,2,3,4],[9,8,7,6],s=10,c='b', marker='v')   

plt.show()

print('------------------------------------------------------------')	#60個


#試著做三群的數據。

cx0 = 0
cy0 = 0

cx1 = -3
cy1 = 3

cx2 = 3
cy2 = 3

#每一群都是 500 個點

x0 = np.random.randn(500) + cx0
y0 = np.random.randn(500) + cy0

x1 = np.random.randn(500) + cx1
y1 = np.random.randn(500) + cy1

x2 = np.random.randn(500) + cx2
y2 = np.random.randn(500) + cy2

#合併三群的點到 x, y 之中。
x = np.concatenate((x0, x1, x2))
y = np.concatenate((y0, y1, y2))

"""
現在第一群的點是第 0 類, 第二群是第 1 類, 第三群是第 2 類，所以我們要做個像這樣
[0, 0, ..., 0, 1, 1, ..., 1, 2, 2, ..., 2]
的標記。
"""

c = np.repeat([0,1,2], 500)

plt.scatter(x, y, c=c, cmap='Set1')

plt.show()


print('------------------------------------------------------------')	#60個


X = []
Y = []
for i in range(1000):
    theta = 2 * random.random() * math.pi
    r = random.random() * 5
    x = math.cos(theta) * r + 5
    y = math.sin(theta) * r + 5
    X.append(x)
    Y.append(y)

plt.scatter(X, Y)
print(len(X))
plt.axis([0, 10, 0, 10])
plt.axis('equal')       #軸比例
plt.show()

print('------------------------------------------------------------')	#60個

X = []
Y = []
for i in range(1000):
    x=random.randint(0, 10) + random.random()
    y=random.randint(0, 10) + random.random()
    if ((x - 5) ** 2 + (y - 5) ** 2) > 25:
        #print('Reject ({0}, {1})'.format(x, y))
        continue
    else :
        X.append(x)
        Y.append(y)
print(len(X))        

plt.scatter(X, Y)
print(len(X))
plt.axis([0, 10, 0, 10])
plt.axis('equal')       #軸比例
plt.show()

print('------------------------------------------------------------')	#60個


degrees = [x * 15 for x in range(0, 25)]
x = [math.cos(math.radians(d)) for d in degrees]
y = [math.sin(math.radians(d)) for d in degrees]

plt.scatter(x, y)
plt.axis('equal')
plt.grid()

plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

"""

matplotlib.pyplot.scatter(x, 
    y, 
    s=20, 
    c='b', 
    marker='o', 
    cmap=None, 
    norm=None, 
    vmin=None, 
    vmax=None, 
    alpha=None, 
    linewidths=None, 
    verts=None, 
    hold=None, 
    **kwargs)

参数：
    x，y：表示的是shape大小为(n,)的数组，也就是我们即将绘制散点图的数据点，输入数据。
    s：表示的是大小，是一个标量或者是一个shape大小为(n,)的数组，可选，默认20。
    c：表示的是色彩或颜色序列，可选，默认蓝色’b’。但是c不应该是一个单一的RGB数字，也不应该是一个RGBA的序列，因为不便区分。c可以是一个RGB或RGBA二维行数组。
     
    marker：MarkerStyle，表示的是标记的样式，可选，默认’o’。
    cmap：Colormap，标量或者是一个colormap的名字，cmap仅仅当c是一个浮点数数组的时候才使用。如果没有申明就是image.cmap，可选，默认None。
    norm：Normalize，数据亮度在0-1之间，也是只有c是一个浮点数的数组的时候才使用。如果没有申明，就是默认None。
    vmin，vmax：标量，当norm存在的时候忽略。用来进行亮度数据的归一化，可选，默认None。
    alpha：标量，0-1之间，可选，默认None。
    linewidths：也就是标记点的长度，默认None。
"""

import numpy as np
import matplotlib.pyplot as plt
 
np.random.seed(0)
x=np.random.rand(20)
y=np.random.rand(20)

area=(50*np.random.rand(20))**2
 
plt.scatter(x,y,s=area,alpha=0.5)
plt.show()


#把c参数改成随机数组。

import numpy as np
import matplotlib.pyplot as plt
 
np.random.seed(0)
x=np.random.rand(20)
y=np.random.rand(20)
 
colors=np.random.rand(20)
area=(50*np.random.rand(20))**2
 
plt.scatter(x,y,s=area,c=colors,alpha=0.5)
plt.show()




#把maker参数改成x的样本。

import numpy as np
import matplotlib.pyplot as plt
 
np.random.seed(0)
x=np.random.rand(20)
y=np.random.rand(20)
 
colors=np.random.rand(20)
area=(50*np.random.rand(20))**2
 
plt.scatter(x,y,s=area,c=colors,alpha=0.5,marker='x')
plt.show()


#修改其中的linewidth参数的大小，但是没什么不同，**注意：**只有marker为封闭的图案的时候，这个参数才有效。

import numpy as np
import matplotlib.pyplot as plt
 
np.random.seed(0)
x=np.random.rand(20)
y=np.random.rand(20)
 
colors=np.random.rand(20)
area=(50*np.random.rand(20))**2

lines=np.zeros(220)+5

plt.scatter(x,y,s=area,c=colors,alpha=0.5,marker='x',linewidths=lines)
plt.show()



#把s参数改成200。

import numpy as np
import matplotlib.pyplot as plt
 
np.random.seed(0)
x=np.random.rand(20)
y=np.random.rand(20)
 
colors=np.random.rand(20)
plt.scatter(x,y,s=200,c=colors,alpha=0.5)
plt.show()




#把linewidths参数改成数组。

import numpy as np
import matplotlib.pyplot as plt
 
np.random.seed(0)
x=np.random.rand(20)
y=np.random.rand(20)

lines=np.zeros(220)+5
plt.scatter(x,y,s=200,c='b',alpha=0.5,linewidths=lines)
#再把alpha改成1
plt.show()

print('------------------------------------------------------------')	#60個
"""
matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, 
vmax=None, alpha=None, linewidths=None, verts=None, edgecolors=None, hold=None, data=None, **kwargs)

基本参数讲解

x, y → 散点的坐标
s → 散点的面积
c → 散点的颜色（默认值为蓝色，'b'，其余颜色同plt.plot( )）
marker → 散点样式（默认值为实心圆，'o'，其余样式同plt.plot( )）
alpha → 散点透明度（[0, 1]之间的数，0表示完全透明，1则表示完全不透明）
linewidths →散点的边缘线宽
edgecolors → 散点的边缘颜色


高级参数讲解

cmap → 指的是matplotlib.colors.Colormap，相当于多个调色盘的合集
norm、vmin、vmax → 散点颜色亮度设置
    


"""

import matplotlib.pyplot as plt
import numpy as np

n = 10 # 用于生成十个点
x = np.random.rand(n)
y = np.random.rand(n)

plt.scatter(x, y)

plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import numpy as np

n = 10 # 用于生成十个点
x = np.random.rand(n)
y = np.random.rand(n)

plt.scatter(x, y, s=100, c='r', marker='*',alpha=0.65)

plt.show()

print('------------------------------------------------------------')	#60個


#numpy.random.RandomState的用法

import matplotlib.pyplot as plt
import numpy as np

rng = np.random.RandomState(0)

x = rng.randn(50)  # 随机产生50个X轴坐标
y = rng.randn(50)  # 随机产生50个Y轴坐标

colors = rng.rand(50)  # 随机产生50个用于颜色映射的数值
sizes = 700 * rng.rand(50)  # 随机产生50个用于改变散点面积的数值

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='viridis')

plt.show()

#这里从cmap中选取了一个叫做'viridis'的调色盘，
#其作用是，将参数c中获取到的数值，映射到“色盘”中已经对应好的颜色上

#并且上图中从“色盘”viridis中获取到的颜色，
#可以通过plt.colorbar( )显示为颜色条（与热力图同理）。


print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import numpy as np

rng = np.random.RandomState(0)

x = rng.randn(50)  # 随机产生50个X轴坐标
y = rng.randn(50)  # 随机产生50个Y轴坐标

colors = rng.rand(50)  # 随机产生50个用于颜色映射的数值
sizes = 700 * rng.rand(50)  # 随机产生50个用于改变散点面积的数值

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='viridis')

plt.colorbar()  # 显示颜色条

plt.show()

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors  # 注意！为了调整“色盘”，需要导入colors

rng = np.random.RandomState(0)
x = rng.randn(50)
y = rng.randn(50)
color = rng.rand(50)
sizes = 700 * rng.rand(50)

changecolor = colors.Normalize(vmin=0.4, vmax=0.8)

plt.scatter(x, y, c=color, s=sizes, alpha=0.3, cmap='viridis',norm=changecolor)

plt.colorbar()
plt.show()

print('------------------------------------------------------------')	#60個

"""
matplotlib.pyplot.scatter(x, y, s=None, 
                            c=None, marker=None, 
                            cmap=None, norm=None, 
                            vmin=None, vmax=None, 
                            alpha=None, linewidths=None, 
                            verts=None, edgecolors=None, 
                            **kwargs)

x，y：输入数据的x，y轴
s：标量或数组，可选参数，散点图点的大小
c：颜色或颜色序列，可选参数，默认为蓝色
marker：散点图中点的形状，默认为圆点
cmap：色图，仅在c是浮点数组的情况下使用
norm：设置数据亮度，用于将亮度数据缩放到0~1之间。仅当c是浮点数组的情况下使用
vmin，vmax：亮度设置，与norm类似，只是设置缩放的范围，当使用了norm参数，则该参数无效
alpha：透明度设置，0（透明）~1（不透明）之间
linewidths：设置散点边界线的宽度
verts：如果marker参数为空，则用（x，y）序列来构造marker，中心的点被置为（0，0），其他点被s重新缩放
edgecolors：设置散点边界线的颜色
"""


    
print('------------------------------------------------------------')	#60個


import matplotlib.pyplot as plt
import numpy as np

np.random.seed(100)

x = np.arange(0.0, 50.0, 1.0)   # 生成一个0到50的序列

y = x ** 1.3 + np.random.rand(*x.shape) * 30.0 # y = x ^ 1.3 + 随机值 * 30 

fig = plt.figure()
ax = fig.add_subplot(111)

ax.scatter(x,y, # 输入的数据
           alpha=0.9, # 设置点的透明度
           label='rand')
ax.set_title('this is title',fontsize=20) # 添加标题，并设置字体大小
ax.set_xlabel('this is x', fontsize=15) # 添加x轴，并设置字体大小
ax.set_ylabel('this is y', fontsize=15) # 添加y轴，并设置字体大小
ax.legend(loc='best')   # 添加图例

plt.show()

print('------------------------------------------------------------')	#60個

np.random.seed(500)

N = 50                  # 数据点总数
x = np.random.rand(N)   # x 轴数据
y = np.random.rand(N)   # y 轴数据
colors = np.random.rand(N)  # 颜色

area = np.pi * (15 * np.random.rand(N))**2 # 每个点对应的面积大小，（即气泡大小，这里可以放入第3个属性数据）

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x,y,
           s=area,
           c=colors,
           alpha=0.5)
plt.show()

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

