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
'''
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

'''
print('------------------------------------------------------------')	#60個

listdata = [[15, 13, 10, 13, 15],
            [12, 8, 5, 8, 12],
            [10, 5, 0, 5, 10],
            [12, 8, 5, 8, 12],
            [15, 13, 10, 13, 15]]

"""
listdata = [[ 1.,          0.91141626,  0.99267261,  0.99020915,  0.12721213,  0.328172,       -0.1305195,  -0.23568907],
            [ 0.91141626,  1.,          0.95445981,  0.9599327,   0.52408571,  0.687798,       0.28900806,  0.18508259],
            [ 0.99267261,  0.95445981,  1.,          0.99982106,  0.24613326,  0.43991025,       -0.00976181, -0.11653121],
            [ 0.99020915,  0.9599327,   0.99982106,  1.,          0.26442422,  0.45681976,       0.009156,   -0.09772227],
            [ 0.12721213,  0.52408571,  0.24613326,  0.26442422,  1.,          0.97869093,       0.96678711,  0.93395042],
            [ 0.328172,    0.687798,    0.43991025,  0.45681976,  0.97869093,  1.,       0.89370463,  0.84066014],
            [-0.1305195,   0.28900806, -0.00976181,  0.009156,    0.96678711,  0.89370463,    1.,          0.99427726],
            [-0.23568907,  0.18508259, -0.11653121, -0.09772227,  0.93395042,  0.84066014, 0.99427726,  1.        ]]
"""

ndarray2d = np.array(listdata)
print(ndarray2d)
print('維度', ndarray2d.ndim)
print('形狀', ndarray2d.shape)
print('數量', ndarray2d.size)

ndarray2d = np.array(listdata)
print(type(ndarray2d))
print(ndarray2d)

sns.heatmap(ndarray2d, cmap = 'Reds')
#sns.heatmap(ndarray2d, cmap="coolwarm")
#sns.heatmap(ndarray2d, annot = True)

plt.show()


print('------------------------------------------------------------')	#60個


