import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

#分類問題における評価方法
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
X = data.data
y = 1 - data.target
# ラベルの0と1を反転

X = X[:, :10]
from sklearn.linear_model import LogisticRegression
model_lor = LogisticRegression()
model_lor.fit(X, y)
y_pred = model_lor.predict(X)

print('------------------------------------------------------------')	#60個

print('混同行列')

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y, y_pred)
print(cm)

print('------------------------------------------------------------')	#60個

print('正解率')
from sklearn.metrics import accuracy_score
accuracy_score(y, y_pred)

print('------------------------------------------------------------')	#60個

print('適合率')
from sklearn.metrics import precision_score
precision_score(y, y_pred)

print('------------------------------------------------------------')	#60個

print('再現率')
from sklearn.metrics import recall_score
recall_score(y, y_pred)

print('------------------------------------------------------------')	#60個

print('F値')
from sklearn.metrics import f1_score
f1_score(y, y_pred)

print('------------------------------------------------------------')	#60個

print('予測確率')
model_lor.predict_proba(X)

print('------------------------------------------------------------')	#60個

y_pred2 = (model_lor.predict_proba(X)[:, 1]>0.1).astype(np.int)
print(confusion_matrix(y, y_pred2))

print(accuracy_score(y, y_pred2))
print(recall_score(y, y_pred2))

print('------------------------------------------------------------')	#60個

print('ROC曲線・AUC')
from sklearn.metrics import roc_curve
probas = model_lor.predict_proba(X)
fpr, tpr, thresholds = roc_curve(y, probas[:, 1])

print('------------------------------------------------------------')	#60個

plt.style.use('fivethirtyeight')

fig, ax = plt.subplots()
fig.set_size_inches(4.8, 5)

ax.step(fpr, tpr, 'gray')
ax.fill_between(fpr, tpr, 0, color='skyblue', alpha=0.8)
ax.set_xlabel('False Positive Rate')
ax.set_ylabel('True Positive Rate')
ax.set_facecolor('xkcd:white')
plt.show()

print('------------------------------------------------------------')	#60個

from sklearn.metrics import roc_auc_score
roc_auc_score(y, probas[:, 1])

print('------------------------------------------------------------')	#60個

print('平均二乗誤差')

from sklearn.metrics import mean_squared_error
mean_squared_error(y, y_pred)

print('------------------------------------------------------------')	#60個
print('決定係数')

from sklearn.metrics import r2_score
print(r2_score(y, y_pred))

print('------------------------------------------------------------')	#60個

print('異なるアルゴリズムを利用した場合との比較')

from sklearn.svm import SVR
model_svr_linear = SVR(C=0.01, kernel='linear')
model_svr_linear.fit(X, y)
y_svr_pred = model_svr_linear.predict(X)
print(y_svr_pred)

"""
fig, ax = plt.subplots()
ax.scatter(X, y, color='pink', marker='s', label='data set')
ax.plot(X, y_pred, color='blue', label='regression curve')
ax.plot(X, y_svr_pred, color='red', label='SVR')
ax.legend()
plt.show()
"""

print(mean_squared_error(y, y_svr_pred)) # 平均二乗誤差 
print(r2_score(y, y_svr_pred)) # 決定係数 
print(model_svr_linear.coef_) # 傾き 
print(model_svr_linear.intercept_) # 切片

print('------------------------------------------------------------')	#60個

print('ハイパーパラメータの設定')

model_svr_rbf = SVR(C=1.0, kernel='rbf')
model_svr_rbf.fit(X, y)
y_svr_pred = model_svr_rbf.predict(X) 
print(mean_squared_error(y, y_svr_pred)) # 平均二乗誤差 
print(r2_score(y, y_svr_pred)) # 決定係数

train_X, test_X = X[:400], X[400:]
train_y, test_y = y[:400], y[400:]
model_svr_rbf_1 = SVR(C=1.0, kernel='rbf')
model_svr_rbf_1.fit(train_X, train_y)
test_y_pred = model_svr_rbf_1.predict(test_X) 
print(mean_squared_error(test_y, test_y_pred)) # 平均二乗誤差 
print(r2_score(test_y, test_y_pred)) # 決定係数

print('------------------------------------------------------------')	#60個

print('学習データと検証データに分割')

from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
X = data.data
y = data.target
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

from sklearn.svm import SVC
model_svc = SVC()
model_svc.fit(X_train, y_train)
y_train_pred = model_svc.predict(X_train)
y_test_pred = model_svc.predict(X_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_train, y_train_pred))
print(accuracy_score(y_test, y_test_pred))

from sklearn.ensemble import RandomForestClassifier
model_rfc = RandomForestClassifier()
model_rfc.fit(X_train, y_train)
y_train_pred = model_rfc.predict(X_train)
y_test_pred = model_rfc.predict(X_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_train, y_train_pred))
print(accuracy_score(y_test, y_test_pred))

print('------------------------------------------------------------')	#60個

print('交差検証（クロスバリデーション）')

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
cv = KFold(5, shuffle=True)
model_rfc_1 = RandomForestClassifier()
cross_val_score(model_rfc_1, X, y, cv=cv, scoring='accuracy')

cross_val_score(model_rfc_1, X, y, cv=cv, scoring="f1")

print('------------------------------------------------------------')	#60個

print('ハイパーパラメータの探索')

from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
X = data.data
y = 1 - data.target # ラベルの0と1を反転
X = X[:, :10]

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
cv = KFold(5, shuffle=True)
param_grid = {'max_depth': [5, 10, 15], 'n_estimators': [10, 20, 30]}
model_rfc_2 = RandomForestClassifier()
grid_search = GridSearchCV(model_rfc_2, param_grid, cv=cv, scoring='accuracy')
grid_search.fit(X, y)

print(grid_search.best_score_)
print(grid_search.best_params_)

grid_search = GridSearchCV(model_rfc_2, param_grid, cv=cv, scoring='f1')

print('------------------------------------------------------------')	#60個

print('機械学習モデルへの適用')

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.datasets import fetch_20newsgroups

categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
remove = ('headers', 'footers', 'quotes')
twenty_train = fetch_20newsgroups(subset='train', 
                                  remove=remove, 
                                  categories=categories) # 学習データ
twenty_test = fetch_20newsgroups(subset='test',
                                 remove=remove, 
                                 categories=categories) # 検証データ

count_vect = CountVectorizer() # 単語カウント
X_train_counts = count_vect.fit_transform(twenty_train.data)
X_test_count = count_vect.transform(twenty_test.data)

model = LinearSVC() 
model.fit(X_train_counts, twenty_train.target)
predicted = model.predict(X_test_count)
np.mean(predicted == twenty_test.target)

tf_vec = TfidfVectorizer()  # tf-idf
X_train_tfidf = tf_vec.fit_transform(twenty_train.data)
X_test_tfidf = tf_vec.transform(twenty_test.data)

model = LinearSVC()
model.fit(X_train_tfidf, twenty_train.target)
predicted = model.predict(X_test_tfidf)
np.mean(predicted == twenty_test.target)

print('------------------------------------------------------------')	#60個

#変換後のベクトルデータを入力として機械学習モデルを適用する

from sklearn import datasets
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier

digits = datasets.load_digits()

n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

model = RandomForestClassifier(n_estimators=10)

model.fit(data[:n_samples // 2], digits.target[:n_samples // 2])

expected = digits.target[n_samples // 2:]
predicted = model.predict(data[n_samples // 2:])

print(metrics.classification_report(expected, predicted))

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

