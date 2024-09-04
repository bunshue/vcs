"""

kilo 不可安裝 pip install sklearn


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
'''
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
import seaborn as sns
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

print('------------------------------------------------------------')	#60個

from sklearn.metrics.pairwise import cosine_similarity
cos_sims = cosine_similarity(doc_df)
print(cos_sims)

sims_df = pd.DataFrame(cos_sims, index = text, columns = text)
print(sims_df)

print('------------------------------------------------------------')	#60個

#tf-idf

vectorizer = TfidfVectorizer(min_df = 1)
data = vectorizer.fit_transform(corpus)
features = vectorizer.get_feature_names_out()
for word in features:
    print(word)

print('------------------------------------------------------------')	#60個

pd.set_option('display.precision', 2)
doc_df = pd.DataFrame(data.toarray(), index = text, columns = vectorizer.get_feature_names_out()).head(10)
print(doc_df)

print('------------------------------------------------------------')	#60個

#normalize
#get_feature_names
#get_feature_names_out

print('------------------------------------------------------------')	#60個

x = np.array([i * np.pi / 180 for i in range(60, 300, 4)])
np.random.seed(10)  #Setting seed for reproducability
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

print('------------------------------------------------------------')	#60個

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

plt.rcParams['figure.figsize'] = 12, 8

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

print('------------------------------------------------------------')	#60個


#Set the display format to be scientific for ease of analysis
pd.options.display.float_format = '{:,.2g}'.format
tt = coef_matrix_simple
print(tt)

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個

pd.options.display.float_format = '{:,.2g}'.format
tt = coef_matrix_ridge

print(tt)

print('------------------------------------------------------------')	#60個

#有多少個系數為0

coef_matrix_ridge.apply(lambda x: sum(x.values==0),axis=1)

print('------------------------------------------------------------')	#60個

""" fail
#L1 Regulariztion Lass Regression

from sklearn.linear_model import Lasso

def lasso_regression(data, predictors, alpha, models_to_plot={}):
    #Fit the model
    #lassoreg = Lasso(alpha=alpha,normalize=True, max_iter=1e5)
    lassoreg = Lasso(alpha=alpha, max_iter=1e5)
    lassoreg.fit(data[predictors],data['y'])
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

#Iterate over the 10 alpha values:
for i in range(10):
    coef_matrix_lasso.iloc[i,] = lasso_regression(data, predictors, alpha_lasso[i], models_to_plot)

plt.show()


print('------------------------------------------------------------')	#60個

pd.options.display.float_format = '{:,.2g}'.format
tt = coef_matrix_lasso
print(tt)


coef_matrix_lasso.apply(lambda x: sum(x.values==0),axis=1)

"""

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

print('------------------------------------------------------------')	#60個


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

print('------------------------------------------------------------')	#60個

similarity = np.asarray(np.asmatrix(data_n) * np.asmatrix(data_n).T)
tt = pd.DataFrame(similarity, index = corpus, columns = corpus).head(10)
print(tt)

import seaborn as sns
sns.heatmap(similarity, cmap = 'Reds')

plt.show()

print(pd.DataFrame(model.components_,index=['component_1','component_2'],columns=vectorizer.get_feature_names_out()).T)

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

import seaborn as sns

print('房價')
#from __future__ import print_function

import scipy.stats as stats

train = pd.read_csv(u'data/houseprice.csv')
print(train.head(3))

import scipy.stats as st

plt.figure()
sns.distplot(train['SalePrice'])

plt.show()

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個

#另一種查看是否服從正態分布的可視化方法

plt.figure()
sns.distplot(train['SalePrice'], fit=st.norm)

plt.figure()
res = st.probplot(train['SalePrice'], plot=plt)

plt.show()

print('------------------------------------------------------------')	#60個

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

'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# import seaborn as sns

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

data = norm.rvs(loc=mu, scale=sigma, size=N)

print(data)

print("------------------------------------------------------------")  # 60個

tt = norm.pdf(x=1.8, loc=1.6, scale=0.2)
print(tt)

tt = norm_prob(h, mu, sigma)
print(tt)

tt = loglikelihood(data, mu, sigma)
print(tt)

plt.hist(data)

plt.show()

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

person = pd.DataFrame()

# Create some feature values for this single row
person["Height"] = [6]
person["Weight"] = [130]
person["Size"] = [8]
person["Gender"] = ["female"]
# View the data
print(person)


print("------------------------------------------------------------")  # 60個

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


print("------------------------------------------------------------")  # 60個


def p_x_given_y_1(team, gender):
    return df3["p"][df3["Team"] == team][df3["Gender"] == gender].values[0]


print(p_x_given_y_1("i100", "female"))
# 0.4


print("------------------------------------------------------------")  # 60個


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


print("------------------------------------------------------------")  # 60個

# Group the data by gender and calculate the means of each feature
data_means = data.groupby("Team").mean()

# View the values
print(data_means)

print("------------------------------------------------------------")  # 60個


# Group the data by gender and calculate the variance of each feature
data_variance = data.groupby("Team").var()

# View the values
print(data_variance)


print("------------------------------------------------------------")  # 60個


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


print("------------------------------------------------------------")  # 60個


# 接下來，我們寫個公式來計算高斯分布的概率


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


print("------------------------------------------------------------")  # 60個

P_i100 * p_x_given_y_1("i100", person["Gender"][0]) * p_x_given_y_2(
    person["Height"][0], i100_height_mean, i100_height_variance
) * p_x_given_y_2(
    person["Weight"][0], i100_weight_mean, i100_weight_variance
) * p_x_given_y_2(
    person["Size"][0], i100_size_mean, i100_size_variance
)


print("------------------------------------------------------------")  # 60個

# Numerator of the posterior if the unclassified observation is a female
P_i500 * p_x_given_y_1("i500", person["Gender"][0]) * p_x_given_y_2(
    person["Height"][0], i500_height_mean, i500_height_variance
) * p_x_given_y_2(
    person["Weight"][0], i500_weight_mean, i500_weight_variance
) * p_x_given_y_2(
    person["Size"][0], i500_size_mean, i500_size_variance
)


print("------------------------------------------------------------")  # 60個


"""



"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
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

import matplotlib
import seaborn as sns

# from __future__ import print_function

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_regression

X, y = make_regression(n_samples=100, n_features=3)

print(X.shape, y.shape)

y = y.reshape((-1, 1))

# (100, 3) (100,)

plt.figure(figsize=(9, 4))

plt.plot(y, alpha=0.5, linewidth=3)

plt.show()

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X, y)

y_pred_sk = model.predict(X)

plt.figure(figsize=(9, 4))

plt.plot(y, color="r")
plt.plot(y, alpha=0.8, linewidth=5)

plt.plot(y_pred_sk, color="g")
plt.plot(y_pred_sk, linewidth=1)

plt.legend()

plt.show()


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

print(model.coef_)

# array([[48.54597102, 82.31351886,  8.52184984]])

print("------------------------------------------------------------")  # 60個

np.random.seed(3)
num_pos = 500

subset1 = np.random.multivariate_normal([0, 0], [[1, 0.6], [0.6, 1]], num_pos)
subset2 = np.random.multivariate_normal([0.5, 4], [[1, 0.6], [0.6, 1]], num_pos)

X = np.vstack((subset1, subset2))
y = np.hstack((np.zeros(num_pos), np.ones(num_pos)))

plt.scatter(X[:, 0], X[:, 1], c=y)

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import linear_model

clf = linear_model.LogisticRegression()

clf.fit(X, y)

"""
LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
,          intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,
,          penalty='l2', random_state=None, solver='liblinear', tol=0.0001,
,          verbose=0, warm_start=False)
"""

y_pred = clf.predict(X)

print(np.sum(y_pred.reshape(-1, 1) == y.reshape(-1, 1)) * 1.0 / len(y))

# 0.99

from sklearn.metrics import confusion_matrix

print(confusion_matrix(y, y_pred))

# [[495   5]
# [  5 495]]


print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個


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

print("------------------------------------------------------------")  # 60個

plt.style.use("bmh")
colors = ["#A60628", "#467821"]
plt.cmap = matplotlib.colors.ListedColormap(colors)

matplotlib.rcParams["figure.figsize"] = (10.0, 6.0)

np.random.seed(3)

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

"""
d:\Anaconda2\lib\site-packages\numpy\ma\core.py:6442: MaskedArrayFutureWarning: In the future the default for ma.maximum.reduce will be axis=0, not the current None, to match np.maximum.reduce. Explicitly pass 0 or None to silence this warning.

  return self.reduce(a)

d:\Anaconda2\lib\site-packages\numpy\ma\core.py:6442: MaskedArrayFutureWarning: In the future the default for ma.minimum.reduce will be axis=0, not the current None, to match np.minimum.reduce. Explicitly pass 0 or None to silence this warning.

  return self.reduce(a)
"""


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

"""
探索性數據分析（EDA）

EDA指對已有的數據用可視化等手段探索數據的結構和規律的一種數據分析方法，其目的是最大化對數據的直覺，完成這個事情的方法是結合統計學的圖形以各種形式展現出來。

在深入機器學習或統計建模之前，EDA是一個重要的步驟，這是因為它提供了為現有問題開發適當模型并正確解釋其結果所需的來龍去脈。

EDA通常涉及以下幾種方法的組合：

.原始數據集中每個字段的單變量可視化和匯總統計

.數據集中每個變量與感興趣目標變量之間的關系的雙變量可視化和匯總統計

.多元可視化以了解數據中不同字段之間的交互作用

.降維以了解數據,通過將數據折疊成幾個小數據點讓觀察值聚類成有區別的小組，可以更容易地識別行為模式

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

saleprice_scaled = StandardScaler().fit_transform(train["SalePrice"][:, np.newaxis])
low_range = saleprice_scaled[saleprice_scaled[:, 0].argsort()][:10]
high_range = saleprice_scaled[saleprice_scaled[:, 0].argsort()][-10:]
print("outer range (low) of the distribution:")
print(low_range)
print("\nouter range (high) of the distribution:")
print(high_range)

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

d:\Anaconda2\lib\site-packages\sklearnutils\validation.py:420: DataConversionWarning: Data with input dtype int64 was converted to float64 by StandardScaler.
  warnings.warn(msg, DataConversionWarning)

d:\Anaconda2\lib\site-packages\sklearnutils\validation.py:420: DataConversionWarning: Data with input dtype int64 was converted to float64 by StandardScaler.
  warnings.warn(msg, DataConversionWarning)
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


"""

d:\Anaconda2\lib\site-packages\sklearn\linear_model\least_angle.py:334: ConvergenceWarning: Early stopping the lars path, as the residues are small and the current value of alpha is no longer well controlled. 87 iterations, alpha=8.170e-04, previous alpha=2.386e-06, with an active set of 70 regressors.

  ConvergenceWarning)

d:\Anaconda2\lib\site-packages\sklearn\linear_model\least_angle.py:334: ConvergenceWarning: Early stopping the lars path, as the residues are small and the current value of alpha is no longer well controlled. 79 iterations, alpha=6.065e-04, previous alpha=1.923e-06, with an active set of 70 regressors.

  ConvergenceWarning)

0.12548614477031952

​"""

print("作業完成")

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
