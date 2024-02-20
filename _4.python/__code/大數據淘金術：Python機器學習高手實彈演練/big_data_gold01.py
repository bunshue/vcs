import sys

import pandas as pd

print('------------------------------------------------------------')	#60個

# 索引
df = pd.DataFrame({"a":[1,3], "b":[2,4]}, index=['line1', 'line2'])
print(df.index) # 顯示行索引
print(df.columns) # 顯示列索引

print('------------------------------------------------------------')	#60個

# 多重索引
df = pd.read_excel('data/test.xlsx', header=[0,1]) # 指定前兩行爲列索引
print(df)
print(df.columns.values) # 查看列索引內容

df.columns = ['_'.join(col).strip() for col in df.columns.values] # 重置字段名
print(df)

print('------------------------------------------------------------')	#60個

# Python日期時間處理
# 時間點
from datetime import datetime

d1 = datetime.now() # 獲取當前時間
print(d1)
print(d1.year, d1.month, d1.day, d1.hour, d1.minute, d1.second)
d2 = datetime(2019, 3, 27) # 通過指定日期構造datetime
print(d2)

# 時間段
from datetime import timedelta
delta = d2-d1 # 通過時間日期相減獲取
print(type(delta))
print(delta)
delta = timedelta(days=3) # 通過指定時定差獲取
print(d1+delta)# 利用時間段計算新日期時間

# 時間戳

import time
print(time.time())

d = datetime.now()
t = time.mktime(d.timetuple()) # 從datetime格式轉換
print(t)
print(time.mktime(time.strptime("2019-03-27", "%Y-%m-%d"))) # 從字符串轉換
print(datetime.fromtimestamp(t)) 
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t)))


# 時間類型轉換
d = datetime.strptime('2019-03-27', '%Y-%m-%d')
print(d)

from dateutil.parser import parse
d = parse('2019/03/27')
print(d)
print(str(d))

print(d.strftime("%Y/%m/%d %H:%M:%S"))

print('------------------------------------------------------------')	#60個

# Pandas日期時間處理
# 時間點TimeStamp

t = pd.to_datetime('2019-03-01 00:00:00') # 從字符串轉換
print(type(t), t)
t = pd.to_datetime(datetime.now()) # 從datetime格式轉換
print(type(t), t)

# 時間間隔
t1 = pd.to_datetime('2019-03-01 00:00:00')
t2 = pd.to_datetime(datetime.now())
delta = t2-t1 # 通過TimeStamp相減獲取
print(type(delta), delta, delta.days, delta.seconds)

delta = pd.Timedelta(days=27) # 構造時間間隔爲27天
print(t2 + delta)

# 時間段Period
t = pd.to_datetime(datetime.now())
p = pd.Period(t, freq='H')
print(p, p.start_time, p.end_time) # 顯示時間段起止時間

# 批量轉換
arr = ['2019-03-01','2019-03-02','2019-03-03']
df = pd.DataFrame({'d':arr})
df['d'] = pd.to_datetime(df['d'])
print(df)

print('------------------------------------------------------------')	#60個

# 時間序列操作
# 時間日期類型索引
df.index = pd.to_datetime(df['d']) # 本例中使用了上例中構造的df[‘d’]
print(df.index)

df = pd.DataFrame()
df['date'] = pd.date_range(start='2017-12-30',end='2019-01-05',freq='d') # 創建時間數據
df['val'] = df['date'].apply(lambda x: x.weekday()) # 計算該日是星期幾
df.set_index('date', inplace = True) # 設置時間索引
print(df.head(3)) # 顯示前三條

# 時間段類型索引
df_period = df.to_period(freq='M') # 按月創建時間段
print(type(df_period.index)) # 查看類型
print(len(df_period)) # 查看記錄個數，與原記錄個數一致
print(df_period.head(3))

print(df_period.index[0].start_time, df_period.index[0].end_time)
print(df_period.index[1].start_time, df_period.index[1].end_time)
print(df.index.is_unique, df_period.index.is_unique)

df_dt = df_period.to_timestamp()
print(df_dt.head(3))
print(type(df_dt.index))

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個

# 時區轉換

import pytz
print('時區個數 :', len(pytz.common_timezones))
print('前3個 :', pytz.common_timezones[:3])

import datetime
t = datetime.datetime.now()
print(t)

utc_dt = pytz.utc.localize(t)
print(utc_dt)

from pytz import timezone
tz = timezone('Asia/Shanghai') # 將時區設爲上海
print(utc_dt.astimezone(tz)) # 轉換時區

df = pd.DataFrame()
df['date'] = pd.date_range(start='2018-12-31',end='2019-01-01',freq='d')
df.set_index('date', inplace=True) # 設置時間索引
print(df.index)

df.index = df.index.tz_localize('UTC')
print(df.index.values, df.index)

df.index = df.index.tz_convert('Asia/Shanghai')
print(df.index.values)
print(df.index)

print('------------------------------------------------------------')	#60個

# 數據重排
# 數據錶轉置
df = pd.DataFrame({"a":[1,2],"b":[3,4]}, index=['l1','l2'])
print(df)
print(df.T)

# 行轉列和列轉行
df1 = df.stack() # 列轉行
print(df1)

print(df1.unstack()) # 將內層行索引轉爲列索引
print(df1.unstack(level=0)) # 將外層行索引轉爲列索引

# 透視轉換
df = pd.DataFrame({"時間":['期中','期末','期中','期末'],
                   "學科":['語文','語文','數學','數學'],
                   "分數":[89,75,90,95]})
df1 = df.pivot(index='時間', columns='學科', values='分數')
print(df, df1)

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個




