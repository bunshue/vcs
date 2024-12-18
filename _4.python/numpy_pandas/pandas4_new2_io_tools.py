import sys
import numpy as np
import pandas as pd

print("------------------------------------------------------------")  # 60個

# 2. Pandas - IO tools

"""
讀寫本文格式的數據

將text轉換為DataFrame的函數，其選項分為:

    索引
    類型推斷 和 數據轉換
    日期解析
    佚代
    不規整數據問題

類型推斷(type inference)是最重要的功能之一，不需要指定列的資料型態
"""

"""
!cat data3/ex1.csv

a,b,c,d,message
1,2,3,4,hello
5,6,7,8,world
9,10,11,12,foo

"""

# read_csv 讀入 csv檔案
df = pd.read_csv("data3/ex1.csv")
print(df)


# 也可以讀入table，不過需要指定分隔符號
df = pd.read_table("data3/ex1.csv", sep=",")
print(df)

# 沒有欄位名稱列的檔案
"""
!type data3/ex2.csv

1,2,3,4,hello
5,6,7,8,world
9,10,11,12,foo
"""
# 預設會把第一列當作 欄位名稱列
df = pd.read_csv(
    "data3/ex2.csv",
)
print(df)

# 標示沒有欄位名稱列
df = pd.read_csv("data3/ex2.csv", header=None)
print(df)

# 自定義 欄位名稱
fields = ["a", "b", "c", "d", "message"]
df = pd.read_csv("data3/ex2.csv", names=fields)
print(df)

# 可以 使用 index_col 參數，將某一欄設定為DataFrame的索引
fields = ["a", "b", "c", "d", "message"]
df = pd.read_csv("data3/ex2.csv", names=fields, index_col="message")
print(df)

# 可以 使用 index_col 參數，將多個欄設定為DataFrame的層次化索引
"""
!type data3/ex3.csv
"""
df = pd.read_csv("data3/ex3.csv", index_col=["key1", "key2"])
print(df)
"""
key1,key2,value1,value2
one,a,1,2
one,b,3,4
one,c,5,6
one,d,7,8
two,a,9,10
two,b,11,12
two,c,13,14
two,d,15,16
"""

# 如果不是以固定的分隔符號來分隔字段，可以用 read_table + regex 作為 sep參數
# 由於列名比資料列的數量少，因此read_table推斷第一列應該是DataFrame的索引
# 以不定數量的空白做分隔

#!type "data3/ex3 - 1.csv"

df = pd.read_table("data3/ex3 - 1.csv", sep="\s+")
print(df)

# 讀檔時，可以用 skiprows 來跳過指定的 rows
#!type data3/ex4.csv

df = pd.read_csv("data3/ex4.csv", skiprows=[0, 2, 3], index_col="message")
print(df)
"""
# hey!
a,b,c,d,message
# just wanted to make things more difficult for you
# who read CSV files with computers, anyway?
1,2,3,4,hello
5,6,7,8,world
9,10,11,12,foo
"""
# 缺失數據的處理
# read_csv 會自動判斷，然後以NaN標示缺失數據的位置
#!type data3/ex5.csv

df = pd.read_csv("data3/ex5.csv", index_col="something")
print(df)

"""
something,a,b,c,d,message
one,1,2,3,4,NA
two,5,6,,8,world
three,9,10,11,12,foo 
"""

# isnull()，判斷元素是否為NaN
cc = df.isnull()
print(cc)

cc = pd.isnull(df)
print(cc)


# na_values 參數可指定用於標示缺失數據的字串
df = pd.read_csv("data3/ex5.csv", index_col="something", na_values=["NULL"])
print(df)

# 為各列分別指定不同的 缺失值標示字串
sentinels = {"message": ["foo", "NA"], "something": ["two"]}
df = pd.read_csv("data3/ex5.csv", na_values=sentinels)
print(df)

print("逐塊讀取文本文件")

# 設定 nrows參數，設定讀入的列數
#!type data3/ex5.csv

df = pd.read_csv("data3/ex5.csv", nrows=2)
print(df)
"""
something,a,b,c,d,message
one,1,2,3,4,NA
two,5,6,,8,world
three,9,10,11,12,foo 
"""
# 如果要逐塊讀取，則設定chunksize
"""
!type data3/ex5.csv
"""
chunker = pd.read_csv("data3/ex5.csv", chunksize=2)
print(chunker)
"""
something,a,b,c,d,message
one,1,2,3,4,NA
two,5,6,,8,world
three,9,10,11,12,foo 
"""
tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece["something"].value_counts(), fill_value=0)
tot = tot.sort_values(ascending=False)
print(tot)

print("將數據寫出到文本格式")

"""
!type data3/ex5.csv
"""
df = pd.read_csv("data3/ex5.csv")
print(df)
"""
something,a,b,c,d,message
one,1,2,3,4,NA
two,5,6,,8,world
three,9,10,11,12,foo 
"""
# 以 to_csv() 將數據寫出到一個 以逗號分隔 的檔案中
df.to_csv("tmp_ex5-1a.csv")
"""
!type "tmp_ex5-1a.csv"

,something,a,b,c,d,message
0,one,1,2,3.0,4,
1,two,5,6,,8,world
2,three,9,10,11.0,12,foo 
"""
# 寫出的時候，可以設定 sep 參數 指定其他的分隔符號
df.to_csv("tmp_ex5-1b.csv", sep="|")
"""
!type "tmp_ex5-1b.csv"

|something|a|b|c|d|message
0|one|1|2|3.0|4|
1|two|5|6||8|world
2|three|9|10|11.0|12|foo 
"""

# 設定 na_rep 參數，以其他的符號 明確地標示 缺失值
df.to_csv("tmp_ex5-1c.csv", na_rep="NULL")
"""
!type "tmp_ex5-1c.csv"

,something,a,b,c,d,message
0,one,1,2,3.0,4,NULL
1,two,5,6,NULL,8,world
2,three,9,10,11.0,12,foo 
"""

# 可以禁止列出 row, column的標籤
# 不輸出index、header
df.to_csv("tmp_ex5-1d.csv", na_rep="NULL", index=False, header=False)
"""
!type "tmp_ex5-1d.csv"

one,1,2,3.0,4,NULL
two,5,6,NULL,8,world
three,9,10,11.0,12,foo 
"""
print("不輸出index")
df.to_csv("tmp_ex5-1e.csv", na_rep="NULL", index=False)
"""
!type "tmp_ex5-1e.csv"

something,a,b,c,d,message
one,1,2,3.0,4,NULL
two,5,6,NULL,8,world
three,9,10,11.0,12,foo 
"""

print("設定 cols 參數，只寫出一部分的欄位")
print(df)
# NG
# df.to_csv("tmp_ex5-1f.csv", index = False, cols = ['a', 'b', 'c']) # 好像無效呢?

"""
!type "tmp_ex5-1f.csv"

something,a,b,c,d,message
one,1,2,3.0,4,
two,5,6,,8,world
three,9,10,11.0,12,foo 
"""

ts = pd.Series(np.arange(7), index=dates)
print(ts)

print("Series物件 也有to_csv方法")
ts.to_csv("tmp_treseries.csv")

"""
!type "tmp_treseries.csv"

2000-01-01,0
2000-01-02,1
2000-01-03,2
2000-01-04,3
2000-01-05,4
2000-01-06,5
2000-01-07,6
"""

print("Series類別 也有to_csv方法 (頂層)")
pd.Series.to_csv(ts, "tmp_treseries.csv")

"""
!type "tmp_treseries.csv

2000-01-01,0
2000-01-02,1
2000-01-03,2
2000-01-04,3
2000-01-05,4
2000-01-06,5
2000-01-07,6
"""

# 使用 from_csv 將檔案讀入成為 Series
# 有 date欄位，須設定 parse_dates 參數
""" NG
ts = pd.Series.from_csv('tmp_treseries.csv', parse_dates = True)
print(ts)
"""

print("JSON(JavaScript Object Notation)數據")

obj = """
{
"name": "Wes", 
"place_lived": ["United States", "Spain", "Germany"],
"pet": null,
"siblings": [{"name": "Scott", "age": 25, "pet": "Zuko"}, {"name": "Wei", "age": 25, "pet": "Cisco"}]
}
"""

print("用 json.loads 可將JSON字串還原成 dict物件")
import json

result = json.loads(obj)
print(result)

"""
{'name': 'Wes',
 'pet': None,
 'place_lived': ['United States', 'Spain', 'Germany'],
 'siblings': [{'age': 25, 'name': 'Scott', 'pet': 'Zuko'},
  {'age': 25, 'name': 'Wei', 'pet': 'Cisco'}]}
"""

print("JSON物件其實是 dict 物件")
print(type(result))

# dict

# 使用索引，可以探及 dict內部的資料
cc = type(result["siblings"][0]["age"])
print(cc)

# int

# json.dumps 可將dict物件轉換成 JSON字串
# json字串 和json物件 需區分清楚
# json物件 其實就是 dict
cc = json.dumps(result)
print(cc)

"""
'{"place_lived": ["United States", "Spain", "Germany"], "siblings": [{"pet": "Zuko", "age": 25, "name": "Scott"}, {"pet": "Cisco", "age": 25, "name": "Wei"}], "pet": null, "name": "Wes"}'
"""

cc = result["siblings"]
print(cc)

"""
[{'age': 25, 'name': 'Scott', 'pet': 'Zuko'},
 {'age': 25, 'name': 'Wei', 'pet': 'Cisco'}]
"""

print("以JSON物件建構DataFrame")
df_siblings = pd.DataFrame(result["siblings"], columns=["age", "name", "pet"]).T
print(df_siblings)

print("DataFrame有 to_json() 方法，可將DataFrame序列化")
siblings_json_string = df_siblings.to_json()
print(siblings_json_string)

#'{"0":{"age":25,"name":"Scott","pet":"Zuko"},"1":{"age":25,"name":"Wei","pet":"Cisco"}}'

siblings_json = json.loads(siblings_json_string)
print(siblings_json)

"""
{'0': {'age': 25, 'name': 'Scott', 'pet': 'Zuko'},
 '1': {'age': 25, 'name': 'Wei', 'pet': 'Cisco'}}
"""

print("DataFrame有 from_dict() 方法，可反序列化")
df_siblings = pd.DataFrame.from_dict(siblings_json)
print(df_siblings)

print("------------------------------------------------------------")  # 60個

print("二進制數據格式")

# pandas物件都有一個 save方法，可以將物件數據以pickle的形式保存到硬碟
df = pd.read_csv("data3/ex1.csv")
print(df)

cc = type(df)
print(cc)

print("輸出 pickle資料到檔案")

import pickle

df.to_pickle("tmp_ex1.pickle")
df = None
del df

print("讀入 pickle檔案資料成為物件")
df = pickle.load(open("tmp_ex1.pickle", "rb"))
print(df)

cc = type(df)
print(cc)

# pandas.core.frame.DataFrame

print("讀取 Microsoft Excel文件")
""" NG
# 使用 ExcelFile 方法
xls_file = pd.ExcelFile('data3/test.xls', header = None)
table = xls_file.parse('Sheet1')
print(table)

cc = type(table)
print(cc)

#pandas.core.frame.DataFrame
"""

print("使用數據庫")

# 使用 SQLite3

import sqlite3

# 連接資料庫
con = sqlite3.connect(":memory:")

# 建立資料表
query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20), c REAL, d INTEGER);
"""
con.execute(query)
con.commit()

# 插入資料
data = [
    ("Atlanta", "Georgia", 1.25, 6),
    ("Tallahassee", "Florida", 2.6, 3),
    ("Sacramento", "California", 1.7, 5),
]
stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"
con.executemany(stmt, data)
con.commit()


# 查詢資料
cursor = con.execute("select * from test")
rows = cursor.fetchall()
print(rows)

"""
[('Atlanta', 'Georgia', 1.25, 6),
 ('Tallahassee', 'Florida', 2.6, 3),
 ('Sacramento', 'California', 1.7, 5)]
"""

# cursor.description 包含 欄位資訊
print(cursor.description)

"""

(('a', None, None, None, None, None, None),
 ('b', None, None, None, None, None, None),
 ('c', None, None, None, None, None, None),
 ('d', None, None, None, None, None, None))
"""

# 用資料庫的資料建立 DataFrame
df = pd.DataFrame(rows, columns=[f[0] for f in cursor.description])
print(df)

# 使用 pandas.io.sql 來讀取資料庫資料並創建 DataFrame

import pandas.io.sql as sql

df = sql.read_sql("select * from test", con)
print(df)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
