import sys
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

print('一次畫一大堆範例... 久')

#1. 讀入 MNSIT 數據集
from keras.datasets import mnist

#(x_train, y_train), (x_test, y_test) = mnist.load_data() 改成以下5行
path = 'C:/_git/vcs/_4.python/ml/mnist.npz'
mnist = np.load(path)  
x_train, y_train = mnist['x_train'], mnist['y_train']  
x_test, y_test = mnist['x_test'], mnist['y_test']  
mnist.close()  

fig = plt.figure(figsize = (8, 8))
for i in range(256):
    ax = plt.subplot2grid((16, 16), (int(i / 16), int(i % 16)))
    ax.imshow(x_train[i], cmap = plt.cm.gray)
    ax.axis('off')
plt.suptitle('畫前100筆資料')
plt.show()

print('------------------------------------------------------------')	#60個


