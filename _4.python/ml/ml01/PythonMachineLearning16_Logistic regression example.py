"""
Logistic regression example

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

# Logistic regression example

names = "response age sex on_thyroxine query_on_thyroxine antithyroid_medication thyroid_surgery query_hypothyroid query_hyperthyroid pregnant \
sick tumor lithium goitre TSH_measured TSH T3_measured \
T3 TT4_measured TT4 T4U_measured T4U FTI_measured FTI TBG_measured TBG"

names = names.split(" ")

#!wget https://raw.githubusercontent.com/tirthajyoti/Machine-Learning-with-Python/master/Datasets/hypothyroid.csv

#!mkdir Data
#!mv hypothyroid.csv Data/

df = pd.read_csv("data/hypothyroid.csv", index_col=False, names=names, na_values=["?"])

df.head()

to_drop = []
for c in df.columns:
    if "measured" in c or "query" in c:
        to_drop.append(c)

to_drop

to_drop.append("TBG")

df.drop(to_drop, axis=1, inplace=True)

df.head()

df.describe().T

# The df.isna() method gives back a full DataFrame with Boolean values - True for data present, False for missing data. We can use sum() on that DataFrame to see and calculate the number of missing values per column.

df.isna().sum()

# We can use df.dropna() method to drop those missing rows

df.dropna(inplace=True)

df.shape

# (2000, 16)

# Creating a transformation function to convert + or - responses to 1 and 0


def class_convert(response):
    if response == "hypothyroid":
        return 1
    else:
        return 0


df["response"] = df["response"].apply(class_convert)

df.head()

df.columns

# Exploratory data analysis

for var in ["age", "TSH", "T3", "TT4", "T4U", "FTI"]:
    sns.boxplot(x="response", y=var, data=df)
    plt.show()

sns.pairplot(
    data=df[df.columns[1:]],
    diag_kws={"edgecolor": "k", "bins": 25},
    plot_kws={"edgecolor": "k"},
)
plt.show()

# Create dummy variables for the categorical variables

df_dummies = pd.get_dummies(data=df)

df_dummies.shape

# (2000, 25)

df_dummies.sample(10)

# Test/train split

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    df_dummies.drop("response", axis=1),
    df_dummies["response"],
    test_size=0.30,
    random_state=42,
)

print("Training set shape", X_train.shape)
print("Test set shape", X_test.shape)

# Training set shape (1400, 24)
# Test set shape (600, 24)

# Using LogisticRegression estimator from Scikit-learn

# We are using the L2 regularization by default

from sklearn.linear_model import LogisticRegression

clf1 = LogisticRegression(penalty="l2", solver="newton-cg")

clf1.fit(X_train, y_train)

# Intercept, coefficients, and score

clf1.intercept_

# array([2.28510517])

clf1.coef_

clf1.score(X_test, y_test)

# 0.9816666666666667

# For LogisticRegression estimator, there is a special predict_proba method which computes the raw probability values

prob_threshold = 0.5

prob_df = pd.DataFrame(
    clf1.predict_proba(X_test[:10]), columns=["Prob of NO", "Prob of YES"]
)
prob_df["Decision"] = (prob_df["Prob of YES"] > prob_threshold).apply(int)
prob_df

y_test[:10]

# Classification report, and confusion matrix

from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(y_test, clf1.predict(X_test)))

pd.DataFrame(
    confusion_matrix(y_test, clf1.predict(X_test)),
    columns=["Predict-YES", "Predict-NO"],
    index=["YES", "NO"],
)

# Using statsmodels library

import statsmodels.formula.api as smf
import statsmodels.api as sm

df_dummies.columns

# Create a 'formula' in the same style as in R language
formula = "response ~ " + "+".join(df_dummies.columns[1:])
formula
"response ~ age+TSH+T3+TT4+T4U+FTI+sex_F+sex_M+on_thyroxine_f+on_thyroxine_t+antithyroid_medication_f+antithyroid_medication_t+thyroid_surgery_f+thyroid_surgery_t+pregnant_f+pregnant_t+sick_f+sick_t+tumor_f+tumor_t+lithium_f+lithium_t+goitre_f+goitre_t"

# Fit a GLM (Generalized Linear model) with this formula and choosing Binomial as the family of function

model = smf.glm(formula=formula, data=df_dummies, family=sm.families.Binomial())

result = model.fit()

# summary method shows a R-style table with all kind of statistical information

print(result.summary())

result.predict(X_test[:10])

# To create binary predictions, you have to apply a threshold probability and convert the booleans into integers

y_pred = (result.predict(X_test) > prob_threshold).apply(int)

print(classification_report(y_test, y_pred))

pd.DataFrame(
    confusion_matrix(y_test, y_pred),
    columns=["Predict-YES", "Predict-NO"],
    index=["YES", "NO"],
)

# A smaller model with only first few variables

# We saw that majority of variables in the logistic regression model has p-values very high and therefore they are not statistically significant. We create another smaller model removing those variables.

formula = "response ~ " + "+".join(df_dummies.columns[1:7])
formula

"response ~ age+TSH+T3+TT4+T4U+FTI"

model = smf.glm(formula=formula, data=df_dummies, family=sm.families.Binomial())

result = model.fit()

print(result.summary())

y_pred = (result.predict(X_test) > prob_threshold).apply(int)
print(classification_report(y_pred, y_test))

pd.DataFrame(
    confusion_matrix(y_test, y_pred),
    columns=["Predict-YES", "Predict-NO"],
    index=["YES", "NO"],
)

# How do the probabilities compare between Scikit-learn and Statsmodels predictions?

sklearn_prob = clf1.predict_proba(X_test)[..., 1][:10]
statsmodels_prob = result.predict(X_test[:10])

prob_comp_df = pd.DataFrame(
    data={
        "Scikit-learn Prob": list(sklearn_prob),
        "Statsmodels Prob": list(statsmodels_prob),
    }
)
prob_comp_df

# Coefficient interpretation


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
