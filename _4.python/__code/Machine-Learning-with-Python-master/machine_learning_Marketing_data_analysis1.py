"""
Marketing_data_analysis

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


NUMBER_OF_RUNS = 2

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import warnings

warnings.filterwarnings("ignore", category=UserWarning)
import matplotlib as mpl

mpl.rcParams["figure.dpi"] = 125

from sklearn.preprocessing import StandardScaler
from sklearn.metrics import f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

# Load (cleaned and formatted) dataset

df = pd.read_csv("AddedFeatures_campaign_sale.csv")

df.info()

df.drop(["Index"], axis=1, inplace=True)

df.columns

cat_vars = [
    "Customer_engagement_length",
    "Language_group",
    "Repurchase Method",
    "Last Transaction Channel",
    "Number of Employees",
    "Service Level",
    "Do No Disturb",
    "Email Available",
    "Desk",
    "Executive Chair",
    "Standard Chair",
    "Monitor",
    "Printer",
    "Computer",
    "Insurance",
    "Toner",
    "Office Supplies",
]

d = pd.get_dummies(df, columns=cat_vars)

d.info()

# Classification

names = [
    "Logistic Regression",
    "Nearest Neighbors",
    "Linear SVM",
    "RBF SVM",
    "Decision Tree",
    "Random Forest",
    "Neural Net",
    "AdaBoost",
    "Bagging",
    "Naive Bayes",
    "QDA",
]

# List of classifier (Scikit-learn estimator objects with hyperparamemetr settings)

classifiers = [
    LogisticRegression(C=0.1, n_jobs=-1),
    KNeighborsClassifier(10, n_jobs=-1),
    SVC(kernel="linear", C=0.1),
    SVC(gamma="scale", C=1),
    DecisionTreeClassifier(max_depth=10, min_samples_leaf=10),
    RandomForestClassifier(
        max_depth=3, n_estimators=50, max_features=5, min_samples_leaf=10, n_jobs=-1
    ),
    MLPClassifier(
        hidden_layer_sizes=(100, 100),
        alpha=0.2,
        max_iter=200,
        learning_rate_init=0.01,
        learning_rate="adaptive",
        early_stopping=True,
        validation_fraction=0.2,
    ),
    AdaBoostClassifier(
        DecisionTreeClassifier(max_depth=3), n_estimators=50, learning_rate=0.1
    ),
    BaggingClassifier(
        DecisionTreeClassifier(max_depth=3), n_estimators=50, max_features=5, n_jobs=-1
    ),
    GaussianNB(),
    QuadraticDiscriminantAnalysis(reg_param=0.1),
]

# Test/train set

X = d.drop(["Campaign Period Sales", "Buy"], axis=1)
y = d["Buy"]

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

X_train = StandardScaler().fit_transform(X_train)
X_test = StandardScaler().fit_transform(X_test)

# Running through the classifiers once

for name, clf in zip(names, classifiers):
    t1 = time.time()
    clf.fit(X_train, y_train)
    t2 = time.time()
    delta_t = round((t2 - t1) * 1000, 3)
    score = round(clf.score(X_test, y_test), 3)
    print(f"Fitting with {name} took {delta_t} ms.\n Score: {score}")
    print("-" * 75)


# Function to run through classifiers repeatedly


def run_classifiers(clf_lst, names=None, num_runs=10, verbose=0):
    # Runs the list of classifiers for a fixed number of times
    if names is None:
        names = [str(type(c)).split(".")[-1][:-2] for c in clf_lst]
    scores = dict.fromkeys(names, [])
    f1_scores = dict.fromkeys(names, [])
    runtimes = dict.fromkeys(names, [])
    for name, clf in zip(names, clf_lst):
        sc, f1, rt = [], [], []
        for i in range(num_runs):
            print(i)
            # 資料分割
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
            X_train = StandardScaler().fit_transform(X_train)
            X_test = StandardScaler().fit_transform(X_test)
            t1 = time.time()
            clf.fit(X_train, y_train)
            t2 = time.time()
            delta_t = round((t2 - t1) * 1000, 3)
            score = round(clf.score(X_test, y_test), 3)
            f1score = f1_score(y_test, clf.predict(X_test))
            sc.append(score)
            f1.append(f1score)
            rt.append(delta_t)
        sc = np.array(sc)
        f1 = np.array(f1)
        rt = np.array(rt)
        scores[name] = sc
        f1_scores[name] = f1
        runtimes[name] = rt
        if verbose:
            print(f"Finished {num_runs} runs for {name} algorithm")
            print("-" * 75)
    # Convert to DataFrame
    df_scores = pd.DataFrame(scores)
    df_f1scores = pd.DataFrame(f1_scores)
    df_runtimes = pd.DataFrame(runtimes)

    return df_scores, df_f1scores, df_runtimes


# Run through clasifiers and plot

print("run_classifiers ST")
d1, d2, d3 = run_classifiers(
    clf_lst=classifiers, names=names, num_runs=NUMBER_OF_RUNS, verbose=1
)
print("run_classifiers SP")


d1


def plot_bars(
    d,
    t1="Mean accuracy score of algorithms",
    t2="Std.dev of the accuracy scores of algorithms",
):
    fig, ax = plt.subplots(1, 2, figsize=(14, 5))
    ax[0].barh(
        y=list(d.columns), width=d.describe().T["mean"], height=0.6, color="goldenrod"
    )
    ax[0].set_title(t1)
    ax[1].barh(
        y=list(d.columns), width=d.describe().T["std"], height=0.6, color="dodgerblue"
    )
    ax[1].set_title(t2)
    ax[0].spines["top"].set_visible(False)
    ax[0].spines["right"].set_visible(False)
    ax[0].spines["left"].set_visible(False)
    ax[0].spines["bottom"].set_color("#DDDDDD")
    ax[1].spines["top"].set_visible(False)
    ax[1].spines["right"].set_visible(False)
    ax[1].spines["left"].set_visible(False)
    ax[1].spines["bottom"].set_color("#DDDDDD")
    plt.tight_layout(pad=1.5)
    show()


mpl.rcParams.update(mpl.rcParamsDefault)
mpl.rcParams["xtick.labelsize"] = 13
mpl.rcParams["ytick.labelsize"] = 13
mpl.rcParams["figure.dpi"] = 125
mpl.rcParams["axes.titlesize"] = 18

plot_bars(
    d1,
    t1="Mean accuracy score of algorithms",
    t2="Std.dev of the accuracy scores of algorithms",
)

plot_bars(
    d2, t1="Mean F1-score of algorithms", t2="Std.dev of the F1-scores of algorithms"
)

plot_bars(
    d3,
    t1="Mean training time of algorithms",
    t2="Std.dev of the training time of algorithms",
)

print("------------------------------")  # 30個

# Grid search of AdaBoost

from sklearn.model_selection import GridSearchCV

abc = AdaBoostClassifier(DecisionTreeClassifier())
parameters = {
    "base_estimator__max_depth": [i for i in range(2, 11, 2)],
    "base_estimator__min_samples_leaf": [5, 10],
    "n_estimators": [10, 50, 250, 1000],
    "learning_rate": [0.01, 0.1],
}
clf = GridSearchCV(abc, parameters, verbose=3, scoring="f1", n_jobs=-1)
""" NG
clf.fit(X_train,y_train)

# Fitting 5 folds for each of 80 candidates, totalling 400 fits

boost_grid=pd.DataFrame(clf.cv_results_['params'])

boost_grid['F1-score']=clf.cv_results_['mean_test_score']

boost_grid

fig, ax = plt.subplots(2,2,figsize=(6,4))
ax= ax.ravel()
for i,c in enumerate(boost_grid.columns[:-1]):
    ax[i].scatter(boost_grid[c],boost_grid['F1-score'],
                 c='blue',edgecolor='k',alpha=0.7,s=150,
                 )
    ax[i].set_title(f"F1-score vs. {c}",fontsize=12)
    ax[i].set_ylim(0.5,0.8)
    ax[i].spines['top'].set_visible(False)
    ax[i].spines['right'].set_visible(False)
    ax[i].grid(True)
plt.tight_layout(pad=1.5)
show()
"""

print("------------------------------")  # 30個

# Regression

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor

# List of regressors (Scikit-learn estimator objects with hyperparamemetr settings)

reg_names = [
    "Linear regression",
    "L1 (LASSO) regression",
    "Ridge regression",
    "Support vector regression",
    "Decision tree regression",
    "Random forest regression",
    "Neural network regression",
]

regressors = [
    LinearRegression(n_jobs=-1),
    Lasso(alpha=0.1),
    Ridge(alpha=0.1),
    SVR(kernel="poly", degree=3),
    DecisionTreeRegressor(max_depth=10, min_samples_leaf=10),
    RandomForestRegressor(
        max_depth=3, n_estimators=50, max_features=5, min_samples_leaf=10, n_jobs=-1
    ),
    MLPRegressor(
        hidden_layer_sizes=(100, 100),
        alpha=0.2,
        max_iter=200,
        learning_rate_init=0.01,
        learning_rate="adaptive",
        early_stopping=True,
        validation_fraction=0.2,
    ),
]

# Regression data and test/train split

d_reg = d[d["Campaign Period Sales"] > 0.0]

X = d_reg.drop(["Campaign Period Sales", "Buy"], axis=1)
y = d_reg["Campaign Period Sales"]

# Function to run through classifiers repeatedly


def run_regressors(reg_lst, names=None, num_runs=10, verbose=0):
    # Runs the list of regressors for a fixed number of times
    if names is None:
        names = [str(type(c)).split(".")[-1][:-2] for c in reg_lst]
    scores = dict.fromkeys(names, [])
    runtimes = dict.fromkeys(names, [])
    for name, reg in zip(names, reg_lst):
        sc, rt = [], []
        for i in range(num_runs):
            print(i)
            # 資料分割
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
            X_train = StandardScaler().fit_transform(X_train)
            X_test = StandardScaler().fit_transform(X_test)
            t1 = time.time()
            reg.fit(X_train, y_train)
            t2 = time.time()
            delta_t = round((t2 - t1) * 1000, 3)
            rmse = round(
                np.sqrt(np.mean((reg.predict(X_test) - y_test) ** 2).mean()), 3
            )
            sc.append(rmse)
            rt.append(delta_t)
        sc = np.array(sc)
        rt = np.array(rt)
        scores[name] = sc
        runtimes[name] = rt
        if verbose:
            print(f"Finished {num_runs} runs for {name} algorithm")
            print("-" * 75)
    # Convert to DataFrame
    df_scores = pd.DataFrame(scores)
    df_runtimes = pd.DataFrame(runtimes)

    return df_scores, df_runtimes


# Run through regressors and plot

print("run_regressors ST")
d1_reg, d2_reg = run_regressors(
    reg_lst=regressors, names=reg_names, num_runs=NUMBER_OF_RUNS, verbose=1
)
print("run_regressors SP")

d1_reg

d1_reg1 = d1_reg.drop(["Linear regression"], axis=1)

d1_reg1["Neural network regression"].mean()

# 123.22044

plot_bars(
    d1_reg1,
    t1="RMSE score of algorithms",
    t2="Std.dev of the RMSE scores of algorithms",
)

plot_bars(
    d2_reg,
    t1="Mean training time of algorithms",
    t2="Std.dev of the training time of algorithms",
)

fig, ax = plt.subplots()
plt.hist(y, bins=100, edgecolor="k")
plt.xlim(0, 2000)
plt.vlines(x=398, ymin=0, ymax=600, color="k", linestyle="--", linewidth=3)
plt.vlines(
    x=d1_reg1["Neural network regression"].mean(),
    ymin=0,
    ymax=600,
    color="orange",
    linestyle="--",
    linewidth=3,
)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.grid(True)
show()

# Regression prediction and ground truth match plot

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
X_train = StandardScaler().fit_transform(X_train)
X_test = StandardScaler().fit_transform(X_test)
print("do MLPRegressor")
nn_reg = MLPRegressor(
    hidden_layer_sizes=(100, 100),
    alpha=0.2,
    max_iter=200,
    learning_rate_init=0.01,
    learning_rate="adaptive",
    early_stopping=True,
    validation_fraction=0.2,
)
nn_reg.fit(X_train, y_train)

preds = nn_reg.predict(X_test)

fig, ax = plt.subplots()
plt.scatter(x=y_test, y=preds, edgecolor="k", alpha=0.7, c="blue")
plt.plot(y_test, y_test, c="red")
plt.xlim(0, 5000)
plt.ylim(0, 5000)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.grid(True)
plt.xlabel("True campaign sales", fontsize=15)
plt.ylabel("Predicted campaign sales", fontsize=15)
show()

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
xlim = y_test.max()
X_train = StandardScaler().fit_transform(X_train)
X_test = StandardScaler().fit_transform(X_test)

fig, ax = plt.subplots(2, 3, figsize=(15, 10))
ax = ax.ravel()
for i in range(6):
    reg = regressors[1:][i]
    reg.fit(X_train, y_train)
    preds = reg.predict(X_test)
    ax[i].scatter(x=y_test, y=preds, edgecolor="k", alpha=0.7, c="blue")
    ax[i].plot(y_test, y_test, c="red")
    ax[i].set_xlim(0, xlim * 1.1)
    ax[i].set_ylim(0, xlim * 1.1)
    ax[i].spines["top"].set_visible(False)
    ax[i].spines["right"].set_visible(False)
    ax[i].grid(True)
    ax[i].set_xlabel("True campaign sales", fontsize=15)
    ax[i].set_ylabel("Predicted campaign sales", fontsize=15)
    ax[i].set_title(reg_names[1:][i])
plt.tight_layout(pad=1.5)
show()

print("NN model tuning for regression")

no_neurons = [i * 10 for i in range(1, 11)]
alpha = [0.01, 0.1, 0.2, 0.5]
learning_rate = [0.01, 0.05, 0.1]
activation = ["relu", "tanh", "logistic"]

nn_grid = {
    "neurons": [],
    "alpha": [],
    "learning_rate": [],
    "activation": [],
    "RMSE": [],
    "training-time": [],
}

nn_grid

X = d_reg.drop(["Campaign Period Sales", "Buy"], axis=1)
y = d_reg["Campaign Period Sales"]

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
X_train = StandardScaler().fit_transform(X_train)
X_test = StandardScaler().fit_transform(X_test)

from tqdm import tqdm

for n in tqdm(no_neurons):
    print("n :", n)
    for a in tqdm(alpha):
        print("a :", a)
        for l in learning_rate:
            print("l :", l)
            for act in activation:
                print("act :", act)
                reg = MLPRegressor(
                    hidden_layer_sizes=(n, n),
                    alpha=a,
                    activation=act,
                    max_iter=200,
                    learning_rate_init=l,
                    learning_rate="adaptive",
                    early_stopping=True,
                    validation_fraction=0.2,
                )
                t1 = time.time()
                reg.fit(X_train, y_train)
                t2 = time.time()
                delta_t = round((t2 - t1) * 1000, 3)
                rmse = round(
                    np.sqrt(np.mean((reg.predict(X_test) - y_test) ** 2).mean()), 3
                )
                nn_grid["neurons"].append(n)
                nn_grid["alpha"].append(a)
                nn_grid["learning_rate"].append(l)
                nn_grid["activation"].append(act)
                nn_grid["RMSE"].append(rmse)
                nn_grid["training-time"].append(delta_t)

nn_grid = pd.DataFrame(nn_grid)

nn_grid.shape

# (360, 6)

nn_grid.head()

plt.scatter(x=[i for i in range(len(nn_grid))], y=nn_grid["RMSE"])
plt.ylim(0, 600)
show()

fig, ax = plt.subplots(2, 2, figsize=(12, 10))
ax = ax.ravel()
for i, c in enumerate(nn_grid.columns[:4]):
    ax[i].scatter(nn_grid[c], nn_grid["RMSE"], edgecolor="k", alpha=0.7, c="blue")
    ax[i].set_title(f"RMSE vs. {c}")
    ax[i].grid(True)
    ax[i].spines["top"].set_visible(False)
    ax[i].spines["right"].set_visible(False)
show()

print("Sample complexity")

sample_complexity = dict.fromkeys(names, [])
frac = [0.1 * i for i in range(1, 11)]
for name, clf in list(zip(names, classifiers)):
    scores = []
    for f in frac:
        d_frac = d.sample(frac=f)
        X = d_frac.drop(["Campaign Period Sales", "Buy"], axis=1)
        y = d_frac["Buy"]
        # 資料分割
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        X_train = StandardScaler().fit_transform(X_train)
        X_test = StandardScaler().fit_transform(X_test)
        t1 = time.time()
        clf.fit(X_train, y_train)
        t2 = time.time()
        delta_t = round((t2 - t1) * 1000, 3)
        f1score = f1_score(y_test, clf.predict(X_test))
        scores.append(f1score)
    sample_complexity[name] = np.array(scores)
    # print(sample_complexity[name])
    print(f"Done for {name}")


sample_complexity = pd.DataFrame(sample_complexity)

fig, ax = plt.subplots(4, 3, figsize=(16, 16), sharey=True)
ax = ax.ravel()
for i, c in enumerate(sample_complexity.columns):
    ax[i].plot(
        [int(j) for j in range(1, 11)], sample_complexity[c], marker="o", color="blue"
    )
    ax[i].set_xticks([int(j) for j in range(1, 11, 2)])
    ax[i].set_xticklabels([str(10 * j) + "%" for j in range(1, 11, 2)])
    ax[i].set_title(f"{c}", fontsize=14)
    ax[i].grid(True)
    ax[i].spines["top"].set_visible(False)
    ax[i].spines["right"].set_visible(False)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Data_wrangling(爭吵,爭辯)

supply = pd.read_csv("data/office_supply.csv")

supply = supply[
    [
        "Customer Number",
        "Service Level",
        " Date of Last Transaction ",
        "Number of Transactions",
        "Email Available",
    ]
]
supply.columns = [
    "Customer Number",
    "Service Level",
    "Date of Last Transaction",
    "Number of Transactions",
    "Email Available",
]

campaign = pd.read_excel(
    "data/office_supply_campaign_results.xlsx",
    sheet_name="Campaign Results",
    na_values=[" ", ""],
    true_values=["TRUE"],
    false_values=["FALSE"],
)

# Columns

campaign.columns

for c1 in supply.columns:
    if c1 not in campaign.columns:
        print(c1)

# Join

supply["Customer Number"] = supply["Customer Number"].apply(lambda x: int(x))

campaign = campaign.dropna(axis=0, subset=["Customer Number"])

campaign["Customer Number"] = campaign["Customer Number"].apply(lambda x: int(x))

df = campaign.merge(supply, on="Customer Number")

df.head()

df["Date of Last Transaction"] = pd.to_datetime(df["Date of Last Transaction"])

df["Number of Prior Year Transactions"] = df["Number of Prior Year Transactions"].apply(
    lambda x: int(x)
)

df.info()

# Fill Language missing values by Unknown

df["Language"].fillna("Unknown", inplace=True)

# Dropping all other missing values

df = df.dropna()

df.columns

df.info()

# Categorical variables

cat_vars = [
    "Do Not Direct Mail Solicit",
    "Do Not Email",
    "Do Not Telemarket",
    "Repurchase Method",
    "Last Transaction Channel",
    "Desk",
    "Executive Chair",
    "Standard Chair",
    "Monitor",
    "Printer",
    "Computer",
    "Insurance",
    "Toner",
    "Office Supplies",
    "Number of Employees",
    "Language",
    "Service Level",
    "Email Available",
]

len(cat_vars)

# What are the unique values in the columns?

for v in cat_vars:
    print(f"Values in {v}: {df[v].unique()}")

# Converting boolean columns to proper data types

# type_dict = {}

df = df.astype(
    {
        "Do Not Direct Mail Solicit": "bool",
        "Do Not Email": bool,
        "Do Not Telemarket": bool,
    }
)

df.info()

fig, ax = plt.subplots(6, 3, figsize=(18, 25), squeeze=False, sharey=True)
fig.tight_layout(pad=2.0)
ax = ax.ravel()
for i in range(18):
    sns.stripplot(
        x=cat_vars[i], y="Campaign Period Sales", data=df, ax=ax[i], edgecolor="k"
    )
    ax[i].set_xlabel(cat_vars[i], fontsize=14)
    if len(df[cat_vars[i]].unique()) > 3:
        ax[i].set_xticklabels(labels=df[cat_vars[i]].unique(), rotation=90)
show()

fig, ax = plt.subplots(6, 3, figsize=(12, 18), squeeze=True, sharey=True)
ax = ax.ravel()
for i in range(18):
    ax[i].pie(df[cat_vars[i]].value_counts(), labels=df[cat_vars[i]].unique())
    ax[i].set_xlabel(cat_vars[i], fontsize=14)
show()

# Buy/No buy?

df["Buy"] = (df["Campaign Period Sales"] > 0).apply(lambda x: int(x))

plt.hist(df["Buy"])
show()

# Customer engagement length (days)

df["Customer_engagement_days"] = (
    pd.Timestamp.now().normalize() - df["Date of First Purchase"]
).dt.days

df["Days_since_last_transaction"] = (
    pd.Timestamp.now().normalize() - df["Date of Last Transaction"]
).dt.days

plt.hist(df["Customer_engagement_days"] / 365, bins=25, edgecolor="k")
show()

df["Date of First Purchase"].describe()

plt.hist(df["Days_since_last_transaction"], bins=25, edgecolor="k")
show()


def customer_engagement(d):
    m = df["Customer_engagement_days"].mean()
    s = df["Customer_engagement_days"].std()
    if d >= m + s:
        return "Long-term"
    elif d > m - s and d < m + s:
        return "Mid-term"
    else:
        return "Short-term"


m = df["Customer_engagement_days"].mean()
s = df["Customer_engagement_days"].std()

print(m / 365, s / 365)

df["Customer_engagement_length"] = df["Customer_engagement_days"].apply(
    customer_engagement
)

sns.stripplot(x="Customer_engagement_length", y="Campaign Period Sales", data=df)
show()

df2 = df[df["Buy"] == 1]
plt.scatter(df2["Customer_engagement_days"] / 365, df2["Campaign Period Sales"])
show()

# Language grouping

df["Language"].unique()


def language_group(lan):
    if lan == "English":
        return "English"
    elif (
        lan == "Hindi"
        or lan == "Chinese"
        or lan == "Hebrew"
        or lan == "Japanese"
        or lan == "Arabic"
        or lan == "Vietnamese"
        or lan == "Thai"
        or lan == "Pashto"
    ):
        return "Asian"
    elif lan == "Unknown":
        return "Unknown"
    else:
        return "European"


df["Language_group"] = df["Language"].apply(language_group)

df.info()

plt.hist(df[df["Buy"] == 1]["Campaign Period Sales"], bins=25, edgecolor="k")
plt.xlim(0, 2000)
show()

# Saving to a CSV

df.to_csv("tmp_Cleaned_campaign_sale.csv")

d = pd.get_dummies(df, columns=cat_vars)

from sklearn.preprocessing import OneHotEncoder

d.info()

d.head()

len(d[d["Campaign Period Sales"] == 0.0])

fig, ax = plt.subplots(1, 2, figsize=(18, 6))
ax[0].scatter(
    d["Historical Sales Volume"], d["Campaign Period Sales"], c="blue", edgecolor="k"
)
ax[0].set_title("Historical Sales Volume", fontsize=18)
ax[1].scatter(
    d["Number of Prior Year Transactions"],
    d["Campaign Period Sales"],
    c="blue",
    edgecolor="k",
)
ax[1].set_title("Number of Prior Year Transactions", fontsize=18)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Dataviz

import warnings

warnings.filterwarnings("ignore", category=UserWarning)
import matplotlib as mpl

mpl.rcParams["figure.dpi"] = 125

df = pd.read_csv("data/AddedFeatures_campaign_sale.csv")

df.info()

df.head()

df.columns[:12]

num_vars = [
    "Historical Sales Volume",
    "Number of Prior Year Transactions",
    "Number of Transactions",
    "Purchase Breadth",
    "Customer_engagement_days",
    "Days_since_last_transaction",
]
cat_vars = [
    "Customer_engagement_length",
    "Language_group",
    "Repurchase Method",
    "Last Transaction Channel",
    "Number of Employees",
    "Service Level",
    "Do No Disturb",
    "Email Available",
    "Desk",
    "Executive Chair",
    "Standard Chair",
    "Monitor",
    "Printer",
    "Computer",
    "Insurance",
    "Toner",
    "Office Supplies",
]
cat_vars1 = [
    "Customer_engagement_length",
    "Language_group",
    "Repurchase Method",
    "Last Transaction Channel",
    "Number of Employees",
    "Service Level",
    "Do No Disturb",
    "Email Available",
]
cat_vars2 = [
    "Desk",
    "Executive Chair",
    "Standard Chair",
    "Monitor",
    "Printer",
    "Computer",
    "Insurance",
    "Toner",
    "Office Supplies",
]

# Categorical variables plots

fig, ax = plt.subplots(2, 4, figsize=(18, 10), squeeze=False, sharey=True)
ax = ax.ravel()
for i in range(8):
    sns.stripplot(
        x=cat_vars1[i], y="Campaign Period Sales", data=df, ax=ax[i], edgecolor="k"
    )
    ax[i].set_xlabel(cat_vars1[i], fontsize=14)
    ax[i].set_ylabel("Campaign Period sales", fontsize=14)
    if len(df[cat_vars1[i]].unique()) > 3:
        ax[i].set_xticklabels(labels=df[cat_vars1[i]].unique(), rotation=90)
plt.tight_layout(pad=1.5)
plt.show()

# Numerical variable plots

fig, ax = plt.subplots(2, 3, figsize=(18, 10), squeeze=False, sharey=True)
ax = ax.ravel()
for i in range(6):
    sns.scatterplot(
        x=num_vars[i], y="Campaign Period Sales", data=df, ax=ax[i], edgecolor="k"
    )
    ax[i].set_xlabel(num_vars[i], fontsize=14)
    ax[i].set_ylabel("Campaign Period sales", fontsize=14)
plt.tight_layout(pad=1.5)
plt.show()

# Violin plots to understand class separation by variables

fig, ax = plt.subplots(2, 3, figsize=(18, 10), squeeze=False)
ax = ax.ravel()
for i in range(6):
    sns.violinplot(x="Buy", y=num_vars[i], data=df, ax=ax[i])
    ax[i].set_xlabel("Buy/No-buy", fontsize=14)
    ax[i].set_ylabel(num_vars[i], fontsize=14)
plt.tight_layout(pad=1.5)
plt.show()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------")  # 30個
