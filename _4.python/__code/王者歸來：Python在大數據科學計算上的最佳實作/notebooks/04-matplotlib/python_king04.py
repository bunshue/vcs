"""



"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
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
'''
x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(8,4)) #❷

plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2) #❸
plt.plot(x,z,"b--",label="$cos(x^2)$") #❹

plt.xlabel("Time(s)") #❺
plt.ylabel("Volt") 
plt.title("PyPlot First Example") 
plt.ylim(-1.2,1.2) 
plt.legend() 

""" NG
import io
buf = io.BytesIO() # 建立一個用來儲存圖形內容的BytesIO物件
plt.savefig(buf, fmt="png") # 將圖形以png格式儲存進buf中
cc = buf.getvalue()[:20] # 顯示圖形內容的前20個位元組
print(cc)
"""

plt.show()

print("------------------------------------------------------------")  # 60個


#面對物件模式繪圖

fig = plt.gcf()
axes = plt.gca()
print(fig, axes)

#Figure(640x320) Axes(0.125,0.1;0.775x0.8)

#組態屬性

#%fig[1x3]=組態繪圖物件的屬性
plt.figure(figsize=(4, 3))
x = np.arange(0, 5, 0.1)
line = plt.plot(x, 0.05*x*x)[0] # plot傳回一個清單
line.set_alpha(0.5) # 呼叫Line2D物件的set_*()方法設定屬性值
plt.show()

print("------------------------------------------------------------")  # 60個

lines = plt.plot(x, np.sin(x), x, np.cos(x))
plt.show()

print("------------------------------------------------------------")  # 60個

print('????')
plt.setp(lines, color="r", linewidth=4.0);
plt.show()

print("------------------------------------------------------------")  # 60個


print(line.get_linewidth())
print(plt.getp(lines[0], "color")) # 傳回color屬性

#2.0
#r

print("------------------------------------------------------------")  # 60個

#繪制多子圖

#%fig[1x2]=在Figure物件中建立多個子圖
for idx, color in enumerate("rgbyck"):
    print(idx, color)
    #plt.subplot(321+idx, axisbg=color)  # NG

plt.show()

print("------------------------------------------------------------")  # 60個

plt.subplot(221) # 第一行的左圖
plt.subplot(222) # 第一行的右圖
plt.subplot(212) # 第二整行;

plt.show()

print("------------------------------------------------------------")  # 60個


#%hide
plt.close("all")

#%fig[1x2]=同時在多幅圖表、多個子圖中進行繪圖
plt.figure(1) # 建立圖表1
plt.figure(2) # 建立圖表2
ax1 = plt.subplot(121) # 在圖表2中建立子圖1
ax2 = plt.subplot(122) # 在圖表2中建立子圖2

x = np.linspace(0, 3, 100)
for i in range(5):
    plt.figure(1)  #❶ 選取圖表1
    plt.plot(x, np.exp(i*x/3))
    plt.sca(ax1)   #❷ 選取圖表2的子圖1
    plt.plot(x, np.sin(i*x))
    plt.sca(ax2)  # 選取圖表2的子圖2
    plt.plot(x, np.cos(i*x))

plt.show()

print("------------------------------------------------------------")  # 60個

#也可以不呼叫sca()指定目前子圖，而直接呼叫ax1和ax2的plot()方法繪圖。

#%nofig
fig, axes = plt.subplots(2, 3)
[a, b, c], [d, e, f] = axes
print(axes.shape)
print(b)

#(2, 3)
#Axes(0.398529,0.536364;0.227941x0.363636)

plt.show()

print("------------------------------------------------------------")  # 60個

#%fig=使用subplot2grid()建立表格佈局

fig = plt.figure(figsize=(6, 6))
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=2)
ax2 = plt.subplot2grid((3, 3), (0, 2), rowspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 0), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 1), colspan=2)
ax5 = plt.subplot2grid((3, 3), (1, 1));
#%hide
for idx, ax in enumerate(fig.axes, 1):
    ax.text(0.5, 0.5, "ax{}".format(idx), ha="center", va="center", fontsize=16)

plt.show()

print("------------------------------------------------------------")  # 60個

#組態檔
import matplotlib

from os import path
path.abspath(matplotlib.get_configdir())

#u'C:\\Users\\RY\\Dropbox\\scipybook2\\settings\\.matplotlib'

path.abspath(matplotlib.matplotlib_fname())

#u'C:\\Users\\RY\\Dropbox\\scipybook2\\settings\\.matplotlib\\matplotlibrc'

print(matplotlib.rc_params())

print(matplotlib.rcParams)

plt.close("all")

matplotlib.rcParams["lines.marker"] = "o"
plt.plot([1,2,3,2])

matplotlib.rc("lines", marker="x", linewidth=2, color="red")

matplotlib.rcdefaults()

matplotlib.rcParams.update( matplotlib.rc_params() )

#透過pyplot模組也可以使用rcParams、rc和rcdefaults。

from matplotlib import style
print(style.available)

#[u'dark_background', u'bmh', u'grayscale', u'ggplot', u'fivethirtyeight']

style.use("ggplot")

#%figonly=使用ggplot型態繪圖
import numpy as np
import matplotlib.pyplot as plt

style.use("ggplot")

plt.close("all")

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(8,4))

plt.plot(x,y,label="$sin(x)$",linewidth=2)
plt.plot(x,z,"--",label="$cos(x^2)$")

plt.xlabel("Time(s)")
plt.ylabel("Volt") 
plt.title("ggplot style") 
plt.ylim(-1.2,1.2) 
plt.legend();

plt.show()

'''
print("------------------------------------------------------------")  # 60個

#在圖表中顯示中文

from matplotlib.font_manager import fontManager

cc = fontManager.ttflist[:6]
print(cc)

print(fontManager.ttflist[0].name)
print(fontManager.ttflist[0].fname)

plt.close("all")

#scpy2/matplotlib/chinese_fonts.py：顯示系統中所有檔案大於1M的TTF字型，請讀者使用該程式查詢電腦中可使用的中文字型名。

#%fig=顯示系統中所有的中文字型名
import os
from os import path

fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(111)
plt.subplots_adjust(0, 0, 1, 1, 0, 0)
plt.xticks([])
plt.yticks([])
x, y = 0.05, 0.05
fonts = [font.name for font in fontManager.ttflist if 
             path.exists(font.fname) and os.stat(font.fname).st_size>1e6] #❶
font = set(fonts)
dy = (1.0 - y) / (len(fonts) // 4 + (len(fonts)%4 != 0))

for font in fonts:
    t = ax.text(x, y + dy / 2, u"中文字型", 
                {'fontname':font, 'fontsize':14}, transform=ax.transAxes) #❷
    ax.text(x, y, font, {'fontsize':12}, transform=ax.transAxes)
    x += 0.25
    if x >= 1.0:
        y += dy
        x = 0.05

plt.show()

print("------------------------------------------------------------")  # 60個

from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14) #❶

t = np.linspace(0, 10, 1000)
y = np.sin(t)
plt.close("all")
plt.plot(t, y)
plt.xlabel(u"時間", fontproperties=font) #❷
plt.ylabel(u"振幅", fontproperties=font)
plt.title(u"正弦波", fontproperties=font)

plt.show()

print("------------------------------------------------------------")  # 60個

from matplotlib.font_manager import _rebuild
_rebuild()

plt.rcParams["font.family"] = "SimHei"
plt.plot([1,2,3])
plt.xlabel(0.5 ,0.5, u"中文字型")

#%hide
#%exec_python -m scpy2.matplotlib.chinese_fonts


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

'''
print("------------------------------------------------------------")  # 60個
plt.savefig("test.png", dpi=120)
    TIP
    若果關閉了圖表視窗，則無法使用savefig()儲存圖形。實際上不需要呼叫show()顯示圖表，可以直接用savefig()將圖表儲存成圖形檔案。使用這種方法可以很容易撰寫批次輸出圖表的程式。



'''
