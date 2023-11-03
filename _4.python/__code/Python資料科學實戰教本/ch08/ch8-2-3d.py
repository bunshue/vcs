import pandas as pd 

df = pd.read_csv("dists.csv", encoding="utf8")

print("資料數= ", len(df))
print("---------------------------")
print("形狀= ", df.shape)
print("---------------------------")
df.info()