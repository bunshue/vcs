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
'''
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
import mplfinance as mpf
from matplotlib.ticker import Formatter
from mplfinance.original_flavor import candlestick_ohlc

dfcvs = DataFrame([
    #    時間            開盤, 最高 ,最低, 收盤
    ["2018/09/17-21:34", 3646, 3650, 3644, 3650],
    ["2018/09/17-21:35", 3650, 3650, 3648, 3648],
    ["2018/09/17-21:36", 3650, 3650, 3648, 3650],
    ["2018/09/17-21:37", 3652, 3654, 3648, 3652]
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
candlestick_ohlc(ax, data_mat, colordown = '#53c156', colorup = '#ff1717', width = 0.2, alpha = 1)

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
import matplotlib as mpl
import matplotlib.dates as mdates
#from mplfinance import candlestick_ohlc
from mplfinance.original_flavor import candlestick_ohlc

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
#plt.legend(loc = 'best')                    # 繪制圖例
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

# 時序圖
import matplotlib.dates as mdates

#     2017/0808/2100    2017/0808/2101    2017/0808/2102    2017/0808/2103
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

print("matplotlib 11 ------------------------------------------------------------")  # 60個

"""
正弦函數 s=sin(x) 
餘弦函數 c=cos(x)
"""

x = np.linspace(-2 * np.pi, 2 * np.pi, 100) #共100個點
x = np.linspace(-2 * np.pi, 2 * np.pi)   #預設為50個點
print(len(x))
s, c = np.sin(x), np.cos(x)

#自訂座標軸的刻度及標籤–xticks()、yticks()
#x座標
ticks = [-2*np.pi, -1.5*np.pi, -1*np.pi, -0.5*np.pi, 0, np.pi * 0.5, np.pi, np.pi * 1.5, np.pi * 2]
#要在x座標寫上的標籤
labels = ['-360°', '-270°', '-180°', '-90°', '0°', '90°', '180°', '270°', '360°']
plt.xticks(ticks, labels)

#x軸刻度 5個點 分別用pi表示
#plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi],['-$2\pi$', '-$\pi$','0', '$\pi$', '$2\pi$'])

plt.plot(x, s)
plt.plot(x, c)
plt.grid()

plt.legend(['sin','cos'])
plt.legend(['sin','cos'],loc=3,fontsize='xx-large',edgecolor='y',facecolor='r')

plt.show()

print("matplotlib 13 ------------------------------------------------------------")  # 60個

print('載入字型範例')

"""
翰字鑄造 台北黑體 regular 版本

TaipeiSansTCBeta-Regular.ttf 

https://drive.google.com/uc?id=1eGAsTN1HBpJAkeVM57_C7ccp7hbgSz3_&export=download

TaipeiSansTCBeta-Regular.ttf'

"""

print("matplotlib 14 ------------------------------------------------------------")  # 60個

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

plt.show()

print("matplotlib 15 ------------------------------------------------------------")  # 60個

from matplotlib import pyplot as plt

x = np.linspace(-np.pi, np.pi, 200, endpoint=True)
s, c = np.sin(x), np.cos(x)

plt.figure(figsize=(20, 6), dpi=80)
plt.subplot(1, 2, 1)

# 使用默认设置画出正弦曲线
plt.plot(x, s)
# 使用默认设置画出余弦曲线
plt.plot(x, c)

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
plt.xlim(x.min() * 1.1, x.max() * 1.1)
plt.ylim(c.min() * 1.1, c.max() * 1.1)

# 设置坐标轴的刻度和标签
plt.xticks((-np.pi, -np.pi/2, np.pi/2, np.pi),
          label=(r'$-\pi$', r'$-\pi/2$', r'$+\pi/2$', r'$+\pi$'))
plt.yticks([-1, -0.5, 0, 0.5, 1])

# 画出正弦曲线，并设置线条颜色，宽度，样式
plt.plot(x, s, color="red", linewidth=2.0, linestyle="-")
# 画出余弦曲线，并设置线条颜色，宽度，样式
plt.plot(x, c, color="blue", linewidth=2.0, linestyle="-")

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

print("matplotlib 16 ------------------------------------------------------------")  # 60個

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

print("matplotlib 17 ------------------------------------------------------------")  # 60個

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

print("matplotlib 18 ------------------------------------------------------------")  # 60個

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
plt_polar()
plt.tight_layout()
plt.show()

print("matplotlib 19 ------------------------------------------------------------")  # 60個

#1. 善用 enumerate

L = ['a', 'b', 'c']

for i in L:
    print(i)

#加上編號。

for i in range(3):
    print(i+1, L[i])

#試試 enumerate 會做什麼。

print(list(enumerate(L)))

#用 for 迴圈一一顯示出來。

for i in enumerate(L):
    print(i)

#用 unpacking 取出內容, 再修正編號從 1 開始。

for i, s in enumerate(L):
    print(i + 1, s)

#2. 畫多個圖

x = np.linspace(-10, 10, 200)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()


#用 2×2的排列方式畫圖。

plt.subplot(2, 2, 1)
plt.plot(x, np.sin(x))

plt.subplot(2, 2, 2)
plt.plot(x, np.cos(x))

plt.subplot(2, 2, 3)
plt.plot(x, x)

plt.subplot(2, 2, 4)
plt.plot(x, x**2)

plt.show()

print("matplotlib 20 ------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x)
fig = plt.figure()
ax1 = fig.add_subplot(121,projection='polar')
ax1.plot(x, y)
ax1.set_title("極座標 Sin 圖",fontsize=12)
ax2 = fig.add_subplot(122)
ax2.plot(x, y)
ax2.set_title('一般座標 Sin 圖',fontsize=12)
ax2.set_aspect(2)
plt.tight_layout()                      # 緊縮佈局

plt.show()

print("matplotlib 21 ------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
import numpy as np

def f1(x, y):                                # 左邊曲面函數
    return (np.power(x,2) + np.power(y, 2))
def f2(x, y):                                # 右邊曲面函數
    r = np.sqrt(np.power(x,2) + np.power(y, 2))
    return (np.sin(r))

X = np.arange(-3, 3, 0.1)                   # 曲面 X 區間
Y = np.arange(-3, 3, 0.1)                   # 曲面 Y 區間
X, Y = np.meshgrid(X, Y)                    # 建立 XY 座標
# 建立子圖
fig,ax = plt.subplots(1,2,figsize=(8,4),subplot_kw={'projection':'3d'})
# 左邊子圖乎叫 f1
ax[0].plot_surface(X, Y, f1(X,Y), cmap='hsv')   # 繪製 3D 圖
# 左邊子圖乎叫 f2
ax[1].plot_surface(X, Y, f2(X,Y), cmap='hsv')   # 繪製 3D 圖
plt.show()

print("matplotlib 22 ------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2 * np.pi, 2 * np.pi, 50)

f1 = 3 * np.sin(x)                  # y陣列的變化
f2 = np.sin(x)
f3 = 0.2 * np.sin(x)

plt.plot(x, f1) 
plt.plot(x, f2, '-x')
plt.plot(x, f3)
plt.plot(x, f1, 'go')
plt.show()

print("matplotlib 23 ------------------------------------------------------------")  # 60個

import csv
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

filename = '_data/TaipeiWeatherJan.csv'
with open(filename) as csvFile:
    csvReader = csv.reader(csvFile)
    headerRow = next(csvReader)          # 讀取文件下一列
    highTemps, meanTemps, lowTemps = [], [], []                       
    for row in csvReader:
        highTemps.append(int(row[1]))    # 儲存最高溫
        meanTemps.append(int(row[2]))    # 儲存均溫
        lowTemps.append(int(row[3]))     # 儲存最低溫

seq = range(1,32)
plt.plot(seq,highTemps,seq,meanTemps,seq,lowTemps)

plt.title("2025年1月台北天氣報告", fontsize=24)
plt.xlabel("", fontsize=14)
plt.ylabel(r'溫度 $C^{o}$', fontsize=14)
plt.show()

print("matplotlib 24 ------------------------------------------------------------")  # 60個

import csv
import matplotlib.pyplot as plt
from datetime import datetime

def convert_tw_date_to_ad(tw_date):
    # 分割日期為年、月、日
    year, month, day = map(int, tw_date.split('/'))
    # 將民國年轉換為西元年
    year += 1911
    # 重組日期並返回
    return f"{year}-{month:02d}-{day:02d}"

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
filename = '_data/ST43_3479_202310.csv'
with open(filename) as csvFile:
    csvReader = csv.reader(csvFile)
    for _ in range(5):                              # 跳過前5列
        next(csvReader)
    all_rows = list(csvReader)
    data_without_last_row = all_rows[:-1]           # 跳過最後一列
    
    mydates, openPrices, highPrices, lowPrices, closePrices = [], [], [], [], []   
    
    for row in data_without_last_row:
        try:
            # 將日期轉換為西元年格式
            converted_date = convert_tw_date_to_ad(row[0])
            # 使用 strptime 解析轉換後的日期字串
            parseDate = datetime.strptime(converted_date, "%Y-%m-%d")
            currentDate = parseDate.strftime("%Y-%m-%d") # 轉換後日期
            openPrice = eval(row[3])
            highPrice = eval(row[4])                # 設定最高價
            lowPrice = eval(row[5])                 # 設定最低價
            closePrice = eval(row[6])               # 設定收盤價
        except Exception:
            print(f'有缺值 {row}')
        else:
            openPrices.append(openPrice)            # 儲存開盤價
            highPrices.append(highPrice)            # 儲存最高價
            lowPrices.append(lowPrice)              # 儲存最低價
            closePrices.append(closePrice)          # 儲存收盤價
            mydates.append(currentDate)             # 儲存日期

fig = plt.figure(figsize=(12, 8))                   # 設定繪圖區大小
plt.plot(mydates, openPrices, '-p', label='開盤價')    # 繪製開盤價
plt.plot(mydates, highPrices, '-*', label='最高價')    # 繪製最高價
plt.plot(mydates, lowPrices, '-o', label='最低價')     # 繪製最低價
plt.plot(mydates, closePrices, '-^', label='收盤價')   # 繪製收盤價
plt.legend()
fig.autofmt_xdate()                                 # 日期旋轉
plt.title("2023年10月安勤公司日線圖", fontsize=24)
plt.ylabel('價格', fontsize=14)
plt.show()

print("matplotlib 25 ------------------------------------------------------------")  # 60個
         
data1 = [1, 2, 3, 4, 5, 6, 7, 8]                # data1線條
data2 = [1, 4, 9, 16, 25, 36, 49, 64]           # data2線條
data3 = [1, 3, 6, 10, 15, 21, 28, 36]           # data3線條
data4 = [1, 7, 15, 26, 40, 57, 77, 100]         # data4線條

seq = [1, 2, 3, 4, 5, 6, 7, 8]
plt.plot(seq,data1,'g--',seq,data2,'r-.',seq,data3,'y:',seq,data4,'k.')   
plt.plot(seq,data1,'-*',seq,data2,'-o',seq,data3,'-^',seq,data4,'-s')   

plt.show()

'''
print("matplotlib 26 ------------------------------------------------------------")  # 60個

# 建立衰減數列.
x = np.linspace(0.0, 5.0, 50)
y = np.cos(3 * np.pi * x) * np.exp(-x)

plt.title(r'衰減數列 cos($3\pi x * e^{x})$',fontsize=20)
plt.plot(x, y, 'go-')
plt.ylabel('衰減值')
plt.show()


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個






"""
plt.rcParams["font.family"] = ["Microsoft JhengHei"]



"""


"""
seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)                         # 設定x軸刻度

plt.plot(seq, Benz, '-*', label='Benz')
plt.plot(seq, BMW, '-o', label='BMW')
plt.plot(seq, Lexus, '-^', label='Lexus')
plt.legend()
plt.legend(loc='best')
plt.legend(loc=0)
plt.legend(loc='upper right')
plt.legend(loc=6)
plt.legend(loc='best')
plt.title("Sales Report", fontsize=24)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Number of Sales", fontsize=14)
plt.show()


plt.title('五月份國外旅遊調查表',fontsize=16,color='b')

#plt.plot(x, y, lw=8, ls='-.')
#plt.plot(x, y, marker='*')
#plt.plot(x, y, marker='D',ms=10, mfc='y', mec='r')
#plt.plot(x, y, color='y')
#plt.plot(x, y, color=(1,1,0))  #RGB
#plt.plot(x, y, color='# FFFF00')  #HEX
#plt.plot(x, y, color='yellow')  #英文全名
#plt.plot(x, y, color='0.5')

plt.xticks(range(0,5500,500))
plt.tick_params(axis = 'both', labelsize = 10, color = 'red')
plt.bar(listx, listy, width = 0.5, color = 'r')
plt.barh(listy, listx, height = 0.5, color = 'r')


製作數據
xpt = list(range(1,101))    # 建立1-100序列x座標點
ypt = [x**2 for x in xpt]   # 以x平方方式建立y座標點
ypt = [math.sin(x/10) for x in xpt]   # 以x平方方式建立y座標點

xpt = np.linspace(0, 10, 500)   # 建立含500個元素的陣列
ypt1 = np.sin(xpt)              # y陣列的變化
ypt2 = np.cos(xpt)


x1 = np.linspace(0, 10, num=11)     # 使用linspace()產生陣列
print(type(x1), x1)
x2 = np.arange(0,11,1)              # 使用arange()產生陣列
print(type(x2), x2)
x3 = np.arange(11)                  # 簡化語法產生陣列
print(type(x3), x3)


"""



""" 共同抽出
plt.savefig('tmp_pic.jpg')

#存圖
#fig2.savefig('./picture.png')

plt.grid()
plt.grid()

plt.grid()

plt.grid()
plt_grid()

plt.grid(True)



"""




