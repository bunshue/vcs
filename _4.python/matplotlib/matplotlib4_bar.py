# bar 集合 長條圖與橫條圖

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
#          編號              圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
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
plt.bar(x, y, width=0.5, color="red")  # 直向bar圖
# plt.bar(x, y, fc = '#e55934', ec = 'none')      #直向bar圖
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
    "蛇": 16,
    "馬": 36,
    "羊": 29,
    "猴": 22,
    "雞": 6,
    "狗": 12,
    "豬": 42,
}

plt.bar(range(len(animals.values())), animals.values(), width=0.8)
plt.xticks(range(len(animals.values())), animals.keys())

# 第四張圖
plt.subplot(234)

"""
#疊加長條圖的應用
#疊加長條圖是繪製出兩個長條圖，並以推疊的方式繪製而出的
#設定將使用的數值，因為這邊需要兩組數值，因此有 y1, y2
"""

x = ["鼠", "牛", "虎", "兔", "龍"]
y1 = [3, 48, 33, 8, 38]
y2 = [10, 32, 25, 15, 30]

# 將兩條長條圖繪製出來，其中第二條 y2 的 y 軸基底座標是建立在 y1 上

plt.bar(x, y1, width=0.5, label="第一群")
plt.bar(x, y2, width=0.5, bottom=y1, label="第二群")

plt.legend()

# 第五張圖
plt.subplot(235)

width = 0.25
listx = ["c", "c++", "c#", "java", "python"]
listx1 = [x - width / 2 for x in range(len(listx))]
listx2 = [x + width / 2 for x in range(len(listx))]
listy1 = [25, 20, 20, 16, 28]
listy2 = [20, 8, 18, 16, 22]

plt.bar(listx1, listy1, width, label="男")
plt.bar(listx2, listy2, width, label="女")

plt.xticks(range(len(listx)), labels=listx)

plt.legend()

# 第六張圖
plt.subplot(236)

listx1 = [1, 5, 7, 9, 13, 16]
listy1 = [15, 50, 80, 40, 70, 50]
plt.bar(listx1, listy1, label="男性")

listx2 = [2, 6, 8, 11, 14, 16]
listy2 = [10, 40, 30, 50, 80, 60]
plt.bar(listx2, listy2, color="red", label="女性")

plt.legend()
plt.xlim(0, 20)
plt.ylim(0, 100)

plt.show()

print("------------------------------------------------------------")  # 60個
#          編號              圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
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

labels = ["Python", "C++", "Java", "JS", "C", "C#"]
index = np.arange(len(labels))
ratings = [5.16, 5.73, 14.99, 3.17, 11.86, 4.45]
change = [1.12, 0.3, -1.69, 0.29, 3.41, -0.45]

index = np.arange(len(labels) * 2)
plt.bar(index[0::2], ratings, label="rating")
plt.bar(index[1::2], change, label="change", color="r")
plt.legend()
plt.xticks(index[0::2], labels)

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

n = 10
x = [i for i in range(0, n + 1)]  # 長條圖x軸座標
y = x
width = 0.35  # 長條圖寬度
plt.xticks(x)
plt.bar(x, y, width, color="g")  # 繪製長條圖

# 第五張圖
plt.subplot(235)

listx1 = [1, 5, 7, 9, 13, 16]
listy1 = [15, 50, 80, 40, 70, 50]
plt.bar(listx1, listy1, label="男性")

listx2 = [2, 6, 8, 11, 14, 16]
listy2 = [10, 40, 30, 50, 80, 60]
plt.bar(listx2, listy2, color="red", label="女性")

plt.legend()

plt.xlim(0, 20)
plt.ylim(0, 100)

# 第六張圖
plt.subplot(236)

# 繪製堆疊長條圖

x = [1, 2, 3, 4, 5, 6]
y1 = [12, 41, 32, 36, 21, 17]
y2 = [43, 1, 6, 17, 17, 9]

labels = ["Apple", "Orange", "Banana", "Pineapple", "Kiwifruit", "Strawberry"]
plt.bar(x, y1, tick_label=labels)  # 繪製 y1 長條圖
plt.bar(x, y2, tick_label=labels, bottom=y1)  # 繪製 y2 長條圖

plt.legend(("y1", "y2"))  # 顯示圖例來識別 y1 與 y2

plt.show()

print("------------------------------------------------------------")  # 60個
#          編號              圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
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

weights = [3, 48, 33, 8, 38]
plt.bar(range(1, 6), weights)

# 第二張圖
plt.subplot(232)

plt.bar(np.arange(0.6, 5), weights)


# 第三張圖
plt.subplot(233)

# 雙色的長條圖
x = np.arange(1, 6)
plt.bar(x - 0.4, [3, 10, 8, 12, 6], width=0.4, ec="none", fc="#e63946")
plt.bar(x, [6, 3, 12, 5, 8], width=0.4, ec="none", fc="#7fb069")

# 第四張圖
plt.subplot(234)

# 疊加型的資料
A = np.random.randint(2, 15, 5)
B = np.random.randint(2, 15, 5)
C = np.random.randint(2, 15, 5)

plt.bar(x, A, fc="#e63946", ec="none")
plt.bar(x, B, fc="#7fb069", ec="none", bottom=A)
plt.bar(x, C, fc="#e55934", ec="none", bottom=A + B)

# 第五張圖
plt.subplot(235)

# 設定長條圖橫軸標籤
x = [1, 2, 3, 4, 5, 6]
y = [12, 41, 32, 36, 21, 17]
labels = ["Apple", "Orange", "Banana", "Pineapple", "Kiwifruit", "Strawberry"]
plt.bar(x, y, tick_label=labels)

# 第六張圖
plt.subplot(236)

# 雙向的長條圖
x = np.arange(0.6, 6)
A = np.random.randint(1, 15, 6)
B = np.random.randint(1, 15, 6)
plt.barh(x, A, fc="#e63946", ec="none")
plt.barh(x, -B, fc="#7fb069", ec="none")

plt.show()

print("------------------------------------------------------------")  # 60個
#          編號              圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
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

# 第二張圖
plt.subplot(232)

width = 0.25
listx = ["c", "c++", "c#", "java", "python"]
listx1 = [x - width / 2 for x in range(len(listx))]
listx2 = [x + width / 2 for x in range(len(listx))]
listy1 = [25, 20, 20, 16, 28]
listy2 = [20, 8, 18, 16, 22]
plt.bar(listx1, listy1, width, label="男")
plt.bar(listx2, listy2, width, label="女")
plt.xticks(range(len(listx)), labels=listx)
plt.legend()
plt.title("資訊程式課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")

# 第三張圖
plt.subplot(233)

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

# 第四張圖
plt.subplot(234)

print("將字典直接輸出給bar圖")

data = {"apples": 10, "oranges": 15, "lemons": 5, "limes": 20}
plt.bar(list(data.keys()), list(data.values()))

# 第五張圖
plt.subplot(235)

print("將字典直接輸出給barh圖, 加error")

data = {"apples": 10, "oranges": 15, "lemons": 5, "limes": 20}
error = [3, 4, 2, 7]
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

# 堆疊圖
y1 = (20, 35, 30, 35, 27)
y2 = (25, 32, 34, 20, 25)
x = np.arange(len(y1))
width = 0.35
p1 = plt.bar(x, y1, width)
p2 = plt.bar(x, y2, width, bottom=y1)  # 堆疊圖


plt.show()

print("------------------------------------------------------------")  # 60個

#          編號              圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
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

x = ["理工學院", "外語學院", "管理學院", "文學院"]
s1 = [540, 2800, 1864, 1285]
s2 = [489, 2968, 1908, 1300]
s = [s1[0] + s2[0], s1[1] + s2[1], s1[2] + s2[2], s1[3] + s2[3]]
print(s)
plt.bar(x, s)
plt.ylabel("總人數(單位:人)")
plt.title("卓越綜合大學通過英檢中高級人數")

# 第二張圖
plt.subplot(232)

x = ["理工學院", "外語學院", "管理學院", "文學院"]
s1 = [540, 2800, 1864, 1285]
s2 = [489, 2968, 1908, 1300]
s = [s1[0] + s2[0], s1[1] + s2[1], s1[2] + s2[2], s1[3] + s2[3]]
plt.bar(x, s, width=0.8, align="edge", color="r", ec="y", lw=2)
plt.ylabel("總人數(單位:人)")
plt.title("卓越綜合大學通過英檢中高級人數")

# 第三張圖
plt.subplot(233)

x = ["理工學院", "外語學院", "管理學院", "文學院"]
s1 = [540, 2800, 1864, 1285]
s2 = [489, 2968, 1908, 1300]
s = [s1[0] + s2[0], s1[1] + s2[1], s1[2] + s2[2], s1[3] + s2[3]]
plt.bar(x, s, width=0.8, align="edge", color="r", ec="y", lw=2)
plt.ylabel("總人數(單位:人)")
plt.title("卓越綜合大學通過英檢中高級人數")


# 第四張圖
plt.subplot(234)

votes = [135, 412, 397]  # 得票數
N = len(votes)  # 計算長度
x = np.arange(N)  # 長條圖x軸座標
width = 0.35  # 長條圖寬度

plt.bar(x, votes, width)  # 繪製長條圖

plt.xticks(x, ("James", "Peter", "Norton"))
plt.yticks(np.arange(0, 450, 30))
plt.title("x用名稱 y設定範圍刻距")

# 第五張圖
plt.subplot(235)


def dice_generator(times, sides):
    # 處理隨機數
    for i in range(times):
        ranNum = random.randint(1, sides)  # 產生1-6隨機數
        dice.append(ranNum)


def dice_count(sides):
    # 計算1-6個出現次數
    for i in range(1, sides + 1):
        frequency = dice.count(i)  # 計算i出現在dice串列的次數
        frequencies.append(frequency)


times = 600  # 擲骰子次數
sides = 6  # 骰子有幾面
dice = []  # 建立擲骰子的串列
frequencies = []  # 儲存每一面骰子出現次數串列
dice_generator(times, sides)  # 產生擲骰子的串列
dice_count(sides)  # 將骰子串列轉成次數串列
x = np.arange(6)  # 長條圖x軸座標
width = 0.35  # 長條圖寬度
plt.bar(x, frequencies, width, color="g")  # 繪製長條圖
plt.ylabel("Frequency")
plt.title("丟骰子600次")
plt.xticks(x, ("1", "2", "3", "4", "5", "6"))
plt.yticks(np.arange(0, 150, 15))


# 第六張圖
plt.subplot(236)

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


plt.show()


print("------------------------------------------------------------")  # 60個

#          編號              圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="bar 集合 6",
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

x = ["第一季", "第二季", "第三季", "第四季"]
s = [20000, 15000, 17000, -8000]
plt.barh(x, s, color="red")
plt.ylabel("季別")
plt.xlabel("損益金額")
plt.title("今年度營業獲利的概況")


# 第四張圖
plt.subplot(234)

x = ["第1學期", "第2學期", "第3學期", "第4學期", "第5學期", "第6學期", "第7學期", "第8學期"]
s = [95.3, 94.2, 91.4, 96.2, 92.3, 93.6, 89.4, 91.2]
plt.barh(x, s)
plt.ylabel("平均分數")
plt.title("大學四年各學期的平均分數")


# 第五張圖
plt.subplot(235)

x = ["第一季", "第二季", "第三季", "第四季"]
s = [20000, 15000, 17000, -8000]
plt.barh(x, s, color="red")
plt.ylabel("季別")
plt.xlabel("損益金額")
plt.title("今年度營業獲利的概況")


# 第六張圖
plt.subplot(236)

x = ["第1學期", "第2學期", "第3學期", "第4學期", "第5學期", "第6學期", "第7學期", "第8學期"]
s = [95.3, 94.2, 91.4, 96.2, 92.3, 93.6, 89.4, 91.2]
plt.bar(x, s, width=0.5, align="edge", color="r", ec="y", lw=2)
plt.ylabel("平均分數")
plt.title("大學四年各學期的平均分數")


plt.show()

print("------------------------------------------------------------")  # 60個

#          編號              圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="bar 集合 7",
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
plt.bar(name, weight)

plt.ylabel("體重(單位:公斤)")
plt.title("動物體重 使用中文")


# 第二張圖
plt.subplot(232)

name = ["鼠", "牛", "虎", "兔", "龍"]
weight = [3, 48, 33, 8, 38]

plt.bar(name, weight, width=0.8, align="edge", color="r", ec="y", lw=2)

plt.ylabel("體重(單位:公斤)")
plt.title("動物體重 使用中文")


# 第三張圖
plt.subplot(233)

name = ["鼠", "牛", "虎", "兔", "龍"]
weight = [3, 48, 33, 8, 38]

plt.bar(name, weight, width=0.8, align="edge", color="r", ec="y", lw=2)

plt.ylabel("體重(單位:公斤)")
plt.title("動物體重 使用中文")


# 第四張圖
plt.subplot(234)

votes = [135, 412, 397]  # 得票數
N = len(votes)  # 計算長度
x = np.arange(N)  # 長條圖x軸座標
width = 0.35  # 長條圖寬度
plt.bar(x, votes, width)  # 繪製長條圖

plt.ylabel("得票數")
plt.title("選舉結果")
plt.xticks(x, ("James", "Peter", "Norton"))  # x 軸刻度
plt.yticks(np.arange(0, 450, 30))  # y 軸刻度


# 第五張圖
plt.subplot(235)

x = ["第1學期", "第2學期", "第3學期", "第4學期", "第5學期", "第6學期", "第7學期", "第8學期"]
s = [95.3, 94.2, 91.4, 96.2, 92.3, 93.6, 89.4, 91.2]
plt.barh(x, s)
plt.ylabel("平均分數")
plt.title("大學四年各學期的平均分數")


# 第六張圖
plt.subplot(236)


plt.show()


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("新進")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
plt.xlabel('程式課程', fontsize="10") # 設定 x 軸標題內容及大小
plt.ylabel('選修人數', fontsize="10") # 設定 y 軸標題標題內容及大小

plt.xlabel('程式課程', fontsize="10") # 設定 x 軸標題內容及大小
plt.ylabel('選修人數', fontsize="10") # 設定 y 軸標題標題內容及大小
plt.title('資訊程式課程選修人數', fontsize="18") # 設定圖表標題內容及大小
-----
from collections import Counter

cyl = [6, 6, 4, 6, 8, 6, 8, 4, 4, 6, 6, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 8, 8, 8, 8, 4, 4, 4, 8, 6, 8, 4]

labels, values = zip(*Counter(cyl).items())
indexes = np.arange(len(values))

plt.bar(indexes, values, width = 0.5)
plt.xticks(indexes, labels)


"""

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("Bar圖")

money = [1.5e5, 2.5e6, 5.5e6, 2.0e7]


def millions(x, pos):
    """The two args are the value and tick position."""
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

print("------------------------------------------------------------")  # 60個

# from basic_units import cm, inch

cm = 1
inch = cm * 0.039

fig, ax = plt.subplots()
N = 5
ind = np.arange(N)  # the x locations for the groups
width = 0.35  # the width of the bars
men_means = [150 * cm, 160 * cm, 146 * cm, 172 * cm, 155 * cm]
men_std = [20 * cm, 30 * cm, 32 * cm, 10 * cm, 20 * cm]
ax.bar(x=ind, height=men_means, width=width, bottom=0 * cm, yerr=men_std, label="Men")
women_means = (145 * cm, 149 * cm, 172 * cm, 165 * cm, 200 * cm)
women_std = (30 * cm, 25 * cm, 20 * cm, 31 * cm, 22 * cm)
ax.bar(
    x=ind + width,
    height=women_means,
    width=width,
    bottom=0 * cm,
    yerr=women_std,
    label="Women",
)
ax.set_title("Scores by group and gender")
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(("G1", "G2", "G3", "G4", "G5"))
ax.legend()
ax.yaxis.set_units(inch)
ax.autoscale_view()

plt.show()

print("------------------------------------------------------------")  # 60個

N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
ind = np.arange(N)  # the x locations for the groups
width = 0.35
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
ax.bar(ind, menMeans, width, color="r")
ax.bar(ind, womenMeans, width, bottom=menMeans, color="b")
ax.set_ylabel("Scores")
ax.set_title("Scores by group and gender")
ax.set_xticks(ind, ("G1", "G2", "G3", "G4", "G5"))
ax.set_yticks(np.arange(0, 81, 10))
ax.legend(labels=["Men", "Women"])

plt.show()

print("------------------------------------------------------------")  # 60個


def dice_generator(times, sides):
    # 處理隨機數
    for i in range(times):
        ranNum = random.randint(1, sides)  # 產生1-6隨機數
        dice.append(ranNum)


def dice_count(sides):
    # 計算1-6個出現次數
    for i in range(1, sides + 1):
        frequency = dice.count(i)  # 計算i出現在dice串列的次數
        frequencies.append(frequency)


times = 600  # 擲骰子次數
sides = 6  # 骰子有幾面
dice = []  # 建立擲骰子的串列
frequencies = []  # 儲存每一面骰子出現次數串列
dice_generator(times, sides)  # 產生擲骰子的串列
dice_count(sides)  # 將骰子串列轉成次數串列
x = np.arange(6)  # 長條圖x軸座標
width = 0.35  # 長條圖寬度
plt.bar(x, frequencies, width, color="g")  # 繪製長條圖
plt.ylabel("次數")
plt.xlabel("骰子點數")
plt.title("測試 600 次")
plt.xticks(x, ("1", "2", "3", "4", "5", "6"))
plt.yticks(np.arange(0, 150, 15))

plt.show()

print("------------------------------------------------------------")  # 60個

# bar累計

areas = ["北部", "中部", "南部", "東部"]
data1 = [800000, 580000, 640000, 420000]
data2 = [750000, 460000, 680000, 340000]
plt.bar(areas, data1, label="上半年")
plt.bar(areas, data2, label="下半年", bottom=data1)

plt.legend()
plt.show()


print("------------------------------------------------------------")  # 60個

# bar並列

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
plt.show()

print("------------------------------------------------------------")  # 60個


def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i])


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
students = ["約翰", "瑪莉", "麥可", "大衛"]
math_scores = [78, 67, 90, 81]
# 預設大小為6.4inches*4.8inches, 80dpi
# 指定 寬6.4inches, 高4.8inches, 160dpi
fig, ax = plt.subplots(figsize=(6.4, 4.8), dpi=160)
ax.set_ylim(0, 100)
ax.bar(students, math_scores, color=["red", "green", "blue", "yellow"])
addlabels(students, math_scores)
ax.set(xlabel="學生", ylabel="數學成績")
ax.set_title("期末考")

plt.show()

print("------------------------------------------------------------")  # 60個


def addlabels(x, y):
    for i in range(len(x)):
        plt.text(y[i], i, y[i])


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
students = ["約翰", "瑪莉", "麥可", "大衛"]
math_scores = [78, 67, 90, 81]
# 預設大小為6.4inches*4.8inches, 80dpi
# 指定 寬6.4inches, 高4.8inches, 160dpi
fig, ax = plt.subplots(figsize=(6.4, 4.8), dpi=160)
ax.set_xlim(0, 100)
ax.barh(students, math_scores, color=["red", "green", "blue", "yellow"])
addlabels(students, math_scores)
ax.set(ylabel="學生", xlabel="數學成績")
ax.set_title("期末考")

plt.show()

print("------------------------------------------------------------")  # 60個


def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i])


# 軸標題字體大小
plt.rc("axes", titlesize=30)
# 軸標籤字體大小
plt.rc("axes", labelsize=20)
# X軸刻度字體大小
plt.rc("xtick", labelsize=20)
# Y軸刻度字體大小
plt.rc("ytick", labelsize=20)
students = ["約翰", "瑪莉", "麥可", "大衛"]
chin_scores = [78, 67, 90, 81]
math_scores = [85, 72, 94, 70]
# 產生總分list，總分相加
all_scores = list(np.array(chin_scores) + np.array(math_scores))
# 柱寬度
width = 0.35
# 預設大小為6.4inches*4.8inches, 80dpi
# 指定 寬6.4inches, 高4.8inches, 160dpi
fig, ax = plt.subplots(figsize=(6.4, 4.8), dpi=160)
ax.set_ylim(0, 200)
# 柱狀圖下層
ax.bar(students, chin_scores, width, label="國文")
# 柱狀圖上層
ax.bar(students, math_scores, width, bottom=chin_scores, label="數學")
addlabels(students, chin_scores)
addlabels(students, all_scores)
ax.set_xlabel("學生")
ax.set_ylabel("總分")
ax.set_title("分數統計圖")
ax.legend()

plt.show()

print("------------------------------------------------------------")  # 60個


def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i])


# 軸標題字體大小
plt.rc("axes", titlesize=30)
# 軸標籤字體大小
plt.rc("axes", labelsize=20)
# X軸刻度字體大小
plt.rc("xtick", labelsize=20)
# Y軸刻度字體大小
plt.rc("ytick", labelsize=20)
students = ["約翰", "瑪莉", "麥可", "大衛"]
chin_scores = [78, 67, 90, 81]
math_scores = [85, 72, 94, 70]
# 產生總分list，總分相加
all_scores = list(np.array(chin_scores) + np.array(math_scores))
# 柱寬度
width = 0.35
# 預設大小為6.4inches*4.8inches, 80dpi
# 指定 寬6.4inches, 高4.8inches, 160dpi
fig, ax = plt.subplots(figsize=(6.4, 4.8), dpi=160)
ax.set_ylim(0, 200)
# 柱狀圖下層
ax.bar(students, chin_scores, width, label="國文")
# 柱狀圖上層
ax.bar(students, math_scores, width, bottom=chin_scores, label="數學")
addlabels(students, chin_scores)
addlabels(students, all_scores)
# 縮小次圖比例為原來的80%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
# 將圖例說明對齊右邊中間
ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

courses = ['C++','Java','Python','C#','PHP']
students = [45, 52, 66, 32, 39]
plt.bar(courses,students)
plt.show()

print("------------------------------------------------------------")  # 60個

courses = ['C++','Java','Python','C#','PHP']
students = [45, 52, 66, 32, 39]
plt.bar(courses,students,align='edge',color='g')
plt.show()

print("------------------------------------------------------------")  # 60個

courses = ['C++','Java','Python','C#','PHP']
students = [45, 52, 66, 32, 39]
plt.bar(courses,students,width=1.0,color='m')
plt.show()

print("------------------------------------------------------------")  # 60個


def dice_generator(num, sides):
    ''' 處理隨機數 '''
    for i in range(num):              
        ranNum = np.random.randint(1, sides+1)    # 產生 1-6 隨機數
        dice.append(ranNum)
def dice_count(sides):
    '''計算1-6個出現次數'''
    for i in range(1, sides+1):
        frequency = dice.count(i)           # 計算i出現在dice串列的次數
        times.append(frequency)          
num = 600                                   # 擲骰子次數
sides = 6                                   # 骰子有幾面
dice = []                                   # 建立擲骰子的串列
times = []                                  # 儲存每一面骰子出現次數串列
dice_generator(num, sides)                  # 產生擲骰子的串列
dice_count(sides)                           # 將骰子串列轉成次數串列                          
x = np.arange(6)                            # 長條圖x軸座標
width = 0.35                                # 長條圖寬度
plt.bar(x,times,width,color='orange',hatch='o')  # 繪製長條圖
plt.ylabel('出現次數',color='b')
plt.title('測試 600次 ',fontsize=16,color='b')
plt.xticks(x, ('1', '2', '3', '4', '5', '6'), color='b')
plt.yticks(np.arange(0, 150, 15), color='b')

plt.show()

print("------------------------------------------------------------")  # 60個

Benz = [3367, 4120, 5539]                   # Benz線條
BMW = [4000, 3590, 4423]                    # BMW線條
Lexus = [5200, 4930, 5350]                  # Lexus線條

X = np.arange(len(Benz))
labels = ["2023年","2024年","2025年"]       # 年度刻度標籤
fig = plt.figure()
ax = fig.add_axes([0.15,0.15,0.7,0.7])
barW = 0.25                                 # 長條圖寬度

plt.bar(X+0.00,Benz,color='r',width=barW,label='Benz')
plt.bar(X+barW,BMW,color='g',width=barW,label='BMW')
plt.bar(X+barW*2,Lexus,color='b',width=barW,label='Lexus')

plt.title("銷售報表", fontsize=24, color='b')
plt.xlabel("年度", fontsize=14, color='b')
plt.ylabel("數量", fontsize=14, color='b')
plt.legend()                                 # 繪製圖例
plt.xticks(X+barW, labels)                   # 加註年度標籤

plt.show()

print("------------------------------------------------------------")  # 60個

Benz = [3367, 4120, 5539]                   # Benz線條
BMW = [4000, 3590, 4423]                    # BMW線條
Lexus = [5200, 4930, 5350]                  # Lexus線條

X = np.arange(len(Benz))
labels = ["2023年","2024年","2025年"]       # 年度刻度標籤
fig = plt.figure()
ax = fig.add_axes([0.15,0.15,0.7,0.7])
barW = 0.22                                 # 長條圖寬度

plt.bar(X+0.0,Benz,color='r',width=barW,label='Benz')
plt.bar(X+0.25,BMW,color='g',width=barW,label='BMW')
plt.bar(X+0.5,Lexus,color='b',width=barW,label='Lexus')

plt.title("銷售報表", fontsize=24, color='b')
plt.xlabel("年度", fontsize=14, color='b')
plt.ylabel("數量", fontsize=14, color='b')
plt.legend()                                # 繪製圖例
plt.xticks(X+barW, labels)                  # 加註年度標籤

plt.show()

print("------------------------------------------------------------")  # 60個

Benz = [3367, 4120, 5539]                       # Benz線條
BMW = [4000, 3590, 4423]                        # BMW線條
Lexus = [5200, 4930, 5350]                      # Lexus線條
year = ["2023年","2024年","2025年"]             # 年度  

barW = 0.35                                     # 長條圖寬度
plt.bar(year,Benz,color="green",width=barW,label="Benz")
plt.bar(year,BMW,color="yellow",width=barW,
        bottom=np.array(Benz),label="BMW")
plt.bar(year,Lexus,color="red",width=barW,
        bottom=np.array(Benz)+np.array(BMW),label="Lexus")
plt.title("銷售報表", fontsize=24, color='b')
plt.xlabel("年度", fontsize=14, color='b')
plt.ylabel("數量", fontsize=14, color='b')
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個

colors = ['grey','grey','red','grey','grey']
courses = ['C++','Java','Python','C#','PHP']
students = [45, 52, 66, 32, 39]
plt.bar(courses,students,color=colors)
plt.title("修課報表", fontsize=24, color='b')
plt.xlabel("課程名稱", fontsize=14, color='b')
plt.ylabel("修課人數", fontsize=14, color='b')

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
ax = fig.add_axes([0.15,0.15,0.7,0.7])
colors = ['b','g','r','y','c']
courses = ['C++','Java','Python','C#','PHP']
students = [45, 52, 66, 32, 39]
plt.barh(courses,students,color=colors)

plt.title("修課報表", fontsize=24, color='b')
plt.xlabel("修課人數", fontsize=12, color='b')
plt.ylabel("課程名稱", fontsize=12, color='b')

plt.show()

print("------------------------------------------------------------")  # 60個

Benz = [3367, 4120, 5539]                   # Benz線條
BMW = [4000, 3590, 4423]                    # BMW線條
Lexus = [5200, 4930, 5350]                  # Lexus線條

X = np.arange(len(Benz))
labels = ["2023年","2024年","2025年"]       # 年度刻度標籤
fig = plt.figure()
ax = fig.add_axes([0.15,0.15,0.7,0.7])
barH = 0.25                                 # 橫條圖高度
plt.barh(X+0.00,Benz,color='r',height=barH,label='Benz')
plt.barh(X+barH,BMW,color='g',height=barH,label='BMW')
plt.barh(X+barH*2,Lexus,color='b',height=barH,label='Lexus')
plt.title("銷售報表", fontsize=24, color='b')
plt.xlabel("數量", fontsize=14, color='b')
plt.ylabel("年度", fontsize=14, color='b')
plt.legend()                                 # 繪製圖例
plt.yticks(X+barH, labels)                   # 加註年度標籤

plt.show()

print("------------------------------------------------------------")  # 60個

Benz = [3367, 4120, 5539]                   # Benz線條
BMW = [4000, 3590, 4423]                    # BMW線條
Lexus = [5200, 4930, 5350]                  # Lexus線條
year = ["2023年","2024年","2025年"]         # 年度  

barH = 0.35                                 # 橫條圖高度
plt.barh(year,Benz,color="green",height=barH,label="Benz")
plt.barh(year,BMW,color="yellow",height=barH,
        left=np.array(Benz),label="BMW")
plt.barh(year,Lexus,color="red",height=barH,
        left=np.array(Benz)+np.array(BMW),label="Lexus")
plt.title("銷售報表", fontsize=24, color='b')
plt.xlabel("數量", fontsize=12, color='b')
plt.ylabel("年度", fontsize=12, color='b')
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個

revenue = [300, 320, 400, 350]
cost = [250, 280, 310, 290]
quarter = ['Q1','Q2','Q3','Q4']

barH = 0.5
plt.barh(quarter,revenue,color='g',height=barH,label='收入')
plt.barh(quarter,-np.array(cost),color='m',height=barH,label='支出')
plt.title("公司收支表", fontsize=24, color='b')
plt.xlabel("收入與支出", fontsize=14, color='b')
plt.ylabel("季度", fontsize=14, color='b')
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個

N = 20                                      # 長條個數
theta = np.linspace(0.0, 2 * np.pi, N)      # 角度個數  
radius = 10 * np.random.rand(N)             # 半徑個數
width = np.pi / 4 * np.random.rand(N)       # 寬度個數
colors = plt.cm.hsv(radius / 10)            # 色彩個數
ax = plt.subplot(projection='polar')        # 建立子圖
# 繪製極座標長條圖
ax.bar(theta,radius,width,bottom=0.0,alpha=0.8,color=colors)

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
