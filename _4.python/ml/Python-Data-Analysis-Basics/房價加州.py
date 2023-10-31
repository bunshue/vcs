"""
加州房價

用線性迴歸預測加州房價


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
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()

print('看一下資料集的描述')
print(housing.DESCR)

print('加州房價資料庫說明資料 :\n', housing['DESCR'])

print('feature names :', housing.feature_names)
print('data shape :', housing.data.shape)
print('target shape :', housing.target.shape)

sys.exit()
print('------------------------------------------------------------')	#60個

print('len :', len(housing))
print('type :', type(housing))

#單獨把特徵的名稱找出來。
print('特徵的名稱 :', housing.feature_names)
#可以看看說明, 一共有 8 個特徵 (features), 20,640 筆數據。

print('------------------------------------------------------------')	#60個

#特徵的數據是在 .data 中, 現在來建一個 Data Frame。
cal = pd.DataFrame(housing.data, columns = housing.feature_names)
print(cal.head())

print('------------------------------------------------------------')	#60個

#把要預測的房價也放進來。
cal['MEDV'] = housing.target
print(cal.head())

print('------------------------------------------------------------')	#60個

#可以用 seaborn 畫個美美的房價分佈圖。

import seaborn as sns
sns.distplot(cal.MEDV, bins = 30)
plt.show()

#再來可以做一個相關係數矩陣 (Correlation Matrix), 並且畫出 "heat map"。
correlation_matrix = cal.corr().round(2)

sns.set(rc = {'figure.figsize' : (11.7, 8.27)})

sns.heatmap(correlation_matrix, annot = True)
plt.show()


#接下來我們把輸入輸出分好
X = cal.loc[:, "MedInc" : "Longitude"].values
Y = cal.MEDV

#切一下訓練及測試資料

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, Y,
                                                    test_size = 0.2,
                                                    random_state = 9487)

#三部曲打造函數學習機

from sklearn.linear_model import LinearRegression

#第一部曲: 開一台函數學習機
model = LinearRegression()

#第二部曲: 訓練
model.fit(x_train, y_train)

LinearRegression()

#第三部曲: 測試
y_predict = model.predict(x_test)

#現在來計算我們預測的成績。
from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test, y_predict)
r2 = r2_score(y_test, y_predict)

print("MSE =", mse)
print("R2 =", r2)

#用很有創意的方法, 把圖給畫出來。

plt.scatter(y_test, y_predict)
plt.xlim(0, 5.5)
plt.ylim(0, 5.5)
plt.plot([0, 5.5], [0, 5.5], 'r')

plt.show()
'''
print('------------------------------------------------------------')	#60個

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
cal = fetch_california_housing()

#跟之前一樣，把「給模型當作參考的特徵」當成 X， 「要模型去學的答案」叫做 Y

X = cal.data

Y = cal.target

#為了怕模型 overfit，我們需要把資料分成訓練資料跟測試資料
#還要養成沒事查看 shape 以防手滑的好習慣

x_train, x_test, y_train, y_test = train_test_split(X, Y,
                                                    test_size = 0.2,
                                                    random_state = 42)

print("x_train:", x_train.shape, " x_test:", x_test.shape, " y_train:", y_train.shape, " y_test:", y_test.shape, )

#x_train: (16512, 8)  x_test: (4128, 8)  y_train: (16512,)  y_test: (4128,)

#因為已經很熟了，所以「叫出函數學習機」，「訓練函數學習機」，「把函數學習機拿來用」 可以一氣呵成！

regr = LinearRegression()
regr.fit(x_train, y_train)
y_predict = regr.predict(x_test)

#為了看看模型是不是學的好棒棒，把「真實的結果」當作 x 座標， 「預測的結果」當作 y 座標描點在圖上
#為了方便比較，再畫一條對角線當作比較基準！
#(學得好的話，所有的點應該都會在對角線上，表示結果一樣)

plt.scatter(y_test, y_predict)
plt.plot([0, 5], [0, 5], 'r')
plt.xlabel('True Price')
plt.ylabel('Predicted Price')
plt.show()

print('------------------------------------------------------------')	#60個

from sklearn.datasets import fetch_california_housing
cal = fetch_california_housing()

#回顧一下所有 features 的名稱。

print(cal.feature_names)

#看各個 feature 和房價的闗係圖。

X = cal.data
Y = cal.target

plt.figure(figsize=(8, 10))

for i, feature in enumerate(cal.feature_names):
    plt.subplot(5, 3, i+1)
    plt.scatter(X[:, i], Y, s=1)
    plt.ylabel('price')
    plt.xlabel(feature)
    plt.tight_layout()

plt.show()

print('------------------------------------------------------------')	#60個

print('作業完成')

