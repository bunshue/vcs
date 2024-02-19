"""
Python Matplotlib.pyplot.hist()用法及代碼示例

Matplotlib是Python中的一個庫，它是數字的-NumPy庫的數學擴展。
Pyplot是Matplotlib模塊的基于狀態的接口，該模塊提供了MATLAB-like接口。
matplotlib.pyplot.hist()函數

matplotlib庫的pyplot模塊中的hist()函數用于繪制直方圖。

用法： matplotlib.pyplot.hist(x, bins=None, range=None, density=False, weights=None, cumulative=False, bottom=None, histtype=’bar’, align=’mid’, orientation=’vertical’, rwidth=None, log=False, color=None, label=None, stacked=False, \*, data=None, \*\*kwargs)

參數：此方法接受以下描述的參數：

    x:此參數是數據序列。
    bins:此參數是可選參數，它包含整數，序列或字符串。
    range:此參數是可選參數，它是箱子的上下限。
    density:此參數是可選參數，它包含布爾值。
    weights:此參數是可選參數，并且是一個權重數組，與x的形狀相同。
    bottom:此參數是每個容器底部基線的位置。
    histtype:此參數是可選參數，用于繪制直方圖的類型。 {‘bar’，‘barstacked’，‘step’，‘stepfilled’}
    align:此參數是可選參數，它控制如何繪制直方圖。 {‘left’，‘mid’，‘right’}
    rwidth:此參數是可選參數，它是條形圖的相對寬度，是箱寬度的一部分
    log:此參數是可選參數，用于將直方圖軸設置為對數刻度
    color:此參數是一個可選參數，它是一個顏色規格或一系列顏色規格，每個數據集一個。
    label:此參數是可選參數，它是一個字符串或匹配多個數據集的字符串序列。

返回值：這將返回以下內容：

    n:這將返回直方圖箱的值。
    垃圾桶：這將返回箱子的邊。
    補丁：這將返回用于創建直方圖的單個補丁的列表。

"""

"""
以上實例中我們生成了三組不同的隨機數據，并使用 hist() 函數繪制了它們的直方圖。通過設置不同的均值和標準差，我們可以生成具有不同分布特征的隨機數據。

我們設置了 bins 參數為 30，這意味著將數據范圍分成 30 個等寬的區間，然后統計每個區間內數據的頻數。
我們設置了 alpha 參數為 0.5，這意味著每個直方圖的顏色透明度為 50%。

我們使用 label 參數設置了每個直方圖的標簽，以便在圖例中顯示。

然后使用 legend() 函數顯示圖例。最后，我們使用 title()、xlabel() 和 ylabel() 函數設置了圖表的標題和坐標軸標簽。
"""
"""
plt.hist()參數設置

arr: 需要計算直方圖的一維數組；
bins: 直方圖的柱數，可選項，默認為10；
density: : 是否將得到的直方圖向量歸一化。默認為0；
color：顏色序列，默認為None；
facecolor: 直方圖顏色；
edgecolor: 直方圖邊框顏色；
alpha: 透明度；
histtype: 直方圖類型，『bar』, 『barstacked』, 『step』, 『stepfilled』；

"""

# hist 集合

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 15  # 設定字型大小
plt.rcParams['font.size'] = 15

print("------------------------------------------------------------")  # 60個

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="hist 集合 1",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

N = 500  # 資料個數
num_bins = 20  # 直方圖顯示時的束數

# 第一張圖
plt.subplot(231)

print("以直方圖顯示常態分佈")
x = np.random.randn(N)  # 常態分佈數字
plt.hist(x, num_bins, color="r", alpha = 0.5)  #alpha調整透明度 給多個直方圖畫在一起用
#plt.hist(x, bins = 'auto')
#plt.hist(x, bins = 'auto', density = True)   #y軸改成密度
x = np.random.randn(N)  # 常態分佈數字
plt.hist(x, num_bins, alpha = 0.5)
#plt.hist(x, bins=range(-5, 5, 1), alpha=0.5)  #設定bin的範圍

# 第二張圖
plt.subplot(232)

normal_samples = np.random.normal(size=N)  # 生成 N 組標準常態分配（平均值為 0，標準差為 1 的常態分配）隨機變數
plt.hist(normal_samples, bins=num_bins)

# 第三張圖
plt.subplot(233)

uniform_samples = np.random.uniform(size=N)  # 生成 N 組介於 0 與 1 之間均勻分配隨機變數
plt.hist(uniform_samples, bins=num_bins)

# 第四張圖
plt.subplot(234)

print("描繪頻率分布圖")

print('用pandas讀取csv檔, 之後用plt.hist畫出來')
# 讀入csv檔
filename = (
    "_data/python_ReadWrite_CSV7_onigiri.csv"
)
dat = pd.read_csv(filename, encoding="UTF-8")

print(type(dat))
print(dat)

# 頻率分布圖
plt.hist(dat["店長"], bins=range(0, 200, 10), alpha=0.5)
plt.hist(dat["太郎"], bins=range(0, 200, 10), alpha=0.5)

bins=range(0, 200, 10)
for b in bins:
    print(b)

print("計算平均數、變異數、標準差")

print("店長---------")
print("平均:", np.mean(dat["店長"]))
print("變異數:", np.var(dat["店長"]))
print("標準差:", np.std(dat["店長"]))

print("太郎---------")
print("平均:", np.mean(dat["太郎"]))
print("變異數:", np.var(dat["太郎"]))
print("標準差:", np.std(dat["太郎"]))

# 第五張圖
plt.subplot(235)

score = [
    800,
    750,
    450,
    680,
    802,
    630,
    710,
    450,
    250,
    320,
    610,
    670,
    815,
    870,
    900,
    650,
    450,
    730,
    840,
    675,
    795,
    585,
    870,
    960,
    190,
]
n, b, p = plt.hist(score, bins=[10, 255, 405, 605, 785, 905, 990])

for i in range(len(n)):
    plt.text(b[i] + 10, n[i], int(n[i]), ha="center", va="bottom", fontsize=10)

plt.title("多益成績分布直方圖")
plt.xlabel("成績")
plt.ylabel("人數")

# 第六張圖
plt.subplot(236)

N = 100
d1 = np.random.randint(1, 6+1, 1000)#不含尾
d2 = np.random.randint(1, 6+1, 1000)

dsums = d1 + d2

#count, bins, ignored = plt.hist(dsums, 11, density=True)   #以密度表示
count, bins, ignored = plt.hist(dsums, 11)  #以總數表示
plt.title("擲兩個骰子多次 看其分布")
plt.xlabel("兩個骰子和")
#plt.ylabel("密度")   #density = True
plt.ylabel("次數")

plt.show()


print("------------------------------------------------------------")  # 60個

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="hist 集合 2",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

N = 10000  # 資料個數
num_bins = 100  # 直方圖顯示時的束數

# 第一張圖
plt.subplot(231)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(N)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=True, alpha=0.75)

plt.xlabel("Smarts")
plt.ylabel("Probability")
plt.title("Histogram of IQ")
plt.text(60, 0.025, r"$\mu=100,\ \sigma=15$")
plt.xlim(40, 160)
plt.ylim(0, 0.03)
plt.grid(True)


# 第二張圖
plt.subplot(232)

mu = 121
sigma = 21
x = mu + sigma * np.random.randn(1000)

num_bins = 100

n, bins, patches = plt.hist(x, num_bins, density=1, color="green", alpha=0.7)

y = (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2)

plt.plot(bins, y, "--", color="black")

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.title("matplotlib.pyplot.hist() function Example\n\n", fontweight="bold")

# 第三張圖
plt.subplot(233)

n_bins = 20
x = np.random.randn(N, 3)

colors = ["green", "blue", "lime"]

plt.hist(x, n_bins, density=True, histtype="bar", color=colors, label=colors)
plt.legend(prop={"size": 10})
plt.title("matplotlib.pyplot.hist() function Example\n\n", fontweight="bold")

# 第四張圖
plt.subplot(234)

x = np.random.rand(50, 5) # 產生共5組，每組50個隨機數,
plt.hist(x)

# 第五張圖
plt.subplot(235)

# 生成三組隨機數據
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(2, 1, 1000)
data3 = np.random.normal(-2, 1, 1000)

# 繪制直方圖
plt.hist(data1, bins=30, alpha=0.5, label="Data 1")
plt.hist(data2, bins=30, alpha=0.5, label="Data 2")
plt.hist(data3, bins=30, alpha=0.5, label="Data 3")

# 設置圖表屬性
plt.title("RUNOOB hist() TEST")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()

# 第六張圖
plt.subplot(236)

# 同坐標軸的多個頻次直方圖

x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)
kwargs = dict(histtype="stepfilled", alpha=0.3, density=True, bins=40)
plt.hist(x1, **kwargs)
plt.hist(x2, **kwargs)
plt.hist(x3, **kwargs)

plt.show()

print("------------------------------------------------------------")  # 60個

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="hist 集合 3",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

N = 10000  # 資料個數
num_bins = 100  # 直方圖顯示時的束數

# 第一張圖
plt.subplot(231)

grade = [90,72,45,18,13,81,65,68,73,84,75,79,58,78,96,100,98,64,43,2,63,71,27,35,45,65]

n, b, p=plt.hist(grade, bins = [0,10,20,30,40,50,60,70,80,90,100])

for i in range(len(n)):
    plt.text(b[i]+10, n[i], int(n[i]), ha='center', va='bottom', fontsize=12)
  
plt.title('全班成績直方圖分布圖')
plt.xlabel('考試分數')
plt.ylabel('人數統計')

# 第二張圖
plt.subplot(232)



# 第三張圖
plt.subplot(233)


# 第四張圖
plt.subplot(234)

score = [800,750,450,680,802,630,710,450,250,320,610,670,815,\
         870,900,650,450,730,840,675,795,585,870,960,190]

plt.hist(score, bins = [10,255,405,605,785,905,990])
plt.title('多益成績分布直方圖')
plt.xlabel('成績')
plt.ylabel('人數')

# 第五張圖
plt.subplot(235)

score = [800,750,450,680,802,630,710,450,250,320,610,670,815,870,900,650,450,730,840,675,795,585,870,960,190]
n, b, p=plt.hist(score, bins = [10,255,405,605,785,905,990])

for i in range(len(n)):
    plt.text(b[i]+10, n[i], int(n[i]), ha='center', va='bottom', fontsize=10)
plt.title('多益成績分布直方圖')
plt.xlabel('成績')
plt.ylabel('人數')


# 第六張圖
plt.subplot(236)

grade = [90,72,45,18,13,81,65,68,73,84,75,79,58,78,96,100,98,64,43,2,63,71,27,35,45,65]

plt.hist(grade, bins = [0,10,20,30,40,50,60,70,80,90,100])
plt.title('全班成績直方圖分布圖')
plt.xlabel('考試分數')
plt.ylabel('人數統計')

plt.show()


print("------------------------------------------------------------")  # 60個


"""
二維頻次直方圖

就像將一維數組分為區間創建一維頻次直方圖一樣，我們也可以將二維數組按照二維區 間進行切分，來創建二維頻次直方圖。

1.plt.hist2d:二維頻次直方圖

繪製二維頻次直方圖最簡單的方法，就是使用Matplotlib的plt.hist2d函數。
"""

"""NG
plt.hist2d(x, y, bins=30, cmap='Blues')
cb = plt.colorbar()
cb.set_label('counts in bin')

plt.show()
"""

"""
2.plt.hexbin:六邊形區間劃分

二維頻次直方圖是由與坐標軸正交的方塊分割而成的，還有一種常用的方式是用正六邊形分割。Matplotlib 提供了 plt.hexbin 滿足此類需求，將二維數據集分割成蜂窩狀。
"""

"""NG
plt.hexbin(x, y, gridsize=30, cmap='Blues')
cb = plt.colorbar(label='count in bin')
plt.show()

"""



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("新進")

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

data = np.arange(1,101)
num_bins = 8

cc = n, b, p = plt.hist(data, num_bins)
print(type(cc))
print(cc)

for i in range(len(n)):
    print("x = ", b[i]+10, ", y = ",n[i], ", text =", int(n[i]))
    plt.text(b[i]+10, n[i], int(n[i]), ha='center', va='bottom', fontsize=10)

print('n')
print(n)
print('b')
print(b)
print('p')
print(p)

plt.show()

print("------------------------------------------------------------")  # 60個

plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'
plt.rcParams['font.size']=18

grade = [90,72,45,18,13,81,65,68,73,84,75,79,58,78,96,100,98,64,43,2,63,71,27,35,45,65]

plt.hist(grade, bins = [0,10,20,30,40,50,60,70,80,90,100],edgecolor = 'b') 
plt.title('全班成績直方圖分布圖')
plt.xlabel('考試分數')
plt.ylabel('人數統計')

plt.show()

print("------------------------------------------------------------")  # 60個

plt.rcParams['font.sans-serif'] = 'Microsoft JhengHei'
plt.rcParams['axes.unicode_minus']=False
plt.rcParams['font.size']=15

grade = [90,72,45,18,13,81,65,68,73,84,75,79,58,78,96,100,98,64,43,2,63,71,27,35,45,65]

n, b, p = plt.hist(grade, bins = [0,10,20,30,40,50,60,70,80,90,100], edgecolor = 'r') 

for i in range(len(n)):
    plt.text(b[i]+10, n[i], int(n[i]), ha='center', va='bottom', fontsize=12)
  
plt.title('全班成績直方圖分布圖')
plt.xlabel('考試分數')
plt.ylabel('人數統計')
plt.show()

print("------------------------------------------------------------")  # 60個

def dice_generator(times, sides):
    # 處理隨機數
    for i in range(times):              
        ranNum = random.randint(1, sides)      # 產生1-6隨機數
        dice.append(ranNum)

times = 10000                           # 擲骰子次數
sides = 6                               # 骰子有幾面
dice = []                               # 建立擲骰子的串列
dice_generator(times, sides)            # 產生擲骰子的串列
h = plt.hist(dice,sides)                # 繪製hist圖
print("bins的y軸 ",h[0])
print("bins的x軸 ",h[1])
plt.ylabel('次數')
plt.title('測試 10000 次')

plt.show()

print("------------------------------------------------------------")  # 60個

print('比上面多了 rwidth=0.8')

def dice_generator(times, sides):
    # 處理隨機數
    for i in range(times):              
        ranNum = random.randint(1, sides)              # 產生1-6隨機數
        dice.append(ranNum)

times = 10000                                   # 擲骰子次數
sides = 6                                       # 骰子有幾面
dice = []                                       # 建立擲骰子的串列
dice_generator(times, sides)                    # 產生擲骰子的串列
h = plt.hist(dice,sides,rwidth=0.8)             # 繪製hist圖
print("bins的y軸 ",h[0])
print("bins的x軸 ",h[1])
plt.ylabel('次數')
plt.title('測試 10000 次')

plt.show()

print("------------------------------------------------------------")  # 60個

print('比上面多了 rwidth=0.8 cumulative=True')

def dice_generator(times, sides):
    # 處理隨機數
    for i in range(times):              
        ranNum = random.randint(1, sides)              # 產生1-6隨機數
        dice.append(ranNum)

times = 10000                                   # 擲骰子次數
sides = 6                                       # 骰子有幾面
dice = []                                       # 建立擲骰子的串列
dice_generator(times, sides)                    # 產生擲骰子的串列
h = plt.hist(dice,sides,rwidth=0.5,cumulative=True) # 繪製hist圖
print("bins的y軸 ",h[0])
print("bins的x軸 ",h[1])
plt.ylabel('次數')
plt.title('測試 10000 次')

plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




"""

plt.hist 參數

facecolor="yellow"
edgecolor="red"

facecolor: 直方圖顏色；   = color
edgecolor: 直方圖邊框顏色；

# Fixing random state for reproducibility
np.random.seed(1234567)

# Fixing random state for reproducibility
np.random.seed(19680801)

np.random.seed(0)
np.random.seed(10**7)


plt.hist(
    density=True,
    histtype="stepfilled",
    color="steelblue",
    edgecolor="none",
)


# 直方圖
x = np.random.rand(50, 2) # 產生共兩組，每組50個隨機數,
plt.hist(x)



"""

#plt.style.use("seaborn-white")

