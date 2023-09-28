import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

# 加载取数与绘图所需的函数包
import pandas as pd
import datetime
from hs_udata import set_token,stock_quote_daily
from mpl_finance import candlestick_ohlc
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
#mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

data_price = [1 ,2, 3, 4, 5]

#4、绘制图片
fig = plt.figure(figsize=(12,10))
grid = plt.GridSpec(12, 10, wspace=0.5, hspace=0.5)
#（1）绘制K线图
# K线数据
#ohlc = data_price[['Date','open_price','high_price','low_price','close_price']]
#ohlc.loc[:,'Date'] = range(len(ohlc))     # 重新赋值横轴数据，绘制K线图无间隔

# 绘制K线
ax1 = fig.add_subplot(grid[0:8,0:12])   # 设置K线图的尺寸
#candlestick_ohlc(ax1, ohlc.values.tolist(), width=.7, colorup='red', colordown='green')
# （2）绘制均线
ax1.plot(range(len(data_price)), data_price, color='red', lw=2, label='MA (5)')

# 设置标注
plt.title('test', fontsize = 14)       # 设置图片标题
plt.ylabel('价 格（元）', fontsize = 14)   # 设置纵轴标题
plt.legend(loc='best')                    # 绘制图例
ax1.set_xticks([])                        # 日期标注在成交量中，故清空此处x轴刻度
ax1.set_xticklabels([])                   # 日期标注在成交量中，故清空此处x轴

#（3）绘制成交量
# 成交量数据

#data_volume = data_price[['Date','close_price','open_price','business_amount']]
#data_volume['color'] = data_volume.apply(lambda row: 1 if row['close_price'] >= row['open_price'] else 0, axis=1)        # 计算成交量柱状图对应的颜色，使之与K线颜色一致
#data_volume.Date = ohlc.Date

data_volume = [3, 2, 1, 4, 6]
# 绘制成交量
ax2 = fig.add_subplot(grid[8:10,0:12])  # 设置成交量图形尺寸
#ax2.bar(data_volume, color='r')                    # 绘制红色柱状图
#ax2.bar(data_volume, color='g')                    # 绘制绿色柱状图
plt.xticks(rotation=30) 
plt.xlabel('日 期',fontsize = 14)                               # 设置横轴标题
# 修改横轴日期标注
date_list = [1, 2, 3, 4, 5]#ohlc.index.tolist()           # 获取日期列表
xticks_len = round(len(date_list)/(len(ax2.get_xticks())-1))      # 获取默认横轴标注的间隔
xticks_num = range(0,len(date_list),xticks_len)                   # 生成横轴标注位置列表
xticks_str = list(map(lambda x:date_list[int(x)],xticks_num))     # 生成正在标注日期列表
ax2.set_xticks(xticks_num)                                        # 设置横轴标注位置
ax2.set_xticklabels(xticks_str)                                   # 设置横轴标注日期

plt.show()

print('------------------------------------------------------------')	#60個
