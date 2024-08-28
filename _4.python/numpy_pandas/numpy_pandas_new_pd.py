"""
numpy的使用

numpy: 數值計算的標準套件
"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

# DataFrame 是二維數組對象
df = pd.DataFrame(np.random.randn(6,4), columns=list('ABCD'))
print(df)

print(df.iloc[0])

print('顯示A欄')
print(df.A)

print("Row data type: {}".format(type(df.iloc[0])))
print("Column data type: {}".format(type(df.A)))

print('df之大小')
print(df.shape)

print('df之內容')
print(df)

print('df之頭3行')
print(df.head(3))

print('df之尾2行')
print(df.tail(2))

print('顯示df之欄')
print(df.columns)
print('顯示df之index')
print(df.index)
print('顯示df之describe')
print(df.describe())

print('排序')
print(df.sort_index(axis=1, ascending=False))

print('依B欄排序')
print(df.sort_values(by='B'))

print('顯示df之3:5')
print(df[3:5])

print('顯示df之A B D欄')
print(df[['A', 'B', 'D']])

print('顯示')
print(df.loc[3, 'A'])

print('顯示')
print(df.iloc[3, 0])

print('顯示')
print(df.iloc[2:5, 0:2])

print('顯示')
print(df[df.C > 0])

print('加入TAG')
df["TAG"] = ["cat", "dog", "cat", "cat", "cat", "dog"]
print(df)

print(df.groupby('TAG').sum())

print('顯示')
n_items = 366
ts = pd.Series(np.random.randn(n_items), index=pd.date_range('20000101', periods=n_items))

print('顯示ts大小')
print(ts.shape)

print('顯示ts頭5項')
print(ts.head(5))

print('顯示')
print(ts.resample("1m").sum())

plt.figure(figsize=(10, 6))
cs = ts.cumsum()
cs.plot()
plt.show()

plt.figure(figsize=(10, 6))
ts.resample("1m").sum().plot.bar()
plt.show()

df = pd.DataFrame(np.random.randn(100, 4), columns=list('ABCD'))
df.to_csv('tmp_data.csv')

df = pd.read_csv('tmp_data.csv', index_col=0)
print(df.shape)
print(df.head(5))

print("------------------------------------------------------------")  # 60個


import sqlite3

con = sqlite3.connect("data/weather_2012.sqlite")
df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con)
print(df)

print("------------------------------")  # 30個

df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con, index_col="id")
print(df)

print("------------------------------")  # 30個

df = pd.read_sql(
    "SELECT * from weather_2012 LIMIT 3", con, index_col=["id", "date_time"]
)
print(df)

print("------------------------------")  # 30個

# Writing to a SQLite database

weather_df = pd.read_csv("data/weather_2012.csv")
con = sqlite3.connect("tmp_test_db.sqlite")
con.execute("DROP TABLE IF EXISTS weather_2012")
weather_df.to_sql("weather_2012", con)


con = sqlite3.connect("tmp_test_db.sqlite")
df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con)
print(df)

con = sqlite3.connect("tmp_test_db.sqlite")
df = pd.read_sql("SELECT * from weather_2012 ORDER BY Weather LIMIT 3", con)
print(df)

print("------------------------------------------------------------")  # 60個

mydata = np.random.randn(4,3)

df2 = pd.DataFrame(mydata, columns=list("ABC"))

df3 = pd.DataFrame(np.random.randn(3,3), columns=list("ABC"))

df4 = pd.concat([df2, df3], axis=0)

df4.index = range(7)

df_grades = pd.DataFrame(np.random.randint(6,16,(100,5)), 
                      columns=["國文", "英文", "數學", 
                               "社會", "自然"])
                               
print("------------------------------------------------------------")  # 60個

print('常態分布 二維 轉 df')
df3 = pd.DataFrame(np.random.randn(3,3), columns=list("ABC"))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

data = [100, 110, 150, 170, 190, 200, 220]
x = pd.Series(data)
x.plot()
plt.show()

print("------------------------------------------------------------")  # 60個

data = [100, 110, 150, 170, 190, 200, 220]
weekday = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
x = pd.Series(data, index=weekday)
x.plot()

plt.show()


#weight = [3, 48,33,8,38,16,36,29,22,6,12,42]
#animals = ["鼠牛虎兔龍蛇馬羊猴雞狗豬"]

print("------------------------------------------------------------")  # 60個

dists = {"name": ["Zhongzheng", "Banqiao", "Taoyuan", "Beitun", 
                   "Annan", "Sanmin", "Daan", "Yonghe", 
                   "Bade", "Cianjhen", "Fengshan", 
                   "Xinyi", "Xindian"],
         "population": [159598, 551452, 441287, 275207,
                        192327, 343203, 309835, 222531,
                        198473, 189623, 359125, 
                        225561, 302070]}
df = pd.DataFrame(dists)
print(df) 
#df.to_html("ch9-4-2-01.html")  #df轉html
df.plot()

df2 = pd.DataFrame(dists, 
                   columns=["population"],
                   index=dists["name"])
print(df2)
#df2.to_html("ch9-4-2-02.html")  #df轉html
df2.plot()
plt.show()

print("------------------------------------------------------------")  # 60個

dists = {"name": ["Zhongzheng", "Banqiao", "Taoyuan", "Beitun", 
                   "Annan", "Sanmin", "Daan", "Yonghe", 
                   "Bade", "Cianjhen", "Fengshan", 
                   "Xinyi", "Xindian"],
         "population": [159598, 551452, 441287, 275207,
                        192327, 343203, 309835, 222531,
                        198473, 189623, 359125, 
                        225561, 302070]}

df = pd.DataFrame(dists, 
                   columns=["population"],
                   index=dists["name"])
print(df)
df.plot(xticks=range(len(df.index)),
        use_index=True)

df.plot(xticks=range(len(df.index)),
        use_index=True,
        rot=90)

plt.show()

print("------------------------------------------------------------")  # 60個

dists = {"區名": ["中正區", "板橋區", "桃園區", "北屯區", 
                  "安南區", "三民區", "大安區", "永和區", 
                  "八德區", "前鎮區", "鳳山區", 
                  "信義區", "新店區"],
         "人口": [159598, 551452, 441287, 275207,
                  192327, 343203, 309835, 222531,
                  198473, 189623, 359125, 
                  225561, 302070],
         "面積": [7.6071, 23.1373, 34.8046, 62.7034, 
                  107.2016, 19.7866, 11.3614, 5.7138, 
                  33.7111, 19.1207, 26.7590, 
                  11.2077, 120.2255]}

df = pd.DataFrame(dists, 
                  columns=["人口", "面積"],
                  index=dists["區名"])
print(df)
#df.to_html("ch9-4-3.html")  #df轉html
df["面積"] *= 1000
df.plot(xticks=range(len(df.index)),
        use_index=True,
        rot=45)

plt.show()

print("------------------------------------------------------------")  # 60個

data = [100, 110, 150, 170, 190, 200, 220]
s = pd.Series(data)
s.plot(kind="bar", rot=0)
plt.show()

print("------------------------------------------------------------")  # 60個

usage = {"os": ["Windows","Mac OS","Linux","Chrome OS","BSD"],
         "percentage": [88.78, 8.21, 2.32, 0.34, 0.02]}

df = pd.DataFrame(usage, 
                  columns=["percentage"],
                  index=usage["os"])
print(df)
df.to_html("tmp_ch9-4-4.html")
df.plot(kind="bar")

plt.show()

print("------------------------------------------------------------")  # 60個

fruits = ["蘋果","梨子","香蕉","橙子"]
percentage = [30, 10, 40, 20]

s = pd.Series(percentage, index=fruits, name="水果")
print(s)
s.plot(kind="pie")
plt.show()

print("------------------------------------------------------------")  # 60個

fruits = ["蘋果","梨子","香蕉","橙子"]
percentage = [30, 10, 40, 20]

s = pd.Series(percentage, index=fruits, name="水果")
print(s)
explode = [0.1, 0.3, 0.1, 0.3]
s.plot(kind="pie",
       figsize=(6, 6),
       explode=explode)
plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)

df = pd.DataFrame({"x":x, "y":y})

df.plot(kind="scatter", x="x", y="y", 
        title="Sin(x)")

plt.show()

print("------------------------------------------------------------")  # 60個

iris = pd.read_csv("data/iris.csv")

iris.boxplot(column="sepal_length",
             by="target",
             figsize=(6,5))
plt.show()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

s = pd.Series([12, 29, 72,4, 8, 10]) 
print(s)

print("------------------------------------------------------------")  # 60個

fruits = ["蘋果", "橘子", "梨子", "櫻桃"]
quantities = [15, 33, 45, 55]
s = pd.Series(quantities, index=fruits) 
print(s)
print("---------------------------")
print(s.index)
print("---------------------------")
print(s.values)  

print("------------------------------------------------------------")  # 60個

fruits = ["蘋果", "橘子", "梨子", "櫻桃"]
quantities = [15, 33, 45, 55]
s = pd.Series(quantities, index=fruits) 
p = pd.Series([11, 16, 21, 32], index=fruits) 
print(s + p)
print("---------------------------")
print("總計=", sum(s + p))

print("------------------------------------------------------------")  # 60個

fruits = ["蘋果", "橘子", "梨子", "櫻桃"]
s = pd.Series([15, 33, 45, 55], index=fruits) 
print("橘子=", s["橘子"])
print("---------------------------")
print(s[["橘子","梨子","櫻桃"]])
print("---------------------------")
print((s+2)*3)
print("---------------------------")
print(s.apply(np.sin))
 
print("------------------------------------------------------------")  # 60個

dists = {"name": ["中正區", "板橋區", "桃園區", "北屯區", 
                   "安南區", "三民區", "大安區", "永和區", 
                   "八德區", "前鎮區", "鳳山區", 
                   "信義區", "新店區"],
         "population": [159598, 551452, 441287, 275207,
                        192327, 343203, 309835, 222531,
                        198473, 189623, 359125, 
                        225561, 302070],
         "city": ["台北市", "新北市", "桃園市", "台中市",
                  "台南市", "高雄市", "台北市", "新北市",
                  "桃園市", "高雄市", "高雄市",
                  "台北市", "新北市"]}
df = pd.DataFrame(dists) 
print(df)
df.to_html("tmp8-2-1.html")

print("------------------------------------------------------------")  # 60個

dists = {"name": ["中正區", "板橋區", "桃園區", "北屯區", 
                   "安南區", "三民區", "大安區", "永和區", 
                   "八德區", "前鎮區", "鳳山區", 
                   "信義區", "新店區"],
         "population": [159598, 551452, 441287, 275207,
                        192327, 343203, 309835, 222531,
                        198473, 189623, 359125, 
                        225561, 302070],
         "city": ["台北市", "新北市", "桃園市", "台中市",
                  "台南市", "高雄市", "台北市", "新北市",
                  "桃園市", "高雄市", "高雄市",
                  "台北市", "新北市"]}
         
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]         
df = pd.DataFrame(dists, index=ordinals) 
print(df)  
df.to_html("tmp8-2-1a.html")
print("---------------------------")
df2 = pd.DataFrame(dists)
df2.index = ordinals
print(df2) 

print("------------------------------------------------------------")  # 60個

dists = {"name": ["中正區", "板橋區", "桃園區", "北屯區", 
                   "安南區", "三民區", "大安區", "永和區", 
                   "八德區", "前鎮區", "鳳山區", 
                   "信義區", "新店區"],
         "population": [159598, 551452, 441287, 275207,
                        192327, 343203, 309835, 222531,
                        198473, 189623, 359125, 
                        225561, 302070],
         "city": ["台北市", "新北市", "桃園市", "台中市",
                  "台南市", "高雄市", "台北市", "新北市",
                  "桃園市", "高雄市", "高雄市",
                  "台北市", "新北市"]}
         
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]         
df = pd.DataFrame(dists, 
                  columns = ["name", "city", "population"],
                  index=ordinals) 
print(df)
df.to_html("tmp8-2-1b.html")  
print("---------------------------")
df2 = pd.DataFrame(dists, index=ordinals)
df2.columns = ["name", "city", "population"]
print(df2) 

print("------------------------------------------------------------")  # 60個

dists = {"name": ["中正區", "板橋區", "桃園區", "北屯區", 
                   "安南區", "三民區", "大安區", "永和區", 
                   "八德區", "前鎮區", "鳳山區", 
                   "信義區", "新店區"],
         "population": [159598, 551452, 441287, 275207,
                        192327, 343203, 309835, 222531,
                        198473, 189623, 359125, 
                        225561, 302070],
         "city": ["台北市", "新北市", "桃園市", "台中市",
                  "台南市", "高雄市", "台北市", "新北市",
                  "桃園市", "高雄市", "高雄市",
                  "台北市", "新北市"]}
         
df = pd.DataFrame(dists, 
                  columns = ["name", "population"],
                  index = dists["city"]) 
print(df) 
df.to_html("tmp8-2-1c.html")

print("------------------------------------------------------------")  # 60個

dists = {"name": ["中正區", "板橋區", "桃園區", "北屯區", 
                   "安南區", "三民區", "大安區", "永和區", 
                   "八德區", "前鎮區", "鳳山區", 
                   "信義區", "新店區"],
         "population": [159598, 551452, 441287, 275207,
                        192327, 343203, 309835, 222531,
                        198473, 189623, 359125, 
                        225561, 302070],
         "city": ["台北市", "新北市", "桃園市", "台中市",
                  "台南市", "高雄市", "台北市", "新北市",
                  "桃園市", "高雄市", "高雄市",
                  "台北市", "新北市"]}
         
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]         
df = pd.DataFrame(dists, 
                  columns = ["name", "population"],
                  index = dists["city"]) 
print(df.T) 
df.T.to_html("tmp8-2-1d.html")

print("------------------------------------------------------------")  # 60個

dists = {"name": ["中正區", "板橋區", "桃園區", "北屯區", 
                   "安南區", "三民區", "大安區", "永和區", 
                   "八德區", "前鎮區", "鳳山區", 
                   "信義區", "新店區"],
         "population": [159598, 551452, 441287, 275207,
                        192327, 343203, 309835, 222531,
                        198473, 189623, 359125, 
                        225561, 302070],
         "city": ["台北市", "新北市", "桃園市", "台中市",
                  "台南市", "高雄市", "台北市", "新北市",
                  "桃園市", "高雄市", "高雄市",
                  "台北市", "新北市"]}
df = pd.DataFrame(dists) 

df.to_csv("tmp_dists2.csv", index=False, encoding="utf8")
df.to_json("tmp_dists.json")

print("------------------------------------------------------------")  # 60個

# 匯入CSV格式的檔案
df = pd.read_csv("tmp_dists2.csv", encoding="utf8")
print(df)
df.to_html("tmp8-2-2a-01.html")
print("---------------------------")

# 匯入JSON格式的檔案
df2 = pd.read_json("tmp_dists.json")
print(df2)
df.to_html("tmp8-2-2a-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

print(df.head())
df.head().to_html("tmp8-2-3-01.html")
print("---------------------------")
print(df.head(3))
df.head(3).to_html("tmp8-2-3-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

print(df.tail())
df.tail().to_html("tmp8-2-3a-01.html")
print("---------------------------")
print(df.tail(3)) 
df.tail(3).to_html("tmp8-2-3a-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

df.columns = ["區", "人口", "直轄市"]
print(df.head(4)) 
df.head(4).to_html("tmp8-2-3b.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

df.columns = ["區", "人口", "直轄市"]
print(df.index)
print("---------------------------")
print(df.columns)
print("---------------------------")
print(df.values)

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

print("資料數= ", len(df))
print("---------------------------")
print("形狀= ", df.shape)
print("---------------------------")
df.info()

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

for index, row in df.iterrows() :
    print(index, row["city"], row["name"], row["population"])

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

df2 = df.set_index("city")
print(df2.head())
df2.head().to_html("tmp8-2-5-01.html")
print("---------------------------")
df3 = df2.reset_index()
print(df3.head())
df3.head().to_html("tmp8-2-5-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

df2 = df.set_index(["city", "name"])
df2.sort_index(ascending=False, inplace=True)
print(df2)
df2.to_html("tmp8-2-5a.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df["population"].head(3))
print("---------------------------")
print(df[["city","name"]].head(3))
df[["city","name"]].head(3).to_html("tmp8-3-1.html")
print("---------------------------")
print(df.population.head(3))   # 使用屬性方式

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df[0:3])                # 不含 3
df[0:3].to_html("tmp8-3-1a-01.html")
print("---------------------------")
print(df["sixth":"eleventh"]) # 含 "eleventh"
df["sixth":"eleventh"].to_html("tmp8-3-1a-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.loc[ordinals[1]])
print(type(df.loc[ordinals[1]]))
print("---------------------------")
print(df.loc[:,["name","population"]].head(3))
df.loc[:,["name","population"]].head(3).to_html("tmp8-3-1b-01.html")
print("---------------------------")
print(df.loc["third":"fifth", ["name","population"]])
print("---------------------------")
print(df.loc["third", ["name","population"]])
df.loc["third":"fifth", ["name","population"]].to_html("tmp8-3-1b-02.html")
print("---------------------------")
# 取得單一純量值
print(df.loc[ordinals[0], "name"])
print(type(df.loc[ordinals[0],"name"]))
print("---------------------------")
print(df.loc["first", "population"])
print(type(df.loc["first", "population"]))

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.iloc[3])          # 第 4 筆
print("---------------------------")
print(df.iloc[3:5, 1:3])   # 切割
df.iloc[3:5, 1:3].to_html("tmp8-3-1c-01.html")
print("---------------------------")
print(df.iloc[1:3, :])     # 切割列
df.iloc[1:3, :].to_html("tmp8-3-1c-02.html")
print("---------------------------")
print(df.iloc[:, 1:3])     # 切割欄
df.iloc[:, 1:3].to_html("tmp8-3-1c-03.html")
print("---------------------------")
print(df.iloc[[1,2,4], [0,2]])   # 索引清單
df.iloc[[1,2,4], [0,2]].to_html("tmp8-3-1c-04.html")
print("---------------------------")
# 取得單一純量值
print(df.iloc[1,1])
print(df.iat[1,1])

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df[df.population > 350000])
df[df.population > 350000].to_html("tmp8-3-2-01.html")
print("---------------------------")
print(df[df["city"].isin(["台北市","高雄市"])])
df[df["city"].isin(["台北市","高雄市"])].to_html("tmp8-3-2-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df[(df.population > 350000) & (df.population < 500000)])
df[(df.population > 350000) & (df.population < 500000)].to_html("tmp8-3-2a-01.html")
print("---------------------------")
print(df[df["city"].str.startswith("台")])
df[df["city"].str.startswith("台")].to_html("tmp8-3-2a-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

df2 = df.set_index("population")
print(df2.head())
df2.head().to_html("tmp8-3-3-01.html")
print("---------------------------")
df2.sort_index(ascending=False, inplace=True)
print(df2.head())
df2.head().to_html("tmp8-3-3-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.head())
df.head().to_html("tmp8-3-3a-01.html")
print("---------------------------")
df2 = df.sort_values("population", ascending=False)
print(df2.head())
df2.head().to_html("tmp8-3-3a-02.html")
print("---------------------------")
df.sort_values(["city","population"], inplace=True)
print(df.head())
df.head().to_html("tmp8-3-3a-03.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.head(2))
print("---------------------------")
# 取得與更新單一純量值
print(df.loc[ordinals[0], "population"])
df.loc[ordinals[0], "population"] = 160000
print(df.iloc[1,1])
df.iloc[1,1] = 560000
print(df.head(2))
df.head(2).to_html("tmp8-4-1.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.head(3))
print("---------------------------")
# 取得與更新單筆記錄
print(df.loc[ordinals[1]])
print("---------------------------")
s = ["新莊區", 416640, "新北市"] 
df.loc[ordinals[1]] = s
print(df.head(3))
df.head(3).to_html("tmp8-4-1a.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df)
print("---------------------------")
# 取得與更新整個欄位
print(df.loc[:, "population"])
print("---------------------------")
df.loc[:, "population"] = np.random.randint(34000, 700000, size=len(df))
print(df.head())
df.head().to_html("tmp8-4-1b.html")

print("------------------------------------------------------------")  # 60個

df = pd.DataFrame(np.random.randint(5, 1500, size=(2,3)))
print(df)
df.to_html("tmp8-4-1c-01.html")
print("---------------------------")
# 取得與更新整個DataFrame
print(df[df > 800])
df[df > 800].to_html("tmp8-4-1c-02.html")
print("---------------------------")
df[df > 800] = df - 100
print(df)
df.to_html("tmp8-4-1c-03.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.head(3))
print("---------------------------")
# 刪除純量值
print(df.loc[ordinals[0], "population"])
df.loc[ordinals[0], "population"] = None
print(df.iloc[1,1])
df.iloc[1,1] = None
print(df.head(3))
df.head(3).to_html("tmp8-4-2.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.head())
print("---------------------------")
# 刪除記錄
df2 = df.drop(["second", "fourth"])    # 2,4 筆
print(df2.head())
df2.head().to_html("tmp8-4-2a-01.html")
print("---------------------------")
df.drop(df.index[[2,3]], inplace=True) # 3,4 筆
print(df.head())
df.head().to_html("tmp8-4-2a-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.head(3))
print("---------------------------")
# 刪除欄位
df2 = df.drop(["population"], axis=1)
print(df2.head(3))
df2.head(3).to_html("tmp8-4-2b.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.tail(3))
print("---------------------------")
# 新增記錄
df.loc["third-1"] = ["士林區", 288340, "台北市"]
print(df.tail(3))
df.tail(3).to_html("tmp8-4-3-01.html")
print("---------------------------")
s = pd.Series({"city":"新北市","name":"中和區","population":413291})
df2 = df.append(s, ignore_index=True)
print(df2.tail(3))
df2.tail(3).to_html("tmp8-4-3-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.DataFrame(columns=("qty1", "qty2", "qty3"))
for i in range(5):
    df.loc[i] = [np.random.randint(-1,1) for n in range(3)]
print(df)
df.to_html("tmp8-4-3a-01.html")
print("---------------------------")
df2 = pd.DataFrame(columns=("qty1", "qty2", "qty3"))
for i in range(5):
    s = pd.Series({"qty1":np.random.randint(-1,1),"qty2":np.random.randint(-1,1),"qty3":np.random.randint(-1,1)})
    df2 = df2.append(s, ignore_index=True)
print(df2)
df.to_html("tmp8-4-3a-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

df["area"] = pd.Series([np.random.randint(6000,9000) for n in range(len(df))]).values 
print(df.head())
df.head().to_html("tmp8-4-3b-01.html")
print("---------------------------")
df.loc[:,"zip"] = np.random.randint(100, 120, size=len(df))
print(df.head())
df.head().to_html("tmp8-4-3b-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

columns =["city","name", "population"]
# 建立空的DataFrame物件
df_empty = pd.DataFrame(np.nan, index=ordinals, columns=columns)
print(df_empty)
print("---------------------------")
# 複製DataFrame物件
df_copy = df.copy()
print(df_copy)

print("------------------------------------------------------------")  # 60個

df1 = pd.DataFrame(np.random.randint(5,10,size=(3,4)),columns=["a","b","c","d"])  
df2 = pd.DataFrame(np.random.randint(5,10,size=(2,3)),columns=["b","d","a"])  
print(df1)
df1.to_html("tmp8-4-4a-01.html")
print("---------------------------")
print(df2)
df2.to_html("tmp8-4-4a-02.html")
print("---------------------------")  
df3 = pd.concat([df1,df2])  
print(df3)
df3.to_html("tmp8-4-4a-03.html")
print("---------------------------")
df4 = pd.concat([df1,df2], ignore_index=True)
print(df4) 
df4.to_html("tmp8-4-4a-04.html") 

print("------------------------------------------------------------")  # 60個

df1 = pd.DataFrame({"key":["a","b","b"],"data1":range(3)})  
df2 = pd.DataFrame({"key":["a","b","c"],"data2":range(3)})  
print(df1)
df1.to_html("tmp8-4-4b-01.html")
print("---------------------------")
print(df2)
df2.to_html("tmp8-4-4b-02.html")
print("---------------------------")
df3 = pd.merge(df1, df2)
print(df3)
df3.to_html("tmp8-4-4b-03.html")
print("---------------------------")
df4 = pd.merge(df2, df1)
print(df4)
df4.to_html("tmp8-4-4b-04.html")
print("---------------------------")
df5 = pd.merge(df2, df1, how='left')
print(df5)
df5.to_html("tmp8-4-4b-05.html")

print("------------------------------------------------------------")  # 60個

df = pd.DataFrame({"名稱" : ["客戶A", "客戶B", "客戶A", "客戶B",
                             "客戶A", "客戶B", "客戶A", "客戶A"],
                   "編號" : ["訂單1", "訂單1", "訂單2", "訂單3",
                             "訂單2", "訂單2", "訂單1", "訂單3"],
                   "數量" : np.random.randint(1,5,size=8),
                   "售價" : np.random.randint(150,500,size=8)})

print(df)
df.to_html("tmp8-5-1-01.html")
print("---------------------------")
print(df.groupby("名稱").sum())
df.groupby("名稱").sum().to_html("tmp8-5-1-02.html")
print("---------------------------")
print(df.groupby(["名稱","編號"]).sum())
df.groupby(["名稱","編號"]).sum().to_html("tmp8-5-1-03.html")

print("------------------------------------------------------------")  # 60個

products = pd.DataFrame({
        "分類": ["居家", "居家", "娛樂", "娛樂", "科技", "科技"],
        "商店": ["家樂福", "頂好", "家樂福", "全聯", "頂好","家樂福"],
        "價格":[11.42, 23.50, 19.99, 15.95, 55.75, 111.55],
        "測試分數": [4, 3, 5, 7, 5, 8]})
print(products)
products.to_html("tmp8-5-2-01.html")
print("---------------------------")
# 呼叫 pivot_table() 方法
pivot_products = products.pivot_table(index='分類',columns='商店',values='價格')
print(pivot_products)
pivot_products.to_html("tmp8-5-2-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.DataFrame(np.random.rand(6,4), columns=list("ABCD"))
print(df)
df.to_html("tmp8-5-3-01.html")
print("---------------------------")
df2 = df.apply(np.cumsum)
print(df2)
df2.to_html("tmp8-5-3-02.html")
print("---------------------------")
df3 = df.apply(lambda x: x.max() - x.min())
print(df3)

print("------------------------------------------------------------")  # 60個






print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
