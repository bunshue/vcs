# plot 集合 動畫

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt  
import numpy as np  
from matplotlib.animation import FuncAnimation  


print('------------------------------------------------------------')	#60個

"""
python学习之matplotlib绘制动图（FuncAnimation()参数）

1、函数FuncAnimation(fig,func,frames,init_func,interval,blit)是绘制动图的主要函数，其参数如下：

　　a.fig 绘制动图的画布名称

　　b.func自定义动画函数，即下边程序定义的函数update

　　c.frames动画长度，一次循环包含的帧数，在函数运行时，其值会传递给函数update(n)的形参“n”

　　d.init_func自定义开始帧，即传入刚定义的函数init,初始化函数

　　e.interval更新频率，以ms计

　　f.blit选择更新所有点，还是仅更新产生变化的点。应选择True，但mac用户请选择False，否则无法显
"""

print('------------------------------------------------------------')	#60個

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()   #生成子图，相当于fig = plt.figure(),ax = fig.add_subplot(),其中ax的函数参数表示把当前画布进行分割，例：fig.add_subplot(2,2,2).表示将画布分割为两行两列　　　　　　　　　　　　　　　　#ax在第2个子图中绘制，其中行优先，
xdata, ydata = [], []      #初始化两个数组
ln, = ax.plot([], [], 'r-', animated=False)  #第三个参数表示画曲线的颜色和线型，具体参见：https://blog.csdn.net/tengqingyong/article/details/78829596

def init():
    ax.set_xlim(0, 2*np.pi)  #设置x轴的范围pi代表3.14...圆周率，
    ax.set_ylim(-1, 1)          #设置y轴的范围
    return ln,               #返回曲线

def update(n):
    xdata.append(n)         #将每次传过来的n追加到xdata中
    ydata.append(np.sin(n))
    ln.set_data(xdata, ydata)    #重新设置曲线的值
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 10),     #这里的frames在调用update函数是会将frames作为实参传递给“n”
                    init_func=init, blit=True)
plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



