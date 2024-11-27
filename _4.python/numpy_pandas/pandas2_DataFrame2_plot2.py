"""
Pandas繪圖 用matplotlib顯示

完整且較複雜的

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

# catplot兩變量關係圖
sns.catplot(x='day',y='total_bill',data=tips,kind='bar')

tc = tips.corr()

sns.heatmap(tc,annot=True,cmap='coolwarm')

plt.show()


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
print("------------------------------------------------------------")  # 60個

print("日本各都市平均氣溫全年資料")

filename = "data/weather_sample.csv"
df = pd.read_csv(filename, header=0, parse_dates=["年月"])
# print(df)

df.plot(kind="line", x="年月", y="東京-平均氣溫(℃)", title="東京", figsize=[10, 5])
df.plot(kind="line", x="年月", y="大阪-平均氣溫(℃)", title="大阪", figsize=[10, 5])

plt.show()

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

plt.show()

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

plt.show()

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

plt.show()

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
df["Berri 1"].plot()  # 無參數, 預設就是 line

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
bikes["Berri 1"].plot()  # 無參數, 預設就是 line
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
plt.rcParams["figure.figsize"] = (8, 3)
plt.rcParams["font.family"] = "sans-serif"

# Canada's weather data for 2012, and saved it to a CSV.
# Here's the temperature every hour for 2012!

df_2012 = pd.read_csv("data/weather_2012.csv", index_col="Date/Time")
df_2012["Temp (C)"].plot(figsize=(8, 4), rot=-10)

plt.show()

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
plt.show()

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
is_snowing.plot()  # 無參數, 預設就是 line

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
print("------------------------------------------------------------")  # 60個
