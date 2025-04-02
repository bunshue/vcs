"""
association_rule_market_basket_analysis

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

import plotly.express as px

# import apyori

from apyori import apriori

data = pd.read_csv("data/Groceries_dataset.csv")
print("Data Dimension:", data.shape)
cc = data.head()
print(cc)

cc = data.isnull().any()
print(cc)

print("Total number of unique products are:", len(data["itemDescription"].unique()))

# Total number of unique products are: 167

# Top 10 frequently sold products
print("Top 10 frequently sold products(Tabular Representation)")
x = data["itemDescription"].value_counts().sort_values(ascending=False)[:10]
print(x)

fig = px.bar(x=x.index, y=x.values)
fig.update_layout(
    title_text="Top 10 frequently sold products (Graphical Representation)",
    xaxis_title="Products",
    yaxis_title="Count",
)
fig.show()

# Exploring Higher sales by time of the year:
data["Year"] = data["Date"].str.split("-").str[-1]
data["Month-Year"] = (
    data["Date"].str.split("-").str[1] + "-" + data["Date"].str.split("-").str[-1]
)
cc = data.head()
print(cc)

fig1 = px.bar(
    data["Month-Year"].value_counts(ascending=False),
    orientation="v",
    color=data["Month-Year"].value_counts(ascending=False),
    labels={"value": "Count", "index": "Date", "color": "Meter"},
)

fig1.update_layout(title_text="Exploring higher sales by the date")

fig1.show()

"""
Observations
- Milk is purchased the highest followed by vegetables
- The most purchases are during August/Sepetember, while February/March has the leats demands
"""

products = data["itemDescription"].unique()

# one hot encoding the products:

dummy = pd.get_dummies(data["itemDescription"])
data.drop(["itemDescription"], inplace=True, axis=1)

data = data.join(dummy)

cc = data.head()
print(cc)

# Transaction: If a customer bought multiple products in one day, it will be considered as 1 transaction:

data1 = data.groupby(["Member_number", "Date"])[products[:]].sum()
data1 = data1.reset_index()[products]

print("New Dimension", data1.shape)
cc = data1.head()
print(cc)

# Replacing all non-zero values with the name of the product:


def product_names(x):
    for product in products:
        if x[product] > 0:
            x[product] = product
    return x


data1 = data1.apply(product_names, axis=1)
cc = data1.head()
print(cc)

print("Total Number of Transactions:", len(data1))

# Total Number of Transactions: 14963

# Removing Zeros, Extracting the list of items bought per customer

x = data1.values
x = [sub[~(sub == 0)].tolist() for sub in x if sub[sub != 0].tolist()]
transactions = x
cc = transactions[0:10]
print(cc)

rules = apriori(
    transactions,
    min_support=0.00030,
    min_confidence=0.05,
    min_lift=3,
    max_length=2,
    target="rules",
)
association_results = list(rules)
print(association_results[0])

# RelationRecord(items=frozenset({'liver loaf', 'fruit/vegetable juice'}), support=0.00040098910646260775, ordered_statistics=[OrderedStatistic(items_base=frozenset({'liver loaf'}), items_add=frozenset({'fruit/vegetable juice'}), confidence=0.12, lift=3.5276227897838903)])

for item in association_results:
    pair = item[0]
    items = [x for x in pair]

    print("Rule : ", items[0], " -> " + items[1])
    print("Support : ", str(item[1]))
    print("Confidence : ", str(item[2][0][2]))
    print("Lift : ", str(item[2][0][3]))

    print("=============================")


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
