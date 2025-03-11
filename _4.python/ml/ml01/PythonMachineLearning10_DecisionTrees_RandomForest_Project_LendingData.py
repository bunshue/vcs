"""
DecisionTrees_RandomForest_Project_LendingData

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
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from matplotlib.colors import ListedColormap

from sklearn import tree


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Random Forest applied to LendingClub data set
"""
    credit.policy: 1 if the customer meets the credit underwriting criteria of LendingClub.com, and 0 otherwise.
    purpose: The purpose of the loan (takes values "credit_card", "debt_consolidation", "educational", "major_purchase", "small_business", and "all_other").
    int.rate: The interest rate of the loan, as a proportion (a rate of 11% would be stored as 0.11). Borrowers judged by LendingClub.com to be more risky are assigned higher interest rates.
    installment: The monthly installments owed by the borrower if the loan is funded.
    log.annual.inc: The natural log of the self-reported annual income of the borrower.
    dti: The debt-to-income ratio of the borrower (amount of debt divided by annual income).
    fico: The FICO credit score of the borrower.
    days.with.cr.line: The number of days the borrower has had a credit line.
    revol.bal: The borrower's revolving balance (amount unpaid at the end of the credit card billing cycle).
    revol.util: The borrower's revolving line utilization rate (the amount of the credit line used relative to total credit available).
    inq.last.6mths: The borrower's number of inquiries by creditors in the last 6 months.
    delinq.2yrs: The number of times the borrower had been 30+ days past due on a payment in the past 2 years.
    pub.rec: The borrower's number of derogatory public records (bankruptcy filings, tax liens, or judgments).
    not.fully.paid: The quantity of interest for classification - whether the borrower paid back the money in full or not
"""

df = pd.read_csv("data/loan_data.csv")

df.info()

df.describe()

df.head()

print(
    "Follwoing is a breakup of credit approval status. 1 means approved credit, 0 means not approved."
)
print(df["credit.policy"].value_counts())

# Exploratory Data Analysis

df[df["credit.policy"] == 1]["fico"].plot.hist(
    bins=30, alpha=0.5, color="blue", label="Credit.Policy=1"
)
df[df["credit.policy"] == 0]["fico"].plot.hist(
    bins=30, alpha=0.5, color="red", label="Credit.Policy=0"
)
plt.legend(fontsize=15)
plt.title(
    "Histogram of FICO score by approved or disapproved credit policies", fontsize=16
)
plt.xlabel("FICO score", fontsize=14)

plt.show()

# Presence or absence of statistical difference of various factors between credit approval status

sns.boxplot(x=df["credit.policy"], y=df["int.rate"])
plt.title("Interest rate varies between risky and non-risky borrowers", fontsize=15)
plt.xlabel("Credit policy", fontsize=15)
plt.ylabel("Interest rate", fontsize=15)

plt.show()

sns.boxplot(x=df["credit.policy"], y=df["log.annual.inc"])
plt.title(
    "Income level does not make a big difference in credit approval odds", fontsize=15
)
plt.xlabel("Credit policy", fontsize=15)
plt.ylabel("Log. annual income", fontsize=15)

plt.show()

sns.boxplot(x=df["credit.policy"], y=df["days.with.cr.line"])
plt.title(
    "Credit-approved users have a slightly higher days with credit line", fontsize=15
)
plt.xlabel("Credit policy", fontsize=15)
plt.ylabel("Days with credit line", fontsize=15)

plt.show()

sns.boxplot(x=df["credit.policy"], y=df["dti"])
plt.title(
    "Debt-to-income level does not make a big difference in credit approval odds",
    fontsize=15,
)
plt.xlabel("Credit policy", fontsize=15)
plt.ylabel("Debt-to-income ratio", fontsize=15)
plt.show()

# Countplot of loans by purpose, with the color hue defined by not.fully.paid

plt.figure(figsize=(10, 6))
sns.countplot(x="purpose", hue="not.fully.paid", data=df, palette="Set1")
plt.title("Bar chart of loan purpose colored by not fully paid status", fontsize=17)
plt.xlabel("Purpose", fontsize=15)

plt.show()

# Trend between FICO score and interest rate

sns.jointplot(x="fico", y="int.rate", data=df, color="purple", size=12)

plt.show()

# lmplot to see if the trend differed between not.fully.paid and credit.policy

plt.figure(figsize=(14, 7))
sns.lmplot(
    y="int.rate",
    x="fico",
    data=df,
    hue="credit.policy",
    col="not.fully.paid",
    palette="Set1",
)

plt.show()

# Setting up the Data
# Categorical Features

df_final = pd.get_dummies(df, ["purpose"], drop_first=True)

df_final.head()

from sklearn.model_selection import train_test_split

X = df_final.drop("not.fully.paid", axis=1)
y = df_final["not.fully.paid"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

X.head()

# Training a Decision Tree Model

from sklearn.tree import DecisionTreeClassifier

# Create an instance of DecisionTreeClassifier() called dtree and fit it to the training data.

dtree = DecisionTreeClassifier(criterion="gini", max_depth=None)

dtree.fit(X_train, y_train)
"""
DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,
            max_features=None, max_leaf_nodes=None,
            min_impurity_split=1e-07, min_samples_leaf=1,
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            presort=False, random_state=None, splitter='best')
"""
# Predictions and Evaluation of Decision Tree

predictions = dtree.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(y_test, predictions))

cm = confusion_matrix(y_test, predictions)
print(cm)
print("Accuracy of prediction:", round((cm[0, 0] + cm[1, 1]) / cm.sum(), 3))

# Training the Random Forest model

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=600)

rfc.fit(X_train, y_train)
"""
RandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini',
            max_depth=None, max_features='auto', max_leaf_nodes=None,
            min_impurity_split=1e-07, min_samples_leaf=1,
            min_samples_split=2, min_weight_fraction_leaf=0.0,
            n_estimators=600, n_jobs=1, oob_score=False, random_state=None,
            verbose=0, warm_start=False)
"""
# Predictions and Evaluation

rfc_pred = rfc.predict(X_test)

cr = classification_report(y_test, predictions)

print(cr)

# Show the Confusion Matrix for the predictions.

cm = confusion_matrix(y_test, rfc_pred)
print(cm)

# Running a loop with increasing number of trees in the random forest and checking accuracy of confusion matrix

# Criterion 'gini' or 'entropy'

nsimu = 21
accuracy = [0] * nsimu
ntree = [0] * nsimu
for i in range(1, nsimu):
    rfc = RandomForestClassifier(
        n_estimators=i * 5, min_samples_split=10, max_depth=None, criterion="gini"
    )
    rfc.fit(X_train, y_train)
    rfc_pred = rfc.predict(X_test)
    cm = confusion_matrix(y_test, rfc_pred)
    accuracy[i] = (cm[0, 0] + cm[1, 1]) / cm.sum()
    ntree[i] = i * 5

plt.figure(figsize=(10, 6))
plt.scatter(x=ntree[1:nsimu], y=accuracy[1:nsimu], s=60, c="red")
plt.title(
    "Number of trees in the Random Forest vs. prediction accuracy (criterion: 'gini')",
    fontsize=18,
)
plt.xlabel("Number of trees", fontsize=15)
plt.ylabel("Prediction accuracy from confusion matrix", fontsize=15)

plt.show()

nsimu = 21
accuracy = [0] * nsimu
ntree = [0] * nsimu
for i in range(1, nsimu):
    rfc = RandomForestClassifier(
        n_estimators=i * 5, min_samples_split=10, max_depth=None, criterion="entropy"
    )
    rfc.fit(X_train, y_train)
    rfc_pred = rfc.predict(X_test)
    cm = confusion_matrix(y_test, rfc_pred)
    accuracy[i] = (cm[0, 0] + cm[1, 1]) / cm.sum()
    ntree[i] = i * 5

plt.figure(figsize=(10, 6))
plt.scatter(x=ntree[1:nsimu], y=accuracy[1:nsimu], s=60, c="red")
plt.title(
    "Number of trees in the Random Forest vs. prediction accuracy (criterion: 'entropy')",
    fontsize=18,
)
plt.xlabel("Number of trees", fontsize=15)
plt.ylabel("Prediction accuracy from confusion matrix", fontsize=15)

plt.show()

# Fixing max tree depth

nsimu = 21
accuracy = [0] * nsimu
ntree = [0] * nsimu
for i in range(1, nsimu):
    rfc = RandomForestClassifier(
        n_estimators=i * 5, min_samples_split=10, max_depth=None, criterion="gini"
    )
    rfc.fit(X_train, y_train)
    rfc_pred = rfc.predict(X_test)
    cm = confusion_matrix(y_test, rfc_pred)
    accuracy[i] = (cm[0, 0] + cm[1, 1]) / cm.sum()
    ntree[i] = i * 5

plt.figure(figsize=(10, 6))
plt.scatter(x=ntree[1:nsimu], y=accuracy[1:nsimu], s=60, c="red")
plt.title(
    "Number of trees in the Random Forest vs. prediction accuracy (max depth: None)",
    fontsize=18,
)
plt.xlabel("Number of trees", fontsize=15)
plt.ylabel("Prediction accuracy from confusion matrix", fontsize=15)

plt.show()

nsimu = 21
accuracy = [0] * nsimu
ntree = [0] * nsimu
for i in range(1, nsimu):
    rfc = RandomForestClassifier(
        n_estimators=i * 5, min_samples_split=10, max_depth=5, criterion="gini"
    )
    rfc.fit(X_train, y_train)
    rfc_pred = rfc.predict(X_test)
    cm = confusion_matrix(y_test, rfc_pred)
    accuracy[i] = (cm[0, 0] + cm[1, 1]) / cm.sum()
    ntree[i] = i * 5

plt.figure(figsize=(10, 6))
plt.scatter(x=ntree[1:nsimu], y=accuracy[1:nsimu], s=60, c="red")
plt.title(
    "Number of trees in the Random Forest vs. prediction accuracy (max depth: 5)",
    fontsize=18,
)
plt.xlabel("Number of trees", fontsize=15)
plt.ylabel("Prediction accuracy from confusion matrix", fontsize=15)

plt.show()

# Minimum sample split criteria

nsimu = 21
accuracy = [0] * nsimu
ntree = [0] * nsimu
for i in range(1, nsimu):
    rfc = RandomForestClassifier(
        n_estimators=i * 5, min_samples_split=2, max_depth=None, criterion="gini"
    )
    rfc.fit(X_train, y_train)
    rfc_pred = rfc.predict(X_test)
    cm = confusion_matrix(y_test, rfc_pred)
    accuracy[i] = (cm[0, 0] + cm[1, 1]) / cm.sum()
    ntree[i] = i * 5

plt.figure(figsize=(10, 6))
plt.scatter(x=ntree[1:nsimu], y=accuracy[1:nsimu], s=60, c="red")
plt.title(
    "Number of trees in the Random Forest vs. prediction accuracy (minimum sample split: 2)",
    fontsize=18,
)
plt.xlabel("Number of trees", fontsize=15)
plt.ylabel("Prediction accuracy from confusion matrix", fontsize=15)

plt.show()

nsimu = 21
accuracy = [0] * nsimu
ntree = [0] * nsimu
for i in range(1, nsimu):
    rfc = RandomForestClassifier(
        n_estimators=i * 5, min_samples_split=20, max_depth=None, criterion="gini"
    )
    rfc.fit(X_train, y_train)
    rfc_pred = rfc.predict(X_test)
    cm = confusion_matrix(y_test, rfc_pred)
    accuracy[i] = (cm[0, 0] + cm[1, 1]) / cm.sum()
    ntree[i] = i * 5

plt.figure(figsize=(10, 6))
plt.scatter(x=ntree[1:nsimu], y=accuracy[1:nsimu], s=60, c="red")
plt.title(
    "Number of trees in the Random Forest vs. prediction accuracy (minimum sample split: 20)",
    fontsize=18,
)
plt.xlabel("Number of trees", fontsize=15)
plt.ylabel("Prediction accuracy from confusion matrix", fontsize=15)

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
