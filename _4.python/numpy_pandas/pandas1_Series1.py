import sys
import numpy as np
import pandas as pd

print("------------------------------------------------------------")  # 60個

s = pd.Series([12, 29, 72, 4, 8, 10])
print(s)

print("------------------------------------------------------------")  # 60個

names = ["蘋果", "橘子", "梨子", "櫻桃"]
weights = [15, 33, 45, 55]
s = pd.Series(weights, index=names)
print(s)
print(s.index)
print(s.values)

print("------------------------------------------------------------")  # 60個

names = ["蘋果", "橘子", "梨子", "櫻桃"]
weights = [15, 33, 45, 55]
s = pd.Series(weights, index=names)
p = pd.Series([11, 16, 21, 32], index=names)

print(s + p)
print("總計=", sum(s + p))

print("------------------------------------------------------------")  # 60個

names = ["蘋果", "橘子", "梨子", "櫻桃"]
s = pd.Series([15, 33, 45, 55], index=names)
print("橘子=", s["橘子"])

print("------------------------------")  # 30個

print(s[["橘子", "梨子", "櫻桃"]])

print((s + 2) * 3)

print(s.apply(np.sin))

print("------------------------------------------------------------")  # 60個

cc = pd.Series([1, 2, 3, 4, 5])
print(cc)  # 顯示Series
print(cc.values)  # 顯示值
print(cc.index)  # 顯示索引

print("------------------------------------------------------------")  # 60個

cc = pd.Series([1, 2, 3, 4, 5])
print(cc[2])
print(cc[2:5])

print("------------------------------------------------------------")  # 60個

cc = pd.Series(["a", "b", "c", "d", "e"])
print(cc[1:3])

print("------------------------------------------------------------")  # 60個

cc = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
print(cc)
print(cc["b"])
print(cc["c":"d"])

print("------------------------------------------------------------")  # 60個

dict1 = {"Taipei": "台北", "Taichung": "台中", "Kaohsiung": "高雄"}
cc = pd.Series(dict1)
print(cc)  # 顯示Series
print(cc.values)  # 顯示值
print(cc.index)  # 顯示索引
print(cc["Taipei"])  # 用索引取值
print(cc["Taichung":"Kaohsiung"])

print("------------------------------------------------------------")  # 60個

# 使用此函數將pandas的df和series轉為NumPy數組。
sex = pd.Series(["Male", "Male", "Female"])
cc = np.array(sex)
print(cc)

print("------------------------------------------------------------")  # 60個


print("建立 Series 物件")

index = ["鼠", "牛", "虎", "兔", "龍"]
datas = [1, 4, 5, 6, 3]
series = pd.Series(datas, index=index)
print(series)

datas = [1, 4, 5, 6, 3]
series = pd.Series(datas)
print(series)

datas = {"orange": 2, "banana": 3}
print(pd.Series(datas))

print("------------------------------------------------------------")  # 60個

# 取出 Series 當中的元素

datas = {"banana": 3, "orange": 4, "grape": 1, "peach": 5}
series = pd.Series(datas)

print(series[0:2])
print(series[["orange", "peach"]])

print("------------------------------------------------------------")  # 60個

# 單取出「索引值」或者「內容值」-.index、.values

index = ["鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬"]
weight = [3, 48, 33, 8, 38, 16, 36, 29, 22, 6, 12, 42]

series = pd.Series(weight, index=index)
print(series)

series_index = series.index
series_values = series.values
print(series_index)
print(series_values)

print("畫出來")
series.plot()

plt.show()

print("------------------------------------------------------------")  # 60個

# 新增 Series 物件的元素 – append()

index = ["鼠", "牛", "虎", "兔", "龍"]
data = [10, 5, 8, 12, 3]
series = pd.Series(data, index=index)
print(series)

pineapple = pd.Series([12], index=["pineapple"])
# pineapple = pd.Series( {"pineapple":12})

# NG
# series = series.append(pineapple)
# print(series)

print("------------------------------------------------------------")  # 60個

# 刪除 Series 物件的元素 – drop()

index = ["鼠", "牛", "虎", "兔", "龍"]
data = [10, 5, 8, 12, 3]
series = pd.Series(data, index=index)
print(series)

series = series.drop("兔")
print(series)

print("------------------------------------------------------------")  # 60個

# 從 Series 物件篩選出想要的元素
index = ["鼠", "牛", "虎", "兔", "龍"]
data = [10, 5, 8, 12, 3]
series = pd.Series(data, index=index)
print(series)

conditions = [True, True, False, False, False]
print(series[conditions])

index = ["鼠", "牛", "虎", "兔", "龍"]
data = [10, 5, 8, 12, 3]
series = pd.Series(data, index=index)
print(series[series >= 5])

series = series[series >= 5][series < 10]
print(series)

print("------------------------------------------------------------")  # 60個

# 將 Series 的元素排序 – sort_index()、sort_values()
index = ["鼠", "牛", "虎", "兔", "龍"]
data = [10, 5, 8, 12, 3]
series = pd.Series(data, index=index)
print(series)

items1 = series.sort_index()
items2 = series.sort_values()
print(items1)
print(items2)

print("------------------------------------------------------------")  # 60個

s = pd.Series([1, 3, 6, np.nan, 4, 1])  # similar with 1D numpy
print(s)

print("------------------------------------------------------------")  # 60個

# Series

# se1.py
se = pd.Series([1, 2, 3, 4])
print(se)  # 顯示Series
print(se.values)  # 顯示值
print(se.index)  # 顯示索引

# se2.py
dict1 = {"a": 100, "b": 200, "c": 300}
se = pd.Series(dict1)
print(se)  # 顯示Series
print(se.values)  # 顯示值
print(se.index)  # 顯示索引

# se3.py
se = pd.Series([1, 2, 3, 4, 5])
print(se[2])
print("-" * 6)
print(se[2:5])

print("------------------------------------------------------------")  # 60個

lst = ["Bike", "Bus", "Car", "Truck"]
print(type(lst))

print("List 轉 Series")
s = pd.Series(lst)
print(type(s))
print(s)

print("------------------------------------------------------------")  # 60個

# Series
# data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data = s2 = pd.Series([65, 90, 81, 79])  # 國文成績
# data = data.cumsum()
data.plot()

plt.show()

print("------------------------------------------------------------")  # 60個


#建立Series
s = pd.Series(np.random.rand(16), index=list("ABCDEFGHIJKLMNOP"))


#s = pd.Series({"鼠": 3, "牛": 48, "虎": 33, "兔": 8, "龍": 38})
#s.name = "動物"
#print(s)



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


"""
Pandas繪圖 用matplotlib顯示


"""

# 共同
import os
import sys
import time
import math
import time
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

print("------------------------------------------------------------")  # 60個
print("Series 畫圖")
print("------------------------------------------------------------")  # 60個

print('0~9選30個出來, 看其分布')
N = 30
datas = np.random.randint(0, 10, N)
print(datas)

s = pd.Series(datas)
#print(s)

s.plot()  # 無參數, 預設就是 line
plt.show()

# 用Series的 value_counts()直接繪製柱狀圖，表達每個數字出現的次數
vc = s.value_counts()
print(vc)
vc.plot(kind="bar")

plt.show()

print("------------------------------------------------------------")  # 60個

N = 1000
datas = np.random.normal(size=N)
s = pd.Series(datas)

# s.hist() #無參數
# s.hist(bins=50, alpha=0.5)# same
# s.plot.hist(bins=50, alpha=0.5)
# s.plot(kind='hist', title='常態分佈轉series 直方圖的使用')
s.plot(kind="hist", bins=50)
# s.plot(kind="hist") # 未指定束數, 預設10束

plt.show()

print("------------------------------------------------------------")  # 60個

index = ["E", "W", "S", "N"]
datas = [4522, 3101, 5211, 4613]
s = pd.Series(datas, index=index)

# 自定列索引
s.index = ["東區", "西區", "南區 ", "北區"]
print(s)

s.plot()  # 無參數, 預設就是 line

plt.show()

print("------------------------------------------------------------")  # 60個

weight = [3, 48, 33, 8, 38, 16, 36, 29, 22, 6, 12, 42]
animals = ["鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬"]

#s = pd.Series(weight, index=animals)
s = pd.Series(weight, index=animals, name="動物")
s.name = "動物"
print(s)

"""
s.plot(kind="bar", rot=45, title = 'Series畫圖')  # bar 圖
#s.plot(kind="bar", rot=45)
s.plot()  # 無參數, 預設就是 line
"""

# 控制派圖為正圓
plt.axes(aspect="equal")

# pie圖, 無 explode
# s.plot(kind="pie") # 無 explode

# pie圖, 有 explode
explode = [0.1, 0.3, 0.1, 0.3, 0.1, 0.3, 0.1, 0.3, 0.1, 0.3, 0.1, 0.3]
s.plot(kind="pie", figsize=(6, 6), explode=explode)

plt.show()

# plot方法對序列進行繪圖
s.plot(
    kind="pie",  # 選擇圖形類型
    autopct="%.1f%%",  # 餅圖中添加數值標簽
    radius=1,  # 設置餅圖的半徑
    startangle=180,  # 設置餅圖的初始角度
    counterclock=False,  # 將餅圖的順序設置為順時針方向
    title="動物",  # 為餅圖添加標題
    wedgeprops={"linewidth": 1.5, "edgecolor": "green"},  # 設置餅圖內外邊界的屬性值
    textprops={"fontsize": 10, "color": "black"},  # 設置文本標簽的屬性值
)

plt.show()

print("------------------------------------------------------------")  # 60個

yyyymmdd = "20240101"  # "1/1/2024"
DAYS = 366
datas = np.random.randn(DAYS)
index = pd.date_range(yyyymmdd, periods=DAYS)
print('從', yyyymmdd, '開始的', DAYS, '天\n', index)
s = pd.Series(datas, index=index)

print("顯示s大小 :", s.shape)
#print(s)

print("月底的數值改為每月總計, 另存成Series格式")
month_sum = s.resample("1ME").sum()
print(type(month_sum))
print(month_sum)

plt.figure(figsize=(10, 6))
s.plot()  # 無參數, 預設就是 line
plt.title("Series畫圖 線圖 每日之漲跌幅")
plt.show()

plt.figure(figsize=(10, 6))
cs = s.cumsum() # 計算累積值 cumulative sum
print(cs)
cs.plot()  # 無參數, 預設就是 line
plt.title("Series畫圖 線圖 漲跌幅之累計")
plt.show()

plt.figure(figsize=(10, 6))
month_sum.plot.bar()
plt.title("Series畫圖 bar圖")
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個
