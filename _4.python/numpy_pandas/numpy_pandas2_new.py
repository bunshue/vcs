"""
numpy pandas 新進

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
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

print("------------------------------------------------------------")  # 60個
print("numpy")
print("------------------------------------------------------------")  # 60個

a = np.array([2,3,4,5,6])
print(f'a = {a}')
b = np.ma.masked_where(a > 3, a)
print(f'b = {b}')

print('------------------------------------------------------------')	#60個


print(np.c_[np.array([1, 2, 3]), np.array([4, 5, 6])])
print(np.c_[np.array([[1, 2, 3]]), 0, 0, np.array([[4, 5, 6]])])

"""
array([[1, 4],
       [2, 5],
       [3, 6]])
"""

#array([[1, 2, 3, ..., 4, 5, 6]])

print('------------------------------------------------------------')	#60個

#numpy.c_() and numpy.r_()的用法


#####np.c_是按行连接两个矩阵，就是把两矩阵左右相加，要求行数相等，类似于pandas中的merge()。
#####np.r_是按列连接两个矩阵，就是把两矩阵上下相加，要求列数相等，类似于pandas中的concat()。

#np.c_是按行连接两个矩阵，就是把两矩阵左右相加，要求行数相等。
#np.r_是按列连接两个矩阵，就是把两矩阵上下相加，要求列数相等。


#1.numpy.c_:

x = np.arange(12).reshape(3,4)
print('x:',x, x.shape)

y = np.arange(10,22).reshape(3,4)
print('y:',y, y.shape)

z = np.c_[x,y]
print('z:',z, z.shape)

#2.numpy.r_用法:

x = np.arange(12).reshape(3,4)
print('x:',x, x.shape)

y = np.arange(10,22).reshape(3,4)
print('y:',y, y.shape)

z = np.r_[x,y]
print('z:',z, z.shape)

print("------------------------------------------------------------")  # 60個

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(type(x))

print("------------------------------------------------------------")  # 60個

print("二維陣列 6 X 4")
a = np.array(
    [[0, 0, 0, 1], [1, 1, 1, 2], [2, 2, 2, 3], [3, 3, 3, 4], [4, 4, 4, 5], [5, 5, 5, 6]]
)
print(a)
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.nbytes)

print("第3列 之 第1~4項(不含尾)")
print(a[3, 1:4])

print("前2列 之 第2欄之後")
print(a[:2, 2:])

print("第2列 之 全部")
print(a[2, :])

print("全部列 之 第3欄, 轉成row")
print(a[:, 3])

print("全部列 之 偶數欄")
print(a[:, ::2])

print("偶數列 之 036欄")
print(a[::2, ::3])

# axis = 0 : 第0維 直行
# axis = 1 : 第1維 橫列
print("全部和:", a.sum())
print("直行加:", a.sum(axis=0))
print("橫列加:", a.sum(axis=1))

# np.argmin()求最小值對應的索引
# np.argmax()求最大值對應的索引

print("每個直行的最小值:", a.min(axis=0))
print("每個直行的最小值對應的索引:", a.argmin(axis=0))
print("每個直行的標準差:", a.std(axis=0))

print("全部平均:", a.mean())
print("直行平均:", a.mean(axis=0))
print("橫列平均:", a.mean(axis=1))

print("------------------------------------------------------------")  # 60個

print("一維陣列 10個元素")
a = np.arange(10)
print(a)

print("前4項")
print(a[:4])

print("第3項 至 第7項(不含尾)")
print(a[3:7])

print("第5項 至 最後")
print(a[5:])

print("第3至第9項 跳一個")
print(a[3:9:2])

print("第2項開始至最後, 跳一個")
print(a[2::2])

print("從頭至最後, 跳二個")
print(a[::3])

print("------------------------------------------------------------")  # 60個

print("使用 numpy函數 對 list做處理")

x = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 0]

print(np.max(x))
print(np.mean(x))
print(np.min(x))

print("------------------------------------------------------------")  # 60個

print("用numpy建立資料")
a = np.arange(5)
print(a)
a = np.arange(2,5,1)
print(a)
a = np.linspace(2,5,4)
print(a)
a = np.logspace(0,2,5)
print(a)

a = np.empty(5) # 生成5個元素，值爲隨機數的數組（速度快）
print(a)
a = np.zeros(5) # 生成5個值全爲0的數組
print(a)
a = np.ones(5) # 生成5個值全爲1的數組
print(a)
a = np.full(5, 6) # 生成5個值全爲6的數組
print(a)

print("------------------------------------------------------------")  # 60個

a = np.array([1,2,3,4,5,6], dtype=np.int64)
print(a.dtype) 
a = a.astype(np.float32)
print(a.dtype) 
print(a.dtype.type)

print("------------------------------------------------------------")  # 60個

print("分段函數")

x=np.arange(10)
print(x)

print(np.where(x<5, x, 9-x))


a=np.arange(10)
print(np.select([x<3,x>6], [-1,1], 0))


a=np.arange(10)
print(np.piecewise(x, [x<3,x>6], [lambda x: x * 2, lambda x: x * 3]))

print("------------------------------------------------------------")  # 60個

print("矩陣與二維數組")
a = np.mat(np.mat([[1,2,3],[4,5,6]]))
print(type(a))

print(np.eye(2))
print(np.diag([2,3]))

a = np.mat([[1.,2.],[3.,4.]])
print(np.dot(a,a))    # 矩陣乘積
print(np.multiply(a,a))    # 矩陣點乘
print(a.T)   # 矩陣轉置
print(a.I)   # 矩陣求逆
print(np.trace(a))    # 求矩陣的跡
print(np.linalg.eig(a))   # 特徵分解

a = np.mat(np.mat([[1,2,3],[4,5,6]]))
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

filename = "data/python_ReadWrite_CSV6_score.csv"

dat = pd.read_csv(filename, encoding="UTF-8")

print(dat.head())

print("數學平均", np.mean(dat["數學"]))
print("數學中位數", np.median(dat["數學"]))

print("------------------------------------------------------------")  # 60­э



print("------------------------------------------------------------")  # 60­э

import numpy as np

a = np.array([1, 2, 3])   # Create a rank 1 array
print(type(a))            # Prints "<type 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)"
print(a[0], a[1], a[2])   # Prints "1 2 3"
a[0] = 5                  # Change an element of the array
print(a)                  # Prints "[5, 2, 3]"
b = np.array([[1,2,3],[4,5,6]])   # Create a rank 2 array
print(b.shape)                     # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])   # Prints "1 2 4"

print('------------------------------------------------------------')	#60個

a = np.zeros((2,2))
print(a) # Prints "[[ 0. 0.]
# [0. 0.]]"

b = np.ones((1,2)) # Create an array of all ones
print(b) # Prints "[[ 1. 1.]]"

c = np.full((2,2), 7) # Create a constant array
print(c)

d = np.eye(3)
print(d)

print('------------------------------------------------------------')	#60個

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
b= a[0:2,1:3]         # 定義b為a 的部分資料
#b= a[0:2,1:3].copy() # 複製b為a 的部分資料
print(b)              #輸出[[2 3], [6 7]]
b[0, 0] = 99          # 修改b的局部資料
print(b)              #輸出[[99  3], [ 6  7]]
print(a)              # 輸出[[ 1 99  3  4],[ 5  6  7  8],[ 9 10 11 12]]

print('------------------------------------------------------------')	#60個

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
row_r1 = a[1, :]
row_r2 = a[1:2, :]
print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)
print(col_r2, col_r2.shape)

print('------------------------------------------------------------')	#60個

a = np.array([[1,2], [3, 4], [5, 6]])
print(a[0, 0])
print(a[1, 1])
b=[a[0, 0], a[1, 1]];
print(b)
b=a[[0, 0], [1, 1]];
print(b)
print(b[1])
print(a[[0,1,2], [0,1,0]])

print('------------------------------------------------------------')	#60個

x = np.array([1, 2])  #numpy自動設定
print(x.dtype)         # 輸出 "int64"
x = np.array([1.0, 2.0])  #numpy自動設定
print(x.dtype)             # 輸出 "float64"
x = np.array([1, 2], dtype=np.int64)  #設定為int64
print(x.dtype)                         # 輸出 "int64"

print('------------------------------------------------------------')	#60個

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
v = np.array([9, 10], dtype=np.float64)

# 加法
print(x + y)        # 輸出 [[ 6.0  8.0] [10.0 12.0]]
print(np.add(x, y)) # 輸出 [[ 6.0  8.0] [10.0 12.0]]
print(x + 10)       # 輸出 [[11. 12.] [13. 14.]]
# 減法
print(x - y)        # 輸出 [[-4.0 -4.0] [-4.0 -4.0]]
print(np.subtract(x, y)) # 輸出 [[-4.0 -4.0] [-4.0 -4.0]]
print(x -[1,2])     # 輸出 [[0. 0.]  [2. 2.]]
# 乘法
print(x * y)
print(np.multiply(x, y)) # 輸出  [[ 5.0 12.0][21.0 32.0]]
# 除法
print(x / y)
print(np.divide(x, y))# 輸出 [[ 0.2  0.33333333] [ 0.42857143  0.5]]
# 平方
print(x **2)
print(np.sqrt(x))# 輸出[[ 1. 1.41421356] [ 1.73205081  2.]]

#矩陣乘法，兩個數組的點積 Dot product
print(x.dot(y))# 輸出         [[19. 22.] [43. 50.]]
print(np.dot(x, y))   # [[5+14 , 6+16] []]

print('------------------------------------------------------------')	#60個

x = np.array([[-1,2,3],[13,14,15]])
print(x)
print(np.sum(x))       # 輸出46   全部累加
print(np.sum(x, axis=0))  # 輸出"[12 16 18]" =(-1+13),(2+14),(3+15)
print(np.sum(x, axis=1))  # 輸出"[ 4 42]" =(-1+2+3),(13+14+15)
print(np.max(x))       #最大值 輸出15
print(np.min(x))       #最小值 輸出-1
print(np.cumsum(x))    # 累加[-1  1  4 17 31 46]
# 加權平均值
print(np.average(x))   # 輸出7.666
# 平均 mean=sum(x)/len(x)
print(np.mean(x))      # 輸出7.666
# 中間值
print(np.median(x))   # 輸出8.0
# 標準偏差 std = sqrt(mean(abs(x - x.mean())**2))
print(np.std(x))       # 輸出 6.472
# 方差 var = mean(abs(x - x.mean())**2)
print(np.var(x))       # 輸出 41.888
print(x.T)       # 輸出 [[-1 13] [ 2 14] [ 3 15]]

print('------------------------------------------------------------')	#60個

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
bool_idx =  ((a % 2)==0)
print(bool_idx)
print(a[bool_idx])
print(a[a > 10])
print(a[a%2==1]*10)

print('------------------------------------------------------------')	#60個

#方法1
x = np.array([[1,2,3], [4,5,6]])
v = np.array([1, 0, 1])
y = np.empty_like(x)
for i in range(2):
    y[i, :] = x[i, :] + v
print(y)    #輸出[[2 2 4][5 5 7]]

#方法2
v2 = np.tile(v, (2, 1))
print(v2)   #輸出[[1 0 1][1 0 1]]
print(x+v2) #輸出[[2 2 4] [5 5 7]]

#方法3
print(x+v)  #輸出[[2 2 4] [5 5 7]]

print('------------------------------------------------------------')	#60個


import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a[0], b[1])

a = np.append(a, b)
print(a)

d = a[1]
print(d)

a2 = np.delete(a, 1)
print(a2)
a3 = np.insert(a, 1, d)
print(a3)

print("------------------------------------------------------------")  # 60個

# 一維
a = np.array([1, 2, 3])
print(a)

# 二維
b = np.array([[1, 2, 3], [5, 6, 7]])
print(b)

# 二維，使用 dtype 定義數據類型
bb = np.array([[1, 2, 3], [5, 6, 7]], dtype=float)
print(bb)

# 最小維度
c = np.array([1, 2, 3], ndmin=3)
print(c)


print("------------------------------------------------------------")  # 60個

a = np.array([[[1, 2, 3], [5, 6, 7]]])

# 取得陣列維度的深度
print(np.ndim(a))

# 依序取得每個維度的數量
print(np.shape(a))

# 修改維度 1,2,3 -> 1,3,2
a.shape = (1, 3, 2)
print(a)

# 也可以使用 reshape，不過不知道為什麼用了之後執行沒問題，但編輯器會報錯
# b = a.reshape(1,2,3)
# print(b)

print("------------------------------------------------------------")  # 60個

# 複製數據
a = [1, 2, 3]
b = np.asarray(a)
c = a
a = [4, 5, 6]
d = np.asarray(a, dtype=float)
print(a)  # [4, 5, 6]
print(b)  # [1 2 3]
print(c)  # [1, 2, 3]
print(d)  # [4. 5. 6.]

# 產生數據
x = np.arange(5, dtype=float)
print(x)  # [0. 1. 2. 3. 4.]
x2 = np.arange(0, 10, 2)
print(x2)  # [0 2 4 6 8]

# 使用 linspace 產生數據
y = np.linspace(1, 10, 10, dtype=int)
print(y)  # [ 1  2  3  4  5  6  7  8  9 10]
y2 = np.linspace(1, 2, 10)
print(y2)
# [1. 1.11111111 1.22222222 1.33333333 1.44444444 1.55555556 1.66666667 1.77777778 1.88888889 2.]

print("------------------------------------------------------------")  # 60個


print('------------------------------------------------------------')	#60個

# Make the graphs a bit prettier, and bigger
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

print('------------------------------------------------------------')	#60個

broken_df = pd.read_csv('data/bikes.csv', encoding = "ISO-8859-1")

# Look at the first 3 rows
print(broken_df[:3])

print('------------------------------------------------------------')	#60個

fixed_df = pd.read_csv('data/bikes.csv', sep = ';', encoding = 'latin1', parse_dates = ['Date'], dayfirst=True, index_col='Date')
print(fixed_df[:3])

print(fixed_df['Berri 1'])

fixed_df['Berri 1'].plot()

plt.show()


fixed_df.plot(figsize=(15, 10))

plt.show()

print('------------------------------------------------------------')	#60個

df = pd.read_csv('data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
df['Berri 1'].plot()

plt.show()

print('------------------------------------------------------------')	#60個

# Make the graphs a bit prettier, and bigger
plt.style.use('ggplot')

# This is necessary to show lots of columns in pandas 0.12. 
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)

plt.rcParams['figure.figsize'] = (15, 5)

# because of mixed types we specify dtype to prevent any errors
complaints = pd.read_csv('data/311-service-requests.csv', dtype='unicode')

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
complaints = pd.read_csv('data/311-service-requests.csv', dtype='unicode')

is_noise = complaints['Complaint Type'] == "Noise - Street/Sidewalk"
noise_complaints = complaints[is_noise]
noise_complaints['Borough'].value_counts()

noise_complaint_counts = noise_complaints['Borough'].value_counts()
complaint_counts = complaints['Borough'].value_counts()

noise_complaint_counts / complaint_counts

noise_complaint_counts / complaint_counts.astype(float)

(noise_complaint_counts / complaint_counts.astype(float)).plot(kind='bar')

plt.show()

print('------------------------------------------------------------')	#60個

# Make the graphs a bit prettier, and bigger
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)
plt.rcParams['font.family'] = 'sans-serif'

# This is necessary to show lots of columns in pandas 0.12. 
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)


bikes = pd.read_csv('data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
bikes['Berri 1'].plot()
plt.show()


berri_bikes = bikes[['Berri 1']].copy()


berri_bikes[:5]



berri_bikes.index


berri_bikes.index.day

berri_bikes.index.weekday

berri_bikes.loc[:,'weekday'] = berri_bikes.index.weekday
berri_bikes[:5]


weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)
weekday_counts

weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_counts


weekday_counts.plot(kind='bar')

plt.show()

print('------------------------------------------------------------')	#60個

bikes = pd.read_csv('data/bikes.csv', 
                    sep=';', encoding='latin1', 
                    parse_dates=['Date'], dayfirst=True, 
                    index_col='Date')
# Add the weekday column
berri_bikes = bikes[['Berri 1']].copy()
berri_bikes.loc[:,'weekday'] = berri_bikes.index.weekday

# Add up the number of cyclists by weekday, and plot!
weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)
weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekday_counts.plot(kind='bar')


plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'

#Canada's weather data for 2012, and saved it to a CSV.
#Here's the temperature every hour for 2012!

weather_2012_final = pd.read_csv('data/weather_2012.csv', index_col='Date/Time')
weather_2012_final['Temp (C)'].plot(figsize=(15, 6))

plt.show()

print('------------------------------------------------------------')	#60個

#Here's an URL template you can use to get data in Montreal.
url_template = "http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"

#To get the data for March 2013, we need to format it with month=3, year=2012.
#url = url_template.format(month=3, year=2012)
#weather_mar2012 = pd.read_csv(url, skiprows=15, index_col='Date/Time', parse_dates=True, encoding='latin1', header=True)

# because the url is broken, we use our saved dataframe for now
weather_mar2012 = pd.read_csv('data/weather_2012.csv')

print(weather_mar2012)


weather_mar2012[u"Temp (C)"].plot(figsize=(15, 5))
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

weather_mar2012 = weather_mar2012.dropna(axis=1, how='any')
print(weather_mar2012[:5])

print('------------------------------------------------------------')	#60個

#fail
#weather_mar2012 = weather_mar2012.drop(['Year', 'Month', 'Day', 'Time', 'Data Quality'], axis=1)
#print(weather_mar2012[:5])

print('------------------------------------------------------------')	#60個


#Plotting the temperature by hour of day

"""fail
temperatures = weather_mar2012[[u'Temp (C)']].copy()
print(temperatures.head)
temperatures.loc[:,'Hour'] = weather_mar2012.index.hour
temperatures.groupby('Hour').aggregate(np.median).plot()

plt.show()
"""

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

import numpy as np

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 3)
plt.rcParams['font.family'] = 'sans-serif'

weather_2012 = pd.read_csv('data/weather_2012.csv', parse_dates=True, index_col='Date/Time')
print(weather_2012[:5])

weather_description = weather_2012['Weather']
is_snowing = weather_description.str.contains('Snow')

# Not super useful
print(is_snowing[:5])

# More useful!
is_snowing=is_snowing.astype(float)
is_snowing.plot()

plt.show()

print('------------------------------------------------------------')	#60個

#Use resampling to find the snowiest month

#If we wanted the median temperature each month, we could use the resample() method like this:

weather_2012['Temp (C)'].resample('M').apply(np.median).plot(kind='bar')

plt.show()

print('------------------------------------------------------------')	#60個


print(is_snowing.astype(float)[:10])





print('------------------------------------------------------------')	#60個

print(is_snowing.astype(float).resample('M').apply(np.mean))

is_snowing.astype(float).resample('M').apply(np.mean).plot(kind='bar')

plt.show()

print('------------------------------------------------------------')	#60個

#Plotting temperature and snowiness stats together

temperature = weather_2012['Temp (C)'].resample('M').apply(np.median)
is_snowing = weather_2012['Weather'].str.contains('Snow')
snowiness = is_snowing.astype(float).resample('M').apply(np.mean)

# Name the columns
temperature.name = "Temperature"
snowiness.name = "Snowiness"

#We'll use concat again to combine the two statistics into a single dataframe.
stats = pd.concat([temperature, snowiness], axis=1)
print(stats)

stats.plot(kind='bar')
plt.show()

#Uh, that didn't work so well because the scale was wrong. We can do better by plotting them on two separate graphs:

stats.plot(kind='bar', subplots=True, figsize=(15, 10))
plt.show()

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Make the graphs a bit prettier, and bigger
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)
plt.rcParams['font.family'] = 'sans-serif'

# This is necessary to show lots of columns in pandas 0.12. 
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)

print('------------------------------------------------------------')	#60個


#NYC 311 service request dataset
requests = pd.read_csv('data/311-service-requests.csv', dtype='unicode')

cc = requests['Incident Zip'].unique()
print(cc)


print('------------------------------------------------------------')	#60個

#Fixing the nan values and string/float confusion

na_values = ['NO CLUE', 'N/A', '0']
requests = pd.read_csv('data/311-service-requests.csv', na_values=na_values, dtype={'Incident Zip': str})

cc = requests['Incident Zip'].unique()
print(cc)


#What's up with the dashes?

rows_with_dashes = requests['Incident Zip'].str.contains('-').fillna(False)
cc = len(requests[rows_with_dashes])
print(cc)

print(requests[rows_with_dashes])

#But then my friend Dave pointed out that 9-digit zip codes are normal.
#Let's look at all the zip codes with more than 5 digits, make sure they're okay, and then truncate them.
long_zip_codes = requests['Incident Zip'].str.len() > 5
cc = requests['Incident Zip'][long_zip_codes].unique()
print(cc)


requests['Incident Zip'] = requests['Incident Zip'].str.slice(0, 5)

#Earlier I thought 00083 was a broken zip code, but turns out Central Park's zip code 00083!
#Shows what I know. I'm still concerned about the 00000 zip codes, though: let's look at that.
cc = requests[requests['Incident Zip'] == '00000']
print(cc)


zero_zips = requests['Incident Zip'] == '00000'
requests.loc[zero_zips, 'Incident Zip'] = np.nan

""" fail
unique_zips = requests['Incident Zip'].unique()
unique_zips.sort()
cc = unique_zips
print(cc)
"""
zips = requests['Incident Zip']
# Let's say the zips starting with '0' and '1' are okay, for now. (this isn't actually true -- 13221 is in Syracuse, and why?)
is_close = zips.str.startswith('0') | zips.str.startswith('1')
# There are a bunch of NaNs, but we're not interested in them right now, so we'll say they're False
is_far = ~(is_close) & zips.notnull()

cc = zips[is_far]
print(cc)

cc = requests[is_far][['Incident Zip', 'Descriptor', 'City']].sort_values('Incident Zip')
print(cc)

cc = requests['City'].str.upper().value_counts()
print(cc)

print('------------------------------------------------------------')	#60個

#Putting it together

na_values = ['NO CLUE', 'N/A', '0']
requests = pd.read_csv('data/311-service-requests.csv', 
                       na_values=na_values, 
                       dtype={'Incident Zip': str})

def fix_zip_codes(zips):
    # Truncate everything to length 5 
    zips = zips.str.slice(0, 5)
    
    # Set 00000 zip codes to nan
    zero_zips = zips == '00000'
    zips[zero_zips] = np.nan
    
    return zips

requests['Incident Zip'] = fix_zip_codes(requests['Incident Zip'])

cc = requests['Incident Zip'].unique()
print(cc)





print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

#Parsing Unix timestamps

# Read it, and remove the last row
popcon = pd.read_csv('data/popularity-contest', sep=' ', )[:-1]
popcon.columns = ['atime', 'ctime', 'package-name', 'mru-program', 'tag']

print(popcon[:5])

popcon['atime'] = popcon['atime'].astype(int)
popcon['ctime'] = popcon['ctime'].astype(int)

popcon['atime'] = pd.to_datetime(popcon['atime'], unit='s')
popcon['ctime'] = pd.to_datetime(popcon['ctime'], unit='s')

print(popcon['atime'].dtype)


print(popcon[:5])

print('------------------------------------------------------------')	#60個

popcon = popcon[popcon['atime'] > '1970-01-01']

#不包含lib的
nonlibraries = popcon[~popcon['package-name'].str.contains('lib')]

cc = nonlibraries.sort_values('ctime', ascending=False)[:10]
print(cc)



print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

#Reading data from SQL databases
import pandas as pd
import sqlite3

con = sqlite3.connect("data/weather_2012.sqlite")
df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con)
print(df)

print('------------------------------------------------------------')	#60個

df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con, index_col='id')
print(df)

print('------------------------------------------------------------')	#60個

df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con, 
                 index_col=['id', 'date_time'])
print(df)

print('--------ddd----------------------------------------------------')	#60個

#Writing to a SQLite database

weather_df = pd.read_csv('data/weather_2012.csv')
con = sqlite3.connect("tmp_test_db.sqlite")
con.execute("DROP TABLE IF EXISTS weather_2012")
weather_df.to_sql("weather_2012", con)


con = sqlite3.connect("tmp_test_db.sqlite")
df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con)
print(df)

con = sqlite3.connect("tmp_test_db.sqlite")
df = pd.read_sql("SELECT * from weather_2012 ORDER BY Weather LIMIT 3", con)
print(df)

print('------------------------------------------------------------')	#60個

"""
#Connecting to other kinds of database

#MySQL / PostgreSQL
import MySQLdb
con = MySQLdb.connect(host="localhost", db="test")

#To connect to a PostgreSQL database:
import psycopg2
con = psycopg2.connect(host="localhost")

"""


print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個


import numpy as np

a = np.array([[1,2,3],[4,5,6]], int)#指定元素型態的陣列
a = np.array([[1,2,3],[4,5,6]], dtype = float)#指定元素型態的陣列
print(a[0, 0], a[0, 1], a[0, 2])
print(a[1, 0], a[1, 1], a[1, 2])

print('陣列元素的資料型態 :', a.dtype)
print('陣列的元素總數', a.size)
print('陣列的形狀', a.shape)
print('陣列元素所占用的拜數', a.itemsize)
print('幾維陣列', a.ndim)
print('整個陣列所占用的拜數', a.nbytes)

print("------------------------------------------------------------")  # 60個

print('陣列的形狀操作 reshape 1')
import numpy as np

a = np.array([1,2,3,4,5,6])
print(a)
b = a.reshape((3, 2))
print(b)

print("------------------------------------------------------------")  # 60個

print('陣列的形狀操作 reshape 2')
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = a.reshape((3, 3))
print(b)
c = b.flatten()
print(c)

print("------------------------------------------------------------")  # 60個

#合併
import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
c = np.concatenate((a, b), axis=0)
print(c)
d = np.concatenate((a, b), axis=1)
print(d)

print("------------------------------------------------------------")  # 60個

#擴充或刪除陣列的維度
import numpy as np

a = np.array([[1,2,3,4,5,6,7,8]])
b = a.reshape(2, 4)
print(b.shape)
c = np.expand_dims(b, axis=0)
d = np.expand_dims(b, axis=1)
print(c.shape, d.shape)
e = np.squeeze(c)
f = np.squeeze(d)
print(e.shape, f.shape)

print("------------------------------------------------------------")  # 60個

#取得陣列最大最小值和索引

import numpy as np

a = np.array([[11,22,13,74,35,6,27,18]])

min_value = np.min(a)
max_value = np.max(a)
print(min_value, max_value)

min_idx = np.argmin(a)
max_idx = np.argmax(a)
print(min_idx, max_idx)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

import numpy as np

x1 = np.linspace(-2.0, 2.0, 11) #包含頭尾共21點

# 移除 x1 > 0.55 的點, 就是保存 x1 <=0.6的點
x2 = x1[x1 <= 0.55]

# 遮罩 x1 > 0.7 的點, 會多了點線標記
x3 = np.ma.masked_where(x1 > 0.7, x1)

print(x1)
print(x2)
print(x3)


"""
x1 = np.random.normal(mu, sigma, size=N*10)  # 隨機數

# list 移除資料的寫法
x2 = x1[x1 <= 100.0]
x2 = x2[x2 >= 0]

"""

#過濾資料

"""
scores1 = np.random.normal(mu, sigma, size=N)  # 隨機數
print("資料個數1 :", len(scores1))
print("最高分 :", max(scores1))
print("最低分 :", min(scores1))

scores2 = scores1[scores1 <= 100.0]
scores3 = scores2[scores2 >= 0.0]
"""




print('------------------------------------------------------------')	#60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



