# bar 集合 長條圖與橫條圖

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

plt.figure(
    num="bar 集合 1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

print("用bar圖畫出字典資料 並標明數值")
animals = {"鼠": 3, "牛": 48, "虎": 33, "兔": 8}
print(type(animals))
print(animals)

plt.bar(range(len(animals)), animals.values(), facecolor="#99ccff")

# plt.xticks(range(len(animals)), animals.keys())
# 以上1行 相當於 以下3行
seq = [0, 1, 2, 3]
labels = ["米老鼠", "班尼牛", "跳跳虎", "彼得兔"]
plt.xticks(seq, labels, rotation=-45)

plt.ylim((0, 55))
for x, y in zip(range(len(animals)), animals.values()):
    plt.text(x - 0.05, y + 0.5, "{:>8,.0f}".format(y), ha="center")


# 第二張圖
plt.subplot(232)

print("垂直/水平 長條圖")

# 設定將使用的數值
x = ["鼠", "牛", "虎", "兔", "龍"]
y = [3, 48, 33, 8, 38]

print("垂直長條圖")
# 繪製出垂直 Bar，這邊使用的是 bar 函數，設定的是 width 寬度
plt.bar(x, y, width=0.5, color="red")
# plt.bar(x, y, fc = '#e55934', ec = 'none')
# plt.xticks(x, y)       #設定x軸刻度為文字

print("水平長條圖")
# 繪製出水平 Bar，這邊使用的是 barh 函數，設定的是 height 寬度
# plt.barh(x, y, height = 0.5, color = 'blue')   #橫向bar圖
# plt.barh(x, y)                                 #橫向bar圖
# plt.yticks(index, labels)       #設定y軸刻度為文字


# 第三張圖
plt.subplot(233)

# 長條圖範例  bar圖畫字典

animals = {
    "鼠": 3,
    "牛": 48,
    "虎": 33,
    "兔": 8,
    "龍": 38,
}

plt.bar(range(len(animals.values())), animals.values(), width=0.8)
plt.xticks(range(len(animals.values())), animals.keys())

# 第四張圖
plt.subplot(234)


def addlabels1(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i])


animals = ["鼠", "牛", "虎", "兔"]
weights2 = [3, 48, 33, 8]

plt.ylim(0, 50)
plt.bar(animals, weights2, color=["red", "green", "blue", "yellow"])
addlabels1(animals, weights2)
plt.title("體重")

# 第五張圖
plt.subplot(235)


def addlabels2(x, y):
    for i in range(len(x)):
        plt.text(y[i], i, y[i])


animals = ["鼠", "牛", "虎", "兔"]
weights2 = [3, 48, 33, 8]

plt.xlim(0, 50)
plt.barh(animals, weights2, color=["red", "green", "blue", "yellow"])
addlabels2(animals, weights2)
plt.title("體重")

# 第六張圖
plt.subplot(236)

print("將字典直接輸出給bar圖")

data = {"鼠": 3, "牛": 48, "虎": 33, "兔": 8}
plt.bar(list(data.keys()), list(data.values()))

plt.show()

print("------------------------------------------------------------")  # 60個
plt.figure(
    num="bar 集合 2",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)


# 第二張圖
plt.subplot(232)

filename = "C:/_git/vcs/_1.data/______test_files1/__RW/_txt/台灣各縣市人口.txt"

with open(filename, "r") as fp:
    populations = fp.readlines()

city = list()
popu = list()

for p in populations:
    cc, pp = p.split(",")
    city.append(cc)
    popu.append(int(pp))

index = np.arange(len(city))

print(index)
print(city)
print(popu)
plt.bar(index, popu)
plt.xticks(index + 0.5, city, rotation=-70)

# 第三張圖
plt.subplot(233)

listCity = [
    "高雄市",
    "屏東縣",
    "臺東縣",
    "新北市",
    "臺中市",
    "臺北市",
    "臺南市",
    "新竹縣",
    "彰化縣",
    "嘉義縣",
    "雲林縣",
    "桃園市",
    "宜蘭縣",
    "苗栗縣",
    "南投縣",
    "基隆市",
    "花蓮縣",
]

listCount = [12, 24, 11, 11, 18, 8, 16, 11, 18, 8, 11, 9, 54, 40, 31, 10, 9]

# 繪製柱狀圖

plt.barh(listCity, listCount, label="農業區")  # 橫向柱狀圖串列數據設定
plt.title("各縣市農場數量")  # 柱狀圖名稱
plt.xlim(0, 60)  # X軸範圍0~60
plt.xlabel("數量")  # X軸名稱
plt.ylabel("縣市")  # Y軸名稱
for y, x in enumerate(listCount):  # 使用迴圈讓柱狀末端顯示各縣市農業區總數
    plt.text(x, y, "%s" % x, ha="center")
plt.legend()  # 圖例(柱狀圖)說明
plt.grid(True)  # 顯示格線


# 第四張圖
plt.subplot(234)

x = ["鼠", "牛", "虎", "兔"]
s = [3, 48, 33, 8]

"""
plt.bar(x, s)
plt.bar(x, s, width=0.8, align="edge", color="r", ec="y", lw=2)
"""
plt.bar(x, s, width=0.8, align="edge", color="r", ec="y", lw=2)

# 第五張圖
plt.subplot(235)

print("將字典直接輸出給barh圖, 加error")

data = {"鼠": 3, "牛": 48, "虎": 33, "兔": 8}
error = [3, 10, 5, 8]
plt.barh(
    list(data.keys()),
    list(data.values()),
    xerr=error,
    align="center",
    color="green",
    ecolor="black",
)

# 第六張圖
plt.subplot(236)

print("畫出頻率分布圖")

filename = "_data/python_ReadWrite_CSV6_score.csv"

dat = pd.read_csv(filename, encoding="UTF-8")

# 計算各組別頻率
hist = [0] * 10  # 頻率（元素個數10，初始化為0）
for dat in dat["數學"]:
    if dat < 10:
        hist[0] += 1
    elif dat < 20:
        hist[1] += 1
    elif dat < 30:
        hist[2] += 1
    elif dat < 40:
        hist[3] += 1
    elif dat < 50:
        hist[4] += 1
    elif dat < 60:
        hist[5] += 1
    elif dat < 70:
        hist[6] += 1
    elif dat < 80:
        hist[7] += 1
    elif dat < 90:
        hist[8] += 1
    elif dat <= 100:
        hist[9] += 1
print("頻率:", hist)

# 頻率分布圖
x = list(range(1, 11))  # x軸的值
labels = [
    "0~",
    "10~",
    "20~",
    "30~",
    "40~",
    "50~",
    "60~",
    "70~",
    "80~",
    "90~",
]  # x軸的刻度標籤
plt.bar(x, hist, tick_label=labels, width=1)  # 描繪長條圖

plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(
    num="bar 集合 3",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

x = ["上學期", "下學期"]
s1, s2, s3, s4 = [96.2, 87.1], [88.9, 95.2], [85.1, 91.5], [95.2, 96.7]

index = np.arange(len(x))
width = 0.15
plt.bar(index - 1.5 * width, s1, width, color="b")
plt.bar(index - 0.5 * width, s2, width, color="r")
plt.bar(index + 0.5 * width, s3, width, color="y")
plt.bar(index + 1.5 * width, s4, width, color="g")

plt.xticks(index, x)
plt.legend(["2017年", "2018年", "2019年", "2020年"])

plt.ylabel("平均分數,取到小數點第一位")
plt.title("大學四年各學期平均成績比較表")

# 第二張圖
plt.subplot(232)

votes = [135, 412, 397]  # 得票數
N = len(votes)  # 計算長度
x = np.arange(N)  # 長條圖x軸座標
width = 0.35  # 長條圖寬度

plt.bar(x, votes, width)  # 繪製長條圖
plt.xticks(x, ("James", "Peter", "Norton"))  # x 軸刻度
plt.yticks(np.arange(0, 450, 30))  # y 軸刻度
plt.title("x用名稱 y設定範圍刻距")

# 第三張圖
plt.subplot(233)



# 第四張圖
plt.subplot(234)

colors = ["b", "g", "r", "y", "c"]

animals = ["鼠", "牛", "虎", "兔", "龍"]

weights = [3, 48, 33, 8, 38]

plt.barh(animals, weights, color=colors)

# 第五張圖
plt.subplot(235)

animals = ["鼠", "牛", "虎", "兔", "龍"]

weights = [3, 48, 33, 8, 38]
# plt.bar(animals,weights)
# plt.bar(animals,weights,align='edge',color='g')
plt.bar(animals, weights, width=0.5, color="m")

# 第六張圖
plt.subplot(236)

colors = ["grey", "grey", "red", "grey", "grey"]
animals = ["鼠", "牛", "虎", "兔", "龍"]

weights = [3, 48, 33, 8, 38]

plt.bar(animals, weights, color=colors)


plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(
    num="bar 集合 4",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

x = ["第1學期", "第2學期", "第3學期", "第4學期", "第5學期", "第6學期", "第7學期", "第8學期"]
s = [95.3, 94.2, 91.4, 96.2, 92.3, 93.6, 89.4, 91.2]
plt.bar(x, s)
plt.ylabel("平均分數")
plt.title("大學四年各學期的平均分數")

# 第二張圖
plt.subplot(232)

x = ["第1學期", "第2學期", "第3學期", "第4學期", "第5學期", "第6學期", "第7學期", "第8學期"]
s = [95.3, 94.2, 91.4, 96.2, 92.3, 93.6, 89.4, 91.2]
plt.bar(x, s, width=0.5, align="edge", color="r", ec="y", lw=2)
plt.ylabel("平均分數")
plt.title("大學四年各學期的平均分數")


# 第三張圖
plt.subplot(233)

x = ["第1學期", "第2學期", "第3學期", "第4學期", "第5學期", "第6學期", "第7學期", "第8學期"]
s = [95.3, 94.2, 91.4, 96.2, 92.3, 93.6, 89.4, 91.2]
plt.barh(x, s)
plt.ylabel("平均分數")
plt.title("大學四年各學期的平均分數")


# 第四張圖
plt.subplot(234)

x = ["第1學期", "第2學期", "第3學期", "第4學期", "第5學期", "第6學期", "第7學期", "第8學期"]
s = [95.3, 94.2, 91.4, 96.2, 92.3, 93.6, 89.4, 91.2]
plt.barh(x, s)
plt.ylabel("平均分數")
plt.title("大學四年各學期的平均分數")


# 第五張圖
plt.subplot(235)

x = ["第1學期", "第2學期", "第3學期", "第4學期", "第5學期", "第6學期", "第7學期", "第8學期"]
s = [95.3, 94.2, 91.4, 96.2, 92.3, 93.6, 89.4, 91.2]
plt.bar(x, s, width=0.5, align="edge", color="r", ec="y", lw=2)
plt.ylabel("平均分數")
plt.title("大學四年各學期的平均分數")


# 第六張圖
plt.subplot(236)


plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(
    num="bar 集合 5",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

name = ["鼠", "牛", "虎", "兔", "龍"]
weight = [3, 48, 33, 8, 38]
# plt.bar(name, weight)
plt.bar(name, weight, width=0.8, align="edge", color="r", ec="y", lw=2)


# 第二張圖
plt.subplot(232)

x = ["鼠", "牛", "虎", "兔", "龍"]
s = [3, 48, 33, 8, -38]
plt.barh(x, s, color="red")


# 第三張圖
plt.subplot(233)

revenue = [300, 320, 400, 350]
cost = [250, 280, 310, 290]
quarter = ["Q1", "Q2", "Q3", "Q4"]

barH = 0.5
plt.barh(quarter, revenue, color="g", height=barH, label="收入")
plt.barh(quarter, -np.array(cost), color="m", height=barH, label="支出")

plt.title("公司收支表")
plt.xlabel("收入與支出")
plt.ylabel("季度")
plt.legend()

# 第四張圖
plt.subplot(234)

x = np.arange(1, 6)
plt.bar(x - 0.4, [3, 10, 8, 12, 6], width=0.4, ec="none", fc="#e63946")
plt.bar(x, [6, 3, 12, 5, 8], width=0.4, ec="none", fc="#7fb069")

plt.title("雙色的長條圖")


# 第五張圖
plt.subplot(235)

x = np.arange(0.6, 6)
A = np.random.randint(1, 15, 6)
B = np.random.randint(1, 15, 6)
plt.barh(x, A, fc="#e63946", ec="none")
plt.barh(x, -B, fc="#7fb069", ec="none")

plt.title("雙向的長條圖")


# 第六張圖
plt.subplot(236)


plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(
    num="bar 集合 6 並列",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

areas = ["北部", "中部", "南部", "東部"]
width = 0.4
x1 = [x - width / 2 for x in range(len(areas))]
x2 = [x + width / 2 for x in range(len(areas))]
data1 = [800000, 580000, 640000, 420000]
data2 = [750000, 460000, 680000, 340000]
plt.bar(x1, data1, width, label="上半年")
plt.bar(x2, data2, width, label="下半年")
plt.xticks(range(len(areas)), labels=areas)

plt.legend()


# 第二張圖
plt.subplot(232)

width = 0.25
listx = ["c", "c++", "c#", "java", "python"]

listx1 = [x - width / 2 for x in range(len(listx))]
listy1 = [25, 20, 20, 16, 28]
plt.bar(listx1, listy1, width, label="男")

listx2 = [x + width / 2 for x in range(len(listx))]
listy2 = [20, 8, 18, 16, 22]
plt.bar(listx2, listy2, width, label="女")

plt.xticks(range(len(listx)), labels=listx)

plt.legend()


# 第三張圖
plt.subplot(233)


# 第四張圖
plt.subplot(234)

N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
ind = np.arange(N)  # the x locations for the groups
width = 0.35
# fig = plt.figure()
# ax = fig.add_axes([0, 0, 1, 1])
plt.bar(ind, menMeans, width, color="r")
plt.bar(ind, womenMeans, width, bottom=menMeans, color="b")
plt.ylabel("Scores")
plt.title("Scores by group and gender")
plt.xticks(ind, ("G1", "G2", "G3", "G4", "G5"))
plt.yticks(np.arange(0, 81, 10))
plt.legend(labels=["Men", "Women"])


# 第五張圖
plt.subplot(235)


# from basic_units import cm, inch

cm = 1
inch = cm * 0.039

N = 5
ind = np.arange(N)  # the x locations for the groups
width = 0.35  # the width of the bars
men_means = [150 * cm, 160 * cm, 146 * cm, 172 * cm, 155 * cm]
men_std = [20 * cm, 30 * cm, 32 * cm, 10 * cm, 20 * cm]
plt.bar(x=ind, height=men_means, width=width, bottom=0 * cm, yerr=men_std, label="Men")
women_means = (145 * cm, 149 * cm, 172 * cm, 165 * cm, 200 * cm)
women_std = (30 * cm, 25 * cm, 20 * cm, 31 * cm, 22 * cm)
plt.bar(
    x=ind + width,
    height=women_means,
    width=width,
    bottom=0 * cm,
    yerr=women_std,
    label="Women",
)
plt.title("Scores by group and gender")
plt.xticks(ind, ("G1", "G2", "G3", "G4", "G5"))
plt.legend()


# 第六張圖
plt.subplot(236)


plt.show()

print("------------------------------------------------------------")  # 60個
plt.figure(
    num="bar 集合 7 堆疊圖 疊加長條圖",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

"""
疊加長條圖的應用
疊加長條圖是繪製出兩個長條圖，並以推疊的方式繪製而出的
設定將使用的數值，因為這邊需要兩組數值，因此有 y1, y2
"""

x = ["鼠", "牛", "虎", "兔", "龍"]
y1 = [3, 48, 33, 8, 38]
y2 = [3, 48, 33, 8, 38]

# 將兩條長條圖繪製出來，其中第二條 y2 的 y 軸基底座標是建立在 y1 上

plt.bar(x, y1, width=0.5, label="第一群")
plt.bar(x, y2, width=0.5, bottom=y1, label="第二群")
plt.legend()


# 第二張圖
plt.subplot(232)

# 繪製堆疊長條圖
x = [1, 2, 3, 4, 5]
y1 = [3, 48, 33, 8, 38]
y2 = [3, 48, 33, 8, 38]

labels = ["鼠", "牛", "虎", "兔", "龍"]  # x軸的刻度標籤
plt.bar(x, y1, tick_label=labels)  # 繪製 y1 長條圖
plt.bar(x, y2, tick_label=labels, bottom=y1)  # 繪製 y2 長條圖

plt.legend(("第一群", "第二群"))  # 顯示圖例來識別 y1 與 y2


# 第三張圖
plt.subplot(233)

x = [1, 2, 3, 4, 5]

# 疊加型的資料
y1 = [3, 48, 33, 8, 38]
y2 = [3, 48, 33, 8, 38]
y3 = [3, 48, 33, 8, 38]

plt.bar(x, y1, fc="#e63946", ec="none")
plt.bar(x, y2, fc="#7fb069", ec="none", bottom=y1)
plt.bar(x, y3, fc="#e55934", ec="none", bottom=np.add(y1, y2))
plt.legend(("第一群", "第二群", "第三群"))  # 顯示圖例來識別 y1 y2 y3

# 第四張圖
plt.subplot(234)

listx = ["中興大學", "成功大學", "東海大學", "逢甲大學"]
listy1 = [9093, 12010, 13090, 18176]
listy2 = [6370, 10815, 1667, 3265]

plt.bar(listx, listy1, width=0.5, label="大學部")
plt.bar(listx, listy2, width=0.5, bottom=listy1, label="研究所")
plt.legend()
plt.title("四校學生數")
plt.ylabel("人數")

plt.ylim((0, 28000))

student_all = {"中興大學": 15463, "成功大學": 22825, "東海大學": 14757, "逢甲大學": 21441}

for x, y in zip(range(len(student_all)), student_all.values()):
    plt.text(x - 0.05, y + 0.5, "{:>8,.0f}".format(y), ha="center")


# 第五張圖
plt.subplot(235)


def addlabels3(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i])


animals = ["鼠", "牛", "虎", "兔"]
weights1 = [3, 48, 33, 8]
weights2 = [3, 48, 33, 8]

# 產生總分list，總分相加
weights_sum = list(np.array(weights1) + np.array(weights2))

width = 0.35  # 柱寬度

plt.ylim(0, 100)
# 柱狀圖下層
plt.bar(animals, weights1, width, label="體重1")
# 柱狀圖上層
plt.bar(animals, weights2, width, bottom=weights1, label="體重2")
addlabels3(animals, weights1)
addlabels3(animals, weights_sum)
plt.ylabel("體重")
plt.title("體重統計圖(累計)")
plt.legend()

# 第六張圖
plt.subplot(236)


def addlabels4(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i])


animals = ["鼠", "牛", "虎", "兔"]
weights1 = [3, 48, 33, 8]
weights2 = [3, 48, 33, 8]
# 產生總分list，總分相加
weights_sum = list(np.array(weights1) + np.array(weights2))

width = 0.35  # 柱寬度

plt.ylim(0, 100)
# 柱狀圖下層
plt.bar(animals, weights1, width, label="體重1")
# 柱狀圖上層
plt.bar(animals, weights2, width, bottom=weights1, label="體重2")
addlabels4(animals, weights1)
addlabels4(animals, weights_sum)

# 將圖例說明對齊右邊中間
plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))

plt.title("體重累計圖")

plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(
    num="bar 集合 8 new 1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

AAA = [3367, 4120, 5539]  # AAA線條
BBB = [4000, 3590, 4423]  # BBB線條
CCC = [5200, 4930, 5350]  # CCC線條

X = np.arange(len(AAA))
labels = ["2023年", "2024年", "2025年"]  # 年度刻度標籤
# fig = plt.figure()
# ax = fig.add_axes([0.15,0.15,0.7,0.7])
barW = 0.22  # 長條圖寬度

"""
plt.bar(X+0.00,AAA,color='r',width=barW,label='AAA')
plt.bar(X+barW,BBB,color='g',width=barW,label='BBB')
plt.bar(X+barW*2,CCC,color='b',width=barW,label='CCC')
"""
plt.bar(X + 0.0, AAA, color="r", width=barW, label="AAA")
plt.bar(X + 0.25, BBB, color="g", width=barW, label="BBB")
plt.bar(X + 0.5, CCC, color="b", width=barW, label="CCC")

plt.title("銷售報表(並列)")
plt.xlabel("年度")
plt.ylabel("數量")
plt.legend()  # 繪製圖例
plt.xticks(X + barW, labels)  # 加註年度標籤


# 第二張圖
plt.subplot(232)

AAA = [3367, 4120, 5539]  # AAA線條
BBB = [4000, 3590, 4423]  # BBB線條
CCC = [5200, 4930, 5350]  # CCC線條
year = ["2023年", "2024年", "2025年"]  # 年度

barW = 0.35  # 長條圖寬度
plt.bar(year, AAA, color="green", width=barW, label="AAA")
plt.bar(year, BBB, color="yellow", width=barW, bottom=np.array(AAA), label="BBB")
plt.bar(
    year,
    CCC,
    color="red",
    width=barW,
    bottom=np.array(AAA) + np.array(BBB),
    label="CCC",
)
plt.title("銷售報表(累計)")
plt.xlabel("年度")
plt.ylabel("數量")
plt.legend()


# 第三張圖
plt.subplot(233)

AAA = [3367, 4120, 5539]  # AAA線條
BBB = [4000, 3590, 4423]  # BBB線條
CCC = [5200, 4930, 5350]  # CCC線條

X = np.arange(len(AAA))
labels = ["2023年", "2024年", "2025年"]  # 年度刻度標籤
# fig = plt.figure()
# ax = fig.add_axes([0.15,0.15,0.7,0.7])
barH = 0.25  # 橫條圖高度

plt.barh(X + 0.00, AAA, color="r", height=barH, label="AAA")
plt.barh(X + barH, BBB, color="g", height=barH, label="BBB")
plt.barh(X + barH * 2, CCC, color="b", height=barH, label="CCC")

plt.title("銷售報表")
plt.xlabel("數量")
plt.ylabel("年度")
plt.legend()  # 繪製圖例

plt.yticks(X + barH, labels)  # 加註年度標籤


# 第四張圖
plt.subplot(234)

AAA = [3367, 4120, 5539]  # AAA線條
BBB = [4000, 3590, 4423]  # BBB線條
CCC = [5200, 4930, 5350]  # CCC線條
year = ["2023年", "2024年", "2025年"]  # 年度

barH = 0.35  # 橫條圖高度
plt.barh(year, AAA, color="green", height=barH, label="AAA")
plt.barh(year, BBB, color="yellow", height=barH, left=np.array(AAA), label="BBB")
plt.barh(
    year, CCC, color="red", height=barH, left=np.array(AAA) + np.array(BBB), label="CCC"
)

plt.title("銷售報表")
plt.xlabel("數量")
plt.ylabel("年度")
plt.legend()

# 第五張圖
plt.subplot(235)

labels = ["Python", "C++", "Java", "JS", "C", "C#"]
index = np.arange(len(labels))
ratings = [5.16, 5.73, 14.99, 3.17, 11.86, 4.45]
change = [1.12, 0.3, -1.69, 0.29, 3.41, -0.45]

index = np.arange(len(labels) * 2)
plt.bar(index[0::2], ratings, label="rating")
plt.bar(index[1::2], change, label="change", color="r")
plt.legend()
plt.xticks(index[0::2], labels)

# 第六張圖
plt.subplot(236)

labels = ["Python", "C++", "Java", "JS", "C", "C#"]
index = np.arange(len(labels)*2)
ratings = [5.168, 5.726, 14.988, 3.165, 11.857, 4.453]
change = [1.12, 0.3, -1.69, 0.29, 3.41, -0.45]
 
plt.bar(index[0::2], ratings, label="使用率")
plt.bar(index[1::2], change, label="增減值", color="r")
plt.legend()
plt.xticks(index[0::2], labels)
plt.ylabel("使用率")
plt.title("程式語言的使用率")

plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("新進")


"""
-----
from collections import Counter

cyl = [6, 6, 4, 6, 8, 6, 8, 4, 4, 6, 6, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 8, 8, 8, 8, 4, 4, 4, 8, 6, 8, 4]

labels, values = zip(*Counter(cyl).items())
indexes = np.arange(len(values))

plt.bar(indexes, values, width = 0.5)
plt.xticks(indexes, labels)

# 預設字體大小
plt.rc("font", size=15)
# 軸標題字體大小
plt.rc("axes", titlesize=30)
# 軸標籤字體大小
plt.rc("axes", labelsize=20)
# X軸刻度字體大小
plt.rc("xtick", labelsize=20)
# Y軸刻度字體大小
plt.rc("ytick", labelsize=20)


#plt.bar(listx2, listy2, color="red", label="女性")

plt.xlim(0, 20)
plt.ylim(0, 100)
"""


cc = np.arange(0.6, 5)
print(cc)

# 預設大小為6.4inches*4.8inches, 80dpi
# 指定 寬6.4inches, 高4.8inches, 160dpi
# fig, ax = plt.subplots(figsize=(6.4, 4.8), dpi=160)


money = [1.5e6, 2.5e6, 5.5e6, 7.0e6]


def millions(x, pos):
    # The two args are the value and tick position.
    return "${:1.1f}M".format(x * 1e-6)


fig, ax = plt.subplots()
# Use automatic FuncFormatter creation
ax.yaxis.set_major_formatter(millions)
ax.bar(["Bill", "Fred", "Mary", "Sue"], money, label="data1", align="edge")
ax.set_title("Bar chart")
ax.set_xlabel("Name")
ax.set_ylabel("Money")
ax.legend(loc=2)

plt.show()
