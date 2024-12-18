"""
pandas 時間相關
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

# # Pandas的时间序列处理

from datetime import datetime
import pandas as pd
import numpy as np

# 指定index为datetime的list
date_list = [
    datetime(2017, 2, 18),
    datetime(2017, 2, 19),
    datetime(2017, 2, 25),
    datetime(2017, 2, 26),
    datetime(2017, 3, 4),
    datetime(2017, 3, 5),
]
time_s = pd.Series(np.random.randn(6), index=date_list)
print(time_s)
print(type(time_s.index))

print("------------------------------------------------------------")  # 60個

# pd.date_range()
dates = pd.date_range("2017-02-18", periods=5, freq="W-SAT")  # 起始日期  # 周期  # 频率
print(dates)
print(pd.Series(np.random.randn(5), index=dates))

print("------------------------------------------------------------")  # 60個

# 索引

# 索引位置
print(time_s[0])

# 索引值
print(time_s[datetime(2017, 2, 18)])

# 可以被解析的日期字符串
print(time_s["2017/02/18"])


# 按“年份”、“月份”索引
print(time_s["2017-2"])

# 切片操作
print(time_s["2017-2-26":])

cc = time_s.truncate(before="2017-2-25")
print(cc)

cc = time_s.truncate(after="2017-2-25")
print(cc)

# ## 生成日期范围

# 传入开始、结束日期，默认生成的该时间段的时间点是按天计算的
date_index = pd.date_range("2017/02/18", "2017/03/18")
print(date_index)

# 只传入开始或结束日期，还需要传入时间段
print(pd.date_range(start="2017/02/18", periods=10))

print(pd.date_range(end="2017/03/18", periods=10))

# 规范化时间戳
print(pd.date_range(start="2017/02/18 12:13:14", periods=10))
print(pd.date_range(start="2017/02/18 12:13:14", periods=10, normalize=True))

# ## 频率与偏移量

print(pd.date_range("2017/02/18", "2017/03/18", freq="2D"))

# 偏移量通过加法连接
sum_offset = pd.tseries.offsets.Week(2) + pd.tseries.offsets.Hour(12)
print(sum_offset)

print(pd.date_range("2017/02/18", "2017/03/18", freq=sum_offset))

# ## 移动数据

ts = pd.Series(
    np.random.randn(5), index=pd.date_range("20170218", periods=5, freq="W-SAT")
)
print(ts)

print(ts.shift(1, freq="2D"))
print(ts.shift(-1))

print("------------------------------------------------------------")  # 60個

# # 时间数据重采样

# ## resample

import pandas as pd
import numpy as np

date_rng = pd.date_range("20170101", periods=100, freq="D")
ser_obj = pd.Series(range(len(date_rng)), index=date_rng)
print(ser_obj.head(10))


# In[2]:


# 统计每个月的数据总和
resample_month_sum = ser_obj.resample("M").sum()
# 统计每个月的数据平均
resample_month_mean = ser_obj.resample("M").mean()

print("按月求和：", resample_month_sum)
print("按月求均值：", resample_month_mean)


# ## 降采样

# In[3]:


# 将数据聚合到5天的频率
five_day_sum_sample = ser_obj.resample("5D").sum()
five_day_mean_sample = ser_obj.resample("5D").mean()
five_day_ohlc_sample = ser_obj.resample("5D").ohlc()

print("降采样，sum")
print(five_day_sum_sample)


# In[4]:


print("降采样，mean")
print(five_day_mean_sample)


# In[6]:


# 使用groupby降采样
print(ser_obj.groupby(lambda x: x.month).sum())

print(ser_obj.groupby(lambda x: x.weekday).sum())

# ## 升采样

df = pd.DataFrame(
    np.random.randn(5, 3),
    index=pd.date_range("20170101", periods=5, freq="W-MON"),
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

# # 时间序列数据统计—滑动窗口
# ## 窗口函数

import pandas as pd
import numpy as np

ser_obj = pd.Series(
    np.random.randn(1000), index=pd.date_range("20170101", periods=1000)
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

# 画图查看
import matplotlib.pyplot as plt

plt.figure(figsize=(15, 5))

ser_obj.plot(style="r--")
ser_obj.rolling(window=10).mean().plot(style="b")

plt.show()

# In[7]:


print(ser_obj.rolling(window=5, center=True).mean())
# %%


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# pd之時間相關


print("Series 也有to_csv方法")
dates = pd.date_range("1/1/2000", periods=7)
print(dates)

"""
DatetimeIndex(['2000-01-01', '2000-01-02', '2000-01-03', '2000-01-04',
               '2000-01-05', '2000-01-06', '2000-01-07'],
              dtype='datetime64[ns]', freq='D')
"""

print("------------------------------------------------------------")  # 60個


yyyymmdd = "20240101"
DAYS = 366
datas = np.random.randn(DAYS, 4)
index = pd.date_range(yyyymmdd, periods=DAYS)
print("從", yyyymmdd, "開始的", DAYS, "天\n", index)
df = pd.DataFrame(datas, index=index, columns=list("ABCD"))
df = df.cumsum()

df.plot(title="線圖")  # 無參數, 預設就是 line

plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

dates = pd.date_range("20130101", periods=6)


dates = pd.date_range("20130101", periods=6)
print(dates)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

"""
for i in pd.date_range(start=start, end=end, freq='1D'):

def random_timestamps(start, end, freq, count):
    index = pd.date_range(start, end, freq=freq)
    locations = np.random.choice(np.arange(len(index)), size=count, replace=False)
    locations.sort()
    return index[locations]

ts_index = random_timestamps("2015-01-01", "2015-10-01", freq="Min", count=5)
pd_index = ts_index.to_period("M")
td_index = pd.TimedeltaIndex(np.diff(ts_index))



dates = pd.date_range(start='2003-01-01', freq='MS', periods=len(sales_data))

"""
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
