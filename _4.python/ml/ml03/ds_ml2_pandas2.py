"""

必學！Python 資料科學‧機器學習最強套件 pandas 2

"""

import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

import numpy as np
import pandas as pd

print('------------------------------------------------------------')	#60個

#索引、欄位內容「一致」時的串接做法

def make_random_df(index, columns, seed):
  np.random.seed(seed)
  df = pd.DataFrame()
  for column in columns:
    df[column] = np.random.choice(range(1, 101), len(index))
  df.index = index
  return df

columns = ["apple", "orange", "banana"]
df_data1 = make_random_df(range(1, 5), columns, 0)
df_data2 = make_random_df(range(1, 5), columns, 1)

print(df_data1)
print(df_data2)

df1 = pd.concat( [df_data1, df_data2], axis = 0)
print(df1)

df2 = pd.concat([df_data1, df_data2], axis = 1)
print(df2)

print('------------------------------------------------------------')	#60個

#索引、欄位內容「不一致」時的串接做法

def make_random_df(index, columns, seed):
  np.random.seed(seed)
  df = pd.DataFrame()
  for column in columns:
    df[column] = np.random.choice(range(1, 101), len(index))
  df.index = index
  return df

columns1 = ["apple", "orange", "banana"]
columns2 = ["orange", "kiwifruit", "banana"]

df_data1 = make_random_df(range(1, 5), columns1, 0)
df_data2 = make_random_df(np.arange(1, 8, 2), columns2, 1)

print(df_data1)
print(df_data2)

df1 = pd.concat([df_data1, df_data2], axis = 0)
print(df1)

df2 = pd.concat([df_data1, df_data2], axis = 1)
print(df2)

print('------------------------------------------------------------')	#60個

#於橫向串接時增列上一層的欄位

def make_random_df(index, columns, seed):
  np.random.seed(seed)
  df = pd.DataFrame()
  for column in columns:
    df[column] = np.random.choice(range(1, 101), len(index))
  df.index = index
  return df

columns = ["apple", "orange", "banana"]
df_data1 = make_random_df(range(1, 5), columns, 0)
df_data2 = make_random_df(range(1, 5), columns, 1)
print(df_data1)
print(df_data2)

df = pd.concat([df_data1, df_data2], axis = 1, keys = ["X", "Y"])
print(df)

Y_banana = df["Y", "banana"]
print(Y_banana)

print('------------------------------------------------------------')	#60個

#用 merge() 做 DataFrame 的交集合併

data1 = {"fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
         "year": [2001, 2002, 2001, 2008, 2006],
         "amount": [1, 4, 5, 6, 3]}
df1 = pd.DataFrame(data1)

data2 = {"fruits": ["apple", "orange", "banana", "strawberry", "mango"],
         "year": [2001, 2002, 2001, 2008, 2007],
         "price": [150, 120, 100, 250, 3000]}

df2 = pd.DataFrame(data2)

print('---- df1 ----\n', df1)
print('---- df2 ----\n', df2)

df3 = pd.merge(df1, df2, on = "fruits", how = "inner")

print('---- df3 ----\n', df3)
#用 merge() 做 DataFrame 的聯集合併

df3 = pd.merge(df1, df2, on = "fruits", how = "outer")

print('---- df3 ----\n', df3)

#透過「具關聯性的欄位」合併多個 DataFrame(一)

order_df = pd.DataFrame([[1000, 2546, 103],
                         [1001, 4352, 101],
                         [1002, 342, 101]],
                        columns = ["id", "item_id", "customer_id"])

print('-----order_df-----')
print(order_df)

customer_df = pd.DataFrame([[101, "Tanaka"],
                            [102, "Suzuki"],
                            [103, "Kato"]],
                           columns = ["id", "name"])

print('-----customer_df-----')
print(customer_df)

order_df = pd.merge(order_df, customer_df, left_on = "customer_id",

right_on = "id", how = "inner")

print('-----交集合併-----')
print(order_df)

print('------------------------------------------------------------')	#60個

#透過「具關聯性的欄位」合併多個DataFrame (二)

order_df = pd.DataFrame([[1000, 2546, 103],
                         [1001, 4352, 101],
                         [1002, 342, 101]],
                        columns = ["id", "item_id", "customer_id"])

print('----訂貨紀錄----\n', order_df)

customer_df = pd.DataFrame([["Tanaka"],
                            ["Suzuki"],
                            ["Kato"]],
                           columns = ["name"])

customer_df.index = [101, 102, 103]

print('----客戶資訊----\n', customer_df)

order_df = pd.merge(order_df, customer_df, left_on = "customer_id",
                    right_index = True, how = "inner")

print('----order_df----\n', order_df)


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


