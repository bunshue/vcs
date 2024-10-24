"""
IntroductiontoPandas

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
'''
import pandas as pd
from pandas import Series, DataFrame

# Series 由一組 索引標籤+數據 組成，就如同Excel中的單一個 column

# Series 由一組 索引標籤+數據 組成

# Series等同是一個 有序 字典####

#建構 Series物件的方式，索引不一定是數字

# 指定索引
s = Series([4, 7, -5, 3], index = ['d', 'b', 'a', 'c'])
s

# 用索引取值
s['b']

# 可以取多個值
s[['b', 'c']]

# 可以使用 陣列式索引
s[s > 3]

# 廣播運算
s * 2

# 用 NumPy的頂級函示對Series做廣播運算
np.exp(s)

# 可以命名 Series物件
s.name = 'test'
s.name

# 可以用Python字典來創建 Series
dt = {'Ohio' : 35000, 'Texas' : 71000, 'Oregon' : 16000, 'Utah' : 5000}
dt

#Series等同是一個有序的字典

s1 = Series(dt)
s1

s1.index

# 建構Series的時候指定 index
# 其中 index California 在 dt中找不到，因此對應的value就標示為 NaN
states = ['Utah', 'California', 'Ohio', 'Oregon', 'Texas']
s2 = Series(dt, index = states)
s2

#pandas的頂級函式都可以對Series物件做廣播運算

# isnull, notnull 可用來檢測 NaN
pd.isnull(s2)


#Series物件也自帶很多ufunc

# Series 的 isnull(), notnull()
s2.isnull()

s2.notnull()

#Series 最重要的功能之一 是能在算術運算中 自動對齊 不同索引的數據####

#依據index自動對齊

s1

s2

s1 + s2

s1 * s2

#可以直接修改index中索引的標籤，資料不會受到影響

# index可以隨時修改，會依照順序對應來修改
s2.index = ['Utah', 'New York', 'Ohio', 'Oregon', 'Texas']
s2

print("------------------------------------------------------------")  # 60個
"""
DataFrame

DataFrame 是一個表格型的數據結構，有一組有序的列，每列可以是不同的資料類型。

DataFrame 既有列索引，也有行索引，
DataFrame可以被視為由一個或多個Series所組成的字典，等同是Excel的工作表####

可以由等長的列表或字典 建構 DataFrame，字典頂層的每個item代表一個Series，也就是Excel工作表中的一個 column

由字典建立DataFrame的時候 columns 會自動以字母排序，除非顯式的以 columns參數指定
"""

# 由等長的列表或字典 建構 DataFrame
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 
        'year': [2000, 2001, 2002, 2001, 2002], 
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
frame

#以字典建立DataFrame的時候，可以用columns參數指定 columns名稱與排序

# 可以指定columns的排序
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 
        'year': [2000, 2001, 2002, 2001, 2002], 
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data, columns = ['state', 'year', 'pop'])
frame

# 找不到的column以NaN表示
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 
        'year': [2000, 2001, 2002, 2001, 2002], 
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data,
                  columns = ['state', 'year', 'pop', 'debt'],
                  index = ['one', 'two', 'three', 'four', 'five']
                 )
frame


# DataFrame的 columns 索引，也是一個 Index物件
frame.columns

#DataFrame的一個 column 就是一個 Series物件，可以用 column索引來取出，每個column也是DataFrame的一個屬性

# 將DataFrame的一個column取出成為一個Series
s = frame['state']
s

# s 有 name屬性
s.name

# 和 frame.state是一樣的，是一個Series
frame.state

frame.year

#由上可知，DataFrame可以被視為由一個或多個Series所組成的字典，字典的key是各個column索引的名稱####
#column索引 和 row索引，可以用'[]'或者'.'交互參照

# row 也可以透過索引取得，返回的是一個視圖，和原本的物件共用資料
frame.state.two

frame['state'].two

frame.state['two']

frame['state']['two']

#對整個Series(column)賦值####
#是一種廣播

# 對整個Series賦值
frame.debt = 16.5
frame

# 長度相同的情況下，會做 mapping
frame.debt = np.arange(5.)
frame

#如果將Series填入DataFrame，會依據index自動對齊

# 使用Series並指定index，並將之填入一個DataFrame, 則DataFrame中空缺的位置都會被填上NaN
s = Series([-1.2, -1.5, -1.7], index = ['two', 'four', 'five'])
frame.debt = s
frame

# 為不存在的column賦值會產生一個新的column
frame['eastern'] = (frame.state == 'Ohio')
frame

frame['eastern']

#如果有指定column索引名稱，則該column的名稱就是其索引的名稱
#如同Excel的欄位名稱

frame['eastern'].name

#可以以雙層的字典，一次性的建立DataFrame

# 以嵌套的字典建立DataFrame，外層的字典作為columns，內層的字典作為rows
pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
pop

frame = DataFrame(pop)
frame

# 也可以進行轉置
frame.T

#如果使用雙層字典來建立DataFrame，且指定的 row Index中沒有對準字典中的內層key，則以指定的row Index為準，沒對到的會被標示為NaN

# 內層的鍵會被合併、排序，但如果顯示地指定了索引，則不會合併或排序
DataFrame(pop, index = [2001, 2002, 2003])

# 可以設置 rows, columns 的名稱
frame.index.name = 'year'
frame.columns.name = 'state'
frame

# DataFrame 的 values屬性 返回一個二維 np.ndarray
v = frame.values
v

#索引(Index)物件
#建構Series或者DataFrame的時候，所用到的任何數組或其他序列的標籤都會被轉換為一個 Index物件####

obj = Series(range(3), name = 'd', index = ['a', 'b', 'c'])
obj

index = obj.index
index # 是一個 Index物件

#Index(['a', 'b', 'c'], dtype='object')

index[1:]

#Index(['b', 'c'], dtype='object')

# Index物件是 immutable，不可以修改
# index[1] = 'b' # 會出錯

# 建立一個Index物件
index = pd.Index(np.arange(3))
index

#Int64Index([0, 1, 2], dtype='int64')

# 置換 Series物件的 index
obj.index = index
obj

# 用Index物件來指定Series的index
obj2 = Series([1.5, -2.5, 0], index = index)
obj2

obj2.index is index

#True

# Index 就像一個大小固定的 Set
frame

'Nevada' in frame.columns

#True

2002 in frame.index

#True

#重新索引###

obj = Series([4.5, 7.2, -5.3, 3.6], index = ['d', 'b', 'a', 'c'])
obj

#reindex()用來移動row或者column的排列

# reindex方法會根據新索引重新排序資料
obj.reindex(['a', 'b', 'c', 'd', 'e'])

# 可以指定 空缺資料的填充值 fill_value
obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value = 0)

obj = Series(['blue', 'purple', 'yellow'], index = [0, 2, 4])
obj

#reindex()會依照指定的方式重新排列rows或者columns，可以指定若遇空缺時，插入rows或者columns的方式

# method參數可以以 "method" 指定 插值 的函式
obj.reindex(range(6), method = 'ffill')

# 如果只傳入一個序列，則 .reindex()會優先對 row重新索引
frame = DataFrame(np.arange(9).reshape((3, 3)),
                  index = ['a', 'c', 'd'], 
                  columns = ['Ohio', 'Texas', 'California'])
frame

frame.reindex(['a', 'b', 'c', 'd'])

#使用reindex()，最好指定是針對row或者column

# 可以以 columns參數重新索引columns
frame.reindex(columns = ['Texas', 'Ohio', 'California'])

# 可以以 對 rows, columns都重新索引
frame.reindex(index = ['a', 'b', 'c', 'd'], 
              columns = ['Texas', 'Ohio', 'California'])

"""
# 插值
frame.reindex(index = ['a', 'b', 'c', 'd'], 
              columns = ['Texas', 'Ohio', 'California'], 
              method = 'ffill')

#.ix[ ] 的索引方式很方便，只需傳入rows, columns 方向的索引列表

# 用 ix函式來重新索引
frame.ix[['a', 'b', 'c', 'd'],
         ['Texas', 'Ohio', 'California']]

#丟棄(drop)指定軸上的項###
"""
# 以一個索引數組指定要刪除的元素
obj = Series(np.arange(5.), index = ['a', 'b', 'c', 'd', 'e'])
obj

new_obj = obj.drop(['c'])
new_obj

new_obj = obj.drop(['c', 'd'])
new_obj

# 對於 DataFrame，可以刪除任意軸上的索引值
data = DataFrame(np.arange(16).reshape((4, 4)),
                 index = ['Ohio', 'Colorado', 'Utah', 'New York'], 
                 columns = ['one', 'two', 'three', 'four'])
data

# 對於 DataFrame，可以刪除任意軸上的索引值
data.drop(['Colorado', 'Ohio'])

# axis = 0 或省略，可以刪除rows
data.drop(['Colorado', 'Ohio'])

# axis = 1，可以刪除columns
data.drop(['two', 'four'], axis = 1)

#索引、選取、過濾###

# Series的索引值不只是整數
obj = Series(np.arange(4.), index = ['a', 'b', 'c', 'd'])
obj

# 單一值，不顯示索引
obj['b']

# 單一值，不顯示索引
#obj[1]

# 多個值，顯示索引
obj[2:4]

# 多個值，顯示索引，依照指定的順序
obj[['b', 'a', 'd']]

# 多個值，顯示索引，依照指定的順序
#obj[[1, 2, 3]]

# 多個值，顯示索引
obj[obj < 2]

# Series, DataFrame的切片算，其末端是包含的
obj['b':'d']

# 賦值的方式也很簡單
obj['b':'c'] = 5
obj

# 對於 DataFrame 索引，其實就是獲取一個或多個列
data = DataFrame(np.arange(16).reshape((4, 4)),
                 index = ['Ohio', 'Colorado', 'Utah', 'New York'], 
                 columns = ['one', 'two', 'three', 'four'])
data

data[['two', 'four']]

data[['four', 'two']]

#data[[1, 3]]

# 這是row方向的切片
data[:2]

# 多層次的索引
data[data['three'] > 5]

# 透過 boolean型態的 DataFrame 進行索引
data

# 透過 boolean型態的 DataFrame 進行索引
data < 5

data[data < 5]

"""
#ix 是重新索引的簡單方法####

# ix 是重新索引的簡單方法
data.ix['Colorado', ['two', 'four']]

# ix 對兩軸重新索引，依照指定的順序
data.ix[['Colorado', 'Utah'], [3, 0, 1]]

# ix 索引，取出第0軸的第2個Series
data.ix[2]

data.ix[: 'Utah', 'two']

data.three > 5

# 對兩個軸索引，取出交集
data.ix[data.three > 5, :3]
"""
print("------------------------------------------------------------")  # 60個

#算數運算和數據對齊###

#pandas最重要的一個功能是: 可以對不同所引的對象進行算術運算。

#在將對象相加時，若存在不同的索引，則結果的索引就是該索引對的聯集。

s1 = Series([7.3, -2.5, 3.4, 1.5], index = ['a', 'c', 'd', 'e'])
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index = ['a', 'c', 'e', 'f', 'g'])

s1
s2

# 兩個Series的索引會自動對齊，空缺的值填入NaN
s1 + s2

# 對於 DataFrame，索引自動對齊會發生在row 和 column方向
df1 = DataFrame(np.arange(9.).reshape((3, 3)),
                index = ['Ohio', 'Texas', 'Colorado'], 
                columns = list('bcd'))
df2 = DataFrame(np.arange(12.).reshape((4, 3)),
                index = ['Utah', 'Ohio', 'Texas', 'Oregon'], 
                columns = list('bde'))

df1
df2

df1 + df2

print("------------------------------------------------------------")  # 60個

#在算術方法中填充值###

df1 = DataFrame(np.arange(12.).reshape((3, 4)),
                columns = list('abcd'))
df2 = DataFrame(np.arange(20.).reshape((4, 5)),
                columns = list('abcde'))

df1
df2

# 以指定的預設值取代 NaN作為自動填充值
# 但是兩個DataFrame都沒有的元素位置，還是會被填入NaN
df1.add(df2, fill_value = 0)

# 重新索引的時候，也可以指定填充值
df1.reindex(columns = df2.columns, fill_value = 0)

#DataFrame 和 Series中間的運算###

arr = np.arange(12.).reshape((3, 4))
arr

arr[0]

# 算術運算 會進行 廣播
arr - arr[0]

# DataFrame 和 Series 之間也是如此
df = DataFrame(np.arange(12.).reshape((4, 3)),
               columns = list("bde"), 
               index = ['Utah', 'Ohio', 'Texas', 'Oregon'])
df

"""
s = df.ix[0]
s
"""

# 也是進行廣播
# 會將Series的索引批被盜DataFrame的columns, 然後沿著rows(軸0)的方向一直向下廣播
df + s

# 如果索引不同，則索引會聯集之後自動對齊
df

s2 = df['d']
s2

# 如果希望索引自動匹配且在row方向上廣播，則必須用算術運算方法
# 傳入的軸就是希望匹配的軸
df.add(s2, axis = 0)

#函數應用和映射

#NumPy的 ufuncs (元素級數組方法) 也可用於操作pandas物件

frame = DataFrame(np.random.randn(4, 3),
                  columns = list('bde'),
                  index = ['Utah', 'Ohio', 'Texas', 'Oregon'])
frame

# NumPy的 ufuncs (元素級數組方法) 也可用於操作pandas物件
np.abs(frame)

# DataFrame 上的 apply方法，可以實現元素級的運算
f = lambda x: x.max() - x.min()
frame.apply(f) # 預設會對每個 column操作


# 沿著軸1
frame.apply(f, axis = 1)

frame

# 返回 由多個值組成的Series
def f(x):
    return Series([x.min(), x.max()], index = ['min', 'max'])
frame.apply(f) # 會對每個column操作 f，每個column傳回一個Series，再重新組合成DataFrame


# DataFrame 也可以透過 applymap(), 使用Python元素級的函式
f = lambda x: "{0:.3f}".format(x)
frame.applymap(f)

# Series 也可以透過 map(), 使用Python元素級的函式
f = lambda x: "{0:.3f}".format(x)
f2 = frame['b']
f2.map(f)


#排序和排名###
#排序####

# 可以使用 sort_index方法 來對軸索引排序
obj = Series(range(4), index = list('dabc'))
obj

# 可以使用 sort_index方法 來對軸索引排序
# 是針對索引來排序，而不是針對資料值
obj.sort_index()

# DataFrame 也可以使用 sort_index 並指定軸來排序索引
frame = DataFrame(np.arange(8).reshape((2, 4)),
                  index = ['three', 'one'],
                  columns = list('dabc')
                 )
frame

frame.sort_index(axis = 0)

frame.sort_index(axis = 1)

# 可以串接
frame.sort_index(axis = 0).sort_index(axis = 1)

# 可以指定 降幕 排序
frame.sort_index(axis = 1, ascending = False)

# 若要以值來排序，可以使用 sort_values()方法
obj['b'] = 4
print(obj)
obj.sort_values()

# 若以sort_values()方法排序，空缺的值會被排到最後面
obj['a'] = None
print(obj)
obj.sort_values()

# 要根據一個或多個column中的值來排序，可以使用 sort_values()
frame = DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
frame

# 使用 sort_values() 根據值來排序
frame.sort_values('b')

# 使用 sort_values() 根據多個columns的值來排序
frame.sort_values(['a', 'b'])

print("------------------------------------------------------------")  # 60個

#彙總和計算描述統計

df = DataFrame([[1.4, np.nan], [7.1, -4.5], 
               [np.nan, np.nan], [0.75, -1.3]], 
               index = list('abcd'), 
               columns = ['one', 'two'])
df

# sum()傳回一個Series
df.sum()

# 指定軸向做 sum()
df.sum(axis = 1)

# NaN會被自動排除(當作0)，可以使用skipna參數改變
df.sum(axis = 1, skipna = False)

# idxmin, idxmax 傳回間接統計，最大值或最小值的索引
df.idxmin()

df.idxmax()

# 累積加總 cumsum()
df.cumsum()

# describe 可以一次性產生多種統計數字
df.describe()

# describe 對非數字資料，產生另外一種統計數字
obj = Series(list('aabc') * 4)
obj

obj.describe()

print("------------------------------------------------------------")  # 60個
"""
#相關係數與協方差##

# 透過 參數對 計算出來的 彙總統計(如 相關係數和協方差)
#import pandas.io.data as web
from pandas_datareader import data, wb

all_data = {}

for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2013', '1/1/2015')
    
price = DataFrame({tic: data['Adj Close'] for tic, data in all_data.items()})
volume = DataFrame({tic: data['Volume'] for tic, data in all_data.items()})

# 百分比變化
returns = price.pct_change()
returns.tail()

# corr() 用來計算相關係數
returns.MSFT.corr(returns.IBM)

0.26199996452035351

# cov()用來計算協方差
returns.MSFT.cov(returns.IBM)

4.0951215814169915e-05

# DataFrame的 corr(), cov() 將會返回相同形狀的矩陣
returns.corr()

returns.cov()

# 利用DataFrame的 corrwith()方法，可以計算列或行 跟另外一個Series或DataFrame之間的相關係數
returns.corrwith(returns.IBM)

returns.corrwith(volume)
"""
print("------------------------------------------------------------")  # 60個

#唯一值、值計數與成員資格

obj = Series(list('cadaabbcc'))
obj

# uniquie 唯一值
obj.unique()

# 排序之後的唯一值
np.sort(obj.unique())

# value_count()傳回 各值出現的次數，依照出現的次數降幕排序
obj.value_counts()

# value_counts()可以做為頂層函式，依照出現的次數降幕排序
pd.value_counts(obj)

# 可以使用 sort 參數 禁止排序
pd.value_counts(obj, sort = False)

# 用 isin() 判斷成員資格
mask = obj.isin(['b', 'c'])
mask

#處理缺失數據(missing data)

# 以NaN標示缺失數據
s = Series(['aardradf', 'asdfasfas', np.nan, 'asdfasfasf'])
s

# 用 isnull()來檢驗NaN
s.isnull()

# None等同於 NaN
s[0] = None
s.isnull()

#濾除缺失數據

from numpy import nan as NA
data = Series([1, NA, 3.5, NA, 7])
data

# 用 dropna()捨棄 NA，index 並不會重新設定
data.dropna()

# 也可透過 boolean型索引過濾
data[data.notnull()]

# 對 DataFrame來說，dropna()預設捨棄任何有NA的row
df = DataFrame([[1., 6.5, 3.], [1., NA, NA], [NA, NA, NA],[NA, 6.5, 3.]])
df

# dropna()預設捨棄任何有NA的row
df.dropna()

# 若傳入 how='all'，則只捨棄 所有數值皆為NA的那個row
df.dropna(how='all')

# 要用這種方式捨棄column，則需傳入 axis=1即可
df[3] = NA
df

# 傳入 axis=1，捨棄整列為NA的column
df.dropna(axis = 1, how = 'all')

# 使用 thresh 參數，只留下一部分觀測數據
df = DataFrame(np.random.randn(7, 3))
df

"""
df.ix[:4, 1] = NA
df.ix[:2, 2] = NA
df
"""

# 用 thresh 參數
df.dropna(thresh = 3)

#填充缺失數據

# 使用 fillna()來填充缺失數據
df.fillna(0)

# 依據字典，對不同的column填充不同的值
df.fillna({1: 0.5, 2: -1})

# fillna()預設傳回副本，但也可以用 inplace 參數來就地修改
df.fillna(0, inplace = True)
df

"""
# 差值的方法 ffill, bfill
df = DataFrame(np.random.randn(6, 3))
df.ix[2:, 1] = NA
df.ix[4:, 2] = NA
df
"""

# 'ffill'的插值方式
df.fillna(method = 'ffill')

# 限制插值的次數
df.fillna(method = 'ffill', limit = 2)

# 用 mean 作為插入值
df.fillna(df.mean())

#層次化索引(hierachical indexing)

# 使用 MultiIndex 索引的Series的格式化輸出形式
# 可以用一維的方式來表達二維的資料，以低維度的形式來處理高維度的資料
s = Series(np.random.randn(10),
           index = [list('aaabbbccdd'),  [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
s
s.index

# 選取數據 子集合
s['b']
s['b':'c']
#s.ix[['b', 'c']]

# 選取 內層 的數據
s[:, 2]

# 數據可以透過 unstack 方法被重新安排到一個 DataFrame中
s.unstack()

# unstack 的逆運算是 stack
s.unstack().stack()

# 對於一個 DataFrame，每條軸都可以有分層索引
df = DataFrame(np.arange(12).reshape((4, 3)), 
               index = [['a', 'a', 'b', 'b'], [1, 2, 1, 2]], 
               columns = [['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
df

# 每層的索引都可以有名字
df.index.names = ['key1', 'key2']
df.columns.names = ['state', 'color']
df

# 可以藉由索引來選取列分組
df['Colorado']

# 可以先建構好 MultiIndex 物件，再用來創建 DataFrame物件
mi = pd.MultiIndex.from_arrays([['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']], names = ['state', 'color'])
mi

#重排分級順序###

# 用 swaplevel 互換級別
df.swaplevel('key1', 'key2')

"""
# sortlevel 根據單一個級別中的值對數據進行排序
df.swaplevel('key1', 'key2').sortlevel(0)

df.swaplevel('key1', 'key2').sortlevel(1)
"""
#根據級別彙總統計###

"""
# 設定 level 參數，用來指定對某個索引級別來操作統計函式
df.sum(level = 'key2')
"""

"""
# 對column上的索引級別來操作統計函式
df.sum(axis = 1, level = 'color')
"""

#使用DataFrame的列###

# 將 DataFrame的一個或多個列當作行索引來用，或者希望將行索引變成DataFrame的列
df = DataFrame({'a': range(7), 'b': range(7, 0, -1), 
                'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'], 
                'd': [0, 1, 2, 0, 1, 2, 3]})
df

# set_index() 會將其一個或多個columns轉換為 row索引，並創建一個 DataFrame
df2 = df.set_index(['c', 'd'])
df2

# 預設情況下，這些columns會被移除，但也可以設定 drop參數將之保留下來
df2 = df.set_index(['c', 'd'], drop = False)
df2

# reset_index() 會將 row方向上的多層次索引 移動到 column上
df2 = df.set_index(['c', 'd'])
df2

# reset_index() 會將 row方向上的多層次索引 移動到 column上
df2.reset_index()

print("------------------------------------------------------------")  # 60個
'''


print("------------------------------------------------------------")  # 60個

"""
ETL : Extract-Transform-Load,中文可譯為"抽取-轉換-載入"。
ETL的作用是將來自不同來源的資料抽取出來,經過清理、轉換、整合等處理後,最終將處理好的資料載入到資料倉儲或其他單一的資料存放區中,為進一步的資料分析做準備。

ETL : extract, transform and load
extract, transform and load,
"""

from pandas import Series, DataFrame
import pandas as pd
import re


#合併數據集
#數據庫風格的DataFrame合併

# pandas 的 merge() 方法
df1 = DataFrame({'key': list('bbacaabd'), 
                 'data1': range(8)})
df2 = DataFrame({'key': list('abd'), 
                 'data2': range(3)})

df1
df2

# 用 merge() 方法，預設以共同的column 'key' 來 join 兩個 DataFrame
pd.merge(df1, df2)

# 也可以顯式的指定 要以哪一個欄位來 join
pd.merge(df1, df2, on = 'key')

# 如果兩個物件的列名不同，也可以分別指定
df3 = DataFrame({'lkey': list('bbacaabd'), 
                 'data1': range(8)})
df4 = DataFrame({'rkey': list('abd'), 
                 'data2': range(3)})
df3
df4

# 分別指定各要以哪一個欄位來join
pd.merge(df3, df4, left_on = 'lkey', right_on = 'rkey')
# lkey = 'c' 的項目不會出現，因為 merge()方法預設以 inner join 的模式來merge

# 可以以 how 參數指定 join的模式 (outer 聯集)
pd.merge(df3, df4, left_on = 'lkey', right_on = 'rkey', how = 'outer')

# 可以以 how 參數指定 join的模式 (inner)
pd.merge(df3, df4, left_on = 'lkey', right_on = 'rkey', how = 'inner')

# 可以以 how 參數指定 join的模式 (left)
pd.merge(df3, df4, left_on = 'lkey', right_on = 'rkey', how = 'left')

# 可以以 how 參數指定 join的模式 (right)
pd.merge(df3, df4, left_on = 'lkey', right_on = 'rkey', how = 'right')

# 多對多的合併
df1 = DataFrame({'key': list('bbacab'), 
                'data1': range(6)})
df2 = DataFrame({'key': list('ababd'), 
                'data2': range(5)})
df1
df2

# 因為 df2中 key a, b 都有對應多個值，所以會產生多個對應 rows
pd.merge(df1, df2, on = 'key', how = 'left')

# 因為 df2中 key a, b 都有對應多個值，所以會產生多個對應 rows
pd.merge(df1, df2, on = 'key', how = 'inner')
# inner join 是求交集，所以不會有 NaN的值出現

# 可以根據多個 keys來 join
df1 = DataFrame({'key1': ['foo', 'foo', 'bar'], 
                 'key2': ['one', 'two', 'one'], 
                 'data': [1, 2, 3]})
df2 = DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'], 
                 'key2': ['one', 'one', 'one', 'two'], 
                 'data': [4, 5, 6, 7]})

df1
df2

# 可以根據多個 keys來 join
pd.merge(df1, df2, on = ['key1', 'key2'], how = 'outer')

# 如果列名重複 ('key2')
pd.merge(df1, df2, on = ['key1'], how = 'outer')

# 如果列名重複 ('key2')
# 使用 suffix 參數來指定附加到左右兩個 DataFrame重複列名的名稱上
pd.merge(df1, df2, on = ['key1'], how = 'outer', suffixes = ['_left', '_right'])

# 設定 sort 參數， 依據 keys來排序
pd.merge(df1, df2, on = ['key1', 'key2'], how = 'outer', suffixes = ['_left', '_right'], sort = True)

print("------------------------------------------------------------")  # 60個

#索引上的合併

# 使用DataFrame的索引作為 join的 key
dfl = DataFrame({'key': list('abaabc'), 
                 'value': range(6)})
# dfr 以 ['a', 'b'] 作為索引
dfr = DataFrame({'value': [3.5, 7]}, index = list('ab'))

dfl

# dfr 以 ['a', 'b'] 作為索引
dfr

# 設定 right_index = True，表示 right DataFrame使用索引作為 join 的 key欄位
pd.merge(dfl, dfr, left_on = 'key', right_index = True, how = 'outer', suffixes = ['_left', '_right'], sort = True)

# 階層化索引
dfl = DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 
                 'key2': [2000, 2001, 2002, 2001, 2002], 
                 'data': np.arange(5.)})
dfr = DataFrame(np.arange(12).reshape((6, 2)), 
                columns = ['data1', 'data2'],
                index = [['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
                         [2001, 2000, 2000, 2000, 2001, 2002]])
dfr.index.names = ['state', 'year']
dfl

dfr

# 階層化索引
# 左方指定用來join的 keys:  left_on = ['key1', 'key2']
# 右方指定使用索引來做為 join的 keys: right_index = True
pd.merge(dfl, dfr, left_on = ['key1', 'key2'], right_index = True, how = 'outer', suffixes = ['_left', '_right'], sort = True)

# 同時使用合併雙方的索引
dfl = DataFrame([[1., 2.], [3., 4.], [5., 6.]], 
                index = list('ace'), 
                columns = ['Ohio', 'Nevada'])
dfr = DataFrame([[7., 8.], [9., 10.], [11., 12.], [13., 14]],
                index = list('bcde'), 
                columns = ['Missouri', 'Alabama'])
dfl
dfr

pd.merge(dfl, dfr, left_index = True, right_index = True, how = 'outer', suffixes = ['_left', '_right'], sort = True )

print("------------------------------------------------------------")  # 60個

#軸向連接(concatenation)

# NumPy中有 concatenate()方法
arr = np.arange(12).reshape((3, 4))
arr

# NumPy 的 concatenate()方法
np.concatenate([arr, arr], axis = 1)

# pandas 有 concat()方法
s1 = Series([0, 1], index = ['a', 'b'])
s2 = Series([2, 3, 4], index = ['c', 'd', 'e'])
s3 = Series([5, 6], index = ['f', 'g'])
sc = pd.concat([s1, s2, s3])
sc
type(sc)

# concat()方法預設以 axis = 0 來連接，如果傳入 axis = 1，則會產生一個 DataFrame
sc = pd.concat([s1, s2, s3], axis = 1)
sc

type(sc)

# 傳入 join = 'inner' 可以看到交集
s4 = pd.concat([s1 * 5, s3])
s4
s1

pd.concat([s1, s4], axis = 1)

# 傳入 join = 'inner' 可以看到交集
sc = pd.concat([s1, s4], axis = 1, join = 'inner')
sc

""" NG
# 透過 join_axes 參數，指定要在其他軸上使用的索引
pd.concat([s1, s4], axis = 1, join_axes = [['a', 'c', 'b', 'e']])
"""
s3

# 使用 keys 參數，建立 階層式索引
result = pd.concat([s1, s1, s3], keys = ['one', 'two', 'three'])
result

# 把具有層次化索引的 Series， unstack 成為 DataFrame
result.unstack()

# 沿著 axis = 1 做 concat，keys就會成為 列頭
result = pd.concat([s1, s1, s3], axis = 1, keys = ['one', 'two', 'three'])
result

# 同樣的邏輯對 DataFrame也是一樣的
# 沿著 axis = 1 做 concat，keys就會成為 列頭
df1 = DataFrame(np.arange(6).reshape((3, 2)), 
                index = ['a', 'b', 'c'], 
                columns = ['one', 'two'])
df2 = DataFrame(5 + np.arange(4).reshape((2, 2)), 
                index = ['a', 'c'], 
                columns = ['three', 'four'])
pd.concat([df1, df2], axis = 1, keys = ['level1', 'level2'])

# 傳入一個字典，則字典的鍵就會被當作keys參數的值
# 這種表達方式比較容易讀懂
pd.concat({'level1': df1, 'level2': df2}, axis = 1)

# names 參數，設定層次化所引的名稱
pd.concat({'level1': df1, 'level2': df2}, axis = 1, names = ['upper', 'lower'])

# 和當下分析工作無關的row索引
df1 = DataFrame(np.random.randn(3, 4), columns = list('abcd'))
df2 = DataFrame(np.random.randn(2, 3), columns = list('bda'))
df1
df2

# concat之後，會保留原來的索引
pd.concat([df1, df2])

# ignore_index = True，不保留原本的索引
pd.concat([df1, df2], ignore_index = True)

print("------------------------------------------------------------")  # 60個

#合併重疊數據

# NumPy的 where 函數
a = Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan], 
           index = list('abcdef'))
b = Series(np.arange(len(a)), dtype = np.float64, 
           index = list('abcdef')) 
a
#b[-1] = np.nan
b

# NumPy的 where 函數，是一種向量化的 if-else
np.where(pd.isnull(a), b, a)

b[:-2]

a[2:]

# Series 的 combine_first()方法，也是一樣的功能，且會自動對齊數據
b[:-2].combine_first(a[2:])

# 對於DataFrame，combine_first的功能就像是在對缺失數據 打補釘
df1 = DataFrame({'a': [1., np.nan, 5., np.nan], 
                 'b': [np.nan, 2., np.nan, 5.], 
                 'c': list(range(2, 18, 4))})
df2 = DataFrame({'a': [5., 4., np.nan, 3., 7.], 
                 'b': [np.nan, 3., 4., 6., 8.]})
df1
df2

# 對於 df1中的缺失數據，會嘗試以df2中的對應數據補充
df1.combine_first(df2)

#重塑(reshape)和軸向旋轉(pivot)
#重塑層次化索引

# 主要兩種方法
# stack: 將 column 旋轉為 row
# unstack: 將 row 旋轉為 column

df = DataFrame(np.arange(6).reshape((2, 3)), 
               index = pd.Index(['Ohio', 'Colorado'], name = 'state'), 
               columns = pd.Index(['one', 'two', 'three'], name = 'number'))
df               

# stack: 將 column 旋轉為 row
s = df.stack()
s

# s 是一個 Series 物件 
type(s)

# unstack: 將 row 旋轉為 column
# Series會變成一個 DataFrame
s.unstack()

# 默認情況下，stack, unstack 操作的是最內層
# 可以傳入分層級別的編號或者名噌，以對其他級別操作
s.unstack(0)

s.unstack('state')

# 如果不是所有的級別值都可以在分組中找到的話，則unstack操作可以會產生缺失數據
s1 = Series([0, 1, 2, 3], index = list('abcd'))
s2 = Series([4, 5, 6], index = list('cde'))
data2 = pd.concat([s1, s2], keys = ['one', 'two'])
data2

# unstack操作可以會產生缺失數據
data2.unstack()

# stack 預設會濾除缺失數據，因此 stack/unstack 是可逆的
data2.unstack().stack()

#NG
# 也可以設定 dropna 參數，不要濾除缺失數據
#data2.unstack().stack(dropna = False)

# unstack操作中，旋轉軸的級別將會成為結果中的最低級別
df = DataFrame({'left': s, 'right': s + 5}, 
               columns = pd.Index(['left', 'right'], name = 'side'))
df

# 索引'state'經過unstack之後，成為最內層的 column索引
df.unstack('state')

# NG
#df.unstack('state').unstack('side')
#df

df.unstack('number').unstack('state')

print("------------------------------------------------------------")  # 60個

#將"長格式"旋轉為"寬格式"

# 重新設定 ldata_string，不用依靠檔案載入
ldata_string = """
{"date":{"0":"1959\\/3\\/31","1":"1959\\/3\\/31","2":"1959\\/3\\/31","3":"1959\\/6\\/30","4":"1959\\/6\\/30","5":"1959\\/6\\/30","6":"1959\\/9\\/30","7":"1959\\/9\\/30","8":"1959\\/9\\/30"},"item":{"0":"realgdp","1":"infl","2":"unemp","3":"realgdp","4":"infl","5":"unemp","6":"realgdp","7":"infl","8":"unemp"},"value":{"0":2710.349,"1":0.0,"2":5.8,"3":2712.349,"4":2.0,"5":7.8,"6":2714.349,"7":4.0,"8":9.8}}
"""

import json
df = DataFrame(json.loads(ldata_string))
df
# 長格式 
# 好處: 值的種類可以隨時增加或減少
# 缺點: 操作起來較麻煩，不易閱讀

# pivot()方法 可以將 長格式 轉換為 寬格式
# 總共需要 index, columns, values 三個參數
pivoted = df.pivot(index = 'date', columns = 'item', values = 'value')
pivoted

# 增加一列 value2
df['value2'] = np.random.randn(len(df))
df

# 如果只指定 index, columns，則DataFrame就會具有層次化的columns
pivoted = df.pivot(index = 'date', columns = 'item')
pivoted

pivoted['value'][:3]

# 也可以用 set_index建立層次化的索引，然後再用 unstack建置
df.set_index(['date', 'item'])

df.set_index(['date', 'item']).unstack('item')


print("------------------------------------------------------------")  # 60個

#數據轉換
#移除重複數據

data = DataFrame({'k1': ['one'] * 3 + ['two'] * 4, 
                  'k2': [1, 1, 2, 3, 3, 4, 4,]})
data

# DataFrame 的 duplicated()方法傳回一個 boolean型態的 Series，表示各row是否重複
data.duplicated()


# drop_duplicates()方法 傳回移除重複項目之後的結果
data.drop_duplicates()

data['k3'] = range(7)
data

# drop_duplicates()預設會對所有的columns來判斷是否有重複的 rows
data.duplicated()

# 也可以針對指定的columns來判斷是否有重複的 rows
data.duplicated(['k1'])

# duplicated, drop_duplicates 預設保留第一個出現的值組合
# 設定參數 keep = 'last'，則會改為保留最後一個出現的值組合
data.duplicated(['k1'], keep = 'last')

print("------------------------------------------------------------")  # 60個

#利用函數或映射進行數據轉換

data = DataFrame({'food':['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef', 'Bacon', 'pastrami', 'honey ham', 'nova lox'], 
                  'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
data

meat_to_animal = {'bacon': 'pig', 
                  'pulled pork': 'pig', 
                  'pastrami': 'cow', 
                  'corned beef': 'cow', 
                  'honey ham': 'pig', 
                  'nova lox': 'salmon'}

# Series 的 map()方法，可以將元素map給特定的 字典或函數 來進行轉換
# 需先規整大小寫，也是透過 map 對每個元素做 str.lower的操作
data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
data

# 也可以透過 lambda來做
data['animal'] = data['food'].map(lambda x: meat_to_animal[x.lower()])
data
# 使用 map()是實現元素級清理與轉換的便捷方式

print("------------------------------------------------------------")  # 60個

#替換值

data = Series([1., -999., 2., -999., -1000., 3.,])
data

# 用 replace()方法來置換數值
data.replace(-999, np.nan)

# 一次置換多個值。要被替換的包裝在一個list中
data.replace([-999, -1000], np.nan)

# 對不同值 進行不同的替換
# 要被替換的放在第一個 list, 替換者放在第二個 list，要匹配
data.replace([-999, -1000], [np.nan, 0])

# 替代關係用 dict表達會比較清楚
data.replace({-999: np.nan, -1000: 0})

print("------------------------------------------------------------")  # 60個

#重新命名軸索引
#軸標籤也可以進行轉換，或者就地修改

data = DataFrame(np.arange(12).reshape((3, 4)), 
                 index = pd.Index(['Ohio', 'Colorado', 'New York'], name = 'state'), 
                 columns = pd.Index(['one', 'two', 'three', 'four'], name = 'quarter'))
data

# Index 也有一個 map()方法，可以傳回一個新的 Index物件
data.index = data.index.map(str.upper)
data

# rename()方法會傳回一個數據集的轉換版本，而不是修改原來的數據
# 使用 index, columns 指定的函式 來修改軸標籤
data.rename(index = str.title, columns = str.upper)

# rename 可以結合字典型物件，實現對部分軸標籤的更新
data.rename(index = {'OHIO': 'INDIANA'}, columns = {'three': 'peekaboo'})
data

# 如果希望就地修改原有的數據集，使需要在 rename()方法中設定參數 inplace = True
data.rename(index = {'OHIO': 'INDIANA'}, columns = {'three': 'peekaboo'}, inplace = True)
data

print("------------------------------------------------------------")  # 60個

#檢測和過濾異常值(outlier)

# 常態分布陣列
np.random.seed(12345)
df = DataFrame(np.random.randn(1000, 4))
df.describe()

# 找出某列中，絕對值大於3的數值
col = df[2]
col[np.abs(col) > 3]

# 找出所有 含有絕對值大於3的數值 的row，可以運用 any()
df[(np.abs(df) > 3).any(axis = 1)]

# 將陣列數值限制在 +-3之間
gt3 = (np.abs(df) > 3)
df[gt3] = np.sign(df) * 3
df.describe()

print("------------------------------------------------------------")  # 60個

#字符串操作
#pandas中向量化的字串函數

data = Series({'Dave': 'dave@google.com', 
        'Steve': 'steve@gmail.com',
        'Rob': 'rob@gmail.com', 
        'Wes': np.nan})
data

# 透過 Series 的 str屬性 可以訪問一些字串的方法
data.str.contains('gmail')

# 是一個 StringMethods物件，之下掛了很多字串方法
data.str

# .str 之下也掛有 reqular expression 的一些方法
pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'

# reg 的 findall()方法
data.str.findall(pattern, flags = re.IGNORECASE)

# reg 的 match()方法
matchs = data.str.match(pattern, flags = re.IGNORECASE)
matchs

# 提取匹配結果中 索引為 1 的元素
#matchs.str.get(1) NG

#matchs.str[0] NG

# 對字串進行子串擷取
data.str[:5]

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

#  GroupBy
# Group By: split-apply-combine

from pandas import Series, DataFrame
import pandas as pd

#GroupBy技術

#分組運算是一種 Split-Apply-Combine的過程，類似於MapReduce的模式

df = DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                'key2' : ['one', 'two', 'one', 'two', 'one'],
                'data1' : np.random.randn(5),
                'data2' : np.random.randn(5)}, columns = ['key1', 'key2', 'data1', 'data2'])
df

# 使用 groupby方法
grouped = df.data1.groupby(df.key1)
grouped
# 產生一個 SeriesGroupBy物件

grouped.size()

# 用GroupBy物件的 mean()方法
# mean()方法是一種 聚合運算
grouped.mean()

#分組所依據的鍵，可以是任何長度的數組，且可以有多層

# 也可以建立多層次的分組
grouped = df.data1.groupby([df.key1, df.key2])
grouped.size()

grouped.mean()

grouped.mean().unstack('key1')

# 也可以對多個 columns同時做分組統計運算
# NG
#df.groupby(df.key1).mean()

# 也可以直接以 column索引的名稱來指定分組
df.groupby(['key1', 'key2']).mean()

# GroupBy 的 size()方法，傳回各分組的大小
df.groupby(['key1', 'key2']).size()

print("------------------------------------------------------------")  # 60個

#對分組進行迭代

for name, group in df.groupby('key1'):
    print(name)
    print(group)
# 所以分組的結果，是拆分為多個 DataFrame    

# 依照多重鍵分組，groupby元素元組的第一個元素是 多重鍵的 元組
for name, group in df.groupby(['key1', 'key2']):
    print(name)
    print(group)

#選取一個或一組columns

df

df.groupby('key1')['data1']
# 等同於
df['data1'].groupby(df['key1'])

df.groupby('key1')['data2']
# 等同於
df[['data2']].groupby(df['key1'])

# 有時候只需要對部分的資料列進行聚合
df.groupby(['key1', 'key2'])[['data2']].mean()
# 傳回 DataFrame

df.groupby(['key1', 'key2'])['data2'].mean()
# 傳回 Series

#通過字典或Series進行分組

people = DataFrame(np.random.randn(5, 5),
                   columns=['a', 'b', 'c', 'd', 'e'],
                   index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
# NG
#people.ix[2:3, ['b', 'c']] = np.nan
people

# 已經知道 列的分組關係
mapping = {'a': 'red', 'b': 'red', 'c': 'blue',
           'd': 'blue', 'e': 'red', 'f' : 'orange'}
#只需要將mapping關係的字典傳給 groupby()
grouped_by_column = people.groupby(mapping, axis = 1)
grouped_by_column.sum()

map_series = Series(mapping)
map_series

# 也可以將mapping關係的Series物件傳給 groupby()
grouped_by_column = people.groupby(map_series, axis = 1)
grouped_by_column.sum()

#透過函數進行分組

people

# 被當作分組鍵的函數都會在各個索引值上被調用一次，返回值就被當作分組名稱
people.groupby(len).mean()

# 函數、列表、字典、Series都可以混用，因為最後都會被轉換為數組
key_list = ['one', 'one', 'one', 'two', 'two']
people.groupby([len, key_list]).min()

# 根據索引級別分組
# 要依據層次化索引來分組聚合，只需要透過 level參數即可
columns = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JP', 'JP'],
                                     [1, 3, 5, 1, 3]], names=['cty', 'tenor'])

hier_df = DataFrame(np.random.randn(4, 5), columns=columns)
hier_df

hier_df.groupby(level = 'cty', axis = 1).count()

print("------------------------------------------------------------")  # 60個

#數據聚合 (pandas.core.groupby.DataFrameGroupBy.aggregate() )

# 可以自訂一聚合方法。聚合方法會對每一個分組之後的group操作一次
df

grouped = df.groupby('key1')
for name, group in grouped:
    print(name)
    print(group)

type(grouped)

for name, group in grouped['data1']:
    print(name)
    print(group)

# Series, DataFrame的方法都可以施加在 group上
# quantile 是 Series的方法
grouped = df.groupby('key1')
grouped['data1'].quantile(0.9)

""" NG
# 透過 aggregate()方法，可以使用自訂函式
def peak_to_peak(arr):
    return arr.max() - arr.min()

grouped.aggregate(peak_to_peak)
"""

# 會對每一個 pandas.core.groupby.DataFrameGroupBy(grouped)中的 DataFrame 中的 Series 做一次指定的 aggregate (在這邊是 peak_to_peak()) 運算

# describe 也可以用
grouped.describe()

#grouped.mean() NG
# 會對每一個 pandas.core.groupby.DataFrameGroupBy中的 DataFrame 中的 Series 做一次指定的 aggregate (在這邊是 mean()) 運算

print("------------------------------------------------------------")  # 60個

#面向列的多函數應用

tips = pd.read_csv('../data/tips.csv')
tips['tip_total_ratio'] = tips['tip']  / tips['total_bill'] 
tips[:5]

# 對不同的列使用不同的聚合函數
grouped = tips.groupby(['sex', 'smoker'])
grouped_pct = grouped['tip_total_ratio']
for name, group in grouped_pct:
    print(name)
    print(group.tail(3))

#What is the difference between pandas agg and apply function?

grouped_pct.agg('mean')

grouped_pct.aggregate('mean')

# 傳入一組函數或函數名，得到的DataFrame的列就會以相應的函數命名
# NG grouped_pct.agg(['mean', 'std', peak_to_peak])

# 如果傳入一個由(name, function)的元組列表，則各元組的第一個元素就會被當作DataFrame的 column名稱
# NG grouped_pct.agg([('foo', 'mean'), ('bar', np.std)])

# 對於 DataFrame，還可以定義使用多個函數
functions = ['count', 'mean', 'max']
# NG
#result = grouped['tip_total_ratio', 'total_bill'].agg(functions)
#result
#result['tip_total_ratio']

# 自訂一結果的列名稱
functions = [('Counts', 'count'), ('Mean', 'mean'), ('Max', 'max')]
#result = grouped['tip_total_ratio', 'total_bill'].agg(functions)
#result

# 對於 DataFrame，還可以定義不同列使用不同的函數
# 傳入一個名稱與函數的字典
#functions = {'tip_total_ratio':  np.max, 'total_bill': np.min}
#result = grouped.agg(functions)
#result

""" NG
# 對於 DataFrame，還可以定義不同列使用不同的函數
functions = {'tip_total_ratio': (np.max,  np.min), 
             'size': ['sum', 'min']}
result = grouped.agg(functions)
result
"""

print("------------------------------------------------------------")  # 60個

""" NG
#以 無索引 的形式返回聚合數據

# 透過 as_index = False，分組鍵不要成為索引
tips.groupby(['sex', 'smoker'], as_index = False).mean()

tips.groupby(['sex', 'smoker']).mean()
"""
print("------------------------------------------------------------")  # 60個

#分組級運算和轉換

# 聚合運算 是數據轉換的一種特例
# 為df增加一列 用於存放各索引分組平均值
df

""" NG
# 計算分組mean
k1_means = df.groupby('key1').mean().add_prefix('mean_')
k1_means

# merge
pd.merge(df, k1_means, left_on = 'key1', right_index = True)
"""

# 使用 transform()
people

key = ['one', 'two', 'one', 'two', 'one']
people.groupby(key).mean()

# 使用 transform()，將分組結果又放到各個row中(使用廣播的方式)
people.groupby(key).transform(np.mean)

# 可以套用各種自訂函式
# 距平均化函數
def demean(arr):
    return arr - arr.mean()

demeaned = people.groupby(key).transform(demean)
demeaned

demeaned.groupby(key).transform(np.mean).applymap(lambda x: '{0:.5f}'.format(x))

print("------------------------------------------------------------")  # 60個

#apply: 一般性的 '拆分-應用-合併'

#Difference between map, applymap and apply methods in Pandas
#apply: 對 整個DataFrame(單一group) 實施一次
#applymap: 對 DataFrame 的每個 儲存格 實施一次
#map: 是 Series 的 function，對 Series 的每個 數值 實施一次

# apply 會將資料拆分成多個片段，對各個片段調用函式，最後再組合各個結果
def top(df, n = 5, column = 'tip_total_ratio'):
    return df.sort_values(by = column)[-n:]

tips.tail()

top(tips, n = 6)

# 使用 apply() 來施加 自訂函式
# NG tips.groupby('smoker').apply(top)

# 自訂函式所需要的參數，可以放在後面一起傳入
# NG tips.groupby(['smoker', 'day']).apply(top, n = 1, column = 'total_bill')

result = tips.groupby(['smoker',])['total_bill'].describe()
result

#smoker       

# NG result.unstack('smoker')

#禁止分組鍵 (group_keys = False)

# 設定 group_keys = False，不讓分組鍵成為row索引
tips.groupby('smoker', group_keys = False).apply(top)

tips.groupby('smoker', group_keys = True).apply(top)

print("------------------------------------------------------------")  # 60個

#範例: 分組加權平均數和相關係數

df = DataFrame({'category': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b'],
                'data': np.random.randn(8),
                'weights': np.random.rand(8)})
df

# 計算分組加權平均數
get_wavg = lambda g: np.average(g.data * g.weights)

# 每個分組施以 get_wavg
df.groupby('category').apply(get_wavg)

# Yahoo Finance 
close_px = pd.read_csv('../data/stock_px.csv',
                       parse_dates = True, index_col = 0)
close_px[:6]

# 計算 日收益率 與 SPX之間的年度相關係數組成的DataFrame
rets = close_px.pct_change().dropna()
rets[:6]

# 與 SPX之間的相關係數
spx_corr = lambda g: g.corrwith(g.SPX)

# 以年度區分
by_year = rets.groupby(lambda x: x.year)

# 計算分組與 SPX的 corr
by_year.apply(spx_corr)


# 也可以計算 列與列之間的相關係數
by_year.apply(lambda g: g.AAPL.corr(g.MSFT))

print("------------------------------------------------------------")  # 60個

#透視表(pivot table)和交叉表(cross-tabulation, 或稱 crosstab)

tips = pd.read_csv('../data/tips.csv')
tips['tip_pct'] = tips['tip']  / tips['total_bill'] 
tips[:5]

# DataFrame 本身就有 pivot_table()方法，預設的 aggregate function 是 average
# NG tips.pivot_table(index = ['sex', 'smoker'])

# 只聚合 tip_pct, size，而且想根據day來分組
# margins = True , 添加分項小計
tips.pivot_table(values = ['tip_pct', 'size'], index = ['sex', 'day'], columns = 'smoker', margins = True) 

tips.pivot_table(values = ['tip_pct'], index = ['sex', 'smoker'], columns = 'day', margins = True) 

# 也可傳入指定的 aggregate function (參數 aggfunc)
tips.pivot_table(values = ['tip_pct'], index = ['sex', 'smoker'], columns = 'day', margins = True, aggfunc = len) 

# 如果存在空的組合(NA)，可以指定 fill_value參數，自動填入空缺值
tips.pivot_table(values = ['size'], index = ['time', 'sex', 'smoker'], columns = 'day', margins = True, aggfunc = sum, fill_value = 0) 

print("------------------------------------------------------------")  # 60個

#交叉表(crosstab)
#用於計算 分組頻率 的特殊 透視表(pivot)

data = DataFrame(
                {'Sample': list(range(1, 11)),
                 'Gender': [random.choice(['Female', 'Male']) for i in range(10)],
                 'Handedness': [random.choice(['Right-handed', 'Left-handed']) for i in range(10)]
                }, 
                columns = ['Sample', 'Gender', 'Handedness'])
data

# 用 crosstab() 方法
pd.crosstab(data.Gender, data.Handedness, margins = True)

# crosstab()方法的參數值可以是 數組
pd.crosstab(index = [tips.time, tips.day], columns = tips.smoker, margins = True)

print("------------------------------------------------------------")  # 60個

