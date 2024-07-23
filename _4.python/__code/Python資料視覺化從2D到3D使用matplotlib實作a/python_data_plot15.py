"""
# plot 集合
第15章：圓餅圖

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

area = ["大陸", "東南亞", "東北亞", "美國", "歐洲", "澳紐"]
people = [10000, 12600, 9600, 7500, 5100, 4800]
"""
plt.pie(people, labels=area)
plt.pie(people, labels=area, autopct="%d%%")
plt.pie(people, labels=area, autopct="%1.2f%%")
exp = [0.0, 0.0, 0.0, 0.0, 0.0, 0.1]
plt.pie(people, labels=area, explode=exp, autopct="%1.2f%%")

exp = [0.0, 0.0, 0.1, 0.0, 0.0, 0.1]
plt.pie(people, labels=area, explode=exp, autopct="%1.2f%%")

exp = [0.0, 0.0, 0.0, 0.0, 0.0, 0.1]
plt.pie(people, labels=area, explode=exp, autopct="%1.2f%%", startangle=90)

exp = [0.0, 0.0, 0.0, 0.0, 0.0, 0.1]
plt.pie(people, labels=area, explode=exp, autopct="%1.2f%%", startangle=90, shadow=True)

exp = [0.0, 0.0, 0.1, 0.0, 0.0, 0.1]
colors = ["#ff9999", "#66b4ff", "#99ff88", "#ffcc99", "#00ffff", "#ff00ff"]
plt.pie(people, labels=area, explode=exp, autopct="%1.2f%%", colors=colors)

exp = [0.0, 0.0, 0.1, 0.0, 0.0, 0.1]
piecolors = ["aqua", "g", "pink", "yellow", "m", "salmon"]
patches, texts, autotexts = plt.pie(
    people, labels=area, explode=exp, autopct="%1.2f%%", colors=piecolors
)
for txt in texts:  # 設定標籤顏色
    txt.set_color("m")

exp = [0.0, 0.0, 0.1, 0.0, 0.0, 0.1]
patches, texts, autotexts = plt.pie(people, labels=area, explode=exp, autopct="%1.2f%%")
for txt in texts:  # 設定標籤顏色
    txt.set_color("m")
for txt in autotexts:  # 設定百分比顏色
    txt.set_color("w")

exp = [0.0, 0.0, 0.1, 0.0, 0.0, 0.1]
patches, texts, autotexts = plt.pie(people, labels=area, explode=exp, autopct="%1.2f%%")
for txt in texts:  # 設定標籤
    txt.set_color("m")  # 色彩設定
    txt.set_size(14)  # 字型大小
for txt in autotexts:  # 設定百分比
    txt.set_color("w")  # 色彩設定
    txt.set_size(12)  # 字型大小
"""

"""
patches = plt.pie(people, labels=area, autopct="%1.2f%%")
for edgecolor in patches[0]:
    edgecolor.set_edgecolor("w")  # 設定圓餅邊界線是白色
plt.title("使用 set_edgecolor() 函數", fontsize=16, color="b")
"""
"""
plt.pie(people, labels=area, autopct="%1.2f%%", wedgeprops={"edgecolor": "w"})
plt.title("使用 wedgeprops 字典", fontsize=16, color="b")
"""

"""
plt.pie(people, labels=area, autopct="%1.2f%%", wedgeprops={"ec": "w", "lw": 5})
plt.title("使用 wedgeprops ec 和 lw", fontsize=16, color="b")
"""

#plt.title("五月份國外旅遊調查表", fontsize=16, color="b")

"""
fig, axs = plt.subplots(nrows=2, ncols=2)  # 建立 2 x 2 子圖
# 建立 [0,0]子圖
axs[0, 0].pie(
    people, labels=area, autopct="%1.2f%%", wedgeprops={"ec": "w", "hatch": "-"}
)
axs[0, 0].set_title("hatch = '-'", color="m")
# 建立 [0,1]子圖
axs[0, 1].pie(
    people, labels=area, autopct="%1.2f%%", wedgeprops={"ec": "w", "hatch": "+"}
)
axs[0, 1].set_title("hatch = '+'", color="m")
# 建立 [1,0]子圖
axs[1, 0].pie(
    people, labels=area, autopct="%1.2f%%", wedgeprops={"ec": "w", "hatch": "o"}
)
axs[1, 0].set_title("hatch = 'o'", color="m")
# 建立 [1,1]子圖
axs[1, 1].pie(
    people, labels=area, autopct="%1.2f%%", wedgeprops={"ec": "w", "hatch": "*"}
)
axs[1, 1].set_title("hatch = '*'", color="m")
plt.suptitle("使用 wedgeprops 字典的 hatch 參數", fontsize=16, color="b")

fig.tight_layout()

"""

"""
plt.pie(people, labels=area, autopct="%1.2f%%")
plt.title("使用 plt.axis() 函數", fontsize=16, color="b")
plt.axis("equal")  # 圓餅圖保持圓形
"""

"""
fig, ax = plt.subplots()
ax.pie(people, labels=area, autopct="%1.2f%%")
ax.set_title("使用 ax.set() 函數", fontsize=16, color="b")
ax.set(aspect="equal")  # 圓餅圖保持圓形
"""

plot.show()

print("------------------------------------------------------------")  # 60個

sorts = ["交通", "娛樂", "教育", "交通", "餐費"]
fee = [8000, 2000, 3000, 5000, 6000]
fee_no = [1, 0, 0, 0]
plt.pie(fee, pctdistance=0.8, labels=sorts, autopct="%1.2f%%")
plt.pie(fee_no, radius=0.6, colors="w")
plt.title("統計個人花費的環圈圖設計", fontsize=16, color="b")
plt.show()


print("------------------------------------------------------------")  # 60個

lang = ["Python", "C", "Java", "C++", "PHP"]  # 程式語言標籤
people = [350, 200, 250, 150, 270]  # 人數
labelgender = ["男生", "女生"]  # 性別標籤
gender = [720, 500]  # 性別人數
colors = ["lightyellow", "lightgreen"]  # 自定性別色彩
# 建立外層程式語言圓餅圖
plt.pie(people, pctdistance=0.8, labels=lang, autopct="%1.2f%%")
# 建立內層性別標籤
plt.pie(
    gender,
    radius=0.6,
    labels=labelgender,
    colors=colors,
    autopct="%1.2f%%",
    labeldistance=0.2,
)
plt.title("程式語言調查表", fontsize=16, color="b")
plt.show()


print("------------------------------------------------------------")  # 60個

lang = ["Python", "C", "Java", "C++", "PHP"]  # 程式語言標籤
people = [350, 200, 250, 150, 270]  # 人數
labelgender = ["男生", "女生"]  # 性別標籤
gender = [720, 500]  # 性別人數
colors = ["lightyellow", "lightgreen"]  # 自定性別色彩
data_no = [1, 0, 0, 0]
# 建立外層程式語言圓餅圖
plt.pie(people, pctdistance=0.8, labels=lang, autopct="%1.2f%%")
# 建立內層性別標籤
plt.pie(
    gender,
    radius=0.6,
    labels=labelgender,
    colors=colors,
    autopct="%1.2f%%",
    labeldistance=0.45,
)
plt.pie(data_no, radius=0.2, colors="w")  # 建立最內層空的圓餅
plt.title("程式語言調查表", fontsize=16, color="b")

plt.show()

print("------------------------------------------------------------")  # 60個

product = ["家電", "生活用品", "圖書", "保健", "彩妝"]  # 產品標籤
revenue = [23000, 18000, 12000, 15000, 16000]  # 業績
plt.pie(revenue, labels=product, autopct="%1.2f%%")
plt.legend()
plt.title("銷售品項分析", fontsize=16, color="b")

plt.show()

print("------------------------------------------------------------")  # 60個

product = ["家電", "生活用品", "圖書", "保健", "彩妝"]  # 產品標籤
revenue = [23000, 18000, 12000, 15000, 16000]  # 業績
patches = plt.pie(revenue, labels=product, autopct="%1.2f%%")
plt.legend(
    patches[0], product, loc="center left", title="產品類別", bbox_to_anchor=(1, 0, 0.5, 1)
)
plt.title("銷售品項分析", fontsize=16, color="b")

plt.show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
recipe = ["100 毫升純水", "90 公克黑糖", "120 毫升仙草", "100 毫升牛奶", "50 黑珍珠"]  # 原料成分
data = [100, 90, 120, 100, 50]  # 原料份量
wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=15)
# 箭頭格式
kw = dict(
    arrowprops=dict(arrowstyle="->", color="b"),
    bbox=dict(boxstyle="square", ec="w", fc="yellow"),
    va="center",
)
# 建立箭頭和註解文字
for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1) / 2.0 + p.theta1  # 箭頭指向角度
    x = np.cos(np.deg2rad(ang))  # 箭頭 x 位置
    y = np.sin(np.deg2rad(ang))  # 箭頭 y 位置
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(
        recipe[i],
        xy=(x, y),
        xytext=(1.35 * np.sign(x), 1.4 * y),
        horizontalalignment=horizontalalignment,
        **kw
    )
ax.set_title("製作燒仙草環圈圖")

plt.show()

print("------------------------------------------------------------")  # 60個

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
fig.subplots_adjust()
# 定義程式語言人數
lang = ["Python", "C", "Java", "C++", "PHP"]
people = [350, 200, 250, 150, 270]
# 定義男女生人數
labelgender = ["男生", "女生"]
gender = [720, 500]
# 繪製程式語言人數圓餅圖
ax1.pie(people, autopct="%1.1f%%", startangle=20, labels=lang)
ax1.set_title("程式語言使用調查表", color="b")
# 繪製男女生圓餅圖
ax2.pie(
    gender,
    autopct="%1.1f%%",
    startangle=70,
    labels=labelgender,
    radius=0.7,
    colors=["lightgreen", "yellow"],
)
ax2.set_title("男女生比例調查表", color="b")

plt.show()

print("------------------------------------------------------------")  # 60個

from matplotlib.patches import ConnectionPatch

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
fig.subplots_adjust()
# 定義程式語言人數
lang = ["Python", "C", "Java", "C++", "PHP"]
people = [350, 200, 250, 150, 270]
# 定義男女生人數
labelgender = ["男生", "女生"]
gender = [720, 500]
# 繪製程式語言人數圓餅圖
ax1.pie(people, autopct="%1.1f%%", startangle=20, labels=lang)
ax1.set_title("程式語言使用調查表", color="b")
# 繪製男女生圓餅圖
ax2.pie(
    gender,
    autopct="%1.1f%%",
    startangle=70,
    labels=labelgender,
    radius=0.7,
    colors=["lightgreen", "yellow"],
)
ax2.set_title("男女生比例調查表", color="b")
# 建立上方線條
con_a = ConnectionPatch(
    xyA=(0, 1),
    xyB=(0, 0.7),
    coordsA=ax1.transData,
    coordsB=ax2.transData,
    axesA=ax1,
    axesB=ax2,
)
# 建立下方線條
con_b = ConnectionPatch(
    xyA=(0, -1),
    xyB=(0, -0.7),
    coordsA=ax1.transData,
    coordsB=ax2.transData,
    axesA=ax1,
    axesB=ax2,
)
# 線條連接
for con in [con_a, con_b]:
    ax2.add_artist(con)
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


plt.rcParams["font.family"] = ["Microsoft JhengHei"]
