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

import time
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

dist = euclidean_distances(rating_matrix)
print(dist)

from sklearn.metrics.pairwise import cosine_similarity
sim = cosine_similarity(rating_matrix)
print(sim)

print('------------------------------------------------------------')	#60個

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

text = ["小贝来到北京清华大学",
        "小花来到了网易杭研大厦",
        "小明硕士毕业于中国科学院",
        "小明爱北京小明爱北京天安门"
        ]
               
corpus = ["小贝 来到 北京 清华大学",
          "小花 来到 了 网易 杭研 大厦",
          "小明 硕士 毕业 于 中国 科学院",
          "小明 爱 北京 小明 爱 北京 天安门"
          ]

print('二值化、词频')
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

plt.rcParams['figure.figsize'] = 18, 9

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

from numpy.random import RandomState
import matplotlib.image as mpimg
from sklearn.datasets import fetch_olivetti_faces
from sklearn import decomposition

n_row, n_col = 2, 5
n_components = n_row * n_col
image_shape = (64, 64)
rng = RandomState(0)

print('------------------------------------------------------------')	#60個

faces = fetch_olivetti_faces(data_home='data\\',shuffle=True, random_state=rng)
print(faces.data.shape)

print('------------------------------------------------------------')	#60個

fig = plt.figure(figsize=(10, 10))
for i in range(10):
    ax = plt.subplot2grid((1, 10), (0, i))    
    ax.imshow(faces.data[i * 10].reshape(64, 64), cmap=plt.cm.gray)
    ax.axis('off')

plt.show()

print('------------------------------------------------------------')	#60個

pca = decomposition.PCA()
pca.fit(faces.data)

print(pca.components_.shape)

print('------------------------------------------------------------')	#60個

fig = plt.figure(figsize=(10, 10))
for i in range(10):
    ax = plt.subplot2grid((1, 10), (0, i))
    
    ax.imshow(pca.components_[i].reshape(64, 64), cmap=plt.cm.gray)
    ax.axis('off')

plt.show()

print('------------------------------------------------------------')	#60個

# pip install scikit-image
from skimage.io import imsave

face = faces.data[0]

trans = pca.transform(face.reshape(1, -1))
print(trans.shape)
for k in range(400):
    rank_k_approx = trans[:, :k].dot(pca.components_[:k]) + pca.mean_
    if k % 10 == 0:
        print('{:>03}'.format(str(k)) + '.jpg')
        #存圖fail
        #imsave('{:>03}'.format(str(k)) + '.jpg', rank_k_approx.reshape(64, 64))
        #imsave('cccc.jpg', rank_k_approx.reshape(64, 64))

print('------------------------------------------------------------')	#60個

"""
import matplotlib as mpl
from IPython.core.pylabtools import figsize

figsize(2 ,4)
plt.style.use('ggplot')
colors = ['#348ABD','#A60628','#7A68A6','#467821','#D55E00','#CC79A7','#56B4E9','#009E73','#F0E442','#0072B2']
plt.cmap = mpl.colors.ListedColormap(colors)
# plt.rcParams['savefig.dpi'] = 300
# plt.rcParams['figure.dpi'] = 300

from sklearn import datasets  
digits = datasets.load_digits(n_class=10)
X = digits.data
y = digits.target
n_samples, n_features = X.shape
n_neighbors = 30

print(X.shape)

fig = plt.figure()
for i in range(10):
    ax = plt.subplot2grid((1, 10), (0, i))
    ax.imshow(digits.data[i * 100].reshape(8, 8), cmap=plt.cm.gray)
    ax.axis('off')

plt.show()

print('------------------------------------------------------------')	#60個

def plot_embedding(ax , X):
    x_min, x_max = np.min(X, 0), np.max(X, 0)
    X = (X - x_min) / (x_max - x_min)
    for i in range(X.shape[0]):
        ax.text(X[i, 0], X[i, 1], str(digits.target[i]),
                color=colors[int(y[i] % 10)],
                fontdict={ 'size': 12})

def format_plot(ax,x_label,y_label, title):
    ax.xaxis.set_major_formatter(plt.NullFormatter())
    ax.yaxis.set_major_formatter(plt.NullFormatter())

    ax.set_title(title)
    

#PCA降維
from sklearn import decomposition,manifold
X_pca = decomposition.TruncatedSVD(n_components=2).fit_transform(X)

fig, ax = plt.subplots()
plot_embedding(ax,X_pca)
format_plot(ax,'','', 'PCA')

plt.show()

print('------------------------------------------------------------')	#60個

embedder = manifold.SpectralEmbedding(n_components=2, random_state=0,
                                      eigen_solver="arpack")
X_se = embedder.fit_transform(X)

tsne = manifold.TSNE(n_components=2, init='pca', random_state=0)

X_tsne = tsne.fit_transform(X)

mds =  manifold.MDS(n_components=2, n_init=1, max_iter=100)
X_mds = mds.fit_transform(X)

fig, ax = plt.subplots(2, 2)
figsize(20,16)
fig.subplots_adjust(left=0.0625, right=0.95, wspace=0.1)

plot_embedding(ax[0,0],X_pca)
format_plot(ax[0,0],'','', 'PCA') 

plot_embedding(ax[0,1],X_mds)
format_plot(ax[0,1],'','', 'MDS')

plot_embedding(ax[1,0],X_se)
format_plot(ax[1,0],'','', 'Spectral')

plot_embedding(ax[1,1],X_tsne)
format_plot(ax[1,1],'','', 'tSNE')

plt.show()


print('------------------------------------------------------------')	#60個

"""
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

sns.heatmap(similarity, cmap = 'Reds')
plt.show()


print(pd.DataFrame(model.components_,index=['component_1','component_2'],columns=vectorizer.get_feature_names_out()).T)


print('------------------------------------------------------------')	#60個

#from __future__ import print_function

"""
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

"""

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

"""
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
"""


print('------------------------------------------------------------')	#60個

from scipy.stats import norm

def norm_prob(x,mu,sigma):
    p = norm(mu,sigma).cdf(x+0.0001) - norm(mu,sigma).cdf(x-0.0001)
    return p

def loglikelihood(data,mu,sigma):
    l = 0.0
    for x in data:
        l -= np.log(norm_prob(x,mu,sigma))
    return l


N=1000
mu, sigma = 1.6, 0.2

h=1.8

data = norm.rvs(loc=mu, scale=sigma,size = N)

print(data)

print('------------------------------------------------------------')	#60個

tt = norm.pdf(x=1.8,loc=1.6,scale=0.2)
print(tt)

tt = norm_prob(h,mu,sigma)
print(tt)

tt = loglikelihood(data,mu,sigma)
print(tt)

plt.hist(data)

plt.show()

sys.exit()

print('------------------------------------------------------------')	#60個

mus = [1.4,1.5,1.6,1.7,1.8,1.9,2.0]
sigma =0.1
print(mus)

l = [loglikelihood(data,mu2,sigma) for mu2 in mus]
print(l)

df = pd.DataFrame()
df['mu'] = mus
df['-logl'] =l
print(df)

plt.figure(figsize=(6,4))

#sns.pointplot(df['mu'],df['-logl'], alpha=0.8) fail
#sns.pointplot(df['mu'],df['-logl']) fail

plt.show()

print('------------------------------------------------------------')	#60個

neg_data = u'data/neg.csv'
pos_data = u'data/pos.csv'

import codecs
import jieba

corpus = []
with codecs.open(neg_data,encoding='utf-8') as f:
    for line in f:
        words = list(jieba.cut(line.replace('|','')))
        corpus.append(' '.join(words))

neg_df = pd.DataFrame()
neg_df['content'] = corpus
neg_df['label'] = 0

corpus2 = []
with codecs.open(pos_data,encoding='utf-8') as f:
    for line in f:
        words = list(jieba.cut(line.replace('|','')))
        corpus2.append(' '.join(words))

pos_df = pd.DataFrame()
pos_df['content']=corpus2
pos_df['label'] = 1   

tt = neg_df.head(5)
print(tt)

tt = pos_df.head(5)
print(tt)

corpus_df = pd.concat((neg_df,pos_df))

tt = corpus_df.head(5)
print(tt)


print('------------------------------------------------------------')	#60個

from sklearn.feature_extraction.text import CountVectorizer

cv=CountVectorizer()
counts = cv.fit_transform(corpus_df['content'].values)

from sklearn.naive_bayes import MultinomialNB
classifier = MultinomialNB()
targets = corpus_df['label'].values
classifier.fit(counts, targets)

examples = [u'这 本 书 真差', u"这个 电影 还 可 以"]
example_counts = cv.transform(examples)
predictions = classifier.predict(example_counts)

print(predictions)


sys.exit()

print('------------------------------------------------------------')	#60個

# Create an empty dataframe
data = pd.DataFrame()

# Create our target variable
data['Gender'] = ['male','male','male','male','female','female','female','female']

# Create our feature variables
data['Height'] = [6,5.92,5.58,5.92,5,5.5,5.42,5.75]
data['Weight'] = [180,190,170,165,100,150,130,150]
data['Size'] = [12,11,12,10,6,8,7,9]
data['Team'] = ['i100','i100','i500','i100','i500','i100','i500','i100']

# View the data
print(data)

print('------------------------------------------------------------')	#60個

person = pd.DataFrame()

# Create some feature values for this single row
person['Height'] = [6]
person['Weight'] = [130]
person['Size'] = [8]
person['Gender'] = ['female']
# View the data 
print(person)


print('------------------------------------------------------------')	#60個

df1 = data.groupby(['Team','Gender']).size().rename('cnt').reset_index().set_index('Team')
df2 = pd.DataFrame(data.groupby(['Team']).size().rename('total'))

df3 = df1.merge(df2,left_index=True,right_index=True)
df3['p'] = df3['cnt'] * 1.0 /df3['total']
df3=df3.reset_index()
print(df3)


print('------------------------------------------------------------')	#60個


def p_x_given_y_1(team,gender):
     return df3['p'][df3['Team'] == team][df3['Gender']== gender].values[0]

print(p_x_given_y_1('i100','female'))
#0.4



print('------------------------------------------------------------')	#60個


#计算先验
# Number of i100
n_i100 = data['Team'][data['Team'] == 'i100'].count()

# Number of i500
n_i500 = data['Team'][data['Team'] == 'i500'].count()

# Total rows
total_ppl = data['Team'].count()



# Number of males divided by the total rows
P_i100 = n_i100*1.0/total_ppl

# Number of females divided by the total rows
P_i500 = n_i500*1.0/total_ppl

print(P_i100,P_i500)




print('------------------------------------------------------------')	#60個

# Group the data by gender and calculate the means of each feature
data_means = data.groupby('Team').mean()

# View the values
print(data_means)

print('------------------------------------------------------------')	#60個


# Group the data by gender and calculate the variance of each feature
data_variance = data.groupby('Team').var()

# View the values
print(data_variance)



print('------------------------------------------------------------')	#60個


#计算我们需要的均值方差
# Means for i100
i100_height_mean = data_means['Height'][data_means.index == 'i100'].values[0]
i100_weight_mean = data_means['Weight'][data_means.index == 'i100'].values[0]
i100_size_mean = data_means['Size'][data_means.index == 'i100'].values[0]

# Variance for i100
i100_height_variance = data_variance['Height'][data_variance.index == 'i100'].values[0]
i100_weight_variance = data_variance['Weight'][data_variance.index == 'i100'].values[0]
i100_size_variance = data_variance['Size'][data_variance.index == 'i100'].values[0]

# Means for i500
i500_height_mean = data_means['Height'][data_means.index == 'i500'].values[0]
i500_weight_mean = data_means['Weight'][data_means.index == 'i500'].values[0]
i500_size_mean = data_means['Size'][data_means.index == 'i500'].values[0]

# Variance for i500
i500_height_variance = data_variance['Height'][data_variance.index == 'i500'].values[0]
i500_weight_variance = data_variance['Weight'][data_variance.index == 'i500'].values[0]
i500_size_variance = data_variance['Size'][data_variance.index == 'i500'].values[0]



print('------------------------------------------------------------')	#60個


#接下来，我们写个公式来计算高斯分布的概率

def p_x_given_y_2(x, mean_y, variance_y):

    # Input the arguments into a probability density function
    p = 1/(np.sqrt(2*np.pi*variance_y)) * np.exp((-(x-mean_y)**2)/(2*variance_y))
    
    # return p
    return p

tt = person['Gender'][0]
print(tt)


print('------------------------------------------------------------')	#60個

P_i100 * p_x_given_y_1('i100',person['Gender'][0]) * \
p_x_given_y_2(person['Height'][0], i100_height_mean, i100_height_variance) * \
p_x_given_y_2(person['Weight'][0], i100_weight_mean, i100_weight_variance) * \
p_x_given_y_2(person['Size'][0], i100_size_mean, i100_size_variance)



print('------------------------------------------------------------')	#60個

# Numerator of the posterior if the unclassified observation is a female
P_i500 * p_x_given_y_1('i500',person['Gender'][0]) *\
p_x_given_y_2(person['Height'][0], i500_height_mean, i500_height_variance) * \
p_x_given_y_2(person['Weight'][0], i500_weight_mean, i500_weight_variance) * \
p_x_given_y_2(person['Size'][0], i500_size_mean, i500_size_variance)


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



