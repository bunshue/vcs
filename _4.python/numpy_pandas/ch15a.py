import sys
import pandas as pd

df = pd.read_csv("missing_data.csv")

print('原資料')
print(df)
print()

print('資料結構訊息')
print(df.info())
print()

print('清除NA')
df1 = df.dropna()
print(df1)
print()

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

df = pd.read_csv("duplicated_data.csv")

print('原資料')
print(df)
print()

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

df = pd.read_csv("labelencoder_data.csv")

print('原資料')
print(df)
print()

from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
df["Gender"] = label_encoder.fit_transform(df["Gender"])
print(df)


print('------------------------------------------------------------')	#60個





'''
import pandas as pd
import matplotlib.pyplot as plt

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示



plt.show()
'''

