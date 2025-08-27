"""
XXXXXXX

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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

# Import neccessay libraries

sns.set_style("darkgrid")

import warnings

warnings.filterwarnings("ignore")

train = pd.read_csv("D:/_git/vcs/_big_files/widsdatathon2021/TrainingWiDS2021.csv")
test = pd.read_csv("D:/_git/vcs/_big_files/widsdatathon2021/UnlabeledWiDS2021.csv")
cc = train.shape, test.shape
print(cc)

# ((130157, 181), (10234, 180))

# Lets have a quick look at train
cc = train.head()
print(cc)

cc = train.info()
print(cc)

# Descriptive Statistics

# Start with descriptive statistics on the data
cc = train.describe().T
print(cc)

# Univariate Insights

# CATEGORY: IDENTIFIERS

print(train.shape)
print(train.encounter_id.nunique())
print(train.hospital_id.nunique())

# CATEGORY: TARGET VARIABLE

sns.catplot(x="diabetes_mellitus", kind="count", data=train)
plt.show()

# Imbalance Ratio
cc = train.diabetes_mellitus.value_counts(normalize=True)
print(cc)

# CATEGORY: DEMOGRAPHICS

# Function to plot distribution of variable and boxplot


def plot_dist_box(df, colname):
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

    # Plot distributions
    plot00 = sns.distplot(df[colname], ax=axes[0][0])
    axes[0][0].set_title("Distribution of {name}".format(name=colname))

    plot01 = sns.distplot(
        df[df["diabetes_mellitus"] == False][colname],
        ax=axes[0][1],
        label="Non Diabetes",
    )
    sns.distplot(
        df[df.diabetes_mellitus == True][colname],
        ax=axes[0][1],
        color="red",
        label="Diabetes",
    )
    axes[0][1].set_title("Distribution of {name}".format(name=colname))
    plot01.axes.legend()

    # Boxplots
    plot10 = sns.boxplot(df[colname], ax=axes[1][0])
    plot11 = sns.boxplot(x="diabetes_mellitus", y=colname, data=df, ax=axes[1][1])
    plt.xticks(ticks=[0, 1], labels=["Non-Diabetes", "Diabetes"])
    axes[1][1].set_xlabel("Category")
    plt.show()


# Variable: bmi

plot_dist_box(train, "bmi")
plt.show()

# Note :- Distribution is almost symmetric with most data between 24-32. There are some outliers present on higher end.

# Variable: Age

plot_dist_box(train, "age")
plt.show()

# Note :- Age Distribution has deviation from normal distribution. It is left skewed (Negative skewness) distribution with most data between 50-75 years. There are some outliers present on lower end (Age=0)

# Lets verify this for age variable
print(train.age.mean())
print(train.age.median())
print(train.age.mode()[0])

# lets check skewness value rather than just estimating from figure
print("Skewness= ", train["age"].skew())

# Skewness=  -0.608436408837161

# Since skewness value is between -1 and -0.5, the data (age) is moderately skewed.

# Kurtosis

# check kurtosis value
print("Kurtosis= ", train["age"].kurt())

# Kurtosis=  -0.21349534669057668

# CATEGORY: APACHE COVARIATE

# Variable: albumin_apache

sns.catplot(y="bilirubin_apache", x="diabetes_mellitus", data=train)
plt.show()

plot_dist_box(train, "bilirubin_apache")
plt.show()

# CATEGORY: APACHE COMORBIDITY

# Variable: hepatic_failure, aids, lymphoma

cc = train.groupby(["hepatic_failure", "diabetes_mellitus"]).size()
print(cc)

cc = train.groupby(["aids", "diabetes_mellitus"]).size()
print(cc)

cc = train.groupby(["lymphoma", "diabetes_mellitus"]).size()
print(cc)

# CATEGORY: VITALS
# Variable: h1_spo2_max

sns.catplot(y="h1_spo2_max", x="diabetes_mellitus", data=train)
plt.show()

plot_dist_box(train, "h1_spo2_max")
plt.show()

# Multivariate Insights

# Pairplot with hue

# Pairplot
# Since we have very large number of features, lets take few features only to understand the workflow
plt.figure(figsize=(6, 5))
sns.pairplot(
    train[
        [
            "height",
            "bmi",
            "apache_2_diagnosis",
            "apache_3j_diagnosis",
            "diabetes_mellitus",
        ]
    ],
    hue="diabetes_mellitus",
)
plt.show()

# Sampling 2000 data points from train
sampletrain = train.sample(2000)

# plotting on sample of dataset coz data is huge

plt.figure(figsize=(5, 4))
sns.pairplot(
    sampletrain[
        [
            "height",
            "bmi",
            "apache_2_diagnosis",
            "apache_3j_diagnosis",
            "diabetes_mellitus",
        ]
    ],
    hue="diabetes_mellitus",
)
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


print("------------------------------")  # 30個
