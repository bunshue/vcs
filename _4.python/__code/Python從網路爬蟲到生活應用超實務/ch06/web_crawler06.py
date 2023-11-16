import pandas as pd

lst = ["Bike", "Bus", "Car", "Truck"]

s = pd.Series(lst)
print(s)


print('------------------------------------------------------------')	#60個



#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-1-2a.py

import pandas as pd

s1 = pd.Series(["Bike","Bus","Car","Truck"])
s2 = pd.Series([3,4,6,2])
s3 = pd.Series([2,4,4,6])
data = {'種類': s1, '數量': s2, '輪數': s3 } 
df = pd.DataFrame(data) 
print(df)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-1-2b.py

import pandas as pd

data = {'種類': ["Bike","Bus","Car","Truck"],
        '數量': [3,4,6,2],
        '輪數': [2,4,4,6] } 
df = pd.DataFrame(data) 
print(df)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-1-2c.py

import pandas as pd

data = {'種類': ["Bike","Bus","Car","Truck"],
        '數量': [3,4,6,2],
        '輪數': [2,4,4,6] } 
df = pd.DataFrame(data) 
labels = ["A","B","E","D"]
df.columns = ["Types", "Count", "Wheels"]
labels[2] = "C"
df.index = labels
print(df)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-1-2d.py

import pandas as pd

data = {'種類': ["Bike","Bus","Car","Truck"],
        '數量': [3,4,6,2],
        '輪數': [2,4,4,6] } 
df = pd.DataFrame(data) 
df.set_index("種類", inplace=True)
print(df)
df.reset_index(inplace=True)
print(df)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-1-2e.py

import pandas as pd

data = {'種類': ["Bike","Bus","Car","Truck"],
        '數量': [3,4,6,2],
        '輪數': [2,4,4,6] } 
df = pd.DataFrame(data) 
s = pd.Series({'種類':"Bicycle",'數量':5,'輪數':2}) 
df2 = df.append(s, ignore_index=True)
print(df2.tail())

df["載客數"] = [1, 20, 4, 2]
print(df)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-1-2f.py

import pandas as pd

data = {'種類': ["Bike","Bus","Car","Truck"],
        '數量': [3,4,6,2],
        '輪數': [2,4,4,6] } 
df = pd.DataFrame(data) 
df.set_index("種類", inplace=True)
print(df)
df2 = df.drop(["Bus", "Truck"])
print(df2)
df3 = df.drop(df.index[[0, 2]])
print(df3)
df4 = df.drop(["輪數"], axis=1)
print(df4)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-1-3.py

import pandas as pd

data = {'種類': ["Bike","Bus","Car","Truck"],
        '數量': [3,4,6,2],
        '輪數': [2,4,4,6] } 
df = pd.DataFrame(data) 
print(df.head(2))
print(df.tail(3))

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-1-3a.py

import pandas as pd

data = {'種類': ["Bike","Bus","Car","Truck"],
        '數量': [3,4,6,2],
        '輪數': [2,4,4,6] } 
df = pd.DataFrame(data) 
print(df.index)
print(df.columns)
print(df.values)

print(df.values[2])
print(df.values[1][2])


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-1-3b.py

import pandas as pd

data = {'種類': ["Bike","Bus","Car","Truck"],
        '數量': [3,4,6,2],
        '輪數': [2,4,4,6] } 
df = pd.DataFrame(data) 
print(len(df))
print(df.shape)



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-1-3c.py

import pandas as pd

data = {'種類': ["Bike","Bus","Car","Truck"],
        '數量': [3,4,6,2],
        '輪數': [2,4,4,6] } 
df = pd.DataFrame(data) 
print(df.info())
print(df.describe())



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-1-4.py

import pandas as pd

data = {'種類': ["Bike","Bus","Car","Truck"],
        '數量': [3,4,6,2],
        '輪數': ["2","4","4","6"] } 
df = pd.DataFrame(data, index=["A","B","C","D"]) 
print(df["種類"])

print(df[["數量", "輪數"]].head(3))

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-1-4a.py

import pandas as pd

data = {'種類': ["Bike","Bus","Car","Truck"],
        '數量': [3,4,6,2],
        '輪數': ["2","4","4","6"] } 
df = pd.DataFrame(data, index=["A","B","C","D"]) 
print(df[0:2])

print(df["A":"C"])

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-1-4b.py

import pandas as pd

data = {'種類': ["Bike","Bus","Car","Truck"],
        '數量': [3,4,6,2],
        '輪數': ["2","4","4","6"] } 
df = pd.DataFrame(data, index=["A","B","C","D"]) 
print(df.loc["A", "數量"])
print(df.loc[["C","D"], ["數量","輪數"]])

print(df.loc[:, ["數量","輪數"]])
print(df.loc["B":"C", "種類":"數量"])

print(df.iloc[3])
print(df.iloc[2:4, 1:3])

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-1-4c.py

import pandas as pd

data = {'種類': ["Bike","Bus","Car","Truck"],
        '數量': [3,4,6,2],
        '輪數': ["2","4","4","6"] } 
df = pd.DataFrame(data, index=["A","B","C","D"]) 
df["輪數"] = df["輪數"].astype("int64")
print(df[df.輪數 > 3])

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-1-4d.py

import pandas as pd

data = {'種類': ["Bike","Bus","Car","Truck"],
        '數量': [3,4,6,2],
        '輪數': ["2","4","4","6"] } 
df = pd.DataFrame(data, index=["A","B","C","D"]) 
df2 = df.sort_values("數量", ascending=False)
print(df2)


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-3.py

import pandas as pd

dates_d = pd.date_range("20170109", periods=5, freq="D")
print(dates_d)
df = pd.read_csv("2330.TW.csv")
df["Date"] = dates_d
print(df)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-3a.py

import pandas as pd

df = pd.read_csv("2330.TW.csv")
print(df["Volume"].pct_change())

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-3b.py

import pandas as pd

df = pd.read_csv("2330.TW.csv")
print(df["Close"].unique())
print(df["Close"].nunique())
print(df["Close"].value_counts())

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-3c.py

import pandas as pd

df1 = pd.DataFrame({"Name":["A", "B"],"Value":[11, 12]})
df2 = pd.DataFrame({"Name":["C"],"Value":[23]})
df3 = pd.concat([df1, df2], ignore_index=True)
print(df3)

df4 = pd.DataFrame({"Name":["A","B"],"Value":[11, 12]})
df5 = pd.DataFrame({"Size":["XL","L"]})
df6 = pd.concat([df4, df5], axis=1)
print(df6)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-3d.py

import pandas as pd

df = pd.read_csv("batchSales.csv")
print(df)
df2 = df.groupby("BatchNo").mean()
print(df2)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-4-1.py

import pandas as pd

df = pd.read_csv("titanic_test.csv")
print(df.head())
print(df.info())

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-4-1a.py

import pandas as pd

df = pd.read_csv("titanic_test.csv")
print(df["Age"].isnull().sum())
df2 = df.dropna(subset=["Age"])
print(len(df2))


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-4-1b.py

import pandas as pd

df = pd.read_csv("titanic_test.csv")
df["Age"] = df["Age"].fillna(value=20)
print(df["Age"].isnull().sum())



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-4-1c.py

import pandas as pd

df = pd.read_csv("titanic_test.csv")
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df["Age"].isnull().sum())



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-4-2.py

import pandas as pd

df = pd.read_csv("sales.csv")
df1 = df.drop_duplicates("Country")
print(df1)




print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-4-3.py

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




print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-5.py

import pandas as pd

df = pd.read_csv("2330_2019_9.csv")
data = pd.DataFrame()
data["Date"] = pd.to_datetime(df["Date"])
data["Adj Close"] = df["Adj Close"]
data["High"] = df["High"]
data["Low"] = df["Low"]
data = data.set_index("Date")

data.plot(kind="line")





print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-5a.py

import pandas as pd

df = pd.read_csv("drinks.csv")
print(df)
df.set_index("Type", inplace=True)
df.plot(kind="bar")

df.plot(kind="barh")


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python從網路爬蟲到生活應用超實務\ch06\ch6-5b.py

import pandas as pd

df = pd.read_csv("NBA_players_salary_stats_2018.csv")
df.plot(kind="scatter", x="PTS", y="salary", 
        title="Scatter Plot of NBA Salary and PTS")



print('------------------------------------------------------------')	#60個

