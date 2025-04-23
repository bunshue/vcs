"""
A_B_Testing



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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import datetime
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
from datetime import date, timedelta

pio.templates.default = "plotly_white"

control_data = pd.read_csv("data/control_group.csv", sep=";")
test_data = pd.read_csv("data/test_group.csv", sep=";")

print(control_data.head())

print(test_data.head())

print("------------------------------------------------------------")  # 60個

control_data.columns = [
    "Campaign Name",
    "Date",
    "Amount Spent",
    "Number of Impressions",
    "Reach",
    "Website Clicks",
    "Searches Received",
    "Content Viewed",
    "Added to Cart",
    "Purchases",
]

print(control_data.head())

test_data.columns = [
    "Campaign Name",
    "Date",
    "Amount Spent",
    "Number of Impressions",
    "Reach",
    "Website Clicks",
    "Searches Received",
    "Content Viewed",
    "Added to Cart",
    "Purchases",
]


print(control_data.isnull().sum())

control_data["Number of Impressions"].fillna(
    value=control_data["Number of Impressions"].mean(), inplace=True
)
control_data["Reach"].fillna(value=control_data["Reach"].mean(), inplace=True)
control_data["Website Clicks"].fillna(
    value=control_data["Website Clicks"].mean(), inplace=True
)
control_data["Searches Received"].fillna(
    value=control_data["Searches Received"].mean(), inplace=True
)
control_data["Content Viewed"].fillna(
    value=control_data["Content Viewed"].mean(), inplace=True
)
control_data["Added to Cart"].fillna(
    value=control_data["Added to Cart"].mean(), inplace=True
)
control_data["Purchases"].fillna(value=control_data["Purchases"].mean(), inplace=True)

print(test_data.isnull().sum())

ab_data = control_data.merge(test_data, how="outer").sort_values(["Date"])
print(ab_data.head())

ab_data = ab_data.reset_index(drop=True)
print(ab_data.head())

print(ab_data.isnull().sum())

print(ab_data["Campaign Name"].value_counts())

figure = px.scatter(
    data_frame=ab_data,
    x="Number of Impressions",
    y="Amount Spent",
    size="Amount Spent",
    color="Campaign Name",
    trendline="ols",
)
figure.show()

label = ["Total Searches from Control Campaign", "Total Searches from Test Campaign"]
counts = [sum(control_data["Searches Received"]), sum(test_data["Searches Received"])]
colors = ["gold", "lightgreen"]
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text="Control Vs Test: Searches")
fig.update_traces(
    hoverinfo="label+percent",
    textinfo="value",
    textfont_size=30,
    marker=dict(colors=colors, line=dict(color="black", width=3)),
)
fig.show()

label = ["Website Clicks from Control Campaign", "Website Clicks from Test Campaign"]
counts = [sum(control_data["Website Clicks"]), sum(test_data["Website Clicks"])]
colors = ["gold", "lightgreen"]
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text="Control Vs Test: Website Clicks")
fig.update_traces(
    hoverinfo="label+percent",
    textinfo="value",
    textfont_size=30,
    marker=dict(colors=colors, line=dict(color="black", width=3)),
)
fig.show()

label = ["Content Viewed from Control Campaign", "Content Viewed from Test Campaign"]
counts = [sum(control_data["Content Viewed"]), sum(test_data["Content Viewed"])]
colors = ["gold", "lightgreen"]
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text="Control Vs Test: Content Viewed")
fig.update_traces(
    hoverinfo="label+percent",
    textinfo="value",
    textfont_size=30,
    marker=dict(colors=colors, line=dict(color="black", width=3)),
)
fig.show()


label = [
    "Products Added to Cart from Control Campaign",
    "Products Added to Cart from Test Campaign",
]
counts = [sum(control_data["Added to Cart"]), sum(test_data["Added to Cart"])]
colors = ["gold", "lightgreen"]
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text="Control Vs Test: Added to Cart")
fig.update_traces(
    hoverinfo="label+percent",
    textinfo="value",
    textfont_size=30,
    marker=dict(colors=colors, line=dict(color="black", width=3)),
)
fig.show()

label = ["Amount Spent in Control Campaign", "Amount Spent in Test Campaign"]
counts = [sum(control_data["Amount Spent"]), sum(test_data["Amount Spent"])]
colors = ["gold", "lightgreen"]
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text="Control Vs Test: Amount Spent")
fig.update_traces(
    hoverinfo="label+percent",
    textinfo="value",
    textfont_size=30,
    marker=dict(colors=colors, line=dict(color="black", width=3)),
)
fig.show()

label = ["Purchases Made by Control Campaign", "Purchases Made by Test Campaign"]
counts = [sum(control_data["Purchases"]), sum(test_data["Purchases"])]
colors = ["gold", "lightgreen"]
fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text="Control Vs Test: Purchases")
fig.update_traces(
    hoverinfo="label+percent",
    textinfo="value",
    textfont_size=30,
    marker=dict(colors=colors, line=dict(color="black", width=3)),
)
fig.show()


figure = px.scatter(
    data_frame=ab_data,
    x="Content Viewed",
    y="Website Clicks",
    size="Website Clicks",
    color="Campaign Name",
    trendline="ols",
)
figure.show()


figure = px.scatter(
    data_frame=ab_data,
    x="Added to Cart",
    y="Content Viewed",
    size="Added to Cart",
    color="Campaign Name",
    trendline="ols",
)
figure.show()


figure = px.scatter(
    data_frame=ab_data,
    x="Purchases",
    y="Added to Cart",
    size="Purchases",
    color="Campaign Name",
    trendline="ols",
)
figure.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
