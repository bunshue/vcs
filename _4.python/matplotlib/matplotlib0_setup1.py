"""
plt之基本設定
plt之基本設定 座標軸設定

"""

print("------------------------------------------------------------")  # 60個

# 共同
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
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="plot 集合 1 函數曲線",
    figsize=(8, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

offset = 0.3

# x = np.linspace(-10, 10, 51)
# y00 = x ** 2

x = np.linspace(-2 * np.pi, 2 * np.pi, 51)
y00 = np.cos(x)

y01 = y00 + offset * 1
y02 = y00 + offset * 2
y03 = y00 + offset * 3
y04 = y00 + offset * 4
y05 = y00 + offset * 5
y06 = y00 + offset * 6
y07 = y00 + offset * 7
y08 = y00 + offset * 8
y09 = y00 + offset * 9
y10 = y00 + offset * 10
y11 = y00 + offset * 11
y12 = y00 + offset * 12
y13 = y00 + offset * 13
y14 = y00 + offset * 14
y15 = y00 + offset * 15
y16 = y00 + offset * 16
y17 = y00 + offset * 17
y18 = y00 + offset * 18
y19 = y00 + offset * 19
y20 = y00 + offset * 20

plt.plot(x, y01, "r-o", lw=1, markevery=5)  # 隔 5 個畫一個 marker
plt.plot(x, y02, "g--")
plt.plot(x, y03, "b:o")
plt.plot(x, y04, "g--s")
plt.plot(x, y05, "g.-")
plt.plot(x, y06, "y--o")
# plt.plot(x, y07, 'y--o')
plt.plot(x, y07, c="#00a676", lw=5)
# plt.plot(x, y08, marker = 'o')
plt.plot(x, y08, lw=3, marker="o", ms=10)
plt.plot(x, y09, lw=3, marker="o", ms=10, markevery=4)  # 隔 5 個畫一個 marker

# 連線
plt.plot(x, y10, color="red")

# linestyle 虛線樣式
plt.plot(x, y11, color="red", linestyle="--")

# linestyle 虛點樣式
plt.plot(x, y12, color="red", linestyle="-.")

# linestyle 虛點樣式「:」
plt.plot(x, y13, color="red", linestyle=":")

# marker 點「.」標記
# 因為需要展示出效果，因此把 linestyle 設為實線，linewidth 為 2.0，markersize 設為 8
plt.plot(x, y14, color="red", linestyle="-", linewidth="2", markersize="8", marker=".")

# marker 圓「o」標記
plt.plot(x, y15, color="red", linestyle="-", linewidth="2", markersize="8", marker="o")

# marker 星「*」標記
plt.plot(x, y16, color="red", linestyle="-", linewidth="2", markersize="8", marker="*")

# marker 矩形「s」標記
plt.plot(x, y17, color="red", linestyle="-", linewidth="2", markersize="8", marker="s")

plt.plot(
    x,
    y18,
    color="red",
    linestyle="-",
    linewidth="2",
    markersize="8",
    marker=".",
    label="Test",
)

# 繪製折線圖，顏色「紅色」，線條樣式「-」，線條寬度「2」，標記大小「16」，標記樣式「.」，圖例名稱「Plot 1」
plt.plot(
    x,
    y19,
    color="red",
    linestyle="-",
    linewidth="2",
    markersize="8",
    marker=".",
    label="Plot 1",
)

# 繪製折線圖，顏色「藍色」，線條樣式「-」，線條寬度「2」，標記大小「16」，標記樣式「.」，圖例名稱「Plot 2」
plt.plot(
    x,
    y20,
    color="blue",
    linestyle="-",
    linewidth="2",
    markersize="8",
    marker=".",
    label="Plot 2",
)

plt.title(label="圖形標題", fontsize=18, color="r")  # 設定圖表標題內容及大小及顏色

plt.xlabel("x軸標記")
plt.xlabel("x軸標記", fontsize=10)  # 設定 x 軸標題內容及大小

plt.ylabel("y軸標記")
plt.ylabel("y軸標記", fontsize=10)  # 設定 y 軸標題內容及大小

print("標示x軸刻度記號")
plt.xticks(
    [
        -2 * np.pi,
        -3 * np.pi / 2,
        -np.pi,
        -np.pi / 2,
        0,
        np.pi / 2,
        np.pi,
        3 * np.pi / 2,
        2 * np.pi,
    ],
    [
        "$-2\pi$",
        "$-3\pi/2$",
        "$-\pi$",
        "$-\pi/2$",
        "$0$",
        "$\pi/2$",
        "$\pi$",
        "$3\pi/2$",
        "$2\pi$",
    ],
)

"""
# 圖例設定
# 設定圖例標籤位置 ( best, upper, lower, right,left,center )
plt.legend(loc=0)
plt.legend(loc='upper right')
plt.legend(loc="upper right")
plt.legend(loc="lower center")
plt.legend(loc=6)
plt.legend(loc='best')
"""
plt.legend()

"""
# 格線設定
plt_grid()
plt.grid(True)  #顯示格線
plt.grid(True, linestyle='-.') # 設置背景網格
plt.grid(axis="y")  # 加上y格線
"""
plt.grid(color="0.8")  # 顯示格線

plt.show()

print("------------------------------------------------------------")  # 60個



d01 = [10 for y in range(1, 9)]  # data1線條之y值
d02 = [20 for y in range(1, 9)]  # data2線條之y值
d03 = [30 for y in range(1, 9)]  # data3線條之y值
d04 = [40 for y in range(1, 9)]  # data4線條之y值
d05 = [50 for y in range(1, 9)]  # data5線條之y值
d06 = [60 for y in range(1, 9)]  # data6線條之y值
d07 = [70 for y in range(1, 9)]  # data7線條之y值
d08 = [80 for y in range(1, 9)]  # data8線條之y值
d09 = [90 for y in range(1, 9)]  # data9線條之y值
d10 = [100 for y in range(1, 9)]  # data10線條之y值
d11 = [110 for y in range(1, 9)]  # data11線條之y值
d12 = [120 for y in range(1, 9)]  # data12線條之y值

x = [1, 2, 3, 4, 5, 6, 7, 8]
plt.plot(x, d01, "-1")
plt.plot(x, d02, "-2")
plt.plot(x, d03, "-3")
plt.plot(x, d04, "-4")
plt.plot(x, d05, "-s")
plt.plot(x, d06, "-p")
plt.plot(x, d07, "-*")
plt.plot(x, d08, "-+")
plt.plot(x, d09, "-D")
plt.plot(x, d10, "-d")
plt.plot(x, d11, "-H")
plt.plot(x, d12, "-h")
plt.title("標記符號")


plt.show()

print("------------------------------------------------------------")  # 60個


print("兩Y軸不同刻度, plot + bar")

import matplotlib.gridspec as gridspec

x = np.linspace(0, 6.28, 10)
y = np.sin(x * 2)
y2 = np.sin(x * 2) * np.sin(x * 2) * 10

fig = plt.figure(figsize=(12, 8))  # 圖像大小[英吋]
gs = gridspec.GridSpec(4, 1, figure=fig)
ax = fig.add_subplot()

ax.plot(x, y, marker="", alpha=0.8)
ax.grid(20)

axx = ax.twinx()
axx.bar(
    x,
    y2,
    alpha=0.2,
    label="hold_volume",
    color="pink",
)
ax.set_title("兩Y軸不同刻度 plot + bar", size=20)

plt.show()

print("------------------------------------------------------------")  # 60個

# 舊金山市中心（1991–2020年正常值，1849年至今極端數據）

# 月份 	1月 	2月 	3月 	4月 	5月 	6月 	7月 	8月 	9月 	10月 	11月 	12月 	全年

# 平均高溫 °C
listy1 = [
    14.3,
    15.8,
    16.7,
    17.2,
    17.8,
    19.2,
    19.1,
    19.9,
    21.2,
    21.0,
    17.6,
    14.4,
]  # , 17.8

# 平均低溫 °C
listy2 = [8.1, 8.8, 9.4, 9.8, 10.8, 11.7, 12.4, 13.1, 13.1, 12.4, 10.4, 8.3]  # , 10.7

# 平均降雨量 mm
listy3 = [112, 111, 80, 41, 18, 5.1, 0.25, 1.5, 2.5, 24, 66, 121]  # , 581

# 在同一張圖 畫 兩條曲線
month = np.arange(1, 13)
print(type(month))
print(month)

plt.plot(month, listy1, "r-.s", lw=2, markersize=5, label="平均高溫")
plt.plot(month, listy2, "g-.s", lw=2, markersize=5, label="平均低溫")
plt.plot(month, listy3, "b--*", lw=2, markersize=5, label="平均降雨量")

"""
plt.plot(listx, listy, color = "red", ls = "--")
plt.plot(listx, listy, color = "red", ls = "--")
plt.plot(listx, listy, color = "red", ls = "--")
"""

# 同一個指令畫兩條線
# plt.plot(month, listy1, 'r-.s', month, listy2, 'y-s')

plt.legend()

month_chi = ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"]
plt.xticks(month, month_chi, rotation=45)

plt.xlim(0.5, 12.5)  # x軸顯示邊界
plt.ylim(-10, 150)  # y軸顯示邊界

plt.grid(color="k", ls=":", lw=2, alpha=0.5)  # 畫格點
plt.grid(color="r", linestyle=":", linewidth="1", alpha=0.5)  # 畫格點

plt.show()

print("------------------------------------------------------------")  # 60個

'''
from matplotlib.ticker import MultipleLocator, FuncFormatter

def piformat(x, pos):
    """刻度間距是 1/2 Pi"""
    return r"$\frac{%d\pi}{%d}$" % (int(np.round(x / (np.pi / 2))), 2)


plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot()

ax.plot(x, y, label="sin(x)", color="g", linewidth=3)

# 建立刻度間距 pi/2
ax.xaxis.set_major_locator(MultipleLocator(np.pi / 2))

# 建立刻度標籤
ax.xaxis.set_major_formatter(FuncFormatter(piformat))

plt.title("Sin函數的刻度標籤是數學符號")

plt.grid()

plt.show()

'''
print("------------------------------------------------------------")  # 60個

from math import log2, factorial
from matplotlib import pyplot

offset = 0.3

# x = np.linspace(-10, 10, 51)
# y00 = x ** 2

x = np.linspace(-2 * np.pi, 2 * np.pi, 51)
y00 = np.cos(x)

y01 = y00 + offset * 1
y02 = y00 + offset * 2
y03 = y00 + offset * 3
y04 = y00 + offset * 4
y05 = y00 + offset * 5
y06 = y00 + offset * 6
y07 = y00 + offset * 7
y08 = y00 + offset * 8
y09 = y00 + offset * 9
y10 = y00 + offset * 10
y11 = y00 + offset * 11
y12 = y00 + offset * 12
y13 = y00 + offset * 13
y14 = y00 + offset * 14
y15 = y00 + offset * 15
y16 = y00 + offset * 16


num = 6
styles = ["r-.", "g-*", "b-o", "y-x", "c-^", "m-+", "k-d"]
legends = ["對數", "線性", "線性對數", "平方", "立方", "幾何級數", "階乘"]
y_datas = [y00, y01, y02, y03, y04, y05, y06]
for index, y_data in enumerate(y_datas):
    pyplot.plot(x, y_data, styles[index])
pyplot.legend(legends)
# pyplot.xticks(np.arange(1, 7, step=1))
# pyplot.yticks(np.arange(0, 751, step=50))

pyplot.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


"""



--- plt.plot 連線樣式 -------------------------------------------------------------

plt.plot(x, y, color='r', linestyle='--')
plt.plot(x, y, color='red', lw='2.0', ls='--', label='label')

plt.plot(x, y, 'go-')
plt.plot(x, y, 'm.-')

plt.plot(x, y, '-*')
plt.plot(x, y, 'm-o')                      

plt.plot(x, y, 'r-.s')
plt.plot(x, y, 'y-s')
plt.plot(x, y, 'r:o')
plt.plot(x, y, 'g--o')
plt.plot(x, y, 'b:o')
plt.plot(x, y, 'y--o')

plt.plot(x, y, '-go')
plt.plot(x, y, '-x')
plt.plot(x, y, '-*')
plt.plot(x, y, '-o')
plt.plot(x, y, '-^')
plt.plot(x, y, '-s')
plt.plot(x, y, '-v')
plt.plot(x, y, 'bo')                  # 繪製 sine wave
plt.plot(x, y, color=('#00ffff'))  # 設定青色cyan            
plt.plot(x, y, color=('#ff0000'))  # 設定紅色red
plt.plot(x, y, color=((0/255,255/255,255/255)))  # 設定青色cyan            
plt.plot(x, y, color=((255/255,0/255,0/255)))    # 設定紅色red
plt.plot(x, y, color=((0/255,255/255,255/255,0.8)))  # 青色,透明度0.8            
plt.plot(x, y, color=((255/255,0/255,0/255,0.2)))    # 紅色,透明度0.2
plt.plot(x, y, color=('0.9'))      # 設定灰階0.9            
plt.plot(x, y, color=('0.3'))      # 設定灰階0.3
plt.plot(x, y, linestyle = 'solid')       # 預設實線
plt.plot(x, y, linestyle = 'dotted')      # 虛點樣式
plt.plot(x, y, ls = 'dashed')             # 虛線樣式
plt.plot(x, y, ls = 'dashdot')            # 虛線點樣式
plt.plot(x, y, '-')                       # 預設實線
plt.plot(x, y, ':')                       # 虛點樣式
plt.plot(x, y, '--')                      # 虛線樣式
plt.plot(x, y, '-.')                      # 虛線點樣式

plt.plot(seq,d1,'-x',seq, d2,'-o',seq,d3,'-^',seq,d4,'-s')   
plt.plot(seq,d1,'g-',seq, d2,'r:',seq,d3,'y--',seq,d4,'k-.')   

#plt.plot(seq,data1,'g--',seq,data2,'r-.',seq,data3,'y:',seq,data4,'k.')   
#plt.plot(seq,data1,'-*',seq,data2,'-o',seq,data3,'-^',seq,data4,'-s')   
#plt.plot(seq, Benz, '-*', seq, BMW, '-o', seq, Lexus, '-^')   

plt.plot(seq, Benz, '-*', seq, BMW, '-o', seq, Lexus, '-^')   

plt.plot(seq, Benz, '-*', label='Benz')
plt.plot(seq, BMW, '-o', label='BMW')
plt.plot(seq, Lexus, '-^', label='Lexus')

plt.plot(x, y, 'go-')
plt.plot(1,0,'bo')                  # 輸出藍點


marker 可以設的參數
marker 	marker 的風格
markeredgecolor (mec) 	邊線顏色
markeredgewidth (mew) 	邊線寬度
markerfacecolor (mfc) 	marker 的顏色
markerfacecoloralt (mfcalt) 	marker 替換色
markersize (ms) 	marker 大小
markevery 	隔多少畫一個 marker



-- 	dash
-. 	點 + dash
: 	點點
o 	大點點
^ 	三角
s 	方塊


alpha 	透明度
color (c) 	顏色
linestyle (ls) 	線條風格
linewidth (lw) 	線寬

marker 	marker 的風格
markeredgecolor (mec) 	邊線顏色
markeredgewidth (mew) 	邊線寬度
markerfacecolor (mfc) 	marker 的顏色
markerfacecoloralt (mfcalt) 	marker 替換色
markersize (ms) 	marker 大小
markevery 	隔多少畫一個 marker

plt.plot(x, y, c='#6b8fb4', lw=5, mfc='#fffa7c', mec="#084c61", mew=3, ms=20)

plt.plot(x, y, lw=3, ms=10)

plt.plot(x, y, lw=3, label='$\sin$')
plt.plot(x, np.cos(x), lw=3, label='$\cos$')

plt.plot(year, city1, 'r-.s', lw=2, ms=10, label="台北")
plt.plot(year, city2, 'g--*', lw=2, ms=10, label="台中")

year = [2016,2017,2018,2019,2020]
city1 = [100,180,90,220,150]
plt.plot(year, city1, 'r-.s', lw=2, ms=10, label="Taipei")
city2 = [160,50,120,140,110]
plt.plot(year, city2, 'g--*', lw=2, ms=10, label="Kaohsiung")

-----

year = [2016,2017,2018,2019,2020]
city1 = [100,180,90,220,150]
plt.plot(year, city1, 'r-.s', lw=2, ms=10, label="台北")
city2 = [160,50,120,140,110]
plt.plot(year, city2, 'g--*', lw=2, ms=10, label="高雄")

--- plt.savefig 存圖命令 -------------------------------------------------------------

plt.savefig 必須寫在 show()之前

plt.savefig('filename.jpg')
plt.savefig('filename.bmp')
plt.savefig('filename.png')
plt.savefig('filename.svg')
plt.savefig("filename.jpg", dpi=300)
plt.savefig('filename.png', format='png', dpi=200)
plt.savefig(fname = 'filename.png', format = "png")
plt.savefig('filename.png', format='png', transparent=True, dpi=300, pad_inches = 0)    #指定分辨率

fig.savefig('./picture.png')

欲刪除圖表四周的空白, 加 bbox_inches='tight'
plt.savefig('myBayes.png', bbox_inches='tight')

filename = "astro" + str(img)
fig.savefig(filename, bbox_inches='tight')

plt.savefig('out1_14.jpg', bbox_inches='tight')

也可以直接寫 不用plt.
savefig("Weight Growth of RN First Rate Line-of-Battle Ships 1630-1875.svg")

--- plt.text 寫字 -------------------------------------------------------------



--- plt.grid 格線 -------------------------------------------------------------

plt.grid()                          # 顯示XY格線
plt.grid(axis='x')                  # 顯示X格線
plt.grid(axis='y')                  # 顯示Y格線

plt.grid(color='black', linestyle=":", linewidth='1', alpha=0.5)
plt.grid(color='k', ls=':', lw=1, alpha=0.5)
plt.grid(color='k', ls=':', lw=1, alpha=0.5)


--- plt.legend 圖例 -------------------------------------------------------------

plt.plot(x, y, label = "$sin(x)$", color = 'red', lw = 2)
plt.plot(x, z, label = "$cos(x^2)$", color = 'b')
plt.legend()

plt.plot(x, y1, label = "$sin(x)$", color = "red", linewidth = 2)
plt.plot(x, y2, "b--", label = "$cos(x^2)$")
plt.legend()

plt.legend(loc = 6)
plt.legend(loc = 'upper left', bbox_to_anchor = (1,1))
plt.legend(loc = 6, bbox_to_anchor = (1,1))

plt.tight_layout(pad = 7)

plt.legend()
plt.legend(loc=4)	#  用 `loc` 去設圖例的位置, 依 1, 2, 3, ... 表示。

plt.legend(bbox_to_anchor=(1,1))
plt.tight_layout(pad=7)

plt.legend(bbox_to_anchor=(1,1),title='圖例說明')
plt.tight_layout(pad=7)

plt.legend(loc='center left',shadow=True)

#plt.legend(bbox_to_anchor=(1,1))

#plt.legend(loc='upper right')

#plt.legend(loc='center left')

plt.legend(loc='center left',frameon=False)

plt.legend(loc=6,edgecolor='b',facecolor='y')


plt.plot(xpt, ypt1, '-o', label="O(1)")                  
plt.plot(xpt, ypt2, '-o', label="O(logn)")                  
plt.plot(xpt, ypt3, '-o', label="O(n)")
plt.plot(xpt, ypt4, '-o', label="O(nlogn)")
plt.plot(xpt, ypt5, '-o', label="O(n*n)")
plt.legend(loc="best")                      # 建立圖例



--- plt.title 標題 -------------------------------------------------------------

plt.title('振幅越來越小的 $\sin$')

myfont = matplotlib.font_manager.FontProperties(fname = font_filename)
plt.xlabel(u'橫座標', fontproperties = myfont)
plt.ylabel(u'縱座標', fontproperties = myfont)
plt.title(u'三角函數', fontproperties = myfont)

plt.title('Euler Number',fontsize=24,loc='left',color='b', fontweight='bold',fontstyle='italic')

plt.title('Euler Number',fontsize=24,loc='left',color='b', fontweight='bold')

plt.title('Euler Number',fontsize=24,loc='left',color='b')

plt.title(r'衰減數列 cos($3\pi x * e^{x})$',fontsize=20)

plt.title(r'$\frac{7}{9}+\sqrt{7}+\alpha\beta$',fontsize=20)

--- plt.subplot 子圖 -------------------------------------------------------------

plt.subplot(2,2,1)  #四格佔1格
plt.subplot(2,2,2)  #四格佔1格
plt.subplot(2,1,2)  #二格佔1格 = 四格佔2格


--- plt.xticks plt.yticks 刻度 -------------------------------------------------------------

labels = ['Sunday','Monday','Tuesday','Wednesday',
          'Thursday','Friday','Saturday']
plt.xticks(week,labels)

----------------------------------------------------------------

plt.xticks([i for i in range(len(chi))],
           ['平時考1', '平時考2', '平時考3', '平時考4', '平時考5', '期中考', '期末考'])

----------------------------------------------------------------

width = 0.45                    # 長條圖寬度
plt.bar(x, votes, width)        # 繪製長條圖, width = 寬度

plt.xticks(x, ('James', 'Peter', 'Norton'))
plt.yticks(np.arange(0, 450, 30))

----------------------------------------------------------------

width = 0.35                    # 長條圖寬度
plt.bar(x, votes, width)        # 繪製長條圖

plt.xticks(x, ('James', 'Peter', 'Norton'))#參數是tuple
plt.yticks(np.arange(0, 450, 30))

----------------------------------------------------------------

seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)

seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)                         # 設定x軸刻度

seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)                         # 設定x軸刻度

year = [2016,2017,2018,2019,2020]

plt.xticks(year)

plt.xticks([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi], 
           [r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$'])


plt.tick_params(axis = 'both', labelsize = 16, color = 'red')#xy軸多加tick
#plt.tick_params(axis = 'y', color = 'red')#y軸多加tick

plt.xlabel('日期',loc="left")         # 靠左對齊
plt.ylabel('溫度',loc="bottom")       # 靠下對齊


---- plt.axis ------------------------------------------------------------


axis axes xlim ylim

#plt.axis('equal')       #軸比例
#xmin, xmax, ymin, ymax = 0.5, 6.5, 15, 32.5
#plt.axis([xmin, xmax, ymin, ymax])  #設定各軸顯示範圍
#plt.axis([0.5, 6.5, 15, 35])
#plt.axes([0.2, 0.2, 0.4, 0.4]) #設定各軸顯示範圍, 參數是串列

#設定 x, y 軸座標範圍
#plt.xlim(0, 30) # 設定 x 軸座標範圍
#plt.ylim(0, 50) # 設定 y 軸座標範圍
#邊界的設定
#plt.xlim(-6,6)
#plt.ylim(-1.2,1.2)

#print(plt.axis())

#plt.axis('off') #座標軸關閉

xmin, xmax, ymin, ymax = plt.axis()
print(f"xmin = {xmin}")
print(f"xmax = {xmax}")
print(f"ymin = {ymin}")
print(f"ymax = {ymax}")


xmin, xmax = plt.xlim()
ymin, ymax = plt.ylim()
print(f"xmin = {xmin}")
print(f"xmax = {xmax}")
print(f"ymin = {ymin}")
print(f"ymax = {ymax}")








調整x軸刻度 1
week = [0,1,2,3,4,5,6]
labels = ['Sunday','Monday','Tuesday','Wednesday',
          'Thursday','Friday','Saturday']

plt.xticks(week,labels,rotation=30) #字體加旋轉


調整x軸刻度 2
year = [2015,2016,2017,2018,2019]
plt.xticks(year)

調整x軸刻度 3
x = [0.5,1.0,10,50,100]
labels = ['A','B','C','D','E']
plt.xticks(x,labels)

調整x軸刻度 4
x = [0.5,1.0,10,50,100]
value = range(len(x))
plt.xticks(value,x)

調整x軸刻度 5
plt.xticks(np.arange(0,7,step=0.5)) # 設定x軸刻度為0 ~ 6.5, 每隔0.5
plt.yticks(np.arange(-1,1.5,step=0.5))


plt.xticks(np.arange(0,7,step=0.5),color='b')
plt.yticks(np.arange(-1,1.5,step=0.5),color='g')


調整x軸刻度 6
x = [0.5,1.0,10,50,100]
value = range(len(x))
plt.xticks(value,x)

調整x軸刻度 7




plt.rcParams['xtick.labelsize'] = 34	X軸刻度的文字大小
plt.rcParams['ytick.labelsize'] = 16	Y軸刻度的文字大小


print('x軸刻度設定')
plt.tick_params(axis='x',direction='in',color='b')
print('y軸刻度設定')
plt.tick_params(axis='y',length=10,direction='inout',color='g')

plt.tick_params(axis='both',length=10,direction='inout',color='r')



locs, the_labels = plt.xticks()         # 回傳位置與標籤字串
print(f'locs       = {locs}')
print(f'the_labels = {the_labels}')



font1 = {'family':'Old English Text MT',
        'color':'blue',
        'weight':'bold',
        'size':20}
font2 = {'family':'Old English Text MT',
        'color':'green',
        'weight':'normal',
        'size':12}

print('文字顯示不同字型')
plt.title('Sin and Cos function',fontdict=font1)
plt.xlabel('x-value',fontdict=font2)
plt.ylabel('y-value',fontdict=font2)

plt.title(r'$H_{2}O$')
plt.title(r'$\pi r^{2}$')
plt.title(r'$\binom{7}{9}$',fontsize=20)
plt.title(r'${2}\pi > {5}x$')
plt.title(r'${2}\pi$')
plt.title(r'$\pi$')
plt.title(r'$\genfrac{}{}{0}{}{7}{9}$',fontsize=20)
plt.title(r'$\frac{7}{9}$', fontsize=20)
plt.title(r'$\frac{7-\frac{3}{2x}}{9}$',fontsize=20)
plt.title(r'$\Omega \/vs\/ \Delta$',fontsize=20)
plt.title(r'$(\frac{7-\frac{3}{2x}}{9})$',fontsize=20)
plt.title(r'$\left(\frac{7-\frac{3}{2x}}{9}\right)$',fontsize=20)
plt.title(r'$\sqrt{7}$',fontsize=20)
plt.title(r'$\sqrt[3]{a}$',fontsize=20)
plt.title(r'$\sum_{i=0}^\infty x_i$',fontsize=20)
plt.tight_layout()
plt.title(r'$\alpha^2 > \beta_i$',fontsize=20)
plt.title(r'$\Omega vs \Delta$',fontsize=20)
plt.title(r'$\Omega \quad vs \quad \Delta$',fontsize=20)
plt.title(r'$y(t) = \mathcal{A}\mathrm{cos}(2\pi \omega t)$',fontsize=20)
plt.rcParams["mathtext.default"] = 'regular'
plt.title(r'$y(t) = \mathcal{A}\mathrm{cos}(2\pi \omega t)$',fontsize=20)
plt.title(r'$y(t) = \mathcal{A}\/\mathrm{cos}(2\pi \omega t)$',fontsize=20)
plt.rcParams["mathtext.fontset"] = "dejavusans"
plt.title(r'$y(t) = A\/\cos(2\pi \omega t)$',fontsize=20)
plt.rcParams["mathtext.fontset"] = "dejavuserif"
plt.title(r'$y(t) = A\/\cos(2\pi \omega t)$',fontsize=20)
plt.rcParams["mathtext.fontset"] = "cm"
plt.title(r'$y(t) = A\/\cos(2\pi \omega t)$',fontsize=20)
#plt.rcParams["mathtext.fontset"] = "stix"
plt.title(r'$y(t) = A\/\cos(2\pi \omega t)$',fontsize=20)
#plt.rcParams["mathtext.fontset"] = "stixsans"
plt.title(r'$y(t) = A\/\cos(2\pi \omega t)$',fontsize=20)



plot 參數
plt.tick_params(axis='both', labelsize=12, color='red')

plt.plot(seq, data1, 'g--', seq, data2, 'r-.', seq, data3, 'y:', seq, data4, 'k.')   
plt.plot(seq, data1, '-*', seq, data2, '-o', seq, data3, '-^', seq, data4, '-s')   
plt.plot(seq, Benz, '-*', seq, BMW, '-o', seq, Lexus, '-^')   

seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)                         # 設定x軸刻度

plt.plot(seq, Benz, '-*', seq, BMW, '-o', seq, Lexus, '-^')   

plt.plot(x, y, label="$sin(x)$", color='red', lw=2)
plt.plot(x, z, label="$cos(x^2)$", color='b')

plt.plot(x, y, c='#6b8fb4', lw=5, mfc='#fffa7c', mec="#084c61", mew=3, ms=20)

plt.plot(x, np.sin(x), c = '#7fb069', lw = 3)
plt.scatter(x, np.random.randn(100), c = '#daa73e', s = 50, alpha = 0.5)
plt.bar(range(10), np.random.randint(1, 30, 10), fc = '#e55934')

plt.plot(x, y, c='#6b8fb4', lw=5, mfc='#fffa7c', mec="#084c61", mew=3, ms=20)

我們現在隔 10 個畫一個 marker 試試。
plt.plot(x, y, lw=3, marker='o', ms=10, markevery=10)

plt.plot(x, y, '-', marker='x')
plt.plot(x, y, '-', marker='o')
plt.plot(x, y, '-', marker='^')
plt.plot(x, y, '-', marker='s') 


# 指定 寬6.4inches, 高4.8inches, 160dpi
plt.figure(figsize=(6.4, 4.8), dpi=160)



"""
