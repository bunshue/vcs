"""
在金融預測上的應用

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

'''
#要平均值 μ, 標準差 σ 的時候呢?

μ = 87

σ = 2.5

eggs = np.random.randn(100) * σ + μ

#我們來檢查這樣生出的平均值、標準差是不是我們想的那樣。

print('平均值 :', eggs.mean())

#87.3032349761459

print('標準差 :', eggs.std())

#2.411544933383249

import seaborn as sns

sns.distplot(eggs)
plt.show()
'''
print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

"""
06. 神經網路

連 SVM 都沒辦法, 那一定是方法還不夠高級, 所以我們用更高級的神經網路來做做看!
"""

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD


#[2] 打造我們的神經網路函數學習機

model = Sequential()

model.add(Dense(20, input_dim=5))

model.add(Activation('relu'))

model.add(Dense(20))

model.add(Activation('relu'))

model.add(Dense(1))

model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#看一下我們神經網路長什麼樣子, 有沒有做錯。

model.summary()


""" TBD
#[3] 訓練

model.fit(x_train, yb_train, batch_size=100, epochs=20)


#[4] 預測

#看起來不太妙, 我們來試試預測...

NN_pred = model.predict_classes(x_test)

YP_NN = yb_test[(NN_pred==1).ravel()]

len(YP_NN)

458

len(YP_NN[YP_NN == 1])

246

246/458

0.537117903930131

結果真是慘慘慘, 怎麼會這樣呢?

"""


print('------------------------------------------------------------')	#60個



print('作業完成')

