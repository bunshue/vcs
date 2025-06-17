"""

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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    # plt.tight_layout()
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
'''
N = 100
index = np.arange(N)
bar_width = 0.8

woe_fig = plt.figure(figsize=(8, 8))

plt.title("Number of Observations and WoE per bucket")
ax = woe_fig.add_subplot(111)
ax.set_ylabel("Observations")
# plt.xticks(index + bar_width / 2, self.bins["labels"])
# plt.bar(index, self.bins["obs"], bar_width, color="b", label="Observations")
ax2 = ax.twinx()
ax2.set_ylabel("Weight of Evidence")
ax2.plot(
    index + bar_width / 2,
    # self.bins["woe"],
    "bo-",
    linewidth=4.0,
    color="r",
    label="WoE",
)
handles1, labels1 = ax.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
handles = handles1 + handles2
labels = labels1 + labels2
plt.legend(handles, labels)
woe_fig.autofmt_xdate()

show()

print("------------------------------------------------------------")  # 60個

"""
使用 yfinance 抓取 S&P 500 的 15 分鐘資料
下面是一個具體範例，從 Yahoo Finance 下載 S&P 500 指數在指定兩天內的每 15 分鐘的歷史資料。
這些數據將包括開盤價（Open）、最高價（High）、最低價（Low）、收盤價（Close）、調整後的收盤價（Adj Close）以及成交量（Volume）。

start_date 和 end_date: 我們選擇了 2 天的日期範圍，這適合使用 15m 這樣的高頻資料。
interval: 15m 代表每 15 分鐘抓取一次資料，適合短期交易分析。
intervals 參數
參考yf.download的定義註解

Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo Intraday data cannot extend last 60 days
一開始嘗試抓取 2023-08-01 ~ 2023-08-02 被拒絕
YFPricesMissingError('$%ticker%: possibly delisted; no price data found (15m 2023-08-01 -> 2023-08-02) (Yahoo error = "15m data not available for startTime=1690862400 and endTime=1690948800. The requested range must be within the last 60 days.")')
"""
import yfinance as yf

# 設定參數
start_date = "2025-04-28"  # 設定開始日期
end_date = "2025-04-30"  # 設定結束日期
interval = "15m"  # 設定時間週期為 15 分鐘


# 抓取 S&P 500 數據
ticker = "^GSPC"  # Yahoo Finance 中 S&P 500 的代號
sp500_data = yf.download(ticker, start=start_date, end=end_date, interval=interval)

# 顯示數據
print(sp500_data.head())


# 使用 yfinance 一次抓取多隻股票的資料
import yfinance as yf

# 設定參數
start_date = "2025-04-28"  # 設定開始日期
end_date = "2025-04-30"  # 設定結束日期
interval = "15m"  # 設定時間週期為 15 分鐘

# 設定多支股票的代號
tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]  # 股票代號

# 抓取多支股票的數據
data = yf.download(
    tickers, start=start_date, end=end_date, interval=interval, group_by="ticker"
)

# 顯示數據
for ticker in tickers:
    print(f"--- {ticker} ---")
    print(data[ticker].head())
    print("\n")

print("------------------------------------------------------------")  # 60個

import tensorflow as tf

# Check that we are using a GPU, if not switch runtimes
#   using Runtime > Change Runtime Type > GPU
# assert len(tf.config.list_physical_devices('GPU')) > 0

length = len(tf.config.list_physical_devices('GPU'))
print('GPU個數 :', length)

print("------------------------------------------------------------")  # 60個

def plot_transition_model(T_track, episode = 0):
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111, projection='3d')
    ax.view_init(elev=20, azim=50)

    color_left = '#008fd5' # ax._get_lines.get_next_color()
    color_right = '#fc4f30' #ax._get_lines.get_next_color()

    left_prob = np.array([1,2,3,4,5,6,7,8,9])

    right_prob = np.array([1,2,3,4,5,6,7,8,9])

    for s in np.arange(9):
        ax.bar3d(s+0.1, np.arange(9)+0.1, np.zeros(9),
                 np.zeros(9)+0.3,
                 np.zeros(9)+0.3, 
                 left_prob[s], 
                 color=color_left, 
                 alpha=0.75,
                 shade=True)
        ax.bar3d(s+0.1, np.arange(9)+0.1, left_prob[s],
                 np.zeros(9)+0.3,
                 np.zeros(9)+0.3, 
                 right_prob[s], 
                 color=color_right, 
                 alpha=0.75,
                 shade=True)

    ax.tick_params(axis='x', which='major', pad=10)
    ax.tick_params(axis='y', which='major', pad=10)
    ax.tick_params(axis='z', which='major', pad=10)

    ax.xaxis.set_rotate_label(False)
    ax.yaxis.set_rotate_label(False)
    ax.zaxis.set_rotate_label(False)
    ax.set_xticks(np.arange(9))
    ax.set_yticks(np.arange(9))

    plt.title('SWS learned MDP after {} episodes'.format(episode+1))
    ax.set_xlabel('Initial\nstate', labelpad=75, rotation=0)
    ax.set_ylabel('Landing\nstate', labelpad=75, rotation=0)
    ax.set_zlabel('Transition\nprobabilities', labelpad=75, rotation=0)

    left_proxy = plt.Rectangle((0, 0), 1, 1, fc=color_left)
    right_proxy = plt.Rectangle((0, 0), 1, 1, fc=color_right)

    plt.legend((left_proxy, right_proxy), 
               ('Left', 'Right'), 
               bbox_to_anchor=(0.15, 0.9), 
               borderaxespad=0.)

    ax.dist = 12
    #plt.gcf().subplots_adjust(left=0.1, right=0.9)

    show()

T_track_dq=[1,2,3,4,5]
plot_transition_model(T_track_dq, episode=0)

print("------------------------------------------------------------")  # 60個

fff = 123.456
training_start = time.time()

print('a')
time.sleep(1.234)
print('b')

elapsed_str = time.strftime("%H:%M:%S", time.gmtime(time.time() - training_start))

debug_message = 'el {}, ep {:04}, ts {:07},\n'
debug_message += 'ar 10  {:05.1f}\u00B1{:05.1f},\n'
debug_message += '100    {:05.1f}\u00B1{:05.1f},\n'
debug_message += 'ex 100 {:02.1f}\u00B1{:02.1f},\n'
debug_message += 'ev     {:05.1f}\u00B1{:05.1f}\n'
debug_message = debug_message.format(
elapsed_str, elapsed_str, elapsed_str, fff, fff,
fff, fff, fff, fff,
fff, fff)
                
print(debug_message, end='\r', flush=True)

print(u'--> reached_max_minutes \u2715')
print(u'--> reached_max_episodes \u2715')
print(u'--> reached_goal_mean_reward \u2713')

print('Final evaluation score {:.2f}\u00B1{:.2f} in {:.2f}s training time,'
      ' {:.2f}s wall-clock time.\n'.format(
          fff, fff, fff, fff))

print("------------------------------------------------------------")  # 60個

N = 30  # 數據數量

trains = np.random.randint(0, 100, size=(N, 2))

# 建立分類, 未來 0 代表 red,  1 代表 blue
labels = np.random.randint(0, 2, (N, 1))

# 列出紅色方塊訓練數據
red = trains[labels.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 50, "r", "s")  # 50是繪圖點大小

# 列出藍色三角形訓練數據
blue = trains[labels.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 50, "b", "^")  # 50是繪圖點大小
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# np.where的用法
# 建立三角波
N = 50

x = np.arange(0, 1, 1.0 / N)
y = np.where(x < 0.5, x, 0)
y = np.where(x >= 0.5, 1 - x, y)

plt.plot(x,y,"o")
plt.title('三角波')

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
# 語法
plt.scatter(mlr.fitted_,mlr.resid_)
plt.hlines(y=0,xmin=np.amin(mlr.fitted_),xmax=np.amax(mlr.fitted_),color="k",linestyle="dashed")

plt.hlines(y=0,xmin=np.amin(self.features_.T[i]),xmax=np.amax(self.features_.T[i]),color='k',linestyle='dashed')
                           
show()

#x = np.linspace(-np.pi, np.pi, num=100, endpoint=True)
#c, s, t = np.cos(x), np.sin(x), np.tan(x)

print('繪製預設的派圖')
plt.pie(df["weight"], labels=df["name"], autopct="%1.1f%%")
show()

print('從12點鐘方向開始繪製的派圖, 設定 startangle, 設定順時針開始')
plt.pie(df["weight"], labels=df["name"],
        autopct="%1.1f%%", startangle=90, counterclock=False) 
show()

"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" 欠缺
# 隨機森林的寫法
# 通过随机森林对变量的重要性进行筛选

import sklearn.ensemble as ensemble

rfc = ensemble.RandomForestClassifier(
    criterion="entropy", n_estimators=3, max_features=0.5, min_samples_split=5
)
rfc_model = rfc.fit(X_rep, Y)
rfc_model.feature_importances_
rfc_fi = pd.DataFrame()
rfc_fi["features"] = list(X.columns)
rfc_fi["importance"] = list(rfc_model.feature_importances_)
rfc_fi = rfc_fi.set_index("features", drop=True)
var_sort = rfc_fi.sort_values(by="importance", ascending=False)
var_sort.plot(kind="bar")
show()
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" many
cur_path=os.path.dirname(__file__) # 取得目前路徑
sample_tree=os.walk(cur_path)
for dirname,subdir,files in sample_tree:
    print("檔案路徑：",dirname)
    print("目錄串列：" , subdir)   
    print("檔案串列：",files)
    print()
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#系統

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

print("------------------------------------------------------------")  # 60個

print('本py檔全檔名')
print(__file__)

print('本py檔所在資料夾')
basedir = os.path.dirname(__file__)
print(basedir)

print("------------------------------------------------------------")  # 60個

cur_dir = os.path.dirname(__file__)
print(cur_dir)


#列出Python所有內建函數 dir()
cc = dir(__builtins__)
print(cc)

#Python的輔助說明 help()
cc = help(print)
print(cc)

print("------------------------------------------------------------")  # 60個
"""
# 刪除特定檔案

catlist = ['666.jpg', '5673.jpg', 'Thumbs.db']
doglist = ['11702.jpg', 'Thumbs.db']
for i in catlist:
  os.remove('PetImages/Cat/' + i)
for i in doglist:
  os.remove('PetImages/Dog/' + i)
"""
print("------------------------------------------------------------")  # 60個

# print(sys.path)  # 查詢模組路徑

print("加入路徑")

foldername = "C:/_git/vcs/_1.data/______test_files5"

sys.path.append(foldername)

# print(sys.path)  # 查詢模組路徑


print("------------------------------------------------------------")  # 60個

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_DIR = Path(__file__).resolve().parent.parent

# 使用 locals()傳遞所有的區域變數

print(locals())

print("------------------------------------------------------------")  # 60個

print(__file__)
print(__file__.lower())
print(__file__.upper())

print(os.path.dirname(__file__))

pathlist = os.environ['PATH'].split(os.pathsep)
print(pathlist)

print("------------------------------------------------------------")  # 60個

# 重新命名檔案

os.rename('filename.txt', 'new_filename.txt')

os.rename('/path/to/dir/filename.txt', '/path/to/dir/new_filename.txt')

dir = '/path/to/dir'
old_file = os.path.join(dir, 'filename.txt')
new_file = os.path.join(dir, 'new_filename.txt')
 
os.rename(old_file, new_file)

print("------------------------------------------------------------")  # 60個

print('# Generated by {}.  Do not edit manually.'.format(__file__))

print(globals())    #印出記憶體內目前所有的變數名稱

print()
print(__doc__ % globals())  #__doc__的內容有%的, 用變數名稱替換
print()
print(__doc__)  #有%不替換




print("------------------------------------------------------------")  # 60個

def lll(dirname):
    for name in os.listdir(dirname):
        #print('a')
        if name not in (os.curdir, os.pardir):
            print('b')
            full = os.path.join(dirname, name)
            print(full)


foldername = 'C:/_git/vcs/_1.data/______test_files5'
# lll(foldername)

print("------------------------------------------------------------")  # 60個
"""
    outdir = os.path.join(WORKDIR, 'diskimage')
    if os.path.exists(outdir):
        shutil.rmtree(outdir)
"""
print("------------------------------------------------------------")  # 60個

drive = os.environ['HOMEDRIVE']
print("HOMEDRIVE :", drive)

path = os.environ['PATH']
print("PATH :", path)

paths = path.split(os.pathsep)
print(paths)

# NG base, ext = os.path.splitext(executable)

print("------------------------------------------------------------")  # 60個

"""
[Python] 遍歷資料夾取得檔案名稱和目錄
這個程式碼示範了如何使用遞迴遍歷指定資料夾中的所有檔案和目錄。當遇到檔案時，它會使用縮排列印檔案名稱，當遇到目錄時，它會使用縮排列印目錄名稱，並且遞迴調用traverse_folder函數處理子目錄。
您可以將 'C:/Users/User/python/path' 替換為您要遍歷的資料夾的實際路徑。運行程式碼後，它會遞迴地列印資料夾中的所有檔案和目錄，並使用縮排來顯示層次結構。
請注意，indent參數用於控制縮排的數量，以便更好地表示層次結構。在遞迴調用時，將 indent + 4 傳遞給下一級目錄，以增加縮排的寬度。您可以根據需要自定義縮排的數量。
"""
def traverse_folder(folder_path, indent=0):
    # 獲取資料夾中的所有檔案和子目錄
    items = os.listdir(folder_path)
    
    for item in items:
        # 構建完整的路徑
        item_path = os.path.join(folder_path, item)
        
        if os.path.isfile(item_path):
            # 如果是檔案，列印檔案名稱
            print(" " * indent + "檔案:", item)
        elif os.path.isdir(item_path):
            # 如果是目錄，列印目錄名稱，並遞迴處理目錄
            print(" " * indent + "目錄:", item)
            traverse_folder(item_path, indent + 4)

# 指定資料夾路徑
folder_path = 'C:/Users/User/python/path'
# 遍歷資料夾中的檔案和目錄
# traverse_folder(folder_path)

print("------------------------------------------------------------")  # 60個

# 撈出多層

foldername = 'C:/_git/vcs/_1.data/______test_files3/DrAP_test'

# This would print all the files and directories
if __name__ == "__main__":
    print(foldername)
    if os.path.isdir(foldername):
        print('是資料夾')
        dirs = os.listdir(foldername)
        print("撈出一層(檔案+資料夾) :", dirs)
        for file in dirs:
            print(file)
            if not os.path.isdir(foldername + "/" + file):
                print('檔案 :', foldername + "/" + file)
            else:
                print('資料夾 :', foldername + "/" + file)
    else:
        print('不是資料夾')


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

'''
cwd = os.getcwd()
print(cwd)

new_folder = "AAAAA"

# 構建完整的路徑
full_path = os.path.join(cwd, new_folder)
print("full_path :", full_path)


# 刪除資料夾
# import shutil
# shutil.rmtree(png_path)


# 打印 print 測試

animals = [
    ("mouse", "鼠", 3),
    ("ox", "牛", 48),
    ("tiger", "虎", 33),
    ("rabbit", "兔", 8),
    ("dragon", "龍", 38),
]

# 保留N格靠左對齊(-N)、保留N格靠右對齊(+N)
print('%-25s %-15s %-15s' % ('英文名','中文名','體重'))
print('========================= =============== ===============')
for i in range(len(animals)):
    # print('%-25s %-15s %-15d' % (animals[i][0], animals[i][1], animals[i][2]))# 保留N格靠左對齊(-N)
    print('%25s %15s %15d' % (animals[i][0], animals[i][1], animals[i][2]))# 保留N格靠右對齊(+N)


pi = 3.14159265358979323846
print('%s: %f' % ("圓周率", pi)) # 預設6位小數
print('%s: %.5f' % ("圓周率", pi))


def pi(n):
    p = 0
    for i in range(1,n+1, 1):
        p += 4 *((-1)**(i+1)/(2*i-1))
    return p

print("  i      PI ")
print("================")
for i in range(1, 10000, 1000):
    print("%5d   %7.5f" % (i, pi(i)))


print("建立二維串列")
animals = [
    ["鼠", "mouse", 3, "米老鼠"],
    ["牛", "ox", 48, "班尼牛"],
    ["虎", "tiger", 33, "跳跳虎"],
    ["兔", "rabbit", 8, "彼得兔"],
    ["龍", "dragon", 38, "逗逗龍"],
]

for i in range(len(animals)):
    print("{:10s} {:10s}".format(animals[i][0], animals[i][1]))
    print("{:10s} {:10s}".format(str(animals[i][2]), animals[i][3]))
    print("{:10s} {:10s} {:10s} {:10s}".format(animals[i][0], animals[i][1], str(animals[i][2]), animals[i][3]))

# another 用 d
# print('  {:4s}: {:3d},'.format(repr(char), char2idx[char]))

print("------------------------------------------------------------")  # 60個

import datetime

now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print("現在時間 :", now)

now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print("現在時間 :", now)

now = datetime.date(2011, 12, 9)
cc = (now - datetime.date(2011, 1, 18)).days == 325
print(cc)

a = datetime.datetime.now()
print(a)   # 输出：2021-12-01 19:43:11.598313

today = datetime.date.today()
print('Day is', today)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print(time.time()) # 输出：1638348236.3917518
# print(time.clock())    # 输出：0.0338435
print(time.sleep(2))  # 括号里是2，程序睡两秒再执行，打印会显示None
print(time.time_ns())  # 输出：1638348716267450500
print(time.gmtime())   # 输出：time.struct_time(tm_year=1974, tm_mon=12, tm_mday=15, tm_hour=1, tm_min=6, tm_sec=0, tm_wday=6, tm_yday=349, tm_isdst=0)
print(time.gmtime(10000000))  #  输出： time.struct_time(tm_year=1970, tm_mon=4, tm_mday=26, tm_hour=17, tm_min=46, tm_sec=40, tm_wday=6, tm_yday=116, tm_isdst=0)
print(time.ctime(123123))   # 输出：Fri Jan  2 18:12:03 1970
print(time.ctime())    # 输出：Wed Dec  1 18:53:33 2021
print(time.strptime('2021-12-1','%Y-%m-%d'))   # 将其转化为机构化时间，前后必须对应
a = time.strptime('2021-12-1','%Y-%m-%d')
print(a.tm_year)  # 可以通过这种方式去取
                  # 输出：2025

print(time.localtime()) # 返回结构化时间，里面加参数，就从计算机元年开始算
a = time.localtime()
print(a.tm_year)  # 可以通过这种方式去取
                  # 输出：2021
print(time.mktime(time.localtime()))    # 输出： 1638358856.0

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
start = time()
# do something
end = time()
print('Execution time: %.3fs' % (end - start))
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


BMI = 12.3456
print(f"{BMI = :5.2f} 體重正常")

print("BMI =", format(BMI, ".2f"), "體重正常")

r1 = 123.456789
r2 = 222.334455 
print(f"{r1 = :6.4f},    {r2 = :6.4f}")

# return "%s:%s" % (self.filename, self.lineno)

humi = 67.89
temp = 23.45
print('溫度:{:.1f}, 濕度:{:.0f}%'.format(humi, temp))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
仿射轉換（Affine transformation），又稱仿射映射，是指在幾何中，對一個向量空間進行一次線性轉換並接上一個平移，轉換為另一個向量空間。

"""





print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


'''
------------------------------------------------------------
snippet 片段
Code Snippet
------------------------------------------------------------


print("------------------------------------------------------------")  # 60個


cv2.waitKey(3000)  # 等待3秒
cv2.destroyWindow("Peony1")  # 刪除Peony1
cv2.waitKey(8000)  # 等待8秒
cv2.destroyAllWindows()

ret = cv2.imwrite("tmp_out1_7_1.tiff", img)  # 將檔案寫入out1_7_1.tiff
ret = cv2.imwrite("tmp_out1_7_2.png", img)  # 將檔案寫入out1_7_2.png
cv2.imwrite("a32.png", a32_image)  # 儲存alpha=32影像

img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取
img = cv2.imread(filename1)  # 彩色讀取

# 影像的屬性

print(f"shape = {img.shape}")
print(f"size  = {img.size}")
print(f"dtype = {img.dtype}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# np.vsplit(data, 2) 垂直方向分割數據
# np.hsplit(data, 2) 水平方向分割數據
# np.repeat(data, N) 元素重複, 每個元素重複N次
# np.repeat(data, 3, axis=1)
# np.repeat(data, 3, axis=0)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
陣列垂直合併 vstack()
陣列水平合併 hstack()
"""

img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)
cv2.imshow("Peony", img)

# 準備搬出

# 建立GRAY影像陣列
image = np.zeros((5, 12), np.uint8)
print(f"修改前 image=\n{image}")  # 顯示修改前GRAY影像
print(f"image[1,4] = {image[1, 4]}")  # 列出特定像素點的內容

image[1, 4] = 255  # 修改像素點的內容
print(f"修改後 image=\n{image}")  # 顯示修改後的GRAY影像
print(f"image[1,4] = {image[1, 4]}")  # 列出特定像素點的內容

print("------------------------------------------------------------")  # 60個

# 取出圖片的一塊
face = img[70:220, 90:240]  # ROI, 先高後寬
cv2.imshow("Face", face)

print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)
src = cv2.imread(filename2)
src = np.random.randint(0, 256, size=[3, 5], dtype=np.uint8)

print("------------------------------------------------------------")  # 60個

# 使用 cv2.TM_SQDIFF 執行模板匹配
result = cv2.matchTemplate(src, template, cv2.TM_SQDIFF)
print(f"result大小 = {result.shape}")
print(f"陣列內容 \n{result}")


# print(f"輸出二維陣列 = \n{data}")
# print(f"轉成一維陣列 = \n{data.ravel()}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

設定 x軸為 log 刻度
plt.xscale('log')

------------------------------------------------------------

# 用np.clip函數設定陣列值的上下限，確保繪圖正確

axes[1].plot(np.clip(20 * np.log10(np.abs(fy[:20])), -120, 120), "o")

------------------------------------------------------------

plt.subplot(231)
plt.imshow(img[:, :, ::-1])
plt.title('部分')


result = cv2.calcHist([img_hsv], [0, 1], None, [40, 40], [0, 256, 0, 256])
print(result)
result /= np.max(result) / 255
print(result)
print(result.shape)

------------------------------------------------------------

import re

sentence = '愛因斯坦（德語：Albert Einstein，1879年3月14日－1955年4月18日），猶太裔理論物理學家，創立了現代物理學的兩大支柱之一的相對論[註 2][2]:274[1]，也是質能等價公式（E = mc2）的發現者[3]。'
s1 = re.sub(r'\[[^\]]*\]', '', sentence)
print(s1)

------------------------------------------------------------

# GridSearchCV

11. Grid searching and making the model perform better

from sklearn.model_selection import GridSearchCV

# Define the grid of values for tol and max_iter
tol = [0.01, 0.001, 0.0001]
max_iter = [100, 150, 200]

# Create a dictionary where tol and max_iter are keys and the lists of their values are corresponding values
param_grid = dict(tol=tol, max_iter=max_iter)

# Instantiate GridSearchCV with the required parameters
grid_model = GridSearchCV(estimator=logreg, param_grid=param_grid, cv=5)

# Use scaler to rescale X and assign it to rescaledX
rescaledX = scaler.fit_transform(X)

# Fit data to grid_model
grid_model_result = grid_model.fit(rescaledX, y)

# Summarize results
best_score, best_params = grid_model_result.best_score_, grid_model_result.best_params_
print("Best: %f using %s" % (best_score, best_params))

# Best: 0.850725 using {'max_iter': 100, 'tol': 0.01}

------------------------------------------------------------
# colab
------------------------------------------------------------

"""
os.chdir("/content/")
"""

from google.colab import drive
drive.mount("/content/drive")
# drive.mount("/content/drive", force_remount=True)

os.chdir("/content/drive/MyDrive/data/ch08")  # 使用 Colab 要換路徑使用，本機環境可以刪除
filenames = os.listdir()  # 轉出一層, 指定目錄, 若無參數, 就是當前目錄
print("4轉出一層(資料夾+檔案)\n", filenames)
print("當前目錄下共有 :", len(filenames), "個項目(資料夾+檔案)")

if os.path.isfile("img3.jpg"):
  print('有')
else:
  print('無')

if os.path.isfile("/content/yolo.h5"):
  print('有')
else:
  print('無')

------------------------------------------------------------

LogisticRegression 与 LogisticRegressionCV 的区别
LogisticRegression 和 LogisticRegressionCV 是 scikit-learn 库中用于逻辑回归的两个类，它们之间的区别如下。

LogisticRegression 是用于二分类或多分类问题的逻辑回归模型

lr = LogisticRegression()
lr.fit(X, y)

LogisticRegressionCV 是基于交叉验证的逻辑回归模型，用于自动选择最佳的正则化强度。

from sklearn.linear_model import LogisticRegressionCV
 
lr_cv = LogisticRegressionCV(cv=5)
lr_cv.fit(X, y)
best_C = lr_cv.C_

------------------------------------------------------------

1. 從匯入資料(查看資料型態)
2. 資料前處理(資料 reshape 把他們壓扁、資料標準化 normalize、label 資料 one hot encodeing)
3. 建立模型(這裡用多元感知器 Multilayer percertron ,MLP?)
 
  # 建立模型
  model = Sequential()

  # 建立輸入層和隱藏層
  model.add(Dense(units=256,input_dim=784,kernel_initializer='normal',activation='relu'))
  # 定義隱藏層神經元個數256
  # 輸入為28*28=784 個float 數字
  # 使用 normal distribution 常態分布的亂數，初始化 weight權重 bias 偏差
  # 定義激活函數為 relu

  # 建立輸出層
  model.add(Dense(units=10,kernel_initializer='normal',activation='softmax'))
  # 定義輸出層為10個 (數字0~9)
  # 也是使用常態分佈初始化
  # 定義激活函數是 softmax
  # 這裡建立的Dense 層，不用設定 input dim ，因為keras 會自動照上一層的256設定

  print(model.summary())
  
4. 模型compile訓練+紀錄訓練過程+訓練曲線視覺化(show train history)
5. 測試(評估測試準確度、進行預測、計算正確率使用confusion table)
7. 模型優化(方法有:增加神經元、加入 dropout 避免 oberfiting、增加隱藏層)
8. 結論:多層感知器有其極限，提高準確度可以試試看 CNN

------------------------------------------------------------

------------------------------------------------------------

#登錄微信, 不過, 沒下文

import itchat

itchat.auto_login()

#查找自己的朋友

friends_list = itchat.get_friends(update=True)
print(len(friends_list))
luohao = friends_list[0]
props = ['NickName', 'Signature', 'Sex']
for prop in props:
    print(luohao[prop])

------------------------------------------------------------

plt.grid(True)
plt.grid(which="major", linestyle="-", linewidth="0.5", color="green")
plt.grid(which="minor", linestyle=":", linewidth="0.5", color="black")

pd.set_option("display.max_rows", 1000)  # 設定最大能顯示1000rows
pd.set_option("display.max_columns", 1000)  # 設定最大能顯示1000columns

from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
mpl.rcParams["axes.unicode_minus"] = False

    x = random.randrange(-200, 200)
    y = random.randrange(-200, 200)
    length = random.randrange(75)


            richTextBox1.Text += "filename old = " + filename + "\n";

            string d_name = Path.GetDirectoryName(filename);
            string f_name = Path.GetFileNameWithoutExtension(filename);
            string ext_name = Path.GetExtension(filename);

------------------------------------------------------------

        private void button1_Click(object sender, EventArgs e)
        {
            Graphics g = this.CreateGraphics();
            Size s = this.Size;
            Bitmap bitmap1 = new Bitmap(s.Width, s.Height, g);
            Graphics memoryGraphics = Graphics.FromImage(bitmap1);
            memoryGraphics.CopyFromScreen(this.Location.X, this.Location.Y, 0, 0, s);

            pictureBox1.Image = bitmap1;

            //e.Graphics.DrawImage(memoryImage, 0, 0);
        }

------------------------------------------------------------

print('原本28欄')
df = pd.read_csv("donations.csv")
cc = df.head()
print(cc)
print(df.shape)

print('原本28欄, 開啟時 直接刪除2欄 直欄')
df = pd.read_csv("donations.csv").drop(
    ["ID", "TARGET_D"], axis=1
)
cc = df.head()
print(cc)
print(df.shape)

cc = df.head()
print(cc)
print(df.shape)

------------------------------------------------------------

# 邏輯迴歸參數
import sklearn.linear_model as linear_model

logistic_model = linear_model.LogisticRegression(
    class_weight=None,
    dual=False,
    fit_intercept=True,
    intercept_scaling=1,
    penalty="l1",
    random_state=None,
    tol=0.001,
)

logistic_model = linear_model.LogisticRegression(
    C=clf_cv.best_params_["C"],
    class_weight=None,
    dual=False,
    fit_intercept=True,
    intercept_scaling=1,
    penalty="l1",
    random_state=None,
    tol=0.001,
)
logistic_model.fit(train_data, train_target)

print(logistic_model.coef_)  # 表明第一个变量被剔除

from sklearn.neural_network import MLPClassifier  # 多層感知器分類器 函數學習機

mlp = MLPClassifier(
    hidden_layer_sizes=(10,), activation="logistic", alpha=0.1, max_iter=1000
)  # 多層感知器分類器 函數學習機

from sklearn import metrics

mlp = MLPClassifier(max_iter=1000)  # 多層感知器分類器 函數學習機

mlp = MLPClassifier(
    hidden_layer_sizes=gcv.best_params_["hidden_layer_sizes"],
    activation=gcv.best_params_["activation"],
    alpha=gcv.best_params_["alpha"],
    max_iter=1000,
)  # 多層感知器分類器 函數學習機

------------------------------------------------------------
------------------------------------------------------------

covMat = [[1,2], [3,4]]

eigVals, eigVects = np.linalg.eig(np.mat(covMat))

print(eigVals, eigVects)

    # step1:当数据量过大时，为了减少不必要的耗时
    if orgdata.iloc[:, 1].count() > 5000:
        data = orgdata.sample(5000)
    else:
        data = orgdata

df = pd.read_csv("xxxx.csv")
print("取出欄名")
print(df.columns)

print("取出2欄存成df, 修改欄名")
df = df[["Date", "Close"]]
df.columns = ["ds", "y"]
print(df)


plt.arrow(0, 0, U[0][0], U[1][0], color="r", linestyle="-")
plt.arrow(0, 0, U[0][1], U[1][1], color="r", linestyle="--")
plt.annotate(
    r"$U_{reduce} = u^{(1)}$",
    xy=(U[0][0], U[1][0]),
    xycoords="data",
    xytext=(U_reduce[0][0] + 0.2, U_reduce[1][0] - 0.1),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"$u^{(2)}$",
    xy=(U[0][1], U[1][1]),
    xycoords="data",
    xytext=(U[0][1] + 0.2, U[1][1] - 0.1),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"raw data",
    xy=(norm[0][0], norm[0][1]),
    xycoords="data",
    xytext=(norm[0][0] + 0.2, norm[0][1] - 0.2),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"projected data",
    xy=(Z[0][0], Z[0][1]),
    xycoords="data",
    xytext=(Z[0][0] + 0.2, Z[0][1] - 0.1),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

------------------------------------------------------------

#不要顯示一些警告
import warnings
warnings.filterwarnings("ignore")

error_caption = 'MSE: {}'.format(round(error,2)) 
fig.text(.1,.1,error_caption)


"""
    fig = plt.figure()
    plt.title(title)
    plt.xticks(np.array([]))
    plt.yticks(np.array([]))

    for x in range(nx):
        for y in range(ny):
            index = nx*y+x
            ax = fig.add_subplot(ny, nx, index + 1)
            ax.imshow(images[index], cmap='gray')
            plt.xticks(np.array([]))
            plt.yticks(np.array([]))
            error_caption = '{} - MSE: {}'.format(index, round(errors[index],2)) 
            ax.text(.1,.1,error_caption)
    show()

"""

"""
def plot_images_together(images):
    fig = plt.figure()
    images = [image[:, 3:25] for image in images]
    image = np.concatenate(images, axis=1)
"""

print('建立資料的方法')

print('range 加條件')
list3 = [x for x in range(10) if x % 2 == 0]
print("[x for x in range(10) if x%2==0]")
print(str(list3))
list4 = [x*2 for x in range(10) if x % 2 == 0]
print("[x*2 for x in range(10) if x%2==0]")
print(str(list4))

------------------------------------------------------------

d1 = {x:x*x for x in range(10)}
print("{x:x*x for x in range(10)}")
print(str(d1))
d2 = {x:x*x for x in range(10) if x % 2 == 1}
print("{x:x*x for x in range(11) if x%2==1}")
print(str(d2))

------------------------------------------------------------

def dice_roll():
    v = random.randint(1, 6)
    return v
    
trials = []    
num_of_trials = 100
for trial in range(num_of_trials):
    trials.append(dice_roll())
print(sum(trials)/float(num_of_trials))

------------------------------------------------------------

print(X)
print(len(X))

df plot
df_kmeans = pd.DataFrame()
df_kmeans["inertia_"] = inertia
df_kmeans.index = list(range(1, 15))
df_kmeans.plot(grid=True)
show()

df map的寫法
c = {0: "r", 1: "g", 2: "b"}
df1["colors"] = df1["pred"].map(c)


#前幾筆資料
plt.plot(X[:3, 0], X[:3, 1], "yx")

#後幾筆資料
plt.plot(X[3:, 0], X[3:, 1], "g.")


plt.plot(X[:3, 0], X[:3, 1], "yx")
plt.plot(X[3:, 0], X[3:, 1], "g.")

------------------------------------------------------------

n = 100000
cc = np.sum(4.0 / np.r_[1:n:4, -3:-n:-4])
print(cc)

"""
# 選取檔案的寫法
from google.colab import files
uploaded = files.upload()
print(uploaded)
"""

print('aaa')
cc = os.listdir("/content/drive/My Drive/Colab Notebooks")
print(cc)

print('bbb')

df = pd.read_csv("/content/drive/MyDrive/CSV/iris_sample.csv")
cc = df.head()
print(cc)

print('ccc')

import matplotlib
import matplotlib.font_manager as fm
!wget -O MicrosoftJhengHei.ttf https://github.com/a7532ariel/ms-web/raw/master/Microsoft-JhengHei.ttf
!wget -O ArialUnicodeMS.ttf https://github.com/texttechnologylab/DHd2019BoA/raw/master/fonts/Arial%20Unicode%20MS.TTF
 
fm.fontManager.addfont('MicrosoftJhengHei.ttf')
matplotlib.rc('font', family='Microsoft Jheng Hei')
 
fm.fontManager.addfont('ArialUnicodeMS.ttf')
matplotlib.rc('font', family='Arial Unicode MS')

        noise_sample = noise * np.random.normal(loc=0, scale=1.0, size=n_samples)
        noise_sample = noise * np.random.uniform(low=0, high=1.0, size=n_samples)
        noise_sample = noise * np.random.beta(a=0.5, b=1.0, size=n_samples)
        noise_sample = noise * np.random.gamma(shape=1.0, scale=1.0, size=n_samples)
        noise_sample = noise * np.random.laplace(loc=0.0, scale=1.0, size=n_samples)

meshgrid() : 可接受兩個一維向量，產生一個座標矩陣
np_c_ : 將兩個矩陣左右相連
ravel() : 將多維矩陣轉換成一維


import py_compile

# py_compile.compile('usemodule.py');
py_compile.compile('usemodule.py','usemodule.pyc')

------------------------------------------------------------

LogisticRegression 与 LogisticRegressionCV 的区别
LogisticRegression 和 LogisticRegressionCV 是 scikit-learn 库中用于逻辑回归的两个类，它们之间的区别如下。

1、LogisticRegression

LogisticRegression 是用于二分类或多分类问题的逻辑回归模型。可以使用不同的优化算法（如拟牛顿法、坐标下降法）来拟合逻辑回归模型。可以根据需要设置正则化项（L1正则化或L2正则化）以控制模型的复杂度。可以通过调整超参数（如正则化强度、优化算法等）来改善模型性能。

示例代码：

from sklearn.linear_model import LogisticRegression
 
lr = LogisticRegression()
lr.fit(X, y)
2、LogisticRegressionCV

LogisticRegressionCV 是基于交叉验证的逻辑回归模型，用于自动选择最佳的正则化强度。在拟合过程中，它会执行交叉验证来评估不同正则化强度的性能，并选择性能最佳的正则化强度。
可以指定要尝试的正则化强度值的范围，以及交叉验证的折数。自动选择的最佳正则化强度可以通过LogisticRegressionCV对象的C_属性获得。

示例代码：

from sklearn.linear_model import LogisticRegressionCV
 
lr_cv = LogisticRegressionCV(cv=5)
lr_cv.fit(X, y)
best_C = lr_cv.C_

3、总结

LogisticRegression 用于拟合逻辑回归模型，并手动调整超参数。LogisticRegressionCV 基于交叉验证自动选择最佳的正则化强度，无需手动调整超参数。

根据你的需求，你可以选择使用其中之一。如果你希望手动调整正则化强度或其他超参数，可以使用LogisticRegression。如果你希望自动选择最佳的正则化强度，并进行交叉验证来提高模型性能，可以使用LogisticRegressionCV。


from PIL import Image
import io

# Open PDF Source #
app_path = os.path.dirname(__file__)
src_pdf= PdfFileReader(open(os.path.join(app_path, "../../../uploads/%s" % filename), "rb"))

# Get the first page of the PDF #
dst_pdf = PdfFileWriter()
dst_pdf.addPage(src_pdf.getPage(0))

# Create BytesIO #
pdf_bytes = io.BytesIO()
dst_pdf.write(pdf_bytes)
pdf_bytes.seek(0)

file_name = "../../../uploads/%s_p%s.png" % (name, pagenum)
img = Image.open(pdf_bytes)
img.save(file_name, 'PNG')
pdf_bytes.flush()


\u0000 ~ \uFFFF
漢字 4E00~9FBB(9FFF)

chr(x) 轉 ASCII
ord(x) 轉 unicode

    def learning_curve(self):
        plt.ion()
        # plt.figure()
        E = np.array(self.Errors)
        E = pd.DataFrame(E)
        plt.plot(E.rolling(50).mean()[50:])
        show()

def sigmoid(x):
    # return x*(x > 0)
    # return np.tanh(x)
    return 1.0 / (1 + np.exp(-x))


data = np.random.uniform(0, 1, (100, 10))

    classCount = {}
    # 对分类字典classCount按value重新排序
    # sorted(data.items(), key=operator.itemgetter(1), reverse=True)
    # 该句是按字典值排序的固定用法
    # classCount.items()：字典迭代器函数
    # key：排序参数；operator.itemgetter(1)：多级排序
    sortedClassCount = sorted(
        classCount.items(), key=operator.itemgetter(1), reverse=True
    )
n

# dtree.loadDataSet("data03/dataset.dat", ["age", "revenue", "student", "credit"])
dtree.loadDataSet("data03/lenses.txt",['age','prescript','astigmatic','tearRate'])

dtree.loadDataSet("tmp_dataset.dat", ["age", "revenue", "student", "credit"])

dtree.loadDataSet("tmp_dataset.dat", ["age", "revenue", "student", "credit"])

dtree = C45DTree()
labels = ["age", "revenue", "student", "credit"]


matrix_data = np.matrix('22,66,140;42,70,148;30,62,125;35,68,160;25,62,152')
row_labels = ['A','B','C','D','E']
column_headings = ['Age', 'Height', 'Weight']

df = pd.DataFrame(data=matrix_data, index=row_labels, columns=column_headings)


Top 5 percentile in terms of Flavanoids?

np.percentile(df3['Flavanoids'],95)


df3[df3['Flavanoids']>=3.4975]

df3[df3['Flavanoids']>=3.4975][['Ash','Alcohol','Magnesium']].mean()


Numpy 操作
1. 各種轉換
2. 生成資料 np.arange  np.linspace
3. Zeroes, Ones, empty, and Identity matrix
np.zeros() 
np.ones() 
np.empty()
np.eye() 
4. Random number generation
5.Reshaping, min, max, sort
Indexing and slicing
Conditional subsetting
Array operations (array-array, array-scalar, universal functions)
NumPy basic statistics on array
np.sum(mat1)
np.sum(mat1,axis=0)
np.sum(mat1,axis=1)
np.prod(mat1,axis=1)
np.prod(mat2,axis=0)
np.mean(mat1)
np.std(mat1)
np.std(mat1)
np.var(mat1)
np.median(mat1)
np.std(mat2,axis=0)
np.sort(mat1.reshape(1,20))
np.percentile(mat1,50)
np.percentile(mat1,90)


Linear Algebra Operations
內積 外積

np.dot(A,B)
np.inner(A,B)
np.outer(A,B)


Transpose

np.transpose(A))
np.transpose(B))
np.dot(B, np.transpose(B)))


Trace
np.trace(A))
np.trace(A,offset=1))
np.trace(A,offset=-1))



# Linear equation solving, matrix inverse, linear least suqare

# 2x + 5y + z = 14;
# 3x - 2y - z = -1;
# x - 3y + z = 4

A = np.array([[2,5,1],[3,-2,-1],[1,-3,1]])
B = np.array([14,-1,4])
x = np.linalg.solve(A,B)

print("The solutions are:",x)

---------------------------------------------------------------------

#from IPython.html import widgets
#from IPython.html.widgets import interact

slider = widgets.FloatSliderWidget(min=0, max=4, value=2)

# from IPython.html.widgets import interact

# NG interact(plot_3D, elev=[-90, 90], azip=(-180, 180))
# NG interact(plot_fit, degree=[1, 30], Npts=[2, 100])

# dimensionality reduction techniques
# Principal component analysis (PCA)
# Independent component analysis (ICA)
# Random projections (RP)


搜尋開始	python	 interact(
# NG interact(plot_svm, N=[10, 200], kernel='linear')
# NG interact(plot_3D, elev=[-90, 90], azip=(-180, 180))
# NG interact(plot_fit, degree=[1, 30], Npts=[2, 100])
# interact(fit_randomized_tree, random_state=[0, 100])
上面搜尋到的資料在檔案	C:\_git\vcs\_4.python\__code\data-science-ipython-notebooks-master\scikit-learn\scikit-learn01.py

interact(plot_pdfs, cohen_d=slider)
上面搜尋到的資料在檔案	C:\_git\vcs\_4.python\__code\data-science-ipython-notebooks-master\scipy\scipy_新進1.py



Python的歷史
1989年聖誕節：Guido von Rossum開始寫Python語言的編譯器。
1991年2月：第一個Python編譯器誕生。
1994年1月：Python 1.0正式發佈。
2000年10月16日：Python 2.0發佈。
2008年12月3日：Python 3.0發佈
最新
Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35)

Python GUI : tkinter、wxPython、PyQt、PyGTK

Tk為控件的擺放提供了三種佈局管理器，通過佈局管理器可以對控件進行定位，這三種佈局管理器分別是：Placer（開發者提供控件的大小和擺放位置）、Packer（自動將控件填充到合適的位置）和Grid（基於網格座標來擺放控件）

python positional argument follows keyword argument

当参数的位置不正确时，就会报上面的错误；
关键字参数必须跟随在位置参数后面! 因为python函数在解析参数时, 是按照顺序来的, 位置参数是必须先满足, 才能考虑其他可变参数.
谨记！！！！


factorplot => catplot
作者发现factorplot已被替换为catplot，使用sns.catplot 成功解决了问题


Old (outdated, not supported in newer sklearn versions):

from sklearn.mixture import GMM

model = GMM(n_components=3,covariance_type='full')
model = mixture.GaussianMixture(n_components=3, covariance_type='full')

https://kotobank.jp/word/%E3%81%8C%E3%81%86%E3%81%99-1521577

plt.axvline(0, color="k", linestyle="--");
plt.axhline, y=0.1, color="k", ls=":"

rng = np.random.RandomState(0)
x = rng.randint(10, size=(3, 4))
x

#需要把woe所在的目录"D:\Python_book\19Case\19_2Donations"设置到python工作目录，
#设置方式为Tools->PYTHONPATH manager 

from woe import WoE # 从本地导入

# 创建一个列表，用来保存所有的建模数据清洗的相关信息
DATA_CLEAN = []
model_data = pd.read_csv("donations2.csv").drop(["ID","TARGET_D"],axis=1)
model_data.head()
model_data.dtypes

#需要把woe所在的目录"D:\Python_book\19Case\19_2Donations"设置到python工作目录，
#设置方式为Tools->PYTHONPATH manager 

from woe import WoE # 从本地导入

# 创建一个列表，用来保存所有的建模数据清洗的相关信息
DATA_CLEAN = []
model_data = pd.read_csv("donations2.csv").drop(["ID","TARGET_D"],axis=1)
model_data.head()
model_data.dtypes

split
⑤shuffle
是否在分割前对数据进行洗牌

⑥stratify
如果不是 “None”，数据将以分层方式分割，并以此作为类别标签


df之ix廢棄, 改成loc或iloc
before :
df.ix[0, '欄位名']

after :
df.loc[0, '欄位名']
df.iloc[0, column_index]

print("------------------------------")  # 30個

df之append廢棄, 改成pd.concat

before :
df = df.append(df_new_data)
df = df.append(df_new_data, ignore_index=True)

after :
df = pd.concat([df, df_new_data], axis=0, ignore_index=True)
df = pd.concat([df, pd.DataFrame([df_new_data])], ignore_index=True)

print("------------------------------")  # 30個

df.groupby()之agg的用法 原本字典方式給參數方法廢棄，改用指定參數

before :
df.groupby([‘id’])[‘click’].agg({‘click_std’:‘std’}).reset_index()
after :
df.groupby([‘id’])[‘click’].agg(click_std=‘std’).reset_index()

print("------------------------------")  # 30個

如何在 CMD 輸出 log 檔
dir		只在終端機上顯示結果

dir > a.log	終端機上不顯示結果 只將訊息存檔 訊息同上
dir 1> b.log	> 和 1> 是一樣的
		1> 錯誤訊息顯示在終端機、正確訊息寫入檔案

dir 2> c.log	和 1> 是相反
		1> 錯誤訊息寫入檔案、正確訊息顯示在終端機


> 等於 1>，負責輸出沒錯誤的部分
2> 負責輸出有錯誤的部分
1 的正式名稱為 stdout 標準輸出
2 的正式名稱為 stderr 標準錯誤輸出


log 種類
	stdout 標準輸出: 代號為 1，正常執行時的 log
	stderr 標準錯誤輸出: 代號為 2，出現錯誤時的 log

輸出 log 的指令
	command >file: 輸出 stdout 到 file
	command 1>file: 同上
	command 2>file: 輸出 stderr 到 file
	command >file 2>&1: 將 stdout 和 stderr 同時輸出到 file
	command >>file: 若 file 存在，就從結尾接續寫下去




其實掌握矩陣, 或很像矩陣的陣列都是「先列後行」就可以!

# axis = 0 : 第0維 直行
# axis = 1 : 第1維 橫列
print("直行加:", cc.sum(axis=0))
print("橫列加:", cc.sum(axis=1))


利用SKlearn實作特徵工程(Feature Engineering)

分類特徵(Categorical Features)

文字特徵(Text Features)

圖片特徵(Image Features)

Derived Features

------------------------------------------------------------

https://ithelp.ithome.com.tw/m/articles/10349618


AttributeError: 'DataFrame' object has no attribute 'ix'

将 

  df.ix[0, ‘column_name’]
 df.loc[0, ‘column_name’] 或 
df.iloc[0, column_index]。


Lasso 為 Linear Regression 加上 L1，
Ridge 為 Linear Regression 加上 L2，
正則化函數是⽤來衡量模型的複雜度，
避免模型有over-fitting的問題。

from sklearn.linear_model import Lasso

reg = Lasso(alpha=0.1) # 其中可以調整 alpha 值決定正則化的強度
reg.fit(X, y)
print(reg.coef_) # 印出訓練後的模型參數


from sklearn.linear_model import Ridge
reg = Ridge (alpha=0.1) #調整alpha值決定正則化的強度
reg.fit(X, y) 
print(reg.coef_) # 印出訓練後的模型參數，數值都明顯小於單純的線性回歸

------------------------------------------------------------

print("欲搜尋字串")
findstr = "aaaa"
index = str_Obj.find(findstr)     # 搜尋findstr字串是否存在
if  index >= 0:             # 搜尋檔案是否有欲尋找字串
    print("搜尋 %s 字串存在 %s 檔案中" % (findstr, filename))
    print("在索引 %s 位置出現" % index)
else:
    print("搜尋 %s 字串不存在 %s 檔案中" % (findstr, filename))

------------------------------------------------------------



def msgShow():
    label["text"] = "I love Python"
    label["bg"] = "lightyellow"
    label["fg"] = "blue"
    

expression = input("請輸入數學表達式 :")
print("結果是 : ", eval(expression))

bmi = round(weight / pow(height, 2), 2)

------------------------------------------------------------

bufsize = 8096
usage = """
usage: md5sum.py [-b] [-t] [-l] [-s bufsize] [file ...]
-b        : read files in binary mode (default)
-t        : read files in text mode (you almost certainly don't want this!)
-l        : print last pathname component only
-s bufsize: read buffer size (default %d)
file ...  : files to sum; '-' or no files means stdin
""" % bufsize

sys.stderr.write('%s: %s\n%s' % ('aaaa', 'bbbbb', usage))

---

# cv2 之讀檔 存檔 (轉換檔案格式) 直接改副檔名即可
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
cv2.imwrite("aaaa.png", img)

撈出一層時 若遇到資料夾 是如何處理的?!

------------------------------------------------------------

# Count each letter in the string 
def countLetters(line, counts): 
    for ch in line:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1

filename = 'data/engnews.txt'

infile = open(filename, "r") # Open the file, 格式要unicode轉ascii

counts = 26 * [0] # Create and initialize counts
for line in infile:
    # Invoke the countLetters function to count each letter
    countLetters(line.lower(), counts)
    
# Display results
for i in range(len(counts)):
    if counts[i] != 0:
        print(chr(ord('a') + i) + " appears " + str(counts[i])
          + (" time" if counts[i] == 1 else " times"))

infile.close() # Close file
  
------------------------------------------------------------

一檔從頭讀到尾
text = open(path.join(d, 'test.txt'),'r',encoding = 'utf-8').read()
text = open(path.join(d, 'test.txt'),'r').read()

是否一個 原本開啟後是亂碼的檔案 加上 encoding = xxx 或 .decode xxx 就會好

text = 'abcd'
text.startswith('ab')

------------------------------------------------------------
io與print + 1 * / ** int string length type 

if-else-for-while

function

tk做一個公版的離開按鈕
tk之button如何做到Enable = false?

for語法
    for rcs_dir in ('.svn', '.git', '.hg', 'build'):
        print('取得特定資料夾:', rcs_dir)

def pathdirs():
    # Convert sys.path into a list of absolute, existing, unique paths.
    dirs = []
    normdirs = []
    for dir in sys.path:
        dir = os.path.abspath(dir or '.')
        normdir = os.path.normcase(dir)
        if normdir not in normdirs and os.path.isdir(dir):
            dirs.append(dir)
            normdirs.append(normdir)
    return dirs
    
------------------------------------------------------------    

系統參數
sys.path:
        scriptdir = os.path.dirname(sys.argv[0])
        if scriptdir in sys.path:
            sys.path.remove(scriptdir)
        sys.path.insert(0, '.')

def cli():
    # Command-line interface (looks at sys.argv to decide what to do).
    import getopt
    class BadUsage(Exception): pass

    # Scripts don't get the current directory in their path by default
    # unless they are run with the '-m' switch
    if '' not in sys.path:
        scriptdir = os.path.dirname(sys.argv[0])
        if scriptdir in sys.path:
            sys.path.remove(scriptdir)
        sys.path.insert(0, '.')


------------------------------------------------------------

    n = read_uint4(f)
    assert n >= 0
    if n > sys.maxsize:
        raise ValueError("unicodestring4 byte count > sys.maxsize: %d" % n)


    def _dbg(self, level, msg):
        # Write debugging output to sys.stderr.
        
        if level <= self.debug:
            print(msg, file=sys.stderr)

        # default setting for prog
        if prog is None:
            prog = _os.path.basename(_sys.argv[0])

------------------------------------------------------------

if 'strxfrm' not in globals():

    lookup = os.environ.get
    for variable in envvars:
        localename = lookup(variable,None)
        if localename:
            if variable == 'LANGUAGE':
                localename = localename.split(':')[0]
            break


要能夠讓自定義的函數放在固定資料夾  讓.py去引用


修改檔案的內容

    if not os.path.isfile(m32):
        return
    with open(m32) as fin:
        with open(makefile, 'w') as fout:
            for line in fin:
                line = line.replace("=tmp32", "=tmp64")
                line = line.replace("=out32", "=out64")
                line = line.replace("=inc32", "=inc64")
                # force 64 bit machine
                line = line.replace("MKLIB=lib", "MKLIB=lib /MACHINE:X64")
                line = line.replace("LFLAGS=", "LFLAGS=/MACHINE:X64 ")
                # don't link against the lib on 64bit systems
                line = line.replace("bufferoverflowu.lib", "")
                fout.write(line)
    os.unlink(m32)

------------------------------------------------------------

SQLite 和 Python 資料型別

None     <->     NULL
int      <->     INTEGER/INT
float    <->     REAL/FLOAT
str      <->     TEXT/VARCHAR(n)
bytes    <->     BLOB
                
                
------------------------------------------------------------

ord函數		給一個Unicode字符，返回該字符的Unicode數字代碼

例如，給定ord('a') 返回整數 97，ord('\u2020') 返回 8224。同chr相反。

------------------------------------------------------------

if __name__ == '__main__':
    if len(sys.argv) == 1:
        _print_tokens(shlex())
    else:
        fn = sys.argv[1]
        with open(fn) as f:
            _print_tokens(shlex(f, fn))

    print("%d: %s[%d]%s %s" % (lineno(), filename(), filelineno(),
                                   isfirstline() and "*" or "", line))
print("%d: %s[%d]" % (lineno(), filename(), filelineno()))

    d = {}

        self.con = sqlite.connect(":memory:")
        self.con.execute("create table test (value text)")
        self.con.execute("insert into test (value) values (?)", ("a\x00b",))

       row = self.con.execute("select value from test").fetchone()
        cur.execute("select 4+5 as foo")
        row = cur.fetchone()

        austria = "Österreich"
        germany = "Deutchland"
        a_row = self.con.execute("select ?", (austria,)).fetchone()
        d_row = self.con.execute("select ?", (germany,)).fetchone()
        
------------------------------------------------------------
            print("The latest version of {} on PyPI is {}, but ensurepip "
                  "has {}".format(project, upstream_version, version))

        sys.stderr.write("can't stat %r: %r\n" % (filename, msg))

------------------------------------------------------------
def usage(msg):
    sys.stderr.write("%s: %s\n" % (sys.argv[0], msg))
    sys.stderr.write("Usage: %s [-l] file ...\n" % sys.argv[0])
    sys.stderr.write("Try `%s -h' for more information.\n" % sys.argv[0])

                print("%s:%d:%s" % (filename, row, line), end=' ')

    list = []
        list.append((tsub, key))
    list.sort()
    list.reverse()
    width = len(repr(list[0][0]))


------------------------------------------------------------

print('format語法 字串填空')

print('直接打印字串Unknown benchmark: {}'.format('zzzzzzzz', file=sys.stderr))
print('保留單引號Unknown benchmark: {!r}'.format('zzzzzzzz', file=sys.stderr))

seconds = 1
seconds_plural = 's' if seconds > 1 else ''
repeat = 3
pattern = ('這個字串要填入資料 第一筆 {}, 第二筆 {}, 第三筆 {}\n'
          '第四筆 {}\n'
          '第五筆 {!r}\n')

print(pattern.format(3, 8, 3, 4, 'dddd'))

sys.stdout.flush()

print "%s.%s unknown bits %x" % (self.name, name, unk)
                print "%s.%sunknown integer type %d" % (self.name, name, size)
        return "CREATE TABLE %s (%s PRIMARY KEY %s)" % (self.name, fields, keys)

    v = db.OpenView("INSERT INTO _Streams (Name, Data) VALUES ('%s', ?)" % name)



_directories = sets.Set()
        while logical in _directories:
            logical = "%s%d" % (_logical, index)
            index += 1
        _directories.add(logical)

------------------------------------------------------------

prog = sys.argv[0]

sys.stderr.write("Unable to open %s.  " % 'aaaaa')
sys.stderr.write("Check for format or version mismatch.\n")

    def touch_pymods(self):
        # force a rebuild of all modules that use OpenSSL APIs
        for fname in self.module_files:
            os.utime(fname)

------------------------------------------------------------

def usage(code, msg=''):
    print(__doc__ % globals(), file=sys.stderr)
    if msg:
        print(msg, file=sys.stderr)
    sys.exit(code)


            print(_(
                '*** %(file)s:%(lineno)s: Seen unexpected token "%(token)s"'
                ) % {
                'token': tstring,
                'file': self.__curfile,
                'lineno': self.__lineno
                }, file=sys.stderr)



                        print(_(
                            '# File: %(filename)s, line: %(lineno)d') % d, file=fp)

------------------------------------------------------------
            print(_(
                "Can't read --exclude-file: %s") % options.excludefilename, file=sys.stderr)

            fp = sys.stdin.buffer

                print('%s: %s, line %d, column %d' % (
                    e.args[0], filename, e.args[1][0], e.args[1][1]),
                    file=sys.stderr)

        print(msg, file=sys.stderr)

------------------------------------------------------------

print('No input file given', file=sys.stderr)
print("Try `msgfmt --help' for more information.", file=sys.stderr)


def pprint(data):
    items = sorted(data.items())
    for k, v in items:
        print('    %-40s%a,' % ('%a:' % k, v))

def print_differences(data, olddata):
    items = sorted(olddata.items())
    for k, v in items:
        if k not in data:
            print('#    removed %a' % k)
        elif olddata[k] != data[k]:
            print('#    updated %a -> %a to %a' % \
                  (k, olddata[k], data[k]))
        # Additions are not mentioned

------------------------------------------------------------

    def print_label(filename, func):
        name = re.split(r'[-.]', filename)[0]
        sys.stdout.write(
            ("[%s] %s... "
                % (name.center(7), func.__doc__.strip())
            ).ljust(52))
        sys.stdout.flush()



    def print_results(size, n, real, cpu):
        bw = n * float(size) / 1024 ** 2 / real
        bw = ("%4d MB/s" if bw > 100 else "%.3g MB/s") % bw
        sys.stdout.write(bw.rjust(12) + "\n")
        if cpu < 0.90 * real:
            sys.stdout.write("   warning: test above used only %d%% CPU, "
                "result may be flawed!\n" % (100.0 * cpu / real))

------------------------------------------------------------
data = ('abc', '123', '   ', '\u1234\u2345\u3456', '\uFFFF'*10)
data = ('abc', '123', '   ', '\xe4\xf6\xfc', '\xdf'*10)
len_data = len(data)

------------------------------------------------------------

def __repr__(self):
	return "<Frame filename=%r lineno=%r>" % (self.filename, self.lineno)

def _normalize_filename(filename):
    filename = os.path.normcase(filename)
    if filename.endswith(('.pyc', '.pyo')):
        filename = filename[:-1]
    return filename

------------------------------------------------------------

sys.stderr.write("WARNING: %s can not be found - standard extensions may not be found\n" % defaultMapName)
sys.stderr.write("No definition of module %s in any specified map file.\n" % (mod))
sys.stderr.write("%s: %s\n" % (dsp, msg))
sys.stderr.write('MARKER 1 never found\n')

sys.stderr.write(
    "Usage:  %s HOSTNAME:PORTNUMBER [, HOSTNAME:PORTNUMBER...]\n" %
    sys.argv[0])

unknown = 'ddddd'
sys.stderr.write('Warning: unknown modules remain: %s\n' %' '.join(unknown))

# Ring bell
sys.stderr.write('\007')

------------------------------------------------------------

磁碟處理 os類, shutil類

1. 建立資料夾
2. 檔案複製
3. 資料夾複製
4. 刪除檔案
5. 刪除資料夾

------------------------------------------------------------

__version__ = 1, 7, 0
__version__ = '2.1'

print('PYTHON %s' % __version__)

------------------------------------------------------------

def prdict(d):
    keys = sorted(d.keys())
    for key in keys:
        value = d[key]
        print("%-15s" % key, str(value))


    keys = sorted(makevars.keys())
    for key in keys:
        outfp.write("%s=%s\n" % (key, makevars[key]))
    outfp.write("\nall: %s\n\n" % target)

------------------------------------------------------------

error = 'mkreal error'

BUFSIZE = 32*1024

sys.stdout = sys.stderr

------------------------------------------------------------

import timeit
import itertools
import re
import optparse

VERSION = '2.0'

def p(*args):
    sys.stdout.write(' '.join(str(s) for s in args) + '\n')

if sys.version_info >= (3,):
    BYTES = bytes_from_str = lambda x: x.encode('ascii')
    UNICODE = unicode_from_str = lambda x: x
else:
    BYTES = bytes_from_str = lambda x: x
    UNICODE = unicode_from_str = lambda x: x.decode('ascii')

class UnsupportedType(TypeError):
    pass

p('stringbench v%s' % VERSION)
p(sys.version)

# Flush buffer before each group
sys.stdout.flush()


p("bytes\tunicode")
p("(in ms)\t(in ms)\t%\tcomment")

bytes_total = uni_total = 0.0


big_s = "A" + ("Z"*128*12)
print(big_s)

_RANGE_1000 = list(range(1000))
_RANGE_100 = list(range(100))
_RANGE_10 = list(range(10))



try:
    average = bytes_time/uni_time
except (TypeError, ZeroDivisionError):
    average = 0.0
print("%s\t%s\t%.1f\t%s (*%d)" % (
    bytes_time_s, uni_time_s, 100.*average,
    v.comment, v.repeat_count))

p("%.2f\t%.2f\t%.1f\t%s" % (
1000*bytes_total, 1000*uni_total, 100.*ratio, "TOTAL"))


------------------------------------------------------------

------------------------------------------------------------

self.chars = list(range(256))

------------------------------------------------------------
print(self.name+":", size*len(self.data), "bytes", file=sys.stderr)

print("%d+%d bins at shift %d; %d bytes" % (len(t1), len(t2), shift, bytes), file=sys.stderr)
print("Size of original table:", len(t)*getsize(t), "bytes", file=sys.stderr)

------------------------------------------------------------
    table = {}
    maxkey = 255
        for key in range(256):
            table[key] = (key, '')

    # Create table code
    maxchar = 0
    for key in range(256):
        if key not in table:
            mapvalue = MISSING_CODE
            mapcomment = 'UNDEFINED'
        else:
            mapvalue, mapcomment = table[key]
        if mapvalue == MISSING_CODE:
            mapchar = UNI_UNDEFINED
        else:
            if isinstance(mapvalue, tuple):
                # 1-n mappings not supported
                return None
            else:
                mapchar = chr(mapvalue)

------------------------------------------------------------mix

#Get a list of module files for a filename, a module or package name, or a directory.

def getFilesForName(name):
    if not os.path.exists(name):
        # check for glob chars
        if containsAny(name, "*?[]"):
            files = glob.glob(name)
            list = []
            for file in files:
                list.extend(getFilesForName(file))
            return list

        # try to find module or package
        name = _get_modpkg_path(name)
        if not name:
            return []

------------------------------------------------------------

def wrong_user_display(user_metadata: dict = {"name": "John", "age": 30}):

------------------------------------------------------------
        words = (
            "Acquaintance", "Rendezvous",
            "Acquaintance", "House", "Trip", "House", "House")
        expected_count = {
            'Acquaintance': 2,
            'Rendezvous': 1,
            'House': 3,
            'Trip': 1,
        }


------------------------------------------------------------



------------------------------------------------------------

self.assertEqual(func(), X + Y)
self.assertEqual((cn.id_, cn.user, cn.location), (42, "root", "127.0.0.1"))
self.assertEqual(customer.resolve_customer_id, 1)
self.assertFalse(hasattr(cn, "extra"))
self.assertTrue(result["latency"] >= 0.1)
self.assertTrue(result["latency"] >= 0.1)

self.assertIsNone(process_account_1.__doc__)
self.assertDictEqual(process_account_1.__annotations__, {})
self.assertTrue(process_account_2.__doc__.startswith("Process"))
self.assertDictEqual(process_account_2.__annotations__, {"account_id": str})
self.assertDictEqual(obtained, {"x": DEFAULT_X, "y": DEFAULT_Y})
self.assertDictEqual(obtained, {"x": DEFAULT_X, "y": DEFAULT_Y})
self.assertNotEqual(end_line, "[clinic]*/[clinic]*/")

------------------------------------------------------------

        for name, group in (
            ('y', -1), ('x', -1),
            ('ch', 0),
            ('attr', 1),
            ):
            p = function.parameters[name]


        for name, group in (
            ('y1', -2), ('y2', -2),
            ('x1', -1), ('x2', -1),
            ('ch', 0),
            ('attr1', 1), ('attr2', 1), ('attr3', 1),
            ('attr4', 2), ('attr5', 2), ('attr6', 2),
            ):
            p = function.parameters[name]
            self.assertEqual(p.group, group)
            self.assertEqual(p.kind, inspect.Parameter.POSITIONAL_ONLY)

        self.assertEqual(function.docstring.strip(),
imaginary([[y1, y2,] x1, x2,] ch, [attr1, attr2, attr3, [attr4, attr5,
          attr6]])

------------------------------------------------------------
                         
import unittest

#從另一個.py檔取得參數
from default_arguments import DEFAULT_X, DEFAULT_Y

DEFAULT_X = 5
DEFAULT_Y = 2

print(DEFAULT_X)
print(DEFAULT_Y)


class TestUnitTest(unittest.TestCase):
    print('UnitTest')
    print('UnitTest')
    print('UnitTest')


if __name__ == "__main__":
    unittest.main()

------------------------------------------------------------

class BaseTokenizer:
    """
    >>> tk = BaseTokenizer("28a2320b-fd3f-4627-9792-a2b38e3c46b0")
    >>> list(tk)
    ['28a2320b', 'fd3f', '4627', '9792', 'a2b38e3c46b0']
    """

    def __init__(self, str_token):
        self.str_token = str_token

    def __iter__(self):
        yield from self.str_token.split("-")


class UpperIterableMixin:
    def __iter__(self):
        return map(str.upper, super().__iter__())


class Tokenizer(UpperIterableMixin, BaseTokenizer):


tk = Tokenizer("28a2320b-fd3f-4627-9792-a2b38e3c46b0")
dddd = list(tk)
print(dddd)
#    ['28A2320B', 'FD3F', '4627', '9792', 'A2B38E3C46B0']

------------------------------------------------------------

import logging

logger = logging.getLogger("RefactoringTool")

logger=self.logger)

logger.info(msg)

            msg = msg % args
logger.debug(msg)


log_debug("Source: %s", line.rstrip("\n"))
log_error("Can't parse docstring in %s line %s: %s: %s",
                           filename, lineno, err.__class__.__name__, err)



    # Set up logging handler
    level = logging.DEBUG if options.verbose else logging.INFO
    logging.basicConfig(format='%(name)s: %(message)s', level=level)
    logger = logging.getLogger('lib2to3.main')

        logger.info('Output in %r will mirror the input directory %r layout.',
                    options.output_dir, input_base_dir)

------------------------------------------------------------

    _default_options = {"print_function" : False,
                        "write_unchanged_files" : False}

------------------------------------------------------------

# Map named tokens to the type value for a LeafPattern
TOKEN_MAP = {"NAME": token.NAME,
             "STRING": token.STRING,
             "NUMBER": token.NUMBER,
             "TOKEN": None}

------------------------------------------------------------

import difflib
import shutil
import optparse

def diff_texts(a, b, filename):
    # Return a unified diff of two strings.
    a = a.splitlines()
    b = b.splitlines()
    return difflib.unified_diff(a, b, filename, filename,
                                "(original)", "(refactored)",
                                lineterm="")
def warn(msg):
    print("WARNING: %s" % (msg,), file=sys.stderr)

filename1 = 'C:/_git/vcs/_1.data/______test_files1/poetrya.txt'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/poetryb.txt'
filename = 'ttttt.txt'

diff_lines = diff_texts(filename1, filename2, filename)
for line in diff_lines:
    print(line)
for line in diff_lines:
    print(line)

warn("couldn't encode %s's diff for your terminal" % (filename,))
warn("--write-unchanged-files/-W implies -w.")

print("At least one file or directory argument required.", file=sys.stderr)
print("Use --help to show usage.", file=sys.stderr)

print("Sorry, -j isn't supported on this platform.", file=sys.stderr)

------------------------------------------------------------

import ensurepip

version=ensurepip._PIP_VERSION
print(version)

EXPECTED_VERSION_OUTPUT = "pip " + ensurepip._PIP_VERSION

print(EXPECTED_VERSION_OUTPUT)

sentinel = object()
orig_pip = sys.modules.get("pip", sentinel)

print(orig_pip)

if orig_pip is sentinel:
    print('aaaaa')
else:
    print('bbbbb')

#print(ensurepip._main(["--version"]))

------------------------------------------------------------

def output(string = '', end = '\n'):
    sys.stdout.write(string + end)


def output(*strings):
    for s in strings:
        sys.stdout.write(str(s) + "\n")

------------------------------------------------------------

# json轉dict

import json
from urllib.request import urlopen
from html.entities import html5

entities_url = 'http://dev.w3.org/html5/spec/entities.json'

def get_json(url):
    # Download the json file from the url and returns a decoded object.
    with urlopen(url) as f:
        data = f.read().decode('utf-8')
    return json.loads(data)

def create_dict(entities):
    # Create the html5 dict from the decoded json object.
    new_html5 = {}
    for name, value in entities.items():
        new_html5[name.lstrip('&')] = value['characters']
    return new_html5

new_html5 = create_dict(get_json(entities_url))

------------------------------------------------------------
        try:
            # RFC 1952 requires the FNAME field to be Latin-1. Do not
            # include filenames that cannot be represented that way.
            fname = os.path.basename(self.name)
                fname = fname[:-3]

------------------------------------------------------------

import locale, copy, io, re, struct

------------------------------------------------------------

    def __repr__(self):
        args = ", ".join(map(repr, self.args))
        keywords = ", ".join("{}={!r}".format(k, v)
                                 for k, v in self.keywords.items())
        format_string = "{module}.{cls}({func}, {args}, {keywords})"
        return format_string.format(module=self.__class__.__module__,
                                    cls=self.__class__.__name__,
                                    func=self.func,
                                    args=args,
                                    keywords=keywords)

------------------------------------------------------------

    exe_dir, _ = os.path.split(os.path.abspath(executable))

    site_prefix = os.path.dirname(exe_dir)
            os.path.join(exe_dir, conf_basename),
            os.path.join(site_prefix, conf_basename)
        if os.path.isfile(conffile)
        here = os.path.dirname(os.__file__)
        dirs.extend([os.path.join(here, os.pardir), here, os.curdir])

------------------------------------------------------------

    ckeys = sorted(caps)
    for type in ckeys:
        print(type)
        entries = caps[type]
        for e in entries:
            keys = sorted(e)
            for k in keys:
                print("  %-15s" % k, e[k])
            print()

------------------------------------------------------------

def _recursion222(object):
    print(type(object))
    print(type(object).__name__)
    print(id(object))
    return ("<Recursion on %s with id=%s>"
            % (type(object).__name__, id(object)))

object = [("string", (1, 2), [3, 4], {5: 6, 7: 8})] * 100000
nnnn = _recursion222(object)
print(nnnn)

------------------------------------------------------------

warnings.warn('the formatter module is deprecated and will be removed in '
	'Python 3.6', PendingDeprecationWarning)

warnings.warn("This class is deprecated, use the netrc module instead",
	DeprecationWarning, 2)

------------------------------------------------------------


def errprint(*args):
    sep = ""
    for arg in args:
        sys.stderr.write(sep + str(arg))
        sep = " "
    sys.stderr.write("\n")


file = 'ffff'
msg = 'mmm'
errprint("%r: I/O Error: %s" % (file, msg))

msg = 'aaaaaa'

errprint('aaaa', 'bbbb', 'kkkk')
errprint("Usage:", sys.argv[0], "[-v] file_or_directory ...")

------------------------------------------------------------

def errprint(*args):
    strings = map(str, args)
    msg = ' '.join(strings)
    if msg[-1:] != '\n':
        msg += '\n'
    sys.stderr.write(msg)

msg = 'aaaaaaaaaaaaaa'
errprint(msg)
errprint("Usage:", __doc__)
errprint("Skipping file %r; can't parse line %d:\n%s" % (self.fname, srow, line))

------------------------------------------------------------

# Definition file template
DEF_TEMPLATE = """\
EXPORTS
%s
"""

------------------------------------------------------------

    def get_prog_name(self):
        if self.prog is None:
            return os.path.basename(sys.argv[0])
        else:
            return self.prog

------------------------------------------------------------

"""
Synopsis: %(prog)s [-h|-b|-g|-r|-a|-d] [ picklefile ] dbfile
Read the given picklefile as a series of key/value pairs and write to a new
hash or btree database using db2pickle.py and reconstitute it to a recno
database with %(prog)s unless your keys are integers.
"""

prog = sys.argv[0]

------------------------------------------------------------

import re

sys.stderr.write('Cannot open %s\n' % filename)

    base = os.path.basename(filename)
    if base[-3:] == '.py':
        base = base[:-3]
    s = base + '\t' + filename + '\t' + '1\n'
    tags.append(s)
    while 1:
        line = fp.readline()
        if not line:
            break


------------------------------------------------------------

USAGE = """\
Usage: mimetypes.py [options] type
Options:
More than one type argument may be given.
"""

def usage(code, msg=''):
    print(USAGE)
    if msg:
        print(msg)

msg = 'kkkk'
usage(1, msg)

usage(0)

------------------------------------------------------------

def _modname(path):
    """Return a plausible module name for the patch."""

    base = os.path.basename(path)
    filename, ext = os.path.splitext(base)
    return filename

    comparepath = os.path.normcase(path)
    longest = ""
    for dir in sys.path:
        dir = os.path.normcase(dir)
        if comparepath.startswith(dir) and comparepath[len(dir)] == os.sep:
            if len(dir) > len(longest):
                longest = dir

    if longest:
        base = path[len(longest) + 1:]
    else:
        base = path
    # the drive letter is never part of the module name
    drive, base = os.path.splitdrive(base)
    base = base.replace(os.sep, ".")
    if os.altsep:
        base = base.replace(os.altsep, ".")
    filename, ext = os.path.splitext(base)
    return filename.lstrip(".")

------------------------------------------------------------

            if filename.endswith((".pyc", ".pyo")):
                filename = filename[:-1]

            if coverdir is None:
                dir = os.path.dirname(os.path.abspath(filename))
                modulename = _modname(filename)
            else:
                dir = coverdir
                if not os.path.exists(dir):
                    os.makedirs(dir)
                modulename = _fullmodname(filename)

                s = os.path.expandvars(s)
                s = os.path.normpath(s)

------------------------------------------------------------

        for n in range(7):
            values = [5*x-12 for x in range(n)]
            for r in range(n+2):

        for n in range(6):
            s = 'ABCDEFG'[:n]
            for r in range(8):
                print(r)

        ans = list('abc')
        long_ans = list(range(10000))

------------------------------------------------------------

    if not isinstance(dt, datetime.datetime):
        time_str = "000000"
    else:
        time_str = "{0.hour:02d}{0.minute:02d}{0.second:02d}".format(dt)

    y = dt.year
    if legacy:
        y = y % 100
        date_str = "{0:02d}{1.month:02d}{1.day:02d}".format(y, dt)
    else:
        date_str = "{0:04d}{1.month:02d}{1.day:02d}".format(y, dt)
    return date_str, time_str

        cmd = 'NEWNEWS {0} {1} {2}'.format(group, date_str, time_str)
        return self._longcmdstring(cmd, file)


            self.sock = socket.create_connection((host, port), timeout)
            self.sock = _encrypt_on(self.sock, ssl_context, host)
            file = self.sock.makefile("rwb")
            _NNTPBase.__init__(self, file, host,
                               readermode=readermode, timeout=timeout)
            if user or usenetrc:
                self.login(user, password, usenetrc)

        def _close(self):
            try:
                _NNTPBase._close(self)
            finally:

                self.sock.close()


        self.host = host
        self.port = port
        self.sock = socket.create_connection((host, port), timeout)
        file = self.sock.makefile("rwb")
        _NNTPBase.__init__(self, file, host,
                           readermode, timeout)
        if user or usenetrc:
            self.login(user, password, usenetrc)

    def _close(self):
        try:
            _NNTPBase._close(self)
        finally:
            self.sock.close()


    def load_file(self, pathname):
        dir, name = os.path.split(pathname)
        name, ext = os.path.splitext(name)

        print()
        print("  %-25s %s" % ("Name", "File"))
        print("  %-25s %s" % ("----", "----"))


            if m.__path__:
                print("P", end=' ')
            else:
                print("m", end=' ')
            print("%-25s" % key, m.__file__ or "")


        new_filename = original_filename = os.path.normpath(co.co_filename)

    path[0] = os.path.dirname(script)

    if os.path.isabs(pathname):
        return '/' + '/'.join(components)
    else:
        return '/'.join(components)

------------------------------------------------------------
            print(file=self.stream)
            print(file=self.stream)
------------------------------------------------------------

import stat

def _get_sep(path):
    if isinstance(path, bytes):
        return b'/'
    else:
        return '/'

def splitdrive(p):
    """Split a pathname into drive and path. On Posix, drive is always
    empty."""
    return p[:0], p

def basename(p):
    """Returns the final component of a pathname"""
    sep = _get_sep(p)
    i = p.rfind(sep) + 1
    return p[i:]


filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
st = os.lstat(filename)
print(st)
isLink = stat.S_ISLNK(st.st_mode)
print(isLink)

aaa = splitdrive(filename)
print(aaa)

bbb = basename(filename)
print(bbb)

------------------------------------------------------------

    def touch(self, mode=0o666, exist_ok=True):
        """
        Create this file with the given access mode, if it doesn't exist.
        """
        if self._closed:
            self._raise_closed()
        if exist_ok:
            # First try to bump modification time
            # Implementation note: GNU touch uses the UTIME_NOW option of
            # the utimensat() / futimens() functions.
            try:
                self._accessor.utime(self, None)
            except OSError:
                # Avoid exception chaining
                pass
            else:
                return
        flags = os.O_CREAT | os.O_WRONLY
        if not exist_ok:
            flags |= os.O_EXCL
        fd = self._raw_open(flags, mode)
        os.close(fd)

------------------------------------------------------------

from stat import S_ISDIR, S_ISLNK, S_ISREG, S_ISSOCK, S_ISBLK, S_ISCHR, S_ISFIFO

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

print(os.lstat(filename))
print(os.lstat(filename).st_mode)
print(os.lstat(filename).st_gid)

reserved_names = (
    {'CON', 'PRN', 'AUX', 'NUL'} |
    {'COM%d' % i for i in range(1, 10)} |
    {'LPT%d' % i for i in range(1, 10)}
    )

for aaa in reserved_names:
    print(aaa, end = ' ')
print()


S_ISSOCK(self.stat().st_mode)
S_ISFIFO(self.stat().st_mode)
S_ISCHR(self.stat().st_mode)
S_ISBLK(self.stat().st_mode)
S_ISLNK(self.lstat().st_mode)
S_ISDIR(self.stat().st_mode)
S_ISREG(self.stat().st_mode)


    def _iterate_directories(self, parent_path, is_dir, listdir):
        yield parent_path
        for name in listdir(parent_path):
            path = parent_path._make_child_relpath(name)
            if is_dir(path):
                for p in self._iterate_directories(path, is_dir, listdir):
                    yield p




    def _select_from(self, parent_path, is_dir, exists, listdir):
        if not is_dir(parent_path):
            return
        path = parent_path._make_child_relpath(self.name)
        if exists(path):
            for p in self.successor._select_from(path, is_dir, exists, listdir):
                yield p

    def _select_from(self, parent_path, is_dir, exists, listdir):
        if not is_dir(parent_path):
            return
        cf = parent_path._flavour.casefold
        for name in listdir(parent_path):
            casefolded = cf(name)
            if self.pat.match(casefolded):
                path = parent_path._make_child_relpath(name)
                for p in self.successor._select_from(path, is_dir, exists, listdir):
                    yield p

        path.is_absolute()

------------------------------------------------------------

from collections.abc import MutableMapping
from collections import OrderedDict as _default_dict, ChainMap as _ChainMap
import functools
import io
import itertools
import re
import warnings

warnings.warn(
    "The 'filename' attribute will be removed in future versions.  "
    "Use 'source' instead.",
    DeprecationWarning, stacklevel=1
    )


    def read(self, filenames, encoding=None):
        if isinstance(filenames, str):
            filenames = [filenames]
        read_ok = []
        for filename in filenames:
            try:
                with open(filename, encoding=encoding) as fp:
                    self._read(fp, filename)
            except OSError:
                continue
            read_ok.append(filename)
        return read_ok

    def read_file(self, f, source=None):
        """Like read() but the argument must be a file-like object.

        The `f' argument must be iterable, returning one line at a time.
        Optional second argument is the `source' specifying the name of the
        file being read. If not given, it is taken from f.name. If `f' has no
        `name' attribute, `<???>' is used.
        """
        if source is None:
            try:
                source = f.name
            except AttributeError:
                source = '<???>'
        self._read(f, source)

        elements_added = set()
        for section, keys in dictionary.items():
            section = str(section)

------------------------------------------------------------

name = ['mouse', 'ox', 'tiger']
weight = [3, 48, 33]
print('名稱     編號  體重')
for i in range(0, 3):
    print(name[i].ljust(10),
          str(i+1).rjust(10),
          str(weight[i]).rjust(10))

------------------------------------------------------------

print('glob: {}'.format(foldername))
for fname in glob.glob(foldername, recursive=False):
    print("loading: {}".format(fname))

------------------------------------------------------------

print('Python之內建函數')
r = abs(-10)
print("abs(-10) = " + str(r))
r = abs(5)
print("abs(5) = " + str(r))
r = pow(8, 2)
print("pow(8, 2) = " + str(r))
r = pow(2, 3)
print("pow(2, 3) = " + str(r))
r = max(9, 3, 12, 32, 81, 92)
print("max(9, 3, 12, 32, 81, 92) = " + str(r))
r = min(9, 3, 12, 32, 81, 92)
print("min(9, 3, 12, 32, 81, 92) = " + str(r))
r = round(5.32)
print("round(5.32) = " + str(r))
r = round(5.52)
print("round(5.52) = " + str(r))
r = round(3.14568757, 3)
print("round(3.14568757, 3) = " + str(r))
r = round(3.14568757, 1)
print("round(3.14568757, 1) = " + str(r))

------------------------------------------------------------

print("D:\\Python\\ch08")
print("HEX: \x48\x45\x58")

------------------------------------------------------------

x, y = 10, 20
s = "Y= {1} X= {0}".format(x, y)
print(s)
s = "y = {a} x = {b}".format(b=x, a = y)
print(s)
print("整數: {0:5d}".format(456))
print("整數: {0:05d}".format(123))
print("浮點數: {0:6.3f}".format(123.45678))
print("二進位: {0:b}".format(200))
print("八進位: {0:o}".format(200))
print("十六進位: {0:x}".format(200))

------------------------------------------------------------

str1 = 'welcome to python'
s = str1.capitalize()
print("str1.capitalize() = " + s)
s = str1.title()
print("str1.title() = " + s)
s = str1.swapcase()
print("str1.swapcase() = " + s)

s = str1.replace('python', 'vcs')
print("str1.replace() = " + s)

------------------------------------------------------------

d1 = {x: x*x for x in range(10)}
print(d1)
d2 = {x: x*x for x in range(10) if x % 2 == 0}
print(d2)

lst1 = [x for x in range(10)]
print(lst1)
lst2 = [x+1 for x in range(10)]
print(lst2)
lst3 = [x for x in range(10) if x % 2 == 1]
print(lst3)
lst4 = [x*2 for x in range(10) if x %2 == 1]
print(lst4)

------------------------------------------------------------

# 字元函數
ch1 = "A"
print("ch1 = " + ch1)
a = ord(ch1)
print("ord(ch1) = " + str(a))
a = chr(97)
print("chr(97) = " + a)
a = ord('B')
print("ord('B') = " + str(a))

split的用法(3)
str1 = "This is a pen."
lst1 = str1.split()
print(lst1)
str2 = "Tom,Bob,Mary,Joe,John"
lst2 = str2.split(",")
print(lst2)
str3 = "23\n52\n44\n78"
lst3 = str3.splitlines()
print(lst3)

------------------------------------------------------------

#eval() 和 exec()，能夠將字串轉換成可以運作的程式碼

m = 10
eval("print('Python')")
eval("print(50 + 10)")
eval("print(55 / 13)")
eval("print( m  * 5)")
eval("print('m' * 5)")

a, b, c = 1, 2, 3
eval('print(a, b, c)')                            # 1, 2, 3
eval('print(a, b, c)', {'a':4, 'b':5, 'c':6})     # 4, 5, 6
eval('print(a, b, c)', {'a':4, 'b':5, 'c':6}, {'a':7, 'b':8, 'c':9})   # 7, 8, 9
eval('print(a, b, c)')   # 1, 2, 3

a = eval('x+y',{'x':1,'y':2})
print(a)       # 3

------------------------------------------------------------

字串處理函數
msg = """CIA Mark told CIA Linda that the secret USB had given to CIA Peter"""
print("字串開頭是CIA: ", msg.startswith("CIA"))
print("字串結尾是CIA: ", msg.endswith("CIA"))
print("CIA出現的次數: ",msg.count("CIA"))
msg = msg.replace('Linda','Lxx')
print("新的msg內容 : ", msg)

------------------------------------------------------------

檢查touch

    mtime = None
    atime = None
    try:
        statbuf = os.stat(filename)
        mtime = statbuf.st_mtime
        atime = statbuf.st_atime
        os.chmod(tempname, statbuf[ST_MODE] & 0o7777)

    if preserve_timestamps:
        if atime and mtime:
            try:
                os.utime(filename, (atime, mtime))
            except OSError as msg:
                err('%s: reset of timestamp failed (%r)\n' % (filename, msg))
                return 1

------------------------------------------------------------

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/poetry2.txt'

with open(filename, "rb") as f:
    data = f.read()
if b'\0' in data:
    print(filename, "\tBinary")
else:
    print(filename, "\tASCII")

------------------------------------------------------------

"""Reverse grep.
Usage: rgrep [-i] pattern file
"""

def usage(msg, code=2):
    sys.stdout = sys.stderr
    print(msg)
    print(__doc__)
    sys.exit(code)


usage("not enough arguments")

------------------------------------------------------------

set

consuming_calls = {"sorted", "list", "set", "any", "all", "tuple", "sum",
                   "min", "max", "enumerate"}

print(type(consuming_calls))

------------------------------------------------------------

串的格式化	使用 format

Python 字串可以做一些格式化, 比如說...

message = "你好, 來自{}的{}!".format(bp, name)


"1 美金是 {:.2f} 台幣。".format(30.1077859)
print("平均 = {:.2f}".format(s/5))

list(range(10))
list(range(1,10))
list(range(3, 15))

------------------------------------------------------------    

    factors = []
:
:
    factors = list(set(factors))


list 轉 set 轉 list

這樣可以把重複地排除掉

------------------------------------------------------------

        textvars = dict(
            VER='aaaaa',
            FULLVER='bbbbb',
        )

------------------------------------------------------------

s = "   this is a sample sentance. this is a cat\n "
print(s.capitalize())
print(s.upper())
print(s.upper().casefold())
print(s.count("a"))
print(s.endswith("ce."))
print(s.find("this"))
print(s.split())
print("#".join(s.split()))
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.rfind("is"))
print(s.zfill(50))

------------------------------------------------------------

for name in sorted(players.keys( )):
    print(name)
    print(f"Hi! {name} 我喜歡看你在 {players[name]} 的表現")
    
    
for team in players.values( ):
    print(team)
    
------------------------------------------------------------    

cars = ['honda','bmw','toyota','ford']     
print(f"目前串列car內容 = {cars}")
print("使用sorted()由小排到大")
cars_sorted = sorted(cars)            
print(f"從小排到大的排序串列結果 = {cars_sorted}")
print("-"*60)
print(f"原先串列car內容 = {cars}")
cars_sorted = sorted(cars,reverse=True)            
print(f"從大排到小的排序串列結果 = {cars_sorted}")
print(f"原先串列car內容不變 = {cars}")
print("="*60)
nums = [5, 3, 9, 2]     
print(f"目前串列num內容 = {nums}")
print("使用sorted()由小排到大")
nums_sorted = sorted(nums)            
print(f"從小排到大的排序串列結果 = {nums_sorted}")
print("-"*60)
print(f"原先串列num內容 = {nums}")
nums_sorted = sorted(nums,reverse=True)            
print(f"從大排到小的排序串列結果 = {nums_sorted}")
print(f"原先串列num內容不變 = {nums}")

------------------------------------------------------------

# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.

------------------------------------------------------------

ans = 0                         # 讀者心中的數字
print("猜生日日期遊戲,請回答下列5個問題,這個程式即可列出你的生日")

truefalse = "輸入y或Y代表有, 其它代表無 : "
# 檢測2進位的第1位是否含1
q1 = "有沒有看到自己的生日日期 : \n" + \
     "1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31 \n"
num = input(q1 + truefalse)
print(num)
if num == "y" or num == "Y":
    ans += 1
# 檢測2進位的第2位是否含1
truefalse = "輸入y或Y代表有, 其它代表無 : "
q2 = "有沒有看到自己的生日日期 : \n" + \
     "2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31 \n"
num = input(q2 + truefalse)
if num == "y" or num == "Y":
    ans += 2
# 檢測2進位的第3位是否含1
truefalse = "輸入y或Y代表有, 其它代表無 : "
q3 = "有沒有看到自己的生日日期 : \n" + \
     "4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31 \n"
num = input(q3 + truefalse)
if num == "y" or num == "Y":
    ans += 4
# 檢測2進位的第4位是否含1
truefalse = "輸入y或Y代表有, 其它代表無 : "
q4 = "有沒有看到自己的生日日期 : \n" + \
     "8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31 \n"
num = input(q4 + truefalse)
if num == "y" or num == "Y":
    ans += 8
# 檢測2進位的第5位是否含1
truefalse = "輸入y或Y代表有, 其它代表無 : "
q5 = "有沒有看到自己的生日日期 : \n" + \
     "16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31 \n"
num = input(q5 + truefalse)
if num == "y" or num == "Y":
    ans += 16

print(f"讀者的生日日期是 : {ans}")

------------------------------------------------------------

song = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# 以下是將單字大寫字母全部改成小寫
songLower = song.lower()            # 單字改為小寫

# 將段落的標點符號用空字元取代
for ch in songLower:                
    if ch in ".,?!-*":
        songLower = songLower.replace(ch,'')

# 將文字段落字串轉成串列
songList = songLower.split()        

# 將單字串列處理成字典 
mydict = {wd:songList.count(wd) for wd in songList}
for wd, count in sorted(mydict.items()):
    print(wd, ":", count)                 
    
------------------------------------------------------------

    
------------------------------------------------------------

sc = {'John':80, 'Tom':90, 'Kevin':77}
newsc1 = sorted(sc.items(), key = lambda x:x[0])  # 依照key排序
print("依照人名排序")
for i in range(len(newsc1)):
    print(f"{newsc1[i][0]:5s}:{newsc1[i][1]}")

print("依照分數排序")
newsc2 = sorted(sc.items(), key = lambda x:x[1])  # 依照value排序
for i in range(len(newsc2)):
    print(f"{newsc2[i][0]:5s}:{newsc2[i][1]}")
    
------------------------------------------------------------

DATA = b'Jack is my hero'

f = open(self.fname1, 'wb')
f.write(self.DATA)
f.close()


f = open(self.fname1, 'rb')
finish = f.readline()
f.close()

self.assertEqual(self.DATA, finish)

------------------------------------------------------------

        for k, v in dict.items():
            if k.endswith('_pre') or k.endswith('_post'):
                assert isinstance(v, function)
            elif isinstance(v, function):
                methods.append(k)
        for m in methods:
            pre = dict.get("%s_pre" % m)
            post = dict.get("%s_post" % m)
            if pre or post:
                dict[m] = cls.make_eiffel_method(dict[m], pre, post)

------------------------------------------------------------

print('zip 測試')
def iterate_simul():
    xpts = [1, 5, 4, 2, 10, 7]
    ypts = [101, 78, 37, 15, 62, 99]
    for x, y in zip(xpts, ypts):
        print(x, y)

    a = [1, 2, 3]
    b = ['w', 'x', 'y', 'z']
    for i in zip(a,b):
        print(i)  # 默认是按最短长度

    headers = ['name', 'shares', 'price']
    values = ['ACME', 100, 490.1]
    s = dict(zip(headers,values))

    for name, val in zip(headers, values):
        print(name, '=', val)


if __name__ == '__main__':
    iterate_simul()



------------------------------------------------------------

# 字典转换成XML格式
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring

def dict_to_xml(tag, d):
    """
    Turn a simple dict of key/value pairs into XML
    """
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

if __name__ == '__main__':
    r = dict_to_xml('root', {'鼠':'mouse', '牛':'ox'})
    print(r)
    print(tostring(r))
    r.set('虎', 'tiger')
    print(tostring(r))

------------------------------------------------------------

import shutil
    
image_foldername = 'tmp_images'
filename = 'tmp_countryfood2222.html'
print('存檔檔案 :', filename)
if os.path.exists(filename):  
    os.remove(filename)     # 若有 tmp_countryfood.html 網頁即刪除
if os.path.exists(image_foldername): 
    shutil.rmtree(image_foldername)    # 若有images目錄即刪除
else:
    os.mkdir(image_foldername)        # 若無images目錄即刪除


    #從網址取得檔名
    imgUrl=col['PicURL']
    print(cnt)
    #網址用'/'分隔取最後一筆資料 => *.jpg
    filename = imgUrl.split('/')[-1] #擷取圖片名稱
    print('圖片網址：', imgUrl)
    print('圖片檔名：', filename)

    #網址用'/'分隔取最後一筆資料 => *.jpg
    picName=row['PicURL'].split('/')[-1]
    print('圖片網址：', row['PicURL'])
    print('圖片檔名：', picName)
    

        #建立取得圖片的 response 物件
        response=requests.get(imgUrl) 
        f=open((image_foldername+'/'+filename),'wb')    #開啟圖片檔案                    
        f.write(response.content)  # 將response.content二進位內容寫入檔案
        print(filename,'下載完畢')



filename = 'aaaaa.html'

print("%s 網頁建置完成" % (filename))

------------------------------------------------------------


def checkpassword(password):
    #檢查密碼長度必須是5到10個字元
    length = len(password)  # 密碼長度
    if length < 5:  # 密碼長度不足
        raise Exception("密碼長度不足")
    if length > 10:  # 密碼長度太長
        raise Exception("密碼長度太長")
    print("密碼長度正確")

print('測試 raise Exception')

password = "lion-mouse"

try:
    checkpassword(password)
except Exception as err:
    print("密碼檢查異常發生: ", str(err))


------------------------------------------------------------


def passWord(pwd):
    # 檢查密碼長度必須是5到8個字元
    pwdlen = len(pwd)  # 密碼長度
    if pwdlen < 5:  # 密碼長度不足
        raise Exception("密碼長度不足")
    if pwdlen > 8:  # 密碼長度太長
        raise Exception("密碼長度太長")
    print("密碼長度正確")


for pwd in ("aaabbbccc", "aaa", "aaabbb"):  # 測試系列密碼值
    try:
        passWord(pwd)
    except Exception as err:
        print("密碼長度檢查異常發生: ", str(err))







'''
