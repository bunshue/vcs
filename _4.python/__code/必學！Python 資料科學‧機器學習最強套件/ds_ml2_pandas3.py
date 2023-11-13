"""

必學！Python 資料科學‧機器學習最強套件 pandas 3

"""

import os
import sys
import time
import random


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


#8-1 載入外部檔案並做資料整理

#8-1-1 使用 Pandas 讀取 CSV 檔

import pandas as pd

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

df = pd.read_csv(url, header=None)

​

​

df.columns = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']

print(df)       

​

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

#8-1-2 將 DataFrame 的內容寫入到 CSV 檔

import pandas as pd

​

data = {'city': ['Nagano', 'Sydney', 'Salt Lake City', 'Athens',

                 'Torino', 'Beijing', 'Vancouver', 'London',

                 'Sochi', 'Rio de Janeiro'],

        'year': [1998, 2000, 2002, 2004, 2006,

                 2008, 2010, 2012, 2014, 2016],

        'season': ['winter', 'summer', 'winter', 'summer', 'winter',

                   'summer', 'winter', 'summer', 'winter', 'summer']}

​

df = pd.DataFrame(data)     

#df.to_csv('C:\\(自行指定存檔路徑)\\olympics.csv')  

​

#8-2 處理 DataFrame 中的缺漏值

#8-2-1 用 dropna() 刪除含有 NaN ( 缺漏值 ) 的列

import numpy as np

from numpy import nan       

import pandas as pd

#   借用 NumPy 的 nan 來設定 NaN 值

​

np.random.seed(0)       

sample_df = pd.DataFrame(np.random.rand(8, 4))      

#   設定亂數種子為 0

#   用 NumPy 隨機產生 8x4 的亂數資料並轉成 DataFrame

​

sample_df.iloc[1, 0] = nan      

sample_df.iloc[2, 2] = nan

sample_df.iloc[6, 1] = nan

sample_df.iloc[5:, 3] = nan

#   將部分值改成 NaN

​

print(sample_df)        

#   檢視 DataFrame

​

          0         1         2         3

0  0.548814  0.715189  0.602763  0.544883

1       NaN  0.645894  0.437587  0.891773

2  0.963663  0.383442       NaN  0.528895

3  0.568045  0.925597  0.071036  0.087129

4  0.020218  0.832620  0.778157  0.870012

5  0.978618  0.799159  0.461479       NaN

6  0.118274       NaN  0.143353       NaN

7  0.521848  0.414662  0.264556       NaN

sample_df_dropped = sample_df.dropna()

print(sample_df_dropped)

​

          0         1         2         3

0  0.548814  0.715189  0.602763  0.544883

3  0.568045  0.925597  0.071036  0.087129

4  0.020218  0.832620  0.778157  0.870012

sample_df_dropped_2 = sample_df[[0, 1, 2]].dropna()

print(sample_df_dropped_2)

​

          0         1         2

0  0.548814  0.715189  0.602763

3  0.568045  0.925597  0.071036

4  0.020218  0.832620  0.778157

5  0.978618  0.799159  0.461479

7  0.521848  0.414662  0.264556

#8-2-2 用 fllna() 填補 NaN 值

import numpy as np

from numpy import nan

import pandas as pd

​

np.random.seed(0)

sample_df = pd.DataFrame(np.random.rand(8, 4))

​

sample_df.iloc[1, 0] = nan

sample_df.iloc[2, 2] = nan

sample_df.iloc[6, 1] = nan

sample_df.iloc[5:, 3] = nan

​

sample_df_fill = sample_df.fillna(0)        # 在 NaN 之處填入 0

print(sample_df_fill)

​

          0         1         2         3

0  0.548814  0.715189  0.602763  0.544883

1  0.000000  0.645894  0.437587  0.891773

2  0.963663  0.383442  0.000000  0.528895

3  0.568045  0.925597  0.071036  0.087129

4  0.020218  0.832620  0.778157  0.870012

5  0.978618  0.799159  0.461479  0.000000

6  0.118274  0.000000  0.143353  0.000000

7  0.521848  0.414662  0.264556  0.000000

sample_df_fill_2 = sample_df.fillna(method='ffill') 

print(sample_df_fill_2)

          0         1         2         3

0  0.548814  0.715189  0.602763  0.544883

1  0.548814  0.645894  0.437587  0.891773

2  0.963663  0.383442  0.437587  0.528895

3  0.568045  0.925597  0.071036  0.087129

4  0.020218  0.832620  0.778157  0.870012

5  0.978618  0.799159  0.461479  0.870012

6  0.118274  0.799159  0.143353  0.870012

7  0.521848  0.414662  0.264556  0.870012

sample_df

, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
	0	1	2	3
0	0.548814	0.715189	0.602763	0.544883
1	NaN	0.645894	0.437587	0.891773
2	0.963663	0.383442	NaN	0.528895
3	0.568045	0.925597	0.071036	0.087129
4	0.020218	0.832620	0.778157	0.870012
5	0.978618	0.799159	0.461479	NaN
6	0.118274	NaN	0.143353	NaN
7	0.521848	0.414662	0.264556	NaN
,

sample_df_fill_3 = sample_df.fillna(sample_df.mean())

print(sample_df_fill_3) 

​

          0         1         2         3

0  0.548814  0.715189  0.602763  0.544883

1  0.531354  0.645894  0.437587  0.891773

2  0.963663  0.383442  0.394133  0.528895

3  0.568045  0.925597  0.071036  0.087129

4  0.020218  0.832620  0.778157  0.870012

5  0.978618  0.799159  0.461479  0.584539

6  0.118274  0.673795  0.143353  0.584539

7  0.521848  0.414662  0.264556  0.584539

#8-3-1 duplicated()、drop_duplicated() - 尋找或刪除 DataFrame 內重複的資料

import pandas as pd

​

dupli_df = pd.DataFrame({'col1':[1, 1, 2, 3, 4, 4, 5, 5],       

                           'col2':['a', 'b', 'b', 'b', 'c', 'c', 'b', 'b']})

print(dupli_df)

​

   col1 col2

0     1    a

1     1    b

2     2    b

3     3    b

4     4    c

5     4    c

6     5    b

7     5    b

dupli_df.duplicated()

0    False
,1    False
,2    False
,3    False
,4    False
,5     True
,6    False
,7     True
,dtype: bool

#8-3-2 map() - 利用 DataFrame 的既有欄位生成新的欄位

import pandas as pd

​

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

​

    ID  birth_year     name city

0  100        1990  Hiroshi   東京

1  101        1989    Akiko   大阪

2  102        1992     Yuki   京都

3  103        1997   Satoru   札幌

4  104        1982   Steeve   東京

5  106        1991   Mituru   東京

6  108        1988      Aoi   大阪

7  110        1990    Tarou   京都

8  111        1995   Suguru   札幌

9  113        1981   Mitsuo   東京

city_map = {'東京': '關東',     

            '札幌': '北海道',

            '大阪': '關西',

            '京都': '關西'}

people_df['city'].map(city_map)

​

0     關東
,1     關西
,2     關西
,3    北海道
,4     關東
,5     關東
,6     關西
,7     關西
,8    北海道
,9     關東
,Name: city, dtype: object

people_df['region'] = people_df['city'].map(city_map)

print(people_df)

​

    ID  birth_year     name city region

0  100        1990  Hiroshi   東京     關東

1  101        1989    Akiko   大阪     關西

2  102        1992     Yuki   京都     關西

3  103        1997   Satoru   札幌    北海道

4  104        1982   Steeve   東京     關東

5  106        1991   Mituru   東京     關東

6  108        1988      Aoi   大阪     關西

7  110        1990    Tarou   京都     關西

8  111        1995   Suguru   札幌    北海道

9  113        1981   Mitsuo   東京     關東

#8-3-3 用 cut() 劃分、篩選資料

import pandas as pd

​

people_data = {'ID': ['100', '101', '102', '103', '104',

                      '106', '108', '110', '111', '113'],

             'name': ['Hiroshi', 'Akiko', 'Yuki', 'Satoru',

                      'Steeve', 'Mituru', 'Aoi', 'Tarou',

                      'Suguru', 'Mitsuo'],

       'birth_year': [1990, 1989, 1992, 1997, 1982,

                      1991, 1988, 1990, 1995, 1981]}

​

people_df = pd.DataFrame(people_data)

print(people_df)

​

    ID     name  birth_year

0  100  Hiroshi        1990

1  101    Akiko        1989

2  102     Yuki        1992

3  103   Satoru        1997

4  104   Steeve        1982

5  106   Mituru        1991

6  108      Aoi        1988

7  110    Tarou        1990

8  111   Suguru        1995

9  113   Mitsuo        1981

birth_year_cut = pd.cut(people_df['birth_year'], 4)

print(birth_year_cut)

​

0      (1989.0, 1993.0]

1      (1985.0, 1989.0]

2      (1989.0, 1993.0]

3      (1993.0, 1997.0]

4    (1980.984, 1985.0]

5      (1989.0, 1993.0]

6      (1985.0, 1989.0]

7      (1989.0, 1993.0]

8      (1993.0, 1997.0]

9    (1980.984, 1985.0]

Name: birth_year, dtype: category

Categories (4, interval[float64]): [(1980.984, 1985.0] < (1985.0, 1989.0] < (1989.0, 1993.0] <

                                    (1993.0, 1997.0]]

print(pd.value_counts(birth_year_cut))

(1989.0, 1993.0]      4

(1993.0, 1997.0]      2

(1985.0, 1989.0]      2

(1980.984, 1985.0]    2

Name: birth_year, dtype: int64

birth_year_bins = [1980, 1985, 1990, 1995, 2000]

birth_year_bins_labels = ['Born in 81~85', 'Born in 86~90', 'Born in 91~95', 'Born in 96~2000']

birth_year_cut = pd.cut(people_df['birth_year'], birth_year_bins, labels=birth_year_bins_labels)

​

print(pd.value_counts(birth_year_cut))

​

Born in 86~90      4

Born in 91~95      3

Born in 81~85      2

Born in 96~2000    1

Name: birth_year, dtype: int64

birth_year_cut

0      Born in 86~90
,1      Born in 86~90
,2      Born in 91~95
,3    Born in 96~2000
,4      Born in 81~85
,5      Born in 91~95
,6      Born in 86~90
,7      Born in 86~90
,8      Born in 91~95
,9      Born in 81~85
,Name: birth_year, dtype: category
,Categories (4, object): ['Born in 81~85' < 'Born in 86~90' < 'Born in 91~95' < 'Born in 96~2000']

people_df['birth_year_bin'] = birth_year_cut

print(people_df)

​

    ID     name  birth_year   birth_year_bin

0  100  Hiroshi        1990    Born in 86~90

1  101    Akiko        1989    Born in 86~90

2  102     Yuki        1992    Born in 91~95

3  103   Satoru        1997  Born in 96~2000

4  104   Steeve        1982    Born in 81~85

5  106   Mituru        1991    Born in 91~95

6  108      Aoi        1988    Born in 86~90

7  110    Tarou        1990    Born in 86~90

8  111   Suguru        1995    Born in 91~95

9  113   Mitsuo        1981    Born in 81~85

#8-4-1 取頭尾列 - head()、tail()

import numpy as np

import pandas as pd

np.random.seed(0)

columns = ["apple", "orange", "banana", "strawberry",

"kiwifruit"]

​

df = pd.DataFrame()

for column in columns:

  df[column] = np.random.choice(range(1, 11), 10)

df.index = [i for i in range(1,11)]

print(df)

    apple  orange  banana  strawberry  kiwifruit

1       6       8       6           3         10

2       1       7      10           4         10

3       4       9       9           9          1

4       4       9      10           2          5

5       8       2       5           4          8

6      10       7       4           4          4

7       4       8       1           4          3

8       6       8       4           8          8

9       3       9       6           1          3

10      5       2       1           2          1

df_head = df.head(3)

df_tail = df.tail()

print('----前 3 列----\n', df_head)

print('----倒數 5 列----\n', df_tail)

----前 3 列----

    apple  orange  banana  strawberry  kiwifruit

1      6       8       6           3         10

2      1       7      10           4         10

3      4       9       9           9          1

----倒數 5 列----

     apple  orange  banana  strawberry  kiwifruit

6      10       7       4           4          4

7       4       8       1           4          3

8       6       8       4           8          8

9       3       9       6           1          3

10      5       2       1           2          1

#8-4-2 對 DataFrame 的值做運算

import numpy as np

import pandas as pd

np.random.seed(0)

​

columns = ["apple", "orange", "banana", "strawberry",

"kiwifruit"]

df = pd.DataFrame()

​

for column in columns:

  df[column] = np.random.choice(range(1, 11), 10)

​

df.index = [i for i in range(1,11)]

print(df)

    apple  orange  banana  strawberry  kiwifruit

1       6       8       6           3         10

2       1       7      10           4         10

3       4       9       9           9          1

4       4       9      10           2          5

5       8       2       5           4          8

6      10       7       4           4          4

7       4       8       1           4          3

8       6       8       4           8          8

9       3       9       6           1          3

10      5       2       1           2          1

double_df = df * 2

square_df = df * df

sqrt_df = np.sqrt(df)

print('----double_df----\n', double_df)

print('----square_df----\n', square_df)

print('----sqrt_df----\n', sqrt_df)

----double_df----

     apple  orange  banana  strawberry  kiwifruit

1      12      16      12           6         20

2       2      14      20           8         20

3       8      18      18          18          2

4       8      18      20           4         10

5      16       4      10           8         16

6      20      14       8           8          8

7       8      16       2           8          6

8      12      16       8          16         16

9       6      18      12           2          6

10     10       4       2           4          2

----square_df----

     apple  orange  banana  strawberry  kiwifruit

1      36      64      36           9        100

2       1      49     100          16        100

3      16      81      81          81          1

4      16      81     100           4         25

5      64       4      25          16         64

6     100      49      16          16         16

7      16      64       1          16          9

8      36      64      16          64         64

9       9      81      36           1          9

10     25       4       1           4          1

----sqrt_df----

        apple    orange    banana  strawberry  kiwifruit

1   2.449490  2.828427  2.449490    1.732051   3.162278

2   1.000000  2.645751  3.162278    2.000000   3.162278

3   2.000000  3.000000  3.000000    3.000000   1.000000

4   2.000000  3.000000  3.162278    1.414214   2.236068

5   2.828427  1.414214  2.236068    2.000000   2.828427

6   3.162278  2.645751  2.000000    2.000000   2.000000

7   2.000000  2.828427  1.000000    2.000000   1.732051

8   2.449490  2.828427  2.000000    2.828427   2.828427

9   1.732051  3.000000  2.449490    1.000000   1.732051

10  2.236068  1.414214  1.000000    1.414214   1.000000

#8-4-3 快速取得 DataFrame 各種統計數據

import numpy as np

import pandas as pd

np.random.seed(0)

​

columns = ["apple", "orange", "banana", "strawberry",

"kiwifruit"]

df = pd.DataFrame()

​

for column in columns:

  df[column] = np.random.choice(range(1, 11), 10)

​

df.index = [i for i in range(1,11)]

print(df)

    apple  orange  banana  strawberry  kiwifruit

1       6       8       6           3         10

2       1       7      10           4         10

3       4       9       9           9          1

4       4       9      10           2          5

5       8       2       5           4          8

6      10       7       4           4          4

7       4       8       1           4          3

8       6       8       4           8          8

9       3       9       6           1          3

10      5       2       1           2          1

print(df.describe())

           apple     orange     banana  strawberry  kiwifruit

count  10.000000  10.000000  10.000000   10.000000  10.000000

mean    5.100000   6.900000   5.600000    4.100000   5.300000

std     2.558211   2.685351   3.306559    2.558211   3.465705

min     1.000000   2.000000   1.000000    1.000000   1.000000

25%     4.000000   7.000000   4.000000    2.250000   3.000000

50%     4.500000   8.000000   5.500000    4.000000   4.500000

75%     6.000000   8.750000   8.250000    4.000000   8.000000

max    10.000000   9.000000  10.000000    9.000000  10.000000

#8-4-4 計算行(列)之間的差 (diﬀ)

import numpy as np

import pandas as pd

np.random.seed(0)

​

columns = ["apple", "orange", "banana", "strawberry",

"kiwifruit"]

df = pd.DataFrame()

​

for column in columns:

  df[column] = np.random.choice(range(1, 11), 10)

​

df.index = [i for i in range(1,11)]

print(df)

    apple  orange  banana  strawberry  kiwifruit

1       6       8       6           3         10

2       1       7      10           4         10

3       4       9       9           9          1

4       4       9      10           2          5

5       8       2       5           4          8

6      10       7       4           4          4

7       4       8       1           4          3

8       6       8       4           8          8

9       3       9       6           1          3

10      5       2       1           2          1

df_diff = df.diff(-2, axis=0)

print(df_diff)

    apple  orange  banana  strawberry  kiwifruit

1     2.0    -1.0    -3.0        -6.0        9.0

2    -3.0    -2.0     0.0         2.0        5.0

3    -4.0     7.0     4.0         5.0       -7.0

4    -6.0     2.0     6.0        -2.0        1.0

5     4.0    -6.0     4.0         0.0        5.0

6     4.0    -1.0     0.0        -4.0       -4.0

7     1.0    -1.0    -5.0         3.0        0.0

8     1.0     6.0     3.0         6.0        7.0

9     NaN     NaN     NaN         NaN        NaN

10    NaN     NaN     NaN         NaN        NaN

#8-4-5 用 groupy() 做分組統計

import pandas as pd

prefecture_df = pd.DataFrame([["Tokyo", 2190, 13636, "Kanto"],

  ["Kanagawa", 2415, 9145, "Kanto"],

  ["Osaka", 1904, 8837, "Kinki"],

  ["Kyoto", 4610, 2605, "Kinki"],

  ["Aichi", 5172, 7505, "Chubu"]],

columns=["Prefecture", "Area",

  "Population", "Region"])

​

print(prefecture_df)

  Prefecture  Area  Population Region

0      Tokyo  2190       13636  Kanto

1   Kanagawa  2415        9145  Kanto

2      Osaka  1904        8837  Kinki

3      Kyoto  4610        2605  Kinki

4      Aichi  5172        7505  Chubu

grouped_region = prefecture_df.groupby("Region")

mean_df = grouped_region.mean()

print(mean_df)

          Area  Population

Region                    

Chubu   5172.0      7505.0

Kanto   2302.5     11390.5

Kinki   3257.0      5721.0




print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


