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

s = pd.Series([12, 29, 72,4, 8, 10]) 
print(s)

print("------------------------------------------------------------")  # 60個

fruits = ["蘋果", "橘子", "梨子", "櫻桃"]
quantities = [15, 33, 45, 55]
s = pd.Series(quantities, index=fruits) 
print(s)
print(s.index)
print(s.values)  

print("------------------------------------------------------------")  # 60個

fruits = ["蘋果", "橘子", "梨子", "櫻桃"]
quantities = [15, 33, 45, 55]
s = pd.Series(quantities, index=fruits) 
p = pd.Series([11, 16, 21, 32], index=fruits) 

print(s + p)
print("總計=", sum(s + p))

print("------------------------------------------------------------")  # 60個

fruits = ["蘋果", "橘子", "梨子", "櫻桃"]
s = pd.Series([15, 33, 45, 55], index=fruits) 
print("橘子=", s["橘子"])

print("------------------------------")  # 30個

print(s[["橘子","梨子","櫻桃"]])

print((s+2)*3)

print(s.apply(np.sin))
 
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
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

print("------------------------------")  # 30個

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

print("------------------------------")  # 30個

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

""" lack file
# 匯入JSON格式的檔案
df2 = pd.read_json("tmp_dists.json")
print(df2)
df.to_html("tmp8-2-2a-02.html")
"""

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
