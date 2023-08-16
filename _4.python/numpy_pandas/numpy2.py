import sys
import pandas as pd

filename = 'data/missing_data.csv'
df = pd.read_csv(filename)

print('原資料\n', df, '\n')

print('資料結構訊息', df.info(), '\n')

df1 = df.dropna()
print('清除NA\n', df1, '\n')

df2 = df.dropna(how="any")
print(df2)
print()

df3 = df.dropna(subset=["B", "C"])
print(df3)
print()

df4 = df.fillna(value=1)
print(df4)
print()

df["B"] = df["B"].fillna(df["B"].mean())
print(df)
print()

print('------------------------------------------------------------')	#60個

filename = 'data/duplicated_data.csv'
df = pd.read_csv(filename)

print('原資料\n', df, '\n')

print(df.duplicated())
print()

print(df.duplicated("B"))
print()

df1 = df.drop_duplicates()
print(df1)
print()

df2 = df.drop_duplicates("B")
print(df2)
print()

df3 = df.drop_duplicates("B", keep=False)
print(df3)
print()

print('------------------------------------------------------------')	#60個

filename = 'data/labelencoder_data.csv'
df = pd.read_csv(filename)

print('原資料\n', df, '\n')

from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
df["Gender"] = label_encoder.fit_transform(df["Gender"])
print(df)

print('------------------------------------------------------------')	#60個


