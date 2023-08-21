# plot 集合

'''

無法用subplot合併的


一次顯示一個

'''

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib


print('------------------------------------------------------------')	#60個

#兩Y軸不同刻度

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
sinhs = np.sinh(x)

fig, ax = plt.subplots()
ax.plot(x, sinus, "r-o")
ax2 = ax.twinx()
ax2.plot(x, sinhs, "g--")

plt.show()



print('------------------------------------------------------------')	#60個

#兩Y軸不同刻度


#plot + bar

import matplotlib.gridspec as gridspec


x = np.linspace(0, 6.28, 10)
y = np.sin(x * 2)
y2 = np.sin(x * 2) * np.sin(x * 2) *10

fig = plt.figure(figsize=(12, 8))	#圖像大小[英吋]
gs = gridspec.GridSpec(4, 1, figure=fig)
ax = fig.add_subplot()

ax.plot(x, y, marker="", alpha=0.8)

ax.grid(20)
axx = ax.twinx()
axx.bar(
	x, y2,
	alpha=0.2,
	label="hold_volume",
	color="pink",
)

plt.show()







print('------------------------------------------------------------')	#60個

'''
fig, ax = plt.subplots()
ax.plot(x, sinus, "r-o")
ax.set_xlabel("x", color="green")
ax.set_ylabel("Sin(x)", color="red")
ax2 = ax.twinx()
ax2.plot(x, sinhs, "g--")
ax2.set_ylabel("Sinh(x)", color="blue")
plt.show()
'''

print('------------------------------------------------------------')	#60個

'''
fig, ax = plt.subplots()
ax.plot(x, sinus, "r-o", label="Sin(x)")
ax.set_xlabel("x", color="green")
ax.set_ylabel("Sin(x)", color="red")
ax.legend(loc="best")
ax2 = ax.twinx()
ax2.plot(x, sinhs, "g--", label="Sinh(x)")
ax2.set_ylabel("Cos(x)", color="blue")
ax2.legend(loc="best")
plt.show()
'''



plt.show()
print('------------------------------------------------------------')	#60個


'''
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

def set_plot(amp, function):
    global figure_w, figure_h, fig
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = np.linspace(-np.pi * 2, np.pi * 2, 100)
    if function == 'sine':
        y= amp * np.sin(x)
        ax.set_title('sin(x)')
    else:
        y=amp*np.cos(x)
        ax.set_title('cos(x)')
    plt.plot(x / np.pi, y)
    
    #centre bottom and left axes to zero

    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')

    #Format axes - nicer eh!
    ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%g $\pi$'))

    figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds
    
amp = 1
function = 'sine'

set_plot(amp, function)

plt.show()


print('------------------------------------------------------------')	#60個


import matplotlib.pyplot as plt

#新增圖表
#plt.figure()
plt.figure(figsize=(8, 8))	#設定圖片視窗大小

plt.plot([1,2,3])
plt.grid(axis='y')  #加上y格線

#新增圖表 並 設定屬性
plt.figure(figsize=[8, 4], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
plt.plot([1,2,3])


plt.axis("off")  #隱藏坐標軸
_ = plt.title('image file', size="x-large", y=-0.1)  #顯示圖片描述

plt.axis("off")
plt.title('Picture Title', size=30, x=0.0, y=0.0)

plt.show()
'''


print('------------------------------------------------------------')	#60個

# 生成 100000 組標準常態分配（平均值為 0，標準差為 1 的常態分配）隨機變數
normal_samples = np.random.normal(size = 100000)

#盒鬚圖（Box plot）
#plt.boxplot(normal_samples)


plt.hist(normal_samples)
plt.show()


print('------------------------------------------------------------')	#60個


