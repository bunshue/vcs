import math

import numpy as np

import matplotlib.pyplot as plt

import matplotlib.colors as mcolors
from matplotlib.patches import Rectangle

'''
def plot_colortable(colors, *, ncols=4, sort_colors=True):

    cell_width = 212
    cell_height = 22
    swatch_width = 48
    margin = 12

    # Sort colors by hue, saturation, value and name.
    if sort_colors is True:
        names = sorted(
            colors, key=lambda c: tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(c))))
    else:
        names = list(colors)

    n = len(names)
    nrows = math.ceil(n / ncols)

    width = cell_width * ncols + 2 * margin
    height = cell_height * nrows + 2 * margin
    dpi = 72

    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
    fig.subplots_adjust(margin/width, margin/height,
                        (width-margin)/width, (height-margin)/height)
    ax.set_xlim(0, cell_width * ncols)
    ax.set_ylim(cell_height * (nrows-0.5), -cell_height/2.)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()

    for i, name in enumerate(names):
        row = i % nrows
        col = i // nrows
        y = row * cell_height

        swatch_start_x = cell_width * col
        text_pos_x = cell_width * col + swatch_width + 7

        ax.text(text_pos_x, y, name, fontsize=14,
                horizontalalignment='left',
                verticalalignment='center')

        ax.add_patch(
            Rectangle(xy=(swatch_start_x, y-9), width=swatch_width,
                      height=18, facecolor=colors[name], edgecolor='0.7')
        )

    return fig

#Base colors
plot_colortable(mcolors.BASE_COLORS, ncols=3, sort_colors=False)
plt.show()

#Tableau Palette

plot_colortable(mcolors.TABLEAU_COLORS, ncols=2, sort_colors=False)
plt.show()

#CSS Colors

plot_colortable(mcolors.CSS4_COLORS)
plt.show()

xkcd_fig = plot_colortable(mcolors.XKCD_COLORS)
xkcd_fig.savefig("XKCD_Colors.png")


print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0.0, 2.0, 201)
s = np.sin(2 * np.pi * t)

# 1) RGB tuple:
fig, ax = plt.subplots(facecolor=(.18, .31, .31))
# 2) hex string:
ax.set_facecolor('#eafff5')
# 3) gray level string:
ax.set_title('Voltage vs. time chart', color='0.7')
# 4) single letter color string
ax.set_xlabel('Time [s]', color='c')
# 5) a named color:
ax.set_ylabel('Voltage [mV]', color='peachpuff')
# 6) a named xkcd color:
ax.plot(t, s, 'xkcd:crimson')
# 7) Cn notation:
ax.plot(t, .7*s, color='C4', linestyle='--')
# 8) tab notation:
ax.tick_params(labelcolor='tab:orange')


plt.show()

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

'''
print('------------------------------------------------------------')	#60個

""" fail no csv file
dataset = np.loadtxt('iris.csv', delimiter=',')

fig = plt.figure()
ax = fig.add_subplot(111)

color = ['r','y','b']
species = ['Setosa','Versicolour','Virginica']
Setosa = []
Versicolour = []
Virginica = []

# 不同种类保存为不同的列表
for i in range(len(dataset)):
    if dataset[i][-1] == 0:
        Setosa.append(dataset[i].tolist())
    elif dataset[i][-1] == 1:
        Versicolour.append(dataset[i].tolist())
    elif dataset[i][-1] == 2:
        Virginica.append(dataset[i].tolist())


ax.scatter(x=np.array(Setosa)[:,0], # Setosa种类的花瓣的长度
     y=np.array(Setosa)[:,1], # Setosa种类的花瓣的宽度
     s=35,                    # 散点大小为35
     c=color[0],              # 颜色为红色
     label=species[0])        # 标签为Setosa

ax.scatter(x=np.array(Versicolour)[:,0],    # Versicolour种类的花瓣的长度
     y=np.array(Versicolour)[:,1],    # Versicolour种类的花瓣的宽度
     s=35,                            # 散点大小为35
     c=color[1],                      # 颜色为黄色
     label=species[1])                # 标签为Versicolour

ax.scatter(x=np.array(Virginica)[:,0],  # Virginica种类的花瓣的长度
     y=np.array(Virginica)[:,1],  # Virginica种类的花瓣的宽度
     s=35,                        # 散点大小为35
     c=color[2],                  # 颜色为蓝色
     label=species[2])            # 标签为Virginica

# 添加轴标签和标题
ax.set_title('花瓣长度与宽度的关系',
       fontproperties='SimHei',
       fontsize=20)
ax.set_xlabel('花瓣的长度',
        fontproperties='SimHei',
        fontsize=15)
ax.set_ylabel('花瓣的宽度',
        fontproperties='SimHei',
        fontsize=15)

ax.legend(loc='best') # 添加图例
"""
    
print('------------------------------------------------------------')	#60個

    
print('------------------------------------------------------------')	#60個

    
print('------------------------------------------------------------')	#60個
