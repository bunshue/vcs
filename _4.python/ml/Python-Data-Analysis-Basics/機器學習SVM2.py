"""

"""

import numpy as np
import matplotlib.pyplot as plt 
from sklearn.svm import SVC

#把我們的模擬資料定義起來

X = np.array([[-3, 2], [-6, 5], [3, -4], [2, -8], [-4, 4], [-5, 3], [4, -6], [0,-1], [-2,-1]])
Y = np.array([1, 3, 2, 2, 3, 3, 2, 1, 1])

#打開一個 SVM 的函數學習機 (SVC 是 SVM 裏面負責做分類的)
#之後開始訓練

clf = SVC(gamma='auto')

clf.fit(X, Y)

"""
SVC(C=1.0, break_ties=False, cache_size=200, class_weight=None, coef0=0.0,
,    decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
,    max_iter=-1, probability=False, random_state=None, shrinking=True,
,    tol=0.001, verbose=False)
"""
#畫一個所有 features 的範圍也就是 X，在二維平面上的分布圖

x_min, x_max, y_min, y_max = (-6, 5, -8, 5)

xx = np.linspace(x_min, x_max, x_max-x_min+1)
yy = np.linspace(y_min, y_max, y_max-y_min+1)

xc, yc = np.meshgrid(xx, yy)
xc = xc.ravel()
yc = yc.ravel()

plt.scatter(xc, yc)
plt.show()

#把這些點代入訓練好的模型進行預測，再用預測的結果作為顏色的表示(不同預測結果，顏色會不一樣)

mesh_X = list(zip(xc, yc))
mesh_predicted_Y = clf.predict(mesh_X)
plt.scatter(xc, yc, c=mesh_predicted_Y)
plt.show()

