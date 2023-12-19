# 新進測試02

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

import pandas as pd
import random

print("------------------------------------------------------------")  # 60個

"""
python用mpl_finance中的candlestick_ohlc畫分時圖

matplotlib.finance獨立出來成爲mpl_finance，而mpl_finance中的candlestick_ochl和candlestick_ohlc一般用來畫股票的K線圖。我需要分析分時圖，也就是一分鐘的行情，這個時候就不能直接用candlestick_ochl函數，因爲candlestick_ochl中x軸最小的單位是日期，不是分鐘。

經過對mpl_finance的源代碼進行分析，問題在於matplotlib的date2num將日期轉換爲浮點數，浮點數的整數部分表示日期，小數部分代表小時和分鐘。比如下面4個時間段是連續的分鐘。
時間 	date2num之後 	乘以1440
2018/09/17-21:34 	736954.8986 	1061215054
2018/09/17-21:35 	736954.8993 	1061215055
2018/09/17-21:36 	736954.9000 	1061215056
2018/09/17-21:37 	736954.9007 	1061215057

可以看出date2num函數計算之後，4個時間的整數部分都是736954，導致在X軸上這4個時間段都重疊在一起，無法區分了。要達到的效果是每一個分鐘也能成爲一個整數，這樣就可以顯示出來了。那麼一天是24小時，每小時60分鐘，那麼一天就是1440分鐘，將date2num計算的浮點數乘以1440就可以將每一分鐘轉爲整數，那麼就可以在x軸上。

最後還需要對x軸格式化，因爲自己對x軸進行了處理（乘以1440），採用默認的格式化是亂碼。需要自定義x軸的格式化函數。
"""

""" OK
from pandas import DataFrame
import matplotlib.dates as dates
import mpl_finance as mpf
from matplotlib.ticker import Formatter


dfcvs = DataFrame([
    ["2018/09/17-21:34", 3646, 3650,3644,3650],
    ["2018/09/17-21:35", 3650, 3650,3648,3648],
    ["2018/09/17-21:36", 3650, 3650,3648,3650],
    ["2018/09/17-21:37", 3652, 3654,3648,3652]
])

dfcvs.columns = ['時間','開盤','最高','最低','收盤']
dfcvs['時間'] = pd.to_datetime(dfcvs['時間'],format = "%Y/%m/%d-%H:%M")

#matplotlib的date2num將日期轉換爲浮點數，整數部分區分日期，小數區分小時和分鐘
#因爲小數太小了，需要將小時和分鐘變成整數，需要乘以24（小時）×60（分鐘）= 1440，這樣小時和分鐘也能成爲整數
#這樣就可以一分鐘就佔一個位置

 

dfcvs['時間'] = dfcvs['時間'].apply(lambda x:dates.date2num(x) * 1440)
data_mat = dfcvs.values
    
fig,ax = plt.subplots(figsize = (10, 6))
 
fig.subplots_adjust(bottom = 0.1)   
mpf.candlestick_ohlc(ax, data_mat, colordown = '#53c156', colorup = '#ff1717', width = 0.2, alpha = 1)

#將x軸的浮點數格式化成日期小時分鐘
#默認的x軸格式化是日期被dates.date2num之後的浮點數，因爲在上面乘以了1440，所以默認是錯誤的
#只能自己將浮點數格式化爲日期時間分鐘
#參考https://matplotlib.org/examples/pylab_examples/date_index_formatter.html
class MyFormatter(Formatter):
            def __init__(self, dates, fmt = '%Y%m%d %H:%M'):
                self.dates = dates
                self.fmt = fmt
    
            def __call__(self, x, pos = 0):
                'Return the label for time x at position pos'
                ind = int(np.round(x))
                #ind就是x軸的刻度數值，不是日期的下標

                return dates.num2date( ind/1440).strftime(self.fmt)
        
formatter = MyFormatter(data_mat[:,0])
ax.xaxis.set_major_formatter(formatter)

for label in ax.get_xticklabels():
            label.set_rotation(90)
            label.set_horizontalalignment('right')
           
plt.show()
"""

""" fail
# 加載取數與繪圖所需的函數包
import datetime
from hs_udata import set_token,stock_quote_daily
from mpl_finance import candlestick_ohlc
import matplotlib as mpl
import matplotlib.dates as mdates

#mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默認字體
#mpl.rcParams['axes.unicode_minus'] = False  # 解決保存圖像是負號'-'顯示為方塊的問題

data_price = [1 ,2, 3, 4, 5]

#4、繪制圖片
fig = plt.figure(figsize = (12, 10))
grid = plt.GridSpec(12, 10, wspace = 0.5, hspace = 0.5)

ax1 = fig.add_subplot(grid[0 : 8, 0 : 12])   # 設置K線圖的尺寸

#candlestick_ohlc(ax1, ohlc.values.tolist(), width = 0.7, colorup = 'red', colordown = 'green')

# （2）繪制均線
#ax1.plot(range(len(data_price)), data_price, color = 'red', lw = 2, label = 'MA (5)')

# 設置標注
plt.title('test', fontsize = 14)       # 設置圖片標題
plt.ylabel('價 格（元）', fontsize = 14)   # 設置縱軸標題
plt.legend(loc = 'best')                    # 繪制圖例
ax1.set_xticks([])                        # 日期標注在成交量中，故清空此處x軸刻度
ax1.set_xticklabels([])                   # 日期標注在成交量中，故清空此處x軸

#（3）繪制成交量
# 成交量數據

data_volume = [3, 2, 1, 4, 6]
# 繪制成交量
ax2 = fig.add_subplot(grid[8 : 10, 0 : 12])  # 設置成交量圖形尺寸
#ax2.bar(data_volume, color = 'r')                    # 繪制紅色柱狀圖
#ax2.bar(data_volume, color = 'g')                    # 繪制綠色柱狀圖
plt.xticks(rotation = 30) 
plt.xlabel('日 期', fontsize = 14)                               # 設置橫軸標題
# 修改橫軸日期標注
date_list = [1, 2, 3, 4, 5]#ohlc.index.tolist()           # 獲取日期列表
xticks_len = round(len(date_list) / (len(ax2.get_xticks()) - 1))      # 獲取默認橫軸標注的間隔
xticks_num = range(0, len(date_list), xticks_len)                   # 生成橫軸標注位置列表
xticks_str = list(map(lambda x:date_list[int(x)], xticks_num))     # 生成正在標注日期列表
ax2.set_xticks(xticks_num)                                        # 設置橫軸標注位置
ax2.set_xticklabels(xticks_str)                                   # 設置橫軸標注日期

plt.show()
"""

print("------------------------------------------------------------")  # 60個

# 設定圖書分類及銷售額比例
listx = ["商業理財", "文學小說", "藝術設計", "人文科普", "語言電腦", "心靈養生", "生活風格", "親子共享"]
listm = [0.14, 0.16, 0.08, 0.13, 0.16, 0.12, 0.16, 0.05]  # 男性比例
listf = [0.1, 0.19, 0.06, 0.1, 0.13, 0.13, 0.2, 0.09]  # 女性比例

# 將比例乘以100
listm = [x * 100 for x in listm]
listf = [x * 100 for x in listf]

# 設定圖表區尺寸以及使用字型
plt.figure(figsize=(12, 9))

# 男性圖書分類銷售率圖餅圖
plt.subplot(221)
plt.title("圖書分類銷售比率-男性", fontsize=16)
plt.pie(listm, labels=listx, autopct="%2.1f%%")

# 女性圖書分類銷售率圖餅圖
plt.subplot(222)
plt.title("圖書分類銷售比率-女性", fontsize=16)
plt.pie(listf, labels=listx, autopct="%2.1f%%")

# 圖書分類男女銷售率長條圖
plt.subplot(223)
width = 0.4
listx1 = [x - width / 2 for x in range(len(listx))]
listx2 = [x + width / 2 for x in range(len(listx))]

plt.title("圖書分類銷售長條圖-性別", fontsize=16)
plt.xlabel("圖書分類", fontsize=12)
plt.ylabel("銷售比率(%)", fontsize=12)

plt.bar(listx1, listm, width, label="男")
plt.bar(listx2, listf, width, label="女")
plt.xticks(range(len(listx)), labels=listx, rotation=45)
plt.legend()

# 圖書分類男女銷售率折線圖
plt.subplot(224)
plt.title("圖書分類銷售折線圖-性別", fontsize=16)
plt.xlabel("圖書分類", fontsize=12)
plt.ylabel("銷售比率(%)", fontsize=12)

plt.plot(listx, listm, marker="s", label="男")
plt.plot(listx, listf, marker="s", label="女")
plt.gca().grid(True)
plt.xticks(rotation=45)
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個

n = np.linspace(1.1, 10, 90)  # 建立1.1-10的陣列
count = 0  # 用於計算每5筆輸出換行
for i in n:
    count += 1
    print("{0:2.1f} = {1:4.3f}".format(i, np.log10(i)), end="    ")
    if count % 5 == 0:  # 每5筆輸出就換行
        print()

print("------------------------------------------------------------")  # 60個

degrees = [30, 45, 60, 90, 120, 135, 150, 180]
for degree in degrees:
    print("角度 = {0:3d},   弧度 = {1:6.3f}".format(degree, math.pi * degree / 180))

print("------------------------------------------------------------")  # 60個

degrees = [30, 60, 90, 120]
r = 10
for degree in degrees:
    curve = 2 * math.pi * r * degree / 360
    print("角度 = {0:3d},   弧長 = {1:6.3f}".format(degree, curve))

print("------------------------------------------------------------")  # 60個

degrees = [30, 60, 90, 120]
r = 10
for degree in degrees:
    area = math.pi * r * r * degree / 360
    print("角度 = {0:3d},   扇形面積 = {1:6.3f}".format(degree, area))

print("------------------------------------------------------------")  # 60個

degrees = [x * 30 for x in range(0, 13)]
for d in degrees:
    rad = math.radians(d)
    sin = math.sin(rad)
    cos = math.cos(rad)
    print(
        "角度={0:3d}, 弧度={1:5.2f}, sin{2:3d}={3:5.2f}, cos{4:3d}={5:5.2f}".format(
            d, rad, d, sin, d, cos
        )
    )

print("------------------------------------------------------------")  # 60個


# foldername = 'C:/_git/vcs/_1.data/______test_files1/source_pic'
foldername = "C:/_git/vcs/_1.data/______test_files1"


"""
import glob
import cv2

files = glob.glob(foldername + "/*.jpg")  #建立測試資料
test_feature=[]
for file in files:
    print(file)
    img = cv2.imread(file)	#讀取本機圖片
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #灰階    
    _, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV) #轉為反相黑白 
    test_feature.append(img)

print(test_feature)

print('畫多張圖')


plt.gcf().set_size_inches(12, 14)

num=25

if num>25: num=25
for i in range(num):
    ax=plt.subplot(5,5, i+1)
    #ax.imshow(images[start_id], cmap='binary')  #顯示黑白圖片
    title = 'label = ' + str(i)
    ax.set_title(title,fontsize=12)  # X,Y軸不顯示刻度
    ax.set_xticks([]);ax.set_yticks([])        
plt.show()


"""

print("------------------------------------------------------------")  # 60個

"""
x = np.linspace(start=-10, stop=10, num=101)

#plt.plot(x, np.absolute(x))

xx = x + 1j * x[:, np.newaxis]

plt.imshow(np.abs(xx), extent=[-10, 10, -10, 10], cmap='gray')
"""

print("------------------------------------------------------------")  # 60個

filename = (
    "C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV6_score.csv"
)

dat = pd.read_csv(filename, encoding="UTF-8")
print(dat.head())

print("------------------------------------------------------------")  # 60個

# 計算平均數、中位數、眾數

filename = (
    "C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV6_score.csv"
)

dat = pd.read_csv(filename, encoding="UTF-8")

# 平均數、中位數
print("平均數", np.mean(dat["數學"]))
print("中位數", np.median(dat["數學"]))

# 眾數
bincnt = np.bincount(dat["數學"])  # 計算同樣的值的個數
mode = np.argmax(bincnt)  # 取得bincnt中最大的值
print("眾數", mode)

print("------------------------------------------------------------")  # 60個
print("亂數")

rand = []
for i in range(10):
    rand.append(random.randint(0, 100))  # 產生0～100的亂數
print(rand)

print("------------------------------------------------------------")  # 60個

a = 4  # 亂數的初始值
b = 7
c = 9  # 取亂數結果 0 ~ 8之整數
rn = 1

rand = []
for i in range(20):
    rn = (a * rn + b) % c  # 不用亂數模組, 自己運算出亂數
    rand.append(rn)
print(rand)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


"""
plt.xticks(range(0,5500,500))
plt.tick_params(axis = 'both', labelsize = 10, color = 'red')

plt.bar(listx, listy, width = 0.5, color = 'r')


plt.barh(listy, listx, height = 0.5, color = 'r')


"""


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
