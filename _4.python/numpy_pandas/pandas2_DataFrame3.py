# DataFrame 測試
import pandas as pd
import matplotlib.pyplot as plt

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print('按照數學遞減排序 ->')
df1 = df.sort_values(by="數學", ascending=False)
print(df1)
print()
print('按照列標題遞增排序 ->')
df2 = df.sort_index(axis=0)
print(df2)
print()

print('------------------------------------------------------------')	#60個

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns)
df.plot(xticks=range(0,4))

plt.show()

print('------------------------------------------------------------')	#60個


datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print('最前 2 位學生成績 ->')
print(df.head(2))
print()
print('最後 2 位學生成績 ->')
print(df.tail(2))


print('------------------------------------------------------------')	#60個

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print('df.iloc[1, :] ->')
print(df.iloc[1, :])
print()
print('df.iloc[1][1] ->')
print(df.iloc[1][1])

print('------------------------------------------------------------')	#60個

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print('df.loc["陳聰明", :] ->')
print(df.loc["陳聰明", :])
#print(df.loc["陳聰明"])
print()
print('df.loc["陳聰明"]["數學"] ->')
print(df.loc["陳聰明"]["數學"])
print()
print('df.loc[("陳聰明", "熊小娟") ->')
print(df.loc[("陳聰明", "熊小娟"), :])
print()
print('df.loc[:, "數學"] ->')
print(df.loc[:, "數學"])
print()
print('df.loc[("陳聰明", "熊小娟"), ("數學", "自然")] ->')
print(df.loc[("陳聰明", "熊小娟"), ("數學", "自然")])
print()
print('df.loc["陳聰明":"熊小娟", "數學":"社會"] ->')
print(df.loc["陳聰明":"熊小娟", "數學":"社會"])
print()
print('df.loc[:黃美麗, "數學":"社會"] ->')
print(df.loc[:"黃美麗", "數學":"社會"])
print()
print('df.loc["陳聰明":, "數學":"社會"] ->')
print(df.loc["陳聰明":, "數學":"社會"])

print('------------------------------------------------------------')	#60個

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print('df["自然"] ->')
print(df["自然"])
print()
print('df[["國文", "數學", "自然"] ->')
print(df[["國文", "數學", "自然"]])
print()
print('df[df.數學>=80] ->')
print(df[df.數學 >= 80])

print('------------------------------------------------------------')	#60個

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print("df.values：")
print(df.values)
print("陳聰明的成績(df.values[1])：")
print(df.values[1])
print("陳聰明的英文成績(df.values[1][2])：")
print(df.values[1][2])

print('------------------------------------------------------------')	#60個

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print('df.loc["陳聰明"]["數學"] (原始)：' + str(df.loc["陳聰明"]["數學"]))
df.loc["陳聰明"]["數學"] = 91
print('df.loc["陳聰明"]["數學"] (修改)：' + str(df.loc["陳聰明"]["數學"]))
print()
print('df.loc["陳聰明", :] ->')
df.loc["陳聰明", :] = 80
print(df.loc["陳聰明", :])

print('------------------------------------------------------------')	#60個

df = pd.DataFrame( {"林大明":[65,92,78,83,70], "陳聰明":[90,72,76,93,56], \
    "黃美麗":[81,85,91,89,77], "熊小娟":[79,53,47,94,80] } )

print(df)

print('------------------------------------------------------------')	#60個

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)

print(df)

print('------------------------------------------------------------')	#60個

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print('移除陳聰明成績 ->')
df1 = df.drop("陳聰明")
print(df1)
print()
print('移除數學科成績 ->')
df2 = df.drop("數學", axis=1)
print(df2)
print()
print('移除數學科及自然科成績 ->')
df3 = df.drop(["數學", "自然"], axis=1)
print(df3)
print()
print('移除陳聰明到熊小娟成績 ->')
df4 = df.drop(df.index[1:4])
print(df4)
print()
print('移除數學科到自然科成績 ->')
df5 = df.drop(df.columns[1:4], axis=1)
print(df5)
print()

print('------------------------------------------------------------')	#60個

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
indexs[0] = "林晶輝"
df.index = indexs
columns[3] = "理化"
df.columns = columns
print(df)

print('------------------------------------------------------------')	#60個

