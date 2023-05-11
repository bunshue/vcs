import pandas as pd
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
