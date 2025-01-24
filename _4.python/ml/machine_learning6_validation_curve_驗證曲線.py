"""

machine_learningA_validation_curve_驗證曲線


"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline


def PolynomialRegression(degree=2, **kwargs):
    return make_pipeline(PolynomialFeatures(degree), LinearRegression(**kwargs))


print("------------------------------------------------------------")  # 60個


def makedata(N, err=1.0, rseed=1):
    # 建立資料
    rng = np.random.RandomState(rseed)
    x = rng.rand(N, 1) ** 2
    y = 10 - 1.0 / (x.ravel() + 0.1)
    if err > 0:
        y += err * rng.randn(N)
    return x, y


x, y = makedata(40)


# We can now visualize our data, along with polynomial fits of several degrees

sns.set()
x_test = np.linspace(-0.1, 1.1, 500)[:, None]
plt.scatter(x.ravel(), y, color="black")
axis = plt.axis()
for degree in [1, 3, 5]:
    y_test = PolynomialRegression(degree).fit(x, y).predict(x_test)
    plt.plot(x_test.ravel(), y_test, label="degree={0}".format(degree))
plt.xlim(-0.1, 1.0)
plt.ylim(-2, 12)
plt.legend(loc="best")
plt.show()

# We can make progress in this by visualizing the validation curve for this particular data and model, we can do this straightforwardly using the validation_curve convenience routine provided by Scikit-Learn. Given a model, data, parameter name, and a range to explore, this function will automatically compute both the training score and validation score across the range

from sklearn.model_selection import validation_curve

degree = np.arange(0, 21)

""" fail
train_score, val_score = validation_curve(PolynomialRegression(), x, y, 'polynomialfeatures__degree',degree, cv=7)
    
plt.plot(degree, np.median(train_score, 1), color='blue', label='training score')
plt.plot(degree, np.median(val_score, 1), color='red', label='validation score')
plt.legend(loc='best')
plt.ylim(0, 1)
plt.xlabel('degree')
plt.ylabel('score')
plt.show()
"""

# From the validation curve, we can read off that the optimal trade-off between bias and variance is found for a third-order polynomial; we can compute and display this fit over the original data as follows:

plt.scatter(x.ravel(), y)
lim = plt.axis()
y_test = PolynomialRegression(3).fit(x, y).predict(x_test)
plt.plot(x_test.ravel(), y_test)
plt.axis(lim)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
