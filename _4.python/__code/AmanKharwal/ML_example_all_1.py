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

"""
font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小
"""


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Best_Streaming_Service_Analysis

# TV Shows on Streaming Platforms
# TV shows on Netflix, Prime Video, Hulu and Disney+

import plotly
import plotly.express as px
from plotly.subplots import make_subplots

tv_shows = pd.read_csv("data/tv_shows.csv")
cc = tv_shows.head()
print(cc)

cc = tv_shows.info()
print(cc)

cc = tv_shows.describe()
print(cc)

tv_shows.drop_duplicates(subset="Title", keep="first", inplace=True)

tv_shows["Rotten Tomatoes"] = tv_shows["Rotten Tomatoes"].fillna("0%")
tv_shows["Rotten Tomatoes"] = tv_shows["Rotten Tomatoes"].apply(lambda x: x.rstrip("%"))
tv_shows["Rotten Tomatoes"] = pd.to_numeric(tv_shows["Rotten Tomatoes"])

tv_shows["IMDb"] = tv_shows["IMDb"].fillna(0)
tv_shows["IMDb"] = tv_shows["IMDb"] * 10
tv_shows["IMDb"] = tv_shows["IMDb"].astype("int")

tv_shows_long = pd.melt(
    tv_shows[["Title", "Netflix", "Hulu", "Disney+", "Prime Video"]],
    id_vars=["Title"],
    var_name="StreamingOn",
    value_name="Present",
)
tv_shows_long = tv_shows_long[tv_shows_long["Present"] == 1]
tv_shows_long.drop(columns=["Present"], inplace=True)

tv_shows_combined = tv_shows_long.merge(tv_shows, on="Title", how="inner")

tv_shows_combined.drop(
    columns=["Unnamed: 0", "Netflix", "Hulu", "Prime Video", "Disney+", "type"],
    inplace=True,
)

tv_shows_both_ratings = tv_shows_combined[
    (tv_shows_combined.IMDb > 0) & tv_shows_combined["Rotten Tomatoes"] > 0
]

tv_shows_combined.groupby("StreamingOn").Title.count().plot(kind="bar")
show()

figure = []
figure.append(
    px.violin(tv_shows_both_ratings, x="StreamingOn", y="IMDb", color="StreamingOn")
)
figure.append(
    px.violin(
        tv_shows_both_ratings, x="StreamingOn", y="Rotten Tomatoes", color="StreamingOn"
    )
)
fig = make_subplots(rows=2, cols=4, shared_yaxes=True)

for i in range(2):
    for j in range(4):
        fig.add_trace(figure[i]["data"][j], row=i + 1, col=j + 1)

fig.update_layout(autosize=False, width=800, height=800)
fig.show()

px.scatter(tv_shows_both_ratings, x="IMDb", y="Rotten Tomatoes", color="StreamingOn")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# House_Price_Prediction

housing = pd.read_csv("data/housing.csv")

cc = housing.head()
print(cc)

cc = housing.info()
print(cc)

cc = housing.ocean_proximity.value_counts()
print(cc)

cc = housing.describe()
print(cc)

housing.hist(bins=50, figsize=(10, 8))
show()

# 資料分割
train_set, test_set = train_test_split(housing, test_size=0.2)

housing["income_cat"] = pd.cut(
    housing["median_income"],
    bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],
    labels=[1, 2, 3, 4, 5],
)
housing["income_cat"].hist()
show()

# stratified sampling
from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]
print(strat_test_set["income_cat"].value_counts() / len(strat_test_set))

# removing the income_cat attribute to put data back to it's original form
for set_ in (strat_train_set, strat_test_set):
    set_.drop("income_cat", axis=1, inplace=True)

housing = strat_train_set.copy()
cc = housing.head()
print(cc)

# visualizing geographical data
housing.plot(
    kind="scatter",
    x="longitude",
    y="latitude",
    alpha=0.4,
    s=housing["population"] / 100,
    label="population",
    figsize=(12, 8),
    c="median_house_value",
    cmap=plt.get_cmap("jet"),
    colorbar=True,
)
plt.legend()
show()
"""
# looking at coorelation between features
corr_matrix = housing.corr()
print(corr_matrix.median_house_value.sort_values(ascending=False))
"""

from pandas.plotting import scatter_matrix

attributes = [
    "median_house_value",
    "median_income",
    "total_rooms",
    "housing_median_age",
]
scatter_matrix(housing[attributes], figsize=(12, 8))
show()

housing.plot(kind="scatter", x="median_income", y="median_house_value", alpha=0.1)
show()

housing["rooms_per_household"] = housing["total_rooms"] / housing["households"]
housing["bedrooms_per_room"] = housing["total_bedrooms"] / housing["total_rooms"]
housing["population_per_household"] = housing["population"] / housing["households"]

"""
corr_matrix = housing.corr()
print(corr_matrix["median_house_value"].sort_values(ascending=False))
"""

# Data Preparation
housing = strat_train_set.drop("median_house_value", axis=1)
housing_labels = strat_train_set["median_house_value"].copy()

median = housing["total_bedrooms"].median()
housing["total_bedrooms"].fillna(median, inplace=True)

housing_num = housing.drop("ocean_proximity", axis=1)

from sklearn.base import BaseEstimator
from sklearn.base import TransformerMixin

# column index
rooms_ix, bedrooms_ix, population_ix, households_ix = 3, 4, 5, 6


class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True):  # no *args or **kargs
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self  # nothing else to do

    def transform(self, X):
        rooms_per_household = X[:, rooms_ix] / X[:, households_ix]
        population_per_household = X[:, population_ix] / X[:, households_ix]
        if self.add_bedrooms_per_room:
            bedrooms_per_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[
                X, rooms_per_household, population_per_household, bedrooms_per_room
            ]
        else:
            return np.c_[X, rooms_per_household, population_per_household]


from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

num_pipeline = Pipeline(
    [
        ("imputer", SimpleImputer(strategy="median")),
        ("attribs_adder", CombinedAttributesAdder()),
        ("std_scaler", StandardScaler()),
    ]
)
housing_num_tr = num_pipeline.fit_transform(housing_num)

from sklearn.compose import ColumnTransformer

num_attribs = list(housing_num)
cat_attribs = ["ocean_proximity"]
full_pipeline = ColumnTransformer(
    [
        ("num", num_pipeline, num_attribs),
        ("cat", OneHotEncoder(), cat_attribs),
    ]
)
housing_prepared = full_pipeline.fit_transform(housing)

from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(housing_prepared, housing_labels)

data = housing.iloc[:5]
labels = housing_labels.iloc[:5]
data_preparation = full_pipeline.transform(data)
print("Predictions: ", lin_reg.predict(data_preparation))

"""
Predictions:  [210644.60459286 317768.80697211 210956.43331178  59218.98886849
 189747.55849879]
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Copy_of_RCB_vs_DC

deliveries_df = pd.read_csv("data/innings_deliveries.csv")

cc = deliveries_df.head()
print(cc)

cc = deliveries_df.describe(include="all")
print(cc)

sns.set_style("whitegrid")

# data preparation for run distribution per over
run_distribution = (
    deliveries_df.groupby(["team", "over"]).agg({"runs_total": "sum"}).reset_index()
)

# plotting run distribution per over for both teams
plt.figure(figsize=(14, 6))
sns.lineplot(data=run_distribution, x="over", y="runs_total", hue="team", marker="o")
plt.title("Run Distribution Per Over")
plt.xlabel("Over Number")
plt.ylabel("Runs Scored")
plt.xticks(range(0, 21))  # over numbers from 0 to 20
plt.legend(title="Team")
show()

# calculating top scorers for each team
top_scorers = (
    deliveries_df.groupby(["team", "batter"])
    .agg({"runs_batter": "sum"})
    .reset_index()
    .sort_values(by="runs_batter", ascending=False)
)

plt.figure(figsize=(14, 8))
sns.barplot(data=top_scorers, x="runs_batter", y="batter", hue="team", dodge=False)
plt.title("Top Scorers from Each Team")
plt.xlabel("Total Runs")
plt.ylabel("Batter")
plt.legend(title="Team", loc="center right")
show()

# preparing data for bowling analysis
deliveries_df["wickets_taken"] = deliveries_df["wicket_kind"].notna().astype(int)
bowling_stats = (
    deliveries_df.groupby(["team", "bowler"])
    .agg({"runs_total": "sum", "wickets_taken": "sum", "over": "nunique"})
    .reset_index()
)

# calculating economy rate (total runs conceded / number of overs bowled)
bowling_stats["economy_rate"] = bowling_stats["runs_total"] / bowling_stats["over"]

# sorting the data for better visualization
bowling_stats_sorted = bowling_stats.sort_values(by="wickets_taken", ascending=False)

# prepare the DataFrame for plotting
bowling_stats_sorted["wickets_taken"] = deliveries_df["wicket_kind"].notna().astype(int)
bowling_stats = (
    deliveries_df.groupby(["team", "bowler"])
    .agg({"runs_total": "sum", "wickets_taken": "sum", "over": "nunique"})
    .reset_index()
)
bowling_stats["economy_rate"] = bowling_stats["runs_total"] / bowling_stats["over"]
bowling_stats_sorted = bowling_stats.sort_values(by="wickets_taken", ascending=False)

# create the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Bar plot for wickets
sns.barplot(
    data=bowling_stats_sorted,
    x="bowler",
    y="wickets_taken",
    hue="team",
    ax=ax1,
    alpha=0.6,
)
ax1.set_ylabel("Wickets Taken")
ax1.set_xlabel("Bowler")
ax1.set_title("Bowling Analysis: Wickets and Economy Rate")
ax1.legend(title="Team", bbox_to_anchor=(1.05, 1), loc="upper left")

for item in ax1.get_xticklabels():
    item.set_rotation(45)

ax2 = ax1.twinx()
sns.lineplot(
    data=bowling_stats_sorted,
    x="bowler",
    y="economy_rate",
    marker="o",
    sort=False,
    ax=ax2,
    color="black",
)
ax2.set_ylabel("Economy Rate")

plt.tight_layout()
show()

# counting dismissal types
dismissal_types = deliveries_df["wicket_kind"].dropna().value_counts()

plt.figure(figsize=(8, 8))
plt.pie(
    dismissal_types,
    labels=dismissal_types.index,
    autopct="%1.1f%%",
    startangle=140,
    colors=sns.color_palette("Set2"),
)
plt.title("Types of Dismissals")
show()


# function to calculate partnerships
def calculate_partnerships(df):
    partnerships = []
    current_partnership = {}
    for i, row in df.iterrows():
        if i == 0 or (row["batter"] not in current_partnership.values()):
            if current_partnership:
                partnerships.append(current_partnership)
            current_partnership = {
                "team": row["team"],
                "batter1": row["batter"],
                "batter2": row["non_striker"],
                "runs": 0,
                "balls": 0,
            }
        current_partnership["runs"] += row["runs_total"]
        current_partnership["balls"] += 1
        if "player_out" in row and pd.notna(row["player_out"]):
            if (
                row["player_out"] == current_partnership["batter1"]
                or row["player_out"] == current_partnership["batter2"]
            ):
                partnerships.append(current_partnership)
                current_partnership = {}
    # append the last partnership if not ended by a wicket
    if current_partnership:
        partnerships.append(current_partnership)
    return partnerships


# calculate partnerships
partnerships_data = calculate_partnerships(deliveries_df)
partnerships_df = pd.DataFrame(partnerships_data)

# filter out significant partnerships (e.g., partnerships with more than 20 runs)
significant_partnerships = partnerships_df[partnerships_df["runs"] > 20]

# sort by highest runs
significant_partnerships = significant_partnerships.sort_values(
    by="runs", ascending=False
)

plt.figure(figsize=(12, 8))
sns.barplot(
    data=significant_partnerships, x="runs", y="batter1", hue="team", dodge=False
)
plt.title("Significant Batting Partnerships")
plt.xlabel("Runs Scored")
plt.ylabel("Batter 1 (Partnership Initiated)")
plt.legend(title="Team")
show()


# function to classify the phase of the game based on the over number
def classify_phase(over):
    if over < 6:
        return "Powerplay"
    elif over < 16:
        return "Middle"
    else:
        return "Death"


# adding phase information to the dataframe
deliveries_df["phase"] = deliveries_df["over"].apply(classify_phase)

# grouping data by phase and team to calculate runs and wickets
phase_analysis = (
    deliveries_df.groupby(["team", "phase"])
    .agg({"runs_total": "sum", "wickets_taken": "sum", "over": "count"})
    .rename(columns={"over": "balls"})
    .reset_index()
)

# calculating the run rate
phase_analysis["run_rate"] = (
    phase_analysis["runs_total"] / phase_analysis["balls"]
) * 6

# plotting the phase analysis
fig, ax1 = plt.subplots(figsize=(12, 8))

# bar plot for runs scored in each phase
sns.barplot(data=phase_analysis, x="phase", y="runs_total", hue="team", ax=ax1)
ax1.set_title("Phase Analysis: Runs and Wickets")
ax1.set_ylabel("Total Runs")
ax1.set_xlabel("Match Phase")

# line plot for wickets lost
ax2 = ax1.twinx()
sns.lineplot(
    data=phase_analysis,
    x="phase",
    y="wickets_taken",
    hue="team",
    marker="o",
    ax=ax2,
    legend=False,
)
ax2.set_ylabel("Wickets Lost")
show()

# calculate runs and balls faced for each batter
batter_stats = (
    deliveries_df.groupby("batter")
    .agg({"runs_batter": "sum", "over": "count"})
    .rename(columns={"over": "balls_faced"})
    .reset_index()
)

# calculate strike rate for each batter (runs per 100 balls)
batter_stats["strike_rate"] = (
    batter_stats["runs_batter"] / batter_stats["balls_faced"]
) * 100

# sorting batters by their strike rate
batter_stats_sorted = batter_stats.sort_values(by="strike_rate", ascending=False)

# displaying calculated strike rates along with runs scored and balls faced
cc = batter_stats_sorted.head(10)  # Display top 10 for brevity
print(cc)

# merging phase information with batter stats
batter_phase_stats = (
    deliveries_df.groupby(["batter", "phase"])
    .agg({"runs_batter": "sum", "over": "count"})
    .rename(columns={"over": "balls_faced"})
    .reset_index()
)

# calculate strike rate for each batter-phase combination
batter_phase_stats["strike_rate"] = (
    batter_phase_stats["runs_batter"] / batter_phase_stats["balls_faced"]
) * 100

# filtering for top performers based on overall strike rate
top_performers = batter_stats_sorted.head(5)["batter"]
batter_phase_stats_top = batter_phase_stats[
    batter_phase_stats["batter"].isin(top_performers)
]

# plotting strike rate across different phases for top performers
plt.figure(figsize=(10, 6))
sns.barplot(data=batter_phase_stats_top, x="batter", y="strike_rate", hue="phase")
plt.title("Strike Rate Across Different Phases for Top Performers")
plt.xlabel("Batter")
plt.ylabel("Strike Rate")
plt.legend(title="Match Phase")
show()

# calculate cumulative runs and wickets for each ball for both teams
deliveries_df["cumulative_runs"] = deliveries_df.groupby("team")["runs_total"].cumsum()
deliveries_df["cumulative_wickets"] = deliveries_df.groupby("team")[
    "wickets_taken"
].cumsum()

# separate data for both teams
rcb_deliveries = deliveries_df[deliveries_df["team"] == "Royal Challengers Bengaluru"]
dc_deliveries = deliveries_df[deliveries_df["team"] == "Delhi Capitals"]

# calculating overs for cumulative analysis
rcb_deliveries["over_ball"] = (
    rcb_deliveries["over"] + (rcb_deliveries.groupby("over").cumcount() + 1) / 6
)
dc_deliveries["over_ball"] = (
    dc_deliveries["over"] + (dc_deliveries.groupby("over").cumcount() + 1) / 6
)

# plotting cumulative run rates and wickets
fig, ax = plt.subplots(figsize=(14, 8))

# plot for RCB
ax.plot(
    rcb_deliveries["over_ball"],
    rcb_deliveries["cumulative_runs"],
    color="blue",
    label="RCB Runs",
)
ax.scatter(
    rcb_deliveries[rcb_deliveries["wickets_taken"] == 1]["over_ball"],
    rcb_deliveries[rcb_deliveries["wickets_taken"] == 1]["cumulative_runs"],
    color="blue",
    marker="X",
    s=100,
)

# plot for DC
ax.plot(
    dc_deliveries["over_ball"],
    dc_deliveries["cumulative_runs"],
    color="red",
    label="DC Runs",
)
ax.scatter(
    dc_deliveries[dc_deliveries["wickets_taken"] == 1]["over_ball"],
    dc_deliveries[dc_deliveries["wickets_taken"] == 1]["cumulative_runs"],
    color="red",
    marker="X",
    s=100,
)

ax.set_title("Cumulative Runs with Wickets for RCB and DC")
ax.set_xlabel("Over")
ax.set_ylabel("Cumulative Runs")
ax.legend()
show()

# calculate runs and wickets per over for both teams
per_over_stats = (
    deliveries_df.groupby(["team", "over"])
    .agg({"runs_total": "sum", "wickets_taken": "sum"})
    .reset_index()
)

# calculate run rate for each over
per_over_stats["run_rate"] = (
    per_over_stats["runs_total"] / 6
)  # Runs per over to runs per ball (standard rate)

# separate data for RCB and DC for plotting
rcb_per_over_stats = per_over_stats[
    per_over_stats["team"] == "Royal Challengers Bengaluru"
]
dc_per_over_stats = per_over_stats[per_over_stats["team"] == "Delhi Capitals"]

# plotting run rates and marking wickets for each team
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8), sharex=True)

# RCB
ax1.plot(
    rcb_per_over_stats["over"],
    rcb_per_over_stats["run_rate"],
    marker="o",
    color="blue",
    label="RCB Run Rate",
)
ax1.scatter(
    rcb_per_over_stats[rcb_per_over_stats["wickets_taken"] > 0]["over"],
    rcb_per_over_stats[rcb_per_over_stats["wickets_taken"] > 0]["run_rate"],
    color="red",
    s=100,
    label="Wickets",
)
ax1.set_title("RCB Run Rate Per Over")
ax1.set_ylabel("Run Rate (Runs per ball)")
ax1.legend()

# DC
ax2.plot(
    dc_per_over_stats["over"],
    dc_per_over_stats["run_rate"],
    marker="o",
    color="red",
    label="DC Run Rate",
)
ax2.scatter(
    dc_per_over_stats[dc_per_over_stats["wickets_taken"] > 0]["over"],
    dc_per_over_stats[dc_per_over_stats["wickets_taken"] > 0]["run_rate"],
    color="blue",
    s=100,
    label="Wickets",
)
ax2.set_title("DC Run Rate Per Over")
ax2.set_xlabel("Over")
ax2.set_ylabel("Run Rate (Runs per ball)")
ax2.legend()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


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
