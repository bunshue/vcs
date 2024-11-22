"""

python_king05_pandas

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
pd.set_option("display.show_dimensions", False)
pd.set_option("display.float_format", "{:4.2g}".format)

#Pandas-方便的資料分析庫

#Pandas中的資料物件
#Series物件

s = pd.Series([1, 2, 3, 4, 5], index=["a", "b", "c", "d", "e"])
print(u"　索引:", s.index)
print(u"值陣列:", s.values)

print(u"位置索引   s[2]:", s[2])
print(u"標簽索引 s['d']:", s['d'])

print(s[1:3])
print(s['b':'d'])

print(s[[1,3,2]])
print(s[['b','d','c']])

#list(s.iteritems())

s2 = pd.Series([20,30,40,50,60], index=["b","c","d","e","f"])

print(s)
print(s2)
print(s+s2)

#DataFrame物件
#DataFrame的各個群組成元素

df_soil = pd.read_csv("data/Soils-simple.csv", index_col=[0, 1], parse_dates=["Date"])
df_soil.columns.name = "Measures"

print(df_soil.dtypes)

print(df_soil.shape)

print(df_soil.columns)
print(df_soil.columns.name)

print(df_soil.index)
print(df_soil.index.names)

print(df_soil["pH"])
print(df_soil[["Dens", "Ca"]])


print(df_soil.loc["0-10", "Top"])
print(df_soil.loc["10-30"])

print(df_soil.values.dtype)

#dtype('O')

#將記憶體中的資料轉為DataFrame物件

df1 = pd.DataFrame(np.random.randint(0, 10, (4, 2)), #❶
                   index=["A", "B", "C", "D"], 
                   columns=["a", "b"])

df2 = pd.DataFrame({"a":[1, 2, 3, 4], "b":[5, 6, 7, 8]},  #❷
                   index=["A", "B", "C", "D"])

arr = np.array([("item1", 1), ("item2", 2), ("item3", 3), ("item4", 4)], 
               dtype=[("name", "10S"), ("count", int)])

df3 = pd.DataFrame(arr) #❸

print(df1)
print(df2)
print(df3)

dict1 = {"a":[1, 2, 3], "b":[4, 5, 6]}
dict2 = {"a":{"A":1, "B":2}, "b":{"A":3, "C":4}}
df1 = pd.DataFrame.from_dict(dict1, orient="index")
df2 = pd.DataFrame.from_dict(dict1, orient="columns")
df3 = pd.DataFrame.from_dict(dict2, orient="index")
df4 = pd.DataFrame.from_dict(dict2, orient="columns")

print(df1)
print(df2)
print(df3)
print(df4)

items = dict1.items()
#df1 = pd.DataFrame.from_items(items, orient="index", columns=["A", "B", "C"])
#df2 = pd.DataFrame.from_items(items, orient="columns")
#print(df1)
#print(df2)

#將DataFrame物件轉為其它格式的資料

print(df2.to_dict(orient="records")) #字典清單
print(df2.to_dict(orient="list")) #清單字典
print(df2.to_dict(orient="dict")) #嵌套字典

[{'a': 1, 'b': 4}, {'a': 2, 'b': 5}, {'a': 3, 'b': 6}]
{'a': [1, 2, 3], 'b': [4, 5, 6]}
{'a': {0: 1, 1: 2, 2: 3}, 'b': {0: 4, 1: 5, 2: 6}}

print(df2.to_records().dtype)
print(df2.to_records(index=False).dtype)

[('index', '<i8'), ('a', '<i8'), ('b', '<i8')]
[('a', '<i8'), ('b', '<i8')]

#Index物件

index = df_soil.columns
index.values

print(index[[1, 3]])
print(index[index > 'c'])
print(index[1::2])

print(index.get_loc('Ca'))
print(index.get_indexer(['Dens', 'Conduc', 'nothing']))

index = pd.Index(["A", "B", "C", "D", "E"], name="level")
s1 = pd.Series([1, 2, 3, 4, 5], index=index)
df1 = pd.DataFrame({"a":[1, 2, 3, 4, 5], "b":[6, 7, 8, 9, 10]}, index=index)
print(s1.index is df1.index)

#True

#MultiIndex物件

mindex = df_soil.index
print(mindex[1])
print(mindex.get_loc(("0-10", "Slope")))
print(mindex.get_indexer([("10-30", "Top"), ("0-10", "Depression"), "nothing"]))

print(mindex.levels[0])
print(mindex.levels[1])

class1 = ["A", "A", "B", "B"]
class2 = ["x", "y", "x", "y"]
pd.MultiIndex.from_arrays([class1, class2], names=["class1", "class2"])

midx = pd.MultiIndex.from_product([["A", "B", "C"], ["x", "y"]], 
                           names=["class1", "class2"])
df1 = pd.DataFrame(np.random.randint(0, 10, (6, 6)), columns=midx, index=midx)

print(df1)


""" #常用的函數參數 NG
print(df_soil.mean())
print(df_soil.mean(axis=1))
print(df_soil.mean(level=1))
"""
#DataFrame的內定結構

df_soil.columns._engine.mapping.get_item("Date")

s = df_soil["Dens"]
s.values.base is df_soil._data.blocks[0].values

#True

print(df_soil[["Dens"]]._data.blocks[0].values.base)

#None

df_float = df_soil[['pH', 'Dens', 'Ca', 'Conduc']]
df_float.values.base is df_float._data.blocks[0].values

#True

df_float.loc["0-10", "Top"].values.base is df_float._data.blocks[0].values

#True

df_soil.values.dtype

#dtype('O')

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pd.set_option("display.show_dimensions", False)
pd.set_option("display.float_format", "{:4.2g}".format)

#索引存取

np.random.seed(42)
df = pd.DataFrame(np.random.randint(0, 10, (5, 3)), 
                  index=["r1", "r2", "r3", "r4", "r5"], 
                  columns=["c1", "c2", "c3"])

"""
[]運算符號

print(df)
print(df[2:4])
print(df["r2":"r4"])

      df              df[2:4]         df["r2":"r4"] 
--------------     --------------     --------------
    c1  c2  c3         c1  c2  c3         c1  c2  c3
r1   6   3   7     r3   2   6   7     r2   4   6   9
r2   4   6   9     r4   4   3   7     r3   2   6   7
r3   2   6   7                        r4   4   3   7
r4   4   3   7                                      
r5   7   2   5                                      

%C 5 df[df.c1 > 4]; df[df > 2]

df[df.c1 > 4]         df[df > 2]   
--------------     ----------------
    c1  c2  c3          c1   c2  c3
r1   6   3   7     r1    6    3   7
r5   7   2   5     r2    4    6   9
                   r3  nan    6   7
                   r4    4    3   7
                   r5    7  nan   5

.loc[]和.iloc[]存取器

%C 5 df.loc["r2"]; df.loc["r2","c2"]

     df.loc["r2"]          df.loc["r2","c2"]
----------------------     -----------------
c1    4                    6                
c2    6                                     
c3    9                                     
Name: r2, dtype: int32                      

%C 5 df.loc[["r2","r3"]]; df.loc[["r2","r3"],["c1","c2"]]

df.loc[["r2","r3"]]     df.loc[["r2","r3"],["c1","c2"]]
-------------------     -------------------------------
    c1  c2  c3              c1  c2                     
r2   4   6   9          r2   4   6                     
r3   2   6   7          r3   2   6                     

%C 5 df.loc["r2":"r4", ["c2","c3"]]; df.loc[df.c1>2, ["c1","c2"]]

df.loc["r2":"r4", ["c2","c3"]]     df.loc[df.c1>2, ["c1","c2"]]
------------------------------     ----------------------------
    c2  c3                             c1  c2                  
r2   6   9                         r1   6   3                  
r3   6   7                         r2   4   6                  
r4   3   7                         r4   4   3                  
                                   r5   7   2                  

%C 5 df.iloc[2]; df.iloc[[2,4]]; df.iloc[[1,3]]; df.iloc[[1,3],[0,2]]

      df.iloc[2]           df.iloc[[2,4]]     df.iloc[[1,3]]     df.iloc[[1,3],[0,2]]
----------------------     --------------     --------------     --------------------
c1    2                        c1  c2  c3         c1  c2  c3         c1  c3          
c2    6                    r3   2   6   7     r2   4   6   9     r2   4   9          
c3    7                    r5   7   2   5     r4   4   3   7     r4   4   7          
Name: r3, dtype: int32                                                               

%C 5 df.iloc[2:4, [0,2]]; df.iloc[df.c1.values>2, [0,1]]

df.iloc[2:4, [0,2]]     df.iloc[df.c1.values>2, [0,1]]
-------------------     ------------------------------
    c1  c3                  c1  c2                    
r3   2   7              r1   6   3                    
r4   4   7              r2   4   6                    
                        r4   4   3                    
                        r5   7   2                    

%C 5 df.ix[2:4, ["c1", "c3"]]; df.ix["r1":"r3", [0, 2]]

df.ix[2:4, ["c1", "c3"]]     df.ix["r1":"r3", [0, 2]]
------------------------     ------------------------
    c1  c3                       c1  c3              
r3   2   7                   r1   6   7              
r4   4   7                   r2   4   9              
                             r3   2   7              

取得單一值

%C 3 df.at["r2", "c2"]; df.iat[1, 1]; df.get_value("r2", "c2")

df.at["r2", "c2"]   df.iat[1, 1]   df.get_value("r2", "c2")
-----------------   ------------   ------------------------
6                   6              6                       

df.lookup(["r2", "r4", "r3"], ["c1", "c2", "c1"])

#多級標簽的存取

soil_df = pd.read_csv("data/Soils-simple.csv", index_col=[0, 1], parse_dates=["Date"])

%C soil_df.loc["10-30", ["pH", "Ca"]]

soil_df.loc["10-30", ["pH", "Ca"]]
----------------------------------
             pH   Ca              
Contour                           
Depression  4.9  7.5              
Slope       5.3  9.5              
Top         4.8   10              

%C soil_df.loc[np.s_[:, "Top"], ["pH", "Ca"]]

soil_df.loc[np.s_[:, "Top"], ["pH", "Ca"]]
------------------------------------------
                pH   Ca                   
Depth Contour                             
0-10  Top      5.3   13                   
10-30 Top      4.8   10                   

query()方法

print(soil_df.query("pH > 5 and Ca < 11"))

                   pH  Dens   Ca  Conduc       Date   Name
Depth Contour                                             
0-10  Depression  5.4  0.98   11     1.5 2015-05-26   Lois
10-30 Slope       5.3   1.3  9.5     4.9 2015-02-06  Diana

pH_low = 5
Ca_hi = 11
print(soil_df.query("pH > @pH_low and Ca < @Ca_hi"))

                   pH  Dens   Ca  Conduc       Date   Name
Depth Contour                                             
0-10  Depression  5.4  0.98   11     1.5 2015-05-26   Lois
10-30 Slope       5.3   1.3  9.5     4.9 2015-02-06  Diana
"""

'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
pd.set_option("display.show_dimensions", False)
pd.set_option("display.float_format", "{:4.2g}".format)

#檔案的輸入輸出
#CSV檔案
"""
    LINK

    http://air.epmap.org/

    空氣質量資料來源：青悅空氣質量歷史資料庫
"""
df_list = []

for df in pd.read_csv(
        u"data/aqi/上海市_201406.csv", 
        encoding="utf-8-sig",  #檔案解碼
        chunksize=100,         #一次讀入的行數
        usecols=[u"時間", u"監測點", "AQI", "PM2.5", "PM10"], #只讀入這些列
        na_values=["-", "—"],  #這些字串表示缺失資料
        parse_dates=[0]):      #第一列為時間列
    df_list.append(df)  #在這裡處理資料

print(df_list[0].count())
print(df_list[0].dtypes)

print(type(df.loc[0, u"監測點"]))

#<type 'unicode'>

"""
HDF5檔案

    LINK

    http://www.nsmc.cma.gov.cn/FENGYUNCast/docs/HDF5.0_chinese.pdf

    中文的HDF5使用簡介
"""

store = pd.HDFStore("a.hdf5", complib="blosc", complevel=9)

df1 = pd.DataFrame(np.random.rand(100000, 4), columns=list("ABCD"))
df2 = pd.DataFrame(np.random.randint(0, 10000, (10000, 3)), 
                   columns=["One", "Two", "Three"])
s1 = pd.Series(np.random.rand(1000))
store["dataframes/df1"] = df1
store["dataframes/df2"] = df2
store["series/s1"] = s1
print(store.keys())
print(df1.equals(store["dataframes/df1"]))

"""
    LINK

    http://pytables.github.io/usersguide/libref/hierarchy_classes.html

    pytables官方文件
"""

root = store.get_node("//")
for node in root._f_walknodes():
    print(node)

store.append('dataframes/df_dynamic1', df1, append=False) #❶
df3 = pd.DataFrame(np.random.rand(100, 4), columns=list("ABCD"))
store.append('dataframes/df_dynamic1', df3) #❷
store['dataframes/df_dynamic1'].shape

print(store.select('dataframes/df_dynamic1', where='index > 97 & index < 102'))

store.append('dataframes/df_dynamic1', df1, append=False, data_columns=["A", "B"])
print(store.select('dataframes/df_dynamic1', where='A > 0.99 & B < 0.01'))

"""
    WARNING

    由於所有從CSV檔案讀入DataFrame物件的行索引都為預設值，因此HDF5檔案中的資料的行索引並不是唯一的。
"""

def read_aqi_files(fn_pattern):
    from glob import glob
    from os import path
    
    UTF8_BOM = b"\xEF\xBB\xBF"
    
    cols = "時間,城市,監測點,質量等級,AQI,PM2.5,PM10,CO,NO2,O3,SO2".split(",")
    float_dtypes = {col:float for col in "AQI,PM2.5,PM10,CO,NO2,O3,SO2".split(",")}
    names_map = {"時間":"Time", 
                 "監測點":"Position", 
                 "質量等級":"Level", 
                 "城市":"City", 
                 "PM2.5":"PM2_5"}
    
    for fn in glob(fn_pattern):
        with open(fn, "rb") as f:
            sig = f.read(3) #❶
            if sig != UTF8_BOM:
                f.seek(0, 0)
            df = pd.read_csv(f, 
                             parse_dates=[0], 
                             na_values=["-", "—"], 
                             usecols=cols, 
                             dtype=float_dtypes) #❷
        df.rename_axis(names_map, axis=1, inplace=True)  
        df.dropna(inplace=True)
        yield df


store = pd.HDFStore("data/aqi/aqi.hdf5", complib="blosc", complevel=9)
string_size = {"City": 12, "Position": 30, "Level":12}

for idx, df in enumerate(read_aqi_files(u"data/aqi/*.csv")):
    store.append('aqi', df, append=idx!=0, min_itemsize=string_size, data_columns=True) #❸
    
store.close()

store = pd.HDFStore("data/aqi/aqi.hdf5")
df_aqi = store.select("aqi")
print(len(df_aqi))

#337250

df_polluted = store.select("aqi", where="PM2_5 > 500")
print(len(df_polluted))

#87

#讀寫資料庫

from sqlalchemy import create_engine

engine = create_engine('sqlite:///data/aqi/aqi.db')

try:
    engine.execute("DROP TABLE aqi")
except:
    pass

str_cols = ["Position", "City", "Level"]

for df in read_aqi_files("data/aqi/*.csv"):
    for col in str_cols:
        df[col] = df[col].str.decode("utf8")
    df.to_sql("aqi", engine, if_exists="append", index=False)

df_aqi = pd.read_sql("aqi", engine)

df_polluted = pd.read_sql("select * from aqi where PM2_5 > 500", engine)
print(len(df_polluted))

#87

#使用Pickle序列化

df_aqi.to_pickle("data/aqi/aqi.pickle")
df_aqi2 = pd.read_pickle("data/aqi/aqi.pickle")
df_aqi.equals(df_aqi2)

#True

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
import pylab as pl
'''
pd.set_option("display.show_dimensions", False)
pd.set_option("display.float_format", "{:4.2g}".format)
df_soil = pd.read_csv("data/Soils-simple.csv", index_col=[0, 1], usecols=range(6))

#數值運算函數

print(df_soil)
print(df_soil.mean())
print(df_soil.mean(axis=1))
#print(df_soil.mean(level=1))

s = pd.Series(dict(Depression=0.9, Slope=1.2))
df_soil.Ca.mul(s, level=1, fill_value=1)

#%fig=中值濾波和搬移平均
t = np.linspace(0, 10, 400)
x = np.sin(0.5*2*np.pi*t)
x[np.random.randint(0, len(t), 40)] += np.random.normal(0, 0.3, 40)
s = pd.Series(x, index=t)
#s_mean = pd.rolling_mean(s, 5, center=True)
#s_median = pd.rolling_median(s, 5, center=True)

ax = s.plot(label=u"噪聲訊號")
#(s_median - 0.2).plot(ax=ax, label=u"中值濾波")
#(s_mean + 0.2).plot(ax=ax, label=u"搬移平均")
ax.legend(loc="best", ncol=3, bbox_to_anchor=(0., 1.02, 1., .102))

plt.show()

print("------------------------------------------------------------")  # 60個

#請讀者思考如何使用NumPy提供的ufunc函數計算ref:fig-next中的三條曲線。

#%fig=用`expanding_*`計算歷史最大值、平均值、最小值
np.random.seed(42)
x = np.cumsum(np.random.randn(400))
""" NG
x_max = pd.expanding_max(x)
x_min = pd.expanding_min(x)
x_mean = pd.expanding_mean(x)

df = pd.DataFrame(np.c_[x, x_max, x_mean, x_min], 
                  columns=["data", "expanding max", "expanding mean", "expanding min"])
ax = df.plot()
"""
ax.legend(ncol=2, loc="upper left")

plt.show()
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
#字串處理

s_abc = pd.Series(["a", "b", "c"])
print(s_abc.str.upper())

"""
s_utf8 = pd.Series([b"北京", b"北京市", b"北京地區"])
s_unicode = s_utf8.str.decode("utf-8")
s_gb2312 = s_unicode.str.encode("gb2312")

print(s_utf8.str.len())
print(s_unicode.str.len())
print(s_gb2312.str.len())

print(s_unicode.str[:2])

print(s_unicode + u"-" + s_abc * 2)

print(s_unicode.str.cat(s_abc, sep="-"))

print(s_unicode.str.len().astype(unicode))
"""
s = pd.Series(["a|bc|de", "x|xyz|yz"])
s_list = s.str.split("|")
s_comma = s_list.str.join(",")
print(s)
print(s_list)
print(s_comma)

s_list.str[1]

print(pd.DataFrame(s_list.tolist(), columns=["A", "B", "C"]))

df_extract1 = s.str.extract(r"(\w+)\|(\w+)\|(\w+)")
df_extract2 = s.str.extract(r"(?P<A>\w+)\|(?P<B>\w+)|")
print(df_extract1)
print(df_extract2)

import io
text = """A, B|C|D
B, E|F
C, A
D, B|C
"""

"""
df = pd.read_csv(io.BytesIO(text), skipinitialspace=True, header=None)
print(df)

nodes = df[1].str.split("|") #❶
from_node = df[0].values.repeat(nodes.str.len().astype(np.int32)) #❷
to_node = np.concatenate(nodes) #❸

print(pd.DataFrame({"from_node":from_node, "to_node":to_node}))

print(df[1].str.get_dummies(sep="|"))

df[1].map(lambda s:max(s.split("|")))

df_soil = pd.read_csv("Soils.csv", usecols=[2, 3, 4, 6])
print(df_soil.dtypes)

for col in ["Contour", "Depth", "Gp"]:
    df_soil[col] = df_soil[col].astype("category")
print(df_soil.dtypes)

Gp = df_soil.Gp
print(Gp.cat.categories)

print(Gp.head(5))
print(Gp.cat.codes.head(5))

depth = df_soil.Depth
print(depth.cat.as_ordered().head())

contour = df_soil.Contour
categories = ["Top", "Slope", "Depression"]
print(contour.cat.reorder_categories(categories, ordered=True).head())
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#時間序列
#時間點、時間段、時間間隔

now = pd.Timestamp.now()
now_shanghai = now.tz_localize("Asia/Shanghai")
now_tokyo = now_shanghai.tz_convert("Asia/Tokyo")
print(u"本機時間:", now)
print(u"上海時區:", now_shanghai)
print(u"東京時區:", now_tokyo)

cc = now_shanghai == now_tokyo
print(cc)

import pytz
print(pytz.common_timezones)

now_day = pd.Period.now(freq="D")
now_hour = pd.Period.now(freq="H")
print(now_day)
print(now_hour)

from pandas.tseries import frequencies

#frequencies._period_code_map.keys()
#frequencies._period_alias_dictionary()

now_week_sun = pd.Period.now(freq="W")
now_week_mon = pd.Period.now(freq="W-MON")
print(now_week_sun)
print(now_week_mon)

print(now_day.start_time)
print(now_day.end_time)

print(now_shanghai.to_period("H"))

#Period('2015-07-25 11:00', 'H')

print(now.year)
print(now.month)
print(now.day)
print(now.dayofweek)
print(now.dayofyear)
print(now.hour)

national_day = pd.Timestamp("2024-9-28")
td = national_day - pd.Timestamp.now()
print(td)

#Timedelta('67 days 12:09:04.039000')

national_day + pd.Timedelta("20 days 10:20:30") 

#Timestamp('2015-10-21 10:20:30')

print(td.days)
print(td.seconds)
print(td.microseconds)

print(pd.Timedelta(days=10, hours=1, minutes=2, seconds=10.5))
print(pd.Timedelta(seconds=100000))

#10 days 01:02:10.500000
#1 days 03:46:40

#時間序列

def random_timestamps(start, end, freq, count):
    index = pd.date_range(start, end, freq=freq)
    locations = np.random.choice(np.arange(len(index)), size=count, replace=False)
    locations.sort()
    return index[locations]

np.random.seed(42)
ts_index = random_timestamps("2015-01-01", "2015-10-01", freq="Min", count=5)
pd_index = ts_index.to_period("M")
td_index = pd.TimedeltaIndex(np.diff(ts_index))

print(ts_index, "\n")
print(pd_index, "\n")
print(td_index, "\n")

print(ts_index.dtype)
print(pd_index.dtype)
print(td_index.dtype)

print(ts_index.weekday)
print(pd_index.month)
print(td_index.seconds)

print(ts_index.shift(1, "H"))

print(ts_index.shift(1, "M"))

print(ts_index.normalize())

print(ts_index.to_period("H").to_timestamp())

ts_series = pd.Series(range(5), index=ts_index)

print(ts_series.between_time("9:00", "18:00"))

print(ts_series.shift(1, freq="D"))

pd_series = pd.Series(range(5), index=pd_index)
td_series = pd.Series(range(4), index=td_index)

print(pd_series.shift(1))
print(td_series.shift(10, freq="H"))

ts_data = pd.Series(ts_index)
pd_data = pd.Series(pd_index)
td_data = pd.Series(td_index)

print(ts_data.dtype)
print(pd_data.dtype)
print(td_data.dtype)

print(ts_data.dt.hour)
print(pd_data.dt.month)
print(td_data.dt.days)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#與NaN關聯的函數

np.random.seed(41)
df_int = pd.DataFrame(np.random.randint(0, 10, (10, 3)), columns=list("ABC"))
df_int["A"] += 10
df_nan = df_int.where(df_int > 2)

print(df_int.dtypes)
print(df_nan.dtypes)

print(df_int)
print(df_nan)

print(df_nan.isnull())
print(df_nan.notnull())

print(df_nan.count())
print(df_nan.count(axis=1))

print(df_nan.dropna())
print(df_nan.dropna(thresh=2))

print(df_nan.ffill())
print(df_nan.bfill())
print(df_nan.interpolate())

s = pd.Series([3, np.NaN, 7], index=[0, 8, 9])
print(s.interpolate())
print(s.interpolate(method="index"))

print(df_nan.fillna({"B":-999, "C":0}))

print(df_nan.sum())
print(df_nan.sum(skipna=False))
print(df_nan.dropna().sum())

df_other = pd.DataFrame(np.random.randint(0, 10, (4, 2)), 
                        columns=["B", "C"], 
                        index=[1, 2, 8, 9])
print(df_nan.combine_first(df_other))
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
pd.set_option("display.show_dimensions", False)
pd.set_option("display.float_format", "{:4.2g}".format)

#改變DataFrame的形狀

soils = pd.read_csv("Soils.csv", index_col=0)[["Depth", "Contour", "Group", "pH", "N"]]
soils_mean = soils.groupby(["Depth", "Contour"]).mean()

print(soils.head())
print(soils_mean.head())

#加入移除列或行

soils["N_percent"] = soils.eval("N * 100")

print(soils.assign(pH2 = soils.pH + 1).head())

def random_dataframe(n):
    columns = ["A", "B", "C"]
    for i in range(n):
        nrow = np.random.randint(10, 20)
        yield pd.DataFrame(np.random.randint(0, 100, size=(nrow, 3)), columns=columns)

df_list = list(random_dataframe(1000))

df_res1 = pd.DataFrame([])
for df in df_list:
    df_res1 = df_res1._append(df)

#Wall time: 1.37 s

df_res2 = pd.concat(df_list, axis=0)

#Wall time: 118 ms

df_res3 = pd.concat(df_list, axis=0, keys=range(len(df_list)))
cc = df_res3.loc[30].equals(df_list[30])
print(cc)

#True

print(soils.drop(["N", "Group"], axis=1).head())

#行索引與列之間相互轉換

print(soils_mean.reset_index(level="Contour").head())

print(soils_mean.set_index("Group", append=True).head())

#行和列的索引相互轉換
print(soils_mean.unstack(1)[["Group", "pH"]].head())
print(soils_mean.stack().head(10))

#交換索引的等級
print(soils_mean.swaplevel(0, 1).sort_index())

df = soils_mean.reset_index()[["Depth", "Contour", "pH", "N"]]
df_pivot_pH = df.pivot(index="Depth", columns="Contour", values="pH")

print(df)
print(df_pivot_pH)

df_before_melt = df_pivot_pH.reset_index()
df_after_melt = pd.melt(df_before_melt, id_vars="Depth", value_name="pH")

print(df_before_melt)
print(df_after_melt)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

pd.set_option("display.show_dimensions", False)
pd.set_option("display.float_format", "{:4.2g}".format)

#分群組運算

dose_df = pd.read_csv("dose.csv")
print(dose_df.head(3))

"""
groupby()方法
    TIP
    groupby()並不立即執行分群組動作，而只是傳回儲存源資料和分群組資料的GroupBy物件。在需要取得每個分群組的實際資料時，GroupBy物件才會執行分群組動作。
"""

tmt_group = dose_df.groupby("Tmt")
print(type(tmt_group))

tmt_age_group = dose_df.groupby(["Tmt", "Age"])

random_values = np.random.randint(0, 5, dose_df.shape[0])
random_group = dose_df.groupby(random_values)

alternating_group = dose_df.groupby(lambda n:n % 3)

crazy_group = dose_df.groupby(["Gender", lambda n: n % 2, random_values])

#GroupBy物件

print(len(tmt_age_group), len(crazy_group))

#10 20

for key, df in tmt_age_group:
    print("key =", key, ", shape =", df.shape)

(_, df_A), (_, df_B), (_, df_C), (_, df_D) = tmt_group

"""
    TIP
    由於GroupBy物件有keys屬性，因此無法透過dict(tmt_group)直接將其轉為字典，可以先將其轉為迭代器，再轉為字典dict(iter(tmt_group))。
"""

print(tmt_group.get_group("A").head(3))
print(tmt_age_group.get_group(("A", "50s")).head(3))

print(tmt_group["Dose"])
print(tmt_group[["Response1", "Response2"]])

print(tmt_group.Dose)

""" NG
#分群組－運算－合並
#agg()－聚合

agg_res1 = tmt_group.agg(np.mean) #❶
agg_res2 = tmt_group.agg(lambda df:df.loc[df.Response1.idxmax()]) #❷
print(agg_res1)
print(agg_res2)
"""

""" NG
#transform()－轉換

transform_res1 = tmt_group.transform(lambda s:s - s.mean()) #❶
transform_res2 = tmt_group.transform(
    lambda df:df.assign(Response1=df.Response1 - df.Response1.mean())) #❷
print(transform_res1.head(5))
print(transform_res2.head(5))
"""

#filter()－過濾

print(tmt_group.filter(lambda df:df.Response1.max() < 11).head())

"""
#apply()－運用
    WARNING
    注意目前的版本采用is判斷索引是否相同，很容易引起混淆，未來的版本可能會對這一點進行修改。
"""

print(tmt_group.apply(pd.DataFrame.max))
#print(tmt_group.apply(pd.DataFrame.mean))

sample_res1 = tmt_group.apply(lambda df:df.Response1.sample(2)) #❶
sample_res2 = tmt_group.apply(
    lambda df:df.Response1.sample(2).reset_index(drop=True)) #❷

print(sample_res1)
print(sample_res2)

group = tmt_group[["Response1", "Response1"]]
apply_res1 = group.apply(lambda df:df - df.mean())
apply_res2 = group.apply(lambda df:(df - df.mean())[:])

print(apply_res1.head())
print(apply_res2.head())

print(tmt_group.apply(lambda df:None if df.Response1.mean() < 5 else df.sample(2)))

# NG print(tmt_group.mean())
# NG print(tmt_group.quantile(q=0.75))
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import pylab as pl

from glob import glob

pl.rcParams['axes.grid'] = True
pd.set_option("display.show_dimensions", False)
pd.set_option("display.float_format", "{:5.3g}".format)

#資料處理和可視化案例
#分析Pandas專案的傳送歷史

def read_git_log(log_fn):
    import io
    with io.open(log_fn, "r", encoding="utf8") as f:
        
        author = datetime = None
        message = []
        message_start = False
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            if line.startswith("commit"):
                if author is not None:
                    yield author, datetime, u"\n".join(message)
                    del message[:]
                message_start = False
            elif line.startswith("Author:"):
                author = line[line.index(":")+1 : line.index("<")].strip()
            elif line.startswith("Date:"):
                datetime = line[line.index(":")+1 :].strip()
                message_start = True
            elif message_start:
                message.append(line)

df_commit = pd.DataFrame(read_git_log("data/pandas.log"), 
                         columns=["Author", "DateString", "Message"])
print(df_commit.shape)

#(12109, 3)

df_commit["Date"] = pd.to_datetime(df_commit.DateString)
print(df_commit[["DateString", "Date"]].head())

df_commit["Timezone"] = df_commit.DateString.str[-5:]

import re
df_commit["Type"] = df_commit.Message.str.extract(r"^([A-Z/]{2,12})", flags=re.MULTILINE)

tz_counts = pd.value_counts(df_commit.Timezone)
type_counts = pd.value_counts(df_commit.Type)

print(tz_counts.head())
print(type_counts.head())

df_commit.set_index("Date", drop=False, inplace=True)
df_commit.sort_index(inplace=True)

#%fig=兩次傳送的時間間隔統計
time_delta = df_commit.Date.diff(1).dropna() #❶
hours_delta = time_delta.dt.days * 24 + time_delta.dt.seconds / 3600.0 #❷
ax = hours_delta.plot(kind="hist", figsize=(8, 3),   #❸
                      bins=100, histtype="step", range=(0, 5), linewidth=2)
ax.set_xlabel("Hours")

plt.show()

print("------------------------------------------------------------")  # 60個
""" NG
#%fig=每個星期的傳送次數
ax = df_commit.Author.resample("W", how="count").plot(kind="area", figsize=(8, 2.5))
ax.grid(True)
ax.set_ylabel(u"傳送次數")

plt.show()
"""
print("------------------------------------------------------------")  # 60個

""" NG
#%fig=每個月的傳送人數
ax = df_commit.Author.resample("M", how=lambda s:len(s.unique())).plot(
    kind="area", figsize=(8, 2.5))
ax.set_ylabel(u"傳送人數")

plt.show()
"""

print("------------------------------------------------------------")  # 60個
"""
    QUESTION

    請讀者思考如何使用groupby()實現與上述resample()相同的運算。
"""
s_authors = df_commit.Author.value_counts()
print(s_authors.head())

""" NG
df_counts = pd.crosstab(df_commit.index.to_period("M"), df_commit.Author)
df_counts.index.name = "Month"
print(df_counts.shape)

#(72, 485)

#%fig=前五名作者的每個月傳送次數
df_counts[s_authors.head(5).index].plot(kind="area", 
                                      subplots=True, 
                                      figsize=(8, 6), 
                                      color=pl.rcParams['axes.color_cycle'][0],
                                      alpha=0.5,
                                      sharex=True,
                                      sharey=True)
plt.show()
"""
print("------------------------------------------------------------")  # 60個

"""
daily_commit = df_commit.index.to_period("D").value_counts() #❶
daily_commit.index = pd.MultiIndex.from_arrays([daily_commit.index.asfreq("W"),  #❷
                                                daily_commit.index.weekday])
daily_commit = daily_commit.sort_index()
active_data = daily_commit.unstack(0).iloc[:, -60:].fillna(0) #❸

#%fig=Pandas專案的活動記錄圖
fig, ax = pl.subplots(figsize=(15, 4))
ax.set_aspect("equal")
ax.pcolormesh(active_data.values, cmap="Greens", 
              vmin=0, vmax=active_data.values.max() * 0.75) #❹

tick_locs = np.arange(3, 60, 10)
ax.set_xticks(tick_locs + 0.5)
ax.set_xticklabels(active_data.columns[tick_locs].to_timestamp(how="start").format())
ax.set_yticks(np.arange(7) + 0.5)

from pandas.tseries.frequencies import DAYS
ax.set_yticklabels(DAYS)

plt.show()
"""
print("------------------------------------------------------------")  # 60個

#分析空氣質量資料
""" NG
store = pd.HDFStore("data/aqi/aqi.hdf5")
df_aqi = store.select("aqi")
cc = df_aqi.head()
print(cc)

print(df_aqi.City.value_counts())

df_aqi["City"] = df_aqi.City.str.replace("市", "").astype("category")
print(df_aqi.City.value_counts())

corr = df_aqi.corr()
print(corr)


fig, ax = pl.subplots()
# remove 

plt.show()
"""
print("------------------------------")  # 30個

"""
#%fig[1x2]=每個城市的日平均PM2.5的分佈圖
daily_city_groupby = df_aqi.groupby([df_aqi.Time.dt.date, "City"]) #❶
mean_pm2_5 = daily_city_groupby.PM2_5.mean().unstack()  #❷
mean_pm2_5.plot(kind="hist", histtype="step", bins=20, normed=True, lw=2) #❸

plt.show()

print("------------------------------")  # 30個

ax = mean_pm2_5.plot(kind="kde")
ax.set_xlim(0, 400)

plt.show()

print("------------------------------")  # 30個

mean_pm2_5.corr()

corr = mean_pm2_5.corr()
corr.index.name = None
corr.columns.name = None
print(corr)

print("------------------------------")  # 30個

#%fig=一星期中PM2.5的平均值
week_mean = df_aqi.groupby([df_aqi.Time.dt.dayofweek, "City"]).PM2_5.mean()
ax = week_mean.unstack().plot(kind="Bar")
ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=3, mode="expand", borderaxespad=0.)
from pandas.tseries.frequencies import DAYS
ax.set_xticklabels(DAYS)

plt.show()

print("------------------------------")  # 30個

#%fig=一天中不同時段的PM2.5的平均值
hour_mean = df_aqi.groupby([df_aqi.Time.dt.hour, "City"]).PM2_5.mean()
ax = hour_mean.unstack().plot(kind="Bar", figsize=(10, 3))
ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=3, borderaxespad=0.)

plt.show()

print("------------------------------")  # 30個

#%fig=北京市各個觀測點的PM2.5的平均值
df_bj = df_aqi.query("City=='北京'")
month_place_mean = df_bj.groupby([df_bj.Time.dt.to_period("M"), "Position"]).PM2_5.mean()
place_mean = month_place_mean.mean(level=1).order()
place_mean.plot(kind="bar")

plt.show()

print("------------------------------")  # 30個

#%fig=北京市各觀測點的月平均PM2.5值
places = place_mean.iloc[[0, 1, -2, -1]].index
month_place_mean.unstack().loc[:, places].plot(kind="bar", figsize=(10, 3), width=0.8)

plt.show()

"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

"""

plt.savefig("test.png", dpi=120)
    TIP
    若果關閉了圖表視窗，則無法使用savefig()儲存圖形。實際上不需要呼叫show()顯示圖表，可以直接用savefig()將圖表儲存成圖形檔案。使用這種方法可以很容易撰寫批次輸出圖表的程式。

print xxxx
print(

b'\n\n\n

plt.show()

print("------------------------------------------------------------")  # 60個

<matplotlib.ticker.NullLocator object at 0x08364F50>

<a list of 2 mcoll.LineCollection objects>


with open(filename, "r", encoding='UTF-8-sig') as f:



"""
