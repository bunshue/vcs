import pandas as pd
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
