# 新進測試03

"""

特殊語法

"""
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

import random
import pandas as pd

print("------------------------------------------------------------")  # 60個

'''
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

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個

#繪製直方圖

plt.subplot(121)
np.random.seed(0)
data = np.random.randn(10000)
plt.hist(data, bins = 'auto')

plt.subplot(122)
np.random.seed(0)
data = np.random.randn(10000)
plt.hist(data, bins = 'auto', density = True)   #y軸改成密度

plt.show()

print('------------------------------------------------------------')	#60個

print('載入字型範例')

"""
翰字鑄造 台北黑體 regular 版本

TaipeiSansTCBeta-Regular.ttf 

https://drive.google.com/uc?id=1eGAsTN1HBpJAkeVM57_C7ccp7hbgSz3_&export=download

TaipeiSansTCBeta-Regular.ttf'

"""

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個

"""
import matplotlib as mpl

# 获取图的坐标信息
ax = plt.gca()
# 设置日期的显示格式
date_format = mpl.dates.DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_format)
# 设置x轴显示多少个日期刻度
# xlocator = mpl.ticker.LinearLocator(10)
# 设置x轴每个刻度的间隔天数
xlocator = mpl.ticker.MultipleLocator(7)
ax.xaxis.set_major_locator(xlocator)
# 为了避免x轴刻度标签的紧凑，将刻度标签旋转45度
plt.xticks(rotation = 45)

# 添加y轴标签
plt.ylabel('人数')
# 添加图形标题
plt.title('每天微信文章阅读人数与人次趋势')
# 添加图例
plt.legend()
# 显示图形
plt.show()
"""



"""
# 读入数据
iris = pd.read_csv(r'F:\\python_Data_analysis_and_mining\\06\\iris.csv')
print(iris.shape)
# 绘制散点图
plt.scatter(x = iris.Petal_Width, # 指定散点图的x轴数据
y = iris.Petal_Length, # 指定散点图的y轴数据
color = 'steelblue' # 指定散点图中点的颜色
)
# 添加x轴和y轴标签
plt.xlabel('花瓣宽度')
plt.ylabel('花瓣长度')
# 添加标题
plt.title('鸢尾花的花瓣宽度与长度关系')
# 显示图形
plt.show()

# Pandas模块绘制散点图
# 绘制散点图
iris.plot(x = 'Petal_Width', y = 'Petal_Length', kind = 'scatter', title = '鸢尾花的花瓣宽度与长度关系')
# 修改x轴和y轴标签
plt.xlabel('花瓣宽度')
plt.ylabel('花瓣长度')
# 显示图形
plt.show()

# seaborn模块绘制分组散点图
sns.lmplot(x = 'Petal_Width', # 指定x轴变量
y = 'Petal_Length', # 指定y轴变量
hue = 'Species', # 指定分组变量
data = iris, # 指定绘图数据集
legend_out = False, # 将图例呈现在图框内
truncate = True # 根据实际的数据范围，对拟合线作截断操作
)
# 修改x轴和y轴标签
plt.xlabel('花瓣宽度')
plt.ylabel('花瓣长度')
# 添加标题
plt.title('鸢尾花的花瓣宽度与长度关系')
# 显示图形
plt.show()
"""
print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個

print('Bar圖')

money = [1.5e5, 2.5e6, 5.5e6, 2.0e7]

def millions(x, pos):
    """The two args are the value and tick position."""
    return '${:1.1f}M'.format(x * 1e-6)

fig, ax = plt.subplots()
# Use automatic FuncFormatter creation
ax.yaxis.set_major_formatter(millions)
ax.bar(['Bill', 'Fred', 'Mary', 'Sue'], money,label = 'data1', align = 'edge')
ax.set_title('Bar chart')
ax.set_xlabel('Name')
ax.set_ylabel('Money')
ax.legend(loc = 2)

plt.show()

print('------------------------------------------------------------')	#60個

# from basic_units import cm, inch

cm = 1
inch = cm*0.039

fig, ax = plt.subplots()
N = 5
ind = np.arange(N)    # the x locations for the groups
width = 0.35         # the width of the bars
men_means = [150*cm, 160*cm, 146*cm, 172*cm, 155*cm]
men_std = [20*cm, 30*cm, 32*cm, 10*cm, 20*cm]
ax.bar(x = ind, height = men_means, width = width, bottom = 0*cm, yerr = men_std, label = 'Men')
women_means = (145*cm, 149*cm, 172*cm, 165*cm, 200*cm)
women_std = (30*cm, 25*cm, 20*cm, 31*cm, 22*cm)
ax.bar(x = ind + width, height = women_means, width = width, bottom = 0*cm, yerr = women_std,label = 'Women')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
ax.legend()
ax.yaxis.set_units(inch)
ax.autoscale_view()

plt.show()

print('------------------------------------------------------------')	#60個

N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
ind = np.arange(N) # the x locations for the groups
width = 0.35
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(ind, menMeans, width, color = 'r')
ax.bar(ind, womenMeans, width,bottom = menMeans, color = 'b')
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
ax.set_yticks(np.arange(0, 81, 10))
ax.legend(labels = ['Men', 'Women'])

plt.show()
'''
print("------------------------------------------------------------")  # 60個

print("散佈圖")

fig, ax = plt.subplots()

N = 50
x = np.random.randint(30, size=N)
y = np.random.randint(30, size=N)
c = np.random.randint(30, size=N)
size = np.exp(np.random.randint(10, size=N) * 200)
sc = ax.scatter(x=x, y=y, c=c, s=c, alpha=0.5, label="scatter plot")

ax.set_xlabel("X軸", loc="left")
ax.set_ylabel("Y軸", loc="top")
ax.legend(loc=1)
cbar = fig.colorbar(sc)
cbar.set_label("Z軸", loc="center")

plt.show()

print("------------------------------------------------------------")  # 60個

print("Hist圖")

fig, ax = plt.subplots(1, 3, figsize=(10, 8))

normal_samples = np.random.normal(
    size=100000
)  # 生成 100000 組標準常態分配（平均值為 0，標準差為 1 的常態分配）隨機變數
uniform_samples = np.random.uniform(size=100000)  # 生成 100000 組介於 0 與 1 之間均勻分配隨機變數
exp_samples = np.random.exponential(scale=2, size=100000)

ax[0].hist(x=normal_samples, bins=1000, label="Normal distribution")
ax[1].hist(x=uniform_samples, bins=1000, label="Uniform distribution")
ax[2].hist(x=exp_samples, bins=1000, label="Exponential distribution")
ax[0].legend()
ax[1].legend()
ax[2].legend()

plt.show()

print("------------------------------------------------------------")  # 60個

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


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
