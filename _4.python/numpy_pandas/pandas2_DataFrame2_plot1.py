import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個
#                  2015,2016,2017,2018,2019
df = pd.DataFrame([[250,320,300,312,280],   #北部
                   [280,300,280,290,310],   #中部
                   [220,280,250,305,250]],  #南部
                   index = ['北部','中部','南部'],
                   columns = [2015,2016,2017,2018,2019])

g0 = df.plot(kind = 'line', title = '線圖', figsize = [10,5])
g1 = df.plot(kind = 'bar', title = '長條圖', figsize = [10,5])
g2 = df.plot(kind = 'barh', title = '橫條圖', figsize = [10,5])
g3 = df.plot(kind = 'bar', stacked = True, title = '堆疊圖', figsize = [10,5])

plt.show()

print('------------------------------------------------------------')	#60個

#                  2015,2016,2017,2018,2019
df = pd.DataFrame([[250,320,300,312,280],   #北部
                   [280,300,280,290,310],   #中部
                   [220,280,250,305,250]],  #南部
                   index = ['北部','中部','南部'],
                   columns = [2015,2016,2017,2018,2019])
g1 = df.iloc[0].plot(kind = 'line', legend = True, xticks = range(2015, 2020), title = '公司分區年度銷售表', figsize = [10, 5])
g1 = df.iloc[1].plot(kind = 'line', legend = True, xticks = range(2015, 2020))
g1 = df.iloc[2].plot(kind = 'line', legend = True, xticks = range(2015, 2020))

plt.show()

print('------------------------------------------------------------')	#60個

#                  2015,2016,2017,2018,2019
df = pd.DataFrame([[250,320,300,312,280],   #北部
                   [280,300,280,290,310],   #中部
                   [220,280,250,305,250]],  #南部
                   index = ['北部','中部','南部'],
                   columns = [2015,2016,2017,2018,2019])
df.plot(kind = 'pie', subplots = True, figsize = [14, 6]) # 繪圖 plot

plt.show()


print('------------------------------------------------------------')	#60個


# 創造一些隨機資料 create some data with random value
ts = pd.Series(np.random.randn(1000), index = pd.date_range('1/1/2000', periods = 1000))
ts = ts.cumsum() # 計算累積值 cumulative sum
df = pd.DataFrame(np.random.randn(1000, 4), index = ts.index, columns = list('ABCD'))
df = df.cumsum()

df.plot()       # 繪圖 plot

plt.show()

print('------------------------------------------------------------')	#60個

#     "國文", "數學", "英文", "自然", "社會"]
datas = [[65,92,78,83,70],  #學生A
         [90,72,76,93,56],  #學生B
         [81,85,91,89,77],  #學生C
         [79,53,47,94,80]]  #學生D
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns = columns,  index = indexs)
df.plot(kind = 'bar', title = '一年甲班成績單', fontsize = 12)

plt.show()

print('------------------------------------------------------------')	#60個

