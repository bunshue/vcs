'''
matplotlib_無法用subplot合併的


一次顯示一個

'''

# plot 集合

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

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

#散點圖

import numpy as np
import matplotlib.pyplot as plt

N = 150
# 產生 150 個 0~2 之間的隨機半徑
r = 2 * np.random.rand(N)
# 產生 150 個 0~2pi 之間的隨機弧度
theta = 2 * np.pi * np.random.rand(N)
# 區域大小與半徑成正比
area = 50 * r**2
# 顏色由弧度決定
colors = theta

ax = plt.subplot(211)
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

# 畫出極座標圖，此時的 x 為弧度，y 為半徑
ax = plt.subplot(212, projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.75)

plt.show()

print('------------------------------------------------------------')	#60個

#圓餅圖

import matplotlib.pyplot as plt

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
# 分離係數，所以只有 'Hogs' 會分離
explode = (0, 0.1, 0, 0)

fig1, ax1 = plt.subplots()
# 從 90° 開始，逆時針排列，並加上陰影，並加上每塊的比例，格式為 '%1.2f%%'
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.2f%%', shadow=True, startangle=90)
# 調整比例，確認顯示為圓形
ax1.axis('equal')

plt.show()

print('------------------------------------------------------------')	#60個

x = np.linspace(-2*np.pi, 2*np.pi, 200)
y = np.sin(x)

ax = plt.gca()
ax.set_facecolor('#69b8bb')
ax.set_xlim(-6,6)
ax.set_ylim(-1.2,1.2)
plt.plot(x,y,lw=5,c='white')

#移動 x, y 座標軸
ax = plt.gca()
ax.set_facecolor('#69b8bb')
ax.set_xlim(-6,6)
ax.set_ylim(-1.2,1.2)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

plt.plot(x, y, lw=5 ,c = 'white')

#使用自定義的中文字型
import matplotlib.font_manager as fm
font_filename = 'C:/_git/vcs/_2.vcs/my_vcs_lesson_6/__MY/vcs_DrawPoem/vcs_DrawPoem/font/康楷體w5.TTC'
#font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'

#myfont = fm.FontProperties(fname="/Users/mac/Library/Fonts/NotoSansHant-Medium.otf")
myfont = fm.FontProperties(fname = font_filename)

plt.title("使用自定義的中文字型", fontproperties=myfont, size=24)

plt.show()

print('------------------------------------------------------------')	#60個


'''
#完完全全改過來
#用 matplotlib 的參數設定, rcParams, 把字型完完全全用某個中文字型

#plt.rcParams['font.sans-serif'] = ['SimHei'] # 選個普通的黑體字
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
plt.rcParams['axes.unicode_minus']=False # 負號不出問題
plt.title("使用自定義的中文字型", size=15) # 不用再設字型!


#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

'''

print('------------------------------------------------------------')	#60個

x1 = np.linspace(-5, 5, 101)
y1 = np.sin(x1)

fig, ax = plt.subplots()
ax.set_title("Sin")
ax.set_xlabel("rad")
ax.plot(x1, y1)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

plt.show()

print('------------------------------------------------------------')	#60個

π = np.pi

θ = np.linspace(0, 2*π, 500)

r = 3
x = r * np.cos(θ)
y = r * np.sin(θ)

#gca 的意思是 "Get Current Axes"。
ax = plt.gca()
ax.set_aspect('equal')

plt.plot(x, y)

plt.show()

print('------------------------------------------------------------')	#60個

r = 1 - np.sin(θ)

x = r * np.cos(θ)
y = r * np.sin(θ)

ax = plt.gca()
ax.set_aspect('equal')

plt.plot(x, y, 'r')

plt.show()

print('------------------------------------------------------------')	#60個

# 建立 x，從 -pi 到 pi，共 100 點，且需包含終點 pi
x = np.linspace(-np.pi, np.pi, num=100, endpoint=True)
c,s,t = np.cos(x), np.sin(x), np.tan(x)

# 第一次呼叫 plt.plot 會自動建立合適的 figure
# 之後若有使用到 plt.method 皆以此 figure 為主
# 可以使用 latex 語法，需用 $ ... $ 包住
plt.plot(x, c, label=r'cos$\theta$')

# 之後呼叫 plt.plot 會使用先前建立的 figure
# 畫出紅色向下三角形
plt.plot(x, s, 'rv', label=r'sin$\theta$')
# 畫出綠虛線，並在各點位置標上綠線青圓點
plt.plot(x, t, color='g', linestyle='dashed', marker='o', markerfacecolor='c', markersize=5)

# 設定 x軸 label
plt.xlabel('X軸')
# 設定 x軸對應的刻度，並替換為文字
plt.xticks( [-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
# 設定 x軸左右範圍
xmin ,xmax = x.min(), x.max()
dx = (xmax - xmin) * 0.2
plt.xlim(xmin - dx, xmax + dx)

# 設定 y軸 label
plt.ylabel('Y軸')
# 設定 x軸對應的刻度
plt.yticks([-1, 0, +1])
# 設定 y軸上下範圍
ymin ,ymax = c.min(), c.max()
dy = (ymax - ymin) * 0.2
plt.ylim(ymin - dy, ymax + dy)

# 需有 label 才會顯示，所以 tanθ 並無顯示
plt.legend()

# 建立中心坐標軸
# 回傳目前的坐標軸 get current axes
ax = plt.gca()
# 將上跟右的線，設成隱藏
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 設定 x軸刻度顯示在下方
ax.xaxis.set_ticks_position('bottom')
# 設定下方的線，移動至 data 為 -1 的地方
ax.spines['bottom'].set_position(('data',-1))
# 設定 y軸刻度顯示在左方
ax.yaxis.set_ticks_position('left')
# 設定左方的線，移動至坐標軸中心
ax.spines['left'].set_position(('axes', 0.5))

plt.show()

print('------------------------------------------------------------')	#60個

x = np.linspace(-2*np.pi, 2*np.pi, 100)
plt.ylim((-1.2, 1.2))
plt.plot(x, np.sin(x), label="SIN", linestyle="--")
plt.plot(x, np.cos(x), label="COS", color="red")
plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], 
           [r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$'])
plt.legend()
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

plt.show()


print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt 
import numpy as np

N = 50                                      # 色彩數列的點數
colorused = ['b','c','g','k','m','r','y']   # 定義顏色
colors = []                                 # 建立色彩數列
for i in range(N):                          # 隨機設定顏色
    colors.append(np.random.choice(colorused))
x = np.linspace(0.0, 2*np.pi, N)            # 建立 50 個點
y = np.sin(x)
fig = plt.figure()                          # 建立畫布物件
ax = fig.add_subplot()                      # 建立子圖(或稱軸物件)ax
ax.scatter(x, y, c=colors, marker='*')      # 繪製 sin
ax.set_title("建立畫布與軸物件,使用OO API繪圖", fontsize=16)

plt.show()


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

