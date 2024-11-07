"""




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
'''
print("------------------------------------------------------------")  # 60個

""" 還沒好
#通過euclidean_distances計算向量之間的距離

#sklearn sklearn向量距離計算

#本文介紹如何利用Python的scikit-learn庫中的euclidean_distances函數，高效地計算多個向量間的歐氏距離。
#在scikit-learn包中，有一個euclidean_distances方法，可以用來計算向量之間的距離。

from sklearn.metrics.pairwise import euclidean_distances
from sklearn.feature_extraction.text import CountVectorizer
 
corpus = ['UNC played Duke in basketball','Duke lost the basketball game','I ate a sandwich']# 文集
vectorizer =CountVectorizer()#
counts = vectorizer.fit_transform(corpus).todense() #得到文集corpus的特征向量，并將其轉為密集矩陣
print(counts)
for x,y in [[0,1],[0,2],[1,2]]:
    dist = euclidean_distances(counts[x],counts[y])
    print('文檔{}與文檔{}的距離{}'.format(x,y,dist))

"""

import matplotlib
import matplotlib as mpl

print('------------------------------------------------------------')	#60個

from sklearn.metrics.pairwise import euclidean_distances

rating_matrix = np.array(
    [[4, 3, 0, 0, 5, 0],
     [5, 0, 4, 0, 4, 0],
     [4, 0, 5, 3, 4, 0],
     [0, 3, 0, 0, 0, 5],
     [0, 4, 0, 0, 0, 4],
     [0, 0, 2, 4, 0, 5]
     ]
)

print('歐幾里得距離 (Euclidean distance)')

dist = euclidean_distances(rating_matrix)
print(dist)

from sklearn.metrics.pairwise import cosine_similarity

sim = cosine_similarity(rating_matrix)
print(sim)

print('------------------------------------------------------------')	#60個

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

text = ["小貝來到北京清華大學",
        "小花來到了網易杭研大廈",
        "小明碩士畢業于中國科學院",
        "小明愛北京小明愛北京天安門"
        ]
               
corpus = ["小貝 來到 北京 清華大學",
          "小花 來到 了 網易 杭研 大廈",
          "小明 碩士 畢業 于 中國 科學院",
          "小明 愛 北京 小明 愛 北京 天安門"
          ]

print('二值化、詞頻')
vectorizer = CountVectorizer(min_df = 1, binary = True) #Transformer
data = vectorizer.fit_transform(corpus)
features = vectorizer.get_feature_names_out()
for word in features:
    print(word)
print(len(features))

print(data.todense())

doc_df = pd.DataFrame(data.toarray(), index = text, columns = vectorizer.get_feature_names_out()).head(10)

print(doc_df)

print('------------------------------')	#30個

from sklearn.metrics.pairwise import cosine_similarity

cos_sims = cosine_similarity(doc_df)
print(cos_sims)

sims_df = pd.DataFrame(cos_sims, index = text, columns = text)
print(sims_df)

print('------------------------------')	#30個

#tf-idf

vectorizer = TfidfVectorizer(min_df = 1)
data = vectorizer.fit_transform(corpus)
features = vectorizer.get_feature_names_out()
for word in features:
    print(word)

print('------------------------------')	#30個

pd.set_option('display.precision', 2)
doc_df = pd.DataFrame(data.toarray(), index = text, columns = vectorizer.get_feature_names_out()).head(10)
print(doc_df)

print('------------------------------------------------------------')	#60個

x = np.array([i * np.pi / 180 for i in range(60, 300, 4)])
y = np.sin(x) + np.random.normal(0, 0.15, len(x))
data = pd.DataFrame(np.column_stack([x, y]), columns = ['x', 'y'])
data.head(10)
plt.scatter(data['x'], data['y'], s = 30)

plt.show()

for i in range(2, 16):
    colname = 'x_%d'%i      
    data[colname] = data['x'] ** i

tt = data.head()
print(tt)

print('------------------------------')	#30個

from sklearn.linear_model import LinearRegression

def linear_regression(data, power, models_to_plot):
    #initialize predictors:
    predictors = ['x']
    if power >= 2:
        predictors.extend(['x_%d'%i for i in range(2, power + 1)])
    
    #Fit the model
    #linreg = LinearRegression(normalize=True)
    linreg = LinearRegression()
    linreg.fit(data[predictors],data['y'])
    y_pred = linreg.predict(data[predictors])
    
    #Return the result in pre-defined format
    rss = sum((y_pred-data['y']) ** 2)
    ret = [rss]
    ret.extend([linreg.intercept_])
    ret.extend(linreg.coef_)
    
    #Check if a plot is to be made for the entered power
    if power in models_to_plot:
        plt.subplot(models_to_plot[power])
        plt.tight_layout()
        plt.plot(data['x'], y_pred, lw = 3)
        plt.plot(data['x'], data['y'], '.')
        plt.title('Plot for power: %d , RSS: %.2f' % (power, rss))
    
    return ret

#Initialize a dataframe to store the results:
col = ['rss','intercept'] + ['coef_x_%d' % i for i in range(1, 16)]
ind = ['model_pow_%d' % i for i in range(1, 16)]
coef_matrix_simple = pd.DataFrame(index = ind, columns = col)

#Define the powers for which a plot is required:
models_to_plot = {1:231,3:232,6:233,9:234,12:235,15:236}

#Iterate through all powers and assimilate results
for i in range(1,16):
    coef_matrix_simple.iloc[i-1,0:i+2] = linear_regression(data, power=i, models_to_plot=models_to_plot)

plt.show()

print('------------------------------')	#30個

#Set the display format to be scientific for ease of analysis
pd.options.display.float_format = '{:,.2g}'.format
tt = coef_matrix_simple
print(tt)

print('------------------------------')	#30個

#L2 Normalization Ridge Regression

from sklearn.linear_model import Ridge

def ridge_regression(data, predictors, alpha, models_to_plot={}):
    #ridgereg = Ridge(alpha=alpha,normalize=True)
    ridgereg = Ridge(alpha=alpha)
    ridgereg.fit(data[predictors],data['y'])
    y_pred = ridgereg.predict(data[predictors])
    
    #Return the result in pre-defined format
    rss = sum((y_pred-data['y'])**2)
    ret = [rss]
    ret.extend([ridgereg.intercept_])
    ret.extend(ridgereg.coef_)


    #Check if a plot is to be made for the entered alpha
    if alpha in models_to_plot:
        plt.subplot(models_to_plot[alpha])
        plt.tight_layout()
        plt.plot(data['x'],y_pred,lw=3)
        plt.plot(data['x'],data['y'],'.')
        plt.title('Plot for alpha: %.3g ,RSS : %.2f'%(alpha,rss))
    return ret


#Initialize predictors to be set of 15 powers of x
predictors=['x']
predictors.extend(['x_%d'%i for i in range(2,16)])

#Set the different values of alpha to be tested
alpha_ridge = [1e-15, 1e-10, 1e-8, 1e-4, 1e-3,1e-2, 1, 5, 10, 20]

#Initialize the dataframe for storing coefficients.
col = ['rss','intercept'] + ['coef_x_%d'%i for i in range(1,16)]
ind = ['alpha_%.2g'%alpha_ridge[i] for i in range(0,10)]
coef_matrix_ridge = pd.DataFrame(index=ind, columns=col)

models_to_plot = {1e-15:231, 1e-10:232, 1e-4:233, 1e-3:234, 1e-2:235, 5:236}
for i in range(10):
    coef_matrix_ridge.iloc[i,] = ridge_regression(data, predictors, alpha_ridge[i], models_to_plot)

plt.show()        

print('------------------------------')	#30個

pd.options.display.float_format = '{:,.2g}'.format
tt = coef_matrix_ridge

print(tt)

print('------------------------------')	#30個

#有多少個系數為0

coef_matrix_ridge.apply(lambda x: sum(x.values==0),axis=1)

print('------------------------------')	#30個

#L1 Regulariztion Lass Regression

from sklearn.linear_model import Lasso

def lasso_regression(data, predictors, alpha, models_to_plot={}):
    #Fit the model
    #lassoreg = Lasso(alpha=alpha,normalize=True, max_iter=1e5)
    lassoreg = Lasso(alpha=alpha, max_iter=1e5)
    lassoreg.fit(data[predictors], data['y'])
    y_pred = lassoreg.predict(data[predictors])
    
    #Return the result in pre-defined format
    rss = sum((y_pred-data['y'])**2)
    ret = [rss]
    ret.extend([lassoreg.intercept_])
    ret.extend(lassoreg.coef_)
    
    #Check if a plot is to be made for the entered alpha
    if alpha in models_to_plot:
        plt.subplot(models_to_plot[alpha])
        plt.tight_layout()
        plt.plot(data['x'],y_pred,lw=3)
        plt.plot(data['x'],data['y'],'.')
        plt.title('Plot for alpha: %.3g'%alpha)
    
    return ret

#Initialize predictors to all 15 powers of x
predictors=['x']
predictors.extend(['x_%d'%i for i in range(2,16)])

#Define the alpha values to test
alpha_lasso = [1e-15, 1e-10, 1e-8, 1e-5,1e-4, 1e-3,1e-2, 1, 5, 10]

#Initialize the dataframe to store coefficients
col = ['rss','intercept'] + ['coef_x_%d'%i for i in range(1,16)]
ind = ['alpha_%.2g'%alpha_lasso[i] for i in range(0,10)]
coef_matrix_lasso = pd.DataFrame(index=ind, columns=col)

#Define the models to plot
models_to_plot = {1e-10:231, 1e-5:232,1e-4:233, 1e-3:234, 1e-2:235, 1:236}

""" NG
#Iterate over the 10 alpha values:
for i in range(10):
    coef_matrix_lasso.iloc[i,] = lasso_regression(data, predictors, alpha_lasso[i], models_to_plot)
"""
plt.show()

print('------------------------------')	#30個

pd.options.display.float_format = '{:,.2g}'.format
tt = coef_matrix_lasso
print(tt)

coef_matrix_lasso.apply(lambda x: sum(x.values==0),axis=1)

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

from sklearn.feature_extraction.text import  CountVectorizer
from sklearn.preprocessing import Normalizer
from sklearn.decomposition import TruncatedSVD

corpus = ["Python is popular in machine learning",
         "Distributed system is important in big data analysis",
        "Machine learning is theoretical foundation of data mining",
        "Learning Python is fun",
        "Playing soccer is fun",
        "Many data scientists like playing soccer",
        "Chinese men's soccer team failed again",
        "Thirty two soccer teams enter World Cup finals"]

vectorizer = CountVectorizer(min_df=1, stop_words="english")
data = vectorizer.fit_transform(corpus)
vectorizer.get_feature_names_out()

tt = pd.DataFrame(data.toarray(), index=corpus, columns=vectorizer.get_feature_names_out()).head(10)
print(tt)

print('------------------------------')	#30個

#Singular value decomposition and LSA
model = TruncatedSVD(2)
data_n = model.fit_transform(data)
data_n = Normalizer(copy=False).fit_transform(data_n)
print(data_n)

tt = pd.DataFrame(data_n, index = corpus, columns = ["component_1", "component_2"])
print(tt)

xs = data_n[:,0]
ys = data_n[:,1]

plt.figure(figsize=(4,4))

ax = plt.gca()
ax.set_xlim([-1, 2])
ax.set_ylim([-1, 2])

plt.scatter(xs, ys)
plt.xlabel('First principal component')
plt.ylabel('Second principal component')
plt.title('Plot of points agains LSA principal components')

plt.show()

print('------------------------------')	#30個

similarity = np.asarray(np.asmatrix(data_n) * np.asmatrix(data_n).T)
tt = pd.DataFrame(similarity, index = corpus, columns = corpus).head(10)
print(tt)

sns.heatmap(similarity, cmap = 'Reds')

plt.show()

print(pd.DataFrame(model.components_,index=['component_1','component_2'],columns=vectorizer.get_feature_names_out()).T)

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

print('房價')

import scipy.stats as stats

train = pd.read_csv(u'data/houseprice.csv')
print(train.head(3))

import scipy.stats as st

plt.figure()
sns.distplot(train['SalePrice'])

plt.show()

print('------------------------------')	#30個

#另一種查看是否服從正態分布的可視化方法

plt.figure()
res = st.probplot(train['SalePrice'], plot=plt)

plt.show()

y = train['SalePrice']

plt.figure(1)
sns.distplot(y,kde=False)

plt.figure(2)
plt.title('Johnson SU')
sns.distplot(y, kde=True, fit=st.johnsonsu)

plt.figure(3)
plt.title('Normal')
sns.distplot(y, kde=False, fit=st.norm)

plt.figure(4)
plt.title('Log Normal')
sns.distplot(y, kde=False, fit=st.lognorm)

plt.show()

print('------------------------------')	#30個

#另一種查看是否服從正態分布的可視化方法

plt.figure()
sns.distplot(train['SalePrice'], fit=st.norm)

plt.figure()
res = st.probplot(train['SalePrice'], plot=plt)

plt.show()

print('------------------------------')	#30個

#把房價做對數變換后再看
SalePrice_log = np.log(train['SalePrice'])
 
#transformed histogram and normal probability plot
sns.distplot(SalePrice_log, fit=st.norm);
#plt.figure()
plt.show()


#另一種查看是否服從正態分布的可視化方法
res = st.probplot(SalePrice_log, plot=plt)
print(res)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


from scipy.stats import norm


def norm_prob(x, mu, sigma):
    p = norm(mu, sigma).cdf(x + 0.0001) - norm(mu, sigma).cdf(x - 0.0001)
    return p


def loglikelihood(data, mu, sigma):
    l = 0.0
    for x in data:
        l -= np.log(norm_prob(x, mu, sigma))
    return l


N = 1000
mu, sigma = 1.6, 0.2

h = 1.8

#rvs: 隨機變量
data = norm.rvs(loc=mu, scale=sigma, size=N)
#print(data)

bins = 50  # 束
plt.hist(data, bins=bins)

plt.title('normal distribution')
plt.show()

print('------------------------------')	#30個

#pdf: 概率密度函數
tt = norm.pdf(x=1.8, loc=1.6, scale=0.2)
print(tt)

tt = norm_prob(h, mu, sigma)
print(tt)

tt = loglikelihood(data, mu, sigma)
print(tt)

print('------------------------------')	#30個

mus = [1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
sigma = 0.1
print(mus)

l = [loglikelihood(data, mu2, sigma) for mu2 in mus]
print(l)

df = pd.DataFrame()
df["mu"] = mus
df["-logl"] = l
print(df)

plt.figure(figsize=(6, 4))

# sns.pointplot(df['mu'],df['-logl'], alpha=0.8) fail
# sns.pointplot(df['mu'],df['-logl']) fail

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

neg_data = "data/neg.csv"
pos_data = "data/pos.csv"

import codecs
import jieba

corpus = []
with codecs.open(neg_data, encoding="utf-8") as f:
    for line in f:
        words = list(jieba.cut(line.replace("|", "")))
        corpus.append(" ".join(words))

neg_df = pd.DataFrame()
neg_df["content"] = corpus
neg_df["label"] = 0

corpus2 = []
with codecs.open(pos_data, encoding="utf-8") as f:
    for line in f:
        words = list(jieba.cut(line.replace("|", "")))
        corpus2.append(" ".join(words))

pos_df = pd.DataFrame()
pos_df["content"] = corpus2
pos_df["label"] = 1

tt = neg_df.head(5)
print(tt)

tt = pos_df.head(5)
print(tt)

corpus_df = pd.concat((neg_df, pos_df))

tt = corpus_df.head(5)
print(tt)

print('------------------------------')	#30個

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()
counts = cv.fit_transform(corpus_df["content"].values)

from sklearn.naive_bayes import MultinomialNB

classifier = MultinomialNB()
targets = corpus_df["label"].values
classifier.fit(counts, targets)

examples = ["這 本 書 真差", "這個 電影 還 可 以"]
example_counts = cv.transform(examples)
predictions = classifier.predict(example_counts)

print(predictions)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Create an empty dataframe
data = pd.DataFrame()

# Create our target variable
data["Gender"] = [
    "male",
    "male",
    "male",
    "male",
    "female",
    "female",
    "female",
    "female",
]

# Create our feature variables
data["Height"] = [6, 5.92, 5.58, 5.92, 5, 5.5, 5.42, 5.75]
data["Weight"] = [180, 190, 170, 165, 100, 150, 130, 150]
data["Size"] = [12, 11, 12, 10, 6, 8, 7, 9]
data["Team"] = ["i100", "i100", "i500", "i100", "i500", "i100", "i500", "i100"]

# View the data
print(data)

print('------------------------------')	#30個

df1 = (
    data.groupby(["Team", "Gender"])
    .size()
    .rename("cnt")
    .reset_index()
    .set_index("Team")
)
df2 = pd.DataFrame(data.groupby(["Team"]).size().rename("total"))

df3 = df1.merge(df2, left_index=True, right_index=True)
df3["p"] = df3["cnt"] * 1.0 / df3["total"]
df3 = df3.reset_index()
print(df3)

print('------------------------------')	#30個

def p_x_given_y_1(team, gender):
    return df3["p"][df3["Team"] == team][df3["Gender"] == gender].values[0]


print(p_x_given_y_1("i100", "female"))
# 0.4

print('------------------------------')	#30個

# 計算先驗
# Number of i100
n_i100 = data["Team"][data["Team"] == "i100"].count()

# Number of i500
n_i500 = data["Team"][data["Team"] == "i500"].count()

# Total rows
total_ppl = data["Team"].count()

# Number of males divided by the total rows
P_i100 = n_i100 * 1.0 / total_ppl

# Number of females divided by the total rows
P_i500 = n_i500 * 1.0 / total_ppl

print(P_i100, P_i500)

print('------------------------------')	#30個
""" NG data_means
# Group the data by gender and calculate the means of each feature
data_means = data.groupby("Team").mean()

# View the values
print(data_means)
"""
print('------------------------------')	#30個
""" NG data_variance
# Group the data by gender and calculate the variance of each feature
data_variance = data.groupby("Team").var()

# View the values
print(data_variance)
"""
print('------------------------------')	#30個
""" data_means / data_variance
# 計算我們需要的均值方差
# Means for i100
i100_height_mean = data_means["Height"][data_means.index == "i100"].values[0]
i100_weight_mean = data_means["Weight"][data_means.index == "i100"].values[0]
i100_size_mean = data_means["Size"][data_means.index == "i100"].values[0]

# Variance for i100
i100_height_variance = data_variance["Height"][data_variance.index == "i100"].values[0]
i100_weight_variance = data_variance["Weight"][data_variance.index == "i100"].values[0]
i100_size_variance = data_variance["Size"][data_variance.index == "i100"].values[0]

# Means for i500
i500_height_mean = data_means["Height"][data_means.index == "i500"].values[0]
i500_weight_mean = data_means["Weight"][data_means.index == "i500"].values[0]
i500_size_mean = data_means["Size"][data_means.index == "i500"].values[0]

# Variance for i500
i500_height_variance = data_variance["Height"][data_variance.index == "i500"].values[0]
i500_weight_variance = data_variance["Weight"][data_variance.index == "i500"].values[0]
i500_size_variance = data_variance["Size"][data_variance.index == "i500"].values[0]
"""

print('------------------------------')	#30個

# 接下來，我們寫個公式來計算高斯分布的概率

person = pd.DataFrame()

# Create some feature values for this single row
person["Height"] = [6]
person["Weight"] = [130]
person["Size"] = [8]
person["Gender"] = ["female"]
# View the data
print(person)

def p_x_given_y_2(x, mean_y, variance_y):
    # Input the arguments into a probability density function
    p = (
        1
        / (np.sqrt(2 * np.pi * variance_y))
        * np.exp((-((x - mean_y) ** 2)) / (2 * variance_y))
    )

    # return p
    return p


tt = person["Gender"][0]
print(tt)

print('------------------------------')	#30個

""" NG
P_i100 * p_x_given_y_1("i100", person["Gender"][0]) * p_x_given_y_2(
    person["Height"][0], i100_height_mean, i100_height_variance
) * p_x_given_y_2(
    person["Weight"][0], i100_weight_mean, i100_weight_variance
) * p_x_given_y_2(
    person["Size"][0], i100_size_mean, i100_size_variance
)
"""

print('------------------------------')	#30個
""" NG
# Numerator of the posterior if the unclassified observation is a female
P_i500 * p_x_given_y_1("i500", person["Gender"][0]) * p_x_given_y_2(
    person["Height"][0], i500_height_mean, i500_height_variance
) * p_x_given_y_2(
    person["Weight"][0], i500_weight_mean, i500_weight_variance
) * p_x_given_y_2(
    person["Size"][0], i500_size_mean, i500_size_variance
)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''


"""
sklearn 使用make_regression生成回归样本数据及NumPy拟合

1. 介绍
sklearn的make_regression函数能生成回归样本数据。

2. 函数语法
make_regression(n_samples=100, n_features=100, n_informative=10, n_targets=1, bias=0.0, 
                effective_rank=None, tail_strength=0.5, noise=0.0, shuffle=True, coef=False, random_state=None)

3. 参数说明：
n_samples：样本数
n_features：特征数(自变量个数)
n_informative：参与建模特征数
n_targets：因变量个数
noise：噪音
bias：偏差(截距)
coef：是否输出coef标识
random_state：随机状态若为固定值则每次产生的数据都一样

"""

from sklearn.datasets import make_regression
X,Y=make_regression(n_samples=10, n_features=1,n_targets=1,noise=1.5,random_state=1)


X.shape,Y.shape

import matplotlib.pyplot as plt
plt.scatter(
    X, #x坐标
    Y, #y坐标
);
plt.show()


#5. 用NumPy实现拟合
#Numpy拟合基于最小二乘法

plt.scatter(
    X, #x坐标
    Y, #y坐标
);

import numpy as np
#用一次多项式拟合，相当于线性拟合
z1 = np.polyfit(X.reshape(10), Y, 1)
p1 = np.poly1d(z1)
print (z1)
print (p1)

y = z1[0] * X + z1[1]
plt.plot(X, y,c='red')

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

sys.exit()

'''
from sklearn.datasets import make_regression
N = 50
X, y = make_regression(n_samples=N, n_features=3)
print(X.shape, y.shape)
print(X)
print(y)

y = y.reshape((-1, 1))
#print(y)

from sklearn.linear_model import LinearRegression

linear_regression = LinearRegression()
linear_regression.fit(X, y)

y_pred_sk = linear_regression.predict(X)
#print(y_pred_sk)

plt.figure(figsize=(9, 4))

plt.plot(y, color="r", linewidth=10)
plt.plot(y_pred_sk, color="g", linewidth=4)

#plt.legend()

plt.show()

print('------------------------------')	#30個


def gd(X, y, theta, l_rate, iterations):
    cost_history = [0] * iterations

    m = X.shape[0]

    for epoch in range(iterations):
        y_hat = X.dot(theta)

        loss = y_hat - y

        gradient = X.T.dot(loss) / m

        theta = theta - l_rate * gradient

        cost = np.dot(loss.T, loss)

        cost_history[epoch] = cost[0, 0]

    return theta, cost_history


def sgd(X, y, theta, l_rate, iterations):
    cost_history = [0] * iterations

    for epoch in range(iterations):
        for i, row in enumerate(X):
            yhat = np.dot(row, theta)

            loss = yhat[0] - y[i]

            theta = theta - l_rate * loss * row.reshape((-1, 1))

            cost_history[epoch] += loss**2

    return theta, cost_history


def predict(X, theta):
    return np.dot(X, theta)


theta = np.random.rand(X.shape[1], 1)

iterations = 100

l_rate = 0.1

theta, cost_history = gd(X, y, theta, l_rate, iterations)

print(theta.T)

# array([[ 1.12259549, 64.22439151, 84.34968956]])

y_predict = predict(X, theta)

y_predict = predict(X, theta)

plt.figure(figsize=(9, 4))

plt.plot(y, color="r")
plt.plot(y, alpha=0.3, linewidth=5)
plt.plot(y_predict, color="g")
plt.plot(y_predict, linewidth=2)

plt.show()

print(linear_regression.coef_)
# array([[48.54597102, 82.31351886,  8.52184984]])

'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
num_pos = 500

subset1 = np.random.multivariate_normal([0, 0], [[1, 0.6], [0.6, 1]], num_pos)
subset2 = np.random.multivariate_normal([0.5, 4], [[1, 0.6], [0.6, 1]], num_pos)

X = np.vstack((subset1, subset2))
y = np.hstack((np.zeros(num_pos), np.ones(num_pos)))

plt.scatter(X[:, 0], X[:, 1], c=y)

plt.show()

print('------------------------------')	#30個

from sklearn import linear_model

clf = linear_model.LogisticRegression()

clf.fit(X, y)

y_pred = clf.predict(X)

print(np.sum(y_pred.reshape(-1, 1) == y.reshape(-1, 1)) * 1.0 / len(y))
# 0.99

from sklearn.metrics import confusion_matrix

print(confusion_matrix(y, y_pred))
# [[495   5]
# [  5 495]]

print('------------------------------')	#30個

# 繪制分類邊界


def plot_decision_boundary(pred_func, X, y, title):
    # Set min and max values and give it some padding
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    h = 0.01
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predict the function value for the whole grid (get class for each grid point)
    Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # print(Z)
    # Plot the contour and training examples
    plt.contourf(xx, yy, Z, alpha=0.3)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=40, alpha=0.8)
    plt.title(title)
    plt.show()


plot_decision_boundary(lambda x: clf.predict(x), X, y, "logistic regression prediction")

print('------------------------------')	#30個


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def log_likelihood(X, y, theta):
    scores = np.dot(X, theta)
    ll = np.sum(y * scores - np.log(1 + np.exp(scores)))
    return ll


def logistic_regression(X, y, l_rate, iterations, add_intercept=True):
    if add_intercept:
        intercept = np.ones((X.shape[0], 1))
        X = np.hstack((intercept, X))

    theta = np.zeros(X.shape[1]).reshape(-1, 1)
    y = y.reshape(-1, 1)
    accu_history = [0] * iterations
    ll_history = [0.0] * iterations
    for epoch in range(iterations):
        x_theta = np.dot(X, theta)
        y_hat = sigmoid(x_theta)
        error = y - y_hat
        gradient = np.dot(X.T, error)
        theta = theta + l_rate * gradient
        preds = np.round(y_hat)

        accu = np.sum(preds == y) * 1.0 / len(y)
        accu_history[epoch] = accu

        if epoch % 100 == 0:
            print("After iter {}; accuracy: {}".format(epoch + 1, accu))
    return theta, accu_history


theta, accu = logistic_regression(X, y, 1, 2000)

print(accu)
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import matplotlib

plt.style.use("bmh")
colors = ["#A60628", "#467821"]
plt.cmap = matplotlib.colors.ListedColormap(colors)

matplotlib.rcParams["figure.figsize"] = (10.0, 6.0)

num_pos = 500

# Bivariate normal distribution mean [0, 0] [0.5, 4], with a covariance matrix

subset1 = np.random.multivariate_normal([0, 0], [[1, 0.6], [0.6, 1]], num_pos)

subset2 = np.random.multivariate_normal([0.5, 4], [[1, 0.6], [0.6, 1]], num_pos)

X = np.vstack((subset1, subset2))

y = np.hstack((np.zeros(num_pos), np.ones(num_pos)))

plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cmap, marker="o", s=40)

plt.show()

from sklearn import linear_model

clf = linear_model.LogisticRegression()
clf.fit(X, y)
print(clf.intercept_, clf.coef_, clf.classes_)
# (array([-5.7268742]), array([[-1.43492343,  3.15471817]]), array([0., 1.]))

y_pred = clf.predict(X)
print(y_pred.shape)
print(np.sum(y_pred.reshape(-1, 1) == y.reshape(-1, 1)) * 1.0 / len(y))

# (1000L,)
# 0.99

from sklearn.metrics import confusion_matrix

print(confusion_matrix(y, y_pred))
sns.heatmap(confusion_matrix(y, y_pred))

plt.show()

"""
[[495   5]

 [  5 495]]
"""

# 繪制分類邊界
plt.style.use("bmh")


def plot_decision_boundary(pred_func, X, y, title):
    # Set min and max values and give it some padding
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    h = 0.01
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predict the function value for the whole grid (get class for each grid point)
    Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # print(Z)
    # Plot the contour and training examples
    plt.contourf(xx, yy, Z, alpha=0.3)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=40, alpha=0.8, cmap=plt.cmap)
    plt.title(title)
    plt.show()


# run on the training dataset with predict function

plot_decision_boundary(lambda x: clf.predict(x), X, y, "logistic regression prediction")

plt.show()

print('------------------------------')	#30個


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def log_likelihood(X, y, theta):
    scores = np.dot(X, theta)
    ll = np.sum(y * scores - np.log(1 + np.exp(scores)))
    return ll


def logistic_regression(X, y, l_rate, iterations, add_intercept=True):
    if add_intercept:
        intercept = np.ones((X.shape[0], 1))
        X = np.hstack((intercept, X))
    theta = np.zeros(X.shape[1]).reshape(-1, 1)
    y = y.reshape(-1, 1)
    accu_history = [0] * iterations
    ll_history = [0.0] * iterations
    for epoch in range(iterations):
        x_theta = np.dot(X, theta)
        y_hat = sigmoid(x_theta)
        error = y - y_hat
        gradient = np.dot(X.T, error)
        theta = theta + l_rate * gradient
        preds = np.round(y_hat)

        accu = np.sum(preds == y) * 1.0 / len(y)
        accu_history[epoch] = accu

        if epoch % 5 == 0:
            print("After iter {}; accuracy: {}".format(epoch + 1, accu))

    return theta, accu_history


theta, accu = logistic_regression(X, y, 1, 500)

print(theta)

"""
array([[-599.88926069],
,       [-181.5414528 ],
,       [ 328.95859873]])
"""
print(accu)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
探索性數據分析（EDA）

EDA指對已有的數據用可視化等手段探索數據的結構和規律的一種數據分析方法，
其目的是最大化對數據的直覺，完成這個事情的方法是結合統計學的圖形以各種形式展現出來。
在深入機器學習或統計建模之前，EDA是一個重要的步驟，
這是因為它提供了為現有問題開發適當模型并正確解釋其結果所需的來龍去脈。
EDA通常涉及以下幾種方法的組合：
.原始數據集中每個字段的單變量可視化和匯總統計
.數據集中每個變量與感興趣目標變量之間的關系的雙變量可視化和匯總統計
.多元可視化以了解數據中不同字段之間的交互作用
.降維以了解數據,通過將數據折疊成幾個小數據點讓觀察值聚類成有區別的小組，
可以更容易地識別行為模式
"""

import scipy.stats as stats
import sklearn.linear_model as linear_model

# import xgboost as xgb
# from sklearn.cross_validation import KFold
# from IPython.display import HTML, display
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# pd.options.display.max_rows = 1000
# pd.options.display.max_columns = 20

print("------------------------------------------------------------")  # 60個

train = pd.read_csv("data/houseprice.csv")
print(train.head(3))

print("------------------------------------------------------------")  # 60個

print("訓練數據集基本信息")

# print(train.info())

print(train.shape)

# 訓練數據集基本信息
# (1460, 81)

# 1.1 首先，區分出數據中的數值型變量和類別型變量
# 數值型變量

quantitative = [f for f in train.columns if train.dtypes[f] != "object"]
quantitative.remove("SalePrice")
quantitative.remove("Id")

# 類別型變量

qualitative = [f for f in train.columns if train.dtypes[f] == "object"]

ccs = [
    "FullBath",
    "HalfBath",
    "TotRmsAbvGrd",
    "Fireplaces",
    "GarageYrBlt",
    "GarageCars",
    "OverallQual",
]
for col in ccs:
    if col in quantitative:
        quantitative.remove(col)
    if not col in qualitative:
        qualitative.append(col)

print("訓練集樣本數量：{}".format(train.shape[0]))
print("數值型變量共有：{}".format(len(quantitative)))
print("類別型變量共有：{}".format(len(qualitative)))

"""
訓練集樣本數量：1460
數值型變量共有：29
類別型變量共有：50
"""
# 1.2查看缺失值的分布情況

missing = train.isnull().sum() / train.shape[0]
print(missing.head(3))

missing = missing[missing > 0]
print("有缺失值的變量共有：{}".format(len(missing)))

missing.sort_values(inplace=True)
print("缺失率超過50%的有{}個".format(len(missing[missing >= 0.5])))

print(missing[missing >= 0.5])

missing.plot.bar(figsize=(6, 4))

plt.show()
"""
Id            0.0
MSSubClass    0.0
MSZoning      0.0
dtype: float64
有缺失值的變量共有：19
缺失率超過50%的有4個
Fence          0.807534
Alley          0.937671
MiscFeature    0.963014
PoolQC         0.995205
dtype: float64
"""

# 可以直接刪除這幾個變量

missing_cols = missing[missing >= 0.5].index.tolist()

for col in missing_cols:
    if col in quantitative:
        quantitative.remove(col)
    if col in qualitative:
        qualitative.remove(col)

print("數值型變量共有：{}".format(len(quantitative)))
print("類別型變量共有：{}".format(len(qualitative)))

# 數值型變量共有：29
# 類別型變量共有：46

# 2 數值型變量
# 2.1 查看目標變量saleprice是否服從正態分布

import scipy.stats as st

y = train["SalePrice"]

plt.figure(1)
sns.distplot(y, kde=False)
plt.show()

plt.figure(2)
plt.title("Johnson SU")
sns.distplot(y, kde=True, fit=st.johnsonsu)
plt.show()

plt.figure(3)
plt.title("Normal")
sns.distplot(y, kde=False, fit=st.norm)
plt.show()

plt.figure(4)
plt.title("Log Normal")
sns.distplot(y, kde=False, fit=st.lognorm)
plt.show()

# 另一種查看是否服從正態分布的可視化方法
sns.distplot(train["SalePrice"], fit=st.norm)
plt.show()

res = st.probplot(train["SalePrice"], plot=plt)
plt.show()

# 把房價做對數變換后再看
SalePrice_log = np.log(train["SalePrice"])
# transformed histogram and normal probability plot
sns.distplot(SalePrice_log, fit=st.norm)
plt.show()


res = st.probplot(SalePrice_log, plot=plt)
print(res)

plt.show()


"""
((array([-3.30513952, -3.04793228, -2.90489705, ...,  2.90489705,
,          3.04793228,  3.30513952]),
,  array([ 10.46024211,  10.47194981,  10.54270639, ...,  13.34550693,
,          13.5211395 ,  13.53447303])),
, (0.39826223081618845, 12.024050901109383, 0.99537614756366088))

顯然，房價本身不服從正態分布，是不能直接用來做回歸建模的。但是經過對數轉換之后，就好了很多。
對于其它的數值型變量，也同樣要做分布的正態性檢驗.
檢驗方法就用：夏皮羅-威爾克(Shapiro-Wilk)法檢驗數據正態性,即W檢驗。
"""

check_normality = lambda x: stats.shapiro(x.fillna(0))[1] < 0.01

normal = pd.DataFrame(train[quantitative])
normal = normal.apply(check_normality)
print(normal.sort_values(ascending=False).head(4))

normal = normal < 0.01
print(not normal.any())

"""
YrSold          True
LowQualFinSF    True
LotFrontage     True
LotArea         True
dtype: bool
True

可以發現所有的數值型變量都沒能通過正態性分布檢驗，都需要做轉換。
我們可以把所有的數值型變量的分布曲線都畫出來，從可視化角度進一步驗證這個判斷
"""

f = pd.melt(train, value_vars=quantitative)
g = sns.FacetGrid(f, col="variable", col_wrap=2, sharex=False, sharey=False)
g = g.map(sns.distplot, "value")
plt.show()

df = pd.DataFrame(
    {"A": {0: "a", 1: "b", 2: "c"}, "B": {0: 1, 1: 3, 2: 5}, "C": {0: 2, 1: 4, 2: 6}}
)
print(df)

pd.melt(df, id_vars=["A"], value_vars=["B", "C"])
print(df)

# 看起來TotalBsmtSF, KitchenAbvGr, LotFrontage, LotArea這幾個變量似乎更適合做些變型，以使其服從正態分布。
# 2.2 異常值分析
# 對saleprice做標準化后再看

"""
# NG
saleprice_scaled = StandardScaler().fit_transform(train["SalePrice"][:, np.newaxis])
low_range = saleprice_scaled[saleprice_scaled[:, 0].argsort()][:10]
high_range = saleprice_scaled[saleprice_scaled[:, 0].argsort()][-10:]
print("outer range (low) of the distribution:")
print(low_range)
print("\nouter range (high) of the distribution:")
print(high_range)
"""


"""
outer range (low) of the distribution:
[[-1.83870376]
 [-1.83352844]
 [-1.80092766]
 [-1.78329881]
 [-1.77448439]
 [-1.62337999]
 [-1.61708398]
 [-1.58560389]
 [-1.58560389]
 [-1.5731    ]]

outer range (high) of the distribution:
[[ 3.82897043]
 [ 4.04098249]
 [ 4.49634819]
 [ 4.71041276]
 [ 4.73032076]
 [ 5.06214602]
 [ 5.42383959]
 [ 5.59185509]
 [ 7.10289909]
 [ 7.22881942]]

"""

# 低房價并沒有太多異常，但是高房價有兩個超過了7，雖然不一定是異常值，但是要小心
# 2.3 查看數值型變量和待預測變量之間的相關性
# 常用pearson相關系數，它是用有前提條件，并且是有局限的——判斷線性相關，非線性相關它是無能為力的。
# Spearman相關系數 vs pearson相關系數的優點：對于數據分布沒有要求。也叫秩和。


def spearman(frame, features):
    spr = pd.DataFrame()
    spr["feature"] = features
    spr["spearman"] = [frame[f].corr(frame["SalePrice"], "spearman") for f in features]
    spr = spr.sort_values("spearman")
    plt.figure(figsize=(6, 0.2 * len(features)))
    sns.barplot(data=spr, y="feature", x="spearman", orient="h")
    return spr


features = quantitative

spr = spearman(train, features)
plt.show()


# 刪除相關系數小于0.3的變量

print("數值型變量共有：{}".format(len(quantitative)))
print("類別型變量共有：{}".format(len(qualitative)))

for col in spr[abs(spr["spearman"]) < 0.3].feature:
    if col in quantitative:
        quantitative.remove(col)

print("數值型變量共有：{}".format(len(quantitative)))
print("類別型變量共有：{}".format(len(qualitative)))

"""
數值型變量共有：29
類別型變量共有：46
數值型變量共有：12
類別型變量共有：46
"""

# 2.4 用散點圖觀察數值型變量之間的關系

# scatterplot

from copy import copy

sns.set(font_scale=2)
cols1 = copy(quantitative)
cols1.append("SalePrice")
# plt.figure('a')
sns.pairplot(train[cols1].fillna(0.0), height=2.5)
plt.show()

# scatterplot

sns.set(font_scale=2)

cols1 = copy(quantitative[:6])

cols1.append("SalePrice")

# plt.figure('b')

sns.pairplot(train[cols1].fillna(0.0), height=2.5)

cols2 = copy(quantitative[6:])

cols2.append("SalePrice")

# plt.figure('c')

sns.pairplot(train[cols2].fillna(0.0), height=2.5)

plt.show()

"""
3.類別型變量

對于類別型的變量，要觀察目標變量（sale_price）在類別的各個取值上的分布情況；用分組箱線圖

對于類別型變量的缺失值，不再用0填充，而是用一個特殊的值'Missing'填充。
"""

for c in qualitative:
    train[c] = train[c].astype("category")
    if train[c].isnull().any():
        train[c] = train[c].cat.add_categories(["MISSING"])
        train[c] = train[c].fillna("MISSING")


def boxplot(x, y, **kwargs):
    sns.boxplot(x=x, y=y)
    x = plt.xticks(rotation=90)


f = pd.melt(train, id_vars=["SalePrice"], value_vars=qualitative)
# g = sns.FacetGrid(f, col="variable",  col_wrap=2, sharex=False, sharey=False, size=5)
g = sns.FacetGrid(f, col="variable", col_wrap=2, sharex=False, sharey=False)
g = g.map(boxplot, "value", "SalePrice")

plt.show()

"""
看起來像LotConfig、LandSlope這樣的變量，對于房價的影響似乎不大。 Neighborhood對房價有影響。 然后每個類別的不同子類之間看起來似乎也有差別。 overallQual的值太多。

具體到一個分類指標和數值型變量之間的相關關系，我們可以用方差分析進行檢查。
3.2 方差分析
"""


def anova(frame):
    anv = pd.DataFrame()
    anv["feature"] = qualitative
    pvals = []
    for c in qualitative:
        samples = []
        for cls in frame[c].unique():
            s = frame[frame[c] == cls]["SalePrice"].values
            samples.append(s)
        pval = stats.f_oneway(*samples)[1]
        pvals.append(pval)
    anv["pval"] = pvals
    return anv.sort_values("pval")


a = anova(train)
a["disparity"] = np.log(1.0 / a["pval"].values)
sns.barplot(data=a, x="feature", y="disparity")
x = plt.xticks(rotation=90)
plt.show()


"""
這里我們用了方差分析，來看每一個類別變量和預測變量Sale_price之間是否有相關關系。

因為我們最后得到了個p值，p>0.05說明樣本的分組之間沒有顯著性差異，

p值越小說明差異越顯著。

因為我們想用一個類似于“變異度”的指標——“差異度”，我們希望這個指標越大，說明差異越明顯。也就是想要一個同向變化的指標，所以對p值取了個倒數。僅此而已。
3.3 對于這些分類變量的每個值做正確編碼

另一種編碼方式是OneHotEncoding或者dummy
"""


def encode(frame, feature):
    ordering = pd.DataFrame()
    ordering["val"] = frame[feature].unique()
    ordering.index = ordering.val
    ordering["spmean"] = (
        frame[[feature, "SalePrice"]].groupby(feature).mean()["SalePrice"]
    )
    ordering = ordering.sort_values("spmean")
    ordering["ordering"] = range(1, ordering.shape[0] + 1)
    ordering = ordering["ordering"].to_dict()

    for cat, o in ordering.items():
        frame.loc[frame[feature] == cat, feature + "_E"] = o


qual_encoded = []
for q in qualitative:
    encode(train, q)
    qual_encoded.append(q + "_E")

print(qual_encoded)

"""
['MSZoning_E', 'Street_E', 'LotShape_E', 'LandContour_E', 'Utilities_E', 'LotConfig_E', 'LandSlope_E', 'Neighborhood_E', 'Condition1_E', 'Condition2_E', 'BldgType_E', 'HouseStyle_E', 'RoofStyle_E', 'RoofMatl_E', 'Exterior1st_E', 'Exterior2nd_E', 'MasVnrType_E', 'ExterQual_E', 'ExterCond_E', 'Foundation_E', 'BsmtQual_E', 'BsmtCond_E', 'BsmtExposure_E', 'BsmtFinType1_E', 'BsmtFinType2_E', 'Heating_E', 'HeatingQC_E', 'CentralAir_E', 'Electrical_E', 'KitchenQual_E', 'Functional_E', 'FireplaceQu_E', 'GarageType_E', 'GarageFinish_E', 'GarageQual_E', 'GarageCond_E', 'PavedDrive_E', 'SaleType_E', 'SaleCondition_E', 'FullBath_E', 'HalfBath_E', 'TotRmsAbvGrd_E', 'Fireplaces_E', 'GarageYrBlt_E', 'GarageCars_E', 'OverallQual_E']
"""
print(train.head(3))

"""
, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
	Id	MSSubClass	MSZoning	LotFrontage	LotArea	Street	Alley	LotShape	LandContour	Utilities	...	PavedDrive_E	SaleType_E	SaleCondition_E	FullBath_E	HalfBath_E	TotRmsAbvGrd_E	Fireplaces_E	GarageYrBlt_E	GarageCars_E	OverallQual_E
0	1	60	RL	65.0	8450	Pave	NaN	Reg	Lvl	AllPub	...	3.0	5.0	5.0	3.0	3.0	8.0	1.0	86.0	3.0	7.0
1	2	20	RL	80.0	9600	Pave	NaN	Reg	Lvl	AllPub	...	3.0	5.0	5.0	3.0	2.0	5.0	2.0	57.0	3.0	6.0
2	3	60	RL	68.0	11250	Pave	NaN	IR1	Lvl	AllPub	...	3.0	5.0	5.0	3.0	3.0	5.0	2.0	91.0	3.0	7.0
,

3 rows × 127 columns
,

"""

print(train["GarageQual_E"].value_counts())

"""
4.0    1311
,2.0      81
,3.0      48
,5.0      14
,6.0       3
,1.0       3
,Name: GarageQual_E, dtype: int64

3.4.查看衍生變量和房價的Spearman相關性

對于相關性的檢測我們使用的是Spearman correlation，這種檢驗方法的好處是即使是非線性相關也能檢測出來。
"""

sns.set(font_scale=1.2)


def spearman(frame, features):
    spr = pd.DataFrame()
    spr["feature"] = features
    spr["spearman"] = [frame[f].corr(frame["SalePrice"], "spearman") for f in features]
    spr = spr.sort_values("spearman")
    plt.figure(figsize=(6, 0.2 * len(features)))
    sns.barplot(data=spr, y="feature", x="spearman", orient="h")


features = qual_encoded
spearman(train, features)
plt.show()

"""
顯然，OverallQual和房價的關系最明顯。房子的鄰居和位置看起來也是有影響的。
3.5 觀察變量之間的相關性

回歸模型對于變量共線的容忍度差，所以，我們需要考慮變量之間的相關性。用相關系數矩陣的熱力圖即可。
"""

sns.set(font_scale=1)

plt.figure(1)

corr = train[quantitative + ["SalePrice"]].corr("spearman")

sns.heatmap(corr, cbar=True, annot=True, square=True, fmt=".2f", annot_kws={"size": 10})

plt.show()

# from functools import partial
# # my_heatmap=partial(sns.heatmap,cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)

plt.figure(2)
corr = train[qual_encoded + ["SalePrice"]].corr()
sns.heatmap(corr, cbar=True, annot=True, square=True, fmt=".2f", annot_kws={"size": 10})

plt.show()

plt.figure(3)
corr = pd.DataFrame(
    np.zeros([len(quantitative) + 1, len(qual_encoded) + 1]),
    index=quantitative + ["SalePrice"],
    columns=qual_encoded + ["SalePrice"],
)
for q1 in quantitative + ["SalePrice"]:
    for q2 in qual_encoded + ["SalePrice"]:
        corr.loc[q1, q2] = train[q1].corr(train[q2])

sns.heatmap(corr, cbar=True, annot=True, square=True, fmt=".2f", annot_kws={"size": 10})

plt.show()

"""
3.6 觀察所有變量（包括衍生變量）和目標變量之間的關系

現在所有類別型變量也做了重新編碼，編碼成數值型。所有所有的特征都可以看作是數值型的了。于是，我們可以再次全景式觀察變量和目標變量之間的關系。
"""


def pairplot(x, y, **kwargs):
    ax = plt.gca()
    ts = pd.DataFrame({"time": x, "val": y})
    ts = ts.groupby("time").mean()
    ts.plot(ax=ax)
    plt.xticks(rotation=90)


# 畫散點圖
sns.set(style="ticks", color_codes=True)

f = pd.melt(train, id_vars=["SalePrice"], value_vars=quantitative + qual_encoded)
# g = sns.FacetGrid(f, col="variable",  col_wrap=2, sharex=False, sharey=False, size=5)
g = sns.FacetGrid(f, col="variable", col_wrap=2, sharex=False, sharey=False)
g = g.map(pairplot, "value", "SalePrice")

plt.show()

"""
看起來，YearBuild、1stFlrSF, 2ndFlrSF, Neighborhood_E There are lots of nonlinearities this may be the cause why some variables wont be selected by Lasso/Lars. Some factors like YearBuilt, 1stFlrSF, 2ndFlrSF, Neighborhood_E look like they would benefit from adding quadratic term to regression. But on the other hand this will most probably provoke overfit.

觀察的結果提示我們，有些變量可以嘗試做些變換，比如平方變換。
4.高級內容

考慮數據本身是否分群，如果分群，就可以用分段回歸。

接下來，考慮是否可以分段進行回歸。

我們把房價200000作為分界點，之下的作為普通住宅，之上的作為豪宅，然后看看在這樣分開后，那些數值型變量的均值有多大差異。
"""

features = quantitative
standard = train[train["SalePrice"] < 200000]
pricey = train[train["SalePrice"] >= 200000]

diff = pd.DataFrame()
diff["feature"] = features
diff["difference"] = [
    (pricey[f].fillna(0.0).mean() - standard[f].fillna(0.0).mean())
    / (standard[f].fillna(0.0).mean())
    for f in features
]

sns.barplot(data=diff, x="feature", y="difference")
x = plt.xticks(rotation=90)

print(diff)

plt.show()

"""
, , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,
	feature	difference
0	MSSubClass	-0.150366
1	LotFrontage	0.238321
2	LotArea	0.536645
3	OverallQual	0.361440
4	OverallCond	-0.047635
5	YearBuilt	0.015026
6	YearRemodAdd	0.010197
7	MasVnrArea	2.029480
8	BsmtFinSF1	0.729316
9	BsmtFinSF2	-0.023328
10	BsmtUnfSF	0.410808
11	TotalBsmtSF	0.515235
12	1stFlrSF	0.396664
13	2ndFlrSF	0.978444
14	LowQualFinSF	-0.298300
15	GrLivArea	0.512153
16	BsmtFullBath	0.577215
17	BsmtHalfBath	-0.487756
18	FullBath	0.424714
19	HalfBath	0.684120
20	BedroomAbvGr	0.092859
21	KitchenAbvGr	-0.050115
22	TotRmsAbvGrd	0.257338
23	Fireplaces	1.102258
24	GarageYrBlt	0.090733
25	GarageCars	0.550690
26	GarageArea	0.596397
27	WoodDeckSF	0.950341
28	OpenPorchSF	1.314906
29	EnclosedPorch	-0.479096
30	3SsnPorch	0.881312
31	ScreenPorch	0.623489
32	PoolArea	2.213669
33	MiscVal	-0.559517
34	MoSold	0.052589
35	YrSold	-0.000021
,

我們用tnse方法，把每個高維樣本映射到二維平面上的點。

然后我們對樣本做標準化處理，處理之后做PCA，提取前30個主成分。也就是把樣本的特征降維到30個特征。

對這30個特征的樣本聚類，聚成5類。

在把這5類用可視化的方法會出來，看看是否有聚集趨勢。
"""

features = quantitative + qual_encoded
model = TSNE(n_components=2, random_state=0, perplexity=50)
X = train[features].fillna(0.0).values
tsne = model.fit_transform(X)

std = StandardScaler()
s = std.fit_transform(X)
pca = PCA(n_components=40)
pca.fit(s)
pc = pca.transform(s)
kmeans = KMeans(n_clusters=5)
kmeans.fit(pc)

fr = pd.DataFrame({"tsne1": tsne[:, 0], "tsne2": tsne[:, 1], "cluster": kmeans.labels_})
sns.lmplot(data=fr, x="tsne1", y="tsne2", hue="cluster", fit_reg=False)

plt.show()

print(np.sum(pca.explained_variance_ratio_))

"""
0.846903058622

看起來聚集趨勢并不明顯，所以分段回歸的意義似乎不大。

另外40個主成分能解釋84%的方差。
"""

y = train["SalePrice"].values


def johnson(y):
    gamma, eta, epsilon, lbda = stats.johnsonsu.fit(y)
    yt = gamma + eta * np.arcsinh((y - epsilon) / lbda)
    return yt, gamma, eta, epsilon, lbda


def johnson_inverse(y, gamma, eta, epsilon, lbda):
    return lbda * np.sinh((y - gamma) / eta) + epsilon


yt, g, et, ep, l = johnson(y)
yt2 = johnson_inverse(yt, g, et, ep, l)

plt.figure(1)
sns.distplot(yt)

plt.figure(2)
sns.distplot(yt2)

plt.show()

# 5.最后建模


def error(actual, predicted):
    actual = np.log(actual)
    predicted = np.log(predicted)
    return np.sqrt(np.sum(np.square(actual - predicted)) / len(actual))


def log_transform(feature):
    train[feature] = np.log1p(train[feature].values)


def quadratic(feature):
    train[feature + "2"] = train[feature] ** 2


# 下面這些特征做log轉化
log_transform("GrLivArea")
log_transform("1stFlrSF")
log_transform("2ndFlrSF")
log_transform("TotalBsmtSF")
log_transform("LotArea")
log_transform("LotFrontage")
log_transform("KitchenAbvGr")
log_transform("GarageArea")

# 下面這些特征取平方轉換
# quadratic('OverallQual') fail
quadratic("YearBuilt")
quadratic("YearRemodAdd")
quadratic("TotalBsmtSF")
quadratic("2ndFlrSF")
quadratic("Neighborhood_E")
quadratic("RoofMatl_E")
quadratic("GrLivArea")

qdr = [
    "OverallQual2",
    "YearBuilt2",
    "YearRemodAdd2",
    "TotalBsmtSF2",
    "2ndFlrSF2",
    "Neighborhood_E2",
    "RoofMatl_E2",
    "GrLivArea2",
]

# 下面這些特征做二值化
train["HasBasement"] = train["TotalBsmtSF"].apply(lambda x: 1 if x > 0 else 0)
train["HasGarage"] = train["GarageArea"].apply(lambda x: 1 if x > 0 else 0)
train["Has2ndFloor"] = train["2ndFlrSF"].apply(lambda x: 1 if x > 0 else 0)
train["HasMasVnr"] = train["MasVnrArea"].apply(lambda x: 1 if x > 0 else 0)
train["HasWoodDeck"] = train["WoodDeckSF"].apply(lambda x: 1 if x > 0 else 0)
train["HasPorch"] = train["OpenPorchSF"].apply(lambda x: 1 if x > 0 else 0)
train["HasPool"] = train["PoolArea"].apply(lambda x: 1 if x > 0 else 0)
train["IsNew"] = train["YearBuilt"].apply(lambda x: 1 if x > 2000 else 0)

boolean = [
    "HasBasement",
    "HasGarage",
    "Has2ndFloor",
    "HasMasVnr",
    "HasWoodDeck",
    "HasPorch",
    "HasPool",
    "IsNew",
]

features = quantitative + qual_encoded + boolean + qdr
lasso = linear_model.LassoLarsCV(max_iter=10000)

""" NG
# sklearn中要求X，y都是矩陣形式，而不是數據框
X = train[features].fillna(0.).values
Y = train['SalePrice'].values

lasso.fit(X, np.log(Y))

#反log1p變換
Ypred = np.exp(lasso.predict(X))
print(error(Y, Ypred))

"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print('------------------------------------------------------------')	#60個

from sklearn.linear_model import LinearRegression

X = [[10.0], [8.0], [13.0], [9.0], [11.0], [14.0], [6.0], [4.0], [12.0], [7.0], [5.0]]
y = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]

linear_regression = LinearRegression()
linear_regression.fit(X, y) 
print(linear_regression.intercept_) # 切片 
print(linear_regression.coef_) # 傾き

y_pred = linear_regression.predict([[0], [1]]) 
print(y_pred) # x=0, x=1に対する予測結果

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

train_size = 20
test_size = 12
train_X = np.random.uniform(low=0, high=1.2, size=train_size)
test_X = np.random.uniform(low=0.1, high=1.3, size=test_size)
train_y = np.sin(train_X * 2 * np.pi) + np.random.normal(0, 0.2, train_size)
test_y = np.sin(test_X * 2 * np.pi) + np.random.normal(0, 0.2, test_size)
poly = PolynomialFeatures(6) # 次數は6
train_poly_X = poly.fit_transform(train_X.reshape(train_size, 1))
test_poly_X = poly.fit_transform(test_X.reshape(test_size, 1))

model = Ridge(alpha=1.0)
model.fit(train_poly_X, train_y)
train_pred_y = model.predict(train_poly_X)
test_pred_y = model.predict(test_poly_X)
print(mean_squared_error(train_pred_y, train_y))
print(mean_squared_error(test_pred_y, test_y))

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

from sklearn.linear_model import LogisticRegression

X_train = np.r_[np.random.normal(3, 1, size=50), np.random.normal(-1, 1, size=50)].reshape((100, -1))
y_train = np.r_[np.ones(50), np.zeros(50)]

logistic_regression = LogisticRegression()
logistic_regression.fit(X_train, y_train)
print(logistic_regression.predict_proba([[0], [1], [2]])[:, 1])

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

from sklearn.svm import LinearSVC
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# データ生成
centers = [(-1, -0.125), (0.5, 0.5)]
X, y = make_blobs(n_samples=50, n_features=2, centers=centers, cluster_std=0.3)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
model = LinearSVC() 
model.fit(X_train, y_train) # 學習
y_pred = model.predict(X_test) 
print(accuracy_score(y_pred, y_test)) # 評価

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

from sklearn.svm import SVC
from sklearn.datasets import make_gaussian_quantiles
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# データ生成
X, y = make_gaussian_quantiles(n_features=2, n_classes=2, n_samples=300)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
model = SVC()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(accuracy_score(y_pred, y_test))

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

from sklearn.naive_bayes import MultinomialNB

# データ生成
X_train = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1]]
y_train = [1, 1, 1, 0, 0, 0]
model = MultinomialNB()
model.fit(X_train, y_train) # 學習
print(model.predict([[0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]])) # 評価

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個








print('------------------------------------------------------------')	#60個
print("------------------------------------------------------------")  # 60個

from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# データ生成
X, y = make_moons(noise=0.3)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
model = KNeighborsClassifier()
model.fit(X_train, y_train)  # 學習
y_pred = model.predict(X_test)
print(accuracy_score(y_pred, y_test))  # 評価

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.decomposition import TruncatedSVD

data = [
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
]
n_components = 2  # 潜在変数の数
model = TruncatedSVD(n_components=n_components)
model.fit(data)
print(model.transform(data))  # 変換したデータ
print(model.explained_variance_ratio_)  # 寄与率
print(sum(model.explained_variance_ratio_))  # 累積寄与率

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.decomposition import NMF

# from sklearn.datasets.samples_generator import make_blobs old
from sklearn.datasets import make_blobs

centers = [[5, 10, 5], [10, 4, 10], [6, 8, 8]]
X, _ = make_blobs(centers=centers)  # centersを中心としたデータを生成
n_components = 2  # 潜在変数の数
model = NMF(n_components=n_components)
model.fit(X)
W = model.transform(X)  # 分解後の行列
H = model.components_
print(W)
print(H)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# removeで本文以外の情報を取り除く
data = fetch_20newsgroups(remove=("headers", "footers", "quotes"))
max_features = 1000
# 文書 データをベクトルに変換
tf_vectorizer = CountVectorizer(max_features=max_features, stop_words="english")
tf = tf_vectorizer.fit_transform(data.data)
n_topics = 20
model = LatentDirichletAllocation(n_components=n_topics)
model.fit(tf)
print(model.components_)  # 各トピックが持つ単語分布
print(model.transform(tf))  # トピックで表現された文書

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" import fail
from sklearn.datasets import samples_generator
from sklearn.manifold import LocallyLinearEmbedding

data, color = samples_generator.make_swiss_roll(n_samples=1500)
n_neighbors = 12 # 近傍点の数 
n_components = 2 # 削減後の次元数
model = LocallyLinearEmbedding(n_neighbors=n_neighbors,
n_components=n_components)
model.fit(data)
print(model.transform(data)) # 変換したデータ
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.manifold import TSNE
from sklearn.datasets import load_digits

data = load_digits()
print(type(data))
print(len(data))

print("TSNE")
n_components = 2  # 削減後の次元を2に設定
model = TSNE(n_components=n_components)
print(model.fit_transform(data.data))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------")  # 30個

print("混同行列")

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y, y_pred)
print(cm)

print("------------------------------")  # 30個

print("正解率")
from sklearn.metrics import accuracy_score

accuracy_score(y, y_pred)

print("------------------------------")  # 30個

print("適合率")
from sklearn.metrics import precision_score

precision_score(y, y_pred)

print("------------------------------")  # 30個

print("再現率")
from sklearn.metrics import recall_score

recall_score(y, y_pred)

print("------------------------------")  # 30個

print("F値")
from sklearn.metrics import f1_score

f1_score(y, y_pred)

print("------------------------------")  # 30個

print("予測確率")
logistic_regression.predict_proba(X)

print("------------------------------")  # 30個

y_pred2 = (logistic_regression.predict_proba(X)[:, 1] > 0.1).astype(np.int)
print(confusion_matrix(y, y_pred2))

print(accuracy_score(y, y_pred2))
print(recall_score(y, y_pred2))

print("------------------------------")  # 30個

print("ROC曲線・AUC")
from sklearn.metrics import roc_curve

probas = logistic_regression.predict_proba(X)
fpr, tpr, thresholds = roc_curve(y, probas[:, 1])

print("------------------------------")  # 30個

plt.style.use("fivethirtyeight")

fig, ax = plt.subplots()
fig.set_size_inches(4.8, 5)

ax.step(fpr, tpr, "gray")
ax.fill_between(fpr, tpr, 0, color="skyblue", alpha=0.8)
ax.set_xlabel("False Positive Rate")
ax.set_ylabel("True Positive Rate")
ax.set_facecolor("xkcd:white")
plt.show()

print("------------------------------")  # 30個

from sklearn.metrics import roc_auc_score

roc_auc_score(y, probas[:, 1])

print("------------------------------")  # 30個

print("平均二乗誤差")

from sklearn.metrics import mean_squared_error

mean_squared_error(y, y_pred)

print("------------------------------")  # 30個

print("決定係数")

from sklearn.metrics import r2_score

print(r2_score(y, y_pred))

print("------------------------------")  # 30個

print("異なるアルゴリズムを利用した場合との比較")

from sklearn.svm import SVR

model_svr_linear = SVR(C=0.01, kernel="linear")
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

print(mean_squared_error(y, y_svr_pred))  # 平均二乗誤差
print(r2_score(y, y_svr_pred))  # 決定係数
print(model_svr_linear.coef_)  # 傾き
print(model_svr_linear.intercept_)  # 切片

print("------------------------------")  # 30個

print("ハイパーパラメータの設定")

model_svr_rbf = SVR(C=1.0, kernel="rbf")
model_svr_rbf.fit(X, y)
y_svr_pred = model_svr_rbf.predict(X)
print(mean_squared_error(y, y_svr_pred))  # 平均二乗誤差
print(r2_score(y, y_svr_pred))  # 決定係数

train_X, test_X = X[:400], X[400:]
train_y, test_y = y[:400], y[400:]
model_svr_rbf_1 = SVR(C=1.0, kernel="rbf")
model_svr_rbf_1.fit(train_X, train_y)
test_y_pred = model_svr_rbf_1.predict(test_X)
print(mean_squared_error(test_y, test_y_pred))  # 平均二乗誤差
print(r2_score(test_y, test_y_pred))  # 決定係数

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("機械学習モデルへの適用")

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.datasets import fetch_20newsgroups

categories = ["alt.atheism", "soc.religion.christian", "comp.graphics", "sci.med"]
remove = ("headers", "footers", "quotes")
twenty_train = fetch_20newsgroups(
    subset="train", remove=remove, categories=categories
)  # 学習データ
twenty_test = fetch_20newsgroups(
    subset="test", remove=remove, categories=categories
)  # 検証データ

count_vect = CountVectorizer()  # 単語カウント
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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 変換後のベクトルデータを入力として機械学習モデルを適用する

from sklearn import datasets
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier

digits = datasets.load_digits()

n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

model = RandomForestClassifier(n_estimators=10)

model.fit(data[: n_samples // 2], digits.target[: n_samples // 2])

expected = digits.target[n_samples // 2 :]
predicted = model.predict(data[n_samples // 2 :])

print(metrics.classification_report(expected, predicted))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("產生測試資料 並畫出")

from sklearn.datasets import make_blobs

N = 500
print("產生", N, "筆資料 2維 2群")
dx, dy = make_blobs(n_samples=N, n_features=2, centers=2, random_state=0)

print(dx.shape)
print(dy.shape)
# print(dx)
# print(dy)

plt.scatter(dx.T[0], dx.T[1], c=dy, cmap="Dark2")
plt.title("dx的分佈狀況, dy是用顏色表示")
plt.grid(True)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# StandardScaler
# 將資料常態分布化，平均值會變為0, 標準差變為1，使離群值影響降低
# MinMaxScaler與StandardScaler類似

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

N = 500
print("產生", N, "筆資料 2維 2群")
dx, dy = make_blobs(n_samples=N, n_features=2, centers=2, random_state=0)

dx_std = StandardScaler().fit_transform(dx)

plt.scatter(dx_std.T[0], dx_std.T[1], c=dy, cmap="Dark2")
plt.grid(True)

plt.show()

# 分割訓練資料集和測試資料集
from sklearn.model_selection import train_test_split

dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

print(dx.shape)
print(dx_train.shape)
print(dx_test.shape)

print(dy.shape)
print(dy_train.shape)
print(dy_test.shape)

# k 最近鄰演算法 (KNN)
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(dx_train, dy_train)
predictions = knn.predict(dx_test)

print(dy_test)
print(predictions)
print(knn.score(dx_train, dy_train))
print(knn.score(dx_test, dy_test))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 邏輯斯迴歸 (logistic regression)

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

print("產生500筆資料 2維 2群")
dx, dy = make_blobs(n_samples=500, n_features=2, centers=2, random_state=0)

dx_std = StandardScaler().fit_transform(dx)

dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

logistic_regression = LogisticRegression()
logistic_regression.fit(dx_train, dy_train)
predictions = logistic_regression.predict(dx_test)

print(logistic_regression.score(dx_train, dy_train))
print(logistic_regression.score(dx_test, dy_test))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 線性支援向量機 (Linear SVM)

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

print("產生500筆資料 2維 2群")
dx, dy = make_blobs(n_samples=500, n_features=2, centers=2, random_state=0)
dx_std = StandardScaler().fit_transform(dx)
dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

linear_svm = LinearSVC()
linear_svm.fit(dx_train, dy_train)
predictions = linear_svm.predict(dx_test)

print(linear_svm.score(dx_train, dy_train))
print(linear_svm.score(dx_test, dy_test))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 非線性 SVM

from sklearn.datasets import make_moons
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC, SVC

dx, dy = make_moons(n_samples=500, noise=0.15, random_state=0)

dx_train, dx_test, dy_train, dy_test = train_test_split(
    StandardScaler().fit_transform(dx), dy, test_size=0.2, random_state=0
)

linear_svm = LinearSVC()

linear_svm.fit(dx_train, dy_train)

predictions = linear_svm.predict(dx_test)

svm = SVC()

svm.fit(dx_train, dy_train)

predictions = svm.predict(dx_test)

print(linear_svm.score(dx_train, dy_train))

print(linear_svm.score(dx_test, dy_test))

print(svm.score(dx_train, dy_train))

print(svm.score(dx_test, dy_test))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 6-1 探索性資料分析──以Titanic(鐵達尼號)之生還預測為例
# 資料科學 0. 問個感興趣的問題

# 資料科學 1. 資料取得
# 資料科學1.1 自建資料或下載資料後上傳到雲端硬碟

# train.csv行資料說明.jpg
# 資料科學1.2 讀取Google雲端硬碟中的csv檔
# 資料科學1.3 將行列結構的資料建立為Pandas的資料框

filename = "data/titanic.csv"
df = pd.read_csv(filename)
"""
print(df)
print(df.info())
print(df.describe())
"""

# 資料科學2.3 資料清理
# 缺失值的補值或刪除

print(df.isnull())

print(df.isnull().sum())

print(df.isnull().count())

print(df.isnull().sum() / df.isnull().count() * 100)

df[df["Age"].isnull() == True]

df["Age"] = df["Age"].fillna(df["Age"].mean())

print(df)

df[df["Embarked"].isnull()]

df["Embarked"].value_counts()

df["Embarked"] = df["Embarked"].fillna("S")

df.loc[[61, 829], :]  # 顯示列索引61,829的資料

print(df.info())

df = df.drop("Cabin", axis=1)

print(df.info())

# 刪除重複值或異常值
df[df.duplicated()]

# 資料轉換
print(df.head())

s = {"female": 0, "male": 1}
df["Sex"] = df["Sex"].map(s)
e = {"S": 0, "C": 1, "Q": 2}
df["Embarked"] = df["Embarked"].map(e)
print(df.head())

# 資料科學3. 探索性資料分析
# 資料科學3.1 觀察資料的分佈(統計)

print(df.head())

# 資料科學3.2 資料視覺化
# 1.全體乘客生還、死亡的比例

print(df["Survived"].value_counts())

df["Survived"].value_counts().plot(kind="pie", autopct="%1.2f%%")
plt.show()

print("------------------------------")  # 30個

# 2.男性、女性乘客的比例

print(df["Sex"].value_counts())

df["Sex"].value_counts().plot(kind="pie", autopct="%1.2f%%")
plt.show()

print("------------------------------")  # 30個

# 3.搭1等艙、2等艙、3等艙的乘客比例

print(df["Pclass"].value_counts())

df["Pclass"].value_counts().plot(kind="pie", autopct="%1.2f%%")
plt.show()

print("------------------------------")  # 30個

# 4.進一步探討性別與生還的關係

# 女、男乘客的人數

print(df.groupby(["Sex"])["PassengerId"].count())

# 不同性別的生還和死亡人數

print(df.groupby(["Sex", "Survived"])["PassengerId"].count())

df.groupby(["Sex", "Survived"])["PassengerId"].count().plot(kind="bar", rot=1)
plt.show()

print("------------------------------")  # 30個

# 不同性別生還人數/不同性別人數

ss = (
    df.groupby(["Sex", "Survived"])["PassengerId"].count()
    / df.groupby(["Sex"])["PassengerId"].count()
    * 100
)
print(ss)

ss.plot(kind="bar", color=["r", "g"], rot=0)
plt.show()

print("------------------------------")  # 30個

# 5.進一步探討艙等與生還的關係

# 三種艙等的生還和死亡人數

print(df.groupby(["Pclass", "Survived"])["PassengerId"].count())

df.groupby(["Pclass", "Survived"])["PassengerId"].count().plot(kind="bar", rot=0)
plt.show()

print("------------------------------")  # 30個

# 不同艙等生還人數/不同艙等人數

ps = (
    df.groupby(["Pclass", "Survived"])["PassengerId"].count()
    / df.groupby(["Pclass"])["PassengerId"].count()
    * 100
)
print(ps)

ps.plot(kind="bar", rot=0)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 6-2 探索性資料分析──以 Iris 的花種分類為例
# 資料科學0. 感興趣的問題

# 資料科學1. 資料取得
# 資料科學1.1 自建資料或從網路下載資料後上傳到雲端硬碟

# Iris.jpg
# 資料科學1.2 讀取Google雲端硬碟中的csv檔
# 資料科學1.3 將行列結構的資料建立為Pandas的資料框

filename = "data/Iris2.csv"
df = pd.read_csv(filename)
print(df)

df = df.drop("Id", axis=1)
print(df.head())

# 資料科學2. 資料處理
# 資料科學2.1 由列資料了解資料集

print(df.head())

# 資料科學2.2 了解行資料的標題與資料型別(整數、浮點數、字串等)

print(df.info())

# 資料科學2.3 資料清理

# 缺失值的補值或刪除

print(df.info())

# 刪除重複值或異常值

print(df[df.duplicated()])

df = df.drop_duplicates()

print(df[df.duplicated()])

df.reset_index(drop=True)  # 將列索引重新編號

# 資料轉換

s = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}
df["Species"] = df["Species"].map(s)
print(df.head())

# 資料科學3. 探索性資料分析
# 資料科學3.1 觀察資料的分佈(統計)
print(df.head())

# 資料科學3.2 資料視覺化

c = {0: "r", 1: "g", 2: "b"}
df["colors"] = df["Species"].map(c)
print(df)

df.plot(kind="scatter", x="SepalLengthCm", y="Species", c=df["colors"])
plt.show()

print("------------------------------")  # 30個

# (圖)-不同欄位和「類別(Species)」所繪製的散佈圖
# (a)花萼長度
df.plot(kind="scatter", x="SepalLengthCm", y="Species", c=df["colors"])
plt.show()

print("------------------------------")  # 30個

# (b)花萼寬度
df.plot(kind="scatter", x="SepalWidthCm", y="Species", c=df["colors"])
plt.show()

print("------------------------------")  # 30個

# (c)花瓣長度
df.plot(kind="scatter", x="PetalLengthCm", y="Species", c=df["colors"])
plt.show()

print("------------------------------")  # 30個

# (d)花瓣寬度
df.plot(kind="scatter", x="PetalWidthCm", y="Species", c=df["colors"])
plt.show()

print("------------------------------")  # 30個

# (圖)-2個欄位組合所繪製的散佈圖
# (a)花萼長度 vs. 花萼寬度
df.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm", c=df["colors"])
plt.show()

print("------------------------------")  # 30個

# (b)花瓣長度 vs. 花瓣寬度
df.plot(kind="scatter", x="PetalLengthCm", y="PetalWidthCm", c=df["colors"])
plt.show()

print("------------------------------")  # 30個

# (c)花萼長度 vs. 花瓣寬度
df.plot(kind="scatter", x="SepalLengthCm", y="PetalWidthCm", c=df["colors"])
plt.show()

print("------------------------------")  # 30個

# (d)花瓣長度 vs. 花萼寬度
df.plot(kind="scatter", x="PetalLengthCm", y="SepalWidthCm", c=df["colors"])
plt.show()

print("------------------------------")  # 30個

# (e)花萼長度 vs. 花瓣長度
df.plot(kind="scatter", x="SepalLengthCm", y="PetalLengthCm", c=df["colors"])
plt.show()

print("------------------------------")  # 30個

# (f)花萼寬度 vs. 花瓣寬度
df.plot(kind="scatter", x="SepalWidthCm", y="PetalWidthCm", c=df["colors"])
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 氣溫
t = [17, 17, 17, 22, 19, 21, 17, 17, 22, 24, 21, 21, 21, 17, 25, 21, 20, 19, 19, 22]

# 飲料銷售量
q = [
    386,
    360,
    383,
    146,
    300,
    254,
    403,
    381,
    269,
    99,
    171,
    204,
    213,
    279,
    97,
    262,
    262,
    225,
    240,
    226,
]

df = pd.DataFrame()

df["T"] = t  # 行資料：氣溫

df["Q"] = q  # 行資料：銷售量

print(df.head())

df.plot(kind="scatter", x="T", y="Q")
plt.show()

df_X = df[["T"]]  # 雙層的中括號(特徵值)，設定成資料框
df_y = df["Q"]  # 單層的中括號(標籤)，設定成序列
print(df_X.head())

print(df_y.head())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 8-2 機器學習實作

# 8-2-1 提出具體的假設
# 8-2-2 找出機器學習模型
# 挑選模型：匯入線性迴歸模型

from sklearn.linear_model import LinearRegression

# 學習訓練：建立並訓練線性迴歸模型

lm = LinearRegression()  # 建立新模型 lm
lm.fit(df_X, df_y)  # 訓練模型

# LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)

# 測試評估
# 決定模型：取出線性迴歸模型的 m、b 參數

print("線性迴歸的模型為 y = f(x) = mx +b")
print("m 為 ", lm.coef_)
print("b 為 ", lm.intercept_)

# 線性迴歸的模型為 y = f(x) = mx +b
# m 為  [-33.19704219]
# b 為  920.2809917355372

# 進行預測

temp = [[23]]  # 輸入特徵值(氣溫)
p = lm.predict(temp)  # 輸出標籤(預測的銷售量)
print(p)

# [156.74902131]

temp = [[23], [18], [36]]
p = lm.predict(temp)
print(p)

# [ 156.74902131  322.73423227 -274.81252719]

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 機器學習前準備─以Iris為例

# 1. 資料取得

filename = "data/Iris2.csv"

df = pd.read_csv(filename)

df = df.drop("Id", axis=1)

print(df.head())

# 2. 資料處理

df.info()

df = df.drop_duplicates()  # 刪除重複列
df.reset_index(drop=True)  # 將列索引重新編號
s = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}
df["Species"] = df["Species"].map(s)
df.info()

# 3. 探索性資料分析
print(df.head())
"""
#4. 機器學習做資料分析
9-2 機器學習實作──以Iris為例
9-2-1 提出具體的假設
9-2-2 找出機器學習模型
挑選模型：匯入 KNN 模型
"""

from sklearn.neighbors import KNeighborsClassifier

# 學習訓練：建立並訓練 KNN 模型

df_X = df[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]]
df_y = df["Species"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.2)

k = 1
knn = KNeighborsClassifier(n_neighbors=k)  # 建立新模型 knn

knn.fit(X_train, y_train)  # 用 training data 去訓練模型

# 測試評估

print("----KNN模式訓練後，取test data 進行分類的正確率計算-------")

print("準確率:", knn.score(X_test, y_test))

s = []
for i in range(3, 11):
    k = i
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)  # 用 training data 去訓練模型
    print("k =", k, " 準確率:", knn.score(X_test, y_test))  # 用 test data 檢測模型的準確率
    s.append(knn.score(X_test, y_test))

k = 8
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

# 加廣知識：視覺化圖表來顯示準確率

df_knn = pd.DataFrame()
df_knn["s"] = s
df_knn.index = [3, 4, 5, 6, 7, 8, 9, 10]
df_knn.plot(grid=True)

plt.show()

print("分類的預測結果：")
pred = knn.predict(X_test)  # 產生Test data預測結果
print(pred)

print(y_test.values)  # 觀察Test data真實數據

# 加廣知識：利用values屬性做橫式顯示

print(y_test)

print(y_test.values)

from sklearn.metrics import accuracy_score

accuracy_score(y_test, pred)

# 1.0

from sklearn.metrics import confusion_matrix

confusion_matrix(y_test, pred)

# 加深知識：交叉驗證概念

from sklearn.model_selection import cross_val_score

s = cross_val_score(knn, df_X, df_y, scoring="accuracy", cv=10)
print("交叉驗證每次的準確率：", s)
print("交叉驗證得到的平均準確率：", s.mean())

# 決定模型
# 進行分類預測

new = [[6.6, 3.1, 5.2, 2.4]]
v = knn.predict(new)
if v == 0:
    s = "Iris-Setosa"
elif v == 1:
    s = "Iris-Versicolour"
elif v == 2:
    s = "Iris-Virginica"
else:
    s = "錯誤"
print("預測結果為：", s)

# 預測結果為： 錯誤

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 機器學習前準備─以Titanic為例

# 1. 資料取得

filename = "data/titanic.csv"
df = pd.read_csv(filename)
print(df.head())

# 2. 資料處理
df.info()

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Embarked"] = df["Embarked"].fillna("S")
df = df.drop("Cabin", axis=1)
print("重複值：", df[df.duplicated()])  # 檢查有無重複值

df["Sex"] = df["Sex"].map({"female": 0, "male": 1})
df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})
print(df.head())

# 重複值： Empty DataFrame

# 3. 探索性資料分析

print(df.head())

"""
4. 機器學習做資料分析
9-4 機器學習實作─以Titanic為例
9-4-1 提出具體的假設
9-4-2 找出機器學習模型
挑選模型：匯入 KNN 模型
"""

from sklearn.neighbors import KNeighborsClassifier

# 學習訓練：建立並訓練 KNN 模型

df_X = df[["Sex", "Pclass"]]
df_y = df["Survived"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.2)

k = 1
knn = KNeighborsClassifier(n_neighbors=k)

knn.fit(X_train, y_train)

# 測試評估

print("----KNN模式訓練後，取test data 進行分類的準確率計算-------")
print("準確率:", knn.score(X_test, y_test))

s = []
for i in range(3, 11):
    k = i
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)  # 用 training data 去訓練模型
    print("k =", k, " 準確率:", knn.score(X_test, y_test))  # 用 test data 檢測模型的準確率
    s.append(knn.score(X_test, y_test))

k = 4
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

print("分類的預測結果：")
pred = knn.predict(X_test)
print(pred)  # 觀察預測結果

print("真實數據：")
print(y_test.values)  # 觀察真實數據(Test data)

from sklearn.metrics import accuracy_score

accuracy_score(y_test, pred)

# 0.7541899441340782

from sklearn.metrics import confusion_matrix

confusion_matrix(y_test, pred)

from sklearn.model_selection import cross_val_score

s = cross_val_score(knn, df_X, df_y, scoring="accuracy", cv=10)
print("準確率：", s)
print("平均準確率：", s.mean())
print("最高：", s.max())
print("最差：", s.min())

# 決定模型
# 進行分類預測

print("-----------(1)電影中兩位主角的生還推測-------------")

Rose = [[0, 1]]  # 女性 頭等艙 蘿絲（Rose DeWitt Bukater）
Jack = [[1, 3]]  # 男性 三等艙 傑克（Jack Dawson）
v = knn.predict(Rose)
if v == 1:
    s = "生還"
else:
    s = "死亡"
print("Rose能生還嗎 ? ", s)  # Rose為女性,及坐頭等艙

v = knn.predict(Jack)
if v == 1:
    s = "生還"
else:
    s = "死亡"

print("Jack能生還嗎 ? ", s)  # Jack為男性,及坐三等艙

# 真實的伊西多和伊達·斯特勞斯（Isidor and Ida Straus）夫婦 (You stay, I stay)
# http://www.epochtimes.com/b5/17/12/6/n9931745.htm
# Isidor 美國梅西百貨創辦人之一

print("-----(2)真實的伊西多和伊達·斯特勞斯夫婦的生還推測-------")
Mrs = [[0, 1]]  # 女性 頭等艙 Straus, Mrs. Isidor (Rosalie Ida Blun)
Mr = [[1, 1]]  # 男性 頭等艙 Straus, Mr. Isidor
v = knn.predict(Mrs)
if v == 1:
    s = "生還"
else:
    s = "死亡"
print("Mrs. Straus能生還嗎 ? ", s)  # Ida為女性,及坐頭等艙，可優先搭乘救生艇存活

v = knn.predict(Mr)  # Isidor的生存率有多高呢？
if v == 1:
    s = "生還"
else:
    s = "死亡"
print("Mr. Straus能生還嗎 ? ", s)

# 真實的 Mrs. Brown
# https://hokkfabrica.com/her-story-margaret-brown-from-titanic/
#

print("-----------(3)真實的Mrs. Brown的生還推測-------------")

# 女性 頭等艙 Brown, Mrs. James Joseph (Margaret Tobin) 故事中的暴發戶 對Jack很友善
Brown = [[0, 1]]
v = knn.predict(Brown)  # Mrs. Brown呢？
if v == 1:
    s = "生還"
else:
    s = "死亡"
print("Mrs. Brown能生還嗎 ? ", s)

print("-------------- (5)若你也搭上了鐵達尼號呢？ ----------------")

# s=input('您的性別（0：女，1：男），請輸入代碼？ ')
s = 1
# c=input('搭乘的船艙艙等（1：S艙，2：C艙，3：Q艙），請輸入代碼？ ')
c = 3
you = [[int(s), int(c)]]
v = knn.predict(you)
if v == 1:
    print("預測為:幸運生還")
else:
    print("預測為:無法生還")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 10-1 機器學習前準備
# 1. 資料取得

filename = "data/Iris2.csv"
df = pd.read_csv(filename)

df = df.drop("Id", axis=1)

print(df.head())

# 2. 資料處理

print(df.info())

df = df.drop_duplicates()  # 刪除重複列

df.reset_index(drop=True)  # 將列索引重新編號

s = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}

df["Species"] = df["Species"].map(s)

print(df.info())

# 3. 探索性資料分析
print(df.head())

# 4. 機器學習做資料分析
# 10-2 機器學習實作
# 挑選模型：匯入 K- 平均法模型

from sklearn.cluster import KMeans

# 學習訓練：建立並訓練 K-平均法模型

df_X = df[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]]
k = 1
km = KMeans(n_clusters=k)
km.fit(df_X)

# 測試評估

print("分群準確性:", km.inertia_)

# 分群準確性: 663.895238095238

s = []
for k in range(1, 15):
    km = KMeans(n_clusters=k)
    km.fit(df_X)
    s.append(km.inertia_)

print(s)

# [663.895238095238, 151.77145833333336, 77.91989035087718, 56.64237065018315, 45.816421929824564, 38.380978808131445, 34.1150969785575, 29.771330051212402, 27.730401211361738, 25.771261585636587, 24.236889472455648, 22.68941452991453, 21.258278047116285, 19.7686452991453]

# 看視覺化圖表決定參數K值
df_kmeans = pd.DataFrame()
df_kmeans["inertia_"] = s
df_kmeans.index = list(range(1, 15))
df_kmeans.plot(grid=True)
plt.show()

k = 3
km = KMeans(n_clusters=k)
km.fit(df_X)

print("分群的預測結果：")
pred = km.fit_predict(df_X)
print(pred)

# 決定模型
# 進行分群預測

df1 = df_X.copy()
df1["pred"] = pred

c = {0: "r", 1: "g", 2: "b"}

df1["colors"] = df1["pred"].map(c)
df1.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm", c=df1["colors"])

plt.show()

# 給一朵鳶尾花的4個特徵值：「花萼長度 6.6公分、花萼寬度 3.1公分、花瓣長度 5.2公分、花寬度 2.4公分」

new = [[6.6, 3.1, 5.2, 2.4]]

v = km.predict(new)

print("預測結果為：", v)

# 預測結果為： [0]

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


#normalize
#get_feature_names
#get_feature_names_out

#plt.rcParams['figure.figsize'] = 12, 8

np.random.seed(3)
np.random.seed(10)  #Setting seed for reproducability
np.random.seed(3)

