import pandas as pd

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


print("------------------------------------------------------------")  # 60個
