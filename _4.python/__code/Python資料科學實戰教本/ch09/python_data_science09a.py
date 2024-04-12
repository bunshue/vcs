"""
Python資料科學實戰教本



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
'''
days = range(0, 22, 3)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
plt.plot(days, celsius)
plt.title("軸範圍: " + str(plt.axis()))
plt.show()

plt.plot(days, celsius)
xmin, xmax, ymin, ymax = -5, 25, 15, 35
plt.axis([xmin, xmax, ymin, ymax])
plt.show()


print("------------------------------------------------------------")  # 60個

days = range(1, 9)
celsius_min = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
celsius_max = [27.6, 26.1, 22.5, 30.4, 29.5, 31.5, 35.1, 39.4]
plt.plot(days, celsius_min, "r-o",
         days, celsius_max, "g--o")
plt.xlabel("日")
plt.ylabel("攝氏溫度")
plt.axis([0, 10, 15, 40])
plt.show()

print("------------------------------------------------------------")  # 60個

days = range(1, 9)
celsius_min = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
celsius_max = [27.6, 26.1, 22.5, 30.4, 29.5, 31.5, 35.1, 39.4]
plt.plot(days, celsius_min, "r-o",
         days, celsius_max, "g--o")
plt.xlabel("日")
plt.ylabel("攝氏溫度")
plt.axis([0, 10, 15, 40])
plt.savefig("Celsius.png")
plt.show()

print("------------------------------------------------------------")  # 60個

days = range(1, 9)
celsius_min = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
celsius_max = [27.6, 26.1, 22.5, 30.4, 29.5, 31.5, 35.1, 39.4]
plt.plot(days, celsius_min, "r-o",
         days, celsius_max, "g--o")
plt.xlabel("日")
plt.ylabel("攝氏溫度")
plt.axis([0, 10, 15, 40])
plt.savefig("Celsius.svg")
plt.show()

print("------------------------------------------------------------")  # 60個

days = range(1, 9)
celsius_min = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
celsius_max = [27.6, 26.1, 22.5, 30.4, 29.5, 31.5, 35.1, 39.4]
plt.plot(days, celsius_min, "r-o",
         days, celsius_max, "g--o")
plt.xlabel("日")
plt.ylabel("攝氏溫度")
plt.axis([0, 10, 15, 40])
plt.savefig("Celsius.pdf")
plt.show()

print("------------------------------------------------------------")  # 60個

x = np.random.rand(1000)
y = np.random.rand(1000)
size = np.random.rand(1000) * 50
color = np.random.rand(1000)
plt.scatter(x, y, size, color)
plt.colorbar()
plt.show()

print("------------------------------------------------------------")  # 60個

labels = ["Python", "C++", "Java", "JS", "C", "C#"]
index = np.arange(len(labels))
ratings = [5.168, 5.726, 14.988, 3.165, 11.857, 4.453]
 
plt.bar(index, ratings)
plt.xticks(index, labels)
plt.ylabel("使用率")
plt.title("程式語言的使用率") 
plt.show()

print("------------------------------------------------------------")  # 60個

labels = ["Python", "C++", "Java", "JS", "C", "C#"]
index = np.arange(len(labels))
ratings = [5.168, 5.726, 14.988, 3.165, 11.857, 4.453]
 
plt.barh(index, ratings)
plt.yticks(index, labels)
plt.ylabel("使用率")
plt.title("程式語言的使用率") 
plt.show()

print("------------------------------------------------------------")  # 60個

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
'''

print("------------------------------------------------------------")  # 60個

#雙Y軸
x = np.linspace(0, 10, 50)
sinus = np.sin(x)
sinhs = np.sinh(x)
fig, ax = plt.subplots()
ax.plot(x, sinus, "r-o")
ax2 = ax.twinx()
ax2.plot(x, sinhs, "g--")
plt.show()


print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
sinhs = np.sinh(x)
fig, ax = plt.subplots()
ax.plot(x, sinus, "r-o")
ax.set_xlabel("x", color="green")
ax.set_ylabel("Sin(x)", color="red")
ax2 = ax.twinx()
ax2.plot(x, sinhs, "g--")
ax2.set_ylabel("Sinh(x)", color="blue")
plt.show()


print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
sinhs = np.sinh(x)
fig, ax = plt.subplots()
ax.plot(x, sinus, "r-o", label="Sin(x)")
ax.set_xlabel("x", color="green")
ax.set_ylabel("Sin(x)", color="red")
ax.legend(loc="best")
ax2 = ax.twinx()
ax2.plot(x, sinhs, "g--", label="Sinh(x)")
ax2.set_ylabel("Sinh(x)", color="blue")
ax2.legend(loc="best")
plt.show()


print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
sinhs = np.sinh(x)
fig, ax = plt.subplots()
lns1 = ax.plot(x, sinus, "r-o", label="Sin(x)")
ax.set_xlabel("x", color="green")
ax.set_ylabel("Sin(x)", color="red")
ax2 = ax.twinx()
lns2 = ax2.plot(x, sinhs, "g--", label="Sinh(x)")
ax2.set_ylabel("Sinh(x)", color="blue")
# 自行建立圖例來顯示所有標籤
lns = lns1 + lns2
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc="best")
plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
sinhs = np.sinh(x)
fig, ax = plt.subplots()
ax.plot(x, sinus, "r-o")
ax.set_xlabel("x", color="green")
ax.set_ylabel("Sin(x)", color="red")
ax2 = ax.twinx()
ax2.plot(x, sinhs, "g--")
ax2.set_ylabel("Sinh(x)", color="blue")
# 指定圖表標題文字
ax.set_title("Sin和Cos三角函數的波型", fontsize="large")
# 更改刻度的外觀
for tick in ax.xaxis.get_ticklabels():
    tick.set_fontsize("large")
    tick.set_fontname("Times New Roman")
    tick.set_color("blue")
    tick.set_weight("bold")   
plt.show()


print("------------------------------------------------------------")  # 60個

days = range(0, 22, 3)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
plt.plot(days, celsius)
plt.xlabel("日")
plt.ylabel("攝氏溫度")
locs1, labels = plt.xticks()
locs2, labels = plt.yticks()
plt.title(str(locs1) + "\n" + str(locs2))
plt.show()


print("------------------------------------------------------------")  # 60個

days = range(0, 22, 3)
celsius = [25.6, 23.2, 18.5, 28.3, 26.5, 30.5, 32.6, 33.1]
plt.plot(days, celsius)
plt.xlabel("日")
plt.ylabel("攝氏溫度")
plt.xticks(range(0, 25, 2))
plt.yticks(range(15, 35, 3))
plt.show()


print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 10, 50)
sinus = np.sin(x)
sinhs = np.sinh(x)
fig, ax = plt.subplots()
ax.plot(x, sinus, "r-o")
ax.set_xlabel("x", color="green")
ax.set_ylabel("Sin(x)", color="red")
ax2 = ax.twinx()
ax2.plot(x, sinhs, "g--")
ax2.set_ylabel("Sinh(x)", color="blue")
plt.xticks(range(0, 11))
ax.set_yticks(np.linspace(-1, 1, 10))
ax2.set_yticks(np.linspace(0, 12000, 10))
plt.show()


print("------------------------------------------------------------")  # 60個

data = [100, 110, 150, 170, 190, 200, 220]
s = pd.Series(data)
s.plot()
plt.show()

print("------------------------------------------------------------")  # 60個

data = [100, 110, 150, 170, 190, 200, 220]
weekday = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
s = pd.Series(data, index=weekday)
s.plot()
plt.show()

'''
weight = [3, 48,33,8,38,16,36,29,22,6,12,42]
animals = ["鼠牛虎兔龍蛇馬羊猴雞狗豬"]
'''

print("------------------------------------------------------------")  # 60個

dists = {"name": ["Zhongzheng", "Banqiao", "Taoyuan", "Beitun", 
                   "Annan", "Sanmin", "Daan", "Yonghe", 
                   "Bade", "Cianjhen", "Fengshan", 
                   "Xinyi", "Xindian"],
         "population": [159598, 551452, 441287, 275207,
                        192327, 343203, 309835, 222531,
                        198473, 189623, 359125, 
                        225561, 302070]}
df = pd.DataFrame(dists)
print(df) 
#df.to_html("ch9-4-2-01.html")  #df轉html
df.plot()

df2 = pd.DataFrame(dists, 
                   columns=["population"],
                   index=dists["name"])
print(df2)
#df2.to_html("ch9-4-2-02.html")  #df轉html
df2.plot()
plt.show()

print("------------------------------------------------------------")  # 60個

dists = {"name": ["Zhongzheng", "Banqiao", "Taoyuan", "Beitun", 
                   "Annan", "Sanmin", "Daan", "Yonghe", 
                   "Bade", "Cianjhen", "Fengshan", 
                   "Xinyi", "Xindian"],
         "population": [159598, 551452, 441287, 275207,
                        192327, 343203, 309835, 222531,
                        198473, 189623, 359125, 
                        225561, 302070]}

df = pd.DataFrame(dists, 
                   columns=["population"],
                   index=dists["name"])
print(df)
df.plot(xticks=range(len(df.index)),
        use_index=True)

df.plot(xticks=range(len(df.index)),
        use_index=True,
        rot=90)

plt.show()

print("------------------------------------------------------------")  # 60個

dists = {"區名": ["中正區", "板橋區", "桃園區", "北屯區", 
                  "安南區", "三民區", "大安區", "永和區", 
                  "八德區", "前鎮區", "鳳山區", 
                  "信義區", "新店區"],
         "人口": [159598, 551452, 441287, 275207,
                  192327, 343203, 309835, 222531,
                  198473, 189623, 359125, 
                  225561, 302070],
         "面積": [7.6071, 23.1373, 34.8046, 62.7034, 
                  107.2016, 19.7866, 11.3614, 5.7138, 
                  33.7111, 19.1207, 26.7590, 
                  11.2077, 120.2255]}

df = pd.DataFrame(dists, 
                  columns=["人口", "面積"],
                  index=dists["區名"])
print(df)
#df.to_html("ch9-4-3.html")  #df轉html
df["面積"] *= 1000
df.plot(xticks=range(len(df.index)),
        use_index=True,
        rot=45)

plt.show()


print("------------------------------------------------------------")  # 60個

dists = {"區名": ["中正區", "板橋區", "桃園區", "北屯區", 
                  "安南區", "三民區", "大安區", "永和區", 
                  "八德區", "前鎮區", "鳳山區", 
                  "信義區", "新店區"],
         "人口": [159598, 551452, 441287, 275207,
                  192327, 343203, 309835, 222531,
                  198473, 189623, 359125, 
                  225561, 302070],
         "面積": [7.6071, 23.1373, 34.8046, 62.7034, 
                  107.2016, 19.7866, 11.3614, 5.7138, 
                  33.7111, 19.1207, 26.7590, 
                  11.2077, 120.2255]}

df = pd.DataFrame(dists, 
                  columns=["人口", "面積"],
                  index=dists["區名"])
print(df)
fig, ax = plt.subplots()
fig.suptitle("分區統計")
ax.set_ylabel("人口")
ax.set_xlabel("分區")
ax2 = ax.twinx()
ax2.set_ylabel("面積")
df["人口"].plot( ax=ax, 
                 style="b--o",
                 use_index=True,
                 rot=90)
df["面積"].plot( ax=ax2, 
                 style="g-s",
                 use_index=True,
                 rot=90)
plt.show()

print("------------------------------------------------------------")  # 60個

data = [100, 110, 150, 170, 190, 200, 220]
s = pd.Series(data)
s.plot(kind="bar", rot=0)
plt.show()

print("------------------------------------------------------------")  # 60個

usage = {"os": ["Windows","Mac OS","Linux","Chrome OS","BSD"],
         "percentage": [88.78, 8.21, 2.32, 0.34, 0.02]}

df = pd.DataFrame(usage, 
                  columns=["percentage"],
                  index=usage["os"])
print(df)
df.to_html("ch9-4-4.html")
df.plot(kind="bar")

plt.show()

print("------------------------------------------------------------")  # 60個

fruits = ["蘋果","梨子","香蕉","橙子"]
percentage = [30, 10, 40, 20]

s = pd.Series(percentage, index=fruits, name="水果")
print(s)
s.plot(kind="pie")
plt.show()

print("------------------------------------------------------------")  # 60個

fruits = ["蘋果","梨子","香蕉","橙子"]
percentage = [30, 10, 40, 20]

s = pd.Series(percentage, index=fruits, name="水果")
print(s)
explode = [0.1, 0.3, 0.1, 0.3]
s.plot(kind="pie",
       figsize=(6, 6),
       explode=explode)
plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)
df = pd.DataFrame({"x":x, "y":y})
df.plot(kind="scatter", x="x", y="y", 
        title="Sin(x)")
plt.show()


print("------------------------------------------------------------")  # 60個

iris = pd.read_csv("iris.csv")

iris.boxplot(column="sepal_length",
             by="target",
             figsize=(6,5))
plt.show()

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
