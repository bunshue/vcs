"""
pandas 時間相關

Pandas的时间序列处理

pd之時間相關

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
# pd.date_range()  # 生成日期范围 ST
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

df = pd.DataFrame(datas, columns=columns, index=dates)
print(df)

print(df.A)

df.iloc[2, 2] = 1111
df.loc["2013-01-03", "D"] = 2222
df["F"] = np.nan
df["G"] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130101", periods=6))
print(df)

print("------------------------------------------------------------")  # 60個

datas = np.arange(24).reshape((6, 4))
columns = ["A", "B", "C", "D"]
dates = pd.date_range("20130101", periods=6)

df = pd.DataFrame(datas, columns=columns, index=dates)

df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df.dropna(axis=0, how="any"))  # how={'any', 'all'}

VALUE = 0
print(df.fillna(value=VALUE))  # 將df內空資料填入指定數值

print("空資料 :")
print(pd.isnull(df))

print("------------------------------------------------------------")  # 60個

dates_d = pd.date_range("20170109", periods=5, freq="D")
print(dates_d)
df = pd.read_csv("_new/2330.TW.csv")
df["Date"] = dates_d
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

dates = pd.date_range("12/18/2024", periods=5)  # 沒寫就是start
print("從某天開始後的5天 :\n", dates)

dates = pd.date_range("20241218", periods=5)
print("從某天開始後的5天 :\n", dates)

dates = pd.date_range(start="2024/12/18", periods=5)
print("生成日期範圍 start:\n", dates)

dates = pd.date_range(end="2024/12/18", periods=5)
print("生成日期範圍 end:\n", dates)

# 传入开始、结束日期，默认生成的该时间段的时间点是按天计算的
dates = pd.date_range("2024/12/18", "2024/12/25")
print("生成日期範圍 start-end:\n", dates)

dates = pd.date_range("2024-12-18", periods=5, freq="W-SAT")  # 起始日期  # 周期  # 频率
print("從某天開始後的5個週六 :\n", dates)

s = pd.Series(np.random.randn(5), index=dates)
print(type(s))
print(s)

dates = pd.date_range(start="2024/12/18 12:13:14", periods=5)
print("無規範化 生成日期範圍 :\n", dates)

dates = pd.date_range(start="2024/12/18 12:13:14", periods=5, normalize=True)
print("有規範化 生成日期範圍 :\n", dates)

# 频率与偏移量
dates = pd.date_range("2024/11/18", "2024/12/18", freq="2D")
print("生成日期範圍 每隔2天:\n", dates)

# 偏移量通过加法连接
sum_offset = pd.tseries.offsets.Week(2) + pd.tseries.offsets.Hour(12)
print("偏移量 :", sum_offset)
dates = pd.date_range("2024/10/18", "2024/12/18", freq=sum_offset)
print("生成日期範圍 start-end 每隔一個偏移量:\n", dates)

start = "2024/12/18"
end = "2024/12/25"
for d in pd.date_range(start=start, end=end, freq="1D"):
    print(d)

dates = pd.date_range(start="2024-01-15", freq="M", periods=5)
print("生成日期範圍 每隔1月 月底:\n", dates)

dates = pd.date_range(start="2024-01-15", freq="MS", periods=5)
print("生成日期範圍 每隔1月 月初:\n", dates)

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

print("------------------------------------------------------------")  # 60個

yyyymmdd = "20240101"
DAYS = 30
datas = np.random.randn(DAYS, 4)
index = pd.date_range(yyyymmdd, periods=DAYS)
print("從", yyyymmdd, "開始的", DAYS, "天\n", index)
df = pd.DataFrame(datas, index=index, columns=list("ABCD"))
df = df.cumsum()
df.plot(title="線圖")  # 無參數, 預設就是 line

show()

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("_new/2330_2019_9.csv")

print("建立空的df, 再加入資料至df")
data = pd.DataFrame()
data["Date"] = pd.to_datetime(df["Date"])
data["Adj Close"] = df["Adj Close"]
data["High"] = df["High"]
data["Low"] = df["Low"]
data = data.set_index("Date")

data.plot(kind="line")

show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# pd.date_range()  # 生成日期范围 SP
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

from datetime import datetime

# 指定index为datetime的list
date_list = [
    datetime(2024, 2, 18),
    datetime(2024, 2, 19),
    datetime(2024, 2, 25),
    datetime(2024, 2, 26),
    datetime(2024, 3, 4),
    datetime(2024, 3, 5),
]
time_s = pd.Series(np.random.randn(6), index=date_list)
print(time_s)
print(type(time_s.index))

# 索引位置
print(time_s[0])

# 索引值
print(time_s[datetime(2024, 2, 18)])

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

# 移动数据
ts = pd.Series(
    np.random.randn(5), index=pd.date_range("20240218", periods=5, freq="W-SAT")
)
print(ts)
print(ts.shift(1, freq="2D"))
print(ts.shift(-1))

print("------------------------------------------------------------")  # 60個

# 时间数据重采样 resample

date_rng = pd.date_range("20240101", periods=100, freq="D")
ser_obj = pd.Series(range(len(date_rng)), index=date_rng)
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

print(ser_obj.groupby(lambda x: x.weekday).sum())

# 升采样
df = pd.DataFrame(
    np.random.randn(5, 3),
    index=pd.date_range("20240101", periods=5, freq="W-MON"),
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

ser_obj = pd.Series(
    np.random.randn(1000), index=pd.date_range("20240101", periods=1000)
)
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

print("日本各都市平均氣溫全年資料")

filename = "data/weather_sample.csv"
df = pd.read_csv(filename, header=0, parse_dates=["年月"])
# print(df)

df.plot(kind="line", x="年月", y="東京-平均氣溫(℃)", title="東京", figsize=[10, 5])
df.plot(kind="line", x="年月", y="大阪-平均氣溫(℃)", title="大阪", figsize=[10, 5])

show()

print("------------------------------")  # 30個

filename = "data/weather_sample.csv"
df = pd.read_csv(filename, header=0, parse_dates=["年月"], index_col=0)
df_average = df[["東京-平均氣溫(℃)", "大阪-平均氣溫(℃)", "那霸-平均氣溫(℃)", "函館-平均氣溫(℃)"]]
print(df_average)

# 在單一圖表繪製多張折線圖的範例

df_average.plot(kind="line")

# 適度調整標籤與圖例
plt.xticks(rotation=30)
plt.legend()

show()

print("------------------------------")  # 30個

# 將多張折線圖的折線設定為同一種類的範例

tmp_stack = (
    df_average.stack()
    .rename_axis(["年月", "category"])
    .reset_index()
    .rename(columns={0: "value"})
)
print(tmp_stack)

# 繪製折線圖
ax = sns.lineplot(data=tmp_stack, x="年月", y="value", hue="category", palette="pastel")

# 適度調整標籤與圖例
plt.xticks(rotation=30)
plt.legend()

show()

print("------------------------------")  # 30個

# 強調特定折線圖的範例
# sns.set(style="white", font="meiryo")
tmp_stack = (
    df_average.stack()
    .rename_axis(["年月", "category"])
    .reset_index()
    .rename(columns={0: "value"})
)
print(tmp_stack)

# 計算分類數量
num_category = len(tmp_stack["category"].unique())
# 設定顏色
point_color = "#CC0000"

# 要變更的分類的編號
point_number = 2

# 建立原始的調色盤
palette = sns.color_palette("gray_r", num_category)

# 變更調色盤的部分顏色
palette[point_number] = point_color

# 繪製折線圖
ax = sns.lineplot(data=tmp_stack, x="年月", y="value", hue="category", palette=palette)

# 適度調整標籤與圖例
plt.xticks(rotation=30)
ax.legend(loc="lower left", bbox_to_anchor=(1, 0))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("bikes ST")

broken_df = pd.read_csv("data/bikes.csv", encoding="ISO-8859-1")

# Look at the first 3 rows
print(broken_df[:3])

print("------------------------------------------------------------")  # 60個

fixed_df = pd.read_csv(
    "data/bikes.csv",
    sep=";",
    encoding="latin1",
    parse_dates=["Date"],
    dayfirst=True,
    index_col="Date",
)
print(fixed_df[:3])

print(fixed_df["Berri 1"])

fixed_df["Berri 1"].plot()  # 無參數, 預設就是 line

show()


fixed_df.plot(figsize=(15, 10))

show()

print("------------------------------------------------------------")  # 60個

df = pd.read_csv(
    "data/bikes.csv",
    sep=";",
    encoding="latin1",
    parse_dates=["Date"],
    dayfirst=True,
    index_col="Date",
)
df["Berri 1"].plot()  # 無參數, 預設就是 line

show()

print("------------------------------------------------------------")  # 60個

# Make the graphs a bit prettier, and bigger
plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = (15, 5)
plt.rcParams["font.family"] = "sans-serif"

# This is necessary to show lots of columns in pandas 0.12.
# Not necessary in pandas 0.13.
pd.set_option("display.width", 5000)
pd.set_option("display.max_columns", 60)


bikes = pd.read_csv(
    "data/bikes.csv",
    sep=";",
    encoding="latin1",
    parse_dates=["Date"],
    dayfirst=True,
    index_col="Date",
)
bikes["Berri 1"].plot()  # 無參數, 預設就是 line
show()

berri_bikes = bikes[["Berri 1"]].copy()

berri_bikes[:5]

berri_bikes.index

berri_bikes.index.day

berri_bikes.index.weekday

berri_bikes.loc[:, "weekday"] = berri_bikes.index.weekday
berri_bikes[:5]

weekday_counts = berri_bikes.groupby("weekday").aggregate(sum)
weekday_counts

weekday_counts.index = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
weekday_counts

weekday_counts.plot(kind="bar")

show()

print("------------------------------------------------------------")  # 60個

bikes = pd.read_csv(
    "data/bikes.csv",
    sep=";",
    encoding="latin1",
    parse_dates=["Date"],
    dayfirst=True,
    index_col="Date",
)
# Add the weekday column
berri_bikes = bikes[["Berri 1"]].copy()
berri_bikes.loc[:, "weekday"] = berri_bikes.index.weekday

# Add up the number of cyclists by weekday, and plot!
weekday_counts = berri_bikes.groupby("weekday").aggregate(sum)
weekday_counts.index = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
weekday_counts.plot(kind="bar")

show()

print("bikes SP")

print("------------------------------------------------------------")  # 60個

plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = (8, 3)
plt.rcParams["font.family"] = "sans-serif"

# Canada's weather data for 2012, and saved it to a CSV.
# Here's the temperature every hour for 2012!

df_2012 = pd.read_csv("data/weather_2012.csv", index_col="Date/Time")
df_2012["Temp (C)"].plot(figsize=(8, 4), rot=-10)

show()

print("------------------------------------------------------------")  # 60個

# Here's an URL template you can use to get data in Montreal.
url_template = "http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"

# To get the data for March 2013, we need to format it with month=3, year=2012.
# url = url_template.format(month=3, year=2012)
# df_mar_2012 = pd.read_csv(url, skiprows=15, index_col='Date/Time', parse_dates=True, encoding='latin1', header=True)

# because the url is broken, we use our saved dataframe for now
df_mar_2012 = pd.read_csv("data/weather_2012.csv")

print(df_mar_2012)

df_mar_2012["Temp (C)"].plot(figsize=(15, 5))
show()

# '\xb0' for that degree character °
""" fail
df_mar_2012.columns = [
    u'Year', u'Month', u'Day', u'Time', u'Data Quality', u'Temp (C)', 
    u'Temp Flag', u'Dew Point Temp (C)', u'Dew Point Temp Flag', 
    u'Rel Hum (%)', u'Rel Hum Flag', u'Wind Dir (10s deg)', u'Wind Dir Flag', 
    u'Wind Spd (km/h)', u'Wind Spd Flag', u'Visibility (km)', u'Visibility Flag',
    u'Stn Press (kPa)', u'Stn Press Flag', u'Hmdx', u'Hmdx Flag', u'Wind Chill', 
    u'Wind Chill Flag', u'Weather']
"""

df_mar_2012 = df_mar_2012.dropna(axis=1, how="any")
print(df_mar_2012[:5])

print("------------------------------------------------------------")  # 60個

# fail
# df_mar_2012 = df_mar_2012.drop(['Year', 'Month', 'Day', 'Time', 'Data Quality'], axis=1)
# print(df_mar_2012[:5])

print("------------------------------------------------------------")  # 60個


# Plotting the temperature by hour of day

"""fail
temperatures = df_mar_2012[[u'Temp (C)']].copy()
print(temperatures.head)
temperatures.loc[:,'Hour'] = df_mar_2012.index.hour
temperatures.groupby('Hour').aggregate(np.median).plot()  # 無參數, 預設就是 line

show()
"""

print("------------------------------------------------------------")  # 60個

""" fail in reading csv data
#5.3 Getting the whole year of data

def download_weather_month(year, month):
    if month == 1:
        year += 1
    url = 'weather_2012.csv'
    weather_data = pd.read_csv(url, skiprows=15, index_col='Date/Time', parse_dates=True, header=True)
    weather_data = weather_data.dropna(axis=1)
    weather_data.columns = [col.replace('\xb0', '') for col in weather_data.columns]
    weather_data = weather_data.drop(['Year', 'Day', 'Month', 'Time', 'Data Quality'], axis=1)
    return weather_data


cc = download_weather_month(2012, 1)[:5]
print(cc)

data_by_month = [download_weather_month(2012, i) for i in range(1, 13)]

weather_2012 = pd.concat(data_by_month)
print(weather_2012)

#save to csv file
weather_2012.to_csv('tmp_weather_2012.csv')
"""
print("------------------------------------------------------------")  # 60個

plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = (15, 3)
plt.rcParams["font.family"] = "sans-serif"

weather_2012 = pd.read_csv(
    "data/weather_2012.csv", parse_dates=True, index_col="Date/Time"
)
print(weather_2012[:5])

weather_description = weather_2012["Weather"]
is_snowing = weather_description.str.contains("Snow")

# Not super useful
print(is_snowing[:5])

# More useful!
is_snowing = is_snowing.astype(float)
is_snowing.plot()  # 無參數, 預設就是 line

show()

print("------------------------------------------------------------")  # 60個

# Use resampling to find the snowiest month

# If we wanted the median temperature each month, we could use the resample() method like this:

weather_2012["Temp (C)"].resample("M").apply(np.median).plot(kind="bar")

show()

print("------------------------------------------------------------")  # 60個

print(is_snowing.astype(float)[:10])

print("------------------------------------------------------------")  # 60個

print(is_snowing.astype(float).resample("M").apply(np.mean))

is_snowing.astype(float).resample("M").apply(np.mean).plot(kind="bar")

show()

print("------------------------------------------------------------")  # 60個

# Plotting temperature and snowiness stats together

temperature = weather_2012["Temp (C)"].resample("M").apply(np.median)
is_snowing = weather_2012["Weather"].str.contains("Snow")
snowiness = is_snowing.astype(float).resample("M").apply(np.mean)

# Name the columns
temperature.name = "Temperature"
snowiness.name = "Snowiness"

# We'll use concat again to combine the two statistics into a single dataframe.
stats = pd.concat([temperature, snowiness], axis=1)
print(stats)

stats.plot(kind="bar")
show()

# Uh, that didn't work so well because the scale was wrong. We can do better by plotting them on two separate graphs:

stats.plot(kind="bar", subplots=True, figsize=(15, 10))
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
