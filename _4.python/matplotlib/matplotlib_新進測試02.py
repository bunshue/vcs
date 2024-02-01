# 新進測試02

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

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="新進測試 01",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False

# 正常顯示
x1 = np.linspace(-1.5, 1.5, 31)
y1 = np.cos(x1) ** 2

# 移除 y1 > 0.6 的點
x2 = x1[y1 <= 0.6]
y2 = y1[y1 <= 0.6]

# 遮罩 y1 > 0.7 的點
y3 = np.ma.masked_where(y1 > 0.7, y1)

# 將 y1 > 0.8 的點設為 NaN
y4 = y1.copy()
y4[y4 > 0.8] = np.nan

plt.plot(x1 * 0.1, y1, "o-", label="正常顯示")
plt.plot(x2 * 0.4, y2, "o-", label="移除點")
plt.plot(x1 * 0.7, y3, "o-", label="遮罩點")
plt.plot(x1 * 1.0, y4, "o-", label="將點設為NaN")
plt.legend()
plt.title("Cos函數顯示與遮蔽點的應用")

# 第二張圖
plt.subplot(232)

d1 = [10 for y in range(1, 9)]  # data1線條之y值
d2 = [20 for y in range(1, 9)]  # data2線條之y值
d3 = [30 for y in range(1, 9)]  # data3線條之y值
d4 = [40 for y in range(1, 9)]  # data4線條之y值
d5 = [50 for y in range(1, 9)]  # data5線條之y值
d6 = [60 for y in range(1, 9)]  # data6線條之y值
d7 = [70 for y in range(1, 9)]  # data7線條之y值
d8 = [80 for y in range(1, 9)]  # data8線條之y值
d9 = [90 for y in range(1, 9)]  # data9線條之y值
d10 = [100 for y in range(1, 9)]  # data10線條之y值
d11 = [110 for y in range(1, 9)]  # data11線條之y值
d12 = [120 for y in range(1, 9)]  # data12線條之y值

seq = [1, 2, 3, 4, 5, 6, 7, 8]
plt.plot(
    seq,
    d1,
    "-1",
    seq,
    d2,
    "-2",
    seq,
    d3,
    "-3",
    seq,
    d4,
    "-4",
    seq,
    d5,
    "-s",
    seq,
    d6,
    "-p",
    seq,
    d7,
    "-*",
    seq,
    d8,
    "-+",
    seq,
    d9,
    "-D",
    seq,
    d10,
    "-d",
    seq,
    d11,
    "-H",
    seq,
    d12,
    "-h",
)

# 第三張圖
plt.subplot(233)

print("畫點")
plt.plot(0, 1, "-o")  # 在 (0, 1) 上 畫一點
plt.plot(1, 5, "r-o")
plt.plot(2, 10, "r-o")
plt.plot(3, 20, "r-o")

plt.title("畫點")

# 第四張圖
plt.subplot(234)

radius = 5
degrees = np.arange(0, 360)
x = radius * np.cos(np.radians(degrees))
y = radius * np.sin(np.radians(degrees))

plt.plot(x, y)
plt.axis("equal")
plt.grid()

# 第五張圖
plt.subplot(235)

x1 = np.linspace(0.1, 10, 99)  # 建立含30個元素的陣列
x2 = np.linspace(0.1, 10, 99)  # 建立含30個元素的陣列
y1 = [math.log2(x) for x in x1]
y2 = [math.log(x, 0.5) for x in x2]

plt.plot(x1, y1, label="基底 = 2")
plt.plot(x2, y2, label="基底 = 0.5")

plt.axis([0, 10, -5, 5])
plt.legend(loc="best")  # 建立圖例
plt.grid()

# 第六張圖
plt.subplot(236)

plt.show()

print("------------------------------------------------------------")  # 60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="新進測試 03",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)


# 第二張圖
plt.subplot(232)


# 第三張圖
plt.subplot(233)


# 第四張圖
plt.subplot(234)


# 第五張圖
plt.subplot(235)


# 第六張圖
plt.subplot(236)


plt.show()


print("------------------------------------------------------------")  # 60個

print("matplotlib 01 ------------------------------------------------------------")  # 60個

"""
python用mpl_finance中的candlestick_ohlc畫分時圖

matplotlib.finance獨立出來成爲mpl_finance，而mpl_finance中的candlestick_ochl和candlestick_ohlc一般用來畫股票的K線圖。我需要分析分時圖，也就是一分鐘的行情，這個時候就不能直接用candlestick_ochl函數，因爲candlestick_ochl中x軸最小的單位是日期，不是分鐘。

經過對mpl_finance的源代碼進行分析，問題在於matplotlib的date2num將日期轉換爲浮點數，浮點數的整數部分表示日期，小數部分代表小時和分鐘。比如下面4個時間段是連續的分鐘。
時間 	date2num之後 	乘以1440
2018/09/17-21:34 	736954.8986 	1061215054
2018/09/17-21:35 	736954.8993 	1061215055
2018/09/17-21:36 	736954.9000 	1061215056
2018/09/17-21:37 	736954.9007 	1061215057

可以看出date2num函數計算之後，4個時間的整數部分都是736954，導致在X軸上這4個時間段都重疊在一起，無法區分了。要達到的效果是每一個分鐘也能成爲一個整數，這樣就可以顯示出來了。那麼一天是24小時，每小時60分鐘，那麼一天就是1440分鐘，將date2num計算的浮點數乘以1440就可以將每一分鐘轉爲整數，那麼就可以在x軸上。

最後還需要對x軸格式化，因爲自己對x軸進行了處理（乘以1440），採用默認的格式化是亂碼。需要自定義x軸的格式化函數。
"""


"""
pip install mpl_finance
pip install --upgrade mplfinance
"""
from pandas import DataFrame
import matplotlib.dates as dates
import mpl_finance as mpf
from matplotlib.ticker import Formatter


dfcvs = DataFrame([
    ["2018/09/17-21:34", 3646, 3650,3644,3650],
    ["2018/09/17-21:35", 3650, 3650,3648,3648],
    ["2018/09/17-21:36", 3650, 3650,3648,3650],
    ["2018/09/17-21:37", 3652, 3654,3648,3652]
])

dfcvs.columns = ['時間','開盤','最高','最低','收盤']
dfcvs['時間'] = pd.to_datetime(dfcvs['時間'],format = "%Y/%m/%d-%H:%M")

#matplotlib的date2num將日期轉換爲浮點數，整數部分區分日期，小數區分小時和分鐘
#因爲小數太小了，需要將小時和分鐘變成整數，需要乘以24（小時）×60（分鐘）= 1440，這樣小時和分鐘也能成爲整數
#這樣就可以一分鐘就佔一個位置

dfcvs['時間'] = dfcvs['時間'].apply(lambda x:dates.date2num(x) * 1440)
data_mat = dfcvs.values
    
fig,ax = plt.subplots(figsize = (10, 6))
 
fig.subplots_adjust(bottom = 0.1)   
mpf.candlestick_ohlc(ax, data_mat, colordown = '#53c156', colorup = '#ff1717', width = 0.2, alpha = 1)

#將x軸的浮點數格式化成日期小時分鐘
#默認的x軸格式化是日期被dates.date2num之後的浮點數，因爲在上面乘以了1440，所以默認是錯誤的
#只能自己將浮點數格式化爲日期時間分鐘
#參考https://matplotlib.org/examples/pylab_examples/date_index_formatter.html
class MyFormatter(Formatter):
            def __init__(self, dates, fmt = '%Y%m%d %H:%M'):
                self.dates = dates
                self.fmt = fmt
    
            def __call__(self, x, pos = 0):
                'Return the label for time x at position pos'
                ind = int(np.round(x))
                #ind就是x軸的刻度數值，不是日期的下標

                return dates.num2date( ind/1440).strftime(self.fmt)
        
formatter = MyFormatter(data_mat[:,0])
ax.xaxis.set_major_formatter(formatter)

for label in ax.get_xticklabels():
            label.set_rotation(90)
            label.set_horizontalalignment('right')
           
plt.show()

print("matplotlib 02 ------------------------------------------------------------")  # 60個

# 加載取數與繪圖所需的函數包
import datetime
from hs_udata import set_token,stock_quote_daily
from mpl_finance import candlestick_ohlc
import matplotlib as mpl
import matplotlib.dates as mdates

#mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默認字體
#mpl.rcParams['axes.unicode_minus'] = False  # 解決保存圖像是負號'-'顯示為方塊的問題

data_price = [1 ,2, 3, 4, 5]

#4、繪制圖片
fig = plt.figure(figsize = (12, 10))
grid = plt.GridSpec(12, 10, wspace = 0.5, hspace = 0.5)

ax1 = fig.add_subplot(grid[0 : 8, 0 : 12])   # 設置K線圖的尺寸

#candlestick_ohlc(ax1, ohlc.values.tolist(), width = 0.7, colorup = 'red', colordown = 'green')

# （2）繪制均線
#ax1.plot(range(len(data_price)), data_price, color = 'red', lw = 2, label = 'MA (5)')

# 設置標注
plt.title('test', fontsize = 14)       # 設置圖片標題
plt.ylabel('價 格（元）', fontsize = 14)   # 設置縱軸標題
plt.legend(loc = 'best')                    # 繪制圖例
ax1.set_xticks([])                        # 日期標注在成交量中，故清空此處x軸刻度
ax1.set_xticklabels([])                   # 日期標注在成交量中，故清空此處x軸

#（3）繪制成交量
# 成交量數據

data_volume = [3, 2, 1, 4, 6]
# 繪制成交量
ax2 = fig.add_subplot(grid[8 : 10, 0 : 12])  # 設置成交量圖形尺寸
#ax2.bar(data_volume, color = 'r')                    # 繪制紅色柱狀圖
#ax2.bar(data_volume, color = 'g')                    # 繪制綠色柱狀圖
plt.xticks(rotation = 30) 
plt.xlabel('日 期', fontsize = 14)                               # 設置橫軸標題
# 修改橫軸日期標注
date_list = [1, 2, 3, 4, 5]#ohlc.index.tolist()           # 獲取日期列表
xticks_len = round(len(date_list) / (len(ax2.get_xticks()) - 1))      # 獲取默認橫軸標注的間隔
xticks_num = range(0, len(date_list), xticks_len)                   # 生成橫軸標注位置列表
xticks_str = list(map(lambda x:date_list[int(x)], xticks_num))     # 生成正在標注日期列表
ax2.set_xticks(xticks_num)                                        # 設置橫軸標注位置
ax2.set_xticklabels(xticks_str)                                   # 設置橫軸標注日期

plt.show()

print("matplotlib 03 ------------------------------------------------------------")  # 60個

# foldername = 'C:/_git/vcs/_1.data/______test_files1/source_pic'
foldername = "C:/_git/vcs/_1.data/______test_files1"


"""
import glob
import cv2

files = glob.glob(foldername + "/*.jpg")  #建立測試資料
test_feature=[]
for file in files:
    print(file)
    img = cv2.imread(file)	#讀取本機圖片
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #灰階    
    _, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV) #轉為反相黑白 
    test_feature.append(img)

print(test_feature)

print('畫多張圖')


plt.gcf().set_size_inches(12, 14)

num=25

if num>25: num=25
for i in range(num):
    ax=plt.subplot(5,5, i+1)
    #ax.imshow(images[start_id], cmap='binary')  #顯示黑白圖片
    title = 'label = ' + str(i)
    ax.set_title(title,fontsize=12)  # X,Y軸不顯示刻度
    ax.set_xticks([]);ax.set_yticks([])        
plt.show()


"""

print("matplotlib 04 ------------------------------------------------------------")  # 60個

"""
x = np.linspace(start=-10, stop=10, num=101)

#plt.plot(x, np.absolute(x))

xx = x + 1j * x[:, np.newaxis]

plt.imshow(np.abs(xx), extent=[-10, 10, -10, 10], cmap='gray')
"""

print("matplotlib 05 ------------------------------------------------------------")  # 60個

""" fail
#zip 高級組合法

xx = [1, 2, 3, 4]
yy = [5, 6, 7, 8]
list(zip(xx, yy))

Z = list(zip(X, Y))
print(Z)

plt.scatter(X, Y, s = 50, c = Z)
plt.show()
"""

print("matplotlib 06 ------------------------------------------------------------")  # 60個

N = 100

sinc2d = np.zeros((N, N))
for x, x1 in enumerate(np.linspace(-10, 10, N)):
    for y, x2 in enumerate(np.linspace(-10, 10, N)):
        sinc2d[x, y] = np.sin(x1) * np.sin(x2) / (x1 * x2)
# print(sinc2d)

# same
x1 = np.linspace(-10, 10, N)
x2 = np.linspace(-10, 10, N)
sinc2d = np.outer(np.sin(x1), np.sin(x2)) / np.outer(x1, x2)
# print(sinc2d)

plt.imshow(sinc2d)
plt.show()

print("matplotlib 07 ------------------------------------------------------------")  # 60個

th = np.arange(0,360,10)
#print(th)

x = np.cos(np.radians(th))
y = np.sin(np.radians(th))

plt.plot(x,y)

plt.show()

print("matplotlib 08 ------------------------------------------------------------")  # 60個

# 時序圖
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

print("matplotlib 09 ------------------------------------------------------------")  # 60個
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

print("matplotlib 10 ------------------------------------------------------------")  # 60個

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

print("matplotlib 11 ------------------------------------------------------------")  # 60個

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

print("matplotlib 12 ------------------------------------------------------------")  # 60個

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

print("matplotlib 13 ------------------------------------------------------------")  # 60個

fig = plt.figure(figsize = (9,6))
ax1 = plt.subplot2grid((3,3), (0,0), colspan = 2)
ax2 = plt.subplot2grid((3,3), (0,2), rowspan = 2) 
ax3 = plt.subplot2grid((3,3), (1,0), rowspan = 2) 
ax4 = plt.subplot2grid((3,3), (1,1)) # rowspan/colspan默認爲1 
ax5 = plt.subplot2grid((3,3), (2,1), colspan = 2) 
ax5.plot([1,2,3,4,1])

plt.show()

print("matplotlib 14 ------------------------------------------------------------")  # 60個

x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[200000,180000,175000,215000,280000,320000,90000,365000,318000,198000,268000,348000]
plt.plot(x, y)
plt.xlabel('Month')
plt.ylabel('Sales amount')
plt.title('2020 sales chart for per month')

plt.show()

print("matplotlib 15 ------------------------------------------------------------")  # 60個

x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[200000,180000,175000,215000,280000,320000,90000,365000,318000,198000,268000,348000]
plt.plot(x, y, lw=8, ls='-.')
plt.xlabel('Month')
plt.ylabel('Sales amount')
plt.title('2020 sales chart for per month')

plt.show()

print("matplotlib 16 ------------------------------------------------------------")  # 60個

x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[200000,180000,175000,215000,280000,320000,90000,365000,318000,198000,268000,348000]
plt.plot(x, y, marker='*')
plt.xlabel('Month')
plt.ylabel('Sales amount')
plt.title('2020 sales chart for per month')

plt.show()

print("matplotlib 17 ------------------------------------------------------------")  # 60個

x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[200000,180000,175000,215000,280000,320000,90000,365000,318000,198000,268000,348000]
plt.plot(x, y, marker='D',ms=10, mfc='y', mec='r')
plt.xlabel('Month')
plt.ylabel('Sales amount')
plt.title('2020 sales chart for per month')

plt.show()

print("matplotlib 18 ------------------------------------------------------------")  # 60個

x=[1,2,3,4,5,6,7,8,9,10,11,12]
y=[200000,180000,175000,215000,280000,320000,90000,365000,318000,198000,268000,348000]
plt.plot(x, y)
plt.plot(x, y, color='y')
#plt.plot(x, y, color=(1,1,0))  #RGB
#plt.plot(x, y, color='# FFFF00')  #HEX
#plt.plot(x, y, color='yellow')  #英文全名
#plt.plot(x, y, color='0.5')
plt.xlabel('Month')
plt.ylabel('Sales amount')
plt.title('2020 sales chart for per month')

plt.show()

print("matplotlib 19 ------------------------------------------------------------")  # 60個

"""
正弦函數 s=sin(x) 
餘弦函數 c=cos(x)
"""

x = np.linspace(-2*np.pi, 2*np.pi, 100)
s, c=np.sin(x), np.cos(x)
plt.plot(x, s)
plt.plot(x, c)
plt.xticks([-2*np.pi,-np.pi,0, np.pi, 2*np.pi],['-$2\pi$', '-$\pi$','0', '$\pi$', '$2\pi$'])

plt.legend(['sin','cos'])
plt.legend(['sin','cos'],loc=3,fontsize='xx-large',edgecolor='y',facecolor='r')

plt.show()

print("matplotlib 20 ------------------------------------------------------------")  # 60個

"""
plt.xticks(range(0,5500,500))
plt.tick_params(axis = 'both', labelsize = 10, color = 'red')

plt.bar(listx, listy, width = 0.5, color = 'r')

plt.barh(listy, listx, height = 0.5, color = 'r')

"""

print("matplotlib 21 ------------------------------------------------------------")  # 60個

plt.figure(figsize = [8,4])

x = np.linspace(0, 2 * np.pi)
y = np.sin(x)

#所佔比例 0~1, 以左下為原點
x_st = 0.1
y_st = 0.1
w = 0.8
h = 0.8
plt.axes([x_st, y_st, w, h])
plt.title(label = '第一張圖')
plt.plot(x, y, 'r:o')

x_st = 0.6
y_st = 0.5
w = 0.25
h = 0.3
plt.axes([x_st, y_st, w, h])
plt.title(label = '第二張圖')
plt.plot(x, y, 'g--o')

plt.show()

print("matplotlib 22 ------------------------------------------------------------")  # 60個

x = np.linspace(0, 2 * np.pi)
y = np.sin(x)

plt.grid(True)

#自訂座標軸的刻度及標籤–xticks()、yticks()
#x座標
ticks = [0, np.pi * 0.5, np.pi, np.pi * 1.5, np.pi * 2]
#要在x座標寫上的標籤
labels = ['0°', '90°', '180°', '270°', '360°']
plt.xticks(ticks, labels)

plt.plot(x, y)

plt.show()

print("matplotlib 23 ------------------------------------------------------------")  # 60個

#在畫布切出子圖區 , 並繪製內容–add_subplot()

x = np.linspace(0, 2 * np.pi)
y = np.sin(x)

fig = plt.figure(figsize = (8, 6))        #整個圖表大小為 8 x 6 英吋
fig.subplots_adjust(wspace = 0.5, hspace = 0.75)    #調整子圖間距

ax1 = fig.add_subplot(2, 3, 1)      #←編號 1 的子圖
ax1.plot(x, y)

ax3 = fig.add_subplot(2, 3, 3)      #← 編號 3 的子圖
#沒畫

ax5 = fig.add_subplot(2, 3, 5)      #←編號 5 的子圖
ax5.plot(x, y)

ax6 = fig.add_subplot(2, 3, 6)      #←編號 6 的子圖
ax6.plot(x, y)
#設定子圖的座標範圍、座標說明文字與子圖標題
ax6.set_xlim(0, 3.14/2)
ax6.set_ylim(-0.1, 1.1)
ax6.set_xlabel('x-axis')
ax6.set_ylabel('y-axis')
ax6.set_title('y = sin(x)')
ax6.plot(x, y)

plt.show()

print("matplotlib 24 ------------------------------------------------------------")  # 60個

print('載入字型範例')

"""
翰字鑄造 台北黑體 regular 版本

TaipeiSansTCBeta-Regular.ttf 

https://drive.google.com/uc?id=1eGAsTN1HBpJAkeVM57_C7ccp7hbgSz3_&export=download

TaipeiSansTCBeta-Regular.ttf'

"""

print("matplotlib 25 ------------------------------------------------------------")  # 60個

# 饼图的绘制

# 构造数据
edu = [0.2515,0.3724,0.3336,0.0368,0.0057]
labels = ['中专','大专','本科','硕士','其他']
# 绘制饼图
plt.pie(x = edu, # 绘图数据
labels = labels, # 添加教育水平标签
autopct = '%.1f%%' # 设置百分比的格式，这里保留一位小数
)
# 添加图标题
plt.title('失信用户的教育水平分布')

plt.show()

print("matplotlib 26 ------------------------------------------------------------")  # 60個

# 构造数据
edu = [0.2515,0.3724,0.3336,0.0368,0.0057]
labels = ['中专','大专','本科','硕士','其他']
# 添加修饰的饼图
explode = [0,0.1,0,0,0] # 生成数据，用于突出显示大专学历人群
colors = ['#9999ff','#ff9999','#7777aa','#2442aa','#dd5555'] # 自定义颜色
# 中文乱码和坐标轴负号的处理
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
# 将横、纵坐标轴标准化处理，确保饼图是一个正圆，否则为椭圆
plt.axes(aspect = 'equal')
# 绘制饼图
plt.pie(x = edu, # 绘图数据
explode = explode, # 突出显示大专人群
labels = labels, # 添加教育水平标签
colors = colors, # 设置饼图的自定义填充色
autopct = '%.1f%%', # 设置百分比的格式，这里保留一位小数
pctdistance = 0.8, # 设置百分比标签与圆心的距离
labeldistance = 1.1, # 设置教育水平标签与圆心的距离
startangle = 180, # 设置饼图的初始角度
radius = 1.2, # 设置饼图的半径
counterclock = False, # 是否逆时针，这里设置为顺时针方向
wedgeprops = {'linewidth': 1.5, 'edgecolor':'green'},# 设置饼图内外边界的属性值
textprops = {'fontsize':10, 'color':'black'}, # 设置文本标签的属性值
)
# 添加图标题
plt.title('失信用户的受教育水平分布')

plt.show()

print("matplotlib 27 ------------------------------------------------------------")  # 60個

# 构建序列
data1 = pd.Series({'中专':0.2515,'大专':0.3724,'本科':0.3336,'硕士':0.0368,'其他':0.0057})
print(data1)
data1.name = ''
# 控制饼图为正圆
plt.axes(aspect = 'equal')
# plot方法对序列进行绘图
data1.plot(kind = 'pie', # 选择图形类型
autopct = '%.1f%%', # 饼图中添加数值标签
radius = 1, # 设置饼图的半径
startangle = 180, # 设置饼图的初始角度
counterclock = False, # 将饼图的顺序设置为顺时针方向
title = '失信用户的受教育水平分布', # 为饼图添加标题
wedgeprops = {'linewidth': 1.5, 'edgecolor':'green'}, # 设置饼图内外边界的属性值
textprops = {'fontsize':10, 'color':'black'} # 设置文本标签的属性值
)

plt.show()

print("matplotlib 28 ------------------------------------------------------------")  # 60個

# 一個完全乾淨、空白的figure:
fig1 = plt.figure()

# 增新一個axes（座標軸），以供繪圖和放置資訊:
#axs = fig1.add_subplot(1,1,1) # 1x1的座標軸

# 增新很多個axes，以供繪圖和放置資訊:
#fig1.delaxes( fig1.gca() ) # 順便示範，把剛剛1x1的座標軸刪掉

#fig1 = plt.figure()  # 等價於fig1 = plt.figure(1)
fig2 = plt.figure()  # 等價於fig2 = plt.figure(2)

# 一般的情況下，axes是"hold on"的, 也就是資料不會被覆蓋掉。
# hold on: 好處是一次要輸出一堆函數，可以把圖疊加上去。
# hold off: 可以更新圖的內容，可是全部的資訊會被洗掉（title, legend等）
# 如果要保留這些資訊，可以單獨抓出圖的內容，直接修改：
x = np.linspace(0, 6.28, 100)
y = np.sin(x)

axes = fig2.add_subplot(1,1,1)
axes.set_title('y = sin(x)')

line, = axes.plot(x,y) # 這裡回傳的line就是畫在圖上的資料

# 當發現畫錯想修改，可以對line修改：
line.set_ydata(np.cos(x))

#存圖
#fig2.savefig('./picture.png')

plt.show()

print("matplotlib 29 ------------------------------------------------------------")  # 60個

"""
Matplotlib 繪圖
    Matplotlib有很多種畫法，不同指令也可以達到相同效果 但較好也較全面的姿勢應該是先釐清fig,ax的關係
    step1:設定好fig,ax和subplots數目及figsize
    step2:個別指定每個ax的畫圖種類，例如line plot, bar chart or hist chart…
    step3:個別指定每個ax的屬性，例如label, xlabel, ylabel,xlim,ylim, legend, xticklabels等等
"""

x = np.linspace(0, 6.28, 50)
y1 = np.sin(x)
y2 = np.cos(x)

fig,axs = plt.subplots(2, 2, figsize = (10, 10), sharex = True, sharey = True)

axs[0][0].plot(x, y1, label = 'Sin(x)')
axs[0][1].plot(x, y1, label = 'Sin(x)', linewidth = 4, color = 'black')
axs[1][0].plot(x, y1, label = 'Sin(x)')
axs[1][1].plot(x, y1, label = 'Sin(x)')
axs[0][0].set_title('(0, 0)')
axs[0][1].set_title('(0, 1)')
axs[1][0].set_title('(1, 0)')
axs[1][1].set_title('(1, 1)')
axs[0][0].set_xlabel('x_label0')
axs[0][1].set_xlabel('x_label1')
axs[1][0].set_xlabel('x_label2')
axs[1][1].set_xlabel('x_label3')
axs[0][0].set_ylabel('y_label0')
axs[0][1].set_ylabel('y_label1')
axs[1][0].set_ylabel('y_label2')
axs[1][1].set_ylabel('y_label3')
#axs[1][0].set_xticklabels(labels = x, rotation = 45)
#axs[1][1].set_xticklabels(labels = x, rotation = 45)
axs[0][0].grid(True)
# axs[0][0].legend(['legend'], loc = 2)
axs[0][0].plot(x, y2, label = 'Cos(x)', marker = 'x', markersize = 5, color = 'r')
axs[0][0].legend(loc = 3)
axs[0][0].set_ylim(-1.2, 1.2)

fig.suptitle('Suptitle')

plt.show()

print("matplotlib 30 ------------------------------------------------------------")  # 60個

from matplotlib import pyplot as plt

X = np.linspace(-np.pi, np.pi, 200, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.figure(figsize=(20, 6), dpi=80)
plt.subplot(1, 2, 1)
# 使用默认设置画出余弦曲线
plt.plot(X, C)
# 使用默认设置画出正弦曲线
plt.plot(X, S)

plt.subplot(1, 2, 2)
# 移动坐标轴边线
# 坐标轴总共有四个连线，我们通过设置透明色隐藏上方和右方的边线
# 通过 set_position() 移动左侧和下侧的边线
# 通过 set_ticks_position() 设置坐标轴的刻度线的显示位置
ax = plt.gca()  # gca 代表当前坐标轴，即 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
# 设置坐标刻度的字体大小，增加半透明背景
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))
    
# 设置坐标轴的长度
plt.xlim(X.min() * 1.1, X.max() * 1.1)
plt.ylim(C.min() * 1.1, C.max() * 1.1)

# 设置坐标轴的刻度和标签
plt.xticks((-np.pi, -np.pi/2, np.pi/2, np.pi),
          label=(r'$-\pi$', r'$-\pi/2$', r'$+\pi/2$', r'$+\pi$'))
plt.yticks([-1, -0.5, 0, 0.5, 1])


# 画出余弦曲线，并设置线条颜色，宽度，样式
plt.plot(X, C, color="blue", linewidth=2.0, linestyle="-")
# 画出正弦曲线，并设置线条颜色，宽度，样式
plt.plot(X, S, color="red", linewidth=2.0, linestyle="-")

# 在左上角添加铭牌
plt.legend(loc='upper left')

# 在坐标轴上标示相应的点
t = 2 * np.pi / 3
# 画出 cos(t) 所在的点在 X 轴上的位置，即画出 (t, 0) -> (t, cos(t)) 线段，使用虚线
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=1.5, linestyle="--")
# 画出标示的坐标点，即在 (t, cos(t)) 处画一个大小为 50 的蓝色点
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')
# 画出标示点的值，即 cos(t) 的值
plt.annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
# 画出 sin(t) 所在的点在 X 轴上的位置，即画出 (t, 0) -> (t, sin(t)) 线段，使用虚线
plt.plot([t, t],[0, np.sin(t)], color='red', linewidth=1.5, linestyle="--")
# 画出标示的坐标点，即在 (t, sin(t)) 处画一个大小为 50 的红色点
plt.scatter([t, ],[np.sin(t), ], 50, color='red')
# 画出标示点的值，即 sin(t) 的值
plt.annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

# 把结果显示在屏幕上
plt.show()

print("matplotlib 31 ------------------------------------------------------------")  # 60個

def tickline():
    plt.xlim(0, 10), plt.ylim(-1, 1), plt.yticks([])
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(16)
    ax.plot(np.arange(11), np.zeros(11))
    return ax

locators = [
                'plt.NullLocator()',
                'plt.MultipleLocator(base=1.0)',
                'plt.FixedLocator(locs=[0, 2, 8, 9, 10])',
                'plt.IndexLocator(base=3, offset=1)',
                'plt.LinearLocator(numticks=5)',
                'plt.LogLocator(base=2, subs=[1.0])',
                'plt.MaxNLocator(nbins=3, steps=[1, 3, 5, 7, 9, 10])',
                'plt.AutoLocator()',
            ]

n_locators = len(locators)

size = 1024, 60 * n_locators
dpi = 72.0
figsize = size[0] / float(dpi), size[1] / float(dpi)
fig = plt.figure(figsize=figsize, dpi=dpi)
fig.patch.set_alpha(0)


for i, locator in enumerate(locators):
    plt.subplot(n_locators, 1, i + 1)
    ax = tickline()
    ax.xaxis.set_major_locator(eval(locator))
    plt.text(5, 0.3, locator[3:], ha='center', size=16)

plt.subplots_adjust(bottom=.01, top=.99, left=.01, right=.99)
plt.show()

print("matplotlib 32 ------------------------------------------------------------")  # 60個

def plt_bar():
    n = 12
    X = np.arange(n)
    Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

    plt.subplot(1, 2, 1)
    plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
    plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

    for x, y in zip(X, Y1):
        plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va= 'bottom')

    for x, y in zip(X, Y2):
        plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va= 'top')

    plt.xlim(-.5, n)
    plt.xticks(())
    plt.ylim(-1.25, 1.25)
    plt.yticks(())

def plt_contour():
    def f(x,y):
        return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

    n = 256
    x = np.linspace(-3, 3, n)
    y = np.linspace(-3, 3, n)
    X,Y = np.meshgrid(x, y)

    plt.subplot(1, 2, 2)

    plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)
    C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
    plt.clabel(C, inline=1, fontsize=10)

    plt.xticks(())
    plt.yticks(())
    
plt.figure(figsize=(16, 6))
plt_bar()
plt_contour()
plt.tight_layout()

plt.show()

print("matplotlib 33 ------------------------------------------------------------")  # 60個

def plt_imshow():
    def f(x, y):
        return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

    plt.subplot(1, 2, 1)
    n = 10
    x = np.linspace(-3, 3, 4 * n)
    y = np.linspace(-3, 3, 3 * n)
    X, Y = np.meshgrid(x, y)
    #plt.imshow(f(X, Y), cmap='hot', origin='low')
    plt.imshow(f(X, Y), cmap='hot')
    plt.colorbar(shrink=.83)

    plt.xticks(())
    plt.yticks(())
    
def plt_pie():
    plt.subplot(1, 2, 2)
    n = 20
    Z = np.ones(n)
    Z[-1] *= 2
    
    plt.pie(Z, explode=Z*.05, colors = ['%f' % (i/float(n)) for i in range(n)])
    plt.axis('equal')
    plt.xticks(())
    plt.yticks()
    
plt.figure(figsize=(16, 6))
plt_imshow()
plt_pie()
plt.tight_layout()
plt.show()

print("matplotlib 34 ------------------------------------------------------------")  # 60個

def plt_grid():
    ax = plt.subplot(1, 2, 1)
    
    ax.set_xlim(0,4)
    ax.set_ylim(0,3)
    ax.xaxis.set_major_locator(plt.MultipleLocator(1.0))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(0.1))
    ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))
    ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
    ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
    ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
    ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    
def plt_polar():
    ax = plt.subplot(1, 2, 2, polar=True)
    
    N = 20
    theta = np.arange(0.0, 2 * np.pi, 2 * np.pi / N)
    radii = 10 * np.random.rand(N)
    width = np.pi / 4 * np.random.rand(N)
    bars = plt.bar(theta, radii, width=width, bottom=0.0)

    for r,bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.jet(r/10.))
        bar.set_alpha(0.5)

    ax.set_xticklabels([])
    ax.set_yticklabels([])
    
plt.figure(figsize=(16, 6))
plt_grid()
plt_polar()
plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



