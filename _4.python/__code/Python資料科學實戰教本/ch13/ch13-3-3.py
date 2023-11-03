import pandas as pd

df = pd.read_csv("test3.csv")
print(df)
df.to_html("ch13-3-3-01.html")
print("---------------------------")
size_mapping = {"XXL": 5,
                "XL": 4,
                "L": 3,
                "M": 2,
                "S": 1,
                "XS": 0}

df["尺寸"] = df["尺寸"].map(size_mapping)
print(df)
df.to_html("ch13-3-3-02.html")