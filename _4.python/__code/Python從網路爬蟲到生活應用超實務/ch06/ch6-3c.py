import pandas as pd

df1 = pd.DataFrame({"Name":["A", "B"],"Value":[11, 12]})
df2 = pd.DataFrame({"Name":["C"],"Value":[23]})
df3 = pd.concat([df1, df2], ignore_index=True)
print(df3)

df4 = pd.DataFrame({"Name":["A","B"],"Value":[11, 12]})
df5 = pd.DataFrame({"Size":["XL","L"]})
df6 = pd.concat([df4, df5], axis=1)
print(df6)
