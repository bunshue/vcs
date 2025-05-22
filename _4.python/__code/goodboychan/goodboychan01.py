"""
goodboychan


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

from sklearn import datasets
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.linear_model import LinearRegression


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

df = pd.read_csv("./data/winequality-red.csv", sep=";")
cc = df.head()
print(cc)

new_df = df.rename(
    columns={
        "fixed acidity": "fixed_acidity",
        "volatile acidity": "volatile_acidity",
        "citric acid": "citric_acid",
        "residual sugar": "residual_sugar",
        "free sulfur dioxide": "free_sulfur_dioxide",
        "total sulfur dioxide": "total_sulfur_dioxide",
    }
)
cc = new_df.head()
print(cc)


def replace_labels(columns):
    labels = list(columns)

    for i in range(len(labels)):
        labels[i] = labels[i].replace(" ", "_")
    return labels


df.columns = replace_labels(df.columns)

cc = df.head()
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = pd.read_csv("./data/iris.csv")
renamed_columns = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
    "species",
]
df.columns = renamed_columns
versicolor_petal_length = df[df["species"] == "Versicolor"]["petal length (cm)"]
setosa_petal_length = df[df["species"] == "Setosa"]["petal length (cm)"]
virginica_petal_length = df[df["species"] == "Virginica"]["petal length (cm)"]


# Create bee swarm plot with Seaborn's default settings
_ = sns.swarmplot(x="species", y="petal length (cm)", data=df)

# Label the axes
_ = plt.xlabel("species")
_ = plt.ylabel("petal length (cm)")

show()

# Create box plot with Seaborn`s default settings
_ = sns.boxplot(x="species", y="petal length (cm)", data=df)

# Label the axes
_ = plt.xlabel("species")
_ = plt.ylabel("petal length (cm)")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = pd.read_csv("./data/frog_tongue.csv", skiprows=14)
df.head()

# Make bee swarm plot
_ = sns.swarmplot(x="ID", y="impact force (mN)", data=df)

# Label axes
_ = plt.xlabel("frog")
_ = plt.ylabel("impact force (mN)")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

sns.set()

# Draw 100000 samples from Normal distribution
# with stds of interest: samples_std1, samples_std3, stamples_std10
samples_std1 = np.random.normal(20, 1, 100000)
samples_std3 = np.random.normal(20, 3, 100000)
samples_std10 = np.random.normal(20, 10, 100000)

# Make histograms
_ = plt.hist(samples_std1, histtype="step", density=True, bins=100)
_ = plt.hist(samples_std3, histtype="step", density=True, bins=100)
_ = plt.hist(samples_std10, histtype="step", density=True, bins=100)

# Make a legend, set limits
_ = plt.legend(("std = 1", "std = 3", "std = 10"))
plt.ylim(-0.01, 0.42)


show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def successive_poisson(tau1, tau2, size=1):
    """Compute time for arrival of 2 successive Poisson processes."""
    # Draw samples out of first exponential distribution: t1
    t1 = np.random.exponential(tau1, size)

    # Draw samples out of second exponential distribution: t2
    t2 = np.random.exponential(tau2, size)

    return t1 + t2


# Draw samples of waiting times: waiting_times
waiting_times = successive_poisson(764, 715, size=100000)

# Make the histogram
_ = plt.hist(waiting_times, bins=100, density=True, histtype="step")

# Label axes
_ = plt.xlabel("waiting times")
_ = plt.ylabel("PDF")


show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = pd.read_csv("./data/female_literacy_fertility.csv")
fertility = np.array(df["fertility"])
illiteracy = np.array(100 - df["female literacy"])


# Plot the illiteracy rate versus fertility
_ = plt.plot(illiteracy, fertility, marker=".", linestyle="none")

# Set the margins and label axes
plt.margins(0.02)
_ = plt.xlabel("percent illiterate")
_ = plt.ylabel("fertility")

# Show the Pearson correlation coefficient
# xxx print(pearson_r(illiteracy, fertility))


# Plot the illiteracy rate versus fertility
_ = plt.plot(illiteracy, fertility, marker=".", linestyle="none")
plt.margins(0.02)
_ = plt.xlabel("percent illiterate")
_ = plt.ylabel("fertility")

# Perform a linear regression using np.polyfit(): a, b
a, b = np.polyfit(illiteracy, fertility, deg=1)

# Print the results to the screen
print("slope =", a, "children per woman / percent illiterate")
print("intercept =", b, "children per woman")

# Make theoretical line to plot
x = np.array([0, 100])
y = a * x + b

# Add regression line to your plot
_ = plt.plot(x, y)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = pd.read_csv("./data/anscombe.csv")
x = np.array(df.iloc[1:, 1].astype("float"))
y = np.array(df.iloc[1:, 2].astype("float"))

# Perform linear regression: a, b
a, b = np.polyfit(x, y, deg=1)

# Print the slope and intercept
print(a, b)

# Generate theoretical x and y data: x_theor, y_theor
x_theor = np.array([3, 15])
y_theor = a * x_theor + b

# Plot the Anscombe data and theoretical line
_ = plt.plot(x, y, marker=".", linestyle="none")
_ = plt.plot(x_theor, y_theor)

# Label the axes
plt.xlabel("x")
plt.ylabel("y")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df_1 = pd.read_csv("./data/finch_beaks_1975.csv")
df_2 = pd.read_csv("./data/finch_beaks_2012.csv")

df_1["year"] = 1975
df_2["year"] = 2012

df_1.columns = ["band", "species", "beak_length", "beak_depth", "year"]
df_2.columns = ["band", "species", "beak_length", "beak_depth", "year"]

df = pd.concat([df_1, df_2])
df.head()


# Create bee swarm plot
_ = sns.swarmplot(x="year", y="beak_depth", data=df)

# Label the axes
_ = plt.xlabel("year")
_ = plt.ylabel("beak depth (mm)")

show()


def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n + 1) / n

    return x, y


bd_1975 = np.array(
    df[(df["year"] == 1975) & (df["species"] == "scandens")]["beak_depth"]
)
bd_2012 = np.array(
    df[(df["year"] == 2012) & (df["species"] == "scandens")]["beak_depth"]
)

# Compute ECDFs
x_1975, y_1975 = ecdf(bd_1975)
x_2012, y_2012 = ecdf(bd_2012)

# Plot the ECDFs
_ = plt.plot(x_1975, y_1975, marker=".", linestyle="none")
_ = plt.plot(x_2012, y_2012, marker=".", linestyle="none")

# Set margins
plt.margins(0.02)

# Add axis labels and legend
_ = plt.xlabel("beak depth (mm)")
_ = plt.ylabel("ECDF")
_ = plt.legend(("1975", "2012"), loc="lower right")

show()

bl_1975 = np.array(
    df[(df["year"] == 1975) & (df["species"] == "scandens")]["beak_length"]
)
bl_2012 = np.array(
    df[(df["year"] == 2012) & (df["species"] == "scandens")]["beak_length"]
)

# Make scatter plot of 1975 data
_ = plt.plot(bl_1975, bd_1975, marker=".", linestyle="None", color="blue", alpha=0.5)

# Make scatter plot of 2012 data
_ = plt.plot(bl_2012, bd_2012, marker=".", linestyle="None", color="red", alpha=0.5)

# Label axes and make legend
_ = plt.xlabel("beak length (mm)")
_ = plt.ylabel("beak depth (mm)")
_ = plt.legend(("1975", "2012"), loc="upper left")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = pd.read_csv("./data/house-votes-84.csv", header=None)
df.columns = [
    "party",
    "infants",
    "water",
    "budget",
    "physician",
    "salvador",
    "religious",
    "satellite",
    "aid",
    "missile",
    "immigration",
    "synfuels",
    "education",
    "superfund",
    "crime",
    "duty_free_exports",
    "eaa_rsa",
]
df.replace({"?": "n"}, inplace=True)
df.replace({"n": 0, "y": 1}, inplace=True)
df.head()

plt.figure(figsize=(5, 5))
sns.countplot(x="education", hue="party", data=df, palette="RdBu")
plt.xticks([0, 1], ["No", "Yes"])

show()

plt.figure(figsize=(5, 5))
sns.countplot(x="satellite", hue="party", data=df, palette="RdBu")
plt.xticks([0, 1], ["No", "Yes"])
show()

plt.figure(figsize=(5, 5))
sns.countplot(x="missile", hue="party", data=df, palette="RdBu")
plt.xticks([0, 1], ["No", "Yes"])
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Load the digits dataset: digits
digits = datasets.load_digits()

# Print the keys and DESCR of the dataset
print(digits.keys())
print(digits["DESCR"])

# Print the shape of the images and data keys
print(digits.images.shape)
print(digits.data.shape)

# Display digit 1010
plt.imshow(digits.images[1010], cmap=plt.cm.gray_r, interpolation="nearest")

show()

from sklearn.neighbors import KNeighborsClassifier

# Create feature and target arrays
X = digits.data
y = digits.target

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=9487, stratify=y
)

# Create a k-NN classifier with 7 neighbors: knn
knn = KNeighborsClassifier(n_neighbors=7)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Print the accuracy
print(knn.score(X_test, y_test))

# Setup arrays to store train and test accuracies
neighbors = np.arange(1, 9)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

# Loop over different values of k
for i, k in enumerate(neighbors):
    # Setup a k-NN Classifier with k neighbors: knn
    knn = KNeighborsClassifier(n_neighbors=k)

    # Fit the classifier to the training data
    knn.fit(X_train, y_train)

    # Compute accuracy on the training set
    train_accuracy[i] = knn.score(X_train, y_train)

    # Compute accuracy on the testing set
    test_accuracy[i] = knn.score(X_test, y_test)

# Generate plot
plt.title("k-NN: Varying Number of Neighbors")
plt.plot(neighbors, test_accuracy, label="Testing Accuracy")
plt.plot(neighbors, train_accuracy, label="Training Accuracy")
plt.legend()
plt.xlabel("Number of Neighbors")
plt.ylabel("Accuracy")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Read the CSV file into a DataFrame: df
df = pd.read_csv("./data/gm_2008_region.csv")
df.drop(labels=["Region"], axis="columns", inplace=True)

# Create arrays for features and target variable
y = df["life"].values
X = df["fertility"].values

# Print the dimensions of X and y before reshaping
print("Dimensions of y before reshaping: {}".format(y.shape))
print("Dimensions of X before reshaping: {}".format(X.shape))

# Reshape X and y
y = y.reshape(-1, 1)
X = X.reshape(-1, 1)

# Print the dimensions of X and y after reshaping
print("Dimensions of y after reshaping: {}".format(y.shape))
print("Dimensions of X after reshaping: {}".format(X.shape))

sns.heatmap(df.corr(), square=True, cmap="RdYlGn")
show()

X_fertility = df["fertility"].values.reshape(-1, 1)
y = df["life"].values.reshape(-1, 1)

sns.scatterplot(x="fertility", y="life", data=df)
show()

from sklearn.linear_model import LinearRegression

# Create the regressor: reg
reg = LinearRegression()

# Create th prediction space
prediction_space = np.linspace(min(X_fertility), max(X_fertility)).reshape(-1, 1)

# Fit the model to the data
reg.fit(X_fertility, y)

# compute predictions over the prediction space: y_pred
y_pred = reg.predict(prediction_space)

# Print $R^2$
print(reg.score(X_fertility, y))

# Plot regression line on scatter plot
sns.scatterplot(x="fertility", y="life", data=df)
plt.plot(prediction_space, y_pred, color="black", linewidth=3)
show()

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=9487
)

# Create the regressor: reg_all
reg_all = LinearRegression()

# Fit the regressor to the training data
reg_all.fit(X_train, y_train)

# Predict on the test data: y_pred
y_pred = reg_all.predict(X_test)

# compute and print R^2 and RMSE
print("R^2: {}".format(reg_all.score(X_test, y_test)))
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error: {}".format(rmse))

# 5-fold cross-validation

from sklearn.model_selection import cross_val_score

# Create a linear regression object: reg
reg = LinearRegression()

# Compute 5-fold cross-validation scores: cv_scores
cv_scores = cross_val_score(reg, X, y, cv=5)

# Print the 5-fold cross-validation scores
print(cv_scores)

print("Average 5-Fold CV Score: {}".format(np.mean(cv_scores)))

# K-Fold CV comparison


# Create a linear regression object: reg
reg = LinearRegression()

# Perform 3-fold CV
#    %timeit cross_val_score(reg, X, y, cv=3)
cvscores_3 = cross_val_score(reg, X, y, cv=3)
print(np.mean(cvscores_3))

# Perform 10-fold CV
#     %timeit cross_val_score(reg, X, y, cv=10)
cvscores_10 = cross_val_score(reg, X, y, cv=10)
print(np.mean(cvscores_10))

# Regularized regression
# Regularization I: Lasso
X = df.drop("life", axis="columns").values
y = df["life"].values

from sklearn.linear_model import Lasso

# Instantiate a lasso regressor: lasso
lasso = Lasso(alpha=0.4)

# Fit the regressor to the data
lasso.fit(X, y)

# Compute and print the coefficients
lasso_coef = lasso.coef_
print(lasso_coef)

# Plot the coefficients
df_columns = df.columns[:-1]
plt.plot(range(len(df_columns)), lasso_coef)
plt.xticks(range(len(df_columns)), df_columns.values, rotation=60)
plt.margins(0.02)


show()

# Regularization II: Ridge


def display_plot(cv_scores, cv_scores_std):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(alpha_space, cv_scores)

    std_error = cv_scores_std / np.sqrt(10)

    ax.fill_between(
        alpha_space, cv_scores + std_error, cv_scores - std_error, alpha=0.2
    )
    ax.set_ylabel("CV Score +/- Std Error")
    ax.set_xlabel("Alpha")
    ax.axhline(np.max(cv_scores), linestyle="--", color=".5")
    ax.set_xlim([alpha_space[0], alpha_space[-1]])
    ax.set_xscale("log")


from sklearn.linear_model import Ridge

# Setup the array of alphas and lists to store scores
alpha_space = np.logspace(-4, 0, 50)
ridge_scores = []
ridge_scores_std = []

# Create a ridge regressor: ridge
ridge = Ridge()

# Compute scores over range of alphas
for alpha in alpha_space:
    # Specify the alpha value to use: ridge.alhpa
    ridge.alpha = alpha

    # Perform 10-fold CV: ridge_cv_scores
    ridge_cv_scores = cross_val_score(ridge, X, y, cv=10)

    # Append the mean of ridge_cv_scores to ridge_scores
    ridge_scores.append(np.mean(ridge_cv_scores))

    # Append the std of ridge_cv_scores to ridge_scores_std
    ridge_scores_std.append(np.std(ridge_cv_scores))

# Display the plot
display_plot(ridge_scores, ridge_scores_std)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = pd.read_csv("./data/diabetes.csv")
df.head()

# pregnancies glucose diastolic triceps  insulin bmi dpf age  diabetes
# 妊娠        葡萄糖  舒張期    肱三頭肌 胰島素  BMI DPF 年齡 糖尿病
# 懷孕        葡萄糖  舒張      三頭肌   胰島素 	BMI DPF 年齡 糖尿病

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=9487
)

# Instantiate a k-NN classifier: knn
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Predict the labels of the test data: y_pred
y_pred = knn.predict(X_test)

# Generate the confusion matrix and classification report
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Logistic regression and the ROC curve

from sklearn.linear_model import LogisticRegression

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=9487
)

# Create the classifier: logreg
logreg = LogisticRegression(max_iter=1000)

# Fit the classifier to the training data
logreg.fit(X_train, y_train)

# Predict the labels of the test set: y_pred
y_pred = logreg.predict(X_test)

# Compute and print the confusion matrix and classification report
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

from sklearn.metrics import roc_curve

# Compute predicted probabilities: y_pred_prob
y_pred_prob = logreg.predict_proba(X_test)[:, 1]

# Generate ROC curve values: fpr, tpr, thresholds
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

# Plot ROC curve
plt.plot([0, 1], [0, 1], "k--")
plt.plot(fpr, tpr)
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
show()

# Precision-recall Curve

from sklearn.metrics import precision_recall_curve

precision, recall, thresholds = precision_recall_curve(y_test, y_pred_prob)

plt.plot(recall, precision)
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision / Recall plot")

show()

# Area under the ROC curve (AUC)
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import cross_val_score

# Compute predicted probabilites: y_pred_prob
y_pred_prob = logreg.predict_proba(X_test)[:, 1]

# Compute and print AUC score
print("AUC: {}".format(roc_auc_score(y_test, y_pred_prob)))

# Compute cross-validated AUC scores: cv_auc
cv_auc = cross_val_score(logreg, X, y, cv=5, scoring="roc_auc")

# Print list of AUC scores
print("AUC scores computed using 5-fold cross-validation: {}".format(cv_auc))

# Hyperparameter tuning
# Hyperparameter tuning with GridSearchCV

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

# Setup the hyperparameter grid
c_space = np.logspace(-5, 8, 15)
param_grid = {"C": c_space}

# Instantiate a logistic regression classifier: logreg
logreg = LogisticRegression(max_iter=1000)

# Instantiate the GridSearchCV object: logreg_cv
logreg_cv = GridSearchCV(logreg, param_grid, cv=5)

# Fit it to the data
logreg_cv.fit(X, y)

# Print the tuned parameters and score
print("Tuned Logistic Regression Parameters: {}".format(logreg_cv.best_params_))
print("Best score is {}".format(logreg_cv.best_score_))

# Hyperparameter tuning with RandomizedSearchCV

from scipy.stats import randint
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import RandomizedSearchCV

# Setup the parameters and distributions to sample from: param_dist
param_dist = {
    "max_depth": [3, None],
    "max_features": randint(1, 9),
    "min_samples_leaf": randint(1, 9),
    "criterion": ["gini", "entropy"],
}

# Instantiate a Decision Tree classifier: tree
tree = DecisionTreeClassifier()

# Instantiate the RandomizedSearchCV object: tree_cv
tree_cv = RandomizedSearchCV(tree, param_dist, cv=5)

# Fit it to the data
tree_cv.fit(X, y)

# Print the tuned parameters and score
print("Tuned Decision Tree Parameters: {}".format(tree_cv.best_params_))
print("Best score is {}".format(tree_cv.best_score_))

from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression

# Create the hyperparameter grid
c_space = np.logspace(-5, 8, 15)
param_grid = {"C": c_space, "penalty": ["l1", "l2"]}

# Instantiate the logistic regression classifier: logreg
logreg = LogisticRegression(max_iter=1000, solver="liblinear")

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=9487
)

# Instantiate the GridSearchCV object: logreg_cv
logreg_cv = GridSearchCV(logreg, param_grid, cv=5)

# Fit it to the training data
logreg_cv.fit(X_train, y_train)

# Print the optimal parameters and best score
print("Tuned Logistic Regression Parameter: {}".format(logreg_cv.best_params_))
print("Tuned Logistic Regression Accuracy: {}".format(logreg_cv.best_score_))


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = pd.read_csv("./data/gm_2008_region.csv")
df.drop(labels=["Region"], axis="columns", inplace=True)
df.head()

X = df.drop("life", axis="columns").values
y = df["life"].values

from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=9487
)

# Create the hyperparameter grid
l1_space = np.linspace(0, 1, 30)
param_grid = {"l1_ratio": l1_space}

# Instantiate the ElasticNet regressor: elastic_net
elastic_net = ElasticNet(max_iter=100000, tol=0.001)

# Setup the GridSearchCV object: gm_cv
gm_cv = GridSearchCV(elastic_net, param_grid, cv=5)

# Fit it to the training data
gm_cv.fit(X_train, y_train)

# Predict on the test set and compute metrics
y_pred = gm_cv.predict(X_test)
r2 = gm_cv.score(X_test, y_test)
mse = mean_squared_error(y_pred, y_test)
print("Tuned ElasticNet l1 ratio: {}".format(gm_cv.best_params_))
print("Tuned ElasticNet R squared: {}".format(r2))
print("Tuned ElasticNet MSE: {}".format(mse))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Preprocessing and pipelines

df = pd.read_csv("./data/gm_2008_region.csv")
df.head()

# Create a boxplot of life expectancy per region
df.boxplot("life", "Region", rot=60)
show()

# Creating dummy variables

df.columns

# Create dummy variables: df_region
df_region = pd.get_dummies(df)

# Print the columns of df_regions
print(df_region.columns)

# Create dummy variables with drop_first=True: df_region
df_region = pd.get_dummies(df, drop_first=True)

# Print the new columns of df_region
print(df_region.columns)

# Regression with categorical features

X = df_region.drop("life", axis="columns")
y = df_region["life"]

from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score

# Instantiate a ridge regressor: ridge
ridge = Ridge(alpha=0.5)

# Perform 5-fold cross-validation: ridge_cv
ridge_cv = cross_val_score(ridge, X, y, cv=5)

# Print the cross-validated scores
print(ridge_cv)

# [0.86808336 0.80623545 0.84004203 0.7754344  0.87503712]

# Handling missing data

# Dropping missing data

# Preprocess

df = pd.read_csv("./data/house-votes-84.csv", header=None)
df.columns = [
    "party",
    "infants",
    "water",
    "budget",
    "physician",
    "salvador",
    "religious",
    "satellite",
    "aid",
    "missile",
    "immigration",
    "synfuels",
    "education",
    "superfund",
    "crime",
    "duty_free_exports",
    "eaa_rsa",
]
df.replace({"n": 0, "y": 1}, inplace=True)
df.head()

# Convert '?' to NaN
df[df == "?"] = np.nan

# Print the number of NaNs
print(df.isnull().sum())

# Print shape of original DataFrame
print("Shape of Original DataFrame: {}".format(df.shape))

# Drop missing values and print shape fo new DataFrame
df = df.dropna()

# Print shape of new DataFrame
print(
    "Shape of DataFrame After Dropping All Rows with Missing Values: {}".format(
        df.shape
    )
)

# Imputing missing data in a ML Pipeline I

from sklearn.impute import SimpleImputer
from sklearn.svm import SVC

# Setup the Imputation transformer: imp
imp = SimpleImputer(missing_values=np.nan, strategy="most_frequent")

# Instantiate the SVC classifier: clf
clf = SVC()

# Setup the pipeline with the required steps: steps
steps = [("imputation", imp), ("SVM", clf)]

# Imputing missing data in a ML Pipeline II

X = df.drop("party", axis="columns")
y = df["party"]

from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline

# Setup the pipeline steps: steps
steps = [
    ("imputation", SimpleImputer(missing_values=np.nan, strategy="most_frequent")),
    ("SVM", SVC()),
]

# Create the pipeline: pipeline
pipeline = Pipeline(steps)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=9487
)

# Fit the pipeline to the train set
pipeline.fit(X_train, y_train)

# Predict the labels of the test set
y_pred = pipeline.predict(X_test)

# Compute metrics
print(classification_report(y_test, y_pred))

# Centering and scaling

# Centering and scaling your data

# You will now explore scaling for yourself on a new dataset - White Wine Quality! Hugo used the Red Wine Quality dataset in the video. We have used the 'quality' feature of the wine to create a binary target variable: If 'quality' is less than 5, the target variable is 1, and otherwise, it is 0.

df = pd.read_csv("./data/winequality-white.csv", sep=";")
cc = df.head()
print(cc)

df["quality"] = df["quality"] < 5
X = df.drop("quality", axis="columns").values
y = df["quality"].values
cc = df.head()
print(cc)

from sklearn.preprocessing import scale

# Scale the features: X_scaled
X_scaled = scale(X)

# Print the mean and standard deviation of the unscaled features
print("Mean of Unscaled Features: {}".format(np.mean(X)))
print("Standard Deviation of Unscaled Features: {}".format(np.std(X)))

# Print the mean and standard deviation of the scaled features
print("Mean of Scaled Features: {}".format(np.mean(X_scaled)))
print("Standard Deviation of Scaled Features: {}".format(np.std(X_scaled)))

# Centering and scaling in a pipeline

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier

# Setup the pipeline steps: steps
steps = [("scaler", StandardScaler()), ("knn", KNeighborsClassifier())]

# Create the pipeline: pipeline
pipeline = Pipeline(steps)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=9487
)

# Fit the pipeline to the training set: knn_scaled
knn_scaled = pipeline.fit(X_train, y_train)

# Instantiate and fit a k-NN classifier to the unscaled data
knn_unscaled = KNeighborsClassifier().fit(X_train, y_train)

# Compute and print metrics
print("Accuracy with Scaling: {}".format(knn_scaled.score(X_test, y_test)))
print("Accuracy without Scaling: {}".format(knn_unscaled.score(X_test, y_test)))

# Bringing it all together I: Pipeline for classification

from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Setup the pipeline
steps = [("scaler", StandardScaler()), ("SVM", SVC())]

pipeline = Pipeline(steps)

# Specify the hyperparameter space
parameters = {"SVM__C": [1, 10, 100], "SVM__gamma": [0.1, 0.01]}

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=9487
)

# Instantiate the GridSearchCV object: cv
cv = GridSearchCV(pipeline, param_grid=parameters, cv=3)

# Fit to the training set
cv.fit(X_train, y_train)

# Predict the labels of the test set: y_pred
y_pred = cv.predict(X_test)

# Compute and print metrics
print("Accuracy: {}".format(cv.score(X_test, y_test)))
print(classification_report(y_test, y_pred))
print("Tuned Model Parameters: {}".format(cv.best_params_))

# Bringing it all together II: Pipeline for regression

df = pd.read_csv("./data/gm_2008_region.csv")
cc = df.head()
print(cc)

df.drop(["Region"], axis="columns", inplace=True)
X = df.drop("life", axis="columns").values
y = df["life"].values

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import ElasticNet
from sklearn.pipeline import Pipeline

# Setup the pipeline steps: steps
steps = [
    ("imputation", SimpleImputer(missing_values=np.nan, strategy="mean")),
    ("scaler", StandardScaler()),
    ("elasticnet", ElasticNet(tol=0.6)),
]

# Create the pipeline: pipeline
pipeline = Pipeline(steps)

# Specify the hyperparameter space
parameters = {"elasticnet__l1_ratio": np.linspace(0, 1, 30)}

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=9487
)

# Create the GridSearchCV object: gm_cv
gm_cv = GridSearchCV(pipeline, param_grid=parameters, cv=3)

# Fit to the training set
gm_cv.fit(X_train, y_train)

# Compute and print the metrics
r2 = gm_cv.score(X_test, y_test)
print("Tuned ElasticNet Alpha: {}".format(gm_cv.best_params_))
print("Tuned ElasticNet R squared: {}".format(r2))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Clustering for dataset exploration

points = np.array(
    [
        [0.06544649, -0.76866376],
        [-1.52901547, -0.42953079],
        [1.70993371, 0.69885253],
        [1.16779145, 1.01262638],
        [-1.80110088, -0.31861296],
        [-1.63567888, -0.02859535],
        [1.21990375, 0.74643463],
        [-0.26175155, -0.62492939],
        [-1.61925804, -0.47983949],
        [-1.84329582, -0.16694431],
        [1.35999602, 0.94995827],
        [0.42291856, -0.7349534],
        [-1.68576139, 0.10686728],
        [0.90629995, 1.09105162],
        [-1.56478322, -0.84675394],
        [-0.0257849, -1.18672539],
        [0.83027324, 1.14504612],
        [1.22450432, 1.35066759],
        [-0.15394596, -0.71704301],
        [0.86358809, 1.06824613],
        [-1.43386366, -0.2381297],
        [0.03844769, -0.74635022],
        [-1.58567922, 0.08499354],
        [0.6359888, -0.58477698],
        [0.24417242, -0.53172465],
        [-2.19680359, 0.49473677],
        [1.0323503, -0.55688],
        [-0.28858067, -0.39972528],
        [0.20597008, -0.80171536],
        [-1.2107308, -0.34924109],
        [1.33423684, 0.7721489],
        [1.19480152, 1.04788556],
        [0.9917477, 0.89202008],
        [-1.8356219, -0.04839732],
        [0.08415721, -0.71564326],
        [-1.48970175, -0.19299604],
        [0.38782418, -0.82060119],
        [-0.01448044, -0.9779841],
        [-2.0521341, -0.02129125],
        [0.10331194, -0.82162781],
        [-0.44189315, -0.65710974],
        [1.10390926, 1.02481182],
        [-1.59227759, -0.17374038],
        [-1.47344152, -0.02202853],
        [-1.35514704, 0.22971067],
        [0.0412337, -1.23776622],
        [0.4761517, -1.13672124],
        [1.04335676, 0.82345905],
        [-0.07961882, -0.85677394],
        [0.87065059, 1.08052841],
        [1.40267313, 1.07525119],
        [0.80111157, 1.28342825],
        [-0.16527516, -1.23583804],
        [-0.33779221, -0.59194323],
        [0.80610749, -0.73752159],
        [-1.43590032, -0.56384446],
        [0.54868895, -0.95143829],
        [0.46803131, -0.74973907],
        [-1.5137129, -0.83914323],
        [0.9138436, 1.51126532],
        [-1.97233903, -0.41155375],
        [0.5213406, -0.88654894],
        [0.62759494, -1.18590477],
        [0.94163014, 1.35399335],
        [0.56994768, 1.07036606],
        [-1.87663382, 0.14745773],
        [0.90612186, 0.91084011],
        [-1.37481454, 0.28428395],
        [-1.80564029, -0.96710574],
        [0.34307757, -0.79999275],
        [0.70380566, 1.00025804],
        [-1.68489862, -0.30564595],
        [1.31473221, 0.98614978],
        [0.26151216, -0.26069251],
        [0.9193121, 0.82371485],
        [-1.21795929, -0.20219674],
        [-0.17722723, -1.02665245],
        [0.64824862, -0.66822881],
        [0.41206786, -0.28783784],
        [1.01568202, 1.13481667],
        [0.67900254, -0.91489502],
        [-1.05182747, -0.01062376],
        [0.61306599, 1.78210384],
        [-1.50219748, -0.52308922],
        [-1.72717293, -0.46173916],
        [-1.60995631, -0.1821007],
        [-1.09111021, -0.0781398],
        [-0.01046978, -0.80913034],
        [0.32782303, -0.80734754],
        [1.22038503, 1.1959793],
        [-1.33328681, -0.30001937],
        [0.87959517, 1.11566491],
        [-1.14829098, -0.30400762],
        [-0.58019755, -1.19996018],
        [-0.01161159, -0.78468854],
        [0.17359724, -0.63398145],
        [1.32738556, 0.67759969],
        [-1.93467327, 0.30572472],
        [-1.57761893, -0.27726365],
        [0.47639, 1.21422648],
        [-1.65237509, -0.6803981],
        [-0.12609976, -1.04327457],
        [-1.89607082, -0.70085502],
        [0.57466899, 0.74878369],
        [-0.16660312, -0.83110295],
        [0.8013355, 1.22244435],
        [1.18455426, 1.4346467],
        [1.08864428, 0.64667112],
        [-1.61158505, 0.22805725],
        [-1.57512205, -0.09612576],
        [0.0721357, -0.69640328],
        [-1.40054298, 0.16390598],
        [1.09607713, 1.16804691],
        [-2.54346204, -0.23089822],
        [-1.34544875, 0.25151126],
        [-1.35478629, -0.19103317],
        [0.18368113, -1.15827725],
        [-1.31368677, -0.376357],
        [0.09990129, 1.22500491],
        [1.17225574, 1.30835143],
        [0.0865397, -0.79714371],
        [-0.21053923, -1.13421511],
        [0.26496024, -0.94760742],
        [-0.2557591, -1.06266022],
        [-0.26039757, -0.74774225],
        [-1.91787359, 0.16434571],
        [0.93021139, 0.49436331],
        [0.44770467, -0.72877918],
        [-1.63802869, -0.58925528],
        [-1.95712763, -0.10125137],
        [0.9270337, 0.88251423],
        [1.25660093, 0.60828073],
        [-1.72818632, 0.08416887],
        [0.3499788, -0.30490298],
        [-1.51696082, -0.50913109],
        [0.18763605, -0.55424924],
        [0.89609809, 0.83551508],
        [-1.54968857, -0.17114782],
        [1.2157457, 1.23317728],
        [0.20307745, -1.03784906],
        [0.84589086, 1.03615273],
        [0.53237919, 1.47362884],
        [-0.05319044, -1.36150553],
        [1.38819743, 1.11729915],
        [1.00696304, 1.0367721],
        [0.56681869, -1.09637176],
        [0.86888296, 1.05248874],
        [-1.16286609, -0.55875245],
        [0.27717768, -0.83844015],
        [0.16563267, -0.80306607],
        [0.38263303, -0.42683241],
        [1.14519807, 0.89659026],
        [0.81455857, 0.67533667],
        [-1.8603152, -0.09537561],
        [0.965641, 0.90295579],
        [-1.49897451, -0.33254044],
        [-0.1335489, -0.80727582],
        [0.12541527, -1.13354906],
        [1.06062436, 1.28816358],
        [-1.49154578, -0.2024641],
        [1.16189032, 1.28819877],
        [0.54282033, 0.75203524],
        [0.89221065, 0.99211624],
        [-1.49932011, -0.32430667],
        [0.3166647, -1.34482915],
        [0.13972469, -1.22097448],
        [-1.5499724, -0.10782584],
        [1.23846858, 1.37668804],
        [1.25558954, 0.72026098],
        [0.25558689, -1.28529763],
        [0.45168933, -0.55952093],
        [1.06202057, 1.03404604],
        [0.67451908, -0.54970299],
        [0.22759676, -1.02729468],
        [-1.45835281, -0.04951074],
        [0.23273501, -0.70849262],
        [1.59679589, 1.11395076],
        [0.80476105, 0.544627],
        [1.15492521, 1.04352191],
        [0.59632776, -1.19142897],
        [0.02839068, -0.43829366],
        [1.13451584, 0.5632633],
        [0.21576204, -1.04445753],
        [1.41048987, 1.02830719],
        [1.12289302, 0.58029441],
        [0.25200688, -0.82588436],
        [-1.28566081, -0.07390909],
        [1.52849815, 1.11822469],
        [-0.23907858, -0.70541972],
        [-0.25792784, -0.81825035],
        [0.59367818, -0.45239915],
        [0.07931909, -0.29233213],
        [-1.27256815, 0.11630577],
        [0.66930129, 1.00731481],
        [0.34791546, -1.20822877],
        [-2.11283993, -0.66897935],
        [-1.6293824, -0.32718222],
        [-1.53819139, -0.01501972],
        [-0.11988545, -0.6036339],
        [-1.54418956, -0.30389844],
        [0.30026614, -0.77723173],
        [0.00935449, -0.53888192],
        [-1.33424393, -0.11560431],
        [0.47504489, 0.78421384],
        [0.59313264, 1.232239],
        [0.41370369, -1.35205857],
        [0.55840948, 0.78831053],
        [0.49855018, -0.789949],
        [0.35675809, -0.81038693],
        [-1.86197825, -0.59071305],
        [-1.61977671, -0.16076687],
        [0.80779295, -0.73311294],
        [1.62745775, 0.62787163],
        [-1.56993593, -0.08467567],
        [1.02558561, 0.89383302],
        [0.24293461, -0.6088253],
        [1.23130242, 1.00262186],
        [-1.9651013, -0.15886289],
        [0.42795032, -0.70384432],
        [-1.58306818, -0.19431923],
        [-1.57195922, 0.01413469],
        [-0.98145373, 0.06132285],
        [-1.48637844, -0.5746531],
        [0.98745828, 0.69188053],
        [1.28619721, 1.28128821],
        [0.85850596, 0.95541481],
        [0.19028286, -0.82112942],
        [0.26561046, -0.04255239],
        [-1.61897897, 0.00862372],
        [0.24070183, -0.52664209],
        [1.15220993, 0.43916694],
        [-1.21967812, -0.2580313],
        [0.33412533, -0.86117761],
        [0.17131003, -0.75638965],
        [-1.19828397, -0.73744665],
        [-0.12245932, -0.45648879],
        [1.51200698, 0.88825741],
        [1.10338866, 0.92347479],
        [1.30972095, 0.59066989],
        [0.19964876, 1.14855889],
        [0.81460515, 0.84538972],
        [-1.6422739, -0.42296206],
        [0.01224351, -0.21247816],
        [0.33709102, -0.74618065],
        [0.47301054, 0.72712075],
        [0.34706626, 1.23033757],
        [-0.00393279, -0.97209694],
        [-1.64303119, 0.05276337],
        [1.44649625, 1.14217033],
        [-1.93030087, -0.40026146],
        [-2.37296135, -0.72633645],
        [0.45860122, -1.06048953],
        [0.4896361, -1.18928313],
        [-1.02335902, -0.17520578],
        [-1.32761107, -0.93963549],
        [-1.50987909, -0.09473658],
        [0.02723057, -0.79870549],
        [1.0169412, 1.26461701],
        [0.47733527, -0.9898471],
        [-1.27784224, -0.547416],
        [0.49898802, -0.6237259],
        [1.06004731, 0.86870008],
        [1.00207501, 1.38293512],
        [1.31161394, 0.62833956],
        [1.13428443, 1.18346542],
        [1.27671346, 0.96632878],
        [-0.63342885, -0.97768251],
        [0.12698779, -0.93142317],
        [-1.34510812, -0.23754226],
        [-0.53162278, -1.25153594],
        [0.21959934, -0.90269938],
        [-1.78997479, -0.12115748],
        [1.23197473, -0.07453764],
        [1.4163536, 1.21551752],
        [-1.90280976, -0.1638976],
        [-0.22440081, -0.75454248],
        [0.59559412, 0.92414553],
        [1.21930773, 1.08175284],
        [-1.99427535, -0.37587799],
        [-1.27818474, -0.52454551],
        [0.62352689, -1.01430108],
        [0.14024251, -0.428266],
        [-0.16145713, -1.16359731],
        [-1.74795865, -0.06033101],
        [-1.16659791, 0.0902393],
        [0.41110408, -0.8084249],
        [1.14757168, 0.77804528],
        [-1.65590748, -0.40105446],
        [-1.15306865, 0.00858699],
        [0.60892121, 0.68974833],
        [-0.08434138, -0.97615256],
        [0.19170053, -0.42331438],
        [0.29663162, -1.13357399],
        [-1.36893628, -0.25052124],
        [-0.08037807, -0.56784155],
        [0.35695011, -1.15064408],
        [0.02482179, -0.63594828],
        [-1.49075558, -0.2482507],
        [-1.408588, 0.25635431],
        [-1.98274626, -0.54584475],
    ]
)

xs = points[:, 0]
ys = points[:, 1]

plt.scatter(xs, ys)
show()

# Clustering 2D points

new_points = np.array(
    [
        [4.00233332e-01, -1.26544471e00],
        [8.03230370e-01, 1.28260167e00],
        [-1.39507552e00, 5.57292921e-02],
        [-3.41192677e-01, -1.07661994e00],
        [1.54781747e00, 1.40250049e00],
        [2.45032018e-01, -4.83442328e-01],
        [1.20706886e00, 8.88752605e-01],
        [1.25132628e00, 1.15555395e00],
        [1.81004415e00, 9.65530731e-01],
        [-1.66963401e00, -3.08103509e-01],
        [-7.17482105e-02, -9.37939700e-01],
        [6.82631927e-01, 1.10258160e00],
        [1.09039598e00, 1.43899529e00],
        [-1.67645414e00, -5.04557049e-01],
        [-1.84447804e00, 4.52539544e-02],
        [1.24234851e00, 1.02088661e00],
        [-1.86147041e00, 6.38645811e-03],
        [-1.46044943e00, 1.53252383e-01],
        [4.98981817e-01, 8.98006058e-01],
        [9.83962244e-01, 1.04369375e00],
        [-1.83136742e00, -1.63632835e-01],
        [1.30622617e00, 1.07658717e00],
        [3.53420328e-01, -7.51320218e-01],
        [1.13957970e00, 1.54503860e00],
        [2.93995694e-01, -1.26135005e00],
        [-1.14558225e00, -3.78709636e-02],
        [1.18716105e00, 6.00240663e-01],
        [-2.23211946e00, 2.30475094e-01],
        [-1.28320430e00, -3.93314568e-01],
        [4.94296696e-01, -8.83972009e-01],
        [6.31834930e-02, -9.11952228e-01],
        [9.35759539e-01, 8.66820685e-01],
        [1.58014721e00, 1.03788392e00],
        [1.06304960e00, 1.02706082e00],
        [-1.39732536e00, -5.05162249e-01],
        [-1.09935240e-01, -9.08113619e-01],
        [1.17346758e00, 9.47501092e-01],
        [9.20084511e-01, 1.45767672e00],
        [5.82658956e-01, -9.00086832e-01],
        [9.52772328e-01, 8.99042386e-01],
        [-1.37266956e00, -3.17878215e-02],
        [2.12706760e-02, -7.07614194e-01],
        [3.27049052e-01, -5.55998107e-01],
        [-1.71590267e00, 2.15222266e-01],
        [5.12516209e-01, -7.60128245e-01],
        [1.13023469e00, 7.22451122e-01],
        [-1.43074310e00, -3.42787511e-01],
        [-1.82724625e00, 1.17657775e-01],
        [1.41801350e00, 1.11455080e00],
        [1.26897304e00, 1.41925971e00],
        [8.04076494e-01, 1.63988557e00],
        [8.34567752e-01, 1.09956689e00],
        [-1.24714732e00, -2.23522320e-01],
        [-1.29422537e00, 8.18770024e-02],
        [-2.27378316e-01, -4.13331387e-01],
        [2.18830387e-01, -4.68183120e-01],
        [-1.22593414e00, 2.55599147e-01],
        [-1.31294033e00, -4.28892070e-01],
        [-1.33532382e00, 6.52053776e-01],
        [-3.01100233e-01, -1.25156451e00],
        [2.02778356e-01, -9.05277445e-01],
        [1.01357784e00, 1.12378981e00],
        [8.18324394e-01, 8.60841257e-01],
        [1.26181556e00, 1.46613744e00],
        [4.64867724e-01, -7.97212459e-01],
        [3.60908898e-01, 8.44106720e-01],
        [-2.15098310e00, -3.69583937e-01],
        [1.05005281e00, 8.74181364e-01],
        [1.06580074e-01, -7.49268153e-01],
        [-1.73945723e00, 2.52183577e-01],
        [-1.12017687e-01, -6.52469788e-01],
        [5.16618951e-01, -6.41267582e-01],
        [3.26621787e-01, -8.80608015e-01],
        [1.09017759e00, 1.10952558e00],
        [3.64459576e-01, -6.94215622e-01],
        [-1.90779318e00, 1.87383674e-01],
        [-1.95601829e00, 1.39959126e-01],
        [3.18541701e-01, -4.05271704e-01],
        [7.36512699e-01, 1.76416255e00],
        [-1.44175162e00, -5.72320429e-02],
        [3.21757168e-01, -5.34283821e-01],
        [-1.37317305e00, 4.64484644e-02],
        [6.87225910e-02, -1.10522944e00],
        [9.59314218e-01, 6.52316210e-01],
        [-1.62641919e00, -5.62423280e-01],
        [1.06788305e00, 7.29260482e-01],
        [-1.79643547e00, -9.88307418e-01],
        [-9.88628377e-02, -6.81198092e-02],
        [-1.05135700e-01, 1.17022143e00],
        [8.79964699e-01, 1.25340317e00],
        [9.80753407e-01, 1.15486539e00],
        [-8.33224966e-02, -9.24844368e-01],
        [8.48759673e-01, 1.09397425e00],
        [1.32941649e00, 1.13734563e00],
        [3.23788068e-01, -7.49732451e-01],
        [-1.52610970e00, -2.49016929e-01],
        [-1.48598116e00, -2.68828608e-01],
        [-1.80479553e00, 1.87052700e-01],
        [-2.01907347e00, -4.49511651e-01],
        [2.87202402e-01, -6.55487415e-01],
        [8.22295102e-01, 1.38443234e00],
        [-3.56997036e-02, -8.01825807e-01],
        [-1.66955440e00, -1.38258505e-01],
        [-1.78226821e00, 2.93353033e-01],
        [7.25837138e-01, -6.23374024e-01],
        [3.88432593e-01, -7.61283497e-01],
        [1.49002783e00, 7.95678671e-01],
        [6.55423228e-04, -7.40580702e-01],
        [-1.34533116e00, -4.75629937e-01],
        [-8.03845106e-01, -3.09943013e-01],
        [-2.49041295e-01, -1.00662418e00],
        [-1.41095118e00, -7.06744127e-02],
        [-1.75119594e00, -3.00491336e-01],
        [-1.27942724e00, 1.73774600e-01],
        [3.35028183e-01, 6.24761151e-01],
        [1.16819649e00, 1.18902251e00],
        [7.15210457e-01, 9.26077419e-01],
        [1.30057278e00, 9.16349565e-01],
        [-1.21697008e00, 1.10039477e-01],
        [-1.70707935e00, -5.99659536e-02],
        [1.20730655e00, 1.05480463e00],
        [1.86896009e-01, -9.58047234e-01],
        [8.03463471e-01, 3.86133140e-01],
        [-1.73486790e00, -1.49831913e-01],
        [1.31261499e00, 1.11802982e00],
        [4.04993148e-01, -5.10900347e-01],
        [-1.93267968e00, 2.20764694e-01],
        [6.56004799e-01, 9.61887161e-01],
        [-1.40588215e00, 1.17134403e-01],
        [-1.74306264e00, -7.47473959e-02],
        [5.43745412e-01, 1.47209224e00],
        [-1.97331669e00, -2.27124493e-01],
        [1.53901171e00, 1.36049081e00],
        [-1.48323452e00, -4.90302063e-01],
        [3.86748484e-01, -1.26173400e00],
        [1.17015716e00, 1.18549415e00],
        [-8.05381721e-02, -3.21923627e-01],
        [-6.82273156e-02, -8.52825887e-01],
        [7.13500028e-01, 1.27868520e00],
        [-1.85014378e00, -5.03490558e-01],
        [6.36085266e-02, -1.41257040e00],
        [1.52966062e00, 9.66056572e-01],
        [1.62165714e-01, -1.37374843e00],
        [-3.23474497e-01, -7.06620269e-01],
        [-1.51768993e00, 1.87658302e-01],
        [8.88895911e-01, 7.62237161e-01],
        [4.83164032e-01, 8.81931869e-01],
        [-5.52997766e-02, -7.11305016e-01],
        [-1.57966441e00, -6.29220313e-01],
        [5.51308645e-02, -8.47206763e-01],
        [-2.06001582e00, 5.87697787e-02],
        [1.11810855e00, 1.30254175e00],
        [4.87016164e-01, -9.90143937e-01],
        [-1.65518042e00, -1.69386383e-01],
        [-1.44349738e00, 1.90299243e-01],
        [-1.70074547e-01, -8.26736022e-01],
        [-1.82433979e00, -3.07814626e-01],
        [1.03093485e00, 1.26457691e00],
        [1.64431169e00, 1.27773115e00],
        [-1.47617693e00, 2.60783872e-02],
        [1.00953067e00, 1.14270181e00],
        [-1.45285636e00, -2.55216207e-01],
        [-1.74092917e00, -8.34443177e-02],
        [1.22038299e00, 1.28699961e00],
        [9.16925397e-01, 7.32070275e-01],
        [-1.60754185e-03, -7.26375571e-01],
        [8.93841238e-01, 8.41146643e-01],
        [6.33791961e-01, 1.00915134e00],
        [-1.47927075e00, -6.99781936e-01],
        [5.44799374e-02, -1.06441970e00],
        [-1.51935568e00, -4.89276929e-01],
        [2.89939026e-01, -7.73145523e-01],
        [-9.68154061e-03, -1.13302207e00],
        [1.13474639e00, 9.71541744e-01],
        [5.36421406e-01, -8.47906388e-01],
        [1.14759864e00, 6.89915205e-01],
        [5.73291902e-01, 7.90802710e-01],
        [2.12377397e-01, -6.07569808e-01],
        [5.26579548e-01, -8.15930264e-01],
        [-2.01831641e00, 6.78650740e-02],
        [-2.35512624e-01, -1.08205132e00],
        [1.59274780e-01, -6.00717261e-01],
        [2.28120356e-01, -1.16003549e00],
        [-1.53658378e00, 8.40798808e-02],
        [1.13954609e00, 6.31782001e-01],
        [1.01119255e00, 1.04360805e00],
        [-1.42039867e-01, -4.81230337e-01],
        [-2.23120182e00, 8.49162905e-02],
        [1.25554811e-01, -1.01794793e00],
        [-1.72493509e00, -6.94426177e-01],
        [-1.60434630e00, 4.45550868e-01],
        [7.37153979e-01, 9.26560744e-01],
        [6.72905271e-01, 1.13366030e00],
        [1.20066456e00, 7.26273093e-01],
        [7.58747209e-02, -9.83378326e-01],
        [1.28783262e00, 1.18088601e00],
        [1.06521930e00, 1.00714746e00],
        [1.05871698e00, 1.12956519e00],
        [-1.12643410e00, 1.66787744e-01],
        [-1.10157218e00, -3.64137806e-01],
        [2.35118217e-01, -1.39769949e-01],
        [1.13853795e00, 1.01018519e00],
        [5.31205654e-01, -8.81990792e-01],
        [4.33085936e-01, -7.64059042e-01],
        [-4.48926156e-03, -1.30548411e00],
        [-1.76348589e00, -4.97430739e-01],
        [1.36485681e00, 5.83404699e-01],
        [5.66923900e-01, 1.51391963e00],
        [1.35736826e00, 6.70915318e-01],
        [1.07173397e00, 6.11990884e-01],
        [1.00106915e00, 8.93815326e-01],
        [1.33091007e00, 8.79773879e-01],
        [-1.79603740e00, -3.53883973e-02],
        [-1.27222979e00, 4.00156642e-01],
        [8.47480603e-01, 1.17032364e00],
        [-1.50989129e00, -7.12318330e-01],
        [-1.24953576e00, -5.57859730e-01],
        [-1.27717973e00, -5.99350550e-01],
        [-1.81946743e00, 7.37057673e-01],
        [1.19949867e00, 1.56969386e00],
        [-1.25543847e00, -2.33892826e-01],
        [-1.63052058e00, 1.61455865e-01],
        [1.10611305e00, 7.39698224e-01],
        [6.70193192e-01, 8.70567001e-01],
        [3.69670156e-01, -6.94645306e-01],
        [-1.26362293e00, -6.99249285e-01],
        [-3.66687507e-01, -1.35310260e00],
        [2.44032147e-01, -6.59470793e-01],
        [-1.27679142e00, -4.85453412e-01],
        [3.77473612e-02, -6.99251605e-01],
        [-2.19148539e00, -4.91199500e-01],
        [-2.93277777e-01, -5.89488212e-01],
        [-1.65737397e00, -2.98337786e-01],
        [7.36638861e-01, 5.78037057e-01],
        [1.13709081e00, 1.30119754e00],
        [-1.44146601e00, 3.13934680e-02],
        [5.92360708e-01, 1.22545114e00],
        [6.51719414e-01, 4.92674894e-01],
        [5.94559139e-01, 8.25637315e-01],
        [-1.87900722e00, -5.21899626e-01],
        [2.15225041e-01, -1.28269851e00],
        [4.99145965e-01, -6.70268634e-01],
        [-1.82954176e00, -3.39269731e-01],
        [7.92721403e-01, 1.33785606e00],
        [9.54363372e-01, 9.80396626e-01],
        [-1.35359846e00, 1.03976340e-01],
        [1.05595062e00, 8.07031927e-01],
        [-1.94311010e00, -1.18976964e-01],
        [-1.39604137e00, -3.10095976e-01],
        [1.28977624e00, 1.01753365e00],
        [-1.59503139e00, -5.40574609e-01],
        [-1.41994046e00, -3.81032569e-01],
        [-2.35569801e-02, -1.10133702e00],
        [-1.26038568e00, -6.93273886e-01],
        [9.60215981e-01, -8.11553694e-01],
        [5.51803308e-01, -1.01793176e00],
        [3.70185085e-01, -1.06885468e00],
        [8.25529207e-01, 8.77007060e-01],
        [-1.87032595e00, 2.87507199e-01],
        [-1.56260769e00, -1.89196712e-01],
        [-1.26346548e00, -7.74725237e-01],
        [-6.33800421e-02, -7.59400611e-01],
        [8.85298280e-01, 8.85620519e-01],
        [-1.43324686e-01, -1.16083678e00],
        [-1.83908725e00, -3.26655515e-01],
        [2.74709229e-01, -1.04546829e00],
        [-1.45703573e00, -2.91842036e-01],
        [-1.59048842e00, 1.66063031e-01],
        [9.25549284e-01, 7.41406406e-01],
        [1.97245469e-01, -7.80703225e-01],
        [2.88401697e-01, -8.32425551e-01],
        [7.24141618e-01, -7.99149200e-01],
        [-1.62658639e00, -1.80005543e-01],
        [5.84481588e-01, 1.13195640e00],
        [1.02146732e00, 4.59657799e-01],
        [8.65050554e-01, 9.57714887e-01],
        [3.98717766e-01, -1.24273147e00],
        [8.62234892e-01, 1.10955561e00],
        [-1.35999430e00, 2.49942654e-02],
        [-1.19178505e00, -3.82946323e-02],
        [1.29392424e00, 1.10320509e00],
        [1.25679630e00, -7.79857582e-01],
        [9.38040302e-02, -5.53247258e-01],
        [-1.73512175e00, -9.76271667e-02],
        [2.23153587e-01, -9.43474351e-01],
        [4.01989100e-01, -1.10963051e00],
        [-1.42244158e00, 1.81914703e-01],
        [3.92476267e-01, -8.78426277e-01],
        [1.25181875e00, 6.93614996e-01],
        [1.77481317e-02, -7.20304235e-01],
        [-1.87752521e00, -2.63870424e-01],
        [-1.58063602e00, -5.50456344e-01],
        [-1.59589493e00, -1.53932892e-01],
        [-1.01829770e00, 3.88542370e-02],
        [1.24819659e00, 6.60041803e-01],
        [-1.25551377e00, -2.96172009e-02],
        [-1.41864559e00, -3.58230179e-01],
        [5.25758326e-01, 8.70500543e-01],
        [5.55599988e-01, 1.18765072e00],
        [2.81344439e-02, -6.99111314e-01],
    ]
)

from sklearn.cluster import KMeans

# Create a KMeans instance with 3 clusters: model
model = KMeans(n_clusters=3)

# Fit model to points
model.fit(points)

# Determine the cluster labels of new_points: labels
labels = model.predict(new_points)

# Print cluster labels of new_points
print(labels)

# Inspect your clustering

# Assign the columns of new_points: xs and ys
xs = new_points[:, 0]
ys = new_points[:, 1]

# Make a scatter plot of xs and ys, using labels to define the colors
plt.scatter(xs, ys, c=labels, alpha=0.5)

# Assign the cluster centers: centroids
centroids = model.cluster_centers_

# Assign the columns of centroids: centroids_x, centroids_y
centroids_x = centroids[:, 0]
centroids_y = centroids[:, 1]

# Make a scatter plot of centroids_x and centroids_y
plt.scatter(centroids_x, centroids_y, marker="D", s=50, color="red")
show()

# Evaluating a clustering

df = pd.read_csv("./data/seeds.csv", header=None)
df[7] = df[7].map({1: "Kama wheat", 2: "Rosa wheat", 3: "Canadian wheat"})
df.head()

samples = df.iloc[:, :-1].values
varieties = df.iloc[:, -1].values

ks = range(1, 6)
inertias = []

for k in ks:
    # Create a KMeans instance with k clusters: model
    model = KMeans(n_clusters=k)

    # Fit model to samples
    model.fit(samples)

    # Append the inertia to the list of inertias
    inertias.append(model.inertia_)

# Plot ks vs inertias
plt.plot(ks, inertias, "-o")
plt.xlabel("number of clusters, k")
plt.ylabel("inertia")
plt.xticks(ks)
show()

# Evaluating the grain clustering

# Create a KMeans model with 3 clusters: model
model = KMeans(n_clusters=3)

# Use fit_predict to fit model and obtain cluster labels: labels
labels = model.fit_predict(samples)

# Create a DataFrame with labels and varieties as columns: df
df = pd.DataFrame({"labels": labels, "varieties": varieties})

# Create crosstab: ct
ct = pd.crosstab(df["labels"], df["varieties"])

# Display ct
print(ct)

# Transforming features for better clusterings

# Scaling fish data for clustering

df = pd.read_csv("./data/fish.csv", header=None)
df.head()

samples = df.iloc[:, 1:].values
species = df.iloc[:, 0].values

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Create scaler: scaler
scaler = StandardScaler()

# Create KMeans instance: kmeans
kmeans = KMeans(n_clusters=4)

# Create pipeline: pipeline
pipeline = make_pipeline(scaler, kmeans)

# Clustering the fish data

# Fit the pipeline to samples
pipeline.fit(samples)

# Calculate the cluster labels: labels
labels = pipeline.predict(samples)

# Create a DataFrame with labels and species as columns: df
df = pd.DataFrame({"labels": labels, "species": species})

# Create crosstab: ct
ct = pd.crosstab(df["labels"], df["species"])

# Display ct
print(ct)

# Clustering stocks using KMeans

df = pd.read_csv("./data/company-stock-movements-2010-2015-incl.csv", index_col=0)
df.head()

movements = df.values
companies = df.index.values

from sklearn.preprocessing import Normalizer

# Create a normalizer: normalizer
normalizer = Normalizer()

# Create a KMeans model with 10 clusters: kmeans
kmeans = KMeans(n_clusters=10)

# Make a pipeline chaining normalizer and kmeans: pipeline
pipeline = make_pipeline(normalizer, kmeans)

# Fit pipeline to the daily price movements
pipeline.fit(movements)

# Which stocks move together?

# Predict the cluster labels: labels
labels = pipeline.predict(movements)

# Create a DataFrame aligning labels and companies: df
df = pd.DataFrame({"labels": labels, "companies": companies})

# Display df sorted by cluster label
print(df.sort_values("labels"))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Visualization with hierarchical clustering and t-SNE

df = pd.read_csv("./data/seeds.csv", header=None)
df[7] = df[7].map({1: "Kama wheat", 2: "Rosa wheat", 3: "Canadian wheat"})
df.head()

samples = df.iloc[:, :-1].values
varieties = df.iloc[:, -1].values

from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram

# Calculate the linkage: mergings
mergings = linkage(samples, method="complete")

# Plot the dendrogram, using varieties as labels
plt.figure(figsize=(15, 5))
dendrogram(
    mergings,
    labels=varieties,
    leaf_rotation=90,
    leaf_font_size=6,
)
show()

# Hierarchies of stocks

df = pd.read_csv("./data/company-stock-movements-2010-2015-incl.csv", index_col=0)
df.head()

movements = df.values
companies = df.index.values

from sklearn.preprocessing import normalize

# Normalize the movements: normalize_movements
normalized_movements = normalize(movements)

# Calculate the linkage: mergings
mergings = linkage(normalized_movements, method="complete")

# Plot the dendrogram
plt.figure(figsize=(15, 5))
dendrogram(mergings, labels=companies, leaf_rotation=90, leaf_font_size=6)
show()

# Cluster labels in hierarchical clustering

# Different linkage, different hierarchical clustering!

df = pd.read_csv("./data/eurovision-2016.csv")
df

samples = df.iloc[:, 2:7].values[:42]
country_names = df.iloc[:, 1].values[:42]

# Calculate the linkage: mergings
mergings = linkage(samples, method="single")

# Plot the dendrogram
plt.figure(figsize=(15, 5))
dendrogram(mergings, labels=country_names, leaf_rotation=90, leaf_font_size=6)
show()

# Extracting the cluster labels

df = pd.read_csv("./data/seeds.csv", header=None)
df[7] = df[7].map({1: "Kama wheat", 2: "Rosa wheat", 3: "Canadian wheat"})
df.head()

samples = df.iloc[:, :-1].values
varieties = df.iloc[:, -1].values

from scipy.cluster.hierarchy import fcluster

mergings = linkage(samples, method="complete")

# Use fcluster to extract labels: labels
labels = fcluster(mergings, 6, criterion="distance")

# Create a DataFrame with labels and varieties as columns: df
df = pd.DataFrame({"labels": labels, "varieties": varieties})

# Create crosstab
ct = pd.crosstab(df["labels"], df["varieties"])

# Display ct
print(ct)

# t-SNE for 2-dimensional maps

# t-SNE visualization of grain dataset

df = pd.read_csv("./data/seeds.csv", header=None)

samples = df.iloc[:, :-1].values
variety_numbers = df.iloc[:, -1].values

from sklearn.manifold import TSNE

# Create a TSNE instance: model
model = TSNE(learning_rate=200)

# Apply fit_transform to samples: tsne_features
tsne_features = model.fit_transform(samples)

# Select the 0th feature: xs
xs = tsne_features[:, 0]

# Select the 1st feature: ys
ys = tsne_features[:, 1]

# Scatter plot, coloring by variety_numbers
plt.scatter(xs, ys, c=variety_numbers)
show()

# A t-SNE map of the stock market

df = pd.read_csv("./data/company-stock-movements-2010-2015-incl.csv", index_col=0)
movements = df.values
companies = df.index.values
normalized_movements = normalize(movements)

# Create a TSNE instance: model
model = TSNE(learning_rate=50)

# Apply fit_transform to normalized_movements: tsne_features
tsne_features = model.fit_transform(normalized_movements)

# Select the 0th feature: xs
xs = tsne_features[:, 0]

# Select the 1st feature: ys
ys = tsne_features[:, 1]

# Scatter plot
plt.figure(figsize=(10, 10))
plt.scatter(xs, ys, alpha=0.5)

# Annotate the points
for x, y, company in zip(xs, ys, companies):
    plt.annotate(company, (x, y), fontsize=8, alpha=0.75)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Decorrelating your data and dimension reduction

# Visualizing the PCA transformation

df = pd.read_csv("./data/seeds-width-vs-length.csv", header=None)
df.head()

grains = df.values

from scipy.stats import pearsonr

# Assign the 0th column of grains: width
width = grains[:, 0]

# Assign the 1st column of grains: length
length = grains[:, 1]

# Scatter plot width vs length
plt.scatter(width, length)
plt.axis("equal")
show()

# Calculate the Pearson correlation
correlation, pvalue = pearsonr(width, length)

# Display the correlation
print(correlation)

# 0.8604149377143466

# Decorrelating the grain measurements with PCA

from sklearn.decomposition import PCA

# Create a PCA instance: model
model = PCA()

# Apply the fit_transform method of model to grains: pca_features
pca_features = model.fit_transform(grains)

# Assign 0th column of pca_features: xs
xs = pca_features[:, 0]

# Assign 1st column of pca_features: ys
ys = pca_features[:, 1]

# Scatter plot xs vs ys
plt.scatter(xs, ys)
plt.axis("equal")
show()

# Calculate the Pearson correlation of xs and ys
correlation, pvalue = pearsonr(xs, ys)

# Display the correlation
print(correlation)

# 4.85722573273506e-17

# Intrinsic dimension

# The first principal component

# Make a scatter plot of the untransformed points
plt.scatter(grains[:, 0], grains[:, 1])

# Create a PCA instance: model
model = PCA()

# Fit model to points
model.fit(grains)

# Get the mean of the grain samples: mean
mean = model.mean_

# Get the first principal component: first_pc
first_pc = model.components_[0, :]

# Plot first_pc as an arrow, starting at mean
plt.arrow(mean[0], mean[1], first_pc[0], first_pc[1], color="red", width=0.01)

# keep axes on same scale
plt.axis("equal")
# plt.savefig('../images/pca-arrow.png')
show()

# Variance of the PCA features

df = pd.read_csv("./data/fish.csv", header=None)
df.head()

samples = df.loc[:, 1:].values

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# Create scaler: scaler
scaler = StandardScaler()

# Create a PCA instance: pca
pca = PCA()

# Create pipeline: pipeline
pipeline = make_pipeline(scaler, pca)

# Fit the pipeline to 'samples'
pipeline.fit(samples)

# Plot the explained variances
features = range(pca.n_components_)
plt.bar(features, pca.explained_variance_)
plt.xlabel("PCA feature")
plt.ylabel("variance")
plt.xticks(features)
show()

# Dimension reduction with PCA

scaler = StandardScaler()
scaled_samples = scaler.fit_transform(samples)

# Create a PCA model with 2 components: pca
pca = PCA(n_components=2)

# Fit the PCA instance to the scaled samples
pca.fit(scaled_samples)

# Transform the scaled samples: pca_features
pca_features = pca.transform(scaled_samples)

# Print the shape of pca_features
print(pca_features.shape)

# (85, 2)

# A tf-idf word-frequency array

documents = ["cats say meow", "dogs say woof", "dogs chase cats"]

from sklearn.feature_extraction.text import TfidfVectorizer

# Create a TfidfVectorizer: tfidf
tfidf = TfidfVectorizer()

# Apply fit_transform to document: csr_mat
csr_mat = tfidf.fit_transform(documents)

# Print result of toarray() method
print(csr_mat.toarray())

# Get the word: words
words = tfidf.get_feature_names_out()

# Print words
print(words)

# Clustering Wikipedia part I

from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline

# Create a TruncatedSVD instance: svd
svd = TruncatedSVD(n_components=50)

# Create a KMeans instance: kmeans
kmeans = KMeans(n_clusters=6)

# Create a pipeline: pipeline
pipeline = make_pipeline(svd, kmeans)

# Clustering Wikipedia part II

from scipy.sparse import csc_matrix

documents = pd.read_csv("./data/wikipedia-vectors.csv", index_col=0)
titles = documents.columns
articles = csc_matrix(documents.values).T

type(articles)

# scipy.sparse.csr.csr_matrix

articles.T.shape

# (13125, 60)

# Fit the pipeline to articles
pipeline.fit(articles)

# Calculate the cluster labels: labels
labels = pipeline.predict(articles)

# Create a DataFrame aligning labels and titles: df
df = pd.DataFrame({"label": labels, "article": titles})

# Display df sorted by cluster label
print(df.sort_values("label"))

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

"""
plt.savefig('../images/iris-swarmplot.png')
plt.savefig("_digits.png")
plt.savefig('../images/gm-boxplot.png', dpi=100)
plt.savefig('../images/kmeans-centroid.png')
plt.savefig('../images/tsne-scatter.png')

"""
