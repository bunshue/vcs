"""
Pandas Series

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
"""
index = ["鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬"]
weight = [3, 48, 33, 8, 38, 16, 36, 29, 22, 6, 12, 42]

s = pd.Series(weight, index=index)
#print(s)  # 顯示Series

index = s.index
values = s.values
print('索引值 :', index)
print('內容值 :', values)
print("龍的體重 : ", s["龍"])
print(s[["猴", "雞", "狗"]])
print((s + 2) * 3)
print(s[2])
print(s[2:5])

#對Series做運算
#print(s.apply(np.sin))

print("------------------------------------------------------------")  # 60個

s = pd.Series(["a", "b", "c", 123, 456, np.nan])
print(s)
print(s[1:3])

print("------------------------------------------------------------")  # 60個

s1 = pd.Series(weight, index=index)
s2 = pd.Series(weight, index=index)

print(s1 + s2)
print("總計=", sum(s1 + s2))

print("------------------------------------------------------------")  # 60個

s = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
print(s)
print(s["b"])
print(s["c":"d"])

print("------------------------------------------------------------")  # 60個

dict1 = {"Taipei": "台北", "Taichung": "台中", "Kaohsiung": "高雄"}
s = pd.Series(dict1)
print(s)  # 顯示Series
print(s.values)  # 顯示值
print(s.index)  # 顯示索引
print(s["Taipei"])  # 用索引取值
print(s["Taichung":"Kaohsiung"])

print("------------------------------------------------------------")  # 60個

# 使用此函數將pandas的df和series轉為NumPy數組。
s = pd.Series(["Male", "Male", "Female"])
cc = np.array(s)
print(cc)

print("------------------------------------------------------------")  # 60個

index = ["鼠", "牛", "虎", "兔", "龍"]
datas = [1, 4, 5, 6, 3]
s = pd.Series(datas, index=index)
print(s)

datas = [1, 4, 5, 6, 3]
s = pd.Series(datas)
print(s)

datas = {"orange": 2, "banana": 3}
print(pd.Series(datas))

print("------------------------------------------------------------")  # 60個

# 取出 Series 當中的元素

datas = {"banana": 3, "orange": 4, "grape": 1, "peach": 5}
s = pd.Series(datas)

print(s[0:2])
print(s[["orange", "peach"]])

print("------------------------------------------------------------")  # 60個

# 新增 Series 物件的元素 – append()

index = ["鼠", "牛", "虎", "兔", "龍"]
data = [10, 5, 8, 12, 3]
s = pd.Series(data, index=index)
print(s)

pineapple = pd.Series([12], index=["pineapple"])
# pineapple = pd.Series( {"pineapple":12})

# NG
# s = series.append(pineapple)
# print(s)

print("------------------------------------------------------------")  # 60個

# 刪除 Series 物件的元素 – drop()

index = ["鼠", "牛", "虎", "兔", "龍"]
data = [10, 5, 8, 12, 3]
s = pd.Series(data, index=index)
print(s)

s = s.drop("兔")
print(s)

print("------------------------------------------------------------")  # 60個

# 從 Series 物件篩選出想要的元素
index = ["鼠", "牛", "虎", "兔", "龍"]
data = [10, 5, 8, 12, 3]
s = pd.Series(data, index=index)
print(s)

conditions = [True, True, False, False, False]
print(s[conditions])

index = ["鼠", "牛", "虎", "兔", "龍"]
data = [10, 5, 8, 12, 3]
s = pd.Series(data, index=index)
print(s[s >= 5])

s = s[s >= 5][s < 10]
print(s)

print("------------------------------------------------------------")  # 60個

# 將 Series 的元素排序 – sort_index()、sort_values()
index = ["鼠", "牛", "虎", "兔", "龍"]
data = [10, 5, 8, 12, 3]
s = pd.Series(data, index=index)
print(s)

items1 = s.sort_index()
items2 = s.sort_values()
print(items1)
print(items2)

print("------------------------------------------------------------")  # 60個

print('字典 轉 Series')

dict1 = {"a": 100, "b": 200, "c": 300}
s = pd.Series(dict1)
print(s)  # 顯示Series
print(s.values)  # 顯示值
print(s.index)  # 顯示索引

print("------------------------------------------------------------")  # 60個

print('字典 轉 Series')

s = pd.Series({"鼠": 3, "牛": 48, "虎": 33, "兔": 8, "龍": 38})
s.name = "動物"
print(s)

print("------------------------------------------------------------")  # 60個

N =100
s = pd.Series(np.random.randn(N), index=np.arange(N))
print(s)

print("------------------------------------------------------------")  # 60個

s = pd.Series(np.random.rand(10), index=list("ABCDEFGHIJ"))
print(s)

print("------------------------------------------------------------")  # 60個

s = pd.Series([10, 20, 30, 40, 50])
print('原Series :\n', s)
s2 = s.cumsum()
print('Series累計 :\n', s2)

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
sys.exit()
print("------------------------------------------------------------")  # 60個
"""
print("------------------------------------------------------------")  # 60個
print("Series 畫圖")
print("------------------------------------------------------------")  # 60個

print("0~9選30個出來, 看其分布")
N = 30
datas = np.random.randint(0, 10, N)
print(datas)

s = pd.Series(datas)
# print(s)

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

# s = pd.Series(weight, index=animals)
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
print("從", yyyymmdd, "開始的", DAYS, "天\n", index)
s = pd.Series(datas, index=index)

print("顯示s大小 :", s.shape)
# print(s)

print("月底的數值改為每月總計, 另存成Series格式")
month_sum = s.resample("1ME").sum()
print(type(month_sum))
print(month_sum)

plt.figure(figsize=(10, 6))
s.plot()  # 無參數, 預設就是 line
plt.title("Series畫圖 線圖 每日之漲跌幅")
plt.show()

plt.figure(figsize=(10, 6))
cs = s.cumsum()  # 計算累積值 cumulative sum
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
