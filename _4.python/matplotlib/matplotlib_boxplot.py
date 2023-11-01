# boxplot 集合

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


N = 11
y = np.arange(N)
y = np.random.randn(N)
print(y)
#y[3]=10
print(y)

#盒鬚圖（Box plot）
plt.boxplot(y) #箱形圖  便於確認資料分布的視覺化方法

plt.show()


print('------------------------------------------------------------')	#60個

x = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0,
     1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
     0, 0]

print(np.max(x))
print(np.mean(x))
print(np.min(x))

plt.boxplot(x)
plt.show()


#python numpy求四分位數
	
import numpy as np
ages=[3,3,6,7,7,10,10,10,11,13,30]
lower_q = np.quantile(ages,0.25,interpolation='lower')#下四分位數
higher_q = np.quantile(ages,0.75,interpolation='higher')#上四分位數
int_r=higher_q-lower_q#四分位距
print('下四分位數 :', lower_q)
print('上四分位數 :', higher_q)
print('四分位距 :', int_r)



'''     
labels = ['x軸標記']
plt.boxplot(x, labels = labels)
plt.show()



     

plt.boxplot(x, whis = 1.8)
plt.show()

'''
      
import math

def percentile(N, percent, key=lambda x:x):
    N = sorted(N)
    k = (len(N)-1) * percent
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return key(N[int(k)])
    d0 = key(N[int(f)]) * (c-k)
    d1 = key(N[int(c)]) * (k-f)
    return round(d0+d1, 5)

print('計算10分位數')
print(percentile([1,2,3,4,5], 0.1))

print('計算50分位數')
print(percentile([1,2,3,4,5], 0.5))


print('計算90分位數')
print(percentile([1,2,3,4,5], 0.9))

print('numpy 计算分位数')

import numpy as np
nums = [1,2,3,4,5]
print(np.percentile(nums, [10, 50, 90]))

print('pandas 计算分位数')
import pandas as pd
data = pd.DataFrame({
    'col': [1,2,3,4,5]
})
print(data.head())
print('计算分位数，分别得到10分位数，50分位数，90分位数')

print(data['col'].quantile([0.1,0.5,0.9]))

print(data['col'].quantile(0.1))


print('用numpy计算分位数')

print(np.percentile(data['col'], [10, 50, 90]))








