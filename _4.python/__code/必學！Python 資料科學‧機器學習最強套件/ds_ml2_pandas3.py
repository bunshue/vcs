"""

必學！Python 資料科學‧機器學習最強套件 pandas 3

"""

import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

#8-1 載入外部檔案並做資料整理
#8-1-1 使用 Pandas 讀取 CSV 檔

"""

抓資料fail

import pandas as pd

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

df = pd.read_csv(url, header = None)

df.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']

print(df)       

     sepal length  sepal width  petal length  petal width           class

0             5.1          3.5           1.4          0.2     Iris-setosa

1             4.9          3.0           1.4          0.2     Iris-setosa

2             4.7          3.2           1.3          0.2     Iris-setosa

3             4.6          3.1           1.5          0.2     Iris-setosa

4             5.0          3.6           1.4          0.2     Iris-setosa

..            ...          ...           ...          ...             ...

145           6.7          3.0           5.2          2.3  Iris-virginica

146           6.3          2.5           5.0          1.9  Iris-virginica

147           6.5          3.0           5.2          2.0  Iris-virginica

148           6.2          3.4           5.4          2.3  Iris-virginica

149           5.9          3.0           5.1          1.8  Iris-virginica



[150 rows x 5 columns]


"""


print('------------------------------------------------------------')	#60個

#8-1-2 將 DataFrame 的內容寫入到 CSV 檔

import pandas as pd

data = {'city': ['Nagano', 'Sydney', 'Salt Lake City', 'Athens',
                 'Torino', 'Beijing', 'Vancouver', 'London',
                 'Sochi', 'Rio de Janeiro'],
        'year': [1998, 2000, 2002, 2004, 2006,
                 2008, 2010, 2012, 2014, 2016],
        'season': ['winter', 'summer', 'winter', 'summer', 'winter',
                   'summer', 'winter', 'summer', 'winter', 'summer']}
df = pd.DataFrame(data)

#df.to_csv('C:\\(自行指定存檔路徑)\\olympics.csv')

print('------------------------------------------------------------')	#60個


#8-2 處理 DataFrame 中的缺漏值
#8-2-1 用 dropna() 刪除含有 NaN ( 缺漏值 ) 的列
import numpy as np
from numpy import nan
import pandas as pd

#   借用 NumPy 的 nan 來設定 NaN 值
np.random.seed(0)       

sample_df = pd.DataFrame(np.random.rand(8, 4))      

#   設定亂數種子為 0

#   用 NumPy 隨機產生 8x4 的亂數資料並轉成 DataFrame

sample_df.iloc[1, 0] = nan      

sample_df.iloc[2, 2] = nan

sample_df.iloc[6, 1] = nan

sample_df.iloc[5:, 3] = nan

#   將部分值改成 NaN

print(sample_df)        

#   檢視 DataFrame

sample_df_dropped = sample_df.dropna()

print(sample_df_dropped)

sample_df_dropped_2 = sample_df[[0, 1, 2]].dropna()

print(sample_df_dropped_2)

print('------------------------------------------------------------')	#60個

#8-2-2 用 fllna() 填補 NaN 值

import numpy as np

from numpy import nan

import pandas as pd

np.random.seed(0)

sample_df = pd.DataFrame(np.random.rand(8, 4))

sample_df.iloc[1, 0] = nan

sample_df.iloc[2, 2] = nan

sample_df.iloc[6, 1] = nan

sample_df.iloc[5:, 3] = nan

sample_df_fill = sample_df.fillna(0)        # 在 NaN 之處填入 0

print(sample_df_fill)

sample_df_fill_2 = sample_df.fillna(method='ffill') 

print(sample_df_fill_2)

print(sample_df)

sample_df_fill_3 = sample_df.fillna(sample_df.mean())

print(sample_df_fill_3) 

print('------------------------------------------------------------')	#60個

#8-3-1 duplicated()、drop_duplicated() - 尋找或刪除 DataFrame 內重複的資料

import pandas as pd

dupli_df = pd.DataFrame({'col1':[1, 1, 2, 3, 4, 4, 5, 5],       
                           'col2':['a', 'b', 'b', 'b', 'c', 'c', 'b', 'b']})

print(dupli_df)

print(dupli_df.duplicated())

print('------------------------------------------------------------')	#60個

#8-3-2 map() - 利用 DataFrame 的既有欄位生成新的欄位

import pandas as pd

people_data = {'ID': ['100', '101', '102', '103', '104',        
                      '106', '108', '110', '111', '113'],
       'birth_year': [1990, 1989, 1992, 1997, 1982,     
                      1991, 1988, 1990, 1995, 1981],
             'name': ['Hiroshi', 'Akiko', 'Yuki', 'Satoru', 
                      'Steeve', 'Mituru', 'Aoi', 'Tarou',
                      'Suguru', 'Mitsuo'],
'city': ['東京', '大阪', '京都', '札幌',            
                      '東京', '東京', '大阪', '京都',
                      '札幌', '東京']}

people_df = pd.DataFrame(people_data)
print(people_df)

city_map = {'東京': '關東',     
            '札幌': '北海道',
            '大阪': '關西',
            '京都': '關西'}

print(people_df['city'].map(city_map))

people_df['region'] = people_df['city'].map(city_map)

print(people_df)

print('------------------------------------------------------------')	#60個

#8-3-3 用 cut() 劃分、篩選資料

import pandas as pd

people_data = {'ID': ['100', '101', '102', '103', '104',
                      '106', '108', '110', '111', '113'],
             'name': ['Hiroshi', 'Akiko', 'Yuki', 'Satoru',
                      'Steeve', 'Mituru', 'Aoi', 'Tarou',
                      'Suguru', 'Mitsuo'],
       'birth_year': [1990, 1989, 1992, 1997, 1982,
                      1991, 1988, 1990, 1995, 1981]}

people_df = pd.DataFrame(people_data)
print(people_df)

birth_year_cut = pd.cut(people_df['birth_year'], 4)

print(birth_year_cut)

print(pd.value_counts(birth_year_cut))

birth_year_bins = [1980, 1985, 1990, 1995, 2000]

birth_year_bins_labels = ['Born in 81~85', 'Born in 86~90', 'Born in 91~95', 'Born in 96~2000']

birth_year_cut = pd.cut(people_df['birth_year'], birth_year_bins, labels=birth_year_bins_labels)

print(pd.value_counts(birth_year_cut))
print(birth_year_cut)

people_df['birth_year_bin'] = birth_year_cut

print(people_df)

print('------------------------------------------------------------')	#60個

#8-4-1 取頭尾列 - head()、tail()

import numpy as np
import pandas as pd

np.random.seed(0)

columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

df = pd.DataFrame()

for column in columns:

  df[column] = np.random.choice(range(1, 11), 10)

df.index = [i for i in range(1,11)]

print(df)

df_head = df.head(3)

df_tail = df.tail()

print('----前 3 列----\n', df_head)

print('----倒數 5 列----\n', df_tail)

print('------------------------------------------------------------')	#60個

#8-4-2 對 DataFrame 的值做運算

import numpy as np

import pandas as pd

np.random.seed(0)

columns = ["apple", "orange", "banana", "strawberry",

"kiwifruit"]

df = pd.DataFrame()

for column in columns:
     df[column] = np.random.choice(range(1, 11), 10)

df.index = [i for i in range(1,11)]

print(df)

double_df = df * 2

square_df = df * df

sqrt_df = np.sqrt(df)

print('----double_df----\n', double_df)

print('----square_df----\n', square_df)

print('----sqrt_df----\n', sqrt_df)

print('------------------------------------------------------------')	#60個

#8-4-3 快速取得 DataFrame 各種統計數據

import numpy as np

import pandas as pd

np.random.seed(0)

columns = ["apple", "orange", "banana", "strawberry",

"kiwifruit"]

df = pd.DataFrame()

for column in columns:

  df[column] = np.random.choice(range(1, 11), 10)

df.index = [i for i in range(1,11)]

print(df)

print(df.describe())

print('------------------------------------------------------------')	#60個

#8-4-4 計算行(列)之間的差 (diﬀ)

import numpy as np

import pandas as pd

np.random.seed(0)

columns = ["apple", "orange", "banana", "strawberry",

"kiwifruit"]

df = pd.DataFrame()

for column in columns:
     df[column] = np.random.choice(range(1, 11), 10)

df.index = [i for i in range(1,11)]

print(df)

df_diff = df.diff(-2, axis=0)

print(df_diff)

print('------------------------------------------------------------')	#60個

#8-4-5 用 groupy() 做分組統計

import pandas as pd

prefecture_df = pd.DataFrame([["Tokyo", 2190, 13636, "Kanto"],
                              ["Kanagawa", 2415, 9145, "Kanto"],
                              ["Osaka", 1904, 8837, "Kinki"],
                              ["Kyoto", 4610, 2605, "Kinki"],
                              ["Aichi", 5172, 7505, "Chubu"]],
                             columns=["Prefecture", "Area", "Population", "Region"])

print(prefecture_df)

grouped_region = prefecture_df.groupby("Region")

mean_df = grouped_region.mean()

print(mean_df)

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


