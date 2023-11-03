import pandas as pd 

df = pd.read_csv("dists.csv", encoding="utf8")

for index, row in df.iterrows() :
    print(index, row["city"], row["name"], row["population"])