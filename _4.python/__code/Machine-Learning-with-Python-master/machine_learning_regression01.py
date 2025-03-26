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

print("------------------------------------------------------------")  # 60個

# from common1 import *
import scipy
import sklearn.linear_model
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.datasets import make_moons
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA  # KernelPCA 萃取特徵

from matplotlib.colors import ListedColormap
from sklearn.preprocessing import MinMaxScaler
from sklearn import tree


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
# Linear_Regression_Methods
# Linear regression with various methods
"""
This is a very simple example of using two scipy tools for linear regression.

    Scipy.Polyfit
    Stats.linregress
    Optimize.curve_fit
    numpy.linalg.lstsq
    statsmodels.OLS
    Analytic solution using Moore-Penrose generalized inverse or simple multiplicative matrix inverse
    sklearn.linear_model.LinearRegression
"""
from numpy import linspace, polyval, polyfit, sqrt#, stats, randn, optimize
from scipy import stats, optimize
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

# Generate random data of a sufficiently large size

#Sample data creation
#number of points 
n=int(5e6)
t=np.linspace(-10,10,n)
#parameters
a=3.25; b=-6.5
x=polyval([a,b],t)
#add some noise
xn=x+3*np.random.randn(n)

# Draw few random sample points and plot

xvar=np.random.choice(t,size=20)
yvar=polyval([a,b],xvar)+3*np.random.randn(20)
plt.scatter(xvar,yvar,c='green',edgecolors='k')
plt.grid(True)
show()

# Method: Scipy.Polyfit

#Linear regressison -polyfit - polyfit can be used other orders polynomials
t1=time.time()
(ar,br)=polyfit(t,xn,1)
xr=polyval([ar,br],t)
#compute the mean square error
err=sqrt(sum((xr-xn)**2)/n)
t2=time.time()
t_polyfit = float(t2-t1)

print('Linear regression using polyfit')
print('parameters: a=%.2f b=%.2f, ms error= %.3f' % (ar,br,err))
print("Time taken: {} seconds".format(t_polyfit))

# Method: Stats.linregress

#Linear regression using stats.linregress
t1=time.time()
(a_s,b_s,r,tt,stderr)=stats.linregress(t,xn)
t2=time.time()
t_linregress = float(t2-t1)

print('Linear regression using stats.linregress')
print('a=%.2f b=%.2f, std error= %.3f, r^2 coefficient= %.3f' % (a_s,b_s,stderr,r))
print("Time taken: {} seconds".format(t_linregress))

# Method: Optimize.curve_fit

def flin(t,a,b):
    result = a*t+b
    return(result)

t1=time.time()
p1,_=optimize.curve_fit(flin,xdata=t,ydata=xn,method='lm')
t2=time.time()
t_optimize_curve_fit = float(t2-t1)

print('Linear regression using optimize.curve_fit')
print('parameters: a=%.2f b=%.2f' % (p1[0],p1[1]))
print("Time taken: {} seconds".format(t_optimize_curve_fit))

# Method: numpy.linalg.lstsq

t1=time.time()
A = np.vstack([t, np.ones(len(t))]).T
result = np.linalg.lstsq(A, xn)
ar,br = result[0]
err = np.sqrt(result[1]/len(xn))
t2=time.time()
t_linalg_lstsq = float(t2-t1)

print('Linear regression using numpy.linalg.lstsq')
print('parameters: a=%.2f b=%.2f, ms error= %.3f' % (ar,br,err))
print("Time taken: {} seconds".format(t_linalg_lstsq))

# Method: Statsmodels.OLS

t1=time.time()
t=sm.add_constant(t)
model = sm.OLS(x, t)
results = model.fit()
ar=results.params[1]
br=results.params[0]
t2=time.time()
t_OLS = float(t2-t1)

print('Linear regression using statsmodels.OLS')
print('parameters: a=%.2f b=%.2f'% (ar,br))
print("Time taken: {} seconds".format(t_OLS))      

print(results.summary())

# Analytic solution using Moore-Penrose pseudoinverse

t1=time.time()
mpinv = np.linalg.pinv(t)
result = mpinv.dot(x)
ar = result[1]
br = result[0]
t2=time.time()
t_inv_matrix = float(t2-t1)

print('Linear regression using Moore-Penrose inverse')
print('parameters: a=%.2f b=%.2f'% (ar,br))
print("Time taken: {} seconds".format(t_inv_matrix)) 

# Analytic solution using simple multiplicative matrix inverse

t1=time.time()
m = np.dot((np.dot(np.linalg.inv(np.dot(t.T,t)),t.T)),x)
ar = m[1]
br = m[0]
t2=time.time()
t_simple_inv = float(t2-t1)

print('Linear regression using simple inverse')
print('parameters: a=%.2f b=%.2f'% (ar,br))
print("Time taken: {} seconds".format(t_simple_inv)) 

# Method: sklearn.linear_model.LinearRegression

t1=time.time()
lm = LinearRegression()
lm.fit(t,x)
ar=lm.coef_[1]
br=lm.intercept_
t2=time.time()
t_sklearn_linear = float(t2-t1)

print('Linear regression using sklearn.linear_model.LinearRegression')
print('parameters: a=%.2f b=%.2f'% (ar,br))
print("Time taken: {} seconds".format(t_sklearn_linear)) 

# Bucket all the execution times in a list and plot

times = [t_polyfit,t_linregress,t_optimize_curve_fit,t_linalg_lstsq,t_OLS,t_inv_matrix,t_simple_inv,t_sklearn_linear]

plt.figure(figsize=(20,5))
plt.grid(True)
plt.bar(x=[l*0.8 for l in range(8)],height=times, width=0.4,
        tick_label=['Polyfit','Stats.linregress','Optimize.curve_fit',
                    'numpy.linalg.lstsq','statsmodels.OLS','Moore-Penrose matrix inverse',
                    'Simple matrix inverse','sklearn.linear_model'])
show()

n_min = 50000
n_max = int(1e7)
n_levels = 25
r = np.log10(n_max/n_min)
l = np.linspace(0,r,n_levels)
n_data = list((n_min*np.power(10,l)))
n_data = [int(n) for n in n_data]

#time_dict={'Polyfit':[],'Stats.lingress':[],'Optimize.curve_fit':[],'linalg.lstsq':[],'statsmodels.OLS':[],
          #'Moore-Penrose matrix inverse':[],'Simple matrix inverse':[], 'sklearn.linear_model':[]}

l1=['Polyfit', 'Stats.lingress','Optimize.curve_fit', 'linalg.lstsq', 
 'statsmodels.OLS', 'Moore-Penrose matrix inverse', 'Simple matrix inverse', 'sklearn.linear_model']
time_dict = {key:[] for key in l1}


for i in range(len(n_data)):
    t=np.linspace(-10,10,n_data[i])
    #parameters
    a=3.25; b=-6.5
    x=polyval([a,b],t)
    #add some noise
    xn=x+3*np.random.randn(n_data[i])
    
    #Linear regressison -polyfit - polyfit can be used other orders polynomials
    t1=time.time()
    (ar,br)=polyfit(t,xn,1)
    t2=time.time()
    t_polyfit = 1e3*float(t2-t1)
    time_dict['Polyfit'].append(t_polyfit)
    
    #Linear regression using stats.linregress
    t1=time.time()
    (a_s,b_s,r,tt,stderr)=stats.linregress(t,xn)
    t2=time.time()
    t_linregress = 1e3*float(t2-t1)
    time_dict['Stats.lingress'].append(t_linregress)
    
    #Linear regression using optimize.curve_fit
    t1=time.time()
    p1,_=optimize.curve_fit(flin,xdata=t,ydata=xn,method='lm')
    t2=time.time()
    t_optimize_curve_fit = 1e3*float(t2-t1)
    time_dict['Optimize.curve_fit'].append(t_optimize_curve_fit)
    
    # Linear regression using np.linalg.lstsq (solving Ax=B equation system)
    t1=time.time()
    A = np.vstack([t, np.ones(len(t))]).T
    result = np.linalg.lstsq(A, xn)
    ar,br = result[0]
    t2=time.time()
    t_linalg_lstsq = 1e3*float(t2-t1)
    time_dict['linalg.lstsq'].append(t_linalg_lstsq)
    
    # Linear regression using statsmodels.OLS
    t1=time.time()
    t=sm.add_constant(t)
    model = sm.OLS(x, t)
    results = model.fit()
    ar=results.params[1]
    br=results.params[0]
    t2=time.time()
    t_OLS = 1e3*float(t2-t1)
    time_dict['statsmodels.OLS'].append(t_OLS)
    
    # Linear regression using Moore-Penrose pseudoinverse matrix
    t1=time.time()
    mpinv = np.linalg.pinv(t)
    result = mpinv.dot(x)
    ar = result[1]
    br = result[0]
    t2=time.time()
    t_mpinverse = 1e3*float(t2-t1)
    time_dict['Moore-Penrose matrix inverse'].append(t_mpinverse)
    
    # Linear regression using simple multiplicative inverse matrix
    t1=time.time()
    m = np.dot((np.dot(np.linalg.inv(np.dot(t.T,t)),t.T)),x)
    ar = m[1]
    br = m[0]
    t2=time.time()
    t_simple_inv = 1e3*float(t2-t1)
    time_dict['Simple matrix inverse'].append(t_simple_inv)
    
    # Linear regression using scikit-learn's linear_model
    t1=time.time()
    lm = LinearRegression()
    lm.fit(t,x)
    ar=lm.coef_[1]
    br=lm.intercept_
    t2=time.time()
    t_sklearn_linear = 1e3*float(t2-t1)
    time_dict['sklearn.linear_model'].append(t_sklearn_linear)

df = pd.DataFrame(data=time_dict)
df

plt.figure(figsize=(15,10))
for i in df.columns:
    plt.semilogx((n_data),df[i],lw=3)
plt.xticks([1e5,2e5,5e5,1e6,2e6,5e6,1e7],fontsize=15)
plt.xlabel("\nSize of the data set (number of samples)",fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel("Milliseconds needed for simple linear regression model fit\n",fontsize=15)
plt.grid(True)
plt.legend([name for name in df.columns],fontsize=20)
show()

a1=df.iloc[n_levels-1]

plt.figure(figsize=(20,5))
plt.grid(True)
plt.bar(x=[l*0.8 for l in range(8)],height=a1, width=0.4,
        tick_label=list(a1.index))
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Linear_Regression_Practice
# Linear Regrssion on US Housing Price

df = pd.read_csv("data/USA_Housing.csv")
df.head()

# Check basic info on the data set

df.info(verbose=True)

# 'describe()' method to get the statistical summary of the various features of the data set

df.describe(percentiles=[0.1,0.25,0.5,0.75,0.9])

#'columns' method to get the names of the columns (features)

df.columns

# Basic plotting and visualization on the data set

#Pairplots using seaborn

sns.pairplot(df)
show()

#Distribution of price (the predicted quantity)

df['Price'].plot.hist(bins=25,figsize=(8,4))

show()

df['Price'].plot.density()

show()

# Correlation matrix and heatmap

""" NG
df.corr()

plt.figure(figsize=(10,7))
sns.heatmap(df.corr(),annot=True,linewidths=2)

show()
"""

# Feature and variable sets

# Make a list of data frame column names

l_column = list(df.columns) # Making a list out of column names
len_feature = len(l_column) # Length of column vector list
l_column

# Put all the numerical features in X and Price in y, ignore Address which is string for linear regression

X = df[l_column[0:len_feature-2]]
y = df[l_column[len_feature-2]]

print("Feature set size:",X.shape)
print("Variable set size:",y.shape)

X.head()

y.head()

# Test-train split

# Create X and y train and test splits in one command using a split ratio and a random seed

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

# Check the size and shape of train/test splits (it should be in the ratio as per test_size parameter above)

print("Training feature set size:",X_train.shape)
print("Test feature set size:",X_test.shape)
print("Training variable set size:",y_train.shape)
print("Test variable set size:",y_test.shape)

# Model fit and training

# Import linear regression model estimator from scikit-learn and instantiate

from sklearn.linear_model import LinearRegression
from sklearn import metrics

lm = LinearRegression() # Creating a Linear Regression object 'lm'

# Fit the model on to the instantiated object itself

lm.fit(X_train,y_train) # Fit the linear model on to the 'lm' object itself i.e. no need to set this to another variable

# LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)

# Check the intercept and coefficients and put them in a DataFrame

print("The intercept term of the linear model:", lm.intercept_)

# The intercept term of the linear model: -2631028.90175

print("The coefficients of the linear model:", lm.coef_)

#idict = {'Coefficients':lm.intercept_}
#idf = pd.DataFrame(data=idict,index=['Intercept'])
cdf = pd.DataFrame(data=lm.coef_, index=X_train.columns, columns=["Coefficients"])
#cdf=pd.concat([idf,cdf], axis=0)
cdf

# Calculation of standard errors and t-statistic for the coefficients

n=X_train.shape[0]
k=X_train.shape[1]
dfN = n-k
train_pred=lm.predict(X_train)
train_error = np.square(train_pred - y_train)
sum_error=np.sum(train_error)
se=[0,0,0,0,0]
for i in range(k):
    r = (sum_error/dfN)
    r = r/np.sum(np.square(X_train[list(X_train.columns)[i]]-X_train[list(X_train.columns)[i]].mean()))
    se[i]=np.sqrt(r)
cdf['Standard Error']=se
cdf['t-statistic']=cdf['Coefficients']/cdf['Standard Error']
cdf

print("Therefore, features arranged in the order of importance for predicting the house price\n",'-'*90,sep='')
l=list(cdf.sort_values('t-statistic',ascending=False).index)
print(' > \n'.join(l))

l=list(cdf.index)
from matplotlib import gridspec
fig = plt.figure(figsize=(18, 10))
gs = gridspec.GridSpec(2,3)
#f, ax = plt.subplots(nrows=1,ncols=len(l), sharey=True)
ax0 = plt.subplot(gs[0])
ax0.scatter(df[l[0]],df['Price'])
ax0.set_title(l[0]+" vs. Price", fontdict={'fontsize':20})

ax1 = plt.subplot(gs[1])
ax1.scatter(df[l[1]],df['Price'])
ax1.set_title(l[1]+" vs. Price",fontdict={'fontsize':20})

ax2 = plt.subplot(gs[2])
ax2.scatter(df[l[2]],df['Price'])
ax2.set_title(l[2]+" vs. Price",fontdict={'fontsize':20})

ax3 = plt.subplot(gs[3])
ax3.scatter(df[l[3]],df['Price'])
ax3.set_title(l[3]+" vs. Price",fontdict={'fontsize':20})

ax4 = plt.subplot(gs[4])
ax4.scatter(df[l[4]],df['Price'])
ax4.set_title(l[4]+" vs. Price",fontdict={'fontsize':20})

show()

# R-square of the model fit

print("R-squared value of this fit:",round(metrics.r2_score(y_train,train_pred),3))

# R-squared value of this fit: 0.917

# Prediction, error estimate, and regression evaluation matrices

# Prediction using the lm model

predictions = lm.predict(X_test)
print ("Type of the predicted object:", type(predictions))
print ("Size of the predicted object:", predictions.shape)

# Scatter plot of predicted price and y_test set to see if the data fall on a 45 degree straight line

plt.figure(figsize=(10,7))
plt.title("Actual vs. predicted house prices",fontsize=25)
plt.xlabel("Actual test set house prices",fontsize=18)
plt.ylabel("Predicted house prices", fontsize=18)
plt.scatter(x=y_test,y=predictions)

show()

# Plotting histogram of the residuals i.e. predicted errors (expect a normally distributed pattern)

plt.figure(figsize=(10,7))
plt.title("Histogram of residuals to check for normality",fontsize=25)
plt.xlabel("Residuals",fontsize=18)
plt.ylabel("Kernel density", fontsize=18)
sns.distplot([y_test-predictions])

show()

# Scatter plot of residuals and predicted values (Homoscedasticity)

plt.figure(figsize=(10,7))
plt.title("Residuals vs. predicted values plot (Homoscedasticity)\n",fontsize=25)
plt.xlabel("Predicted house prices",fontsize=18)
plt.ylabel("Residuals", fontsize=18)
plt.scatter(x=predictions,y=y_test-predictions)

show()

# Regression evaluation metrices

print("Mean absolute error (MAE):", metrics.mean_absolute_error(y_test,predictions))
print("Mean square error (MSE):", metrics.mean_squared_error(y_test,predictions))
print("Root mean square error (RMSE):", np.sqrt(metrics.mean_squared_error(y_test,predictions)))

# R-square value

print("R-squared value of predictions:",round(metrics.r2_score(y_test,predictions),3))

# R-squared value of predictions: 0.919
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Linear regression as a statistical estimation problem

df = pd.read_csv("data/slump_test.csv", sep=",")

df.drop("No", axis=1, inplace=True)

df.head()

df.shape

# (103, 10)
"""
# Import MyLinearRegression from MLR and fit

from mlr.MLR import MyLinearRegression as mlr

m = mlr()

predictors = list(df.columns[:7])

print(predictors)

response = 'Compressive Strength (28-day)(Mpa)'

m.fit_dataframe(X=predictors,y=response,dataframe=df)

# Print all the coefficients and the intercept

m.coef_

m.intercept_

# 139.7814998489339

# Print metrics

print ("R-squared: ",m.r_squared())
print ("Adjusted R-squared: ",m.adj_r_squared())
print("MSE: ",m.mse())

# All metrics at once!

cc = m.print_metrics()
print(cc)

n = df.shape[0]
p = df.shape[1]-3

r2 = 1-(m.sse()/m.sst())
adjr2 = 1 - (m.sse()/m.sst())*((n-1)/(n-p-1))

print("R^2 from first principles:",round(r2,4))
print("Adjusted-R^2 from first principles:",round(adjr2,4))

#R^2 from first principles: 0.8968
#Adjusted-R^2 from first principles: 0.8892

#AIC and BIC

# AIC : Akaike information criterion
# BIC : Bayesian information criterion

# Residuals plots

m.fitted_vs_residual()

m.fitted_vs_features()

# Histogram and Q-Q plot of the standardized residuals

m.histogram_resid()

m.qqplot_resid()

# F-test of overall significance

m.ftest()

# (117.98260528684814, 5.444633963386908e-44)

# Standard errors, t-statistic, p-values

print("Standard errors:",m.std_err())
print()
print("t-test values:",m.tvalues())
print()
print("P-values:",m.pvalues())

for i in range(7):
    print(f"Predictor: {df.columns[i]}, Standard error: {m.std_err()[i+1]}, t-statistic: {m.tvalues()[i+1]}, p-value: {m.pvalues()[i+1]}")
    print()

# We can print the confidence interval of the regression coefficients directly

m.conf_int()[1:]

# If we change the statistical significance level to 0.01 from 0.05, then two more variables show range including zero

m.conf_int(alpha=0.01)[1:]

# Now, we can build a model removing those three variables who showed p-val > 0.05

m2 = mlr()

predictors = ['Cement', 'Fly ash', 'Water', 'Coarse Aggr.']

m2.fit_dataframe(X=predictors,y=response,dataframe=df)

print("Metrics of the old (full) model\n"+"-"*40)
m.print_metrics()

print("Metrics of the new (smaller) model\n"+"-"*40)
m2.print_metrics()

# We can also plot something called Cook's distance plot to see if there is any outliers in the data

m.cook_distance()

# We can plot the full pairwise scatterplots

m.pairplot()

# This may take a little time. Have patience...

# You can also use Seaborn library for visualization like pairplots and correlation heatmaps

sns.pairplot(data=df[df.columns[:7]])
show()

corr = np.corrcoef(df[df.columns[:7]],rowvar=False)
plt.figure(figsize=(10,10))
sns.heatmap(data=corr,linewidths=1,annot=True)
show()
"""
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


print("------------------------------------------------------------")  # 60個
