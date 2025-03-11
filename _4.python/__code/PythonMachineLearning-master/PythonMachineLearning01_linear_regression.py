"""
PythonMachineLearning-master 01

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

import sklearn.linear_model
import statsmodels.api as sm
from sklearn import tree
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from matplotlib.colors import ListedColormap
from sklearn.linear_model import LinearRegression

from scipy import stats
from scipy import optimize


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Interactive Machine Learning Demo

from ipywidgets import interact, interactive, IntSlider, Layout, interact_manual
import ipywidgets as widgets
from IPython.display import display

# Linear Regression and Regularization

N_samples = 25
x_min = -5
x_max = 5
x1 = np.linspace(x_min, x_max, N_samples * 5)
x = np.random.choice(x1, size=N_samples)
noise_std = 1
noise_mean = 0
noise_magnitude = 2

# Function definitions (ideal fitting function and actual data generating function with noise)


def func_gen(N_samples, x_min, x_max, noise_magnitude, noise_sd, noise_mean):
    x1 = np.linspace(x_min, x_max, N_samples * 5)
    x = np.random.choice(x1, size=N_samples)
    y = 2 * x - 0.6 * x**2 + 0.2 * x**3 + 18 * np.sin(x)
    y1 = 2 * x1 - 0.6 * x1**2 + 0.2 * x1**3 + 18 * np.sin(x1)
    y = y + noise_magnitude * np.random.normal(
        loc=noise_mean, scale=noise_sd, size=N_samples
    )
    plt.figure(figsize=(8, 5))
    plt.plot(x1, y1, c="k", lw=2)
    plt.scatter(x, y, edgecolors="k", c="yellow", s=60)
    plt.grid(True)
    plt.show()
    return (x, y, x1, y1)


# Call the 'interactive' widget with the data generating function, which also plots the data real-time

p = interactive(
    func_gen,
    N_samples={"Low (50 samples)": 50, "High (200 samples)": 200},
    x_min=(-5, 0, 1),
    x_max=(0, 5, 1),
    noise_magnitude=(0, 5, 1),
    noise_sd=(0.1, 1, 0.1),
    noise_mean=(-2, 2, 0.5),
)
display(p)

# Extract the data

# NG x,y,x1,y1 = p.result

# Load scikit-learn libraries

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LassoCV
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

# Machine learning (regression) model encapsulated within a function

lasso_eps = 0.01
lasso_nalpha = 20
lasso_iter = 3000
ridge_alphas = (0.001, 0.01, 0.1, 1)


def func_fit(model_type, test_size, degree):
    X_train, X_test, y_train, y_test = train_test_split(
        x, y, test_size=test_size, random_state=55
    )

    t1 = np.min(X_test)
    t2 = np.max(X_test)
    t3 = np.min(y_test)
    t4 = np.max(y_test)

    t5 = np.min(X_train)
    t6 = np.max(X_train)
    t7 = np.min(y_train)
    t8 = np.max(y_train)

    posx_test = t1 + (t2 - t1) * 0.7
    posx_train = t5 + (t6 - t5) * 0.7
    posy_test = t3 + (t4 - t3) * 0.2
    posy_train = t7 + (t8 - t7) * 0.2

    if model_type == "Linear regression":
        model = make_pipeline(
            PolynomialFeatures(degree, interaction_only=False),
            LinearRegression(normalize=True),
        )
    if model_type == "LASSO with CV":
        model = make_pipeline(
            PolynomialFeatures(degree, interaction_only=False),
            LassoCV(
                eps=lasso_eps,
                n_alphas=lasso_nalpha,
                max_iter=lasso_iter,
                normalize=True,
                cv=5,
            ),
        )

    if model_type == "Ridge with CV":
        model = make_pipeline(
            PolynomialFeatures(degree, interaction_only=False),
            RidgeCV(alphas=ridge_alphas, normalize=True, cv=5),
        )

    X_train = X_train.reshape(-1, 1)
    X_test = X_test.reshape(-1, 1)

    model.fit(X_train, y_train)

    train_pred = np.array(model.predict(X_train))
    train_score = model.score(X_train, y_train)

    test_pred = np.array(model.predict(X_test))
    test_score = model.score(X_test, y_test)

    RMSE_test = np.sqrt(np.mean(np.square(test_pred - y_test)))
    RMSE_train = np.sqrt(np.mean(np.square(train_pred - y_train)))

    print("Test score: {}, Training score: {}".format(test_score, train_score))

    print("RMSE Test: {}, RMSE train: {}".format(RMSE_test, RMSE_train))

    plt.figure(figsize=(12, 4))

    plt.subplot(1, 2, 1)
    plt.title("Test set performance\n", fontsize=16)
    plt.xlabel("X-test", fontsize=13)
    plt.ylabel("y-test", fontsize=13)
    plt.scatter(X_test, y_test, edgecolors="k", c="blue", s=60)
    plt.scatter(X_test, test_pred, edgecolors="k", c="yellow", s=60)
    plt.grid(True)
    plt.legend(["Actual test values", "Predicted values"])
    plt.text(x=posx_test, y=posy_test, s="Test score: %.3f" % (test_score), fontsize=15)

    plt.subplot(1, 2, 2)
    plt.title("Training set performance\n", fontsize=16)
    plt.xlabel("X-train", fontsize=13)
    plt.ylabel("y-train", fontsize=13)
    plt.scatter(X_train, y_train, c="blue")
    plt.scatter(X_train, train_pred, c="yellow")
    plt.grid(True)
    plt.legend(["Actual training values", "Fitted values"])
    plt.text(
        x=posx_train,
        y=posy_train,
        s="Training score: %.3f" % (train_score),
        fontsize=15,
    )

    plt.show()

    return (train_score, test_score)


# Run the encapsulated ML function with ipywidget interactive

style = {"description_width": "initial"}
# Continuous_update = False for IntSlider control to stop continuous model evaluation while the slider is being dragged
m = interactive(
    func_fit,
    model_type=widgets.RadioButtons(
        options=["Linear regression", "LASSO with CV", "Ridge with CV"],
        description="Choose Model",
        style=style,
        layout=Layout(width="250px"),
    ),
    test_size=widgets.Dropdown(
        options={
            "10% of data": 0.1,
            "20% of data": 0.2,
            "30% of data": 0.3,
            "40% of data": 0.4,
            "50% of data": 0.5,
        },
        description="Test set size",
        style=style,
    ),
    degree=widgets.IntSlider(
        min=1,
        max=10,
        step=1,
        description="Polynomial degree",
        stye=style,
        continuous_update=False,
    ),
)

# Set the height of the control.children[-1] so that the output does not jump and flicker
output = m.children[-1]
output.layout.height = "350px"

# Display the control
display(m)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Generate random data of a sufficiently large size

# Sample data creation
# number of points
n = int(5e6)
t = np.linspace(-10, 10, n)
# parameters
a = 3.25
b = -6.5
x = np.polyval([a, b], t)
# add some noise
xn = x + 3 * np.random.randn(n)

# Draw few random sample points and plot

xvar = np.random.choice(t, size=20)
yvar = np.polyval([a, b], xvar) + 3 * np.random.randn(20)
plt.scatter(xvar, yvar, c="green", edgecolors="k")
plt.grid(True)
plt.show()

print("------------------------------------------------------------")  # 60個

# Method: Scipy.Polyfit

# Linear regressison -polyfit - polyfit can be used other orders polynomials
t1 = time.time()
(ar, br) = np.polyfit(t, xn, 1)
xr = np.polyval([ar, br], t)
# compute the mean square error
err = np.sqrt(sum((xr - xn) ** 2) / n)
t2 = time.time()
t_polyfit = float(t2 - t1)

print("Linear regression using polyfit")
print("parameters: a=%.2f b=%.2f, ms error= %.3f" % (ar, br, err))
print("Time taken: {} seconds".format(t_polyfit))

"""
Linear regression using polyfit
parameters: a=3.25 b=-6.50, ms error= 3.000
Time taken: 1.7698638439178467 seconds
"""

# Method: Stats.linregress

# Linear regression using stats.linregress
t1 = time.time()
(a_s, b_s, r, tt, stderr) = stats.linregress(t, xn)
t2 = time.time()
t_linregress = float(t2 - t1)

print("Linear regression using stats.linregress")
print("a=%.2f b=%.2f, std error= %.3f, r^2 coefficient= %.3f" % (a_s, b_s, stderr, r))
print("Time taken: {} seconds".format(t_linregress))
"""
Linear regression using stats.linregress
a=3.25 b=-6.50, std error= 0.000, r^2 coefficient= 0.987
Time taken: 0.15017366409301758 seconds
"""

# Method: Optimize.curve_fit


def flin(t, a, b):
    result = a * t + b
    return result


t1 = time.time()
p1, _ = optimize.curve_fit(flin, xdata=t, ydata=xn, method="lm")
t2 = time.time()
t_optimize_curve_fit = float(t2 - t1)

print("Linear regression using optimize.curve_fit")
print("parameters: a=%.2f b=%.2f" % (p1[0], p1[1]))
print("Time taken: {} seconds".format(t_optimize_curve_fit))
"""
Linear regression using optimize.curve_fit
parameters: a=3.25 b=-6.50
Time taken: 1.2034447193145752 seconds
"""

# Method: numpy.linalg.lstsq

t1 = time.time()
A = np.vstack([t, np.ones(len(t))]).T
result = np.linalg.lstsq(A, xn)
ar, br = result[0]
err = np.sqrt(result[1] / len(xn))
t2 = time.time()
t_linalg_lstsq = float(t2 - t1)

print("Linear regression using numpy.linalg.lstsq")
print("parameters: a=%.2f b=%.2f, ms error= %.3f" % (ar, br, err))
print("Time taken: {} seconds".format(t_linalg_lstsq))
"""
Linear regression using numpy.linalg.lstsq
parameters: a=3.25 b=-6.50, ms error= 3.000
Time taken: 0.3698573112487793 seconds
"""
print("------------------------------")  # 30個

# Method: Statsmodels.OLS

t1 = time.time()
t = sm.add_constant(t)
model = sm.OLS(x, t)
results = model.fit()
ar = results.params[1]
br = results.params[0]
t2 = time.time()
t_OLS = float(t2 - t1)

print("Linear regression using statsmodels.OLS")
print("parameters: a=%.2f b=%.2f" % (ar, br))
print("Time taken: {} seconds".format(t_OLS))
"""
Linear regression using statsmodels.OLS
parameters: a=3.25 b=-6.50
Time taken: 0.9167804718017578 seconds
"""
print(results.summary())

# Analytic solution using Moore-Penrose pseudoinverse

t1 = time.time()
mpinv = np.linalg.pinv(t)
result = mpinv.dot(x)
ar = result[1]
br = result[0]
t2 = time.time()
t_inv_matrix = float(t2 - t1)

print("Linear regression using Moore-Penrose inverse")
print("parameters: a=%.2f b=%.2f" % (ar, br))
print("Time taken: {} seconds".format(t_inv_matrix))
"""
Linear regression using Moore-Penrose inverse
parameters: a=3.25 b=-6.50
Time taken: 0.6019864082336426 seconds
"""
# Analytic solution using simple multiplicative matrix inverse

t1 = time.time()
m = np.dot((np.dot(np.linalg.inv(np.dot(t.T, t)), t.T)), x)
ar = m[1]
br = m[0]
t2 = time.time()
t_simple_inv = float(t2 - t1)

print("Linear regression using simple inverse")
print("parameters: a=%.2f b=%.2f" % (ar, br))
print("Time taken: {} seconds".format(t_simple_inv))
"""
Linear regression using simple inverse
parameters: a=3.25 b=-6.50
Time taken: 0.13125276565551758 seconds
"""

# Method: sklearn.linear_model.LinearRegression

t1 = time.time()
lm = LinearRegression()
lm.fit(t, x)
ar = lm.coef_[1]
br = lm.intercept_
t2 = time.time()
t_sklearn_linear = float(t2 - t1)

print("Linear regression using sklearn.linear_model.LinearRegression")
print("parameters: a=%.2f b=%.2f" % (ar, br))
print("Time taken: {} seconds".format(t_sklearn_linear))
"""
Linear regression using sklearn.linear_model.LinearRegression
parameters: a=3.25 b=-6.50
Time taken: 0.5318112373352051 seconds
"""
# Bucket all the execution times in a list and plot

times = [
    t_polyfit,
    t_linregress,
    t_optimize_curve_fit,
    t_linalg_lstsq,
    t_OLS,
    t_inv_matrix,
    t_simple_inv,
    t_sklearn_linear,
]

plt.figure(figsize=(12, 5))

plt.grid(True)
plt.bar(
    x=[l * 0.8 for l in range(8)],
    height=times,
    width=0.4,
    tick_label=[
        "Polyfit",
        "Stats.linregress",
        "Optimize.curve_fit",
        "numpy.linalg.lstsq",
        "statsmodels.OLS",
        "Moore-Penrose matrix inverse",
        "Simple matrix inverse",
        "sklearn.linear_model",
    ],
)
plt.show()

n_min = 50000
n_max = int(1e7)
n_levels = 25
r = np.log10(n_max / n_min)
l = np.linspace(0, r, n_levels)
n_data = list((n_min * np.power(10, l)))
n_data = [int(n) for n in n_data]

# time_dict={'Polyfit':[],'Stats.lingress':[],'Optimize.curve_fit':[],'linalg.lstsq':[],'statsmodels.OLS':[],
#'Moore-Penrose matrix inverse':[],'Simple matrix inverse':[], 'sklearn.linear_model':[]}

l1 = [
    "Polyfit",
    "Stats.lingress",
    "Optimize.curve_fit",
    "linalg.lstsq",
    "statsmodels.OLS",
    "Moore-Penrose matrix inverse",
    "Simple matrix inverse",
    "sklearn.linear_model",
]
time_dict = {key: [] for key in l1}

from tqdm import tqdm

for i in tqdm(range(len(n_data))):
    t = np.linspace(-10, 10, n_data[i])
    # parameters
    a = 3.25
    b = -6.5
    x = np.polyval([a, b], t)
    # add some noise
    xn = x + 3 * np.random.randn(n_data[i])

    # Linear regressison -polyfit - polyfit can be used other orders polynomials
    t1 = time.time()
    (ar, br) = np.polyfit(t, xn, 1)
    t2 = time.time()
    t_polyfit = 1e3 * float(t2 - t1)
    time_dict["Polyfit"].append(t_polyfit)

    # Linear regression using stats.linregress
    t1 = time.time()
    (a_s, b_s, r, tt, stderr) = stats.linregress(t, xn)
    t2 = time.time()
    t_linregress = 1e3 * float(t2 - t1)
    time_dict["Stats.lingress"].append(t_linregress)

    # Linear regression using optimize.curve_fit
    t1 = time.time()
    p1, _ = optimize.curve_fit(flin, xdata=t, ydata=xn, method="lm")
    t2 = time.time()
    t_optimize_curve_fit = 1e3 * float(t2 - t1)
    time_dict["Optimize.curve_fit"].append(t_optimize_curve_fit)

    # Linear regression using np.linalg.lstsq (solving Ax=B equation system)
    t1 = time.time()
    A = np.vstack([t, np.ones(len(t))]).T
    result = np.linalg.lstsq(A, xn)
    ar, br = result[0]
    t2 = time.time()
    t_linalg_lstsq = 1e3 * float(t2 - t1)
    time_dict["linalg.lstsq"].append(t_linalg_lstsq)

    # Linear regression using statsmodels.OLS
    t1 = time.time()
    t = sm.add_constant(t)
    model = sm.OLS(x, t)
    results = model.fit()
    ar = results.params[1]
    br = results.params[0]
    t2 = time.time()
    t_OLS = 1e3 * float(t2 - t1)
    time_dict["statsmodels.OLS"].append(t_OLS)

    # Linear regression using Moore-Penrose pseudoinverse matrix
    t1 = time.time()
    mpinv = np.linalg.pinv(t)
    result = mpinv.dot(x)
    ar = result[1]
    br = result[0]
    t2 = time.time()
    t_mpinverse = 1e3 * float(t2 - t1)
    time_dict["Moore-Penrose matrix inverse"].append(t_mpinverse)

    # Linear regression using simple multiplicative inverse matrix
    t1 = time.time()
    m = np.dot((np.dot(np.linalg.inv(np.dot(t.T, t)), t.T)), x)
    ar = m[1]
    br = m[0]
    t2 = time.time()
    t_simple_inv = 1e3 * float(t2 - t1)
    time_dict["Simple matrix inverse"].append(t_simple_inv)

    # Linear regression using scikit-learn's linear_model
    t1 = time.time()
    lm = LinearRegression()
    lm.fit(t, x)
    ar = lm.coef_[1]
    br = lm.intercept_
    t2 = time.time()
    t_sklearn_linear = 1e3 * float(t2 - t1)
    time_dict["sklearn.linear_model"].append(t_sklearn_linear)

df = pd.DataFrame(data=time_dict)
df

plt.figure(figsize=(12, 8))
for i in df.columns:
    plt.semilogx((n_data), df[i], lw=3)
plt.xticks([1e5, 2e5, 5e5, 1e6, 2e6, 5e6, 1e7], fontsize=15)
plt.xlabel("\nSize of the data set (number of samples)", fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel("Milliseconds needed for simple linear regression model fit\n", fontsize=15)
plt.grid(True)
plt.legend([name for name in df.columns], fontsize=20)
plt.show()


a1 = df.iloc[n_levels - 1]

plt.figure(figsize=(12, 5))
plt.grid(True)
plt.bar(x=[l * 0.8 for l in range(8)], height=a1, width=0.4, tick_label=list(a1.index))
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Linear Regrssion on US Housing Price

df = pd.read_csv("./Datasets/USA_Housing.csv")
df.head()

# Check basic info on the data set

cc = df.info(verbose=True)
print(cc)

cc = df.describe(percentiles=[0.1, 0.25, 0.5, 0.75, 0.9])
print(cc)

cc = df.columns
print(cc)

# Basic plotting and visualization on the data set

# Pairplots using seaborn

sns.pairplot(df)
plt.show()

# Distribution of price (the predicted quantity)

df["Price"].plot.hist(bins=25, figsize=(8, 4))

plt.show()

df["Price"].plot.density()

plt.show()

# Correlation matrix and heatmap

# NG df.corr()

""" NG
plt.figure(figsize=(10,7))
sns.heatmap(df.corr(),annot=True,linewidths=2)

plt.show()
"""

# Feature and variable sets
# Make a list of data frame column names

l_column = list(df.columns)  # Making a list out of column names
len_feature = len(l_column)  # Length of column vector list
cc = l_column
print(cc)

# Put all the numerical features in X and Price in y, ignore Address which is string for linear regression

X = df[l_column[0 : len_feature - 2]]
y = df[l_column[len_feature - 2]]

print("Feature set size:", X.shape)
print("Variable set size:", y.shape)

# Feature set size: (5000, 5)
# Variable set size: (5000,)

cc = X.head()
print(cc)

cc = y.head()
print(cc)

# Test-train split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123
)

print("Training feature set size:", X_train.shape)
print("Test feature set size:", X_test.shape)
print("Training variable set size:", y_train.shape)
print("Test variable set size:", y_test.shape)

# Model fit and training

lm = LinearRegression()  # Creating a Linear Regression object 'lm'

# Fit the model on to the instantiated object itself

lm.fit(
    X_train, y_train
)  # Fit the linear model on to the 'lm' object itself i.e. no need to set this to another variable

# LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)

# Check the intercept and coefficients and put them in a DataFrame

print("The intercept term of the linear model:", lm.intercept_)

# The intercept term of the linear model: -2631028.90175

print("The coefficients of the linear model:", lm.coef_)

# idict = {'Coefficients':lm.intercept_}
# idf = pd.DataFrame(data=idict,index=['Intercept'])
cdf = pd.DataFrame(data=lm.coef_, index=X_train.columns, columns=["Coefficients"])
# cdf=pd.concat([idf,cdf], axis=0)
cdf

# Calculation of standard errors and t-statistic for the coefficients

n = X_train.shape[0]
k = X_train.shape[1]
dfN = n - k
train_pred = lm.predict(X_train)
train_error = np.square(train_pred - y_train)
sum_error = np.sum(train_error)
se = [0, 0, 0, 0, 0]
for i in range(k):
    r = sum_error / dfN
    r = r / np.sum(
        np.square(
            X_train[list(X_train.columns)[i]] - X_train[list(X_train.columns)[i]].mean()
        )
    )
    se[i] = np.sqrt(r)
cdf["Standard Error"] = se
cdf["t-statistic"] = cdf["Coefficients"] / cdf["Standard Error"]
cdf

print(
    "Therefore, features arranged in the order of importance for predicting the house price\n",
    "-" * 90,
    sep="",
)
l = list(cdf.sort_values("t-statistic", ascending=False).index)
print(" > \n".join(l))


l = list(cdf.index)

from matplotlib import gridspec

fig = plt.figure(figsize=(12, 8))
gs = gridspec.GridSpec(2, 3)
# f, ax = plt.subplots(nrows=1,ncols=len(l), sharey=True)
ax0 = plt.subplot(gs[0])
ax0.scatter(df[l[0]], df["Price"])
ax0.set_title(l[0] + " vs. Price", fontdict={"fontsize": 20})

ax1 = plt.subplot(gs[1])
ax1.scatter(df[l[1]], df["Price"])
ax1.set_title(l[1] + " vs. Price", fontdict={"fontsize": 20})

ax2 = plt.subplot(gs[2])
ax2.scatter(df[l[2]], df["Price"])
ax2.set_title(l[2] + " vs. Price", fontdict={"fontsize": 20})

ax3 = plt.subplot(gs[3])
ax3.scatter(df[l[3]], df["Price"])
ax3.set_title(l[3] + " vs. Price", fontdict={"fontsize": 20})

ax4 = plt.subplot(gs[4])
ax4.scatter(df[l[4]], df["Price"])
ax4.set_title(l[4] + " vs. Price", fontdict={"fontsize": 20})

plt.show()

# R-square of the model fit

print("R-squared value of this fit:", round(metrics.r2_score(y_train, train_pred), 3))

# R-squared value of this fit: 0.917

# Prediction, error estimate, and regression evaluation matrices

# Prediction using the lm model

predictions = lm.predict(X_test)
print("Type of the predicted object:", type(predictions))
print("Size of the predicted object:", predictions.shape)

# Type of the predicted object: <class 'numpy.ndarray'>
# Size of the predicted object: (1500,)

# Scatter plot of predicted price and y_test set to see if the data fall on a 45 degree straight line

plt.figure(figsize=(10, 7))
plt.title("Actual vs. predicted house prices", fontsize=25)
plt.xlabel("Actual test set house prices", fontsize=18)
plt.ylabel("Predicted house prices", fontsize=18)
plt.scatter(x=y_test, y=predictions)
plt.show()

# Plotting histogram of the residuals i.e. predicted errors (expect a normally distributed pattern)

plt.figure(figsize=(10, 7))
plt.title("Histogram of residuals to check for normality", fontsize=25)
plt.xlabel("Residuals", fontsize=18)
plt.ylabel("Kernel density", fontsize=18)
sns.histplot([y_test - predictions])

plt.show()

# Scatter plot of residuals and predicted values (Homoscedasticity)

plt.figure(figsize=(10, 7))

plt.title("Residuals vs. predicted values plot (Homoscedasticity)\n", fontsize=25)
plt.xlabel("Predicted house prices", fontsize=18)
plt.ylabel("Residuals", fontsize=18)
plt.scatter(x=predictions, y=y_test - predictions)

plt.show()

# Regression evaluation metrices

print("Mean absolute error (MAE):", metrics.mean_absolute_error(y_test, predictions))
print("Mean square error (MSE):", metrics.mean_squared_error(y_test, predictions))
print(
    "Root mean square error (RMSE):",
    np.sqrt(metrics.mean_squared_error(y_test, predictions)),
)

# Mean absolute error (MAE): 81739.7748272
# Mean square error (MSE): 10489638335.8
# Root mean square error (RMSE): 102418.935436

# R-square value

print(
    "R-squared value of predictions:", round(metrics.r2_score(y_test, predictions), 3)
)

# R-squared value of predictions: 0.919


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
