"""

#pandas製作資料 修改資料 用matplotlib顯示


"""

print("------------------------------------------------------------")  # 60個

import seaborn as sns  # 海生, 自動把圖畫得比較好看

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

name = ["鼠", "牛", "虎", "兔"]
weight = [3, 48, 33, 8]

print("建立 DataFrame")
df = pd.DataFrame()
df["name"] = name
df["weight"] = weight
print(df)

"""
df.index = df["name"]
df["weight"].plot(kind="pie", autopct="%.0f%%", title = '派圖', fontsize = 12)
"""

"""
df["weight"].plot(kind = 'line', title = '線圖', fontsize = 12)
"""

df["weight"].plot(kind="bar", title="長條圖", fontsize=12)

plt.show()

print("------------------------------------------------------------")  # 60個

#                  2015,2016,2017,2018,2019
df = pd.DataFrame(
    [
        [250, 320, 300, 312, 280],  # 北部
        [280, 300, 280, 290, 310],  # 中部
        [220, 280, 250, 305, 250],
    ],  # 南部
    index=["北部", "中部", "南部"],
    columns=[2015, 2016, 2017, 2018, 2019],
)

df.plot(kind="line", title="線圖", figsize=[10, 5])
plt.show()

df.plot(kind="bar", title="長條圖", figsize=[10, 5])
plt.show()

df.plot(kind="barh", title="橫條圖", figsize=[10, 5])
plt.show()

df.plot(kind="bar", stacked=True, title="堆疊圖", figsize=[10, 5])
plt.show()

print("------------------------------------------------------------")  # 60個

#                  2015,2016,2017,2018,2019
df = pd.DataFrame(
    [
        [250, 320, 300, 312, 280],  # 北部
        [280, 300, 280, 290, 310],  # 中部
        [220, 280, 250, 305, 250],
    ],  # 南部
    index=["北部", "中部", "南部"],
    columns=[2015, 2016, 2017, 2018, 2019],
)
g1 = df.iloc[0].plot(
    kind="line",
    legend=True,
    xticks=range(2015, 2020),
    title="公司分區年度銷售表",
    figsize=[10, 5],
)
g1 = df.iloc[1].plot(kind="line", legend=True, xticks=range(2015, 2020))
g1 = df.iloc[2].plot(kind="line", legend=True, xticks=range(2015, 2020))

plt.show()

print("------------------------------------------------------------")  # 60個

#                  2015,2016,2017,2018,2019
df = pd.DataFrame(
    [
        [250, 320, 300, 312, 280],  # 北部
        [280, 300, 280, 290, 310],  # 中部
        [220, 280, 250, 305, 250],
    ],  # 南部
    index=["北部", "中部", "南部"],
    columns=[2015, 2016, 2017, 2018, 2019],
)
df.plot(kind="pie", subplots=True, figsize=[14, 6])  # 繪圖 plot

plt.show()

print("------------------------------------------------------------")  # 60個


#     "國文", "數學", "英文", "自然", "社會"
datas = [
    [65, 92, 78, 83, 70],  # 學生A
    [90, 72, 76, 93, 56],  # 學生B
    [81, 85, 91, 89, 77],  # 學生C
    [79, 53, 47, 94, 80],
]  # 學生D
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]

df = pd.DataFrame(datas, columns=columns, index=indexs)
df.plot(kind="bar", title="一年甲班成績單", fontsize=12)

plt.show()

print("------------------------------------------------------------")  # 60個

#      "國文","數學","英文","自然","社會"
datas = [
    [65, 92, 78, 83, 70],  # 學生A
    [90, 72, 76, 93, 56],  # 學生B
    [81, 85, 91, 89, 77],  # 學生C
    [79, 53, 47, 94, 80],
]  # 學生D
columns = ["國文", "數學", "英文", "自然", "社會"]

df = pd.DataFrame(datas, index=list(range(1, 5)), columns=columns)
df.plot(xticks=range(1, 5), title="一年甲班成績單", fontsize=12)

plt.show()

print("------------------------------------------------------------")  # 60個

""" no file
filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV5_Kobe_stats.csv'

df = pd.read_csv(filename)

data = pd.DataFrame()
data["Season"] = pd.to_datetime(df["Season"])
data["PTS"] = df["PTS"]
data["AST"] = df["AST"]
data["REB"] = df["TRB"]

data = data.set_index("Season")
data.plot(kind = 'line')

plt.show()
"""
print("------------------------------------------------------------")  # 60個

""" no file
filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV5_HOU_players_stats.csv'
df = pd.read_csv(filename)
df_grouped = df.groupby("Pos")
points = df_grouped["PTS/G"].mean()

data = pd.DataFrame()
data["Points"] = points
points.plot(kind = 'bar')

plt.show()
"""

print("------------------------------------------------------------")  # 60個

filename = "data/hours_used_performance.csv"
df = pd.read_csv(filename)
df.plot(kind="scatter", x="hours_used", y="work_performance")
print("係數矩陣 :", df.corr())

print("------------------------------------------------------------")  # 60個

""" no sklearn
filename = 'data/fb_tracking_happiness.csv'
df = pd.read_csv(filename)
print(df.head())

from sklearn import preprocessing

scaler = preprocessing.StandardScaler()
np_std = scaler.fit_transform(df)
df_std = pd.DataFrame(np_std, columns=["fb_tracking_s", "happiness_s"])
print(df_std.head())

df_std.plot(kind = "scatter", x = "fb_tracking_s", y = "happiness_s")

print('------------------------------------------------------------')	#60個

filename = 'data/fb_tracking_happiness.csv'
df = pd.read_csv(filename)
print(df.head())

from sklearn import preprocessing

scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
np_minmax = scaler.fit_transform(df)
df_minmax = pd.DataFrame(np_minmax, columns=["fb_tracking_m", "happiness_m"])
print(df_minmax.head())

df_minmax.plot(kind = "scatter", x = "fb_tracking_m", y = "happiness_m")

plt.show()
"""
print("------------------------------------------------------------")  # 60個

# df = pd.DataFrame(np.random.randn(3,3), columns=list("甲乙丙"))
# print(df)

# df = pd.DataFrame(np.random.randn(5, 3), index=list(range(1,6)), columns=list("ABC"))

#                    A  B  C  D  E
df = pd.DataFrame(
    [
        [65, 92, 78, 83, 70],
        [90, 72, 76, 93, 56],
        [81, 85, 91, 89, 77],
        [79, 53, 47, 94, 80],
    ],
    index=list(range(1, 5)),
    columns=list("ABCDE"),
)

print("原資料 :\n", df)

print("常用統計數據")
print(df.describe())

print("相關係數")
print(df.corr())

print("df轉csv")
df.to_csv("tmp_df_data1.csv")

print("data_frame 畫點圖")

x = df.A.values
y = df.B.values

plt.scatter(x, y)

print("存圖")
plt.savefig("tmp_df_data.png")

plt.show()

"""
loc 的用法
df.loc[列的範圍, 行的範圍]

df.loc[2:3, "B":"C"]


列或行只要一個
df.loc[2, "B"]

df.loc[2, "B"]=-1
"""

plt.show()

print("------------------------------------------------------------")  # 60個

# Python繪圖的方法-使用 pandas
# pandas 繪圖

data = np.random.randn(1000, 4)

df = pd.DataFrame(data=data, index=np.arange(1000), columns=["a", "b", "c", "d"])

# line plot

fig, axs = plt.subplots(2, 1, sharex=True)
df.plot(y=["a"], kind="line", ax=axs[0], title="ax1")
df.plot(y=["b", "c", "d"], kind="line", ax=axs[1], title="ax2", figsize=(10, 8))
axs[0].set_ylabel("ylabel")
axs[1].set_ylabel("ylabel")
axs[1].set_xlabel("Xlabel")
fig.suptitle("This is a somewhat long figure title", fontsize=16)

plt.show()

fig, axs = plt.subplots(1, 2, sharey=True)
df.plot(y=["a"], kind="line", ax=axs[0], legend=False)
df.plot(y=["b", "c", "d"], kind="line", ax=axs[1], figsize=(20, 5))

# 設定title
axs[0].set_title("ax1")
axs[1].set_title("ax2")

# 設定label
axs[0].set_xlabel("xlabel")
axs[1].set_xlabel("xlabel")
axs[0].set_xlabel("ylabel")

# 調整各個圖的間距
plt.subplots_adjust(hspace=0.5, wspace=0.1)

plt.show()

print("------------------------------------------------------------")  # 60個

# bar chart

speed = [0.1, 17.5, 40, 48, 52, 69, 88]
lifespan = [2, 8, 70, 1.5, 25, 12, 28]
index = ["snail", "pig", "elephant", "rabbit", "giraffe", "coyote", "horse"]
df = pd.DataFrame({"speed": speed, "lifespan": lifespan}, index=index)
ax = df.plot.bar(rot=45)  # rot表示xstick旋轉的角度
ax.legend(loc=2)  # legend的位置可以用loc調整

plt.show()

axes = df.plot.bar(rot=45, subplots=True, sharex=False)
axes[1].legend(loc=1)
plt.subplots_adjust(hspace=1, wspace=0.5)  # 調整各個ax間的距離
plt.suptitle("Bar chart")

plt.show()

fig, axs = plt.subplots(1, 2, sharey=False, figsize=(15, 4))
df.plot.bar(y="speed", rot=45, ax=axs[0])
df.plot.bar(y=["speed", "lifespan"], rot=45, ax=axs[1])
plt.subplots_adjust(wspace=0.1)
plt.suptitle("Bar chart")

plt.show()

print("------------------------------------------------------------")  # 60個

# scatter plot chart

fig, axs = plt.subplots(1, 2, figsize=(20, 8), sharey=False)
df = pd.DataFrame(
    [[5.1, 3.5, 0], [4.9, 3.0, 0], [7.0, 3.2, 1], [6.4, 3.2, 1], [5.9, 3.0, 2]],
    columns=["length", "width", "species"],
)
df.plot.scatter(
    x="length", y="width", s=50, marker="*", c="species", colormap="viridis", ax=axs[0]
)  # s設定點的大小
df.plot.bar(y=["length"], rot=45, ax=axs[1])
axs[1].set_xlabel("xlabel")
axs[1].set_ylabel("ylabel")
axs[1].legend(loc=2)
plt.suptitle("scatter plot")
plt.subplots_adjust(wspace=0.1)

plt.show()

print("------------------------------------------------------------")  # 60個

# hist plot

fig, ax = plt.subplots(1, 1, figsize=(10, 8))
df = pd.DataFrame(np.random.randint(1, 7, 6000), columns=["one"])
df["two"] = df["one"] + np.random.randint(1, 7, 6000)
df.plot.hist(bins=12, alpha=0.5, ax=ax)
ax.set_title("Hist. plot")
ax.set_xlabel("Xlabel")

plt.show()

print("------------------------------------------------------------")  # 60個

# box plot

df = pd.DataFrame(np.random.randn(10, 4), columns=["Col1", "Col2", "Col3", "Col4"])
df.boxplot(column=["Col1", "Col2", "Col3"])

plt.show()

print("------------------------------------------------------------")  # 60個

# kde plot

speed = [0.1, 17.5, 40, 48, 52, 69, 88]
lifespan = [2, 8, 70, 1.5, 25, 12, 28]
index = ["snail", "pig", "elephant", "rabbit", "giraffe", "coyote", "horse"]
df = pd.DataFrame({"speed": speed, "lifespan": lifespan}, index=index)
ax = df.plot.hist(y="lifespan", rot=45)  # rot表示xstick旋轉的角度

plt.show()

df = pd.DataFrame(
    {
        "x": [1, 2, 2.5, 3, 3.5, 4, 5],
        "y": [4, 4, 4.5, 5, 5.5, 6, 6],
    }
)
df.plot.kde()

plt.show()

print("------------------------------------------------------------")  # 60個

from matplotlib import style

style.use("fivethirtyeight")

dictionary1 = {
    "順序": [1, 2, 3, 4],
    "中文名": ["鼠", "牛", "虎", "兔"],
    "英文名": ["mouse", "ox", "tiger", "rabbit"],
    "體重": [3, 48, 33, 8],
    "代表": ["米老鼠", "班尼牛", "跳跳虎", "彼得兔"],
}
print("字典轉DataFrame")
df1 = pd.DataFrame(dictionary1)
print(df1)

print("-----------------")

dictionary2 = {
    "順序": [5, 6, 7, 8],
    "中文名": ["龍", "蛇", "馬", "羊"],
    "英文名": ["dragon", "snake", "horse", "goat"],
    "體重": [38, 16, 36, 29],
    "代表": ["逗逗龍", "貪吃蛇", "草泥馬", "喜羊羊"],
}

df2 = pd.DataFrame(dictionary2)

print("合併兩個DataFrame")
df3 = pd.concat([df1, df2])
print(df3)

print("-----------------")

# 設定陣列的第一欄
df3.set_index("順序", inplace=True)

# 排序, 升冪排序
df3.sort_values(by=["順序"])

print(df3)

df3.plot()

plt.show()

print("------------------------------------------------------------")  # 60個

# 常態分佈轉series
N = 1000  # 樣本數
s = pd.Series(np.random.normal(size=N))

# s.hist() #無參數
# s.hist(bins=50, alpha=0.5)# same
# s.plot.hist(bins=50, alpha=0.5)
# s.plot(kind='hist', title='常態分佈轉series 直方圖的使用')
s.plot(kind="hist", bins=50)
# s.plot(kind="hist") # 未指定束數, 預設10束

plt.show()

print("------------------------------------------------------------")  # 60個

mu = 170
sigma = 10
N = 500
random_data = np.random.normal(mu, sigma, N)

# np陣列轉df
df = pd.DataFrame(random_data)

# df.hist()
df.plot(kind="hist", bins=50)

plt.show()

print("------------------------------------------------------------")  # 60個

print("日本各都市平均氣溫全年資料")

filename = "data/weather_sample.csv"
weather = pd.read_csv(filename, header=0, parse_dates=["年月"])
# print(weather)

weather.plot(kind="line", x="年月", y="東京-平均氣溫(℃)", title="東京", figsize=[10, 5])
weather.plot(kind="line", x="年月", y="大阪-平均氣溫(℃)", title="大阪", figsize=[10, 5])

plt.show()

print("------------------------------")  # 30個

filename = "data/weather_sample.csv"
weather_index = pd.read_csv(filename, header=0, parse_dates=["年月"], index_col=0)
tmp_ave = weather_index[["東京-平均氣溫(℃)", "大阪-平均氣溫(℃)", "那霸-平均氣溫(℃)", "函館-平均氣溫(℃)"]]
print(tmp_ave)

# 在單一圖表繪製多張折線圖的範例

tmp_ave.plot(kind="line")

# 適度調整標籤與圖例
plt.xticks(rotation=30)
plt.legend()

plt.show()

print("------------------------------")  # 30個

# 將多張折線圖的折線設定為同一種類的範例

tmp_stack = (
    tmp_ave.stack()
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

plt.show()

print("------------------------------")  # 30個

# 強調特定折線圖的範例
# sns.set(style="white", font="meiryo")
tmp_stack = (
    tmp_ave.stack()
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

plt.show()

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

fixed_df["Berri 1"].plot()

plt.show()


fixed_df.plot(figsize=(15, 10))

plt.show()

print("------------------------------------------------------------")  # 60個

df = pd.read_csv(
    "data/bikes.csv",
    sep=";",
    encoding="latin1",
    parse_dates=["Date"],
    dayfirst=True,
    index_col="Date",
)
df["Berri 1"].plot()

plt.show()

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
bikes["Berri 1"].plot()
plt.show()

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

plt.show()

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

plt.show()

print("bikes SP")

print("------------------------------------------------------------")  # 60個

plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = (15, 3)
plt.rcParams["font.family"] = "sans-serif"

# Canada's weather data for 2012, and saved it to a CSV.
# Here's the temperature every hour for 2012!

weather_2012_final = pd.read_csv("data/weather_2012.csv", index_col="Date/Time")
weather_2012_final["Temp (C)"].plot(figsize=(15, 6))

plt.show()

print("------------------------------------------------------------")  # 60個

# Here's an URL template you can use to get data in Montreal.
url_template = "http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"

# To get the data for March 2013, we need to format it with month=3, year=2012.
# url = url_template.format(month=3, year=2012)
# weather_mar2012 = pd.read_csv(url, skiprows=15, index_col='Date/Time', parse_dates=True, encoding='latin1', header=True)

# because the url is broken, we use our saved dataframe for now
weather_mar2012 = pd.read_csv("data/weather_2012.csv")

print(weather_mar2012)

weather_mar2012["Temp (C)"].plot(figsize=(15, 5))
plt.show()

# '\xb0' for that degree character °
""" fail
weather_mar2012.columns = [
    u'Year', u'Month', u'Day', u'Time', u'Data Quality', u'Temp (C)', 
    u'Temp Flag', u'Dew Point Temp (C)', u'Dew Point Temp Flag', 
    u'Rel Hum (%)', u'Rel Hum Flag', u'Wind Dir (10s deg)', u'Wind Dir Flag', 
    u'Wind Spd (km/h)', u'Wind Spd Flag', u'Visibility (km)', u'Visibility Flag',
    u'Stn Press (kPa)', u'Stn Press Flag', u'Hmdx', u'Hmdx Flag', u'Wind Chill', 
    u'Wind Chill Flag', u'Weather']
"""

weather_mar2012 = weather_mar2012.dropna(axis=1, how="any")
print(weather_mar2012[:5])

print("------------------------------------------------------------")  # 60個

# fail
# weather_mar2012 = weather_mar2012.drop(['Year', 'Month', 'Day', 'Time', 'Data Quality'], axis=1)
# print(weather_mar2012[:5])

print("------------------------------------------------------------")  # 60個


# Plotting the temperature by hour of day

"""fail
temperatures = weather_mar2012[[u'Temp (C)']].copy()
print(temperatures.head)
temperatures.loc[:,'Hour'] = weather_mar2012.index.hour
temperatures.groupby('Hour').aggregate(np.median).plot()

plt.show()
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
is_snowing.plot()

plt.show()

print("------------------------------------------------------------")  # 60個

# Use resampling to find the snowiest month

# If we wanted the median temperature each month, we could use the resample() method like this:

weather_2012["Temp (C)"].resample("M").apply(np.median).plot(kind="bar")

plt.show()

print("------------------------------------------------------------")  # 60個

print(is_snowing.astype(float)[:10])

print("------------------------------------------------------------")  # 60個

print(is_snowing.astype(float).resample("M").apply(np.mean))

is_snowing.astype(float).resample("M").apply(np.mean).plot(kind="bar")

plt.show()

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
plt.show()

# Uh, that didn't work so well because the scale was wrong. We can do better by plotting them on two separate graphs:

stats.plot(kind="bar", subplots=True, figsize=(15, 10))
plt.show()

print("------------------------------------------------------------")  # 60個

# Make the graphs a bit prettier, and bigger
plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = (15, 5)
plt.rcParams["font.family"] = "sans-serif"

# This is necessary to show lots of columns in pandas 0.12.
# Not necessary in pandas 0.13.
pd.set_option("display.width", 5000)
pd.set_option("display.max_columns", 60)

print("------------------------------------------------------------")  # 60個

"""
# Make the graphs a bit prettier, and bigger
plt.style.use('ggplot')

# This is necessary to show lots of columns in pandas 0.12. 
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)

plt.rcParams['figure.figsize'] = (15, 5)

# because of mixed types we specify dtype to prevent any errors
csv_filename = 'C:/_git/vcs/_big_files/311-service-requests.csv'
complaints = pd.read_csv(csv_filename, dtype='unicode')

print(complaints)
complaints['Complaint Type']

complaints['Complaint Type'].value_counts()

complaint_counts = complaints['Complaint Type'].value_counts()
complaint_counts[:10]

complaint_counts[:10].plot(kind='bar')
plt.show()

print('------------------------------------------------------------')	#60個

# Make the graphs a bit prettier, and bigger
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

# This is necessary to show lots of columns in pandas 0.12. 
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)


# because of mixed types we specify dtype to prevent any errors
csv_filename = 'C:/_git/vcs/_big_files/311-service-requests.csv'
complaints = pd.read_csv(csv_filename, dtype='unicode')

is_noise = complaints['Complaint Type'] == "Noise - Street/Sidewalk"
noise_complaints = complaints[is_noise]
noise_complaints['Borough'].value_counts()

noise_complaint_counts = noise_complaints['Borough'].value_counts()
complaint_counts = complaints['Borough'].value_counts()

noise_complaint_counts / complaint_counts

noise_complaint_counts / complaint_counts.astype(float)

(noise_complaint_counts / complaint_counts.astype(float)).plot(kind='bar')

plt.show()
"""
print("------------------------------------------------------------")  # 60個

print("顯示")
n_items = 366
s = pd.Series(
    np.random.randn(n_items), index=pd.date_range("20000101", periods=n_items)
)

print("顯示s大小")
print(s.shape)

print("顯示s頭5項")
print(s.head(5))

print("顯示")
print(s.resample("1m").sum())

plt.figure(figsize=(10, 6))
cs = s.cumsum()
cs.plot()
plt.title("aaa")
plt.show()

plt.figure(figsize=(10, 6))
s.resample("1m").sum().plot.bar()
plt.title("bbb")
plt.show()

df = pd.DataFrame(np.random.randn(100, 4), columns=list("ABCD"))
print("df轉csv")
df.to_csv("tmp_df_data2.csv")

df = pd.read_csv("tmp_df_data2.csv", index_col=0)
print(df.shape)
print(df.head(5))

print("------------------------------------------------------------")  # 60個

dists = {
    "name": [
        "Zhongzheng",
        "Banqiao",
        "Taoyuan",
        "Beitun",
        "Annan",
        "Sanmin",
        "Daan",
        "Yonghe",
        "Bade",
        "Cianjhen",
        "Fengshan",
        "Xinyi",
        "Xindian",
    ],
    "population": [
        159598,
        551452,
        441287,
        275207,
        192327,
        343203,
        309835,
        222531,
        198473,
        189623,
        359125,
        225561,
        302070,
    ],
}
print(type(df))
df = pd.DataFrame(dists)
print(df)

# df.to_html("ch9-4-2-01.html")  #df轉html
df.plot()

df2 = pd.DataFrame(dists, columns=["population"], index=dists["name"])
print(df2)
# df2.to_html("ch9-4-2-02.html")  #df轉html
df2.plot()

plt.title("eee")
plt.show()

print("------------------------------------------------------------")  # 60個

dists = {
    "name": [
        "Zhongzheng",
        "Banqiao",
        "Taoyuan",
        "Beitun",
        "Annan",
        "Sanmin",
        "Daan",
        "Yonghe",
        "Bade",
        "Cianjhen",
        "Fengshan",
        "Xinyi",
        "Xindian",
    ],
    "population": [
        159598,
        551452,
        441287,
        275207,
        192327,
        343203,
        309835,
        222531,
        198473,
        189623,
        359125,
        225561,
        302070,
    ],
}

df = pd.DataFrame(dists, columns=["population"], index=dists["name"])
print(df)
df.plot(xticks=range(len(df.index)), use_index=True)

df.plot(xticks=range(len(df.index)), use_index=True, rot=90)

plt.title("fff")
plt.show()

print("------------------------------------------------------------")  # 60個

dists = {
    "區名": [
        "中正區",
        "板橋區",
        "桃園區",
        "北屯區",
        "安南區",
        "三民區",
        "大安區",
        "永和區",
        "八德區",
        "前鎮區",
        "鳳山區",
        "信義區",
        "新店區",
    ],
    "人口": [
        159598,
        551452,
        441287,
        275207,
        192327,
        343203,
        309835,
        222531,
        198473,
        189623,
        359125,
        225561,
        302070,
    ],
    "面積": [
        7.6071,
        23.1373,
        34.8046,
        62.7034,
        107.2016,
        19.7866,
        11.3614,
        5.7138,
        33.7111,
        19.1207,
        26.7590,
        11.2077,
        120.2255,
    ],
}

df = pd.DataFrame(dists, columns=["人口", "面積"], index=dists["區名"])
print(df)
# df.to_html("ch9-4-3.html")  #df轉html
df["面積"] *= 1000
df.plot(xticks=range(len(df.index)), use_index=True, rot=45)

plt.title("ggg")
plt.show()

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2 * np.pi, 50)
y = np.sin(x)

df = pd.DataFrame({"x": x, "y": y})

df.plot(kind="scatter", x="x", y="y", title="Sin(x)")

plt.title("lll")
plt.show()

print("------------------------------------------------------------")  # 60個

iris = pd.read_csv("data/iris.csv")

iris.boxplot(column="sepal_length", by="target", figsize=(6, 5))

plt.title("mmm")
plt.show()

print("------------------------------------------------------------")  # 60個

weight = [3, 48, 33, 8, 38, 16, 36, 29, 22, 6, 12, 42]
animals = ["鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬"]

x = pd.Series(weight)

x.plot(kind="bar", rot=0)
x.plot()

x = pd.Series(weight, index=animals)
x.plot()

plt.show()

print("------------------------------------------------------------")  # 60個

weight = [3, 48, 33, 8, 38, 16, 36, 29, 22, 6, 12, 42]
animals = ["鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬"]

fruits = ["蘋果", "梨子", "香蕉", "橙子"]
percentage = [30, 10, 40, 20]


s = pd.Series(percentage, index=fruits, name="水果")
print(s)

# s.plot(kind="pie")

explode = [0.1, 0.3, 0.1, 0.3]
s.plot(kind="pie", figsize=(6, 6), explode=explode)

plt.show()

print("------------------------------------------------------------")  # 60個

# 構建序列
data1 = pd.Series({"鼠": 3, "牛": 48, "虎": 33, "兔": 8, "龍": 38})
print(data1)

data1.name = ""

# 控制餅圖為正圓
plt.axes(aspect="equal")

# plot方法對序列進行繪圖
data1.plot(
    kind="pie",  # 選擇圖形類型
    autopct="%.1f%%",  # 餅圖中添加數值標簽
    radius=1,  # 設置餅圖的半徑
    startangle=180,  # 設置餅圖的初始角度
    counterclock=False,  # 將餅圖的順序設置為順時針方向
    title="分佈",  # 為餅圖添加標題
    wedgeprops={"linewidth": 1.5, "edgecolor": "green"},  # 設置餅圖內外邊界的屬性值
    textprops={"fontsize": 10, "color": "black"},  # 設置文本標簽的屬性值
)

plt.show()

print("------------------------------------------------------------")  # 60個

# 創造一些隨機資料 create some data with random value

s = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
s = s.cumsum()  # 計算累積值 cumulative sum

s.plot()

plt.show()


df = pd.DataFrame(np.random.randn(1000, 4), index=s.index, columns=list("ABCD"))
df = df.cumsum()

df.plot()

plt.show()

print("------------------------------------------------------------")  # 60個

"""
Pandas繪圖筆記
有以下類型的圖

折線圖df.plot()
柱狀圖df.plot(kind='bar')
橫向柱狀圖df.plot(kind='barh')
直方圖df.plot(kind='hist')
KDE圖df.plot(kind='kde')
面積圖df.plot(kind='area')
圓餅圖df.plot(kind='pie')
散佈圖df.plot(kind='scatter')
六角形箱體圖df.plot(kind='hexbin')
箱形圖df.plot(kind='box')
"""
print("------------------------------------------------------------")  # 60個

# 1.初始化

pd.set_option("display.max_rows", 1000)  # 設定最大能顯示1000rows
pd.set_option("display.max_columns", 1000)  # 設定最大能顯示1000columns

# 2.解決plot不能顯示中文問題
from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
mpl.rcParams["axes.unicode_minus"] = False

# 3.讀取檔案

df = pd.read_excel("data/2017_PM25.xlsx")

# 4.資料操作
# 4.1NaN與重複值處理

df = df.dropna()
df = df.drop_duplicates()

cc = df.head(30)
print(cc)

# 4.2檢視資料類型(有無非數值類型存在)

cc = df.dtypes
print(cc)

# 如果屬性是Object，如何改成數值屬性
# df["屬於Object的欄位"] = pd.to_numeric(df.屬於Object的欄位, errors='coerce')

"""
#相關係數
cc = df.corr()
print(cc)
"""
print("折線圖")

df.plot(x="監測月份", y="PM25", title="監測月份與PM2.5的關係")
plt.show()

df.plot(x="監測月份", y="PM10", title="監測月份與PM10的關係")
plt.show()

print("柱狀圖")
df.plot(kind="bar", x="監測月份", y="PM25", title="監測月份與PM2.5的關係")
plt.show()

print("橫向柱狀圖")
df.plot(kind="barh", x="監測月份", y="PM25", title="監測月份與PM2.5的關係")
plt.show()

print("直方圖")
df.plot(kind="hist", x="監測月份", y="PM25", title="監測月份與PM2.5的關係")
plt.show()

"""
print("核密度(KDE)圖")
df.plot(kind='kde',x='監測月份', y='PM25',title='監測月份與PM2.5的關係')
plt.show()
"""

print("面積圖")
df.plot(kind="area", x="監測月份", y="PM25", title="監測月份與PM2.5的關係")
plt.show()

print("圓餅圖")
df.plot(kind="pie", x="監測月份", y="PM25", title="監測月份與PM2.5的關係", autopct="%1.2f%%")
plt.show()

print("散佈圖")
df.plot(kind="scatter", x="PM25", y="PM10", title="PM2.5與PM10的關係")  # X,Y需為數值
plt.show()

print("六角形箱體圖")
df.plot(kind="hexbin", x="PM25", y="PM10", title="PM2.5與PM10的關係")  # X,Y需為數值
plt.show()

print("箱形圖")
df.plot(kind="box", x="PM25", y="PM10", title="監測月份與PM2.5的關係")  # X,Y需為數值
plt.show()

print("------------------------------------------------------------")  # 60個

import seaborn as sns  # 海生, 自動把圖畫得比較好看

tips = sns.load_dataset("tips")
cc = tips.head()
print(cc)


sns.distplot(tips["total_bill"])
plt.show()

sns.distplot(tips["total_bill"], kde=False, bins=30)
plt.show()

sns.jointplot(x="total_bill", y="tip", data=tips, kind="scatter")

sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex")
sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg")

sns.pairplot(tips)

sns.pairplot(tips, hue="sex", palette="coolwarm")

sns.kdeplot(tips["total_bill"])
sns.rugplot(tips["tip"])

plt.show()


sns.barplot(x="sex", y="total_bill", data=tips, estimator=np.std)
plt.show()

sns.countplot(x="sex", data=tips)
plt.show()

sns.boxplot(x="day", y="total_bill", data=tips, hue="smoker")
plt.show()

sns.violinplot(x="day", y="total_bill", data=tips, hue="sex", split=True)
plt.show()

sns.stripplot(x="day", y="total_bill", data=tips, jitter=True, hue="sex", dodge=True)
plt.show()

sns.violinplot(x="day", y="total_bill", data=tips)
sns.swarmplot(x="day", y="total_bill", data=tips, color="black")

plt.show()
""" NG
sns.factorplot(x='day',y='total_bill',data=tips,kind='bar')

tc = tips.corr()

sns.heatmap(tc,annot=True,cmap='coolwarm')

plt.show()
"""

""" NG
fp=flights.pivot_table(index='month',columns='year',values='passengers')

sns.heatmap(fp,cmap='magma',linecolor='white',linewidths=1)

plt.show()

sns.clustermap(fp,cmap='coolwarm',standard_scale=1)

sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['o','v'],scatter_kws={'s':100})


sns.lmplot(x='total_bill',y='tip',data=tips,col='sex',row='time',aspect=1,size=4)
"""
iris = sns.load_dataset("iris")
cc = iris.head()
print(cc)

cc = iris["species"].unique()
print(cc)

# array(['setosa', 'versicolor', 'virginica'], dtype=object)

g = sns.PairGrid(iris)
g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)

g = sns.FacetGrid(data=tips, col="time", row="smoker")

g.map(plt.scatter, "total_bill", "tip")

sns.set_style("ticks")
sns.countplot(x="sex", data=tips)

plt.show()

sns.despine(left=True, bottom=True)


sns.countplot(x="sex", data=tips)

plt.show()

sns.set_context("paper")
sns.countplot(x="sex", data=tips)

plt.show()

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/年度銷售金額.csv")

df.index = df["AREA"]

df = df.drop("AREA", axis=1)

print(df)

df["1st"].plot(kind="pie", autopct="%.2f%%")
# df["1st"].plot(kind="pie")
plt.show()

print("------------------------------")  # 30個

df.plot(kind="bar", rot=0)
plt.show()

print("------------------------------")  # 30個

# 旋轉X軸標籤角度
df.plot(kind="bar")
plt.show()

print("------------------------------")  # 30個

df.plot(kind="bar", rot=0)
plt.show()

print("------------------------------------------------------------")  # 60個

df.plot(kind="barh")
plt.show()

print("------------------------------------------------------------")  # 60個

"""
df["1st"].plot(kind="pie", title="Proportion of each area")
df["1st"].plot(kind="pie", colors=["red", "#00FF00", "blue", "yellow"])
df["1st"].plot(kind="pie", fontsize=12)
df["1st"].plot(kind="pie", figsize=(1, 1))
df["1st"].plot(kind="pie", figsize=(4, 4))
df["1st"].plot(kind="pie", autopct="%.2f")
df["1st"].plot(kind="pie", autopct="%.0f%%")
"""

print("------------------------------------------------------------")  # 60個

# 折線圖

df = pd.read_csv("data/觀光人數統計.csv")

df.index = df["Month"]  # 自定列索引為Month內容

print(df[["Green Island", "Guguan"]].head())

df[["Green Island", "Guguan"]].plot()

plt.show()

print("------------------------------------------------------------")  # 60個

# 折線圖
df = pd.read_csv("data/觀光人數統計.csv")
df.index = df["Month"]  # 自定列索引為Month內容
df = df.drop("Month", axis=1)  # 刪除原本的月份行資料
print(df.head())

df.plot()

plt.show()

print("------------------------------------------------------------")  # 60個

# 折線圖 + 參數
df.plot(linewidth=2, linestyle=":", title="Number of visitors")

plt.show()

print("------------------------------------------------------------")  # 60個

# 折線圖

a = ["E", "W", "S", "N"]
m = [4522, 3101, 5211, 4613]
s = pd.Series(m, index=a)
print(s)

s.plot()

plt.show()

print("------------------------------------------------------------")  # 60個


# 加廣知識：自定列索引

a = ["E", "W", "S", "N"]

m = [4522, 3101, 5211, 4613]

s = pd.Series(m, index=a)

print(s)

s.plot()

plt.show()

print("------------------------------------------------------------")  # 60個

s.index = ["EAST", "WEST", "SOUTH", "NORTH"]

print(s)

s.plot()

plt.show()

print("------------------------------------------------------------")  # 60個

print(df.head())

df_T = df.T

print(df_T.head())

# 實作-折線圖(部份資料框)【EX5-2.1b.ipynb】
# Step 01

df1 = df["Green Island"]

print(df1.head())

# Step 02
df1.plot()
plt.show()

print("------------------------------------------------------------")  # 60個

# Step 03

df2 = df[["Green Island", "Guguan"]]

print(df2.head())

# Step 04

df2.plot()

plt.show()

print("------------------------------------------------------------")  # 60個

# Step 05

df_T = df.T

print(df_T.head())

# Step 06

df3 = df_T[3]

df3.plot()

plt.show()

print("------------------------------------------------------------")  # 60個


# 5-2-4 掌握分佈局勢的直方圖
# (圖)-直方圖：顯示成績分布的情形

df = pd.read_csv("data/第一次期中考.csv")

print(df)

df["第1次期中考"].plot(kind="bar")

plt.show()

print("------------------------------------------------------------")  # 60個

df["第1次期中考"].plot(kind="hist", bins=10)

plt.show()

print("------------------------------------------------------------")  # 60個

# 直方圖 hist

df = pd.read_csv("data/學生成績檔.csv")
print(df.head())

df["第1次平時考"].plot(kind="hist")
plt.show()

print("------------------------------------------------------------")  # 60個

# 直方圖 hist
df["第1次平時考"].plot(kind="hist", bins=20)
plt.show()

print("------------------------------------------------------------")  # 60個

# 直方圖 hist
df["第1次平時考"].plot(kind="hist", bins=40)
plt.show()

print("------------------------------------------------------------")  # 60個

# 直方圖 hist
df["第1次平時考"].plot(kind="hist", color="blue", edgecolor="orange")
plt.show()

print("------------------------------------------------------------")  # 60個

# 散佈圖：氣溫與紅茶銷售量之間的相關性

df = pd.read_csv("data/紅茶銷售量.csv")
print(df)

df.plot(kind="scatter", x="temperature", y="sale")

plt.show()

print("------------------------------------------------------------")  # 60個

# 散佈圖

df = pd.read_csv("data/sunshine.csv")
print(df)

df.plot(kind="scatter", x="SunShine", y="Temperature")

plt.show()

print("------------------------------------------------------------")  # 60個

# 設定散佈圖X、Y軸的座標值

df.plot(kind="scatter", x="SunShine", y="Temperature")
plt.show()

print("------------------------------------------------------------")  # 60個

df.plot(kind="scatter", x="SunShine", y="Temperature", xlim=(0, 200), ylim=(0, 40))
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


# 如果是pandas資料 用 plt畫圖的 要改成pandas資料之使用


# df 轉  html

usage = {
    "os": ["Windows", "Mac OS", "Linux", "Chrome OS", "BSD"],
    "percentage": [88.78, 8.21, 2.32, 0.34, 0.02],
}

df = pd.DataFrame(usage, columns=["percentage"], index=usage["os"])
print(df)
df.to_html("tmp_ch9-4-4.html")

print("------------------------------------------------------------")  # 60個


"""

#準備做 pandas 多圖 TBD

name = ["鼠", "牛", "虎", "兔"]
weight = [3, 48, 33, 8]

print('建立 DataFrame')
df = pd.DataFrame()
df["name"] = name
df["weight"] = weight
print(df)

df["weight"].plot(kind = 'line', title = '線圖', fontsize = 12)

plt.show()


df = pd.DataFrame(np.random.randint(1, 7, 6000),columns = ['one'])
df['two'] = df['one'] + np.random.randint(1, 7, 6000)

fig,ax1=plt.subplots(2,1,figsize=(10,8))
df.plot.hist(bins=12, alpha=0.5,ax=ax1)
ax1.set_title('Hist. plot')
ax1.set_xlabel('Xlabel')


fig,ax2=plt.subplots(1,2,figsize=(10,8))
df.plot.hist(bins=12, alpha=0.5,ax=ax2)
ax2.set_title('Hist. plot')
ax2.set_xlabel('Xlabel')


plt.show()
"""


# pd_plot1.py

df = pd.DataFrame(
    [[250, 320, 300, 312, 280], [280, 300, 280, 290, 310], [220, 280, 250, 305, 250]],
    index=["北部", "中部", "南部"],
    columns=[2015, 2016, 2017, 2018, 2019],
)
g1 = df.plot(kind="bar", title="長條圖", figsize=[10, 5])
g2 = df.plot(kind="barh", title="橫條圖", figsize=[10, 5])
g3 = df.plot(kind="bar", stacked=True, title="堆疊圖", figsize=[10, 5])

# pd_plot2.py

df = pd.DataFrame(
    [[250, 320, 300, 312, 280], [280, 300, 280, 290, 310], [220, 280, 250, 305, 250]],
    index=["北部", "中部", "南部"],
    columns=[2015, 2016, 2017, 2018, 2019],
)
g1 = df.iloc[0].plot(
    kind="line",
    legend=True,
    xticks=range(2015, 2020),
    title="公司分區年度銷售表",
    figsize=[10, 5],
)
g1 = df.iloc[1].plot(kind="line", legend=True, xticks=range(2015, 2020))
g1 = df.iloc[2].plot(kind="line", legend=True, xticks=range(2015, 2020))

# pd_plot3.py

df = pd.DataFrame(
    [[250, 320, 300, 312, 280], [280, 300, 280, 290, 310], [220, 280, 250, 305, 250]],
    index=["北部", "中部", "南部"],
    columns=[2015, 2016, 2017, 2018, 2019],
)
df.plot(kind="pie", subplots=True, figsize=[20, 20])


