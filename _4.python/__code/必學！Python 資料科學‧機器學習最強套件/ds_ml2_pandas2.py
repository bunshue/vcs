"""

必學！Python 資料科學‧機器學習最強套件 pandas 2

"""

import os
import sys
import time
import random


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


#7-2-1 索引、欄位內容「一致」時的串接做法

import numpy as np

import pandas as pd

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

   apple  orange  banana

1     45      68      37

2     48      10      88

3     65      84      71

4     68      22      89

   apple  orange  banana

1     38      76      17

2     13       6       2

3     73      80      77

4     10      65      72

df1 = pd.concat( [df_data1, df_data2], axis=0)

print(df1)

   apple  orange  banana

1     45      68      37

2     48      10      88

3     65      84      71

4     68      22      89

1     38      76      17

2     13       6       2

3     73      80      77

4     10      65      72

df2 = pd.concat([df_data1, df_data2], axis=1)

print(df2)

   apple  orange  banana  apple  orange  banana

1     45      68      37     38      76      17

2     48      10      88     13       6       2

3     65      84      71     73      80      77

4     68      22      89     10      65      72

#7-2-2 索引、欄位內容「不一致」時的串接做法

import numpy as np

import pandas as pd

​

def make_random_df(index, columns, seed):

  np.random.seed(seed)

  df = pd.DataFrame()

  for column in columns:

    df[column] = np.random.choice(range(1, 101), len(index))

  df.index = index

  return df

​

columns1 = ["apple", "orange", "banana"]

columns2 = ["orange", "kiwifruit", "banana"]

df_data1 = make_random_df(range(1, 5), columns1, 0)

df_data2 = make_random_df(np.arange(1, 8, 2), columns2, 1)

​

print(df_data1)

print(df_data2)

   apple  orange  banana

1     45      68      37

2     48      10      88

3     65      84      71

4     68      22      89

   orange  kiwifruit  banana

1      38         76      17

3      13          6       2

5      73         80      77

7      10         65      72

df1 = pd.concat([df_data1, df_data2], axis=0)

print(df1)

   apple  orange  banana  kiwifruit

1   45.0      68      37        NaN

2   48.0      10      88        NaN

3   65.0      84      71        NaN

4   68.0      22      89        NaN

1    NaN      38      17       76.0

3    NaN      13       2        6.0

5    NaN      73      77       80.0

7    NaN      10      72       65.0

df2 = pd.concat([df_data1, df_data2], axis=1)

print(df2)

   apple  orange  banana  orange  kiwifruit  banana

1   45.0    68.0    37.0    38.0       76.0    17.0

2   48.0    10.0    88.0     NaN        NaN     NaN

3   65.0    84.0    71.0    13.0        6.0     2.0

4   68.0    22.0    89.0     NaN        NaN     NaN

5    NaN     NaN     NaN    73.0       80.0    77.0

7    NaN     NaN     NaN    10.0       65.0    72.0

#7-2-3 於橫向串接時增列上一層的欄位

import numpy as np

import pandas as pd

​

def make_random_df(index, columns, seed):

  np.random.seed(seed)

  df = pd.DataFrame()

  for column in columns:

    df[column] = np.random.choice(range(1, 101), len(index))

  df.index = index

  return df

​

columns = ["apple", "orange", "banana"]

df_data1 = make_random_df(range(1, 5), columns, 0)

df_data2 = make_random_df(range(1, 5), columns, 1)

​

print(df_data1)

print(df_data2)

​

   apple  orange  banana

1     45      68      37

2     48      10      88

3     65      84      71

4     68      22      89

   apple  orange  banana

1     38      76      17

2     13       6       2

3     73      80      77

4     10      65      72

df = pd.concat([df_data1, df_data2], axis=1, keys=["X", "Y"])

print(df)

      X                   Y              

  apple orange banana apple orange banana

1    45     68     37    38     76     17

2    48     10     88    13      6      2

3    65     84     71    73     80     77

4    68     22     89    10     65     72

Y_banana = df["Y", "banana"]

print(Y_banana)

1    17

2     2

3    77

4    72

Name: (Y, banana), dtype: int64

#7-3-2 用 merge() 做 DataFrame 的交集合併

import pandas as pd

data1 = {"fruits": ["apple", "orange", "banana", "strawberry",

  "kiwifruit"],

  "year": [2001, 2002, 2001, 2008, 2006],

  "amount": [1, 4, 5, 6, 3]}

df1 = pd.DataFrame(data1)

​

data2 = {"fruits": ["apple", "orange", "banana", "strawberry",

  "mango"],

  "year": [2001, 2002, 2001, 2008, 2007],

  "price": [150, 120, 100, 250, 3000]}

df2 = pd.DataFrame(data2)

​

print('---- df1 ----\n', df1)

print('---- df2 ----\n', df2)

---- df1 ----

        fruits  year  amount

0       apple  2001       1

1      orange  2002       4

2      banana  2001       5

3  strawberry  2008       6

4   kiwifruit  2006       3

---- df2 ----

        fruits  year  price

0       apple  2001    150

1      orange  2002    120

2      banana  2001    100

3  strawberry  2008    250

4       mango  2007   3000

df3 = pd.merge(df1, df2, on="fruits", how="inner")

print('---- df3 ----\n', df3)

---- df3 ----

        fruits  year_x  amount  year_y  price

0       apple    2001       1    2001    150

1      orange    2002       4    2002    120

2      banana    2001       5    2001    100

3  strawberry    2008       6    2008    250

#7-3-3 用 merge() 做 DataFrame 的聯集合併

df3 = pd.merge(df1, df2, on="fruits", how="outer")

print('---- df3 ----\n', df3)

---- df3 ----

        fruits  year_x  amount  year_y   price

0       apple  2001.0     1.0  2001.0   150.0

1      orange  2002.0     4.0  2002.0   120.0

2      banana  2001.0     5.0  2001.0   100.0

3  strawberry  2008.0     6.0  2008.0   250.0

4   kiwifruit  2006.0     3.0     NaN     NaN

5       mango     NaN     NaN  2007.0  3000.0

#7-3-4 透過「具關聯性的欄位」合併多個 DataFrame(一)

import pandas as pd

order_df = pd.DataFrame([[1000, 2546, 103],

  [1001, 4352, 101],

  [1002, 342, 101]],

  columns=["id", "item_id", "customer_id"])

print('-----order_df-----')

print(order_df)

​

customer_df = pd.DataFrame([[101, "Tanaka"],

  [102, "Suzuki"],

  [103, "Kato"]],

  columns=["id", "name"])

print('-----customer_df-----')

print(customer_df)

-----order_df-----

     id  item_id  customer_id

0  1000     2546          103

1  1001     4352          101

2  1002      342          101

-----customer_df-----

    id    name

0  101  Tanaka

1  102  Suzuki

2  103    Kato

order_df = pd.merge(order_df, customer_df, left_on="customer_id",

right_on="id", how="inner")

print('-----交集合併-----')

print(order_df)

-----交集合併-----

   id_x  item_id  customer_id  id_y    name

0  1000     2546          103   103    Kato

1  1001     4352          101   101  Tanaka

2  1002      342          101   101  Tanaka

#7-3-5 透過「具關聯性的欄位」合併多個DataFrame (二)

import pandas as pd

order_df = pd.DataFrame([[1000, 2546, 103],

  [1001, 4352, 101],

  [1002, 342, 101]],

  columns=["id", "item_id", "customer_id"])

print('----訂貨紀錄----\n', order_df)

​

customer_df = pd.DataFrame([["Tanaka"],

  ["Suzuki"],

  ["Kato"]],

  columns=["name"])

​

customer_df.index = [101, 102, 103]

print('----客戶資訊----\n', customer_df)

----訂貨紀錄----

      id  item_id  customer_id

0  1000     2546          103

1  1001     4352          101

2  1002      342          101

----客戶資訊----

        name

101  Tanaka

102  Suzuki

103    Kato

order_df = pd.merge(order_df, customer_df, left_on="customer_id",

                    right_index=True, how="inner")

print('----order_df----\n', order_df)

----order_df----

      id  item_id  customer_id    name

0  1000     2546          103    Kato

1  1001     4352          101  Tanaka

2  1002      342          101  Tanaka





print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


