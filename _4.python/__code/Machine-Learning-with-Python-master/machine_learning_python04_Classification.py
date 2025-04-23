"""
machine_learning_python04_Classification

Classification algorithms
Logistic regression with Titanic data
Naive bayes
Support vector machine with breast cancer data
Skewed logistic regression (imbalanced class divisions)
k-Nearest neighbor classification
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

# Logistic_Regression_Classification
# Logistic Regression with Kaggle Titanic data set

train = pd.read_csv("Datasets/titanic_train.csv")  # Training set is already available
cc = train.head()
print(cc)

# Check basic info about the data set including missing value

cc = train.info()
print(cc)

d = train.describe()
print(d)

# Exploratory analysis and plots

dT = d.T
dT.plot.bar(y="count")
plt.title("Bar plot of the count of numeric features", fontsize=17)
show()

# Check the relative size of survived and not-survived

sns.set_style("whitegrid")
sns.countplot(x="Survived", data=train, palette="RdBu_r")
show()

# Is there a pattern for the survivability based on sex?
# It looks like more female survived than males!

sns.set_style("whitegrid")
sns.countplot(x="Survived", hue="Sex", data=train, palette="RdBu_r")
show()

# What about any pattern related to passenger class?
# It looks like disproportionately large number of 3rd class passengers died!

sns.set_style("whitegrid")
sns.countplot(x="Survived", hue="Pclass", data=train, palette="rainbow")
show()

# Following code extracts and plots the fraction of passenger count that survived, by each class

f_class_survived = train.groupby("Pclass")["Survived"].mean()
f_class_survived = pd.DataFrame(f_class_survived)
f_class_survived
f_class_survived.plot.bar(y="Survived")
plt.title("Fraction of passengers survived by class", fontsize=17)
show()

# What about any pattern related to having sibling and spouse?
# It looks like there is a weak trend that chance of survibility increased if there were more number of sibling or spouse

sns.set_style("whitegrid")
sns.countplot(x="Survived", hue="SibSp", data=train, palette="rainbow")
show()

# How does the overall age distribution look like?

plt.xlabel("Age of the passengers", fontsize=18)
plt.ylabel("Count", fontsize=18)
plt.title("Age histogram of the passengers", fontsize=22)
train["Age"].hist(bins=30, color="darkred", alpha=0.7, figsize=(10, 6))
show()

# How does the age distribution look like across passenger class?
# It looks like that the average age is different for three classes and it generally decreases from 1st class to 3rd class.

plt.figure(figsize=(12, 10))
plt.xlabel("Passenger Class", fontsize=18)
plt.ylabel("Age", fontsize=18)
sns.boxplot(x="Pclass", y="Age", data=train, palette="winter")
show()

f_class_Age = train.groupby("Pclass")["Age"].mean()
f_class_Age = pd.DataFrame(f_class_Age)
f_class_Age.plot.bar(y="Age")
plt.title("Average age of passengers by class", fontsize=17)
plt.ylabel("Age (years)", fontsize=17)
plt.xlabel("Passenger class", fontsize=17)
show()

# Data wrangling (impute and drop)
#    Impute age (by averaging)
#    Drop unncessary features
#    Convert categorical features to dummy variables

# Define a function to impute (fill-up missing values) age feature

a = list(f_class_Age["Age"])


def impute_age(cols):
    Age = cols[0]
    Pclass = cols[1]

    if pd.isnull(Age):
        if Pclass == 1:
            return a[0]

        elif Pclass == 2:
            return a[1]

        else:
            return a[2]

    else:
        return Age


# Apply the above-defined function and plot the count of numeric features

train["Age"] = train[["Age", "Pclass"]].apply(impute_age, axis=1)
d = train.describe()
dT = d.T
dT.plot.bar(y="count")
plt.title("Bar plot of the count of numeric features", fontsize=17)
show()

# Drop the 'Cabin' feature and any other null value

train.drop("Cabin", axis=1, inplace=True)
train.dropna(inplace=True)
cc = train.head()
print(cc)

# Drop other unnecessary features like 'PassengerId', 'Name', 'Ticket'

train.drop(["PassengerId", "Name", "Ticket"], axis=1, inplace=True)
cc = train.head()
print(cc)

# Convert categorial feature like 'Sex' and 'Embarked' to dummy variables

# Use pandas 'get_dummies()' function

sex = pd.get_dummies(train["Sex"], drop_first=True)
embark = pd.get_dummies(train["Embarked"], drop_first=True)

# Now drop the 'Sex' and 'Embarked' columns and concatenate the new dummy variables

train.drop(["Sex", "Embarked"], axis=1, inplace=True)
train = pd.concat([train, sex, embark], axis=1)
cc = train.head()
print(cc)

# This data set is now ready for logistic regression analysis!

# Logistic Regression model fit and prediction

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    train.drop("Survived", axis=1), train["Survived"], test_size=0.30, random_state=111
)

# F1-score as a fucntion of regularization (penalty) parameter

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

nsimu = 201
penalty = [0] * nsimu
logmodel = [0] * nsimu
predictions = [0] * nsimu
class_report = [0] * nsimu
f1 = [0] * nsimu
for i in range(1, nsimu):
    logmodel[i] = LogisticRegression(C=i / 1000, tol=1e-4, max_iter=100, n_jobs=4)
    logmodel[i].fit(X_train, y_train)
    predictions[i] = logmodel[i].predict(X_test)
    class_report[i] = classification_report(y_test, predictions[i])
    l = class_report[i].split()
    f1[i] = l[len(l) - 2]
    penalty[i] = 1000 / i

plt.scatter(penalty[1 : len(penalty) - 2], f1[1 : len(f1) - 2])
plt.title("F1-score vs. regularization parameter", fontsize=20)
plt.xlabel("Penalty parameter", fontsize=17)
plt.ylabel("F1-score on test data", fontsize=17)
plt.show()

# F1-score as a function of test set size (fraction)

nsimu = 101
class_report = [0] * nsimu
f1 = [0] * nsimu
test_fraction = [0] * nsimu
for i in range(1, nsimu):
    X_train, X_test, y_train, y_test = train_test_split(
        train.drop("Survived", axis=1),
        train["Survived"],
        test_size=0.1 + (i - 1) * 0.007,
        random_state=111,
    )
    logmodel = LogisticRegression(C=1, tol=1e-4, max_iter=1000, n_jobs=4)
    logmodel.fit(X_train, y_train)
    predictions = logmodel.predict(X_test)
    class_report[i] = classification_report(y_test, predictions)
    l = class_report[i].split()
    f1[i] = l[len(l) - 2]
    test_fraction[i] = 0.1 + (i - 1) * 0.007

plt.plot(test_fraction[1 : len(test_fraction) - 2], f1[1 : len(f1) - 2])
plt.title("F1-score vs. test set size (fraction)", fontsize=20)
plt.xlabel("Test set size (fraction)", fontsize=17)
plt.ylabel("F1-score on test data", fontsize=17)
plt.show()

# F1-score as a function of random seed of test/train split

nsimu = 101
class_report = [0] * nsimu
f1 = [0] * nsimu
random_init = [0] * nsimu
for i in range(1, nsimu):
    X_train, X_test, y_train, y_test = train_test_split(
        train.drop("Survived", axis=1),
        train["Survived"],
        test_size=0.3,
        random_state=i + 100,
    )
    logmodel = LogisticRegression(C=1, tol=1e-5, max_iter=1000, n_jobs=4)
    logmodel.fit(X_train, y_train)
    predictions = logmodel.predict(X_test)
    class_report[i] = classification_report(y_test, predictions)
    l = class_report[i].split()
    f1[i] = l[len(l) - 2]
    random_init[i] = i + 100

plt.plot(random_init[1 : len(random_init) - 2], f1[1 : len(f1) - 2])
plt.title("F1-score vs. random initialization seed", fontsize=20)
plt.xlabel("Random initialization seed", fontsize=17)
plt.ylabel("F1-score on test data", fontsize=17)
plt.show()

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
