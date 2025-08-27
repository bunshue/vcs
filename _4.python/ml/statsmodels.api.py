"""
statsmodels.api

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


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

# 多圖組合
# jointplot兩變量圖

import statsmodels.api as sm  # 为统计计算提供了一个补充，包括描述性统计和统计模型的估计


sns.set(style="darkgrid")
data = sm.datasets.ccard.load_pandas().data
sns.jointplot(
    x="AVGEXP", y="AGE", data=data, kind="reg", xlim=(0, 1000), ylim=(0, 50), color="m"
)
show()

print("------------------------------------------------------------")  # 60個

import statsmodels.api as sm

# pairplot多變量圖
data = sm.datasets.ccard.load_pandas().data
sns.pairplot(data, vars=["AGE", "INCOME", "INCOMESQ", "OWNRENT"])

show()

print("------------------------------------------------------------")  # 60個

# catplot兩變量關係圖
data = sm.datasets.fair.load_pandas().data
sns.catplot(x="occupation", y="affairs", hue="religious", data=data)

show()

print("------------------------------------------------------------")  # 60個

print("簡單隨機抽樣")

import statsmodels.api as sm

data = sm.datasets.anes96.load_pandas().data
df = data.sample(50)
print(df.head())

print("系統抽樣")

index_list = [i for i in range(len(data)) if i % 10 == 0]
df = data.iloc[index_list]
print(df.head())

print("分層抽樣")


def typicalSampling(grp, typicalFracDict):
    name = grp.name
    frac = typicalFracDict[name]
    return grp.sample(frac=frac)


typicalFracDict = {
    0.0: 0.35,
    1.0: 0.5,
}
df = data.groupby("vote").apply(typicalSampling, typicalFracDict)
print(df.head())

print("整羣抽樣")
unique = np.unique(data["income"])
sample = random.sample(list(unique), 2)
df = pd.DataFrame()
for label in sample:
    tmp = data[data["income"] == label]
    df = pd.concat([df, tmp])
print(df.head())

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
