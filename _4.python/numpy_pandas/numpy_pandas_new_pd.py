"""
pandas的使用


"""


print("------------------------------")  # 30個

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

df = pd.read_excel("1111data.xlsx")
city = ["台北", "新北", "桃園", "台中", "台南", "高雄"]  # 六都
citycount = []  # 存六都工作職缺數量的串列
for i in range(len(city)):
    df1 = df[df["工作地點"].str.contains(city[i])]  # 取出包含指定地點的資料
    citycount.append(len(df1))

ser = pd.Series(citycount, index=city)  # 串列轉Series
print(ser)
plt.axis("off")
ser.plot(kind="pie", title="六都電腦職缺數量", figsize=(6, 6))  # 繪製圓餅圖

print("------------------------------------------------------------")  # 60個

# 1111salary.py
import re

df = pd.read_excel("1111data.xlsx")
city = ["台北", "新北", "桃園", "台中", "台南", "高雄"]  # 六都
salarylist = []
for i in range(len(city)):
    df1 = df[(df["工作地點"].str.contains(city[i])) & (df["薪資"].str.contains("月薪"))]
    indexlist = df1.index  # 取得資料索引
    total = 0  # 薪資總額
    for j in range(len(df1)):
        salarytem = df1["薪資"][indexlist[j]].replace(",", "")  # 以資料索引取得資料
        salanum = re.findall(r"\d+\.?\d*", salarytem)  # 取出資料中的數值
        if len(salanum) == 1:  # 若是1個數值即為薪資
            salary = int(salanum[0])
        else:  # 若是2個數值則取平均數
            salary = (int(salanum[0]) + int(salanum[1])) / 2
        total += salary
    salarycity = int(total / len(df1))  # 平均薪資
    salarylist.append(salarycity)

ser = pd.Series(salarylist, index=city)  # 串列轉Series
print(ser)
plt.ylabel("單位：元")
ser.plot(kind="bar", title="六都電腦職缺薪資", figsize=(5, 5))  # 繪製長條圖

print("------------------------------------------------------------")  # 60個

# dataframe.py

columns = ["姓名", "班級"]
data = [
    ["林大和", "一年甲班"],
    ["張小明", "一年乙班"],
    ["林美麗", "一年乙班"],
    ["鄭中林", "二年甲班"],
    ["林品朋", "二年甲班"],
    ["陳明朋", "二年乙班"],
]
df = pd.DataFrame(data, columns=columns)
# print(df)

df1 = df[df["班級"] == "二年甲班"]
# print(df1)
df2 = df[df["姓名"].str.contains("林")]
# print(df2)
df3 = df[(df["姓名"].str.contains("林")) & (df["班級"].str.contains("一年"))]
print(df3)

print("------------------------------------------------------------")  # 60個

# 索引
df = pd.DataFrame({"a": [1, 3], "b": [2, 4]}, index=["line1", "line2"])
print(df.index)  # 顯示行索引
print(df.columns)  # 顯示列索引

print("------------------------------------------------------------")  # 60個

from datetime import datetime

# Pandas日期時間處理
# 時間點TimeStamp

t = pd.to_datetime("2019-03-01 00:00:00")  # 從字符串轉換
print(type(t), t)
t = pd.to_datetime(datetime.now())  # 從datetime格式轉換
print(type(t), t)

# 時間間隔
t1 = pd.to_datetime("2019-03-01 00:00:00")
t2 = pd.to_datetime(datetime.now())
delta = t2 - t1  # 通過TimeStamp相減獲取
print(type(delta), delta, delta.days, delta.seconds)

delta = pd.Timedelta(days=27)  # 構造時間間隔爲27天
print(t2 + delta)

# 時間段Period
t = pd.to_datetime(datetime.now())
p = pd.Period(t, freq="H")
print(p, p.start_time, p.end_time)  # 顯示時間段起止時間

# 批量轉換
arr = ["2019-03-01", "2019-03-02", "2019-03-03"]
df = pd.DataFrame({"d": arr})
df["d"] = pd.to_datetime(df["d"])
print(df)

print("------------------------------------------------------------")  # 60個

# 時間序列操作
# 時間日期類型索引
df.index = pd.to_datetime(df["d"])  # 本例中使用了上例中構造的df[‘d’]
print(df.index)

df = pd.DataFrame()
df["date"] = pd.date_range(start="2017-12-30", end="2019-01-05", freq="d")  # 創建時間數據
df["val"] = df["date"].apply(lambda x: x.weekday())  # 計算該日是星期幾
df.set_index("date", inplace=True)  # 設置時間索引
print(df.head(3))  # 顯示前三條

# 時間段類型索引
df_period = df.to_period(freq="M")  # 按月創建時間段
print(type(df_period.index))  # 查看類型
print(len(df_period))  # 查看記錄個數，與原記錄個數一致
print(df_period.head(3))

print(df_period.index[0].start_time, df_period.index[0].end_time)
print(df_period.index[1].start_time, df_period.index[1].end_time)
print(df.index.is_unique, df_period.index.is_unique)

df_dt = df_period.to_timestamp()
print(df_dt.head(3))
print(type(df_dt.index))

print("------------------------------------------------------------")  # 60個
""" no df
# 篩選和切分
print(df['2019'])  # 篩選2019全年數據
print(df['2019-01'])  #  篩選2019年一月全月數據
print(df['2018':'2019'].head()) # 篩選2018年初到2019年底的所有數據
print(df['2018-12-31':].head()) # 篩選2018-12-31及之後的數據

# 重採樣
tmp = df.resample('w').sum() # 使用疊加方式按周重採樣
print(tmp.head(3))

tmp = df.resample('M').ohlc() # 使用用ohlc方式按月降採樣
print(tmp.head(3))

tmp = df.resample('M').sum().to_period('M') # 按月降採樣，同時將時間變爲時間段
print(tmp.head(3))

df1 = pd.DataFrame({'val':[8,7,6]})
df1.index = pd.to_datetime(['2019-03-01','2019-03-15','2019-03-31']) # 僅含三條數據
df2 = df1.resample('D').interpolate() # 用插值方式升採樣
print(len(df2))
print(df2.head(3))

df3 = df1.asfreq('D')
print(df3.head(3))

# 偏移
df['prev'] = df['val'].shift() # 取前一條數據的val值作爲當前記錄中prev字段的值
print(df.head(3))

# 計算滑動窗口
df['sw'] = df['val'].rolling(window=3).mean() # 計算窗口中數據的均值
print(df.head(3))

df['emw_3'] = df['val'].ewm(span=3).mean()
df['emw_7'] = df['val'].ewm(span=7).mean()
df['rolling'] = df['val'].rolling(7).mean()
"""
print("------------------------------------------------------------")  # 60個

# 時區轉換

import pytz

print("時區個數 :", len(pytz.common_timezones))
print("前3個 :", pytz.common_timezones[:3])

import datetime

t = datetime.datetime.now()
print(t)

utc_dt = pytz.utc.localize(t)
print(utc_dt)

from pytz import timezone

tz = timezone("Asia/Shanghai")  # 將時區設爲上海
print(utc_dt.astimezone(tz))  # 轉換時區

df = pd.DataFrame()
df["date"] = pd.date_range(start="2018-12-31", end="2019-01-01", freq="d")
df.set_index("date", inplace=True)  # 設置時間索引
print(df.index)

df.index = df.index.tz_localize("UTC")
print(df.index.values, df.index)

df.index = df.index.tz_convert("Asia/Shanghai")
print(df.index.values)
print(df.index)

print("------------------------------------------------------------")  # 60個

# 數據重排
# 數據錶轉置
df = pd.DataFrame({"a": [1, 2], "b": [3, 4]}, index=["l1", "l2"])
print(df)
print(df.T)

# 行轉列和列轉行
df1 = df.stack()  # 列轉行
print(df1)

print(df1.unstack())  # 將內層行索引轉爲列索引
print(df1.unstack(level=0))  # 將外層行索引轉爲列索引

# 透視轉換
df = pd.DataFrame(
    {
        "時間": ["期中", "期末", "期中", "期末"],
        "學科": ["語文", "語文", "數學", "數學"],
        "分數": [89, 75, 90, 95],
    }
)
df1 = df.pivot(index="時間", columns="學科", values="分數")
print(df, df1)

print("------------------------------------------------------------")  # 60個

print("基本類型轉換")

dic = {
    "string": ["dog", "snake", "cat", "dog", "monkey", "elephant"],
    "integer": [2000, 2000, 2001, 2002, 2003, np.nan],
    "float": [1.5, 1.5, 1.7, np.nan, np.nan, 8.3],
    "dtime": [
        "2018-01-01",
        "2018/01/02",
        "2018-01-03",
        "2018-01-04",
        "2018-01-05",
        np.nan,
    ],
    "mix": [1, 1, 0, "+", 0, 1],
    "classify": ["A", "B", "A", "B", "A", "A"],
}
data = pd.DataFrame(dic)
print(data.dtypes)
""" NG
data['dtime'] = pd.to_datetime(data['dtime'], infer_datetime_format=True)
data['mix']=pd.to_numeric(data['mix'],errors='coerce')
data['classify']=pd.Categorical(data['classify'])
data['float']=data['float'].astype(np.float32)
print(data.dtypes)
"""
print("------------------------------------------------------------")  # 60個

print("缺失值處理")

dic = {
    "state": ["Ohio", "Ohio", "Ohio", "Ohio", "Nevada", "Nevada"],
    "year": [2000, 2000, 2001, 2002, 2003, 3456],
    "score": [1.5, 1.5, 1.7, np.nan, np.nan, 8.3],
    "desc": [np.nan, np.nan, np.nan, np.nan, np.nan, 3],
    "val1": [1, 1, 0, "+", 0, 1],
}
data = pd.DataFrame(dic)

print(data["desc"].nunique())  # 不同取值個數
print(data["desc"].unique())  # 不同取值列表
print(data["year"].value_counts())  # 不同取值出現次數

print(data["desc"].isnull())  # 是否缺失
print(data["desc"].isnull().any())  # 是否含有任意缺失
print(data["desc"].isnull().all())  # 是否全部缺失
print(data["desc"].isnull().sum(), len(data))  # 空值個數與記錄個數
print(data.dropna(axis=1, how="all"))
print(data["score"].fillna(data["score"].mean()))
print(data["score"].fillna(method="ffill", limit=1))

print(data.interpolate(mdthod="polynomial", order=2))  # 二次多項式插值
print(data.interpolate(mdthod="spline", order=3))  # 三次樣條插值

print("異常值處理")

print(data.query("year<2050"))
print(data[data["year"] < 2050])

data["val1"] = data["val1"].apply(lambda x: 1 if x == "+" else x)

print("去重處理")

print(data.drop_duplicates(keep="last"))
print(data.drop_duplicates(keep="last", subset="year"))

print("------------------------------------------------------------")  # 60個

print("merge方法")

df1 = pd.DataFrame({"id": [1, 2, 3], "val1": [2, 4, 6]})
df2 = pd.DataFrame({"id": [3, 2, 2], "val2": [9, 6, 5]})
print(pd.merge(df1, df2, how="left"))

print("------------------------------------------------------------")  # 60個

print("concat方法")

df1 = pd.DataFrame({"id": [1, 2, 3], "val1": [2, 4, 6]})
df2 = pd.DataFrame({"id": [3, 2, 2], "val2": [9, 6, 5]})
print(pd.concat([df1, df2]))
print(pd.concat([df1, df2], axis=1))

print("------------------------------------------------------------")  # 60個

print("數值型特徵")

dic = {"height": [1.6, 1.7, 1.8], "weight": [60, 70, 90]}
data = pd.DataFrame(dic)
data["bmi"] = data["weight"] / (data["height"] ** 2)
print(data)
data["overweight"] = data["bmi"] > 25
print(data)
data["overweight"] = data["overweight"].map({True: "Yes", False: "No"})
print(data)

print("------------------------------------------------------------")  # 60個

print("類型特徵")

dic = {"string": ["第一組", "第二組", "第二組"]}
data = pd.DataFrame(dic)
print(pd.factorize(data.string))  # 轉換成數值型編碼

data["num"] = pd.factorize(data["string"])[0]
df = pd.get_dummies(data["string"], prefix="組別")  # 轉換成onehot類型編碼
new_data = pd.concat([data, df], axis=1)
print(new_data)

print("------------------------------------------------------------")  # 60個

results = []
for num_throws in range(1, 10001):
    throws = np.random.randint(low=0, high=2, size=num_throws)
    probability_of_throws = throws.sum() / num_throws
    results.append(probability_of_throws)

df = pd.DataFrame({"投擲": results})

df.plot(color="b")
plt.title("大數法則(Law of Large Numbers)")
plt.xlabel("投擲次數")
plt.ylabel("平均機率")
plt.show()

print("------------------------------------------------------------")  # 60個

results = []
for num_throws in range(1, 10001):
    throws = np.random.randint(low=1, high=7, size=num_throws)
    mask = throws == 1
    probability_of_throws = len(throws[mask]) / num_throws
    results.append(probability_of_throws)

df = pd.DataFrame({"投擲": results})

df.plot(color="r")
plt.title("大數法則(Law of Large Numbers)")
plt.xlabel("投擲次數")
plt.ylabel("平均機率")
plt.show()

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/titanic.csv")
s = pd.Series([30, 1, 5, 10, 30, 50, 30, 15, 40, 45, 30])

print(df["Age"].mode())
print(s.mode())

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/titanic.csv")
s = pd.Series([30, 1, 5, 10, 30, 50, 30, 15, 40, 45, 30])

print(df["Age"].median())
print(s.median())

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/titanic.csv")
s = pd.Series([30, 1, 5, 10, 30, 50, 30, 15, 40, 45, 30])

print(df["Age"].quantile(q=0.25))
print(df["Age"].quantile(q=0.5))
print(df["Age"].quantile(q=0.75))
print(s.quantile(q=0.25))
print(s.quantile(q=0.5))
print(s.quantile(q=0.75))

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/titanic.csv")
s = pd.Series([30, 1, 5, 10, 30, 50, 30, 15, 40, 45, 30])

print(df["Age"].mean())
print(s.mean())

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/titanic.csv")
s = pd.Series([30, 1, 5, 10, 30, 50, 30, 15, 40, 45, 30])

print(df["Age"].max() - df["Age"].min())
print(s.max() - s.min())

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/titanic.csv")
s = pd.Series([30, 1, 5, 10, 30, 50, 30, 15, 40, 45, 30])

print(df["Age"].quantile(0.75) - df["Age"].quantile(0.25))
print(s.quantile(0.75) - s.quantile(0.25))

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/titanic.csv")
s = pd.Series([30, 1, 5, 10, 30, 50, 30, 15, 40, 45, 30])

print(df["Age"].var())
print(s.var())

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/titanic.csv")
s = pd.Series([30, 1, 5, 10, 30, 50, 30, 15, 40, 45, 30])

print(df["Age"].std())
print(s.std())

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/titanic.csv")
s = pd.Series([30, 1, 5, 10, 30, 50, 30, 15, 40, 45, 30])

print(df["Age"].describe())
print("---------------------------")
print(s.describe())

print("------------------------------------------------------------")  # 60個

friends = [
    110,
    1017,
    1127,
    417,
    624,
    957,
    89,
    951,
    947,
    797,
    981,
    125,
    455,
    731,
    1641,
    486,
    1307,
    472,
    1131,
    1771,
    905,
    532,
    742,
    622,
]

s_friends = pd.Series(friends)
print(s_friends.describe())

print("------------------------------------------------------------")  # 60個

friends = [
    110,
    1017,
    1127,
    417,
    624,
    957,
    89,
    951,
    947,
    797,
    981,
    125,
    455,
    731,
    1641,
    486,
    1307,
    472,
    1131,
    1771,
    905,
    532,
    742,
    622,
]

s_friends = pd.Series(friends)
m = s_friends.mean()
print("平均數: ", m)
s = s_friends.std()
print("標準差: ", s)

z_scores = []
for x in friends:
    z = (x - m) / s  # 公式
    z_scores.append(z)
print(z_scores)

print("------------------------------------------------------------")  # 60個

friends = [
    110,
    1017,
    1127,
    417,
    624,
    957,
    89,
    951,
    947,
    797,
    981,
    125,
    455,
    731,
    1641,
    486,
    1307,
    472,
    1131,
    1771,
    905,
    532,
    742,
    622,
]

s_friends = pd.Series(friends)
m = s_friends.mean()
s = s_friends.std()
z_scores = []
for x in friends:
    z = (x - m) / s  # 公式
    z_scores.append(z)
index = np.arange(len(friends))
plt.bar(index, z_scores)
plt.show()

print("------------------------------------------------------------")  # 60個

dice = [1, 2, 3, 4, 5, 6]
sample_means = []
for x in range(100):
    sample = np.random.choice(a=dice, size=1)
    sample_means.append(sample.mean())

df = pd.DataFrame(sample_means)
df.plot(kind="density")
plt.show()

print("------------------------------------------------------------")  # 60個

dice = [1, 2, 3, 4, 5, 6]
sample_means = []
for x in range(100):
    sample = np.random.choice(a=dice, size=10)
    sample_means.append(sample.mean())

df = pd.DataFrame(sample_means)
df.plot(kind="density")
plt.show()

print("------------------------------------------------------------")  # 60個

dice = [1, 2, 3, 4, 5, 6]
sample_means = []
for x in range(100):
    sample = np.random.choice(a=dice, size=100)
    sample_means.append(sample.mean())

df = pd.DataFrame(sample_means)
df.plot(kind="density")
plt.show()

print("------------------------------------------------------------")  # 60個

dice = [1, 2, 3, 4, 5, 6]
population = []
for x in range(10000):
    sample = np.random.choice(a=dice, size=100)
    population.append(sample.mean())
print("母體平均數:", sum(population) / 10000.0)

size_range = [10, 100, 1000]
for sample_size in size_range:
    sample = np.random.choice(a=population, size=sample_size)
    sample_mean = sample.mean()
    print(sample_size, "樣本平均數:", sample_mean)

print("------------------------------------------------------------")  # 60個

population = (
    (["臺灣閩南語"] * 7330) + (["臺灣客家語"] * 1200) + (["其他漢語方言"] * 1300) + (["原住民語"] * 170)
)
sample_size = 1000
sample = random.sample(population, sample_size)
for lang in set(sample):
    print(lang + "比例估計:", sample.count(lang) / sample_size)

print("------------------------------------------------------------")  # 60個

voter_gender = np.array((["男"] * 352) + (["男"] * 315) + (["女"] * 217) + (["女"] * 331))
voter_favorite = np.array(
    (["喜歡"] * 352) + (["不喜歡"] * 315) + (["喜歡"] * 217) + (["不喜歡"] * 331)
)
voters = pd.DataFrame({"gender": voter_gender, "favorite": voter_favorite})
voter_tab = pd.crosstab(voters.gender, voters.favorite, margins=True)
voter_tab.columns = ["喜歡", "不喜歡", "小計"]
voter_tab.index = ["男", "女", "小計"]
observed = voter_tab.iloc[0:3, 0:3]
print(observed)

print("------------------------------------------------------------")  # 60個

voter_gender = np.array((["男"] * 352) + (["男"] * 315) + (["女"] * 217) + (["女"] * 331))
voter_favorite = np.array(
    (["喜歡"] * 352) + (["不喜歡"] * 315) + (["喜歡"] * 217) + (["不喜歡"] * 331)
)
voters = pd.DataFrame({"gender": voter_gender, "favorite": voter_favorite})
voter_tab = pd.crosstab(voters.gender, voters.favorite, margins=True)
voter_tab.columns = ["喜歡", "不喜歡", "小計"]
voter_tab.index = ["男", "女", "小計"]
observed = voter_tab.iloc[0:3, 0:3]
print(observed)
print("---------------------------")
expected = np.outer(voter_tab["小計"][0:2], voter_tab.loc["小計"][0:2]) / 1215
expected = pd.DataFrame(expected)
expected.columns = ["喜歡", "不喜歡"]
expected.index = ["男", "女"]
print(expected)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
