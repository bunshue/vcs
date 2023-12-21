# boxplot 集合

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"

import sys
import matplotlib.pyplot as plt
import numpy as np

# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

print("固定亂數種子")
np.random.seed(10)

N = 100
y = np.random.randn(N)

#plt.boxplot(y) # 無參數 最基本的箱形圖 直式
#plt.show()

#print("全部\n",y) #  many
print("最大: ",y.max())
print("最小: ",y.min())
print("平均: ",y.mean())
#print("中位數: ",y.median())
print("標準差: ",y.std())

print("求 四分位數")
lower_q = np.quantile(y, 0.25, method="lower")  # 下四分位數
higher_q = np.quantile(y, 0.75, method="higher")  # 上四分位數
int_r = higher_q - lower_q  # 四分位距
print("下四分位數 :", lower_q)
print("上四分位數 :", higher_q)
print("四分位距 :", int_r)

# y[3]=10 #  造一個超大值

# 箱形圖  便於確認資料分布的視覺化方法
# 盒鬚圖（Box plot）

# plt.boxplot(y) # 無參數
labels = ['常態分佈亂數產生']
#plt.boxplot(y, labels = labels)

#plt.boxplot(y, whis = 1.8) # ???

median_line = dict(linestyle='--',
                   linewidth=2.5,
                   color='g')

#vert=True 垂直箱圖, vert=False 水平箱圖

#在箱圖上 多畫 中位數線
#plt.boxplot(y,labels=labels,vert=True,medianprops=median_line)

#多標記平均數線
#plt.boxplot(y,labels=labels,vert=True,showmeans=True)

# 設計箱線圖的晶鬚線
whisker_line = dict(linestyle='--',linewidth=2.5,color='m')
#plt.boxplot(y,labels=labels,vert=True,whiskerprops=whisker_line)

# 隱藏箱線圖的異常值
# plt.boxplot(y,labels=labels,showfliers=False)


# 設計箱線圖的caps
caps_line = dict(linestyle='--',linewidth=2.5,color='r')
#plt.boxplot(y,labels=labels,vert=True,capprops=caps_line)

# 隨機數據的箱線圖
mean_mark = dict(markerfacecolor='b', markeredgecolor='b', marker='D')
plt.boxplot(y,labels=labels,vert=True, showmeans=True,meanprops=mean_mark)


plt.grid(True)
plt.show()

print("------------------------------------------------------------")  # 60個

""" 計算分位數
import math

def percentile(N, percent, key=lambda x: x):
    N = sorted(N)
    k = (len(N) - 1) * percent
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return key(N[int(k)])
    d0 = key(N[int(f)]) * (c - k)
    d1 = key(N[int(c)]) * (k - f)
    return round(d0 + d1, 5)

print("計算10分位數")
print(percentile([1, 2, 3, 4, 5], 0.1))

print("計算50分位數")
print(percentile([1, 2, 3, 4, 5], 0.5))

print("計算90分位數")
print(percentile([1, 2, 3, 4, 5], 0.9))

print("numpy 计算分位数")

import numpy as np

nums = [1, 2, 3, 4, 5]
print(np.percentile(nums, [10, 50, 90]))

print("pandas 计算分位数")
import pandas as pd

data = pd.DataFrame({"col": [1, 2, 3, 4, 5]})
print(data.head())
print("计算分位数，分别得到10分位数，50分位数，90分位数")

print(data["col"].quantile([0.1, 0.5, 0.9]))

print(data["col"].quantile(0.1))


print("用numpy计算分位数")

print(np.percentile(data["col"], [10, 50, 90]))
"""

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


import matplotlib.pyplot as plt

x = [9, 12, 30, 31, 31, 32, 33, 33, 35, 35,
     38, 38, 41, 42, 43, 46, 46, 48, 52, 70]

bp = plt.boxplot(x,showmeans=True)
outliers = [y.get_ydata() for y in bp["fliers"]]
boxes = [y.get_ydata() for y in bp["boxes"]]
medians = [y.get_ydata() for y in bp["medians"]]
means = [y.get_ydata() for y in bp["means"]]
whiskers = [y.get_ydata() for y in bp["whiskers"]]
caps = [y.get_ydata() for y in bp["caps"]]
print(f"異常值Outliers : {outliers}")
print(f"盒  子Boxes    : {boxes}")
print(f"中位數Medians  : {medians}")
print(f"均  值Means    : {means}")
print(f"晶  鬚Whiskers : {whiskers}")
print(f"帽  子caps     : {caps}")
plt.show()


      


print("------------------------------------------------------------")  # 60個


import matplotlib.pyplot as plt

x = [9, 12, 30, 31, 31, 32, 33, 33, 35, 35,
     38, 38, 41, 42, 43, 46, 46, 48, 52, 70]

bp = plt.boxplot(x,showmeans=True)
outliers = [y.get_ydata() for y in bp["fliers"]]
Q1 = [min(y.get_ydata()) for y in bp["boxes"]]
Q3 = [max(y.get_ydata()) for y in bp["boxes"]]
medians = [y.get_ydata()[0] for y in bp["medians"]]
means = [y.get_ydata()[0] for y in bp["means"]]
whiskers = [y.get_ydata() for y in bp["whiskers"]]
minimum = [y.get_ydata()[0] for y in bp["caps"][::2]]
maximum = [y.get_ydata()[0] for y in bp["caps"][1::2]]
print(f"異常值Outliers : {outliers}")
print(f"     Q1        : {Q1[0]}")
print(f"     Q3        : {Q3[0]}")
print(f"中位數Medians  : {medians[0]}")
print(f"均  值Means    : {means[0]}")
print(f"晶  鬚Whiskers : {whiskers}")
print(f"極小值mimimums : {minimum[0]}")
print(f"極大值maximums : {maximum[0]}")
plt.show()

  
      


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

