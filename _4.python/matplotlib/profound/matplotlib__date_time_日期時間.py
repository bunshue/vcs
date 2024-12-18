"""
日期時間相關


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


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

# 時序圖
import matplotlib.dates as mdates

#     2017/0808/2100    2017/0808/2101    2017/0808/2102    2017/0808/2103
x = [
    "20170808210000",
    "20170808210100",
    "20170808210200",
    "20170808210300",
    "20170808210400",
    "20170808210500",
    "20170808210600",
    "20170808210700",
    "20170808210800",
    "20170808210900",
]

x = pd.to_datetime(x)
y = [3900.0, 3903.0, 3891.0, 3888.0, 3893.0, 3899.0, 3906.0, 3914.0, 3911.0, 3912.0]

plt.plot(x, y)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%m-%d %H:%M"))  # 設置時間顯示格式
plt.gcf().autofmt_xdate()  # 自動旋轉角度，以避免重疊

plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.dates as mdates

total_bars = 25

dates = pd.date_range("3/4/2020", periods=total_bars, freq="ME")

diff = pd.DataFrame(data=np.random.randn(total_bars), index=dates, columns=["A"])

figure, axes = plt.subplots(figsize=(10, 6))

axes.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

axes.bar(diff.index, diff["A"], width=25, align="center")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import matplotlib
from datetime import datetime

origin = ["2020-02-05 17:17:55", "2020-02-05 17:17:51", "2020-02-05 17:17:49"]

a = [datetime.strptime(d, "%Y-%m-%d %H:%M:%S") for d in origin]

b = ["35.764299", "20.3008", "36.94704"]

for _ in a:
    print(_)

x = matplotlib.dates.date2num(a)
print(x)

formatter = matplotlib.dates.DateFormatter("%H:%M:%S")

figure = plt.figure()
axes = figure.add_subplot(111)

axes.xaxis.set_major_formatter(formatter)
plt.setp(axes.get_xticklabels(), rotation=25)
plt.setp(axes.get_yticklabels(), rotation=25)

axes.plot(x, b)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import matplotlib as mpl

# 獲取圖的坐標信息
ax = plt.gca()
# 設置日期的顯示格式
date_format = mpl.dates.DateFormatter("%m-%d")
ax.xaxis.set_major_formatter(date_format)
# 設置x軸顯示多少個日期刻度
# xlocator = mpl.ticker.LinearLocator(10)
# 設置x軸每個刻度的間隔天數
xlocator = mpl.ticker.MultipleLocator(7)
ax.xaxis.set_major_locator(xlocator)

# 為了避免x軸刻度標簽的緊湊，將刻度標簽旋轉45度
plt.xticks(rotation=45)
# 添加y軸標簽
plt.ylabel("人數")
# 添加圖形標題
plt.title("每天微信文章閱讀人數與人次趨勢")
# 添加圖例Virginica
# plt.legend()
# 顯示圖形

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

xx = np.arange(
    np.datetime64("2025-01-01"), np.datetime64("2025-01-02"), np.timedelta64(60, "m")
)  # 每隔 60分 取一個點
print(len(xx))
print(xx)
yy = np.random.randn(len(xx))
print(yy)
fig, ax = plt.subplots()
ax.plot(xx, yy)

plt.xticks(rotation=25)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from datetime import datetime
import matplotlib.dates as mdates

# 生成横纵坐标信息
dates = ["01/02/2025", "01/03/2025", "01/04/2025"]
xx = [datetime.strptime(d, "%m/%d/%Y").date() for d in dates]
yy = np.random.randn(len(xx))

# 配置横坐标
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y"))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

plt.plot(xx, yy)
plt.gcf().autofmt_xdate()  # 自动旋转日期标记

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
2.设置日期坐标轴主副刻度值
所有坐标轴日期格式类型
MinuteLocator: locate minutes（f）
HourLocator: locate hours
DayLocator: locate specified days of the month
WeekdayLocator: Locate days of the week, e.g., MO, TU
MonthLocator: locate months, e.g., 7 for july
YearLocator: locate years that are multiples of base
RRuleLocator: locate using a matplotlib.dates.rrulewrapper. The rrulewrapper is a simple wrapper around adateutil.rrule (dateutil) which allow almost arbitrary date tick specifications. See rrule example.
AutoDateLocator: On autoscale, this class picks the best MultipleDateLocator to set the view limits and the tick locations.
"""

# (1)获取坐标轴日期格式类型

from matplotlib.dates import DateFormatter
from matplotlib.dates import MonthLocator
from matplotlib.dates import WeekdayLocator
from matplotlib.dates import DayLocator
from matplotlib.dates import MONDAY
from matplotlib.dates import YEARLY

# 获取每月一日数据
monthdays = MonthLocator()

# 获取每周一的日期数据
mondays = WeekdayLocator(MONDAY)

# 获取每日数据
alldays = DayLocator()

# import constants for the days of the week
from matplotlib.dates import MO, TU, WE, TH, FR, SA, SU

# tick on mondays every week
# loc = WeekdayLocator(byweekday=MO, tz=tz)
# tick on mondays and saturdays
loc = WeekdayLocator(byweekday=(MO, SA))
# tick on mondays every second week
loc = WeekdayLocator(byweekday=MO, interval=2)
# tick every 5th easter(每隔5个选1个)

# matplotlib.dates.rrulewrapper
rule = matplotlib.dates.rrulewrapper(YEARLY, byeaster=1, interval=5)
from matplotlib.dates import RRuleLocator

loc = RRuleLocator(rule)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
(2)设置坐标轴日期格式
#设置主副刻度
ax.xaxis.set_major_locator(mondays)ax.xaxis.set_minor_locator(alldays)
#设置坐标轴刻度标签格式
mondayFormatter = DateFormatter('%Y-%m-%d') # 如：2-29-2015dayFormatter = DateFormatter('%d') # 如：12ax.xaxis.set_major_formatter(mondayFormatter)
#字符串旋转
for label in ax1.get_xticklabels(): label.set_rotation(30) label.set_horizontalalignment('right')
"""

import matplotlib as mpl
import matplotlib.dates as mdates
from datetime import datetime

# 销售数据

xx = np.arange(
    np.datetime64("2025-01-01"), np.datetime64("2025-01-05"), np.timedelta64(1, "D")
)  # 每隔 1天 取一個點
print(len(xx))
print(xx)

dates = [20171101, 20171102, 20171103, 20171104]
sales = [102.1, 100.6, 849, 682]

# 将dates改成日期格式
x = [datetime.strptime(str(d), "%Y%m%d").date() for d in dates]
print(x)

# figure布局
fig = plt.figure(figsize=(8, 6))
ax1 = fig.add_subplot(1, 1, 1)
# 绘图
ax1.plot(
    dates,
    sales,
    ls="--",
    lw=3,
    color="b",
    marker="o",
    ms=6,
    mec="r",
    mew=2,
    mfc="w",
    label="业绩趋势走向",
)
plt.gcf().autofmt_xdate()  # 自动旋转日期标记

""" NG
#设置x轴主刻度格式
alldays =  mdates.DayLocator()                #主刻度为每天
ax1.xaxis.set_major_locator(alldays)          #设置主刻度
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y%m%d'))  

#设置副刻度格式
hoursLoc = mpl.dates.HourLocator(interval=6) #为6小时为1副刻度
ax1.xaxis.set_minor_locator(hoursLoc)
ax1.xaxis.set_minor_formatter(mdates.DateFormatter('%H'))
#参数pad用于设置刻度线与标签间的距离
ax1.tick_params(pad=10)
"""

plt.xlabel("日期")
plt.ylabel("銷售額")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 3.设置日期时间刻度值
import matplotlib as mpl
import datetime as dt

fig = plt.figure()
ax2 = fig.add_subplot(212)

date2_1 = dt.datetime(2008, 9, 23)
date2_2 = dt.datetime(2008, 10, 3)
delta2 = dt.timedelta(days=1)  # 每隔 1天 取一個點
dates2 = mpl.dates.drange(date2_1, date2_2, delta2)
y2 = np.random.rand(len(dates2))
ax2.plot_date(dates2, y2, linestyle="-")
dateFmt = mpl.dates.DateFormatter("%Y-%m-%d")
ax2.xaxis.set_major_formatter(dateFmt)

daysLoc = mpl.dates.DayLocator()
hoursLoc = mpl.dates.HourLocator(interval=6)
ax2.xaxis.set_major_locator(daysLoc)
ax2.xaxis.set_minor_locator(hoursLoc)

fig.autofmt_xdate(bottom=0.18)
fig.subplots_adjust(left=0.18)

ax1 = fig.add_subplot(211)
date1_1 = dt.datetime(2008, 9, 23)
date1_2 = dt.datetime(2009, 2, 16)
delta1 = dt.timedelta(days=10)  # 每隔 10天 取一個點
dates1 = mpl.dates.drange(date1_1, date1_2, delta1)
y1 = np.random.rand(len(dates1))
ax1.plot_date(dates1, y1, linestyle="--")
monthsLoc = mpl.dates.MonthLocator()
weeksLoc = mpl.dates.WeekdayLocator()
ax1.xaxis.set_major_locator(monthsLoc)
ax1.xaxis.set_minor_locator(weeksLoc)
monthsFmt = mpl.dates.DateFormatter("%b")
ax1.xaxis.set_major_formatter(monthsFmt)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
python用mpl_finance中的candlestick_ohlc畫分時圖

matplotlib.finance獨立出來成爲mpl_finance，而mpl_finance中的candlestick_ochl和candlestick_ohlc一般用來畫股票的K線圖。
我需要分析分時圖，也就是一分鐘的行情，這個時候就不能直接用candlestick_ochl函數，因爲candlestick_ochl中x軸最小的單位是日期，不是分鐘。

經過對mpl_finance的源代碼進行分析，問題在於matplotlib的date2num將日期轉換爲浮點數，
浮點數的整數部分表示日期，小數部分代表小時和分鐘。比如下面4個時間段是連續的分鐘。
時間 	date2num之後 	乘以1440
2018/09/17-21:34 	736954.8986 	1061215054
2018/09/17-21:35 	736954.8993 	1061215055
2018/09/17-21:36 	736954.9000 	1061215056
2018/09/17-21:37 	736954.9007 	1061215057

可以看出date2num函數計算之後，4個時間的整數部分都是736954，導致在X軸上這4個時間段都重疊在一起，無法區分了。
要達到的效果是每一個分鐘也能成爲一個整數，這樣就可以顯示出來了。
那麼一天是24小時，每小時60分鐘，那麼一天就是1440分鐘，將date2num計算的浮點數乘以1440就可以將每一分鐘轉爲整數，那麼就可以在x軸上。

最後還需要對x軸格式化，因爲自己對x軸進行了處理（乘以1440），採用默認的格式化是亂碼。需要自定義x軸的格式化函數。

pip install mpl_finance
pip install --upgrade mplfinance

"""

from pandas import DataFrame
import matplotlib.dates as dates
import mplfinance as mpf
from matplotlib.ticker import Formatter
from mplfinance.original_flavor import candlestick_ohlc

dfcvs = DataFrame(
    [
        #    時間            開盤, 最高 ,最低, 收盤
        ["2018/09/17-21:34", 3646, 3650, 3644, 3650],
        ["2018/09/17-21:35", 3650, 3650, 3648, 3648],
        ["2018/09/17-21:36", 3650, 3650, 3648, 3650],
        ["2018/09/17-21:37", 3652, 3654, 3648, 3652],
    ]
)

dfcvs.columns = ["時間", "開盤", "最高", "最低", "收盤"]
dfcvs["時間"] = pd.to_datetime(dfcvs["時間"], format="%Y/%m/%d-%H:%M")

# matplotlib的date2num將日期轉換爲浮點數，整數部分區分日期，小數區分小時和分鐘
# 因爲小數太小了，需要將小時和分鐘變成整數，需要乘以24（小時）×60（分鐘）= 1440，這樣小時和分鐘也能成爲整數
# 這樣就可以一分鐘就佔一個位置

dfcvs["時間"] = dfcvs["時間"].apply(lambda x: dates.date2num(x) * 1440)
data_mat = dfcvs.values

fig, ax = plt.subplots(figsize=(10, 6))

fig.subplots_adjust(bottom=0.1)
candlestick_ohlc(
    ax, data_mat, colordown="#53c156", colorup="#ff1717", width=0.2, alpha=1
)


# 將x軸的浮點數格式化成日期小時分鐘
# 默認的x軸格式化是日期被dates.date2num之後的浮點數，因爲在上面乘以了1440，所以默認是錯誤的
# 只能自己將浮點數格式化爲日期時間分鐘
# 參考https://matplotlib.org/examples/pylab_examples/date_index_formatter.html
class MyFormatter(Formatter):
    def __init__(self, dates, fmt="%Y%m%d %H:%M"):
        self.dates = dates
        self.fmt = fmt

    def __call__(self, x, pos=0):
        "Return the label for time x at position pos"
        ind = int(np.round(x))
        # ind就是x軸的刻度數值，不是日期的下標

        return dates.num2date(ind / 1440).strftime(self.fmt)


formatter = MyFormatter(data_mat[:, 0])
ax.xaxis.set_major_formatter(formatter)

for label in ax.get_xticklabels():
    label.set_rotation(90)
    label.set_horizontalalignment("right")

show()

print("------------------------------------------------------------")  # 60個

# 加載取數與繪圖所需的函數包
import datetime
from hs_udata import set_token, stock_quote_daily
import matplotlib as mpl
import matplotlib.dates as mdates

# from mplfinance import candlestick_ohlc
from mplfinance.original_flavor import candlestick_ohlc

data_price = [1, 2, 3, 4, 5]

# 繪製圖片
fig = plt.figure(
    num="matplotlib 02",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

grid = plt.GridSpec(12, 10, wspace=0.5, hspace=0.5)

ax1 = fig.add_subplot(grid[0:8, 0:12])  # 設置K線圖的尺寸

# candlestick_ohlc(ax1, ohlc.values.tolist(), width = 0.7, colorup = 'red', colordown = 'green')

# （2）繪制均線
# ax1.plot(range(len(data_price)), data_price, color = 'red', lw = 2, label = 'MA (5)')

# 設置標注
plt.title("test", fontsize=14)  # 設置圖片標題
plt.ylabel("價 格（元）", fontsize=14)  # 設置縱軸標題
# plt.legend(loc = 'best')                    # 繪制圖例
ax1.set_xticks([])  # 日期標注在成交量中，故清空此處x軸刻度
ax1.set_xticklabels([])  # 日期標注在成交量中，故清空此處x軸

# （3）繪制成交量
# 成交量數據

data_volume = [3, 2, 1, 4, 6]
# 繪制成交量
ax2 = fig.add_subplot(grid[8:10, 0:12])  # 設置成交量圖形尺寸
# ax2.bar(data_volume, color = 'r')                    # 繪制紅色柱狀圖
# ax2.bar(data_volume, color = 'g')                    # 繪制綠色柱狀圖
plt.xticks(rotation=30)
plt.xlabel("日 期", fontsize=14)  # 設置橫軸標題
# 修改橫軸日期標注
date_list = [1, 2, 3, 4, 5]  # ohlc.index.tolist()           # 獲取日期列表
xticks_len = round(len(date_list) / (len(ax2.get_xticks()) - 1))  # 獲取默認橫軸標注的間隔
xticks_num = range(0, len(date_list), xticks_len)  # 生成橫軸標注位置列表
xticks_str = list(map(lambda x: date_list[int(x)], xticks_num))  # 生成正在標注日期列表
ax2.set_xticks(xticks_num)  # 設置橫軸標注位置
ax2.set_xticklabels(xticks_str)  # 設置橫軸標注日期

show()

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
