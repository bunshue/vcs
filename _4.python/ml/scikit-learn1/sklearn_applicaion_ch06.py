"""
Scikit-learn 詳解與企業應用_機器學習最佳入門與實戰

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#06_01_logistic_regression_validation

#證明 Exp(log(x)) = x

import math

for i in range(1, 101):
    assert round(math.e ** math.log(i), 6) == i

#證明 log(1/x) = - log(x)

for i in range(1, 101):
    assert round(math.log(i), 6) == -round(math.log(1/i), 6)

cc = math.log(100), -math.log(1/100)
print(cc)

#計算羅吉斯函數的上限與下限

from sympy import *
import numpy as np
 
x = symbols('x')
expr = 1/(1 + np.e **(-x))
limit(expr, x, -1000), limit(expr, x, np.inf)

#不使用 limit

cc = 1/(np.e ** np.inf)
print(cc)

#繪製羅吉斯函數

import matplotlib.pyplot as plt

x = np.linspace(-6, 6, 101)
y = 1/(1 + np.e **(-x))
plt.plot(x, y)
plt.axhline(0, linestyle='-.', c='r')
plt.axhline(1, linestyle='-.', c='r');
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#06_02_logistic_regression_SGD
#以梯度下降法求解羅吉斯迴歸

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets

#載入資料集

iris = datasets.load_iris()

# 只取前兩個特徵，方便繪圖
X = iris.data[:, :2]
# 只取前兩個類別
y = (iris.target != 0) * 1

plt.figure(figsize=(10, 6))
plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='b', label='0')
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='r', label='1')
plt.legend()
plt.show()

#建立羅吉斯迴歸類別

class LogisticRegression:
    def __init__(self, lr=0.01, num_iter=100000, fit_intercept=True, verbose=False):
        self.lr = lr
        self.num_iter = num_iter
        self.fit_intercept = fit_intercept
        self.verbose = verbose
    
    # 加入偏差項(1)至X
    def __add_intercept(self, X):
        intercept = np.ones((X.shape[0], 1))
        return np.concatenate((intercept, X), axis=1)
    
    # 羅吉斯函數
    def __sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    # 損失函數
    def __loss(self, h, y):
        return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()
    
    # 以梯度下降法訓練模型
    def fit(self, X, y):
        if self.fit_intercept:
            X = self.__add_intercept(X)
        
        # 權重初始值給 0
        self.theta = np.zeros(X.shape[1])
        
        # 正向傳導與反向傳導
        for i in range(self.num_iter):
            # WX
            z = np.dot(X, self.theta)
            h = self.__sigmoid(z)
            # 梯度
            gradient = np.dot(X.T, (h - y)) / y.size
            # 更新權重
            self.theta -= self.lr * gradient
            
            # 依據更新的權重計算損失
            z = np.dot(X, self.theta)
            h = self.__sigmoid(z)
            loss = self.__loss(h, y)
            
            # 列印損失
            if(self.verbose ==True and i % 10000 == 0):
                print(f'loss: {loss} \t')
    
    # 預測機率
    def predict_prob(self, X):
        if self.fit_intercept:
            X = self.__add_intercept(X)
    
        return self.__sigmoid(np.dot(X, self.theta))
    
    # 預測
    def predict(self, X):
        return self.predict_prob(X).round()

#模型訓練

model = LogisticRegression(lr=0.1, num_iter=300000)
model.fit(X, y)

#預測

preds = model.predict(X)
cc = (preds == y).mean()
print(cc)

print("羅吉斯迴歸係數")

print(model.theta)

#array([-25.89066442,  12.523156  , -13.40150447])

#分類結果繪圖

plt.figure(figsize=(10, 6))
plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='b', label='0')
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='r', label='1')
plt.legend()
x1_min, x1_max = X[:,0].min(), X[:,0].max(),
x2_min, x2_max = X[:,1].min(), X[:,1].max(),
xx1, xx2 = np.meshgrid(np.linspace(x1_min, x1_max), np.linspace(x2_min, x2_max))
grid = np.c_[xx1.ravel(), xx2.ravel()]
probs = model.predict_prob(grid).reshape(xx1.shape)
plt.contour(xx1, xx2, probs, [0.5], linewidths=1, colors='black');
plt.show()

#以 Scikit-learn 驗證

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(C=1e20)
model.fit(X, y)

preds = model.predict(X)
cc = (preds == y).mean()
print(cc)

cc = model.intercept_, model.coef_
print(cc)

plt.figure(figsize=(10, 6))
plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color='b', label='0')
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color='r', label='1')
plt.legend()
x1_min, x1_max = X[:,0].min(), X[:,0].max(),
x2_min, x2_max = X[:,1].min(), X[:,1].max(),
xx1, xx2 = np.meshgrid(np.linspace(x1_min, x1_max), np.linspace(x2_min, x2_max))
grid = np.c_[xx1.ravel(), xx2.ravel()]
probs = model.predict_proba(grid)[:,1].reshape(xx1.shape)
plt.contour(xx1, xx2, probs, [0.5], linewidths=1, colors='black');
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#06_03_logistic_regression_attrition

#員工流失預測

from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

#載入資料集

df =pd.read_csv('./data/WA_Fn-UseC_-HR-Employee-Attrition.csv')
cc = df.head()
print(cc)

#2. 資料清理、資料探索與分析

cc = df.isna().sum()
print(cc)

# 觀察資料集彙總資訊
cc = df.info()
#print(cc)

# 描述統計量
cc = df.describe()
print(cc)

#繪圖

# y 各類別資料筆數統計
import seaborn as sns
sns.countplot(x=df['Attrition'])
plt.show()

# 以Pandas函數統計各類別資料筆數
cc = df['Attrition'].value_counts()
print(cc)

print("檢查與時間有關的特徵相關性")

import matplotlib.pyplot as plt
import numpy as np

# 設定關聯度上限為 0.4
max_corr = 0.4
time_params=['Age','TotalWorkingYears','YearsAtCompany','YearsInCurrentRole',
             'YearsSinceLastPromotion','YearsWithCurrManager']
# 計算關聯度
corr_df=df[time_params].corr().round(2)

# 繪製熱力圖
plt.figure(figsize=(8,5))
mask = np.zeros_like(corr_df)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(7, 5))
    ax = sns.heatmap(corr_df, mask=mask,vmax=max_corr, square=True, 
                     annot=True, cmap="YlGnBu")
plt.show()

# 刪除欄位
df.drop({'TotalWorkingYears','YearsInCurrentRole','YearsSinceLastPromotion',
         'YearsWithCurrManager'}, axis=1, inplace=True)

print("檢查與薪資(Salary)有關的特徵相關性")

salary_params=['DailyRate','HourlyRate','MonthlyIncome','MonthlyRate',
               'PercentSalaryHike','StockOptionLevel']
# 計算關聯度
corr_df=df[salary_params].corr().round(2)

# 繪製熱力圖
plt.figure(figsize=(8,5))
mask = np.zeros_like(corr_df)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(7, 5))
    ax = sns.heatmap(corr_df, mask=mask,vmax=max_corr, square=True, 
                     annot=True, cmap="YlGnBu");
plt.show()


print("找出所有類別變數，並顯示其類別")

df.select_dtypes('object').head()
print('Levels of categories: ')
for key in df.select_dtypes('object').keys():
    print(key ,':' ,df[key].unique())

print("進行One-hot encoding")

df2 = pd.get_dummies(df,columns=df.select_dtypes('object').keys(), 
                   prefix=df.select_dtypes('object').keys())
cc = df2.keys()
print(cc)
      
print("刪除One-hot encoding的第一個類別欄位(base category)")

df2.drop({'Attrition_No','BusinessTravel_Non-Travel','Department_Human Resources',
         'EducationField_Human Resources','Gender_Female', 'MaritalStatus_Single',
          'OverTime_No'}, axis=1,inplace=True)
cont_vars=df2.select_dtypes('int').keys()
""" NG
dummies= df2.select_dtypes('uint8').keys().drop('Attrition_Yes') # 刪除目標變數(Y) 
print(dummies)
"""
print("指定特徵(X)及目標變數(Y)")

X = df2.drop('Attrition_Yes', axis=1)
y = df2['Attrition_Yes']

#3. 不須進行特徵工程

#4. 資料分割

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)
      
#特徵縮放

scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

#5. 選擇演算法、6. 模型訓練

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
clf.fit(X_train_std, y_train)

#7. 模型評分

# 計算準確率
y_pred = clf.predict(X_test_std)
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

#90.14%

# 混淆矩陣
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

""" NG
#statsmodels 作法

import statsmodels.api as sm

model=sm.Logit(y_train, X_train)
result=model.fit()
print(result.summary())

#顯示權重資訊

stat_df=pd.DataFrame({'coefficients':result.params, 'p-value': result.pvalues,
                      'odds_ratio': np.exp(result.params)})
print(stat_df)

print("篩選重要的特徵變數")

significant_params=stat_df[stat_df['p-value']<=0.05].index
print(significant_params)

print("勝負比(Odds)")

cc = stat_df.loc[significant_params].sort_values('odds_ratio', ascending=False)['odds_ratio']
print(cc)
      
print("最後底定的模型：只保留重要的特徵變數")

y=df2['Attrition_Yes']
X=df2[significant_params]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model=sm.Logit(y_train,X_train)
result=model.fit()
print(result.summary())
"""

"""
8. 模型評估

9. 模型佈署

10.模型預測
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#06_04_logistic_regression_with_nonlinear_data

#以二次迴歸預測世界人口數

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#載入資料集

from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split

X, y = make_circles(n_samples=1_000, factor=0.3, noise=0.05, random_state=0)

# 資料切割
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)

# 繪製訓練及測試資料
_, (train_ax, test_ax) = plt.subplots(ncols=2, sharex=True, sharey=True, figsize=(8, 4))
train_ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train)
train_ax.set_ylabel("Feature #1")
train_ax.set_xlabel("Feature #0")
train_ax.set_title("Training data")

test_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
test_ax.set_xlabel("Feature #0")
_ = test_ax.set_title("Testing data")
plt.show()

#使用Scikit-Learn LinearRegression類別驗算

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()
clf.fit(X_train, y_train)
#cc = clf.coef_, lr.intercept_
#print(cc)

#計算準確率

from sklearn.metrics import accuracy_score

y_pred = clf.predict(X_test)
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

#48.80%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#06_05_knn_iris

#鳶尾花(Iris)品種的辨識

from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#載入資料集

ds = datasets.load_iris()

#2. 資料清理、資料探索與分析

import pandas as pd
df = pd.DataFrame(ds.data, columns=ds.feature_names)
print(df)

y = ds.target
print(y)

print(ds.target_names)

# 箱型圖
import seaborn as sns
sns.boxplot(data=df)
plt.show()

# 是否有含遺失值(Missing value)
cc = df.isnull().sum()
print(cc)

# y 各類別資料筆數統計
import seaborn as sns
sns.countplot(x=y)
plt.show()

# 以Pandas函數統計各類別資料筆數
cc = pd.Series(y).value_counts()
print(cc)

#3. 不須進行特徵工程

#4. 資料分割

# 指定X，並轉為 Numpy 陣列
X = df.values

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

print(y_train)

#特徵縮放

scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

#5. 選擇演算法

from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=5)

#6. 模型訓練

clf.fit(X_train_std, y_train)

#7. 模型評分

# 計算準確率
y_pred = clf.predict(X_test_std)
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

#90.00%

#最近鄰的距離與索引值

cc = clf.kneighbors(X_test[0:1])
print(cc)

#設定距離為加權值

from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=5, weights='distance')
clf.fit(X_train_std, y_train)

# 計算準確率
y_pred = clf.predict(X_test_std)
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

#96.67%

# 混淆矩陣
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred)
                              , display_labels=ds.target_names)
disp.plot()
plt.show()

"""
8. 模型評估

9. 模型佈署

10.模型預測
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#06_06_knn_book_recommender

#以KNN演算法實作書籍推薦

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#載入資料集

# 書籍資料
books = pd.read_csv('C:/_git/vcs/_big_files/Scikit-learn_data/BX-Books.csv', sep=';', on_bad_lines='skip', 
                    low_memory=False, encoding="latin-1")
books.columns = ['ISBN', 'bookTitle', 'bookAuthor', 'yearOfPublication', 'publisher', 
                 'imageUrlS', 'imageUrlM', 'imageUrlL']

# 讀者資料
users = pd.read_csv('C:/_git/vcs/_big_files/Scikit-learn_data/BX-Users.csv', sep=';', on_bad_lines='skip', 
                    encoding="latin-1")
users.columns = ['userID', 'Location', 'Age']


# 評價資料
ratings = pd.read_csv('C:/_git/vcs/_big_files/Scikit-learn_data/BX-Book-Ratings.csv', sep=';', on_bad_lines='skip', 
                      encoding="latin-1")
ratings.columns = ['userID', 'ISBN', 'bookRating']

#資料探索與分析

# 評價資料筆數
print(ratings.shape)

cc = ratings.head(10)
print(cc)

# 評價筆數繪圖
import seaborn as sns

plt.rc("font", size=15)
sns.countplot(x='bookRating', data=ratings)
plt.title('Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Count')

plt.show()

print("大部份書籍都未被評價")

print("書籍資料筆數")
print(books.shape)

print("讀者資料筆數")
print(users.shape)

print("讀者年齡分析")

users.Age.hist(bins=[0, 10, 20, 30, 40, 50, 100])
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.savefig('system2.png', bbox_inches='tight')
plt.show()

print("最多人評分的書籍")

rating_count = pd.DataFrame(ratings.groupby('ISBN')['bookRating'].count())
top_rating = rating_count.sort_values('bookRating', ascending=False).head()
print(top_rating)

print("最多人評分的書籍明細")

most_rated_books = pd.DataFrame(top_rating.index, index=np.arange(5), columns = ['ISBN'])
most_rated_books_summary = pd.merge(most_rated_books, books, on='ISBN')
print(most_rated_books_summary)

print("書籍評價的平均得分")

average_rating = pd.DataFrame(ratings.groupby('ISBN')['bookRating'].mean())
average_rating['ratingCount'] = pd.DataFrame(ratings.groupby('ISBN')['bookRating'].count())
cc = average_rating.sort_values('ratingCount', ascending=False).head()
print(cc)


#觀察: 最多人評分書籍的平均得分並沒有相對比較高
#為確保統計顯著性，只保留讀者評分超過200次者，書籍評分超過100次者

counts1 = ratings['userID'].value_counts()
ratings = ratings[ratings['userID'].isin(counts1[counts1 >= 200].index)]
counts = ratings['bookRating'].value_counts()
ratings = ratings[ratings['bookRating'].isin(counts[counts >= 100].index)]

#User-Item matrix

ratings_pivot = ratings.pivot(index='userID', columns='ISBN').bookRating
userID = ratings_pivot.index
ISBN = ratings_pivot.columns
print(ratings_pivot.shape)
cc = ratings_pivot.head()
print(cc)

#任選一本書 0316666343，計算與其他書籍的相關係數

test_book = '0316666343'
bones_ratings = ratings_pivot[test_book]
# 計算與其他書籍的相關係數
similar_to_bones = ratings_pivot.corrwith(bones_ratings)
corr_bones = pd.DataFrame(similar_to_bones, columns=['pearsonR'])
corr_bones.dropna(inplace=True)

# 結合書籍評價的平均得分
corr_summary = corr_bones.join(average_rating['ratingCount'])

# 只保留評價的平均得分>=300
high_corr_book = corr_summary[corr_summary['ratingCount']>=300] \
        .sort_values('pearsonR', ascending=False).head(10)
print(high_corr_book)

#取得書名

# 取得書名，扣除自己，取前9名
books_corr_to_bones = pd.DataFrame(high_corr_book.index[1:], 
                                  index=np.arange(9), columns=['ISBN'])
corr_books = pd.merge(books_corr_to_bones, books, on='ISBN')
print(corr_books)

#KNN

# 合併評價表及書籍基本資料
combine_book_rating = pd.merge(ratings, books, on='ISBN')
columns = ['yearOfPublication', 'publisher', 'bookAuthor', 'imageUrlS', 
           'imageUrlM', 'imageUrlL']
combine_book_rating = combine_book_rating.drop(columns, axis=1)
cc = combine_book_rating.head()
print(cc)

# 去除未評價書籍
combine_book_rating = combine_book_rating.dropna(axis = 0, 
                                     subset = ['bookTitle'])
# 統計書籍的評價次數
book_ratingCount = (combine_book_rating.
     groupby(by = ['bookTitle'])['bookRating'].
     count().
     reset_index().
     rename(columns = {'bookRating': 'totalRatingCount'})
     [['bookTitle', 'totalRatingCount']]
    )
cc = book_ratingCount.head()
print(cc)

# 合併評價次數及書籍基本資料
rating_with_totalRatingCount = combine_book_rating.merge(book_ratingCount, 
             left_on = 'bookTitle', right_on = 'bookTitle', how = 'left')
cc = rating_with_totalRatingCount.head()
print(cc)

# 顯示評價次數的統計量
pd.set_option('display.float_format', lambda x: '%.3f' % x)
print(book_ratingCount['totalRatingCount'].describe())

# 顯示百分位數
print(book_ratingCount['totalRatingCount'].quantile(np.arange(.9, 1, .01)))

#熱門書籍：只有1%的書籍有超過50次的評分

# 篩選有超過50次評分的書籍
popularity_threshold = 50
rating_popular_book = rating_with_totalRatingCount.query(
    'totalRatingCount >= @popularity_threshold')
cc = rating_popular_book.head()
print(cc)

#合併熱門書籍及讀者基本資料，使用美國及加拿大資料

# 合併熱門書籍及讀者基本資料
combined = rating_popular_book.merge(users, left_on = 'userID', 
                                     right_on = 'userID', how = 'left')

# 只考慮美國及加拿大讀者
us_canada_user_rating = combined[combined['Location'] \
                                 .str.contains("usa|canada")]
us_canada_user_rating=us_canada_user_rating.drop('Age', axis=1)
cc = us_canada_user_rating.head()
print(cc)

print(us_canada_user_rating.shape)

#KNN模型訓練

from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

# 去除重複值
us_canada_user_rating = us_canada_user_rating.drop_duplicates(['userID', 'bookTitle'])
# 產生商品與讀者的樞紐分析表，會有很多 null value，均以0替代
us_canada_user_rating_pivot = us_canada_user_rating.pivot(index = 'bookTitle', 
                                  columns = 'userID', values = 'bookRating').fillna(0)
# csr_matrix：壓縮稀疏矩陣，加速矩陣計算
us_canada_user_rating_matrix = csr_matrix(us_canada_user_rating_pivot.values)

# 找出相似商品，X為每一個讀者的評分
model_knn = NearestNeighbors(metric = 'cosine', algorithm = 'brute')
model_knn.fit(us_canada_user_rating_matrix)

#測試

# 隨機抽取一件商品作預測
query_index = np.random.choice(us_canada_user_rating_pivot.shape[0])
distances, indices = model_knn.kneighbors(np.array(
    us_canada_user_rating_pivot.iloc[query_index, :])
      .reshape(1, -1), n_neighbors = 6)

# 顯示最相似的前5名商品，並顯示距離(相似性)
for i in range(0, len(distances.flatten())):
    if i == 0: # 第一筆是自己
        print(f'{us_canada_user_rating_pivot.index[query_index]} 的推薦:')
    else:
        print(f'{i}: {us_canada_user_rating_pivot.index[indices.flatten()[i]]}' + \
              f', 距離: {distances.flatten()[i]:.2f}:')

#SVD 矩陣分解(Matrix Factorization)

# User-Item Matrix
us_canada_user_rating_pivot2 = us_canada_user_rating.pivot(
    index = 'userID', columns = 'bookTitle', values = 'bookRating').fillna(0)
cc = us_canada_user_rating_pivot2.head()
print(cc)

cc = us_canada_user_rating_pivot2.shape
print(cc)

X = us_canada_user_rating_pivot2.values.T
print(X.shape)

#TruncatedSVD 降維至 12 個

# 萃取 12 個特徵
import sklearn
from sklearn.decomposition import TruncatedSVD

SVD = TruncatedSVD(n_components=12, random_state=17)
matrix = SVD.fit_transform(X)
print(matrix.shape)

# 依據 12 個特徵計算相關係數
corr = np.corrcoef(matrix)
print(corr.shape)

#測試

# 取得 "The Green Mile" 書籍索引值
us_canada_book_list = list(us_canada_user_rating_pivot2.columns)
coffey_hands = us_canada_book_list.index("The Green Mile")
print("The Green Mile 書籍索引值:", coffey_hands)

# 依照索引值找出與其他書的相關係數
corr_coffey_hands  = corr[coffey_hands]
print(corr_coffey_hands)

# 列出相關係數 > 80% 的書籍
us_canada_book_title = us_canada_user_rating_pivot2.columns
cc = list(us_canada_book_title[(corr_coffey_hands >= 0.8)])
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 06_07_surprise_test

#Surprise 測試

from surprise import SVD, KNNBasic
from surprise import Dataset
from surprise import accuracy
from surprise.model_selection import train_test_split

#載入資料集

# 載入內建 movielens-100k 資料集
data = Dataset.load_builtin('ml-100k')
print('user id\titem id\trating\ttimestamp')
cc = data.raw_ratings[:10]
print(cc)

#資料分割

# 切分為訓練及測試資料，測試資料佔 25%
trainset, testset = train_test_split(data, test_size=.25)

#模型訓練

# 使用 KNN 演算法
model = KNNBasic()

# 訓練
model.fit(trainset)

#模型評分

# 測試
predictions = model.test(testset)

# 計算 RMSE
accuracy.rmse(predictions);

#RMSE: 0.9874

#SVD

model = SVD()
model.fit(trainset)
predictions = model.test(testset)
accuracy.rmse(predictions);

#RMSE: 0.9405

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#06_08_knn_from_scratch_iris

#自行開發KNN

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

#公用函數

# 依筆數找出最大類別
def most_common(lst):
    return max(set(lst), key=lst.count)

# 歐幾里得距離(Euclidean distance)
def euclidean(point, data):
    return np.sqrt(np.sum((point - data)**2, axis=1))

#KNN 演算法

class KNN:
    def __init__(self, k=5, dist_metric=euclidean):
        self.k = k
        self.dist_metric = dist_metric

    # 指定訓練資料
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    # 預測
    def predict(self, X_test):
        neighbors = []
        for x in X_test:
            # 計算距離
            distances = self.dist_metric(x, self.X_train)
            # 距離排序
            y_sorted = [y for _, y in sorted(zip(distances, self.y_train))]
            # K個最近鄰
            neighbors.append(y_sorted[:self.k])
        
        # 找出最大類別
        return list(map(most_common, neighbors))

    def evaluate(self, X_test, y_test):
        y_pred = self.predict(X_test)
        accuracy = sum(y_pred == y_test) / len(y_test)
        return accuracy

#載入資料集

X, y = datasets.load_iris(return_X_y=True)

#資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

#特徵縮放

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

#選擇演算法

clf = KNN()

#模型訓練

clf.fit(X_train_std, y_train)

#模型評估

# 計算準確率
y_pred = clf.predict(X_test_std)
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#06_09_naive_bayes_from_scratch

#自行開發高斯單純貝氏分類器

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

#NaiveBayes 演算法

# 貝氏定理 P(y|X) = P(X|y) * P(y) / P(X)
class NaiveBayesClassifier():
    # 計算常態分配的機率(pdf)：P(X)
    def gaussian_density(self, class_idx, x):     
        """
        常態分配 pdf 公式:
        (1/√2pi*σ) * exp((-1/2)*((x-μ)^2)/(2*σ²))
        """
        mean = self.mean[class_idx]
        var = self.var[class_idx]
        numerator = np.exp((-1/2)*((x-mean)**2) / (2 * var))
        denominator = np.sqrt(2 * np.pi * var)
        prob = numerator / denominator
        return prob
    
    # 計算後驗機率 P(y|X)
    def calc_posterior(self, x):
        posteriors = []

        # 計算每一類的後驗機率 P(y|X)
        for i in range(self.count):
            # 使用 log 比較穩定
            prior = np.log(self.prior[i]) 
            conditional = np.sum(np.log(self.gaussian_density(i, x))) 
            posterior = prior + conditional
            posteriors.append(posterior)
        
        # 傳回最大機率的類別
        return self.classes[np.argmax(posteriors)]
     
    # 訓練
    def fit(self, features, target):
        self.classes = np.unique(target)
        self.count = len(self.classes)
        self.feature_nums = features.shape[1]
        self.rows = features.shape[0]
        
        # 計算每個特徵的平均數、變異數
        data = np.concatenate((target.reshape(-1, 1), features), axis=1)
        self.mean = np.array([np.mean(data[data[:,0]==i, 1:], axis=0) 
                              for i in self.classes])
        self.var = np.array([np.var(data[data[:,0]==i, 1:], axis=0) 
                             for i in self.classes]) 
        # 計算先驗機率 P(y)
        self.prior = np.array([target[target==i].shape[0] 
                               for i in self.classes]) / self.rows
        
    # 預測
    def predict(self, features):
        preds = [self.calc_posterior(f) for f in features]
        return preds

#載入資料集

X, y = datasets.load_iris(return_X_y=True)

#資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

#選擇演算法

clf = NaiveBayesClassifier()

#模型訓練

clf.fit(X_train, y_train)

#模型評估

# 計算準確率
y_pred = clf.predict(X_test)
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

#96.67%


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#06_10_Scikit-learn_naive_bayes

#以單純貝氏分類器進行鳶尾花(Iris)品種的辨識

from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#載入資料集

X, y = datasets.load_iris(return_X_y=True)

#資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

#模型訓練

from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()
clf.fit(X_train, y_train)

#模型評分

# 計算準確率
y_pred = clf.predict(X_test)
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

#93.33%

#使用伯努利單純貝氏分類器

from sklearn.naive_bayes import BernoulliNB

clf = BernoulliNB()
clf.fit(X_train, y_train)

# 計算準確率
y_pred = clf.predict(X_test)
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

#20.00%

#使用多項單純貝氏分類器

from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB()
clf.fit(X_train, y_train)

# 計算準確率
y_pred = clf.predict(X_test)
print(f'{accuracy_score(y_test, y_pred)*100:.2f}%') 

#80.00%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#06_11_naive_bayes_spam

#垃圾信分類

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import WordNetLemmatizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from math import log, sqrt
import pandas as pd
import numpy as np
import re

#讀取資料集

mails = pd.read_csv('./data/spam.csv', encoding = 'latin-1')
cc = mails.head()
print(cc)

#資料整理

mails.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis = 1, inplace = True)
cc = mails.head()
print(cc)

mails.rename(columns = {'v1': 'label', 'v2': 'message'}, inplace = True)
cc = mails.head()
print(cc)

cc = mails['label'].value_counts()
print(cc)

mails['label'] = mails['label'].map({'ham': 0, 'spam': 1})
cc = mails.head()
print(cc)

# 設定停用詞
import string
stopword_list = set(stopwords.words('english') 
                    + list(string.punctuation))
# 詞形還原(Lemmatization)
lem = WordNetLemmatizer()

# 前置處理(Preprocessing)
def preprocess(text, is_lower_case=True):
    if is_lower_case:
        text = text.lower()
    tokens = word_tokenize(text)
    tokens = [token.strip() for token in tokens if len(token) > 1 and token != '...']
    filtered_tokens = [token for token in tokens if token not in stopword_list]
    filtered_tokens = [lem.lemmatize(token) for token in filtered_tokens]
    filtered_text = ' '.join(filtered_tokens)    
    return filtered_text

mails['message'] = mails['message'].map(preprocess)
cc = mails.head()
print(cc)

#文字雲

# 凸顯垃圾信的常用單字
spam_words = ' '.join(list(mails[mails['label'] == 1]['message']))
spam_wc = WordCloud(width = 512,height = 512).generate(spam_words)
plt.figure(figsize = (10, 8), facecolor = 'k')
plt.imshow(spam_wc)
plt.axis('off')
plt.tight_layout(pad = 0)
plt.show()

# 找出正常信件的常用單字
ham_words = ' '.join(list(mails[mails['label'] == 0]['message']))
ham_wc = WordCloud(width = 512,height = 512).generate(ham_words)
plt.figure(figsize = (10, 8), facecolor = 'k')
plt.imshow(ham_wc)
plt.axis('off')
plt.tight_layout(pad = 0)
plt.show()

#使用 SciKit-learn TF-IDF

mails_message, labels = mails['message'].values, mails['label'].values
mails_message = mails_message.astype(str)

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(mails_message)
print(tfidf_matrix.shape)

#(5572, 8114)

cc = tfidf_vectorizer.get_feature_names_out()
print(cc)

no=0
for i in tfidf_matrix.toarray()[0]:
    if i>0.0:
        no+=1
print(no)

#資料分割

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(tfidf_matrix.toarray()
                                                    , labels, test_size=0.2)
#模型訓練

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X_train, y_train)

#模型評分

from sklearn.metrics import accuracy_score
y_pred = clf.predict(X_test)
cc = accuracy_score(y_pred, y_test)
print(cc)
#0.895067264573991

from sklearn.metrics import classification_report, confusion_matrix
print(classification_report(y_test, y_pred))

cc = confusion_matrix(y_test, y_pred)
print(cc)

#測試

message_processed_list = (
    'I cant pick the phone right now. Pls send a message',
    'Congratulations ur awarded $500',
    'Thanks for your subscription to Ringtone UK your mobile will be charged',
    "Oops, I'll let you know when my roommate's done",
    "FreeMsg Hey there darling it's been 3 week's now and no word back! I'd like some fun you up for it still? Tb ok! XxX std chgs to send, 憯1.50 to rcv",
    "Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. Text FA to 87121 to receive entry question(std txt rate)T&C's apply 08452810075over18's",
)
X_new = tfidf_vectorizer.transform(message_processed_list)
cc = clf.predict(X_new.toarray())
print(cc)


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
