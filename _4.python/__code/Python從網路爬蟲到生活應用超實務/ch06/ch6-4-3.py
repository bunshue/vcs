import pandas as pd

df = pd.read_csv("shoes.csv")
print(df)
size_mapping = {"XXL": 5,
                "XL": 4,
                "L": 3,
                "M": 2,
                "S": 1,
                "XS": 0}

df["Size"] = df["Size"].map(size_mapping)
print(df)



