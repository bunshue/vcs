# 熱圖 heatmap 集合

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'

import sys
import matplotlib.pyplot as plt
import numpy as np

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

import pandas as pd
import seaborn as sns #海生, 自動把圖畫得比較好看

#熱圖
#咖啡廳每月商品銷售量資料

# 載入資料與定義資料
filename = '../numpy_pandas/data/cafe.csv'
cafe = pd.read_csv(filename, header=0, index_col=0)
print(cafe)

#sns.set(font="meiryo")
sns.heatmap(cafe)

sns.heatmap(cafe, linewidths=.1, annot=True, fmt="d")

sns.heatmap(cafe, linewidths=.5, cmap="coolwarm", fmt="d", annot=True)

plt.show()





print('------------------------------------------------------------')	#60個


#熱圖
#咖啡廳每月商品銷售量資料

# 載入資料與定義資料
filename = '../numpy_pandas/data/cafe.csv'
cafe = pd.read_csv(filename, header=0, index_col=0)
print(type(cafe))
print(cafe)
print(cafe.shape)


df = pd.DataFrame([[65,92,78,83,70], 
                   [90,72,76,93,56], 
                   [81,85,91,89,77], 
                   [79,53,47,94,80]])
print('原資料 :\n', df, '\n')

#sns.set(font="meiryo")
sns.heatmap(df)

sns.heatmap(df, linewidths=.1, annot=True, fmt="d")

sns.heatmap(df, linewidths=.5, cmap="coolwarm", fmt="d", annot=True)

plt.show()






print('------------------------------------------------------------')	#60個


