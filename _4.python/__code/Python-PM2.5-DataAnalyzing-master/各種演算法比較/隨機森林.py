"""
隨機森林

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

df = pd.read_excel("20160101-20190101(Daily)隨機森林.xlsx")
"""
cc = df.head(10)
print(cc)

#資料長度
print(len(df))
print(len(df["PM25"]))

cc = df.info()
print(cc)

cc = df.describe()
print(cc)
"""
# One-hot encode the data using pandas get_dummies
df = pd.get_dummies(df)

# Display the first 5 rows of the last 12 columns
cc = df.iloc[:, 5:].head(5)
print(cc)

# Labels are the values we want to predict
labels = np.array(df["PM25"])

# Remove the labels from the df
# axis 1 refers to the columns
df = df.drop("PM25", axis=1)

# Saving feature names for later use
feature_list = list(df.columns)

# Convert to numpy array
df = np.array(df)

# 將資料分成訓練組及測試組
from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)# 訓練組8成, 測試組2成
X_train, X_test, y_train, y_test = train_test_split(df, labels, test_size=0.25, random_state=42)# 訓練組7.5成, 測試組2.5成

print("Training Features Shape:", X_train.shape)
print("Training Labels Shape:", y_train.shape)
print("Testing Features Shape:", X_test.shape)
print("Testing Labels Shape:", y_test.shape)

# 載入隨機森林演算法，並訓練模型
from sklearn.ensemble import RandomForestRegressor

# Instantiate model with 1000 decision trees
random_forest_regressor = RandomForestRegressor(n_estimators=60, random_state=42)

# Train the model on training data
random_forest_regressor.fit(X_train, y_train)

# 進行預測

# Use the forest's predict method on the test data
predictions = random_forest_regressor.predict(X_test)

# Calculate the absolute errors
errors = abs(predictions - y_test)

# Print out the mean absolute error (mae)
print("MAE : Mean Absolute Error:", round(np.mean(errors), 2), "degrees.")

# Mean Absolute Error: 8.93 degrees.

# Get numerical feature importances
importances = list(random_forest_regressor.feature_importances_)

# List of tuples with variable and importance
feature_importances = [
    (feature, round(importance, 2))
    for feature, importance in zip(feature_list, importances)
]

# Sort the feature importances by most important first
feature_importances = sorted(feature_importances, key=lambda x: x[1], reverse=True)

# Print out the feature and importances
[print("Variable: {:20} Importance: {}".format(*pair)) for pair in feature_importances]

# Set the style
plt.style.use("fivethirtyeight")

# list of x locations for plotting
x_values = list(range(len(importances)))

# Make a bar chart
plt.bar(x_values, importances, orientation="vertical")

# Tick labels for x axis
plt.xticks(x_values, feature_list, rotation="vertical")

# Axis labels and title
plt.ylabel("Importance")
plt.xlabel("Variable")
plt.title("Variable Importances")

plt.show()


# 計算MAE

# New random forest with only the two most important variables
rf_most_important = RandomForestRegressor(n_estimators=1000, random_state=42)

# Extract the two most important df
important_indices = [feature_list.index("O3"), feature_list.index("TEMP")]
train_important = X_train[:, important_indices]
test_important = X_test[:, important_indices]

# Train the random forest
rf_most_important.fit(train_important, y_train)

# Make predictions and determine the error
predictions = rf_most_important.predict(test_important)

errors = abs(predictions - y_test)

# Display the performance metrics
print("MAE : Mean Absolute Error:", round(np.mean(errors), 2), "degrees.")
# Mean Absolute Error: 11.31 degrees.


# 建立小棵的決測樹
from sklearn.tree import export_graphviz
import pydot

# Limit depth of tree to 3 levels
rf_small = RandomForestRegressor(n_estimators=20, max_depth=3)
rf_small.fit(X_train, y_train)

# Extract the small tree
tree_small = rf_small.estimators_[5]

# Save the tree as a png image
export_graphviz(tree_small, out_file = 'small_tree222.dot', feature_names = feature_list, rounded = True, precision = 1)

(graph, ) = pydot.graph_from_dot_file('small_tree222.dot')

# NG
# graph.write_png('tmp_small_tree222.png');



from IPython.display import Image
from IPython.core.display import HTML

PATH = "small_tree222.png"
Image(filename=PATH, width=850, height=600)

# Use datetime for creating date objects for plotting
import datetime

# Dates of training values
months = df[:, feature_list.index("month")]
days = df[:, feature_list.index("day")]
years = df[:, feature_list.index("year")]

# List and then convert to datetime object
dates = [
    str(int(year)) + "-" + str(int(month)) + "-" + str(int(day))
    for year, month, day in zip(years, months, days)
]
dates = [datetime.datetime.strptime(date, "%Y-%m-%d") for date in dates]

# Dataframe with true values and dates
true_data = pd.DataFrame(data={"date": dates, "actual": labels})

# Dates of predictions
months = X_test[:, feature_list.index("month")]
days = X_test[:, feature_list.index("day")]
years = X_test[:, feature_list.index("year")]

# Column of dates
test_dates = [
    str(int(year)) + "-" + str(int(month)) + "-" + str(int(day))
    for year, month, day in zip(years, months, days)
]

# Convert to datetime objects
test_dates = [datetime.datetime.strptime(date, "%Y-%m-%d") for date in test_dates]

# Dataframe with predictions and dates
predictions_data = pd.DataFrame(data={"date": test_dates, "prediction": predictions})

# Plot the actual values
plt.plot(true_data["date"], true_data["actual"], "b-", label="actual")

# Plot the predicted values
plt.plot(
    predictions_data["date"], predictions_data["prediction"], "ro", label="prediction"
)
plt.xticks(rotation="60")
plt.legend()

# Graph labels
plt.xlabel("Date")
plt.ylabel("Maximum Temperature (F)")
plt.title("Actual and Predicted Values")

plt.show()

"""
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-17-e76cdb8cf408> in <module>
      3 
      4 # Dates of training values
----> 5 months = features[:, feature_list.index('month')]
      6 days = features[:, feature_list.index('day')]
      7 years = features[:, feature_list.index('year')]

ValueError: 'month' is not in list

 
"""

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
