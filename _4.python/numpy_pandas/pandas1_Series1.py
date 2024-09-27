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

index = ["鼠", "牛", "虎", "兔", "龍"]
data = [10, 5, 8, 12, 3]
series = pd.Series(data, index=index)
print(series)

series_index = series.index
series_values = series.values

print(series_index)
print(series_values)

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


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
