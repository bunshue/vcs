"""

必學！Python 資料科學‧機器學習最強套件 pandas 1

"""

import os
import sys
import time
import random


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個



#6-2-1 建立 Series 物件

import pandas as pd

idx = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

data = [1, 4, 5, 6, 3]

series = pd.Series(data, index=idx)

print(series)

​

apple         1

orange        4

banana        5

strawberry    6

kiwifruit     3

dtype: int64

series.shape

(5,)

import pandas as pd

data = [1, 4, 5, 6, 3]

series = pd.Series(data)

print(series)

0    1

1    4

2    5

3    6

4    3

dtype: int64

import pandas as pd

fruits = {"orange": 2, "banana": 3}

print(pd.Series(fruits))

orange    2

banana    3

dtype: int64

#6-2-2 取出 Series 當中的元素

import pandas as pd

fruits = {"banana": 3, "orange": 4, "grape": 1, "peach": 5}

series = pd.Series(fruits)

print(series[0:2])

banana    3

orange    4

dtype: int64

print(series[["orange", "peach"]])

orange    4

peach     5

dtype: int64

#6-2-3 單取出「索引值」或者「內容值」-.index、.values

import pandas as pd

index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

data = [10, 5, 8, 12, 3]

series = pd.Series(data, index=index)

print(series)

apple         10

orange         5

banana         8

strawberry    12

kiwifruit      3

dtype: int64

series_index = series.index

series_values = series.values

print(series_index)

print(series_values)

Index(['apple', 'orange', 'banana', 'strawberry', 'kiwifruit'], dtype='object')

[10  5  8 12  3]

#6-2-4 新增 Series 物件的元素 – append()

import pandas as pd

idx = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

data = [10, 5, 8, 12, 3]

series = pd.Series(data, index=idx)

print(series)

apple         10

orange         5

banana         8

strawberry    12

kiwifruit      3

dtype: int64

pineapple = pd.Series([12], index=["pineapple"])

# pineapple = pd.Series( {"pineapple":12})

series = series.append(pineapple)

print(series)

apple         10

orange         5

banana         8

strawberry    12

kiwifruit      3

pineapple     12

dtype: int64

#6-2-5 刪除 Series 物件的元素 – drop()

import pandas as pd

index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

data = [10, 5, 8, 12, 3]

series = pd.Series(data, index=index)

print(series)

apple         10

orange         5

banana         8

strawberry    12

kiwifruit      3

dtype: int64

series = series.drop("strawberry")

print(series)

apple        10

orange        5

banana        8

kiwifruit     3

dtype: int64

#6-2-6 從 Series 物件篩選出想要的元素

import pandas as pd

index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

data = [10, 5, 8, 12, 3]

series = pd.Series(data, index=index)

print(series)

apple         10

orange         5

banana         8

strawberry    12

kiwifruit      3

dtype: int64

conditions = [True, True, False, False, False]

print(series[conditions])

apple     10

orange     5

dtype: int64

import pandas as pd

index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

data = [10, 5, 8, 12, 3]

series = pd.Series(data, index=index)

print(series[series >= 5])

apple         10

orange         5

banana         8

strawberry    12

dtype: int64

series = series[series >= 5][series < 10]

print(series)

orange    5

banana    8

dtype: int64

#6-2-7 將 Series 的元素排序 – sort_index()、sort_values()

import pandas as pd

index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

data = [10, 5, 8, 12, 3]

series = pd.Series(data, index=index)

print(series)

apple         10

orange         5

banana         8

strawberry    12

kiwifruit      3

dtype: int64

items1 = series.sort_index()

items2 = series.sort_values()

print(items1)

print()

print(items2)

apple         10

banana         8

kiwifruit      3

orange         5

strawberry    12

dtype: int64



kiwifruit      3

orange         5

banana         8

apple         10

strawberry    12

dtype: int64

#6-3-1 建立 DataFrame 物件 – pd.DataFrame()

import pandas as pd

index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

data1 = [10, 5, 8, 12, 3]

data2 = [30, 25, 12, 10, 8]

series1 = pd.Series(data1, index=index)

series2 = pd.Series(data2, index=index)

df = pd.DataFrame([series1, series2])

print(df)

   apple  orange  banana  strawberry  kiwifruit

0     10       5       8          12          3

1     30      25      12          10          8

import pandas as pd

data = {"fruits": ["apple", "orange", "banana", "strawberry","kiwifruit"],

        "time": [1, 4, 5, 6, 3],

        "year": [2001, 2002, 2001, 2008, 2006]}

df = pd.DataFrame(data)

print(df)

       fruits  time  year

0       apple     1  2001

1      orange     4  2002

2      banana     5  2001

3  strawberry     6  2008

4   kiwifruit     3  2006

import pandas as pd

order_df = pd.DataFrame( [[1000, 2546, 103],

                [1001, 4352, 101],

                [1002, 342, 101]],

columns=["id", "item_id", "customer_id"])

print(order_df)

     id  item_id  customer_id

0  1000     2546          103

1  1001     4352          101

2  1002      342          101

#6-3-2 修改 index 和 column 的名稱 –.index、.column

import pandas as pd

index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

data1 = [10, 5, 8, 12, 3]

data2 = [30, 25, 12, 10, 8]

series1 = pd.Series(data1, index=index)

series2 = pd.Series(data2, index=index)

df = pd.DataFrame([series1, series2])

df.index = [1, 2]

print(df)

   apple  orange  banana  strawberry  kiwifruit

1     10       5       8          12          3

2     30      25      12          10          8

#6-3-4 加入新的資料列 – append()

import pandas as pd

data = {"fruits": ["apple", "orange", "banana", "strawberry",

    "kiwifruit"],

     "year": [2001, 2002, 2001, 2008, 2006],

    "time": [1, 4, 5, 6, 3]}

df = pd.DataFrame(data)

series = pd.Series(["mango", 2008, 7], index=["fruits", "year", "time"])

​

df = df.append(series, ignore_index=True)

print(df)

       fruits  year  time

0       apple  2001     1

1      orange  2002     4

2      banana  2001     5

3  strawberry  2008     6

4   kiwifruit  2006     3

5       mango  2008     7

import pandas as pd

index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

data1 = [10, 5, 8, 12, 3]

data2 = [30, 25, 12, 10, 8]

data3 = [30, 12, 10, 8, 25, 3]

​

series1 = pd.Series(data1, index=index)

series2 = pd.Series(data2, index=index)

​

df = pd.DataFrame([series1, series2])

​

index.append("pineapple")

​

series3 = pd.Series(data3, index=index)

df = df.append(series3, ignore_index=True)

print(df)

   apple  orange  banana  strawberry  kiwifruit  pineapple

0     10       5       8          12          3        NaN

1     30      25      12          10          8        NaN

2     30      12      10           8         25        3.0

#6-3-4 加入新的欄位

import pandas as pd

data = {"fruits": ["apple", "orange", "banana", "strawberry",

  "kiwifruit"],

  "year": [2001, 2002, 2001, 2008, 2006],

  "time": [1, 4, 5, 6, 3]}

df = pd.DataFrame(data)

df["price"] = [150, 120, 100, 300, 150]

print(df)

       fruits  year  time  price

0       apple  2001     1    150

1      orange  2002     4    120

2      banana  2001     5    100

3  strawberry  2008     6    300

4   kiwifruit  2006     3    150

import pandas as pd

​

index = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

data1 = [10, 5, 8, 12, 3]

data2 = [30, 25, 12, 10, 8]

series1 = pd.Series(data1, index=index)

series2 = pd.Series(data2, index=index)

​

df = pd.DataFrame([series1, series2])

​

new_column = pd.Series([15, 7], index=[0, 1])

​

df["mango"] = new_column

print(df)

   apple  orange  banana  strawberry  kiwifruit  mango

0     10       5       8          12          3     15

1     30      25      12          10          8      7

#6-3-5 取出 DataFrame 當中的元素 –df.loc[]、df.iloc[]

data = {"fruits": ["apple", "orange", "banana", "strawberry",

  "kiwifruit"],

  "year": [2001, 2002, 2001, 2008, 2006],

  "time": [1, 4, 5, 6, 3]}

df = pd.DataFrame(data)

print(df)

       fruits  year  time

0       apple  2001     1

1      orange  2002     4

2      banana  2001     5

3  strawberry  2008     6

4   kiwifruit  2006     3

df = df.loc[[1,2],["time","year"]]

print(df)

   time  year

1     4  2002

2     5  2001

import numpy as np

import pandas as pd

np.random.seed(0)

​

df = pd.DataFrame()

​

columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

for column in columns:

  df[column] = np.random.choice(range(1, 11), 10)

print(df)

​

   apple  orange  banana  strawberry  kiwifruit

0      6       8       6           3         10

1      1       7      10           4         10

2      4       9       9           9          1

3      4       9      10           2          5

4      8       2       5           4          8

5     10       7       4           4          4

6      4       8       1           4          3

7      6       8       4           8          8

8      3       9       6           1          3

9      5       2       1           2          1

df = df.loc[range(2,6),["banana","kiwifruit"]]

print(df)

   banana  kiwifruit

2       9          1

3      10          5

4       5          8

5       4          4

import pandas as pd

data = {"fruits": ["apple", "orange", "banana", "strawberry",

"kiwifruit"],

"time": [1, 4, 5, 6, 3],

"year": [2001, 2002, 2001, 2008, 2006] }

df = pd.DataFrame(data)

print(df)

       fruits  time  year

0       apple     1  2001

1      orange     4  2002

2      banana     5  2001

3  strawberry     6  2008

4   kiwifruit     3  2006

df = df.iloc[[1, 3], [0, 2]]

print(df)

       fruits  year

1      orange  2002

3  strawberry  2008

#6-3-6 刪除 df 物件的列或行 – drop()

import pandas as pd

data = {"fruits": ["apple", "orange", "banana", "strawberry",

"kiwifruit"],

"time": [1, 4, 5, 6, 3] ,

"year": [2001, 2002, 2001, 2008, 2006]}

df = pd.DataFrame(data)

print(df)

       fruits  time  year

0       apple     1  2001

1      orange     4  2002

2      banana     5  2001

3  strawberry     6  2008

4   kiwifruit     3  2006

df_1 = df.drop([0,1])

print(df_1)

       fruits  time  year

2      banana     5  2001

3  strawberry     6  2008

4   kiwifruit     3  2006

df_2 = df.drop("year", axis=1)

print(df_2)

       fruits  time

0       apple     1

1      orange     4

2      banana     5

3  strawberry     6

4   kiwifruit     3

import numpy as np

import pandas as pd

np.random.seed(0)

​

df = pd.DataFrame()

columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

for column in columns:

  df[column] = np.random.choice(range(1, 11), 10)

print(df)

​

   apple  orange  banana  strawberry  kiwifruit

0      6       8       6           3         10

1      1       7      10           4         10

2      4       9       9           9          1

3      4       9      10           2          5

4      8       2       5           4          8

5     10       7       4           4          4

6      4       8       1           4          3

7      6       8       4           8          8

8      3       9       6           1          3

9      5       2       1           2          1

df = df.drop(np.arange(0, 9, 2))

df = df.drop("strawberry", axis=1)

print(df)

   apple  orange  banana  kiwifruit

1      1       7      10         10

3      4       9      10          5

5     10       7       4          4

7      6       8       4          8

9      5       2       1          1

#6-3-7 將欄位值依大小排序 – sort_values()

import pandas as pd

data = {"fruits": ["apple", "orange", "banana", "strawberry",

  "kiwifruit"],

  "time": [1, 4, 3, 6, 3],

  "year": [2001, 2002, 2001, 2008, 2006]}

df = pd.DataFrame(data)

print(df)

       fruits  time  year

0       apple     1  2001

1      orange     4  2002

2      banana     3  2001

3  strawberry     6  2008

4   kiwifruit     3  2006

df = df.sort_values(by="year", ascending = True)

print(df)

       fruits  time  year

0       apple     1  2001

2      banana     3  2001

1      orange     4  2002

4   kiwifruit     3  2006

3  strawberry     6  2008

df = df.sort_values(by=["time", "year"] , ascending = True)

print(df)

       fruits  time  year

0       apple     1  2001

2      banana     3  2001

4   kiwifruit     3  2006

1      orange     4  2002

3  strawberry     6  2008

#6-3-8 從 df 物件篩選出想要的資料

import pandas as pd

data = {"fruits": ["apple", "orange", "banana", "strawberry",

  "kiwifruit"],

  "time": [1, 4, 5, 6, 3] ,

  "year": [2001, 2002, 2001, 2008, 2006] }

df = pd.DataFrame(data)

print(df)

       fruits  time  year

0       apple     1  2001

1      orange     4  2002

2      banana     5  2001

3  strawberry     6  2008

4   kiwifruit     3  2006

print(df.index % 2 == 0)

print(df[df.index % 2 == 0])

​

[ True False  True False  True]

      fruits  time  year

0      apple     1  2001

2     banana     5  2001

4  kiwifruit     3  2006

import numpy as np

import pandas as pd

np.random.seed(0)

df = pd.DataFrame()

columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

for column in columns:

  df[column] = np.random.choice(range(1, 11), 10)

print(df)

   apple  orange  banana  strawberry  kiwifruit

0      6       8       6           3         10

1      1       7      10           4         10

2      4       9       9           9          1

3      4       9      10           2          5

4      8       2       5           4          8

5     10       7       4           4          4

6      4       8       1           4          3

7      6       8       4           8          8

8      3       9       6           1          3

9      5       2       1           2          1

df = df[df["apple"] >= 5]

df = df[df["kiwifruit"] >= 5]

​

# df = df.loc[df["apple"] >= 5][df["kiwifruit"] >= 5]

print(df)

​

   apple  orange  banana  strawberry  kiwifruit

0      6       8       6           3         10

4      8       2       5           4          8

7      6       8       4           8          8




print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


