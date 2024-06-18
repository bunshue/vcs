# 派圖 集合

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

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="派圖 集合 1",
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
圓餅圖是使用 pie 函數繪製出來的，語法為：

plt.pie(串列資料, [其餘參數值])

其餘參數介紹：
pie參數 	說明
color 	指定圓餅圖的顏色 ('blue', 'red', 'green', 'yellow', 色碼('#CC00CC')),預設為藍色 blue
label 	項目標題，需搭配 legend 函式才有效果
explode 	設定分隔的區塊位置
autopct 	項目百分比格式，語法為「%格式%%」，Example:autopct = "%2.2f%%"(表示整數2位數及小數點2位數)
pctdistance 	數值文字與圓心距離
shadow 	圓餅圖陰影開啟/關閉，True 有陰影，False 沒有陰影
startangle 	繪製起始角度，繪製會以逆時鐘旋轉計算角度
radius 	圓餅圖的半徑，預設是1
"""

# 設定將使用的數值，將要有項目標題、數值串列、圓餅圖顏色、分隔的區塊位置
values = [3, 48, 33, 8, 38]
labels = ["鼠", "牛", "虎", "兔", "龍"]
colors = ["r", "g", "b", "c", "m"]
# 分離係數，所以只有 '虎' 會分離
explode = (0, 0, 0.15, 0, 0)  # 設定分隔的區塊位置

# 設定 pie 函數參數繪製圓餅圖
# 從 90° 開始，逆時針排列，並加上陰影，並加上每塊的比例，格式為 '%1.2f%%'
plt.pie(
    values,  # 數值
    labels=labels,  # 項目標題
    colors=colors,  # 指定圓餅圖的顏色
    explode=explode,  # 設定分隔的區塊位置
    labeldistance=1.1,
    autopct="%2.1f%%",  # 項目百分比的格式, 顯示數字
    pctdistance=0.5,  # 數值文字與圓心距離
    shadow=True,  # 圓餅圖陰影開啟/關閉
    startangle=90,  # 繪製起始角度
    radius=0.9,  # 圓餅圖的半徑，預設是1
)

# 設定 legnd 的位置，將圖表顯示出來，並顯示圖例名稱
plt.legend(loc="right")  # 設定 legend 的位置
plt.title("指定顏色 使用圖例")

# 第二張圖
plt.subplot(232)

# 設定將使用的數值，將要有項目標題、數值串列、圓餅圖顏色、分隔的區塊位置
values = [3, 48, 33, 8, 38]
labels = ["鼠", "牛", "虎", "兔", "龍"]
colors = ["r", "g", "b", "c", "m"]
# 分離係數，所以只有 '虎' 會分離
explode = (0, 0, 0.15, 0, 0)  # 設定分隔的區塊位置

plt.pie(
    values,
    explode=explode,
    labels=labels,
    colors=colors,
    labeldistance=1.1,
    autopct="%2.1f%%",
    pctdistance=0.6,
    shadow=True,
    startangle=90,
)
plt.title("指定顏色")

# 第三張圖
plt.subplot(233)

values = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
names = "鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬"
explode = (0, 0.1, 0, 0.2, 0, 0.3, 0, 0.4, 0, 0.5, 0, 0.6)
plt.pie(values, labels=names, explode=explode, autopct="%.1f%%", shadow=True)

# 第四張圖
plt.subplot(234)

values = [3, 48, 33, 8, 38]
labels = ["鼠", "牛", "虎", "兔", "龍"]  # list格式
labels = "鼠", "牛", "虎", "兔", "龍"  # tuple格式
print(type(labels))

explode = (0.2, 0, 0, 0, 0)  # 將圓餅圖的特定區塊向外推

plt.pie(
    values, labels=labels, explode=explode, autopct="%1.2f%%", shadow=True
)  # 繪製圓餅圖, 自動計算百分比, 加入立體陰影

# 第五張圖
plt.subplot(235)

data = {"鼠": 3, "牛": 48, "虎": 33, "兔": 8, "龍": 38}
explode = (0, 0, 0, 0.2, 0)  # 向外擴展顯示的區域

plt.pie(
    data.values(),
    explode=explode,
    labels=data.keys(),
    autopct="%1.1f%%",
    shadow=True,
    startangle=90,
)

# 第六張圖
plt.subplot(236)

lexus_models = {
    "CT-200h": 139,
    "ES": 167,
    "GS": 221,
    "IS": 173,
    "LC": 539,
    "LS": 337,
    "LX": 465,
    "NX": 155,
    "RC": 243,
    "RX": 224,
    "RX L": 260,
    "UX": 139,
}
lexus_prices = np.array(list(lexus_models.values()), dtype=np.int64)
lexus = list()
lexus.append(np.count_nonzero(lexus_prices <= 150))
lexus.append(np.count_nonzero((lexus_prices > 150) & (lexus_prices <= 200)))
lexus.append(np.count_nonzero((lexus_prices > 200) & (lexus_prices <= 300)))
lexus.append(np.count_nonzero(lexus_prices > 300))

labels = ["<=150", "151~200", "201~300", ">300"]
explode = [0.2, 0, 0, 0]

plt.pie(
    lexus, explode=explode, autopct="%1.0f%%", radius=1.0, labels=labels, shadow=True
)

plt.show()

print("------------------------------------------------------------")  # 60個

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="派圖 集合 2",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 第一張圖
plt.subplot(231)

area = ["大陸", "東南亞", "東北亞", "美國", "歐洲", "澳紐"]
people = [10000, 12600, 9600, 7500, 5100, 4800]
exp = [0.0, 0.0, 0.1, 0.0, 0.0, 0.1]
colors = ["aqua", "g", "pink", "yellow", "m", "salmon"]
plt.pie(people, labels=area, explode=exp, autopct="%1.2f%%", colors=colors)
plt.title("五月份國外旅遊調查表", fontsize=16, color="b")


# 第二張圖
plt.subplot(232)

edu = [0.2515, 0.3724, 0.3336, 0.0368, 0.0057]
labels = ["中專", "大專", "本科", "碩士", "其他"]
colors = ["#9999ff", "#ff9999", "#7777aa", "#2442aa", "#dd5555"]  # 自定義顏色
explode = [0, 0.1, 0, 0, 0]  # 生成數據，用于突出顯示大專學歷人群

# 繪制餅圖

plt.pie(
    x=edu,  # 繪圖數據
    explode=explode,  # 突出顯示大專人群
    labels=labels,  # 添加教育水平標簽
    colors=colors,  # 設置餅圖的自定義填充色
    autopct="%.1f%%",  # 設置百分比的格式，這里保留一位小數
    pctdistance=0.8,  # 設置百分比標簽與圓心的距離
    labeldistance=1.1,  # 設置教育水平標簽與圓心的距離
    startangle=180,  # 設置餅圖的初始角度
    radius=1.2,  # 設置餅圖的半徑
    counterclock=False,  # 是否逆時針，這里設置為順時針方向
    wedgeprops={"linewidth": 1.5, "edgecolor": "green"},  # 設置餅圖內外邊界的屬性值
    textprops={"fontsize": 10, "color": "black"},  # 設置文本標簽的屬性值
)


# 第三張圖
plt.subplot(233)

labels = ["Python", "C++", "Java", "JS", "C", "C#"]
ratings = [5, 6, 15, 3, 12, 4]
explode = (0, 0, 0, 0.2, 0, 0.2)

patches, texts = plt.pie(ratings, labels=labels, explode=explode)
plt.legend(patches, labels, loc="best")
plt.title("使用回傳值")
plt.axis("equal")


# 第四張圖
plt.subplot(234)

from pylab import mpl

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

sizes = [25, 30, 15, 10]
labels = ["北部", "西部", "南部", "東部"]
explode = (0, 0, 0.2, 0)

plt.pie(sizes, labels=sizes, explode=explode, autopct="%1.2f%%")


# 第五張圖
plt.subplot(235)

#pie指定顏色

sizes = [25, 30, 15, 10]
labels = ["北部", "西部", "南部", "東部"]
colors = ["red", "green", "blue", "yellow"]
explode = (0, 0, 0.2, 0)

plt.pie(
    sizes,
    explode=explode,
    labels=labels,
    colors=colors,
    labeldistance=1.1,
    autopct="%2.1f%%",
    pctdistance=0.6,
    shadow=True,
    startangle=90,
)


# 第六張圖
plt.subplot(236)

#pie指定顏色

sizes = [25, 30, 15, 10]
labels = ["北部", "西部", "南部", "東部"]
colors = ["red", "green", "blue", "yellow"]
explode = (0, 0, 0.2, 0)

plt.pie(sizes, labels=labels, colors=colors, explode=explode, autopct='%2.1f%%',startangle=0, shadow=True)


plt.show()

print("------------------------------------------------------------")  # 60個

dices=['1點','2點','3點','4點','5點','6點']
data=[]
times=[]
for i in range(1000):
    data.append(random.randint(1,6))

for i in range(1,7):
    times.append(data.count(i))
    
plt.pie(times,labels=dices,autopct='%2.1f%%',explode=[0.1,0.1,0.1,0.1,0.1,0.1],shadow=True)
plt.title('擲骰子機率圖',fontsize=18)

plt.show()

print("------------------------------------------------------------")  # 60個

#預設字體大小
plt.rc('font', size=20)
#軸標題字體大小
plt.rc('axes', titlesize=30)
#X軸刻度字體大小
plt.rc('xtick', labelsize=20)
#圖例字體大小
plt.rc('legend', fontsize=10)
#薪水分配 六三一分配法
#圓餅圖
salarypay = ['生活費', '儲蓄', '娛樂/緊急預備金']
#佔比
ratios = [60, 30, 10]
#設定分離區塊
explode = [0, 0, 0.1] 
#顏色
color = [(1.0,0,0), (0,1.0,0), (0,1.0,1.0)] 
fig, ax = plt.subplots(figsize=(10,10), dpi=80)
ax.pie(ratios, explode=explode, labels=salarypay, autopct='%1.1f%%',
        colors=color, shadow=True, startangle=40)
#設定Y/X軸長度比例 
ax.set_aspect(0.7) 
ax.set_title('薪水分配 六三一分配法')
ax.legend()

plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


"""

edu = [0.2515,0.3724,0.3336,0.0368,0.0057]
plt.pie(x = edu, # 繪圖數據
labels = labels, # 添加教育水平標簽
autopct = '%.1f%%' # 設置百分比的格式，這里保留一位小數


# 將橫、縱坐標軸標準化處理，確保餅圖是一個正圓，否則為橢圓
plt.axes(aspect = 'equal')

"""
