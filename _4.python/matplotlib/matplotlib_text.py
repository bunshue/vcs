# text 集合

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="text 集合 1",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)


# 第一張圖
plt.subplot(231)

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64]
plt.plot(squares)
plt.axis([0, 8, 0, 70])  # 繪製線條
x = 2
y = 30
plt.plot(x, y, "bo")  # 輸出位智繪製藍色的點
plt.text(x, y, "把字寫在這裡")  # 輸出字串
plt.grid()


# 第二張圖
plt.subplot(232)

plt.axis([0, 10, 0, 10])
s = "Welcome to the United States" "God bless you" "Thanks Got It's Friday"

plt.text(
    5,
    10,
    s,
    family="Old English Text MT",
    style="oblique",
    ha="center",
    fontsize=15,
    va="top",
    wrap=True,
)
plt.text(5, 1, s, c="b", ha="left", rotation=15, wrap=True)
plt.text(6, 4, s, c="g", ha="left", rotation=15, wrap=True)
plt.text(5, 4, s, c="m", ha="right", rotation=-15, wrap=True)
plt.text(-1, 1, s, c="y", ha="left", rotation=-15, wrap=True)


# 第三張圖
plt.subplot(233)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.axis([0, 10, 0, 10])
s1 = "歡迎來到美國"
plt.text(5, 8, s1, ha="center", fontsize=16, va="top", wrap=True)
s2 = "Welcome to the United States" "God bless you" "Thanks Got It's Friday"

plt.text(5, 1, s2, c="b", ha="left", rotation=15, wrap=True)
plt.text(6, 4, s2, c="g", ha="left", rotation=15, wrap=True)
plt.text(5, 4, s2, c="m", ha="right", rotation=-15, wrap=True)
plt.text(-1, 1, s2, c="y", ha="left", rotation=-15, wrap=True)


# 第四張圖
plt.subplot(234)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
s1 = "歡迎來到美國"
plt.text(
    0.7,
    0.7,
    s1,
    size=30,
    rotation=30.0,
    ha="center",
    va="center",
    bbox=dict(
        boxstyle="round",
        ec="g",
        fc="lightgreen",
    ),
)
s2 = "美利堅合眾國"
plt.text(
    0.5,
    0.35,
    s2,
    size=20,
    ha="right",
    va="top",
    bbox=dict(
        boxstyle="circle",
        ec="y",
        fc="lightyellow",
    ),
)


# 第五張圖
plt.subplot(235)


plt.rcParams["font.family"] = ["Microsoft JhengHei"]
s = "歡迎來到美國"
s1 = "Welcome to the United States"
plt.text(
    0.1,
    0.2,
    s,
    size=20,
    ha="left",
    va="center",
    bbox=dict(
        boxstyle="square",
        ec="g",
        fc="lightgreen",
    ),
)
plt.text(
    0.1,
    0.4,
    s,
    size=20,
    ha="left",
    va="center",
    bbox=dict(
        boxstyle="sawtooth",
        ec="y",
        fc="lightgreen",
    ),
)
plt.text(
    0.1,
    0.6,
    s,
    size=20,
    ha="left",
    va="center",
    bbox=dict(
        boxstyle="Roundtooth",
        ec="y",
        fc="lightgreen",
    ),
)
plt.text(
    0.6,
    0.2,
    s,
    size=20,
    ha="left",
    va="center",
    bbox=dict(
        boxstyle="DArrow",
        ec="y",
        fc="lightgreen",
    ),
)
plt.text(
    0.6,
    0.4,
    s,
    size=20,
    ha="left",
    va="center",
    bbox=dict(
        boxstyle="LArrow",
        ec="y",
        fc="lightgreen",
    ),
)
plt.text(
    0.6,
    0.6,
    s,
    size=20,
    ha="left",
    va="center",
    bbox=dict(
        boxstyle="RArrow",
        ec="y",
        fc="lightgreen",
    ),
)
plt.text(
    0.1,
    0.8,
    s1,
    size=18,
    ha="left",
    va="center",
    bbox=dict(
        boxstyle="Square",
        ec="y",
        fc="lightgreen",
    ),
)

# 第六張圖
plt.subplot(236)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
my_kwargs = dict(ha="center", va="center", fontsize=50, c="b")
plt.text(0.5, 0.5, "歡迎來到美國", **my_kwargs)

plt.show()

print("------------------------------------------------------------")  # 60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="text 集合 2",
    figsize=(20, 15),
    dpi=84,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)


# 第一張圖
plt.subplot(231)

# 放置文字
plt.text(0.05, 0.05, "歡迎來到美國", color="red")
plt.text(0.4, 0.6, r"$\int_0^5 f(x)\mathrm{d}x$", fontsize=20, color="blue")
plt.text(0.4, 0.3, r"$\sum_{n=1}^\infty\frac{-e^{2\pi}}{3^n}!$", fontsize=20)
plt.text(0.4, 0.1, "sin(x)", fontsize=20)  # 輸出公式

# 第二張圖
plt.subplot(232)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
my_kwargs = dict(ha="center", va="center", fontsize=50, c="b")
plt.text(0.5, 0.5, "歡迎來到美國", **my_kwargs)


# 第三張圖
plt.subplot(233)

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"


import matplotlib.pyplot as plt
import matplotlib.image as img

t = [10, 20, 30, 40]

plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.title("title")

image = img.imread(filename)
imgplot = plt.imshow(image)

plt.plot(t, t, "r--")
plt.text(70, 10, "牡丹亭")


# 第四張圖
plt.subplot(234)

print("寫字")
#                      H對齊方式       V對齊方式
my_kwargs = dict(ha="center", va="center", fontsize=30, c="b")
my_kwargs = dict(ha="left", va="top", fontsize=30, c="b")
x_st = 0
y_st = 17.5
text = "歡迎來到美國"
plt.text(x_st, y_st, text, **my_kwargs)
plt.plot(x_st, y_st, "r-o")  # 畫基準點

# 第五張圖
plt.subplot(235)

print("從windows字型中找出可以顯示的中文字型")
import matplotlib as mpl
zhfont = mpl.font_manager.FontProperties(fname='C:/Windows/Fonts/mingliu.ttc')
plt.text(0, 0, u'測試一下 ', fontsize=20, fontproperties=zhfont)

plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
plt.rcParams['axes.unicode_minus'] = False

plt.text(0.5, 0.5, u'測試一下')

# 第六張圖
plt.subplot(236)


plt.show()

print("------------------------------------------------------------")  # 60個
