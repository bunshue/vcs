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

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = '新進測試 2', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)


#第二張圖
plt.subplot(232)


#第三張圖
plt.subplot(233)


#第四張圖
plt.subplot(234)


#第五張圖
plt.subplot(235)


#第六張圖
plt.subplot(236)


plt.show()

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



'''
print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np

data = np.random.randn(200)
np.mean(data)


ax = plt.subplot()
sns.distplot(data, kde=False, ax=ax)
_ = ax.set(title='Histogram of observed data', xlabel='x', ylabel='# observations');


plt.show()

'''

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

import random
import math
import matplotlib.pyplot as plt

X = []
Y = []
for i in range(1000):
    theta = 2 * random.random() * math.pi
    r= random.random() * 5
    x=math.cos(theta)* r +5
    y=math.sin(theta)* r + 5
    X.append(x)
    Y.append(y)




plt.figure(figsize=(6,6))
plt.scatter(X,Y)
len(X)
plt.axis([0, 10, 0, 10])

plt.show()

print('------------------------------------------------------------')	#60個

import random
import math
import matplotlib.pyplot as plt

X = []
Y = []
for i in range(1000):
    x=random.randint(0,10)+random.random()
    y=random.randint(0,10)+random.random()
    if ((x-5)**2 + (y-5)**2) >25:
        #print('Reject ({0},{1})'.format(x,y))
        continue
    else :
        X.append(x)
        Y.append(y)
print(len(X))        

plt.figure(figsize=(6,6))
plt.scatter(X,Y)
print(len(X))
plt.axis([0, 10, 0, 10])

plt.show()


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個





