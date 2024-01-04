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

print('線性回歸的範例 1')

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
X = [[1], [2], [3], [4], [5]]
y = [88, 72, 90, 76, 92]
lm.fit(X, y)
print('第6次考試分數：', lm.predict([[6]]))

print('線性回歸的範例 2')

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
X = [[1], [2], [3], [4], [5]]
y = [1, 4, 9, 16, 25]
lm.fit(X, y)

xx = np.linspace(0,10,11)
yy = np.linspace(0,10,11)
for i in range(11):
    print(i)
    print('第',i,'項', lm.predict([[i]]))
    xx[i] = i
    yy[i] = lm.predict([[i]])

plt.plot(X,y,'ro-')
plt.plot(xx,yy,'go:')


plt.show()

print("------------------------------------------------------------")  # 60個

