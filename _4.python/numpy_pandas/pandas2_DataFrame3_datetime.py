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

print("------------------------------------------------------------")  # 60個
# pd.date_range()  # 生成日期范围 ST
print("------------------------------------------------------------")  # 60個

dates = pd.date_range("12/18/2024", periods=5)  # 沒寫就是start
print('從某天開始後的5天 :\n', dates)

dates = pd.date_range("20241218", periods=5)
print('從某天開始後的5天 :\n', dates)

dates = pd.date_range(start="2024/12/18", periods=5)
print('生成日期範圍 start:\n', dates)

dates = pd.date_range(end="2024/12/18", periods=5)
print('生成日期範圍 end:\n', dates)

# 传入开始、结束日期，默认生成的该时间段的时间点是按天计算的
dates = pd.date_range("2024/12/18", "2024/12/25")
print('生成日期範圍 start-end:\n', dates)

dates = pd.date_range("2024-12-18", periods=5, freq="W-SAT")  # 起始日期  # 周期  # 频率
print('從某天開始後的5個週六 :\n', dates)

s = pd.Series(np.random.randn(5), index=dates)
print(type(s))
print(s)

dates = pd.date_range(start="2024/12/18 12:13:14", periods=5)
print('無規範化 生成日期範圍 :\n', dates)

dates = pd.date_range(start="2024/12/18 12:13:14", periods=5, normalize=True)
print('有規範化 生成日期範圍 :\n', dates)

# 频率与偏移量
dates = pd.date_range("2024/11/18", "2024/12/18", freq="2D")
print('生成日期範圍 每隔2天:\n', dates)

# 偏移量通过加法连接
sum_offset = pd.tseries.offsets.Week(2) + pd.tseries.offsets.Hour(12)
print("偏移量 :", sum_offset)
dates = pd.date_range("2024/10/18", "2024/12/18", freq=sum_offset)
print('生成日期範圍 start-end 每隔一個偏移量:\n', dates)

start = "2024/12/18"
end = "2024/12/25"
for d in pd.date_range(start=start, end=end, freq='1D'):
    print(d)

dates = pd.date_range(start='2024-01-15', freq='M', periods=5)
print('生成日期範圍 每隔1月 月底:\n', dates)

dates = pd.date_range(start='2024-01-15', freq='MS', periods=5)
print('生成日期範圍 每隔1月 月初:\n', dates)

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

#plt.show()

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

#plt.show()

print(ser_obj.rolling(window=5, center=True).mean())

print("------------------------------------------------------------")  # 60個


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
