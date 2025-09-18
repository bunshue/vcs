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

filename = "D:/_git/vcs/_big_files/Online Retail.xlsx"
df = pd.read_excel(io=filename, sheet_name="Online Retail")

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

filename = "D:/_git/vcs/_big_files/Online Retail.xlsx"
df = pd.read_excel(io=filename, sheet_name="Online Retail")

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

# Customer Behaviors

df = pd.read_csv("data/WA_Fn-UseC_-Marketing-Customer-Value-Analysis.csv")

df.shape

df.head()

# 2. Analytics on Engaged Customers
# 2. 參與客戶的分析
# - Overall Engagement Rate

cc = df.groupby("Response").count()["Customer"]
print(cc)

ax = (
    df.groupby("Response")
    .count()["Customer"]
    .plot(
        kind="bar",
        color="skyblue",
        grid=True,
        figsize=(10, 7),
        title="Marketing Engagment",
    )
)

ax.set_xlabel("Engaged")
ax.set_ylabel("Count")

plt.show()

cc = df.groupby("Response").count()["Customer"] / df.shape[0]
print(cc)

# - Engagement Rates by Offer Type
# - 按優惠類型劃分的參與率

by_offer_type_df = (
    df.loc[df["Response"] == "Yes"].groupby(["Renew Offer Type"]).count()["Customer"]
    / df.groupby("Renew Offer Type").count()["Customer"]
)

cc = by_offer_type_df
print(cc)


ax = (by_offer_type_df * 100.0).plot(
    kind="bar", figsize=(7, 7), color="skyblue", grid=True
)

ax.set_ylabel("Engagement Rate (%)")

plt.show()

# Offer Type & Vehicle Class

by_offer_type_df = (
    df.loc[df["Response"] == "Yes"]
    .groupby(["Renew Offer Type", "Vehicle Class"])
    .count()["Customer"]
    / df.groupby("Renew Offer Type").count()["Customer"]
)

cc = by_offer_type_df

print(cc)


by_offer_type_df = by_offer_type_df.unstack().fillna(0)
cc = by_offer_type_df

print(cc)

ax = (by_offer_type_df * 100.0).plot(kind="bar", figsize=(10, 7), grid=True)

ax.set_ylabel("Engagement Rate (%)")

plt.show()

# - Engagement Rates by Sales Channel

by_sales_channel_df = (
    df.loc[df["Response"] == "Yes"].groupby(["Sales Channel"]).count()["Customer"]
    / df.groupby("Sales Channel").count()["Customer"]
)

cc = by_sales_channel_df

print(cc)

ax = (by_sales_channel_df * 100.0).plot(
    kind="bar", figsize=(7, 7), color="skyblue", grid=True
)

ax.set_ylabel("Engagement Rate (%)")

plt.show()


# Sales Channel & Vehicle Size

by_sales_channel_df = (
    df.loc[df["Response"] == "Yes"]
    .groupby(["Sales Channel", "Vehicle Size"])
    .count()["Customer"]
    / df.groupby("Sales Channel").count()["Customer"]
)

cc = by_sales_channel_df
print(cc)

by_sales_channel_df = by_sales_channel_df.unstack().fillna(0)
cc = by_sales_channel_df
print(cc)


ax = (by_sales_channel_df * 100.0).plot(kind="bar", figsize=(10, 7), grid=True)

ax.set_ylabel("Engagement Rate (%)")

plt.show()


# - Engagement Rates by Months Since Policy Inception


by_months_since_inception_df = (
    df.loc[df["Response"] == "Yes"]
    .groupby(by="Months Since Policy Inception")["Response"]
    .count()
    / df.groupby(by="Months Since Policy Inception")["Response"].count()
    * 100.0
)

cc = by_months_since_inception_df.fillna(0)
print(cc)


ax = by_months_since_inception_df.fillna(0).plot(
    figsize=(10, 7),
    title="Engagement Rates by Months Since Inception",
    grid=True,
    color="skyblue",
)

ax.set_xlabel("Months Since Policy Inception")
ax.set_ylabel("Engagement Rate (%)")

plt.show()


# 3. Customer Segmentation by CLV & Months Since Policy Inception

cc = df["Customer Lifetime Value"].describe()
print(cc)

df["CLV Segment"] = df["Customer Lifetime Value"].apply(
    lambda x: "High" if x > df["Customer Lifetime Value"].median() else "Low"
)
cc = df["Months Since Policy Inception"].describe()
print(cc)

df["Policy Age Segment"] = df["Months Since Policy Inception"].apply(
    lambda x: "High" if x > df["Months Since Policy Inception"].median() else "Low"
)
cc = df.head()
print(cc)

ax = df.loc[
    (df["CLV Segment"] == "High") & (df["Policy Age Segment"] == "High")
].plot.scatter(
    x="Months Since Policy Inception",
    y="Customer Lifetime Value",
    logy=True,
    color="red",
)

df.loc[
    (df["CLV Segment"] == "Low") & (df["Policy Age Segment"] == "High")
].plot.scatter(
    ax=ax,
    x="Months Since Policy Inception",
    y="Customer Lifetime Value",
    logy=True,
    color="blue",
)

df.loc[
    (df["CLV Segment"] == "High") & (df["Policy Age Segment"] == "Low")
].plot.scatter(
    ax=ax,
    x="Months Since Policy Inception",
    y="Customer Lifetime Value",
    logy=True,
    color="orange",
)

df.loc[(df["CLV Segment"] == "Low") & (df["Policy Age Segment"] == "Low")].plot.scatter(
    ax=ax,
    x="Months Since Policy Inception",
    y="Customer Lifetime Value",
    logy=True,
    color="green",
    grid=True,
    figsize=(10, 7),
)

ax.set_ylabel("CLV (in log scale)")
ax.set_xlabel("Months Since Policy Inception")

ax.set_title("Segments by CLV and Policy Age")

plt.show()


engagment_rates_by_segment_df = (
    df.loc[df["Response"] == "Yes"]
    .groupby(["CLV Segment", "Policy Age Segment"])
    .count()["Customer"]
    / df.groupby(["CLV Segment", "Policy Age Segment"]).count()["Customer"]
)

cc = engagment_rates_by_segment_df
print(cc)

ax = (engagment_rates_by_segment_df.unstack() * 100.0).plot(
    kind="bar", figsize=(10, 7), grid=True
)

ax.set_ylabel("Engagement Rate (%)")
ax.set_title("Engagement Rates by Customer Segments")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# PredictingEngagement

# 1. Load Data

df = pd.read_csv("data/WA_Fn-UseC_-Marketing-Customer-Value-Analysis.csv")

# df.shape

# (9134, 24)

# df.head()

# 2. Variable Encoding
# 2.1. Response Variable: Response

df["Engaged"] = df["Response"].apply(lambda x: 1 if x == "Yes" else 0)

cc = df["Engaged"].mean()
print(cc)

# 0.14320122618786948

# 2.2. Features

cc = df.describe()
print(cc)

continuous_features = [
    "Customer Lifetime Value",
    "Income",
    "Monthly Premium Auto",
    "Months Since Last Claim",
    "Months Since Policy Inception",
    "Number of Open Complaints",
    "Number of Policies",
    "Total Claim Amount",
]

# - Creating Dummy Variables

columns_to_encode = [
    "Sales Channel",
    "Vehicle Size",
    "Vehicle Class",
    "Policy",
    "Policy Type",
    "EmploymentStatus",
    "Marital Status",
    "Education",
    "Coverage",
]

categorical_features = []
for col in columns_to_encode:
    encoded_df = pd.get_dummies(df[col])
    encoded_df.columns = [col.replace(" ", ".") + "." + x for x in encoded_df.columns]

    categorical_features += list(encoded_df.columns)

    df = pd.concat([df, encoded_df], axis=1)

# - Encoding Gender

df["Is.Female"] = df["Gender"].apply(lambda x: 1 if x == "F" else 0)

categorical_features.append("Is.Female")

# - all features & response

all_features = continuous_features + categorical_features
response = "Engaged"

sample_df = df[all_features + [response]]
sample_df.columns = [x.replace(" ", ".") for x in sample_df.columns]
all_features = [x.replace(" ", ".") for x in all_features]

cc = sample_df.head()
print(cc)

# 3. Training & Testing

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(
    sample_df[all_features], sample_df[response], test_size=0.3
)

# sample_df.shape

# (9134, 51)

# x_train.shape

# (6393, 50)

# x_test.shape

# (2741, 50)

# 3.1. Building RandomForest Model

from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(n_estimators=200, max_depth=5)

rf_model.fit(X=x_train, y=y_train)

# - Individual Trees

cc = rf_model.estimators_
print(cc)

cc = rf_model.estimators_[0]
print(cc)

cc = rf_model.estimators_[0].predict(x_test)[:10]
print(cc)
# array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

cc = rf_model.estimators_[1].predict(x_test)[:10]
print(cc)
# array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

cc = rf_model.estimators_[2].predict(x_test)[:10]
print(cc)
# array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

cc = rf_model.estimators_[3].predict(x_test)[:10]
print(cc)
# array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

cc = rf_model.estimators_[4].predict(x_test)[:10]
print(cc)
# array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])

# - Feature Importances

cc = rf_model.feature_importances_
print(cc)

feature_importance_df = pd.DataFrame(
    list(zip(rf_model.feature_importances_, all_features))
)
feature_importance_df.columns = ["feature.importance", "feature"]

feature_importance_df.sort_values(by="feature.importance", ascending=False)

# 3.2. Evaluating Models
# - Accuracy, Precision, and Recall

from sklearn.metrics import accuracy_score, precision_score, recall_score

in_sample_preds = rf_model.predict(x_train)
out_sample_preds = rf_model.predict(x_test)

print("In-Sample Accuracy: %0.4f" % accuracy_score(y_train, in_sample_preds))
print("Out-of-Sample Accuracy: %0.4f" % accuracy_score(y_test, out_sample_preds))

# In-Sample Accuracy: 0.8789
# Out-of-Sample Accuracy: 0.8676

print("In-Sample Precision: %0.4f" % precision_score(y_train, in_sample_preds))
print("Out-of-Sample Precision: %0.4f" % precision_score(y_test, out_sample_preds))

# In-Sample Precision: 0.9921
# Out-of-Sample Precision: 0.9123

print("In-Sample Recall: %0.4f" % recall_score(y_train, in_sample_preds))
print("Out-of-Sample Recall: %0.4f" % recall_score(y_test, out_sample_preds))

# In-Sample Recall: 0.1392
# Out-of-Sample Recall: 0.1268

# - ROC & AUC

from sklearn.metrics import roc_curve, auc

in_sample_preds = rf_model.predict_proba(x_train)[:, 1]
out_sample_preds = rf_model.predict_proba(x_test)[:, 1]

in_sample_fpr, in_sample_tpr, in_sample_thresholds = roc_curve(y_train, in_sample_preds)
out_sample_fpr, out_sample_tpr, out_sample_thresholds = roc_curve(
    y_test, out_sample_preds
)

in_sample_roc_auc = auc(in_sample_fpr, in_sample_tpr)
out_sample_roc_auc = auc(out_sample_fpr, out_sample_tpr)

print("In-Sample AUC: %0.4f" % in_sample_roc_auc)
print("Out-Sample AUC: %0.4f" % out_sample_roc_auc)

# In-Sample AUC: 0.8842
# Out-Sample AUC: 0.8277

plt.figure(figsize=(10, 7))

plt.plot(
    out_sample_fpr,
    out_sample_tpr,
    color="darkorange",
    label="Out-Sample ROC curve (area = %0.4f)" % in_sample_roc_auc,
)
plt.plot(
    in_sample_fpr,
    in_sample_tpr,
    color="navy",
    label="In-Sample ROC curve (area = %0.4f)" % out_sample_roc_auc,
)
plt.plot([0, 1], [0, 1], color="gray", lw=1, linestyle="--")
plt.grid()
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("RandomForest Model ROC Curve")
plt.legend(loc="lower right")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# CustomerLifetimeValue

# 1. Load Data

filename = "D:/_git/vcs/_big_files/Online Retail.xlsx"
df = pd.read_excel(filename, sheet_name="Online Retail")

# df.shape
# (541909, 8)

# df.head()

# 2. Data Clean-Up
# - Negative Quantity

# df.loc[df['Quantity'] <= 0].shape

# (10624, 8)

# df.shape

# (541909, 8)

df = df.loc[df["Quantity"] > 0]

# df.shape

# (531285, 8)

# - Missing CustomerID

cc = pd.isnull(df["CustomerID"]).sum()
print(cc)

# 133361

cc = df.shape
print(cc)

# (531285, 8)

df = df[pd.notnull(df["CustomerID"])]

cc = df.shape
print(cc)

# (397924, 8)

cc = df.head()
print(cc)

# - Excluding Incomplete Month

print("Date Range: %s ~ %s" % (df["InvoiceDate"].min(), df["InvoiceDate"].max()))

# Date Range: 2010-12-01 08:26:00 ~ 2011-12-09 12:50:00

cc = df.loc[df["InvoiceDate"] >= "2011-12-01"].shape
print(cc)

# (17304, 8)

# df.shape

# (397924, 8)

df = df.loc[df["InvoiceDate"] < "2011-12-01"]

# df.shape

# (380620, 8)

# - Total Sales

df["Sales"] = df["Quantity"] * df["UnitPrice"]

cc = df.head()
print(cc)

# - Per Order Data

orders_df = df.groupby(["CustomerID", "InvoiceNo"]).agg(
    {"Sales": sum, "InvoiceDate": max}
)

cc = orders_df
print(cc)

# 3. Data Analysis


def groupby_mean(x):
    return x.mean()


def groupby_count(x):
    return x.count()


def purchase_duration(x):
    return (x.max() - x.min()).days


def avg_frequency(x):
    return (x.max() - x.min()).days / x.count()


groupby_mean.__name__ = "avg"
groupby_count.__name__ = "count"
purchase_duration.__name__ = "purchase_duration"
avg_frequency.__name__ = "purchase_frequency"

summary_df = (
    orders_df.reset_index()
    .groupby("CustomerID")
    .agg(
        {
            "Sales": [min, max, sum, groupby_mean, groupby_count],
            "InvoiceDate": [min, max, purchase_duration, avg_frequency],
        }
    )
)

cc = summary_df
print(cc)

summary_df.columns = ["_".join(col).lower() for col in summary_df.columns]

cc = summary_df
print(cc)

# summary_df.shape

# (4298, 9)

summary_df = summary_df.loc[summary_df["invoicedate_purchase_duration"] > 0]

# summary_df.shape
# (2692, 9)

ax = (
    summary_df.groupby("sales_count")
    .count()["sales_avg"][:20]
    .plot(kind="bar", color="skyblue", figsize=(12, 7), grid=True)
)

ax.set_ylabel("count")

plt.show()

cc = summary_df["sales_count"].describe()
print(cc)

cc = summary_df["sales_avg"].describe()
print(cc)

ax = summary_df["invoicedate_purchase_frequency"].hist(
    bins=20, color="skyblue", rwidth=0.7, figsize=(12, 7)
)

ax.set_xlabel("avg. number of days between purchases")
ax.set_ylabel("count")

plt.show()

cc = summary_df["invoicedate_purchase_frequency"].describe()
print(cc)

cc = summary_df["invoicedate_purchase_duration"].describe()
print(cc)

# 4. Predicting 3-Month CLV
# 4.1. Data Preparation

clv_freq = "3M"

data_df = (
    orders_df.reset_index()
    .groupby(["CustomerID", pd.Grouper(key="InvoiceDate", freq=clv_freq)])
    .agg(
        {
            "Sales": [sum, groupby_mean, groupby_count],
        }
    )
)

data_df.columns = ["_".join(col).lower() for col in data_df.columns]

data_df = data_df.reset_index()

cc = data_df.head(10)
print(cc)

date_month_map = {
    str(x)[:10]: "M_%s" % (i + 1)
    for i, x in enumerate(
        sorted(data_df.reset_index()["InvoiceDate"].unique(), reverse=True)
    )
}

data_df["M"] = data_df["InvoiceDate"].apply(lambda x: date_month_map[str(x)[:10]])

cc = date_month_map
print(cc)

cc = data_df.head(10)
print(cc)

# - Building Sample Set

features_df = pd.pivot_table(
    data_df.loc[data_df["M"] != "M_1"],
    values=["sales_sum", "sales_avg", "sales_count"],
    columns="M",
    index="CustomerID",
)

features_df.columns = ["_".join(col) for col in features_df.columns]

# features_df.shape
# (3616, 12)

cc = features_df.head(10)
print(cc)

features_df = features_df.fillna(0)

cc = features_df.head()
print(cc)

response_df = data_df.loc[data_df["M"] == "M_1", ["CustomerID", "sales_sum"]]

response_df.columns = ["CustomerID", "CLV_" + clv_freq]

# response_df.shape
# (2407, 2)

cc = response_df.head(10)
print(cc)

sample_set_df = features_df.merge(
    response_df, left_index=True, right_on="CustomerID", how="left"
)

# sample_set_df.shape
# (3616, 14)

cc = sample_set_df.head(10)
print(cc)

sample_set_df = sample_set_df.fillna(0)

cc = sample_set_df.head()
print(cc)

cc = sample_set_df["CLV_" + clv_freq].describe()
print(cc)

# 4.2. Regression Models

from sklearn.model_selection import train_test_split

target_var = "CLV_" + clv_freq
all_features = [x for x in sample_set_df.columns if x not in ["CustomerID", target_var]]

x_train, x_test, y_train, y_test = train_test_split(
    sample_set_df[all_features], sample_set_df[target_var], test_size=0.3
)

# - Linear Regression Model

from sklearn.linear_model import LinearRegression

# Try these models as well
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor

reg_fit = LinearRegression()

reg_fit.fit(x_train, y_train)

cc = reg_fit.intercept_
print(cc)

# 57.372538081909454

coef = pd.DataFrame(list(zip(all_features, reg_fit.coef_)))
coef.columns = ["feature", "coef"]

cc = coef
print(cc)

# 4.3. Evaluation

from sklearn.metrics import r2_score, median_absolute_error

train_preds = reg_fit.predict(x_train)
test_preds = reg_fit.predict(x_test)

# - R-Squared

print("In-Sample R-Squared: %0.4f" % r2_score(y_true=y_train, y_pred=train_preds))
print("Out-of-Sample R-Squared: %0.4f" % r2_score(y_true=y_test, y_pred=test_preds))

# In-Sample R-Squared: 0.7271
# Out-of-Sample R-Squared: 0.6739

# - Median Absolute Error

print(
    "In-Sample MSE: %0.4f" % median_absolute_error(y_true=y_train, y_pred=train_preds)
)
print(
    "Out-of-Sample MSE: %0.4f" % median_absolute_error(y_true=y_test, y_pred=test_preds)
)

# In-Sample MSE: 174.0245
# Out-of-Sample MSE: 198.8963

# - Scatter Plot

plt.scatter(y_train, train_preds)
plt.plot([0, max(y_train)], [0, max(train_preds)], color="gray", lw=1, linestyle="--")

plt.xlabel("actual")
plt.ylabel("predicted")
plt.title("In-Sample Actual vs. Predicted")
plt.grid()

plt.show()

plt.scatter(y_test, test_preds)
plt.plot([0, max(y_test)], [0, max(test_preds)], color="gray", lw=1, linestyle="--")

plt.xlabel("actual")
plt.ylabel("predicted")
plt.title("Out-of-Sample Actual vs. Predicted")
plt.grid()

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Customer Segmentation

filename = "D:/_git/vcs/_big_files/Online Retail.xlsx"

# 1. Load Data

df = pd.read_excel(filename, sheet_name="Online Retail")

# df.shape
# (541909, 8)

# df.head()

# 2. Data Clean-Up
# - Negative Quantity

# df.loc[df['Quantity'] <= 0].shape
# (10624, 8)

# df.shape
# (541909, 8)

df = df.loc[df["Quantity"] > 0]

# df.shape
# (531285, 8)

# - Missing CustomerID

pd.isnull(df["CustomerID"]).sum()

# 133361

df.shape

# (531285, 8)

df = df[pd.notnull(df["CustomerID"])]

# df.shape

# (397924, 8)

# df.head()

# - Excluding Incomplete Month

print("Date Range: %s ~ %s" % (df["InvoiceDate"].min(), df["InvoiceDate"].max()))

# Date Range: 2010-12-01 08:26:00 ~ 2011-12-09 12:50:00

df.loc[df["InvoiceDate"] >= "2011-12-01"].shape

# (17304, 8)

df.shape

# (397924, 8)

df = df.loc[df["InvoiceDate"] < "2011-12-01"]

df.shape

# (380620, 8)

# - Total Sales

df["Sales"] = df["Quantity"] * df["UnitPrice"]

df.head()

# - Per Customer Data

customer_df = df.groupby("CustomerID").agg(
    {"Sales": sum, "InvoiceNo": lambda x: x.nunique()}
)

customer_df.columns = ["TotalSales", "OrderCount"]
customer_df["AvgOrderValue"] = customer_df["TotalSales"] / customer_df["OrderCount"]

# customer_df.head(15)

cc = customer_df.describe()
print(cc)

rank_df = customer_df.rank(method="first")

cc = rank_df.head(15)
print(cc)

cc = rank_df.describe()
print(cc)

normalized_df = (rank_df - rank_df.mean()) / rank_df.std()

cc = normalized_df.head(15)
print(cc)

cc = normalized_df.describe()
print(cc)

# 3. Customer Segmentation via K-Means Clustering

from sklearn.cluster import KMeans

# - K-Means Clustering

kmeans = KMeans(n_clusters=4).fit(
    normalized_df[["TotalSales", "OrderCount", "AvgOrderValue"]]
)

# kmeans

cc = kmeans.labels_
print(cc)

cc = kmeans.cluster_centers_
print(cc)

four_cluster_df = normalized_df[["TotalSales", "OrderCount", "AvgOrderValue"]].copy(
    deep=True
)
four_cluster_df["Cluster"] = kmeans.labels_

cc = four_cluster_df.head()
print(cc)

cc = four_cluster_df.groupby("Cluster").count()["TotalSales"]
print(cc)

plt.scatter(
    four_cluster_df.loc[four_cluster_df["Cluster"] == 0]["OrderCount"],
    four_cluster_df.loc[four_cluster_df["Cluster"] == 0]["TotalSales"],
    c="blue",
)

plt.scatter(
    four_cluster_df.loc[four_cluster_df["Cluster"] == 1]["OrderCount"],
    four_cluster_df.loc[four_cluster_df["Cluster"] == 1]["TotalSales"],
    c="red",
)

plt.scatter(
    four_cluster_df.loc[four_cluster_df["Cluster"] == 2]["OrderCount"],
    four_cluster_df.loc[four_cluster_df["Cluster"] == 2]["TotalSales"],
    c="orange",
)

plt.scatter(
    four_cluster_df.loc[four_cluster_df["Cluster"] == 3]["OrderCount"],
    four_cluster_df.loc[four_cluster_df["Cluster"] == 3]["TotalSales"],
    c="green",
)

plt.title("TotalSales vs. OrderCount Clusters")
plt.xlabel("Order Count")
plt.ylabel("Total Sales")

plt.grid()
plt.show()


plt.scatter(
    four_cluster_df.loc[four_cluster_df["Cluster"] == 0]["OrderCount"],
    four_cluster_df.loc[four_cluster_df["Cluster"] == 0]["AvgOrderValue"],
    c="blue",
)

plt.scatter(
    four_cluster_df.loc[four_cluster_df["Cluster"] == 1]["OrderCount"],
    four_cluster_df.loc[four_cluster_df["Cluster"] == 1]["AvgOrderValue"],
    c="red",
)

plt.scatter(
    four_cluster_df.loc[four_cluster_df["Cluster"] == 2]["OrderCount"],
    four_cluster_df.loc[four_cluster_df["Cluster"] == 2]["AvgOrderValue"],
    c="orange",
)

plt.scatter(
    four_cluster_df.loc[four_cluster_df["Cluster"] == 3]["OrderCount"],
    four_cluster_df.loc[four_cluster_df["Cluster"] == 3]["AvgOrderValue"],
    c="green",
)

plt.title("AvgOrderValue vs. OrderCount Clusters")
plt.xlabel("Order Count")
plt.ylabel("Avg Order Value")

plt.grid()
plt.show()


plt.scatter(
    four_cluster_df.loc[four_cluster_df["Cluster"] == 0]["TotalSales"],
    four_cluster_df.loc[four_cluster_df["Cluster"] == 0]["AvgOrderValue"],
    c="blue",
)

plt.scatter(
    four_cluster_df.loc[four_cluster_df["Cluster"] == 1]["TotalSales"],
    four_cluster_df.loc[four_cluster_df["Cluster"] == 1]["AvgOrderValue"],
    c="red",
)

plt.scatter(
    four_cluster_df.loc[four_cluster_df["Cluster"] == 2]["TotalSales"],
    four_cluster_df.loc[four_cluster_df["Cluster"] == 2]["AvgOrderValue"],
    c="orange",
)

plt.scatter(
    four_cluster_df.loc[four_cluster_df["Cluster"] == 3]["TotalSales"],
    four_cluster_df.loc[four_cluster_df["Cluster"] == 3]["AvgOrderValue"],
    c="green",
)

plt.title("AvgOrderValue vs. TotalSales Clusters")
plt.xlabel("Total Sales")
plt.ylabel("Avg Order Value")

plt.grid()
plt.show()

# - Selecting the best number of clusters

from sklearn.metrics import silhouette_score

for n_cluster in [4, 5, 6, 7, 8]:
    kmeans = KMeans(n_clusters=n_cluster).fit(
        normalized_df[["TotalSales", "OrderCount", "AvgOrderValue"]]
    )
    silhouette_avg = silhouette_score(
        normalized_df[["TotalSales", "OrderCount", "AvgOrderValue"]], kmeans.labels_
    )

    print("Silhouette Score for %i Clusters: %0.4f" % (n_cluster, silhouette_avg))

"""
Silhouette Score for 4 Clusters: 0.4114
Silhouette Score for 5 Clusters: 0.3779
Silhouette Score for 6 Clusters: 0.3780
Silhouette Score for 7 Clusters: 0.3907
Silhouette Score for 8 Clusters: 0.3811
"""

# - Interpreting Customer Segments

kmeans = KMeans(n_clusters=4).fit(
    normalized_df[["TotalSales", "OrderCount", "AvgOrderValue"]]
)

four_cluster_df = normalized_df[["TotalSales", "OrderCount", "AvgOrderValue"]].copy(
    deep=True
)
four_cluster_df["Cluster"] = kmeans.labels_

cc = four_cluster_df.head(15)
print(cc)

cc = kmeans.cluster_centers_
print(cc)

high_value_cluster = four_cluster_df.loc[four_cluster_df["Cluster"] == 2]
cc = high_value_cluster.head()
print(cc)

cc = customer_df.loc[high_value_cluster.index].describe()
print(cc)

cc = pd.DataFrame(
    df.loc[df["CustomerID"].isin(high_value_cluster.index)]
    .groupby("Description")
    .count()["StockCode"]
    .sort_values(ascending=False)
    .head()
)
print(cc)

cc = pd.DataFrame(
    df.loc[
        df["CustomerID"].isin(
            four_cluster_df.loc[four_cluster_df["Cluster"] == 3].index
        )
    ]
    .groupby("Description")
    .count()["StockCode"]
    .sort_values(ascending=False)
    .head()
)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Customer Retention

df = pd.read_excel("data/WA_Fn-UseC_-Telco-Customer-Churn.xlsx")

# df.shape
# (7043, 21)

# df.head(10)

# 2. Data Analysis & Preparation
# - Encoding target var: Churn

df["Churn"] = df["Churn"].apply(lambda x: 1 if x == "Yes" else 0)

cc = df["Churn"].mean()
print(cc)

# 0.2653698707936959

# - TotalCharges

df["TotalCharges"] = df["TotalCharges"].replace(" ", np.nan).astype(float)

# df.shape

# (7043, 21)

df.dropna().shape

# (7032, 21)

df = df.dropna()

# - Continuous Vars

cc = df[["tenure", "MonthlyCharges", "TotalCharges"]].describe()
print(cc)

df["MonthlyCharges"] = np.log(df["MonthlyCharges"])
df["MonthlyCharges"] = (df["MonthlyCharges"] - df["MonthlyCharges"].mean()) / df[
    "MonthlyCharges"
].std()

df["TotalCharges"] = np.log(df["TotalCharges"])
df["TotalCharges"] = (df["TotalCharges"] - df["TotalCharges"].mean()) / df[
    "TotalCharges"
].std()

df["tenure"] = (df["tenure"] - df["tenure"].mean()) / df["tenure"].std()

cc = df[["tenure", "MonthlyCharges", "TotalCharges"]].describe()
print(cc)

continuous_vars = list(df.describe().columns)
cc = continuous_vars
print(cc)

# ['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges', 'Churn']

# - One-Hot Encoding

for col in list(df.columns):
    print(col, df[col].nunique())

df.groupby("gender").count()["customerID"].plot(
    kind="bar", color="skyblue", grid=True, figsize=(8, 6), title="Gender"
)
plt.show()

df.groupby("InternetService").count()["customerID"].plot(
    kind="bar", color="skyblue", grid=True, figsize=(8, 6), title="Internet Service"
)
plt.show()

df.groupby("PaymentMethod").count()["customerID"].plot(
    kind="bar", color="skyblue", grid=True, figsize=(8, 6), title="Payment Method"
)
plt.show()

dummy_cols = []

sample_set = df[["tenure", "MonthlyCharges", "TotalCharges", "Churn"]].copy(deep=True)

for col in list(df.columns):
    if (
        col not in ["tenure", "MonthlyCharges", "TotalCharges", "Churn"]
        and df[col].nunique() < 5
    ):
        dummy_vars = pd.get_dummies(df[col])
        dummy_vars.columns = [col + str(x) for x in dummy_vars.columns]
        sample_set = pd.concat([sample_set, dummy_vars], axis=1)

cc = sample_set.head(10)
print(cc)

# sample_set.shape
# (7032, 47)

cc = list(sample_set.columns)
print(cc)

# 3. Train & Test Sets

target_var = "Churn"
features = [x for x in list(sample_set.columns) if x != target_var]

# 4. Aritificial Neural Network (ANN) with Keras

from keras.models import Sequential
from keras.layers import Dense

# - Training a Neural Network Model

model = Sequential()
model.add(Dense(16, input_dim=len(features), activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(1, activation="sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    sample_set[features], sample_set[target_var], test_size=0.3
)

model.fit(X_train, y_train, epochs=50, batch_size=100)

# - Accuracy, Precision, Recall

from sklearn.metrics import accuracy_score, precision_score, recall_score

in_sample_preds = [round(x[0]) for x in model.predict(X_train)]
out_sample_preds = [round(x[0]) for x in model.predict(X_test)]

print("In-Sample Accuracy: %0.4f" % accuracy_score(y_train, in_sample_preds))
print("Out-of-Sample Accuracy: %0.4f" % accuracy_score(y_test, out_sample_preds))

print("\n")

print("In-Sample Precision: %0.4f" % precision_score(y_train, in_sample_preds))
print("Out-of-Sample Precision: %0.4f" % precision_score(y_test, out_sample_preds))

print("\n")

print("In-Sample Recall: %0.4f" % recall_score(y_train, in_sample_preds))
print("Out-of-Sample Recall: %0.4f" % recall_score(y_test, out_sample_preds))
"""
In-Sample Accuracy: 0.8143
Out-of-Sample Accuracy: 0.8028

In-Sample Precision: 0.6837
Out-of-Sample Precision: 0.6604

In-Sample Recall: 0.5684
Out-of-Sample Recall: 0.5099
"""

# - ROC & AUC

from sklearn.metrics import roc_curve, auc

in_sample_preds = [x[0] for x in model.predict(X_train)]
out_sample_preds = [x[0] for x in model.predict(X_test)]

in_sample_fpr, in_sample_tpr, in_sample_thresholds = roc_curve(y_train, in_sample_preds)
out_sample_fpr, out_sample_tpr, out_sample_thresholds = roc_curve(
    y_test, out_sample_preds
)

in_sample_roc_auc = auc(in_sample_fpr, in_sample_tpr)
out_sample_roc_auc = auc(out_sample_fpr, out_sample_tpr)

print("In-Sample AUC: %0.4f" % in_sample_roc_auc)
print("Out-Sample AUC: %0.4f" % out_sample_roc_auc)

# In-Sample AUC: 0.8659
# Out-Sample AUC: 0.8466

plt.figure(figsize=(10, 7))

plt.plot(
    out_sample_fpr,
    out_sample_tpr,
    color="darkorange",
    label="Out-Sample ROC curve (area = %0.4f)" % in_sample_roc_auc,
)
plt.plot(
    in_sample_fpr,
    in_sample_tpr,
    color="navy",
    label="In-Sample ROC curve (area = %0.4f)" % out_sample_roc_auc,
)
plt.plot([0, 1], [0, 1], color="gray", lw=1, linestyle="--")
plt.grid()
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend(loc="lower right")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = pd.read_excel("data/WA_Fn-UseC_-Marketing-Campaign-Eff-UseC_-FastF.xlsx")

# df.shape
# (548, 7)
# df.head(15)

# 2. Data Analysis
# - Total Sales

cc = df["SalesInThousands"].describe()
print(cc)

ax = (
    df.groupby("Promotion")
    .sum()["SalesInThousands"]
    .plot.pie(figsize=(7, 7), autopct="%1.0f%%")
)

ax.set_ylabel("")
ax.set_title("sales distribution across different promotions")

plt.show()

# - Market Size

cc = df.groupby("MarketSize").count()["MarketID"]
print(cc)

ax = (
    df.groupby(["Promotion", "MarketSize"])
    .count()["MarketID"]
    .unstack("MarketSize")
    .plot(
        kind="bar",
        figsize=(12, 10),
        grid=True,
    )
)

ax.set_ylabel("count")
ax.set_title("breakdowns of market sizes across different promotions")

plt.show()

ax = (
    df.groupby(["Promotion", "MarketSize"])
    .sum()["SalesInThousands"]
    .unstack("MarketSize")
    .plot(kind="bar", figsize=(12, 10), grid=True, stacked=True)
)

ax.set_ylabel("Sales (in Thousands)")
ax.set_title("breakdowns of market sizes across different promotions")

plt.show()

# - Store Age

cc = df["AgeOfStore"].describe()
print(cc)

ax = (
    df.groupby("AgeOfStore")
    .count()["MarketID"]
    .plot(kind="bar", color="skyblue", figsize=(10, 7), grid=True)
)

ax.set_xlabel("age")
ax.set_ylabel("count")
ax.set_title("overall distributions of age of store")

plt.show()

ax = (
    df.groupby(["AgeOfStore", "Promotion"])
    .count()["MarketID"]
    .unstack("Promotion")
    .iloc[::-1]
    .plot(kind="barh", figsize=(12, 15), grid=True)
)

ax.set_ylabel("age")
ax.set_xlabel("count")
ax.set_title("overall distributions of age of store")

plt.show()

cc = df.groupby("Promotion").describe()["AgeOfStore"]
print(cc)

# - Week Number

cc = df.groupby("Week").count()["MarketID"]
print(cc)

cc = df.groupby(["Promotion", "Week"]).count()["MarketID"]
print(cc)

ax1, ax2, ax3 = (
    df.groupby(["Week", "Promotion"])
    .count()["MarketID"]
    .unstack("Promotion")
    .plot.pie(subplots=True, figsize=(24, 8), autopct="%1.0f%%")
)

ax1.set_ylabel("Promotion #1")
ax2.set_ylabel("Promotion #2")
ax3.set_ylabel("Promotion #3")

ax1.set_xlabel("distribution across different weeks")
ax2.set_xlabel("distribution across different weeks")
ax3.set_xlabel("distribution across different weeks")

plt.show()

# 3. Statistical Significance

import numpy as np
from scipy import stats

# - t-test

means = df.groupby("Promotion").mean()["SalesInThousands"]
cc = means
print(cc)

stds = df.groupby("Promotion").std()["SalesInThousands"]
cc = stds
print(cc)

ns = df.groupby("Promotion").count()["SalesInThousands"]
cc = ns
print(cc)

# - Promotion 1 vs. 2

t_1_vs_2 = (means.iloc[0] - means.iloc[1]) / np.sqrt(
    (stds.iloc[0] ** 2 / ns.iloc[0]) + (stds.iloc[1] ** 2 / ns.iloc[1])
)

df_1_vs_1 = ns.iloc[0] + ns.iloc[1] - 2

p_1_vs_2 = (1 - stats.t.cdf(t_1_vs_2, df=df_1_vs_1)) * 2

cc = t_1_vs_2
print(cc)

# 6.427528670907475

cc = p_1_vs_2
print(cc)

# 4.143296816749853e-10

# - using scipy

t, p = stats.ttest_ind(
    df.loc[df["Promotion"] == 1, "SalesInThousands"].values,
    df.loc[df["Promotion"] == 2, "SalesInThousands"].values,
    equal_var=False,
)

print(t)

# 6.42752867090748

print(p)

# 4.2903687179871785e-10

# - Promotion 1 vs. 3

t_1_vs_3 = (means.iloc[0] - means.iloc[2]) / np.sqrt(
    (stds.iloc[0] ** 2 / ns.iloc[0]) + (stds.iloc[2] ** 2 / ns.iloc[2])
)

df_1_vs_3 = ns.iloc[0] + ns.iloc[1] - 2

p_1_vs_3 = (1 - stats.t.cdf(t_1_vs_3, df=df_1_vs_3)) * 2

cc = t_1_vs_3
print(cc)
# 1.5560224307759116

cc = p_1_vs_3
print(cc)
# 0.12058631176433687

# - using scipy

t, p = stats.ttest_ind(
    df.loc[df["Promotion"] == 1, "SalesInThousands"].values,
    df.loc[df["Promotion"] == 3, "SalesInThousands"].values,
    equal_var=False,
)
print(t)
# 1.5560224307758634

print(p)
# 0.12059147742229478

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


filename = "D:/_git/vcs/_big_files/Online Retail.xlsx"
