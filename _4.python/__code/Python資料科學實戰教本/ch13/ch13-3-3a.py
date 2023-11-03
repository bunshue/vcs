import pandas as pd
from sklearn import preprocessing

df = pd.read_csv("test3.csv")

label_encoder = preprocessing.LabelEncoder()
df["性別"] = label_encoder.fit_transform(df["性別"])
print(df)
df.to_html("ch13-3-3a.html")