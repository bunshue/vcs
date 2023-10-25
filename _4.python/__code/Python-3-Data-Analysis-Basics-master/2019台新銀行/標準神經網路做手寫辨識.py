"""
標準神經網路做手寫辨識


"""

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


print('------------------------------------------------------------')	#60個


import numpy as np

import matplotlib.pyplot as plt

'''
2-2 讀入 MNIST 數據庫

MNIST 是有一堆 0-9 的手寫數字圖庫。有 6 萬筆訓練資料, 1 萬筆測試資料。
它是 "Modified" 版的 NIST 數據庫, 原來的版本有更多資料。
這個 Modified 的版本是由 LeCun, Cortes, 及 Burges 等人做的。可以參考這個數據庫的原始網頁。

MNIST 可以說是 Deep Learning 最有名的範例, 它被 Deep Learning 大師 Hinton 稱為「機器學習的果蠅」。
2.2.1 由 Keras 讀入 MNIST

Keras 很貼心的幫我們準備好 MNIST 數據庫, 我們可以這樣讀進來 (第一次要花點時間)。
'''

from keras.datasets import mnist

#Using TensorFlow backend.

(x_train, y_train), (x_test, y_test) = mnist.load_data()





print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('作業完成')

