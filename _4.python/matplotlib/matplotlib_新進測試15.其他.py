# matplotlib_新進測試14_其他

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個


import os
import time
import random

print("------------------------------------------------------------")  # 60個






print("------------------------------------------------------------")  # 60個

print("寫字")
#                      H對齊方式       V對齊方式
my_kwargs = dict(ha="center", va="center", fontsize=30, c="b")
my_kwargs = dict(ha="left", va="top", fontsize=30, c="b")
x_st = 0
y_st = 17.5
text = "歡迎來到美國"
plt.text(x_st, y_st, text, **my_kwargs)
plt.plot(x_st, y_st, "r-o")  # 畫基準點

plt.show()

print("------------------------------------------------------------")  # 60個

print("從windows字型中找出可以顯示的中文字型")
import matplotlib as mpl
zhfont = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/mingliu.ttc')
plt.text(0, 0, u'測試一下 ', fontsize=20, fontproperties=zhfont)


plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
plt.rcParams['axes.unicode_minus'] = False

plt.text(0.5, 0.5, u'測試一下')

plt.show()

print("------------------------------------------------------------")  # 60個

#文字顯示問題

from os import path
from matplotlib.font_manager import fontManager

"""
print('顯示所有字型')
for i in fontManager.ttflist:
    print(i.fname, i.name)
"""

print("------------------------------------------------------------")  # 60個


plt.figure(figsize=(18, 4))
plt.subplot(2, 2, 1)
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'subplot(2,2,1)', ha='center', va='center',
        size=20, alpha=.5)

plt.subplot(2, 2, 2)
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'subplot(2,2,2)', ha='center', va='center',
        size=20, alpha=.5)

plt.subplot(2, 2, 3)
plt.xticks(())
plt.yticks(())

plt.text(0.5, 0.5, 'subplot(2,2,3)', ha='center', va='center',
        size=20, alpha=.5)

plt.subplot(2, 2, 4)
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'subplot(2,2,4)', ha='center', va='center',
        size=20, alpha=.5)

plt.tight_layout()
plt.show()


print("------------------------------------------------------------")  # 60個


import matplotlib.gridspec as gridspec

plt.figure(figsize=(18, 4))
G = gridspec.GridSpec(3, 3)

axes_1 = plt.subplot(G[0, :])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 1', ha='center', va='center', size=24, alpha=.5)

axes_2 = plt.subplot(G[1:, 0])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 2', ha='center', va='center', size=24, alpha=.5)

axes_3 = plt.subplot(G[1:, -1])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 3', ha='center', va='center', size=24, alpha=.5)

axes_4 = plt.subplot(G[1, -2])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 4', ha='center', va='center', size=24, alpha=.5)

axes_5 = plt.subplot(G[-1, -2])
plt.xticks(())
plt.yticks(())
plt.text(0.5, 0.5, 'Axes 5', ha='center', va='center', size=24, alpha=.5)

plt.tight_layout()
plt.show()


print("------------------------------------------------------------")  # 60個


plt.figure(figsize=(18, 4))

plt.axes([.1, .1, .8, .8])
plt.xticks(())
plt.yticks(())
plt.text(.2, .5, 'axes([0.1, 0.1, .8, .8])', ha='center', va='center',
        size=20, alpha=.5)

plt.axes([.5, .5, .3, .3])
plt.xticks(())
plt.yticks(())
plt.text(.5, .5, 'axes([.5, .5, .3, .3])', ha='center', va='center',
        size=16, alpha=.5)

plt.show()





print("------------------------------------------------------------")  # 60個


# 箱線圖

data = np.random.rand(20, 5) # 生成5個維度數據，每組20個
plt.boxplot(data)

plt.show()

print("------------------------------------------------------------")  # 60個

# 小提琴圖
data = np.random.rand(20, 5)
plt.violinplot(data,showmeans=False,showmedians=True)

plt.show()

print("------------------------------------------------------------")  # 60個

# Matplotlib技巧

import matplotlib

fig = plt.figure(figsize = (6,4), dpi=120) # 設置繪製對象大小
plt.style.use('ggplot') # 設置顯示風格

plt.plot([12,13,45,15,16], label='label1') # 繪圖及設置圖例文字
plt.annotate('local max', xy=(2, 45), xytext=(3, 45),arrowprops=dict(facecolor='black',
    shrink=0.05))  # 繪製帶箭頭的標註
x = np.arange(0, 6)
y = x * x
plt.plot(x, y, marker='o', label='label2') # 繪圖及設置圖例文字
for xy in zip(x, y):
    plt.annotate("(%s,%s)" % xy, xy=xy, xytext=(-20, 10), # 繪製標註
                 textcoords='offset points')
plt.text(4.5, 10, 'Draw text', fontsize=20) # 在位置0,20繪製文字

plt.legend(loc='upper left')  # 在左上角顯示圖例
plt.xlabel("x value")  # 設置x軸上的標籤
plt.ylabel("y value")  # 設置y軸上的標籤
plt.xlim(-0.5,7)  # 設置x軸範圍
plt.ylim(-5,50) # 設置y軸範圍
plt.show()

print(matplotlib.artist.getp(fig.patch))  # 顯示繪製對象的各個屬性值


print("------------------------------------------------------------")  # 60個


plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'
plt.rcParams['font.size']=12

#橫條圖
def diagram_1(s,x):
	plt.barh(x, s)

#圓餅圖
def diagram_2(s,x):	 
	plt.pie(s,labels=x, autopct='%.2f%%')
#折線圖+長條圖

def diagram_4(s,x):
    plt.plot(x, s, marker='.')
    plt.bar(x, s, alpha=0.5)	

#長條圖
def diagram_3(s,x):
	plt.bar(x, s)	

#要繪圖的數據
x = ['高雄','台中','宜蘭','花蓮']
s = [89,58,63,50]

#設定子圖
plt.figure(1, figsize=(8, 8),clear=True)
plt.subplots_adjust(left=0.1, right=0.95)

plt.subplot(221)
diagram_1(s,x)

plt.subplot(222)
diagram_2(s,x)

plt.subplot(223)
diagram_3(s,x)

plt.subplot(2,2,4)
diagram_4(s,x)

plt.show()




print("------------------------------------------------------------")  # 60個


plt.rcParams['font.size']=12

#折線圖
def lineChart(s,x):
    plt.xlabel('城市名稱')
    plt.ylabel('民調原分比')
    plt.title('各種城市喜好度比較')
    plt.plot(x, s, marker='.')

#長條圖
def barChart(s,x):
    plt.xlabel('城市名稱')
    plt.ylabel('民調原分比')
    plt.title('各種城市喜好度比較')
    plt.bar(x, s)

#橫條圖
def barhChart(s,x):
    plt.barh(x, s)

#圓餅圖
def pieChart(s,x):	 
    plt.pie(s,labels=x, autopct='%.2f%%')

#要繪圖的數據
x = ['第一季', '第二季', '第三季', '第四季']
s = [13.2, 20.1, 11.9, 14.2]

#定義子圖
plt.figure(1, figsize=(8, 6),clear=True)
plt.subplots_adjust(left=0.1, right=0.95)

plt.subplot(2,2,1)
pieChart(s,x)

x = ['程式設計概論', '多媒體概論', '計算機概論', '網路概論']
s = [3560, 4000, 4356, 1800]
plt.subplot(2,2,2)
barhChart(s,x)

x = ['新北市', '台北市', '高雄市', '台南市','桃園市','台中市']
s = [0.2, 0.3, 0.15, 0.23,0.19, 0.27]
plt.subplot(223)
lineChart(s,x)

plt.subplot(224)
barChart(s,x)

plt.show()



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

'''

print("箱圖")

# Creating dataset
np.random.seed(10)
data_1 = np.random.normal(100, 10, 200)
data_2 = np.random.normal(90, 20, 200)
data_3 = np.random.normal(80, 30, 200)
data_4 = np.random.normal(70, 40, 200)
data = [data_1, data_2, data_3, data_4]

fig = plt.figure(figsize=(10, 7))

# 圖加軸
ax = fig.add_axes([0, 0, 1, 1])

bp = ax.boxplot(data, labels=["mu = 100", "mu = 90", "mu = 80", "mu = 70"])
ax.set_title("Box plot")

plt.show()

print("------------------------------------------------------------")  # 60個

print("subplot 100張圖")

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

import matplotlib.image as img

# print('使用 matplotlib 顯示一圖')
image = img.imread(filename)

N = 100
for i in range(N):
    plt.subplot(10, N // 10, i + 1)
    plt.imshow(image)

plt.show()

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

# 導出圖表

from io import BytesIO
from lxml import etree
import base64
import webbrowser

data = pd.DataFrame({'id':['1','2','3','4','5'], # 構造數據
                     'math':[90,89,99,78,63],
                     'english':[89,94,80,81,94]})
plt.plot(data['math']) # matplotlib做圖
plt.plot(data['english'])

# 保存圖片（與網頁顯示無關）
plt.savefig('導出圖表.jpg',dpi=300)

# 保存網頁
buffer = BytesIO()
plt.savefig(buffer)  
plot_data = buffer.getvalue()

imb = base64.b64encode(plot_data)  # 生成網頁內容
ims = imb.decode()
imd = "data:image/png;base64,"+ims
data_im = """<h1>Figure</h1>  """ + """<img src="%s">""" % imd   
data_des = """<h1>Describe</h1>"""+data.describe().T.to_html()
root = "<title>Dataset</title>"
root = root + data_des + data_im

html = etree.HTML(root)
tree = etree.ElementTree(html)
tree.write('導出圖表.html')
#使用默認瀏覽器打開 html 文件
webbrowser.open('導出圖表.html',new = 1)
'''
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

