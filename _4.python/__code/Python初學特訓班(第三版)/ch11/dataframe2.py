import pandas as pd
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



import pandas as pd

df = pd.DataFrame( {"林大明":[65,92,78,83,70], "陳聰明":[90,72,76,93,56], \
    "黃美麗":[81,85,91,89,77], "熊小娟":[79,53,47,94,80] } )

print(df)


import pandas as pd

datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)

print(df)


import pandas as pd
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


import pandas as pd
datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
indexs[0] = "林晶輝"
df.index = indexs
columns[3] = "理化"
df.columns = columns
print(df)



