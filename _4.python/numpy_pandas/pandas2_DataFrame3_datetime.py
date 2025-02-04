"""
pandas 時間相關

Pandas的时间序列处理

pd之時間相關

1. pd.date_range()  # 生成日期範圍
2. pd.to_datetime() # 轉換日期

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("pd.date_range() 生成日期範圍 ST")
print("------------------------------------------------------------")  # 60個

start = "2024/12/18"  # 或 "12/18/2024" 或 "20241218"
end = "2024/12/25"

# 使用start
dates = pd.date_range(start=start, periods=5)
print("從某天開始後的5個日期 :\n", dates, sep="")

# 使用end
dates = pd.date_range(end=end, periods=5)
print("從某天倒數後的5個日期 :\n", dates, sep="")

# 使用freq
dates = pd.date_range(start=start, end=end, freq="1D")
print(dates)

# 使用freq1 預設 1D
dates = pd.date_range(start=start, end=end)
print("從某天到某天 start-end 預設每隔1天:\n", dates, sep="")

# 使用freq2
dates = pd.date_range(start=start, end=end, freq="2D")
print("從某天到某天 start-end 每隔2天:\n", dates, sep="")

# 使用freq3
dates = pd.date_range(start=start, end=end, freq="8h")
print("從某天到某天 start-end 每隔8小時:\n", dates, sep="")

# 使用freq4 MS 月初
dates = pd.date_range(start=start, freq="MS", periods=5)
print("從某天開始後的5個日期 每隔1月 月初:\n", dates, sep="")

# 使用freq4 ME 月底
dates = pd.date_range(start=start, freq="ME", periods=5)
print("從某天開始後的5個日期 每隔1月 月底:\n", dates, sep="")

# 使用freq4 W-SAT
dates = pd.date_range("2024-12-18", periods=5, freq="W-SAT")  # 起始日期  # 周期  # 频率
print("從某天開始後的5個週六 :\n", dates, sep="")

dates = pd.date_range(start="2024/12/18 12:13:14", periods=5)
print("從某天開始後的5個日期 : 日期有時分秒, 無規範化\n", dates, sep="")

dates = pd.date_range(start="2024/12/18 12:13:14", periods=5, normalize=True)
print("從某天開始後的5個日期 : 日期有時分秒, 有規範化\n", dates, sep="")

# 偏移量通过加法连接
sum_offset = pd.tseries.offsets.Week(2) + pd.tseries.offsets.Hour(12)
print("偏移量 :", sum_offset)
dates = pd.date_range("2024/10/18", "2024/12/18", freq=sum_offset)
print("生成日期範圍 start-end 每隔一個偏移量:\n", dates, sep="")

"""
def random_timestamps(start, end, freq, count):
    index = pd.date_range(start, end, freq=freq)
    locations = np.random.choice(np.arange(len(index)), size=count, replace=False)
    locations.sort()
    return index[locations]

ts_index = random_timestamps("2015-01-01", "2015-10-01", freq="Min", count=5)
pd_index = ts_index.to_period("M")
td_index = pd.TimedeltaIndex(np.diff(ts_index))
"""

s = pd.Series(np.random.randn(5), index=dates)
print(type(s))
print(s)

print("------------------------------------------------------------")  # 60個

datas = [
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4],
    [5, 5, 5, 5],
    [6, 6, 6, 6],
]

columns = ["A", "B", "C", "D"]
dates = pd.date_range("20130101", periods=6)
print("從某天開始後的6個日期 :\n", dates, sep="")

df = pd.DataFrame(datas, index=dates, columns=columns)

print(df["A"], df.A)
print(df[0:3], df["20130102":"20130104"])

# select by label: loc
print(df.loc["20130102"])
print(df.loc[:, ["A", "B"]])
print(df.loc["20130102", ["A", "B"]])

""" no ix
# mixed selection: ix
print(df.ix[:3, ["A", "C"]])
# Boolean indexing
print(df[df.A > 0])
"""
print("------------------------------------------------------------")  # 60個

datas = [
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4],
    [5, 5, 5, 5],
    [6, 6, 6, 6],
]

columns = ["A", "B", "C", "D"]
dates = pd.date_range("20130101", periods=6)
print("從某天開始後的6個日期 :\n", dates, sep="")

df = pd.DataFrame(datas, columns=columns, index=dates)
print(df)

print(df.A)  # A欄的資料

df.iloc[2, 2] = 1111
df.loc["2013-01-03", "D"] = 2222
df["F"] = np.nan
df["G"] = pd.Series([1, 2, 3, 4, 5, 6], index=dates)
print(df)

print("------------------------------------------------------------")  # 60個

datas = np.arange(24).reshape((6, 4))
columns = ["A", "B", "C", "D"]
dates = pd.date_range("20130101", periods=6)
print("從某天開始後的6個日期 :\n", dates, sep="")

df = pd.DataFrame(datas, columns=columns, index=dates)

df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df.dropna(axis=0, how="any"))  # how={'any', 'all'}

VALUE = 0
print(df.fillna(value=VALUE))  # 將df內空資料填入指定數值

print("空資料 :")
print(pd.isnull(df))

print("------------------------------------------------------------")  # 60個

dates = pd.date_range("20170109", periods=5, freq="D")
print("從某天開始後的5個日期 每隔1日 :\n", dates, sep="")

df = pd.read_csv("_new/2330.TW.csv")
df["Date"] = dates
print(df)

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("_new/2330.TW.csv")
print(df["Volume"].pct_change())

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("_new/2330.TW.csv")
print(df["Close"].unique())
print(df["Close"].nunique())
print(df["Close"].value_counts())

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

import datetime

# 指定index为datetime的list
date_list = [
    datetime.datetime(2024, 2, 18),
    datetime.datetime(2024, 2, 19),
    datetime.datetime(2024, 2, 25),
    datetime.datetime(2024, 2, 26),
    datetime.datetime(2024, 3, 4),
    datetime.datetime(2024, 3, 5),
]
time_s = pd.Series(np.random.randn(6), index=date_list)
print(time_s)
print(type(time_s.index))

# 索引位置
print(time_s[0])

# 索引值
print(time_s[datetime.datetime(2024, 2, 18)])

# 可以被解析的日期字符串
print(time_s["2024/02/18"])

# 按“年份”、“月份”索引
print(time_s["2024-2"])

# 切片操作
print(time_s["2024-2-26":])

cc = time_s.truncate(before="2024-2-25")
print(cc)

cc = time_s.truncate(after="2024-2-25")
print(cc)

dates = pd.date_range("20240218", periods=5, freq="W-SAT")  # 起始日期  # 周期  # 频率
print("從某天開始後的5個週六 :\n", dates, sep="")

# 移动数据
ts = pd.Series(np.random.randn(5), index=dates)

print(ts)
print(ts.shift(1, freq="2D"))
print(ts.shift(-1))

print("------------------------------------------------------------")  # 60個

# 时间数据重采样 resample

dates = pd.date_range("20240101", periods=100, freq="D")
print("從某天開始後的100個日期 每隔1日 :\n", dates, sep="")

ser_obj = pd.Series(range(len(dates)), index=dates)
print(ser_obj.head(10))

# 统计每个月的数据总和
resample_month_sum = ser_obj.resample("M").sum()
# 统计每个月的数据平均
resample_month_mean = ser_obj.resample("M").mean()

print("按月求和：", resample_month_sum)
print("按月求均值：", resample_month_mean)

# 降采样
# 将数据聚合到5天的频率
five_day_sum_sample = ser_obj.resample("5D").sum()
five_day_mean_sample = ser_obj.resample("5D").mean()
five_day_ohlc_sample = ser_obj.resample("5D").ohlc()

print("降采样，sum")
print(five_day_sum_sample)

print("降采样，mean")
print(five_day_mean_sample)

# 使用groupby降采样
print(ser_obj.groupby(lambda x: x.month).sum())

# NG print(ser_obj.groupby(lambda x: x.weekday).sum())

dates = pd.date_range("20240101", periods=5, freq="W-MON")  # 起始日期  # 周期  # 频率
print("從某天開始後的5個週一 :\n", dates, sep="")

# 升采样
df = pd.DataFrame(
    np.random.randn(5, 3),
    index=dates,
    columns=["S1", "S2", "S3"],
)
print(df)

# 直接重采样会产生空值
print(df.resample("D").asfreq())

# ffill
print(df.resample("D").ffill(2))

print(df.resample("D").bfill())

print(df.resample("D").fillna("ffill"))

print(df.resample("D").interpolate("linear"))

print("------------------------------------------------------------")  # 60個

# 时间序列数据统计—滑动窗口 窗口函数

dates = pd.date_range("20240101", periods=1000)
print("從某天開始後的1000個日期 :\n", dates, sep="")

ser_obj = pd.Series(np.random.randn(1000), index=dates)
ser_obj_c = ser_obj.cumsum()
print(ser_obj.head())

print(ser_obj_c.head())

r_obj = ser_obj.rolling(window=5)
print(r_obj)

print(r_obj.mean())

# 验证：
# 前5个数据的均值
# print(ser_obj[0:5].mean())

# 1-6个数据的均值
# print(ser_obj[1:6].mean())

plt.figure(figsize=(15, 5))

ser_obj.plot(style="r--")
ser_obj.rolling(window=10).mean().plot(style="b")

show()

print(ser_obj.rolling(window=5, center=True).mean())

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("pd.date_range() 生成日期範圍 SP")
print("------------------------------------------------------------")  # 60個

print("pd.to_datetime() 轉換日期")

# 資料 台積電股價 18 X 7
df = pd.read_csv("_new/2330_2019_9.csv")

print("原本7欄, 取出3欄, 再加上index")
print("建立空的df, 再加入資料至df")
df2 = pd.DataFrame()

df2["Date"] = pd.to_datetime(df["Date"])
df2["Adj Close"] = df[
    "Adj Close"
]  # Adj Close (Adjusted Close)是經過調整的收盤價，是遇到股票分割或發放股利時的調整值，可將除權後的數值進行計算，還原其值。
df2["High"] = df["High"]
df2["Low"] = df["Low"]
df2 = df2.set_index("Date")

print(df2)
print(df2.shape)
print("一次畫出3欄資料")
df2.plot(kind="line", title="台積電 2019年 9月")

show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
