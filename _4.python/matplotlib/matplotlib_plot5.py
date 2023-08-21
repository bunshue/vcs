'''
xkcd

使用matplotlib绘制xkcd动漫风格的图表（解决中文字体问题）

'''

'''
import numpy as np

#  使用动漫风格

bo = np.arange(5)
prices = [ 234, 123, 348, 287, 186]
persons = [ 568, 720, 520, 484, 386]

from matplotlib import pyplot as plt 

plt.rcParams.update({'font.family': "Microsoft YaHei"})

plt.xkcd()

plt.figure(figsize=(16,10),dpi=100)

plt.rcParams['font.sans-serif']=['Microsoft YaHei'] # 使用微软雅黑的字体

plt.title("中国票房2021TOP5") 

plt.plot(bo,prices,'r^--',label='票房与票价')

plt.plot(bo,persons,'g*-',label='票房与人次')

#plt.plot(bo,points,color='blue',marker='o',markersize=10,label='票房与评价')

plt.legend() # 显示标签

plt.xlabel('票房') # 横坐标轴标题

plt.ylabel('行情') # 纵坐标轴标题

plt.grid()

plt.savefig("cnbotop5_300.png")

plt.show()

'''

'''
def xkcd(scale=1, length=100, randomness=2):
    return _xkcd(scale, length, randomness)

class _xkcd:
    # This cannot be implemented in terms of rc_context() because this needs to
    # work as a non-contextmanager too.

    def __init__(self, scale, length, randomness):
        self._orig = rcParams.copy()

        if rcParams['text.usetex']:
            raise RuntimeError(
                "xkcd mode is not compatible with text.usetex = True")

        from matplotlib import patheffects
        rcParams.update({
            'font.family': ['xkcd', 'xkcd Script', 'Humor Sans', 'Comic Neue',
                            'Comic Sans MS'],
            'font.size': 14.0,
            'path.sketch': (scale, length, randomness),
            'path.effects': [
                patheffects.withStroke(linewidth=4, foreground="w")],
            'axes.linewidth': 1.5,
            'lines.linewidth': 2.0,
            'figure.facecolor': 'white',
            'grid.linewidth': 0.0,
            'axes.grid': False,
            'axes.unicode_minus': False,
            'axes.edgecolor': 'black',
            'xtick.major.size': 8,
            'xtick.major.width': 3,
            'ytick.major.size': 8,
            'ytick.major.width': 3,
        })

    def __enter__(self):
        return self

    def __exit__(self, *args):
        dict.update(rcParams, self._orig)
        

'''


'''
import matplotlib.pyplot as plt

plt.rcParams.update({'font.family': "Comic Sans"})

with plt.xkcd():
    plt.bar([1,2,3],[1,2,3])
    plt.title('test')
plt.show()
'''

import matplotlib.pyplot as plt

plt.xkcd()
plt.rcParams.update({'font.family': "FZKaTong-M19S"})
plt.bar([1,2,3],[1,2,3])
plt.title("测试")
plt.show()




