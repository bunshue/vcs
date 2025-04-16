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

# Robust linear regression

from sklearn.linear_model import HuberRegressor, LinearRegression
from sklearn.datasets import make_regression

# Creating a regression problem using make_regression method

rng = np.random.RandomState(0)

X, y, coef = make_regression(
    n_samples=200, n_features=2, noise=4.0, coef=True, random_state=0
)

# Plot

fix, ax = plt.subplots(1, 2, figsize=(10, 3))
ax[0].scatter(X[:, 0], y)
ax[0].grid(True)
ax[1].scatter(X[:, 1], y)
ax[1].grid(True)
plt.show()

# Inserting random outliers in the data

X[:4] = rng.uniform(10, 20, (4, 2))
y[:4] = rng.uniform(100, 200, 4)

# Plot to show the inserted outliers

fix, ax = plt.subplots(1, 2, figsize=(10, 3))
ax[0].scatter(X[:, 0], y)
ax[0].grid(True)
ax[1].scatter(X[:, 1], y)
ax[1].grid(True)
plt.show()

# Create a HuberRegressor object and fit

huber = HuberRegressor()

huber.fit(X, y)

cc = X[1].reshape(1, -1)
print(cc)

cc = huber.predict(X[1].reshape(1, -1))
print(cc)

# A simple linear regression fit for comparison

linear = LinearRegression()

linear.fit(X, y)

# Compare the estimated coefficients

print("True coefficients:", coef)
print("Huber coefficients:", huber.coef_)
print("Linear Regression coefficients:", linear.coef_)

fix, ax = plt.subplots(1, 2, figsize=(12, 3), sharey=True)
ax[0].barh(
    ["True coef", "Huber coef", "Linear fit coef"],
    width=[coef[0], huber.coef_[0], linear.coef_[0]],
)
ax[0].set_title("1st coefficients", fontsize=15)
ax[1].barh(
    ["True coef", "Huber coef", "Linear fit coef"],
    width=[coef[1], huber.coef_[1], linear.coef_[1]],
)
ax[1].set_title("2nd coefficients", fontsize=15)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Support vector regression

# A simple nonlinear function


def nonlinear(array):
    return (
        10 * array[:, 0] - np.exp(0.01 * array[:, 1] + np.log(1 + array[:, 2] ** 2))
    ) / (array[:, 3] ** 2 + 5)


# Generate features and target data for regression

n_samples = 200
n_features = 4

x = 5 * np.random.rand(n_samples, n_features)

y = nonlinear(x) + np.random.randn(n_samples)

y = y.reshape(n_samples, 1)

df = pd.DataFrame(data=np.hstack((x, y)), columns=["X1", "X2", "X3", "X4", "y"])

cc = df.head()
print(cc)

# Plotting the data

fig, ax = plt.subplots(2, 2, figsize=(10, 8))
ax = ax.ravel()
for i in range(4):
    ax[i].scatter(df[df.columns[i]], df["y"], edgecolor="k", color="red", alpha=0.75)
    ax[i].set_title(f"{df.columns[i]} vs. y", fontsize=14)
    ax[i].grid(True)
plt.show()

# Test/train split

X = df[["X1", "X2", "X3", "X4"]]
y = df["y"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)

# Support vector regressor with linear kernel

from sklearn.svm import SVR

svr_linear = SVR(kernel="linear", gamma="scale", C=1.0, epsilon=0.1)
svr_linear.fit(X_train, y_train)

# Test score

svr_linear.score(X_test, y_test)

# 0.5039103904226544

# Linear regression as a baseline

from sklearn.linear_model import LinearRegression

linear = LinearRegression()

linear.fit(X_train, y_train)

LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None)

linear.score(X_test, y_test)

# 0.5131204583471316

# Support vector regressor with Gaussian (radial basis function) kernel

svr_rbf = SVR(kernel="rbf", gamma="scale", C=1.0, epsilon=0.1)
svr_rbf.fit(X_train, y_train)

svr_rbf.score(X_test, y_test)

# 0.6473177483091139

# So, clearly, the RBF kernel showed better accuracy on the test set

from sklearn.metrics import mean_squared_error

print(
    "RMSE for linear SVR:",
    np.sqrt(mean_squared_error(y_test, svr_linear.predict(X_test))),
)
print(
    "RMSE for RBF kernelized SVR:",
    np.sqrt(mean_squared_error(y_test, svr_rbf.predict(X_test))),
)

# We can do a grid search of hyperparameters (with 5-fold cross-validation) to see if the test/validation score be improved

from sklearn.model_selection import GridSearchCV

params = {"C": [0.01, 0.05, 0.1, 0.5, 1, 2, 5], "epsilon": [0.1, 0.2, 0.5, 1]}

grid = GridSearchCV(
    svr_rbf, param_grid=params, cv=5, scoring="r2", verbose=1, return_train_score=True
)

grid.fit(X_train, y_train)

# Fitting 5 folds for each of 28 candidates, totalling 140 fits

# Check which was deemed best estimator by the grid search

cc = grid.best_estimator_
print(cc)

# Fit that estimator to the data and see

svr_best = SVR(kernel="rbf", gamma="scale", C=5.0, epsilon=0.5)
svr_best.fit(X_train, y_train)

svr_best.score(X_test, y_test)

# 0.6776661577094625

print(
    "RMSE for RBF kernelized SVR:",
    np.sqrt(mean_squared_error(y_test, svr_best.predict(X_test))),
)

# RMSE for RBF kernelized SVR: 1.163125361525394

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Regression_Diagnostics

# Visual analytics and diagnostics of model fit for linear regression

import statsmodels.formula.api as sm

# The dataset path may be different in your situation. Please use the correct path
df = pd.read_excel("data/Concrete_Data.xls")

cc = df.head()
print(cc)

cc = df.describe().T
print(cc)

# Taking a peek at the relationship between the predicting variables and the response

for c in df.columns[:-1]:
    print(c)
    plt.figure(figsize=(8, 5))
    plt.title("{} vs. \nConcrete Compressive Strength".format(c), fontsize=16)
    plt.scatter(
        x=df[c],
        y=df["Concrete compressive strength(MPa, megapascals) "],
        color="blue",
        edgecolor="k",
    )
    plt.grid(True)
    plt.xlabel(c, fontsize=14)
    plt.ylabel("Concrete compressive strength\n(MPa, megapascals)", fontsize=14)
    plt.show()

# Creating a copy with suitable column names for processing with statsmodels.OLS()

df1 = df.copy()

df1.columns = ["Component" + str(i) for i in range(1, 8)] + ["Age"] + ["y"]

cc = df1.head()
print(cc)

# Pairwise scatter plots

from seaborn import pairplot

pairplot(df1)
show()

# Correlation matrix and heatmap to visually check for multicollinearity

corr = df1[:-1].corr()

print(corr)

from statsmodels.graphics.correlation import plot_corr

fig = plot_corr(corr, xnames=corr.columns)
show()

# Creating a formula string for using in the statsmodels.OLS()

formula_str = df1.columns[-1] + " ~ " + "+".join(df1.columns[:-1])

print(formula_str)

# "y ~ Component1+Component2+Component3+Component4+Component5+Component6+Component7+Age"

# Construct and fit the model. Print summary of the fitted model

model = sm.ols(formula=formula_str, data=df1)

fitted = model.fit()

print("檢視模型架構")
fitted.summary()  # 檢視模型架構

# A new Result dataframe: p-values and statistical significance of the features

df_result = pd.DataFrame()

df_result["pvalues"] = fitted.pvalues[1:]

df_result["Features"] = df.columns[:-1]

df_result.set_index("Features", inplace=True)


def yes_no(b):
    if b:
        return "Yes"
    else:
        return "No"


df_result["Statistically significant?"] = df_result["pvalues"].apply(yes_no)

print(df_result)

# Residuals vs. predicting variables plots

for c in df.columns[:-1]:
    print(c)
    plt.figure(figsize=(8, 5))
    plt.title("{} vs. \nModel residuals".format(c), fontsize=16)
    plt.scatter(x=df[c], y=fitted.resid, color="blue", edgecolor="k")
    plt.grid(True)
    xmin = min(df[c])
    xmax = max(df[c])
    plt.hlines(y=0, xmin=xmin * 0.9, xmax=xmax * 1.1, color="red", linestyle="--", lw=3)
    plt.xlabel(c, fontsize=14)
    plt.ylabel("Residuals", fontsize=14)
    plt.show()

# Residual plots show some bit of clustering but overall the assumptions linearity and independence seem to hold because the distribution seem random around the 0 axis.

# Fitted vs. residuals

plt.figure(figsize=(8, 5))
p = plt.scatter(x=fitted.fittedvalues, y=fitted.resid, edgecolor="k")
xmin = min(fitted.fittedvalues)
xmax = max(fitted.fittedvalues)
plt.hlines(y=0, xmin=xmin * 0.9, xmax=xmax * 1.1, color="red", linestyle="--", lw=3)
plt.xlabel("Fitted values", fontsize=15)
plt.ylabel("Residuals", fontsize=15)
plt.title("Fitted vs. residuals plot", fontsize=18)
plt.grid(True)
plt.show()

# The fitted vs. residuals plot shows violation of the constant variance assumption - Heteroscedasticity.

# Histogram of normalized residuals

plt.figure(figsize=(8, 5))
plt.hist(fitted.resid_pearson, bins=20, edgecolor="k")
plt.ylabel("Count", fontsize=15)
plt.xlabel("Normalized residuals", fontsize=15)
plt.title("Histogram of normalized residuals", fontsize=18)
plt.show()

# Q-Q plot of the residuals

from statsmodels.graphics.gofplots import qqplot

plt.figure(figsize=(8, 5))
fig = qqplot(fitted.resid_pearson, line="45", fit="True")
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
plt.xlabel("Theoretical quantiles", fontsize=15)
plt.ylabel("Sample quantiles", fontsize=15)
plt.title("Q-Q plot of normalized residuals", fontsize=18)
plt.grid(True)
plt.show()

# The Q-Q plot (and the histogram above) shows that the normality assumption is satisfied pretty good

# Normality (Shapiro-Wilk) test of the residuals

from scipy.stats import shapiro

_, p = shapiro(fitted.resid)

if p < 0.01:
    print("The residuals seem to come from Gaussian process")
else:
    print("The normality assumption may not hold")

# The residuals seem to come from Gaussian process

# Cook"s distance (checking for outliers in residuals)

from statsmodels.stats.outliers_influence import OLSInfluence as influence

inf = influence(fitted)

(c, p) = inf.cooks_distance
plt.figure(figsize=(8, 5))
plt.title("Cook's distance plot for the residuals", fontsize=16)
plt.stem(np.arange(len(c)), c, markerfmt=",")
plt.grid(True)
plt.show()

# There are few data points with residuals being possible outliers

# Variance inflation factor

from statsmodels.stats.outliers_influence import variance_inflation_factor as vif

for i in range(len(df1.columns[:-1])):
    v = vif(np.matrix(df1[:-1]), i)
    print("Variance inflation factor for {}: {}".format(df.columns[i], round(v, 2)))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Ridge/LASSO polynomial regression with linear and random sampling

# Global variables for the program

N_points = 41  # Number of points for constructing function
x_min = 1  # Min of the range of x (feature)
x_max = 10  # Max of the range of x (feature)
noise_mean = 0  # Mean of the Gaussian noise adder
noise_sd = 2  # Std.Dev of the Gaussian noise adder
ridge_alpha = tuple(
    [10 ** (x) for x in range(-3, 0, 1)]
)  # Alpha (regularization strength) of ridge regression
lasso_eps = 0.001
lasso_nalpha = 20
lasso_iter = 1000
degree_min = 2
degree_max = 8

x_smooth = np.array(np.linspace(x_min, x_max, 1001))

# Linearly spaced sample points
X = np.array(np.linspace(x_min, x_max, N_points))

# Samples drawn from uniform random distribution
X_sample = x_min + np.random.rand(N_points) * (x_max - x_min)


def func(x):
    result = x**2 * np.sin(x) * np.exp(-(1 / x_max) * x)
    return result


noise_x = np.random.normal(loc=noise_mean, scale=noise_sd, size=N_points)

y = func(X) + noise_x
y_sampled = func(X_sample) + noise_x

df = pd.DataFrame(data=X, columns=["X"])
df["Ideal y"] = df["X"].apply(func)
df["y"] = y
df["X_sampled"] = X_sample
df["y_sampled"] = y_sampled
cc = df.head()
print(cc)

# Plot the function(s), both the ideal characteristic and the observed output (with process and observation noise)

df.plot.scatter(
    "X",
    "Ideal y",
    title="Ideal y",
    grid=True,
    edgecolors=(0, 0, 0),
    c="blue",
    s=40,
    figsize=(10, 5),
)
plt.plot(x_smooth, func(x_smooth), "k")
show()

df.plot.scatter(
    "X_sampled",
    y="y_sampled",
    title="Randomly sampled y",
    grid=True,
    edgecolors=(0, 0, 0),
    c="orange",
    s=40,
    figsize=(10, 5),
)
plt.plot(x_smooth, func(x_smooth), "k")
show()

df.plot.scatter(
    "X",
    y="y",
    title="Linearly sampled y",
    grid=True,
    edgecolors=(0, 0, 0),
    c="orange",
    s=40,
    figsize=(10, 5),
)
plt.plot(x_smooth, func(x_smooth), "k")
show()

# Import scikit-learn librares and prepare train/test splits

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LassoCV
from sklearn.linear_model import RidgeCV
from sklearn.ensemble import AdaBoostRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

X_train, X_test, y_train, y_test = train_test_split(df["X"], df["y"], test_size=0.33)
X_train = X_train.values.reshape(-1, 1)
X_test = X_test.values.reshape(-1, 1)

# Polynomial model with Ridge regularization (pipelined) with lineary spaced samples

linear_sample_score = []
poly_degree = []
for degree in range(degree_min, degree_max + 1):
    # model = make_pipeline(PolynomialFeatures(degree), RidgeCV(alphas=ridge_alpha,normalize=True,cv=5))
    model = make_pipeline(
        PolynomialFeatures(degree),
        LassoCV(eps=lasso_eps, n_alphas=lasso_nalpha, max_iter=lasso_iter, cv=5),
    )
    # model = make_pipeline(PolynomialFeatures(degree), LinearRegression(normalize=True))
    model.fit(X_train, y_train)
    y_pred = np.array(model.predict(X_train))
    test_pred = np.array(model.predict(X_test))
    RMSE = np.sqrt(np.sum(np.square(y_pred - y_train)))
    test_score = model.score(X_test, y_test)
    linear_sample_score.append(test_score)
    poly_degree.append(degree)
    print("Test score of model with degree {}: {}\n".format(degree, test_score))

    # plt.figure()
    # plt.title("RMSE: {}".format(RMSE),fontsize=10)
    # plt.suptitle("Polynomial of degree {}".format(degree),fontsize=15)
    # plt.xlabel("X training values")
    # plt.ylabel("Fitted and training values")
    # plt.scatter(X_train,y_pred)
    # plt.scatter(X_train,y_train)

    plt.figure()
    plt.title(
        "Predicted vs. actual for polynomial of degree {}".format(degree), fontsize=15
    )
    plt.xlabel("Actual values")
    plt.ylabel("Predicted values")
    plt.scatter(y_test, test_pred)
    plt.plot(y_test, y_test, "r", lw=2)

print(linear_sample_score)

# Modeling with randomly sampled data set

X_train, X_test, y_train, y_test = train_test_split(
    df["X_sampled"], df["y_sampled"], test_size=0.33
)
X_train = X_train.values.reshape(-1, 1)
X_test = X_test.values.reshape(-1, 1)

random_sample_score = []
poly_degree = []
for degree in range(degree_min, degree_max + 1):
    # model = make_pipeline(PolynomialFeatures(degree), RidgeCV(alphas=ridge_alpha,normalize=True,cv=5))
    model = make_pipeline(
        PolynomialFeatures(degree),
        LassoCV(eps=lasso_eps, n_alphas=lasso_nalpha, max_iter=lasso_iter, cv=5),
    )
    # model = make_pipeline(PolynomialFeatures(degree), LinearRegression(normalize=True))
    model.fit(X_train, y_train)
    y_pred = np.array(model.predict(X_train))
    test_pred = np.array(model.predict(X_test))
    RMSE = np.sqrt(np.sum(np.square(y_pred - y_train)))
    test_score = model.score(X_test, y_test)
    random_sample_score.append(test_score)
    poly_degree.append(degree)

    print("Test score of model with degree {}: {}\n".format(degree, test_score))

    # plt.figure()
    # plt.title("RMSE: {}".format(RMSE),fontsize=10)
    # plt.suptitle("Polynomial of degree {}".format(degree),fontsize=15)
    # plt.xlabel("X training values")
    # plt.ylabel("Fitted and training values")
    # plt.scatter(X_train,y_pred)
    # plt.scatter(X_train,y_train)

    plt.figure()
    plt.title(
        "Predicted vs. actual for polynomial of degree {}".format(degree), fontsize=15
    )
    plt.xlabel("Actual values")
    plt.ylabel("Predicted values")
    plt.scatter(y_test, test_pred)
    plt.plot(y_test, y_test, "r", lw=2)
    show()

print(random_sample_score)

df_score = pd.DataFrame(
    data={
        "degree": [d for d in range(degree_min, degree_max + 1)],
        "Linear sample score": linear_sample_score,
        "Random sample score": random_sample_score,
    }
)
print(df_score)

plt.figure(figsize=(8, 5))
plt.grid(True)
plt.plot(df_score["degree"], df_score["Linear sample score"], lw=2)
plt.plot(df_score["degree"], df_score["Random sample score"], lw=2)
plt.xlabel("Model Complexity: Degree of polynomial", fontsize=20)
plt.ylabel("Model Score: R^2 score on test set", fontsize=15)
plt.legend(fontsize=15)
show()


# Cehcking the regularization strength from the cross-validated model pipeline

m = model.steps[1][1]
print(m.alpha_)

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
