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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Product Analytics


df = pd.read_excel(io="data/Online Retail.xlsx", sheet_name="Online Retail")

# df.shape

# df.head()

# 2. Product Analytics
# - Quantity Distribution

ax = df["Quantity"].plot.box(showfliers=False, grid=True, figsize=(10, 7))

ax.set_ylabel("Order Quantity")
ax.set_title("Quantity Distribution")

plt.suptitle("")
plt.show()

cc = pd.DataFrame(df["Quantity"].describe())
print(cc)

cc = df.loc[df["Quantity"] > 0].shape
print(cc)

cc = df.shape
print(cc)

cc = df = df.loc[df["Quantity"] > 0]
print(cc)

# - Time-series Number of Orders

monthly_orders_df = df.set_index("InvoiceDate")["InvoiceNo"].resample("M").nunique()

cc = monthly_orders_df
print(cc)

ax = pd.DataFrame(monthly_orders_df.values).plot(
    grid=True, figsize=(10, 7), legend=False
)

ax.set_xlabel("date")
ax.set_ylabel("number of orders/invoices")
ax.set_title("Total Number of Orders Over Time")

plt.xticks(
    range(len(monthly_orders_df.index)),
    [x.strftime("%m.%Y") for x in monthly_orders_df.index],
    rotation=45,
)

plt.show()

invoice_dates = df.loc[df["InvoiceDate"] >= "2011-12-01", "InvoiceDate"]

print("Min date: %s\nMax date: %s" % (invoice_dates.min(), invoice_dates.max()))

cc = df.loc[df["InvoiceDate"] < "2011-12-01"].shape
print(cc)

# (506150, 8)

cc = df.shape
print(cc)

# (531285, 8)

df = df.loc[df["InvoiceDate"] < "2011-12-01"]

monthly_orders_df = df.set_index("InvoiceDate")["InvoiceNo"].resample("M").nunique()

cc = monthly_orders_df
print(cc)

ax = pd.DataFrame(monthly_orders_df.values).plot(
    grid=True, figsize=(10, 7), legend=False
)

ax.set_xlabel("date")
ax.set_ylabel("number of orders")
ax.set_title("Total Number of Orders Over Time")

ax.set_ylim([0, max(monthly_orders_df.values) + 500])

plt.xticks(
    range(len(monthly_orders_df.index)),
    [x.strftime("%m.%Y") for x in monthly_orders_df.index],
    rotation=45,
)

plt.show()

# - Time-series Revenue

df["Sales"] = df["Quantity"] * df["UnitPrice"]

monthly_revenue_df = df.set_index("InvoiceDate")["Sales"].resample("M").sum()

cc = monthly_revenue_df
print(cc)

ax = pd.DataFrame(monthly_revenue_df.values).plot(
    grid=True, figsize=(10, 7), legend=False
)

ax.set_xlabel("date")
ax.set_ylabel("sales")
ax.set_title("Total Revenue Over Time")

ax.set_ylim([0, max(monthly_revenue_df.values) + 100000])

plt.xticks(
    range(len(monthly_revenue_df.index)),
    [x.strftime("%m.%Y") for x in monthly_revenue_df.index],
    rotation=45,
)

plt.show()

# - Time-series Repeat Customers

cc = df.head()
print(cc)

invoice_customer_df = (
    df.groupby(by=["InvoiceNo", "InvoiceDate"])
    .agg(
        {
            "Sales": sum,
            "CustomerID": max,
            "Country": max,
        }
    )
    .reset_index()
)

cc = invoice_customer_df.head()
print(cc)

monthly_repeat_customers_df = (
    invoice_customer_df.set_index("InvoiceDate")
    .groupby([pd.Grouper(freq="M"), "CustomerID"])
    .filter(lambda x: len(x) > 1)
    .resample("M")
    .nunique()["CustomerID"]
)

cc = monthly_repeat_customers_df
print(cc)

monthly_unique_customers_df = (
    df.set_index("InvoiceDate")["CustomerID"].resample("M").nunique()
)

cc = monthly_unique_customers_df
print(cc)

monthly_repeat_percentage = (
    monthly_repeat_customers_df / monthly_unique_customers_df * 100.0
)
cc = monthly_repeat_percentage
print(cc)

ax = pd.DataFrame(monthly_repeat_customers_df.values).plot(figsize=(10, 7))

pd.DataFrame(monthly_unique_customers_df.values).plot(ax=ax, grid=True)


ax2 = pd.DataFrame(monthly_repeat_percentage.values).plot.bar(
    ax=ax, grid=True, secondary_y=True, color="green", alpha=0.2
)

ax.set_xlabel("date")
ax.set_ylabel("number of customers")
ax.set_title("Number of All vs. Repeat Customers Over Time")

ax2.set_ylabel("percentage (%)")

ax.legend(["Repeat Customers", "All Customers"])
ax2.legend(["Percentage of Repeat"], loc="upper right")

ax.set_ylim([0, monthly_unique_customers_df.values.max() + 100])
ax2.set_ylim([0, 100])

plt.xticks(
    range(len(monthly_repeat_customers_df.index)),
    [x.strftime("%m.%Y") for x in monthly_repeat_customers_df.index],
    rotation=45,
)

plt.show()

# - Revenue from Repeat Customers

monthly_rev_repeat_customers_df = (
    invoice_customer_df.set_index("InvoiceDate")
    .groupby([pd.Grouper(freq="M"), "CustomerID"])
    .filter(lambda x: len(x) > 1)
    .resample("M")
    .sum()["Sales"]
)

monthly_rev_perc_repeat_customers_df = (
    monthly_rev_repeat_customers_df / monthly_revenue_df * 100.0
)

cc = monthly_rev_repeat_customers_df
print(cc)

ax = pd.DataFrame(monthly_revenue_df.values).plot(figsize=(12, 9))

pd.DataFrame(monthly_rev_repeat_customers_df.values).plot(
    ax=ax,
    grid=True,
)

ax.set_xlabel("date")
ax.set_ylabel("sales")
ax.set_title("Total Revenue vs. Revenue from Repeat Customers")

ax.legend(["Total Revenue", "Repeat Customer Revenue"])

ax.set_ylim([0, max(monthly_revenue_df.values) + 100000])

ax2 = ax.twinx()

pd.DataFrame(monthly_rev_perc_repeat_customers_df.values).plot(
    ax=ax2, kind="bar", color="g", alpha=0.2
)

ax2.set_ylim([0, max(monthly_rev_perc_repeat_customers_df.values) + 30])
ax2.set_ylabel("percentage (%)")
ax2.legend(["Repeat Revenue Percentage"])

ax2.set_xticklabels(
    [x.strftime("%m.%Y") for x in monthly_rev_perc_repeat_customers_df.index]
)

plt.show()

# - Popular Items Over Time

date_item_df = pd.DataFrame(
    df.set_index("InvoiceDate")
    .groupby([pd.Grouper(freq="M"), "StockCode"])["Quantity"]
    .sum()
)
cc = date_item_df
print(cc)

# Rank items by the last month sales
last_month_sorted_df = (
    date_item_df.loc["2011-11-30"]
    .sort_values(by="Quantity", ascending=False)
    .reset_index()
)

cc = last_month_sorted_df
print(cc)

# Regroup for top 5 items
date_item_df = pd.DataFrame(
    df.loc[df["StockCode"].isin([23084, 84826, 22197, 22086, "85099B"])]
    .set_index("InvoiceDate")
    .groupby([pd.Grouper(freq="ME"), "StockCode"])["Quantity"]
    .sum()
)
cc = date_item_df
print(cc)

""" NG
trending_itmes_df = date_item_df.reset_index().pivot('InvoiceDate','StockCode').fillna(0)

trending_itmes_df = trending_itmes_df.reset_index()
trending_itmes_df = trending_itmes_df.set_index('InvoiceDate')
trending_itmes_df.columns = trending_itmes_df.columns.droplevel(0)

cc = trending_itmes_df
print(cc)

ax = pd.DataFrame(trending_itmes_df.values).plot(
    figsize=(10,7),
    grid=True,
)

ax.set_ylabel('number of purchases')
ax.set_xlabel('date')
ax.set_title('Item Trends over Time')

ax.legend(trending_itmes_df.columns, loc='upper left')

plt.xticks(
    range(len(trending_itmes_df.index)), 
    [x.strftime('%m.%Y') for x in trending_itmes_df.index], 
    rotation=45
)

plt.show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Product Recommendation

df = pd.read_excel(io="data/Online Retail.xlsx", sheet_name="Online Retail")

cc = df.shape
print(cc)

# (541909, 8)

cc = df.head()
print(cc)

df = df.loc[df["Quantity"] > 0]

# 2. Data Preparation
# - Handle NaNs in CustomerID field

cc = df["CustomerID"].describe()
print(cc)

cc = df["CustomerID"].isna().sum()
print(cc)
# 133361

cc = df.loc[df["CustomerID"].isna()].head()
print(cc)

cc = df.shape
print(cc)
# (531285, 8)

df = df.dropna(subset=["CustomerID"])

cc = df.shape
print(cc)
# (397924, 8)

cc = df.head()
print(cc)

# - Customer-Item Matrix

customer_item_matrix = df.pivot_table(
    index="CustomerID", columns="StockCode", values="Quantity", aggfunc="sum"
)

cc = customer_item_matrix.loc[12481:].head()
print(cc)

cc = customer_item_matrix.shape
print(cc)
# (4339, 3665)

cc = df["StockCode"].nunique()
print(cc)
# 3665

cc = df["CustomerID"].nunique()
print(cc)
# 4339

cc = customer_item_matrix.loc[12348.0].sum()
print(cc)
# 2341.0

customer_item_matrix = customer_item_matrix.applymap(lambda x: 1 if x > 0 else 0)

cc = customer_item_matrix.loc[12481:].head()
print(cc)

# 3. Collaborative Filtering

from sklearn.metrics.pairwise import cosine_similarity

# 3.1. User-based Collaborative Filtering
# - User-to-User Similarity Matrix

user_user_sim_matrix = pd.DataFrame(cosine_similarity(customer_item_matrix))

cc = user_user_sim_matrix.head()
print(cc)

user_user_sim_matrix.columns = customer_item_matrix.index

user_user_sim_matrix["CustomerID"] = customer_item_matrix.index
user_user_sim_matrix = user_user_sim_matrix.set_index("CustomerID")

cc = user_user_sim_matrix.head()
print(cc)

# - Making Recommendations

cc = user_user_sim_matrix.loc[12350.0].sort_values(ascending=False)
print(cc)

items_bought_by_A = set(
    customer_item_matrix.loc[12350.0].iloc[customer_item_matrix.loc[12350.0]].index
)

cc = items_bought_by_A
print(cc)

items_bought_by_B = set(
    customer_item_matrix.loc[17935.0].iloc[customer_item_matrix.loc[17935.0]].index
)

cc = items_bought_by_B
print(cc)

items_to_recommend_to_B = items_bought_by_A - items_bought_by_B

cc = items_to_recommend_to_B
print(cc)

cc = (
    df.loc[df["StockCode"].isin(items_to_recommend_to_B), ["StockCode", "Description"]]
    .drop_duplicates()
    .set_index("StockCode")
)
print(cc)

# 3.2. Item-based Collaborative Filtering
# - Item-to-Item Similarity Matrix

item_item_sim_matrix = pd.DataFrame(cosine_similarity(customer_item_matrix.T))

item_item_sim_matrix.columns = customer_item_matrix.T.index

item_item_sim_matrix["StockCode"] = customer_item_matrix.T.index
item_item_sim_matrix = item_item_sim_matrix.set_index("StockCode")

cc = item_item_sim_matrix
print(cc)

# - Making Recommendations

top_10_similar_items = list(
    item_item_sim_matrix.loc[23166].sort_values(ascending=False).iloc[:10].index
)

cc = top_10_similar_items
print(cc)

cc = (
    df.loc[df["StockCode"].isin(top_10_similar_items), ["StockCode", "Description"]]
    .drop_duplicates()
    .set_index("StockCode")
    .loc[top_10_similar_items]
)

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
