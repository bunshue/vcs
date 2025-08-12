"""
新進

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


def show():
    # pass
    plt.tight_layout()  # 緊密排列，並填滿原圖大小
    plt.show()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# plt.style.use('classic')
# plt.style.use('seaborn-v0_8')

x = np.linspace(0, 10, 100)

fig = plt.figure()
# plt.plot(x, np.sin(x), '-')
# plt.plot(x, np.cos(x), '--')

"""
plt.plot(x, np.sin(x - 0), color='blue')        # specify color by name
plt.plot(x, np.sin(x - 1), color='g')           # short color code (rgbcmyk)
plt.plot(x, np.sin(x - 2), color='0.75')        # Grayscale between 0 and 1
plt.plot(x, np.sin(x - 3), color='#FFDD44')     # Hex code (RRGGBB from 00 to FF)
plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3)) # RGB tuple, values 0 to 1
plt.plot(x, np.sin(x - 5), color='chartreuse') # all HTML color names supported
"""

"""
plt.plot(x, x + 0, linestyle='solid')
plt.plot(x, x + 1, linestyle='dashed')
plt.plot(x, x + 2, linestyle='dashdot')
plt.plot(x, x + 3, linestyle='dotted')

# For short, you can use the following codes:
plt.plot(x, x + 4, linestyle='-')  # solid
plt.plot(x, x + 5, linestyle='--') # dashed
plt.plot(x, x + 6, linestyle='-.') # dashdot
plt.plot(x, x + 7, linestyle=':')  # dotted
"""
"""
plt.plot(x, x + 0, '-g')  # solid green
plt.plot(x, x + 1, '--c') # dashed cyan
plt.plot(x, x + 2, '-.k') # dashdot black
plt.plot(x, x + 3, ':r')  # dotted red
"""


rng = np.random.RandomState(0)
for marker in ["o", ".", ",", "x", "+", "v", "^", "<", ">", "s", "d"]:
    plt.plot(rng.rand(5), rng.rand(5), marker, label="marker='{0}'".format(marker))
plt.legend(numpoints=1)
plt.xlim(0, 1.8)

show()

cc = plt.figure().canvas.get_supported_filetypes()
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap="viridis")
plt.colorbar()  # show color scale

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.datasets import load_iris

iris = load_iris()
features = iris.data.T

plt.scatter(
    features[0],
    features[1],
    alpha=0.2,
    s=100 * features[3],
    c=iris.target,
    cmap="viridis",
)
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.gaussian_process import GaussianProcessRegressor

# define the model and draw some data
model = lambda x: x * np.sin(x)
xdata = np.array([1, 3, 5, 6, 8])
ydata = model(xdata)

# Compute the Gaussian process fit
gp = GaussianProcessRegressor()
gp.fit(xdata[:, np.newaxis], ydata)

xfit = np.linspace(0, 10, 1000)
yfit, dyfit_ori = gp.predict(xfit[:, np.newaxis], return_std=True)
dyfit = 2 * dyfit_ori  # 2*sigma ~ 95% confidence region

# Visualize the result
plt.plot(xdata, ydata, "or")
plt.plot(xfit, yfit, "-", color="gray")

plt.fill_between(xfit, yfit - dyfit, yfit + dyfit, color="gray", alpha=0.2)
plt.xlim(0, 10)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)

kwargs = dict(histtype="stepfilled", alpha=0.3, density=True, bins=40)

plt.hist(x1, **kwargs)
plt.hist(x2, **kwargs)
plt.hist(x3, **kwargs)
show()

data = np.random.randn(1000)
counts, bin_edges = np.histogram(data, bins=5)
print(counts)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Two-Dimensional Histograms and Binnings
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 10000).T

plt.hist2d(x, y, bins=30, cmap="Blues")
cb = plt.colorbar()
cb.set_label("counts in bin")

show()

counts, xedges, yedges = np.histogram2d(x, y, bins=30)

plt.hexbin(x, y, gridsize=30, cmap="Blues")
cb = plt.colorbar(label="count in bin")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Kernel density estimation

from scipy.stats import gaussian_kde

# fit an array of size [Ndim, Nsamples]
data = np.vstack([x, y])
kde = gaussian_kde(data)

# evaluate on a regular grid
xgrid = np.linspace(-3.5, 3.5, 40)
ygrid = np.linspace(-6, 6, 40)
Xgrid, Ygrid = np.meshgrid(xgrid, ygrid)
Z = kde.evaluate(np.vstack([Xgrid.ravel(), Ygrid.ravel()]))

# Plot the result as an image
plt.imshow(
    Z.reshape(Xgrid.shape),
    origin="lower",
    aspect="auto",
    extent=[-3.5, 3.5, -6, 6],
    cmap="Blues",
)
cb = plt.colorbar()
cb.set_label("density")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" no file
cities = pd.read_csv('data/california_cities.csv')

# Extract the data we're interested in
lat, lon = cities['latd'], cities['longd']
population, area = cities['population_total'], cities['area_total_km2']

# Scatter the points, using size and color but no label
plt.scatter(lon, lat, label=None,
            c=np.log10(population), cmap='viridis',
            s=area, linewidth=0, alpha=0.5)
plt.axis(aspect='equal')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.colorbar(label='log$_{10}$(population)')
plt.clim(3, 7)

# Here we create a legend:
# we'll plot empty lists with the desired size and label
for area in [100, 300, 500]:
    plt.scatter([], [], c='k', alpha=0.3, s=area,
                label=str(area) + ' km$^2$')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='City Area')

plt.title('California Cities: Area and Population')

show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 10, 1000)
I = np.sin(x) * np.cos(x[:, np.newaxis])

plt.imshow(I)
plt.colorbar()

show()

# Customizing Colorbars
plt.imshow(I, cmap="gray")

show()


from matplotlib.colors import LinearSegmentedColormap


def grayscale_cmap(cmap):
    # Return a grayscale version of the given colormap
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))

    # convert RGBA to perceived grayscale luminance
    # cf. http://alienryderflex.com/hsp.html
    RGB_weight = [0.299, 0.587, 0.114]
    luminance = np.sqrt(np.dot(colors[:, :3] ** 2, RGB_weight))
    colors[:, :3] = luminance[:, np.newaxis]

    return LinearSegmentedColormap.from_list(cmap.name + "_gray", colors, cmap.N)


def view_colormap(cmap):
    # Plot a colormap with its grayscale equivalent
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))

    cmap = grayscale_cmap(cmap)
    grayscale = cmap(np.arange(cmap.N))

    fig, ax = plt.subplots(2, figsize=(6, 2), subplot_kw=dict(xticks=[], yticks=[]))
    ax[0].imshow([colors], extent=[0, 10, 0, 1])
    ax[1].imshow([grayscale], extent=[0, 10, 0, 1])


view_colormap("jet")
show()

view_colormap("viridis")
show()

view_colormap("cubehelix")
show()

view_colormap("RdBu")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# make noise in 1% of the image pixels
speckles = np.random.random(I.shape) < 0.01
I[speckles] = np.random.normal(0, 3, np.count_nonzero(speckles))

plt.subplot(1, 2, 1)
plt.imshow(I, cmap="RdBu")
plt.colorbar()

plt.subplot(1, 2, 2)
plt.imshow(I, cmap="RdBu")
plt.colorbar(extend="both")
plt.clim(-1, 1)

show()

# Discrete Color Bars

plt.imshow(I, cmap=plt.cm.get_cmap("Blues", 6))
plt.colorbar()
plt.clim(-1, 1)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

for i in range(1, 7):
    plt.subplot(2, 3, i)
    plt.text(0.5, 0.5, str((2, 3, i)), fontsize=18, ha="center")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

fig = plt.figure()
fig.subplots_adjust(hspace=0.4, wspace=0.4)
for i in range(1, 7):
    ax = fig.add_subplot(2, 3, i)
    ax.text(0.5, 0.5, str((2, 3, i)), fontsize=18, ha="center")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(2, 3, sharex="col", sharey="row")

for i in range(2):
    for j in range(3):
        ax[i, j].text(0.5, 0.5, str((i, j)), fontsize=18, ha="center")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# plt.GridSpec: More Complicated Arrangements
grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)

plt.subplot(grid[0, 0])
plt.subplot(grid[0, 1:])
plt.subplot(grid[1, :2])
plt.subplot(grid[1, 2])

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Create some normally distributed data
mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 3000).T

# Set up the axes with gridspec
fig = plt.figure(figsize=(6, 6))
grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)
main_ax = fig.add_subplot(grid[:-1, 1:])
y_hist = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax)
x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)

# scatter points on the main axes
main_ax.plot(x, y, "ok", markersize=3, alpha=0.2)

# histogram on the attached axes
x_hist.hist(x, 40, histtype="stepfilled", orientation="vertical", color="gray")
x_hist.invert_yaxis()

y_hist.hist(y, 40, histtype="stepfilled", orientation="horizontal", color="gray")
y_hist.invert_xaxis()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Set the global default size of matplotlib figures
plt.rc("figure", figsize=(10, 8))

# Set seaborn aesthetic parameters to defaults
sns.set()

x = np.linspace(0, 2, 10)

plt.plot(x, x, "o-", label="linear")
plt.plot(x, x**2, "x-", label="quadratic")

plt.legend(loc="best")
plt.title("Linear vs Quadratic progression")
plt.xlabel("Input")
plt.ylabel("Output")
show()

# Histograms

# Gaussian, mean 1, stddev .5, 1000 elements
samples = np.random.normal(loc=1.0, scale=0.5, size=1000)
print(samples.shape)
print(samples.dtype)
print(samples[:30])
plt.hist(samples, bins=50)
show()

# Two Histograms on the Same Plot

samples_1 = np.random.normal(loc=1, scale=0.5, size=10000)
samples_2 = np.random.standard_t(df=10, size=10000)
bins = np.linspace(-3, 3, 50)

# Set an alpha and use the same bins since we are plotting two hists
plt.hist(samples_1, bins=bins, alpha=0.5, label="samples 1")
plt.hist(samples_2, bins=bins, alpha=0.5, label="samples 2")
plt.legend(loc="upper left")
show()


# Scatter Plots

plt.scatter(samples_1, samples_2, alpha=0.1)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" NG
#Applying Matplotlib Visualizations to Kaggle: Titanic

# Set the global default size of matplotlib figures
plt.rc('figure', figsize=(10, 8))

sns.set()

df_train = pd.read_csv('../data/titanic/train.csv')

def clean_data(df):
    
    # Get the unique values of Sex
    sexes = np.sort(df['Sex'].unique())
    
    # Generate a mapping of Sex from a string to a number representation    
    genders_mapping = dict(zip(sexes, range(0, len(sexes) + 1)))

    # Transform Sex from a string to a number representation
    df['Sex_Val'] = df['Sex'].map(genders_mapping).astype(int)
    
    # Get the unique values of Embarked
    embarked_locs = np.sort(df['Embarked'].unique())

    # Generate a mapping of Embarked from a string to a number representation        
    embarked_locs_mapping = dict(zip(embarked_locs, 
                                     range(0, len(embarked_locs) + 1)))
    
    # Transform Embarked from a string to dummy variables
    df = pd.concat([df, pd.get_dummies(df['Embarked'], prefix='Embarked_Val')], axis=1)
    
    # Fill in missing values of Embarked
    # Since the vast majority of passengers embarked in 'S': 3, 
    # we assign the missing values in Embarked to 'S':
    if len(df[df['Embarked'].isnull()] > 0):
        df.replace({'Embarked_Val' : 
                       { embarked_locs_mapping[np.nan] : embarked_locs_mapping['S'] 
                       }
                   }, 
                   inplace=True)
    
    # Fill in missing values of Fare with the average Fare
    if len(df[df['Fare'].isnull()] > 0):
        avg_fare = df['Fare'].mean()
        df.replace({ None: avg_fare }, inplace=True)
    
    # To keep Age in tact, make a copy of it called AgeFill 
    # that we will use to fill in the missing ages:
    df['AgeFill'] = df['Age']

    # Determine the Age typical for each passenger class by Sex_Val.  
    # We'll use the median instead of the mean because the Age 
    # histogram seems to be right skewed.
    df['AgeFill'] = df['AgeFill'] \
                        .groupby([df['Sex_Val'], df['Pclass']]) \
                        .apply(lambda x: x.fillna(x.median()))
            
    # Define a new feature FamilySize that is the sum of 
    # Parch (number of parents or children on board) and 
    # SibSp (number of siblings or spouses):
    df['FamilySize'] = df['SibSp'] + df['Parch']
    
    return df

df_train = clean_data(df_train)


#Bar Plots, Histograms, subplot2grid

# Size of matplotlib figures that contain subplots
figsize_with_subplots = (10, 10)

# Set up a grid of plots
fig = plt.figure(figsize=figsize_with_subplots) 
fig_dims = (3, 2)

# Plot death and survival counts
plt.subplot2grid(fig_dims, (0, 0))
df_train['Survived'].value_counts().plot(kind='bar', 
                                         title='Death and Survival Counts',
                                         color='r',
                                         align='center')

# Plot Pclass counts
plt.subplot2grid(fig_dims, (0, 1))
df_train['Pclass'].value_counts().plot(kind='bar', 
                                       title='Passenger Class Counts')

# Plot Sex counts
plt.subplot2grid(fig_dims, (1, 0))
df_train['Sex'].value_counts().plot(kind='bar', 
                                    title='Gender Counts')
plt.xticks(rotation=0)

# Plot Embarked counts
plt.subplot2grid(fig_dims, (1, 1))
df_train['Embarked'].value_counts().plot(kind='bar', 
                                         title='Ports of Embarkation Counts')

# Plot the Age histogram
plt.subplot2grid(fig_dims, (2, 0))
df_train['Age'].hist()
plt.title('Age Histogram')

show()

# Get the unique values of Embarked and its maximum
family_sizes = np.sort(df_train['FamilySize'].unique())
family_size_max = max(family_sizes)

df1 = df_train[df_train['Survived'] == 0]['FamilySize']
df2 = df_train[df_train['Survived'] == 1]['FamilySize']
plt.hist([df1, df2], 
         bins=family_size_max + 1, 
         range=(0, family_size_max), 
         stacked=True)
plt.legend(('Died', 'Survived'), loc='best')
plt.title('Survivors by Family Size')

show()

#Normalized Plots

pclass_xt = pd.crosstab(df_train['Pclass'], df_train['Survived'])

# Normalize the cross tab to sum to 1:
pclass_xt_pct = pclass_xt.div(pclass_xt.sum(1).astype(float), axis=0)

pclass_xt_pct.plot(kind='bar', 
                   stacked=True, 
                   title='Survival Rate by Passenger Classes')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')

# Plot survival rate by Sex
females_df = df_train[df_train['Sex'] == 'female']
females_xt = pd.crosstab(females_df['Pclass'], df_train['Survived'])
females_xt_pct = females_xt.div(females_xt.sum(1).astype(float), axis=0)
females_xt_pct.plot(kind='bar', 
                    stacked=True, 
                    title='Female Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')

# Plot survival rate by Pclass
males_df = df_train[df_train['Sex'] == 'male']
males_xt = pd.crosstab(males_df['Pclass'], df_train['Survived'])
males_xt_pct = males_xt.div(males_xt.sum(1).astype(float), axis=0)
males_xt_pct.plot(kind='bar', 
                  stacked=True, 
                  title='Male Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')

show()

#Scatter Plots, subplots

# Set up a grid of plots
fig, axes = plt.subplots(2, 1, figsize=figsize_with_subplots)

# Histogram of AgeFill segmented by Survived
df1 = df_train[df_train['Survived'] == 0]['Age']
df2 = df_train[df_train['Survived'] == 1]['Age']
max_age = max(df_train['AgeFill'])

axes[1].hist([df1, df2], 
             bins=max_age / 10, 
             range=(1, max_age), 
             stacked=True)
axes[1].legend(('Died', 'Survived'), loc='best')
axes[1].set_title('Survivors by Age Groups Histogram')
axes[1].set_xlabel('Age')
axes[1].set_ylabel('Count')

# Scatter plot Survived and AgeFill
axes[0].scatter(df_train['Survived'], df_train['AgeFill'])
axes[0].set_title('Survivors by Age Plot')
axes[0].set_xlabel('Survived')
axes[0].set_ylabel('Age')

show()

#Kernel Density Estimation Plots

# Get the unique values of Pclass:
passenger_classes = np.sort(df_train['Pclass'].unique())

for pclass in passenger_classes:
    df_train.AgeFill[df_train.Pclass == pclass].plot(kind='kde')
plt.title('Age Density Plot by Passenger Class')
plt.xlabel('Age')
plt.legend(('1st Class', '2nd Class', '3rd Class'), loc='best')

show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Text and Annotation

import matplotlib as mpl

plt.style.use("seaborn-whitegrid")

# Example: Effect of Holidays on US Births

""" births.csv 15547筆資料 5欄位
year,month,day,gender,births
1969,1,1,F,4046
1969,1,1,M,4440
1969,1,2,F,4454
1969,1,2,M,4548
"""

births = pd.read_csv("data/births.csv")

quartiles = np.percentile(births["births"], [25, 50, 75])
mu, sig = quartiles[1], 0.74 * (quartiles[2] - quartiles[0])
births = births.query("(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)")

births["day"] = births["day"].astype(int)

births.index = pd.to_datetime(
    10000 * births.year + 100 * births.month + births.day, format="%Y%m%d"
)
births_by_date = births.pivot_table("births", [births.index.month, births.index.day])
births_by_date.index = [
    pd.datetime(2012, month, day) for (month, day) in births_by_date.index
]

fig, ax = plt.subplots(figsize=(12, 8))
births_by_date.plot(ax=ax)
show()


# 畫上一些註解

fig, ax = plt.subplots(figsize=(12, 8))
births_by_date.plot(ax=ax)

# Add labels to the plot
style = dict(size=10, color="gray")

ax.text("2012-1-1", 3950, "New Year's Day", **style)
ax.text("2012-7-4", 4250, "Independence Day", ha="center", **style)
ax.text("2012-9-4", 4850, "Labor Day", ha="center", **style)
ax.text("2012-10-31", 4600, "Halloween", ha="right", **style)
ax.text("2012-11-25", 4450, "Thanksgiving", ha="center", **style)
ax.text("2012-12-25", 3850, "Christmas ", ha="right", **style)

# Label the axes
ax.set(title="USA births by day of year (1969-1988)", ylabel="average daily births")

# Format the x axis with centered month labels
ax.xaxis.set_major_locator(mpl.dates.MonthLocator())
ax.xaxis.set_minor_locator(mpl.dates.MonthLocator(bymonthday=15))
ax.xaxis.set_major_formatter(plt.NullFormatter())
ax.xaxis.set_minor_formatter(mpl.dates.DateFormatter("%h"))
show()


# Transforms and Text Position

fig, ax = plt.subplots(facecolor="lightgray")
ax.axis([0, 10, 0, 10])

# transform=ax.transData is the default, but we'll specify it anyway
ax.text(1, 5, ". Data: (1, 5)", transform=ax.transData)
ax.text(0.5, 0.1, ". Axes: (0.5, 0.1)", transform=ax.transAxes)
ax.text(0.2, 0.2, ". Figure: (0.2, 0.2)", transform=fig.transFigure)
show()


ax.set_xlim(0, 2)
ax.set_ylim(-6, 6)
fig.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Arrows and Annotation

fig, ax = plt.subplots()

x = np.linspace(0, 20, 1000)
ax.plot(x, np.cos(x))
ax.axis("equal")

ax.annotate(
    "local maximum",
    xy=(6.28, 1),
    xytext=(10, 4),
    arrowprops=dict(facecolor="black", shrink=0.05),
)

ax.annotate(
    "local minimum",
    xy=(5 * np.pi, -1),
    xytext=(2, -6),
    arrowprops=dict(arrowstyle="->", connectionstyle="angle3,angleA=0,angleB=-90"),
)
show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(figsize=(12, 8))
births_by_date.plot(ax=ax)

# Add labels to the plot
ax.annotate(
    "New Year's Day",
    xy=("2012-1-1", 4100),
    xycoords="data",
    xytext=(50, -30),
    textcoords="offset points",
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.2"),
)

ax.annotate(
    "Independence Day",
    xy=("2012-7-4", 4250),
    xycoords="data",
    bbox=dict(boxstyle="round", fc="none", ec="gray"),
    xytext=(10, -40),
    textcoords="offset points",
    ha="center",
    arrowprops=dict(arrowstyle="->"),
)

ax.annotate(
    "Labor Day",
    xy=("2012-9-4", 4850),
    xycoords="data",
    ha="center",
    xytext=(0, -20),
    textcoords="offset points",
)
ax.annotate(
    "",
    xy=("2012-9-1", 4850),
    xytext=("2012-9-7", 4850),
    xycoords="data",
    textcoords="data",
    arrowprops={
        "arrowstyle": "|-|,widthA=0.2,widthB=0.2",
    },
)

ax.annotate(
    "Halloween",
    xy=("2012-10-31", 4600),
    xycoords="data",
    xytext=(-80, -40),
    textcoords="offset points",
    arrowprops=dict(
        arrowstyle="fancy",
        fc="0.6",
        ec="none",
        connectionstyle="angle3,angleA=0,angleB=-90",
    ),
)

ax.annotate(
    "Thanksgiving",
    xy=("2012-11-25", 4500),
    xycoords="data",
    xytext=(-120, -60),
    textcoords="offset points",
    bbox=dict(boxstyle="round4,pad=.5", fc="0.9"),
    arrowprops=dict(arrowstyle="->", connectionstyle="angle,angleA=0,angleB=80,rad=20"),
)


ax.annotate(
    "Christmas",
    xy=("2012-12-25", 3850),
    xycoords="data",
    xytext=(-30, 0),
    textcoords="offset points",
    size=13,
    ha="right",
    va="center",
    bbox=dict(boxstyle="round", alpha=0.1),
    arrowprops=dict(arrowstyle="wedge,tail_width=0.5", alpha=0.1),
)

# Label the axes
ax.set(title="USA births by day of year (1969-1988)", ylabel="average daily births")

# Format the x axis with centered month labels
ax.xaxis.set_major_locator(mpl.dates.MonthLocator())
ax.xaxis.set_minor_locator(mpl.dates.MonthLocator(bymonthday=15))
ax.xaxis.set_major_formatter(plt.NullFormatter())
ax.xaxis.set_minor_formatter(mpl.dates.DateFormatter("%h"))

ax.set_ylim(3600, 5400)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Customizing Ticks

# Major and Minor Ticks

plt.style.use("classic")

ax = plt.axes(xscale="log", yscale="log")
ax.grid()
show()

# tick properties—locations and labels

print(ax.xaxis.get_major_locator())
print(ax.xaxis.get_minor_locator())

print(ax.xaxis.get_major_formatter())
print(ax.xaxis.get_minor_formatter())

# Hiding Ticks or Labels

ax = plt.axes()
ax.plot(np.random.rand(50))

ax.yaxis.set_major_locator(plt.NullLocator())
ax.xaxis.set_major_formatter(plt.NullFormatter())
show()

# Notice that we've removed the labels (but kept the ticks/gridlines) from the x axis, and removed the ticks (and thus the labels as well) from the y axis. Having no ticks at all can be useful in many situations—for example, when you want to show a grid of images. For instance, consider the following figure, which includes images of different faces, an example often used in supervised machine learning problems (see, for example, In-Depth: Support Vector Machines):

fig, ax = plt.subplots(5, 5, figsize=(12, 8))
fig.subplots_adjust(hspace=0, wspace=0)

# Get some face data from scikit-learn
from sklearn.datasets import fetch_olivetti_faces

faces = fetch_olivetti_faces().images

for i in range(5):
    for j in range(5):
        ax[i, j].xaxis.set_major_locator(plt.NullLocator())
        ax[i, j].yaxis.set_major_locator(plt.NullLocator())
        ax[i, j].imshow(faces[10 * i + j], cmap="bone")
show()


# Reducing or Increasing the Number of Ticks

fig, ax = plt.subplots(4, 4, sharex=True, sharey=True)

# For every axis, set the x and y major locator
for axi in ax.flat:
    axi.xaxis.set_major_locator(plt.MaxNLocator(3))
    axi.yaxis.set_major_locator(plt.MaxNLocator(3))
fig.show()

# Fancy Tick Formats

# Plot a sine and cosine curve
fig, ax = plt.subplots()
x = np.linspace(0, 3 * np.pi, 1000)
ax.plot(x, np.sin(x), lw=3, label="Sine")
ax.plot(x, np.cos(x), lw=3, label="Cosine")

# Set up grid, legend, and limits
ax.grid(True)
ax.legend(frameon=False)
ax.axis("equal")
ax.set_xlim(0, 3 * np.pi)
show()

ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 4))
fig.show()


def format_func(value, tick_number):
    # find number of multiples of pi/2
    N = int(np.round(2 * value / np.pi))
    if N == 0:
        return "0"
    elif N == 1:
        return r"$\pi/2$"
    elif N == 2:
        return r"$\pi$"
    elif N % 2 > 0:
        return r"${0}\pi/2$".format(N)
    else:
        return r"${0}\pi$".format(N // 2)


ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func))
fig.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Settings-and-Stylesheets

# Customizing Matplotlib: Configurations and Stylesheets

# Plot Customization by Hand

plt.style.use("classic")

x = np.random.randn(1000)
plt.hist(x)
show()

# use a gray background
ax = plt.axes(facecolor="#E6E6E6")
ax.set_axisbelow(True)

# draw solid white grid lines
plt.grid(color="w", linestyle="solid")

# hide axis spines
for spine in ax.spines.values():
    spine.set_visible(False)

# hide top and right ticks
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()

# lighten ticks and labels
ax.tick_params(colors="gray", direction="out")
for tick in ax.get_xticklabels():
    tick.set_color("gray")
for tick in ax.get_yticklabels():
    tick.set_color("gray")

# control face and edge color of histogram
ax.hist(x, edgecolor="#E6E6E6", color="#EE6666")
show()

# Changing the Defaults: rcParams

IPython_default = plt.rcParams.copy()

from matplotlib import cycler

colors = cycler(
    "color", ["#EE6666", "#3388BB", "#9988DD", "#EECC55", "#88BB44", "#FFBBBB"]
)
plt.rc(
    "axes",
    facecolor="#E6E6E6",
    edgecolor="none",
    axisbelow=True,
    grid=True,
    prop_cycle=colors,
)
plt.rc("grid", color="w", linestyle="solid")
plt.rc("xtick", direction="out", color="gray")
plt.rc("ytick", direction="out", color="gray")
plt.rc("patch", edgecolor="#E6E6E6")
plt.rc("lines", linewidth=2)

# With these settings defined, we can now create a plot and see our settings in action:

plt.hist(x)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Let's see what simple line plots look like with these rc parameters:

for i in range(4):
    plt.plot(np.random.rand(10))
show()

print("------------------------------------------------------------")  # 60個

# Stylesheets

cc = plt.style.available[:5]
print(cc)

"""
plt.style.use('stylename')
with plt.style.context('stylename'):
    make_a_plot()
"""


def hist_and_lines():
    np.random.seed(0)
    fig, ax = plt.subplots(1, 2, figsize=(12, 8))
    ax[0].hist(np.random.randn(1000))
    for i in range(3):
        ax[1].plot(np.random.rand(10))
    ax[1].legend(["a", "b", "c"], loc="lower left")
    show()


# Default style

# reset rcParams
IPython_default = plt.rcParams.copy()
plt.rcParams.update(IPython_default)
show()


hist_and_lines()

# FiveThiryEight style

with plt.style.context("fivethirtyeight"):
    hist_and_lines()

# ggplot


with plt.style.context("ggplot"):
    hist_and_lines()

# Bayesian Methods for Hackers

with plt.style.context("bmh"):
    hist_and_lines()

# Dark background

with plt.style.context("dark_background"):
    hist_and_lines()

# Grayscale

with plt.style.context("grayscale"):
    hist_and_lines()

hist_and_lines()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
# Three-Dimensional Plotting in Matplotlib

from mpl_toolkits import mplot3d

fig = plt.figure()
ax = plt.axes(projection='3d')

show()

#Three-dimensional Points and Lines

ax = plt.axes(projection='3d')

# Data for a three-dimensional line
zline = np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'gray')

# Data for three-dimensional scattered points
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens')
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""



"""
# Geographic Data With Basemap
# pip install basemap
# pip install basemap-data-hires

from mpl_toolkits.basemap import Basemap

plt.figure(figsize=(12, 8))
m = Basemap(projection='ortho', resolution=None, lat_0=50, lon_0=-100)
m.bluemarble(scale=0.5)
show()



fig = plt.figure(figsize=(12, 8))
m = Basemap(projection='lcc', resolution=None,
            width=8E6, height=8E6, 
            lat_0=45, lon_0=-100,)
m.etopo(scale=0.5, alpha=0.5)

# Map (long, lat) to (x, y) for plotting
x, y = m(-122.3, 47.6)
plt.plot(x, y, 'ok', markersize=5)
plt.text(x, y, ' Seattle', fontsize=12)
show()

# Map Projections

from itertools import chain

def draw_map(m, scale=0.2):
    # draw a shaded-relief image
    m.shadedrelief(scale=scale)
    
    # lats and longs are returned as a dictionary
    lats = m.drawparallels(np.linspace(-90, 90, 13))
    lons = m.drawmeridians(np.linspace(-180, 180, 13))

    # keys contain the plt.Line2D instances
    lat_lines = chain(*(tup[1][0] for tup in lats.items()))
    lon_lines = chain(*(tup[1][0] for tup in lons.items()))
    all_lines = chain(lat_lines, lon_lines)
    
    # cycle through these lines and set the desired style
    for line in all_lines:
        line.set(linestyle='-', alpha=0.3, color='w')

#Cylindrical projections

fig = plt.figure(figsize=(12, 8), edgecolor='w')
m = Basemap(projection='cyl', resolution=None,
            llcrnrlat=-90, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180, )
draw_map(m)
show()

#Pseudo-cylindrical projections

fig = plt.figure(figsize=(12, 8), edgecolor='w')
m = Basemap(projection='moll', resolution=None,
            lat_0=0, lon_0=0)
draw_map(m)
show()

# Perspective projections

fig = plt.figure(figsize=(12, 8))
m = Basemap(projection='ortho', resolution=None,
            lat_0=50, lon_0=0)
draw_map(m)
show()

# Conic projections

fig = plt.figure(figsize=(12, 8))
m = Basemap(projection='lcc', resolution=None,
            lon_0=0, lat_0=50, lat_1=45, lat_2=55,
            width=1.6E7, height=1.2E7)
draw_map(m)
show()

print("------------------------------------------------------------")  # 60個

#Drawing a Map Background

from mpl_toolkits.basemap import Basemap

fig, ax = plt.subplots(1, 2, figsize=(12, 8))

for i, res in enumerate(['l', 'h']):
    m = Basemap(projection='gnom', lat_0=57.3, lon_0=-6.2,
                width=90000, height=120000, resolution=res, ax=ax[i])
    m.fillcontinents(color="#FFDDCC", lake_color='#DDEEFF')
    m.drawmapboundary(fill_color="#DDEEFF")
    m.drawcoastlines()
    ax[i].set_title("resolution='{0}'".format(res))

show()

#Plotting Data on Maps

# Example: California Cities

from mpl_toolkits.basemap import Basemap

cities = pd.read_csv('data/california_cities.csv')

# Extract the data we're interested in
lat = cities['latd'].values
lon = cities['longd'].values
population = cities['population_total'].values
area = cities['area_total_km2'].values

# 1. Draw the map background
fig = plt.figure(figsize=(12, 8))
m = Basemap(projection='lcc', resolution='h', 
            lat_0=37.5, lon_0=-119,
            width=1E6, height=1.2E6)
m.shadedrelief()
m.drawcoastlines(color='gray')
m.drawcountries(color='gray')
m.drawstates(color='gray')

# 2. scatter city data, with color reflecting population
# and size reflecting area
m.scatter(lon, lat, latlon=True,
          c=np.log10(population), s=area,
          cmap='Reds', alpha=0.5)

# 3. create colorbar and legend
plt.colorbar(label=r'$\log_{10}({\rm population})$')
plt.clim(3, 7)

# make legend with dummy points
for a in [100, 300, 500]:
    plt.scatter([], [], c='k', alpha=0.5, s=a,
                label=str(a) + ' km$^2$')
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, loc='lower left')
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# Example: Surface Temperature Data
# https://data.giss.nasa.gov/pub/gistemp/
# !curl -O http://data.giss.nasa.gov/pub/gistemp/gistemp250.nc.gz
# !gunzip gistemp250.nc.gz
# pip install netcdf4

from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap

data = Dataset("D:/_git/vcs/_big_files/gistemp250_GHCNv4.nc")

from netCDF4 import date2index
from datetime import datetime

timeindex = date2index(datetime(2014, 1, 15), data.variables["time"])

lat = data.variables["lat"][:]
lon = data.variables["lon"][:]
lon, lat = np.meshgrid(lon, lat)
temp_anomaly = data.variables["tempanomaly"][timeindex]

fig = plt.figure(figsize=(12, 8))
m = Basemap(
    projection="lcc",
    resolution="c",
    width=8e6,
    height=8e6,
    lat_0=45,
    lon_0=-100,
)
m.shadedrelief(scale=0.5)
m.pcolormesh(lon, lat, temp_anomaly, latlon=True, cmap="RdBu_r")
plt.clim(-8, 8)
m.drawcoastlines(color="lightgray")

plt.title("January 2014 Temperature Anomaly")
plt.colorbar(label="temperature anomaly (°C)")
show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x)

plt.plot(x, y, color="red")
plt.plot(x, z, "b--")

plt.ylim(-1.2, 1.2)

import io

buf = io.BytesIO()  # 建立一個用來儲存圖形內容的BytesIO物件
plt.savefig(buf, format="png")  # 將圖形以png格式儲存進buf中
cc = buf.getvalue()[:20]  # 顯示圖形內容的前20個位元組
print(cc)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("設定線圖的透明度")
x = np.arange(0, 5, 0.1)

line = plt.plot(x, 0.05 * x * x, "r")[0]  # plot傳回一個清單
line.set_alpha(0.3)  # 呼叫Line2D物件的set_*()方法設定屬性值

line = plt.plot(x, 0.08 * x * x, "r")[0]  # plot傳回一個清單
line.set_alpha(0.6)  # 呼叫Line2D物件的set_*()方法設定屬性值

line = plt.plot(x, 0.10 * x * x, "r")[0]  # plot傳回一個清單
line.set_alpha(0.9)  # 呼叫Line2D物件的set_*()方法設定屬性值

show()

print("------------------------------------------------------------")  # 60個

from matplotlib import style

print(style.available)

style.use("ggplot")  # 使用ggplot型態繪圖

x = np.linspace(0, 10, 1000)
y = np.sin(x)

plt.plot(x,y)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#在圖表中顯示中文

from matplotlib.font_manager import fontManager

cc = fontManager.ttflist[:6]
print(cc)

print(fontManager.ttflist[0].name)
print(fontManager.ttflist[0].fname)

plt.close("all")

# 顯示系統中所有的中文字型名

fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(111)
plt.subplots_adjust(0, 0, 1, 1, 0, 0)
plt.xticks([])
plt.yticks([])
x, y = 0.05, 0.05
fonts = [font.name for font in fontManager.ttflist if 
             os.path.exists(font.fname) and os.stat(font.fname).st_size>1e6]
font = set(fonts)
dy = (1.0 - y) / (len(fonts) // 4 + (len(fonts)%4 != 0))

for font in fonts:
    t = ax.text(x, y + dy / 2, u"中文字型", 
                {'fontname':font, 'fontsize':14}, transform=ax.transAxes)
    ax.text(x, y, font, {'fontsize':12}, transform=ax.transAxes)
    x += 0.25
    if x >= 1.0:
        y += dy
        x = 0.05

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)

x = np.linspace(0, 10, 1000)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel("時間", fontproperties=font)
plt.ylabel("振幅", fontproperties=font)
plt.title("正弦波", fontproperties=font)

show()

print("------------------------------------------------------------")  # 60個

#Artist物件

fig = plt.figure()

#新增軸, 水平 : 0.15~0.7, 垂直 : 0.1~0.3
ax = fig.add_axes([0.15, 0.1, 0.7, 0.3])

line = ax.plot([1, 2, 3], [1, 2, 1])[0]  # 傳回的是只有一個元素的清單
print(line is ax.lines[0])

ax.set_xlabel("水平軸")
ax.set_ylabel("垂直軸")
print("ax.xaxis:", ax.xaxis)
print('ax.xaxis.label:', ax.xaxis.label)
print('ax.xaxis.label._text :', ax.xaxis.label._text)

cc = ax.get_xaxis().get_label().get_text()
print('x軸 :', cc)
cc = ax.get_yaxis().get_label().get_text()
print('y軸 :', cc)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#Artist的屬性

fig = plt.figure()
fig.patch.set_color("g") # 設定背景彩色為綠色

line = plt.plot([1, 2, 3, 2, 1], lw=4)[0]
line.set_alpha(0.5)

show()

line.set(alpha=0.5, zorder=2)

show()

cc = plt.getp(fig.patch)
print(cc)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

fig = plt.figure()

ax1 = fig.add_subplot(211)
ax2 = fig.add_axes([0.1, 0.1, 0.7, 0.3])

print(ax1 in fig.axes and ax2 in fig.axes)

show()

for ax in fig.axes:
    ax.grid(True)

from matplotlib.lines import Line2D

fig = plt.figure()
line1 = Line2D(
    [0, 1], [0, 1], transform=fig.transFigure, figure=fig, color="r")
line2 = Line2D(
    [0, 1], [1, 0], transform=fig.transFigure, figure=fig, color="g")
fig.lines.extend([line1, line2])

show()

print("------------------------------------------------------------")  # 60個

#Axes容器

fig = plt.figure()
ax = fig.add_subplot(111)
ax.patch.set_facecolor("green")

x, y = np.random.rand(2, 100)
line = ax.plot(x, y, "-", color="blue", linewidth=2)[0]
cc = line is ax.lines[0]
print(cc)

show()

fig, ax = plt.subplots()
n, bins, rects = ax.hist(np.random.randn(1000), 50, facecolor="blue")
cc = rects[0] is ax.patches[0]
print(cc)

show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots()
rect = plt.Rectangle((1,1), width=5, height=12)

show()

ax.add_patch(rect) # 將rect加入進ax
#cc = rect.get_axes()
#print(cc)

fig, ax = plt.subplots()
t = ax.scatter(np.random.rand(20), np.random.rand(20))
print(t, t in ax.collections)

show()

print("------------------------------------------------------------")  # 60個

#Axis容器

fig, ax = plt.subplots()
axis = ax.xaxis

show()

cc = axis.get_ticklocs()
print(cc)

print(axis.get_ticklabels()) # 獲得刻度標簽清單
print([x.get_text() for x in axis.get_ticklabels()]) # 獲得刻度的文字字串

cc = axis.get_ticklines()
print(cc)

cc = axis.get_ticklines(minor=True) # 獲得副刻度線清單

print(cc)

# 組態X軸的刻度線和刻度文字的型態
for label in axis.get_ticklabels():
    label.set_color("red")
    label.set_rotation(45)
    label.set_fontsize(16)
     
for line in axis.get_ticklines():
    line.set_color("green")
    line.set_markersize(25)
    line.set_markeredgewidth(3)
fig

show()

print(axis.get_minor_locator()) # 計算副刻度位置的物件
print(axis.get_major_locator()) # 計算主刻度位置的物件

print("------------------------------------------------------------")  # 60個

# 組態X軸的刻度線的位置和文字，並開啟副刻度線

from fractions import Fraction
from matplotlib.ticker import MultipleLocator, FuncFormatter

x = np.arange(0, 4*np.pi, 0.01)
fig, ax = plt.subplots(figsize=(8,4))
plt.plot(x, np.sin(x), x, np.cos(x))

def pi_formatter(x, pos):
    frac = Fraction(int(np.round(x / (np.pi/4))), 4)
    d, n = frac.denominator, frac.numerator
    if frac == 0:
        return "0"
    elif frac == 1:
        return "$\pi$"
    elif d == 1:
        return r"${%d} \pi$" % n
    elif n == 1:
        return r"$\frac{\pi}{%d}$" % d
    return r"$\frac{%d \pi}{%d}$" % (n, d)

# 設定兩個座標軸的範圍
plt.ylim(-1.5,1.5)
plt.xlim(0, np.max(x))

# 設定圖的底邊距
plt.subplots_adjust(bottom = 0.15)

# 主刻度為pi/4
ax.xaxis.set_major_locator( MultipleLocator(np.pi/4) )

# 主刻度文字用pi_formatter函數計算
ax.xaxis.set_major_formatter( FuncFormatter( pi_formatter ) )

# 副刻度為pi/20
ax.xaxis.set_minor_locator( MultipleLocator(np.pi/20) )

# 設定刻度文字的大小
for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontsize(16)

show()

print("------------------------------------------------------------")  # 60個

# annotate
#座標變換和注解

# 為圖表加入各種注解元素

def func1(x):
    return 0.6*x + 0.3

def func2(x):
    return 0.4*x*x + 0.1*x + 0.2
    
def find_curve_intersects(x, y1, y2):
    d = y1 - y2
    idx = np.where(d[:-1]*d[1:]<=0)[0]
    x1, x2 = x[idx], x[idx+1]
    d1, d2 = d[idx], d[idx+1]
    return -d1*(x2-x1)/(d2-d1) + x1

x = np.linspace(-3,3,100)
f1 = func1(x)
f2 = func2(x)
fig, ax = plt.subplots(figsize=(8,4))
ax.plot(x, f1)
ax.plot(x, f2)

x1, x2 = find_curve_intersects(x, f1, f2)
ax.plot(x1, func1(x1), "o") 
ax.plot(x2, func1(x2), "o")

ax.fill_between(x, f1, f2, where=f1>f2, facecolor="green", alpha=0.5)

from matplotlib import transforms

trans = transforms.blended_transform_factory(ax.transData, ax.transAxes)
ax.fill_between([x1, x2], 0, 1, transform=trans, alpha=0.1)

a = ax.text(0.05, 0.95, u"直線和二次曲線的交點",
    transform=ax.transAxes,
    verticalalignment = "top",
    fontsize = 18,
    bbox={"facecolor":"red","alpha":0.4,"pad":10}
)

arrow = {"arrowstyle":"fancy,tail_width=0.6", 
         "facecolor":"gray", 
         "connectionstyle":"arc3,rad=-0.3"}

ax.annotate(u"交點",
    xy=(x1, func1(x1)), xycoords="data",
    xytext=(0.05, 0.5), textcoords="axes fraction",
    arrowprops = arrow)
                  
ax.annotate(u"交點",
    xy=(x2, func1(x2)), xycoords="data",
    xytext=(0.05, 0.5), textcoords="axes fraction",
    arrowprops = arrow)

xm = (x1+x2)/2
ym = (func1(xm) - func2(xm))/2+func2(xm)
o = ax.annotate(u"直線大於曲線區域",
    xy =(xm, ym), xycoords="data",
    xytext = (30, -30), textcoords="offset points",    
    bbox={"boxstyle":"round", "facecolor":(1.0, 0.7, 0.7), "edgecolor":"none"},
    fontsize=16,
    arrowprops={"arrowstyle":"->"}
)

show()

print("------------------------------------------------------------")  # 60個

#四種座標系

print(type(ax.transData))
ax.transData.transform([(-3,-2), (3,5)])

ax.transAxes.transform([(0,0), (1,1)])

fig.transFigure.transform([(0,0), (1,1)])

inv = ax.transData.inverted()
print(type(inv))
inv.transform((320, 160))

print(ax.set_xlim(-3, 2)) # 設定X軸的範圍為-3到2
print(ax.transData.transform((3, 5))) # 資料座標變換物件已經發生了變化

#使用axvspan()和axhspan()可以快速繪制垂直方向和水平方向上的區間。

#座標變換的管線

cc = fig.dpi_scale_trans == fig.transFigure._boxout._transform
print(cc)

cc = ax.transAxes._boxout._transform == fig.transFigure
print(cc)

cc = ax.get_position()
print(cc)

cc = ax.transAxes._boxout.bounds
print(cc)

print(ax.transLimits.transform((-3, -2)))
print(ax.transLimits.transform((2, 5)))

print(ax.get_xlim()) # 獲得X軸的顯示範圍
print(ax.get_ylim()) # 獲得Y軸的顯示範圍

t = ax.transLimits + ax.transAxes
print(t.transform((0,0)))
print(ax.transData.transform((0,0)))

cc = ax.transScale
print(cc)

#TransformWrapper(BlendedAffine2D(IdentityTransform(),IdentityTransform()))

#由於本例中的X軸的取值範圍是(-3,3)，因此若果將X軸改為對數座標，並且重新繪圖，會產生很多錯誤訊息。

# X軸為對數座標時的transScale物件的內定結構
ax.set_xscale("log") # 將X軸改為對數座標
# dddd %dot GraphvizMPLTransform.graphviz(ax.transScale)
ax.set_xscale("linear") # 將X軸改為線性座標

print("------------------------------------------------------------")  # 60個

#製作陰影效果

from matplotlib import transforms

# 使用座標變換繪制的帶陰影的曲線
fig, ax = plt.subplots()
x = np.arange(0., 2., 0.01)
y = np.sin(2*np.pi*x)

N = 7 # 陰影的條數
for i in range(N, 0, -1):
    offset = transforms.ScaledTranslation(i, -i, transforms.IdentityTransform())
    shadow_trans = plt.gca().transData + offset
    ax.plot(x,y,linewidth=4,color="black", 
        transform=shadow_trans,
        alpha=(N-i)/2.0/N)
    
ax.plot(x,y,linewidth=4,color='black')    
ax.set_ylim((-1.5, 1.5))

show()

cc = offset.transform((0,0)) # 將(0,0)變換為(1,-1)
print(cc)

print(ax.transData.transform((0,0))) # 對(0,0)進行資料座標變換
print(shadow_trans.transform((0,0))) # 對(0,0)進行資料座標變換和偏移變換

print("------------------------------------------------------------")  # 60個

#加入注解

# 三個座標系中的文字
x = np.linspace(-1,1,10)
y = x**2

fig, ax = plt.subplots(figsize=(8,4))
ax.plot(x,y)

for i, (_x, _y) in enumerate(zip(x, y)):
    ax.text(_x, _y, str(i), color="red", fontsize=i+10)

ax.text(0.5, 0.8, u"子圖座標系中的文字", color="blue", ha="center", 
    transform=ax.transAxes)
    
plt.figtext(0.1, 0.92, u"圖表座標系中的文字", color="green")

show()

print("------------------------------------------------------------")  # 60個

from matplotlib import collections as mc

#塊、路徑和集合
#Path與Patch

rect_patch = plt.Rectangle((0, 1), 2, 1)
rect_path = rect_patch.get_path()
print(rect_path.vertices)
print(rect_path.codes)

tran = rect_patch.get_patch_transform()
cc = tran.transform(rect_path.vertices)
print(cc)

ax = plt.gca()

ax.set_aspect("equal")
ax.invert_yaxis()
ax.autoscale()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

X, Y = np.mgrid[-2:2:5j, -2:2:5j]
init_pos = np.c_[X.ravel(), Y.ravel()]
t = np.linspace(0, 5, 50)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.5))  # 1X2 子圖
fig.subplots_adjust(0, 0, 1, 1)
ax1.plot(init_pos[:, 0], init_pos[:, 1], "x")
ax2.plot(init_pos[:, 0], init_pos[:, 1], "o")

ax1.autoscale()
ax1.set_aspect("equal")

ax2.autoscale()
ax2.set_aspect("equal")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#多邊形集合(PolyCollection)

# 用PolyCollection繪制大量多邊形
from numpy.random import randint, rand, uniform
from matplotlib import collections as mc

def star_polygon(x, y, r, theta, n, s): 
    angles = np.arange(0, 2*np.pi, 2*np.pi/2/n) + theta
    xs = r * np.cos(angles)
    ys = r * np.sin(angles)
    xs[1::2] *= s
    ys[1::2] *= s
    xs += x
    ys += y
    return np.vstack([xs, ys]).T

stars = []
for i in range(1000):
    star = star_polygon(randint(800), randint(500), 
                        uniform(5, 20), uniform(0, 2*np.pi),
                        randint(3, 9), uniform(0.1, 0.7))
    stars.append(star)

fig, ax = plt.subplots(figsize=(10, 5))
polygons = mc.PolyCollection(stars, alpha=0.5, array=np.random.rand(len(stars)))
ax.add_collection(polygons)# add_collection 只能用 ax
ax.autoscale()
ax.margins(0)
ax.set_aspect("equal")

show()

print("length of facecolors:", len(polygons.get_facecolors()))
print("length of edgecolors:", len(polygons.get_edgecolors()))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#路徑集合(PathCollection)

N = 30
np.random.seed(42)
x = np.random.rand(N)
y = np.random.rand(N)
size = np.random.randint(20, 60, N)
value = np.random.rand(N)

fig, ax = plt.subplots()
pc = ax.scatter(x, y, s=size, c=value)

show()

print(pc.get_transforms().shape)
print(pc.get_transforms()[0]) #索引為0的點對應的縮放矩陣

print(pc.get_offsets()[0]) #索引為0的點對應的中心座標
#計算索引為0的點對應的螢幕座標
print(pc.get_offset_transform().transform(pc.get_offsets())[0])
print(pc.get_offset_transform() is ax.transData)

print(pc.get_transform())

#cc = pc.get_offset_position()
#print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#資料空間中的圓形集合物件

from matplotlib.collections import CircleCollection, Collection
from matplotlib.transforms import Affine2D

class DataCircleCollection(CircleCollection):

    def set_sizes(self, sizes):
        self._sizes = sizes

    def draw(self, render):
        ax = self.axes
        ms = np.zeros((len(self._sizes), 3, 3))
        ms[:, 0, 0] = self._sizes
        ms[:, 1, 1] = self._sizes
        ms[:, 2, 2] = 1
        self._transforms = ms

        m = ax.transData.get_affine().get_matrix().copy()
        m[:2, 2:] = 0
        self.set_transform(Affine2D(m))

        return Collection.draw(self, render)

# 使用DataCircleCollection繪制大量的圓形

data = np.loadtxt("data/venus-face.csv", delimiter=",", encoding='UTF-8-sig')
offsets = data[:, :2]
sizes = data[:, 2] * 1.05
colors = data[:, 3:] / 256.0

fig, axe = plt.subplots(figsize=(8, 8))
axe.set_rasterized(True)
cc = DataCircleCollection(sizes, facecolors=colors, edgecolors="w", linewidths=0.1,
                          offsets=offsets, transOffset=axe.transData)

axe.add_collection(cc)# add_collection 只能用 ax
axe.axis((0, 512, 512, 0))
axe.axis("off")

show()

print("------------------------------------------------------------")  # 60個

#繪圖函數簡介
#對數座標圖

# 低通濾波器的頻率響應：算術座標（左上）、X軸對數座標（右上）、Y軸對數座標（左下）、雙對數座標（右上） 
w = np.linspace(0.1, 1000, 1000)
p = np.abs(1/(1+0.1j*w)) # 計算低通濾波器的頻率響應

fig, axes = plt.subplots(2, 2)

functions = ("plot", "semilogx", "semilogy", "loglog")

for ax, fname in zip(axes.ravel(), functions):
    func = getattr(ax, fname)
    func(w, p, linewidth=2)
    ax.set_ylim(0, 1.5)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" NG
#柱狀圖

# 中國男女人口的年齡分佈圖
data = np.loadtxt("data/china_population.txt", encoding='UTF-8-sig')
width = (data[1,0] - data[0,0])*0.4
c1, c2 = plt.rcParams['axes.color_cycle'][:2]
plt.bar(data[:,0]-width, data[:,1]/1e7, width, color=c1, label=u"男")
plt.bar(data[:,0], data[:,2]/1e7, width, color=c2, label=u"女")
plt.xlim(-width, 100)
plt.xlabel("年齡")
plt.ylabel("人口（千萬）")
plt.legend()

show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 四邊形網格

X = np.array([[0, 1, 2], [0, 1, 2]])
Y = np.array([[0, 0.2, 0], [1, 0.8, 1]])
Z = np.array([[0.5, 0.8]])

# 示範pcolormesh()繪制的四邊形以及其填充彩色
plt.plot(X.ravel(), Y.ravel(), "ko")
plt.pcolormesh(X, Y, Z)
plt.margins(0.1)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 使用pcolormesh()繪制復數平面上的座標變換
def make_mesh(n):
    x, y = np.mgrid[-10 : 0 : n * 1j, -5 : 5 : n * 1j]

    s = x + 1j * y
    z = (2 + s) / (2 - s)
    return s, z


fig, axes = plt.subplots(2, 2, figsize=(8, 8))
axes = axes.ravel()
for ax in axes:
    ax.set_aspect("equal")

s1, z1 = make_mesh(10)
s2, z2 = make_mesh(200)
axes[0].pcolormesh(s1.real, s1.imag, np.abs(s1))
axes[1].pcolormesh(z1.real, z1.imag, np.abs(s1))
axes[2].pcolormesh(s2.real, s2.imag, np.abs(s2), rasterized=True)
axes[3].pcolormesh(z2.real, z2.imag, np.abs(s2), rasterized=True)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 使用pcolormesh()繪制極座標中的網格
def func(theta, r):
    y = theta * np.sin(r)
    return np.sqrt(y * y)


T, R = np.mgrid[0 : 2 * np.pi : 360j, 0:10:100j]
Z = func(T, R)

ax = plt.subplot(111, projection="polar", aspect=1.0)
ax.pcolormesh(T, R, Z, rasterized=True)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 箭頭圖


# 用quiver()繪制向量場
def f(x, y):
    return x * np.exp(-(x**2) - y**2)


def vec_field(f, x, y, dx=1e-6, dy=1e-6):
    x2 = x + dx
    y2 = y + dy
    v = f(x, y)
    vx = (f(x2, y) - v) / dx
    vy = (f(x, y2) - v) / dy
    return vx, vy


X, Y = np.mgrid[-2:2:20j, -2:2:20j]
C = f(X, Y)
U, V = vec_field(f, X, Y)
plt.quiver(X, Y, U, V, C)
plt.colorbar()
plt.gca().set_aspect("equal")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
# 使用箭頭表示參數曲線的切線方向
n = 40
arrow_size = 16
t = np.linspace(0, 1, 1000)
x = np.sin(3*2*np.pi*t)
y = np.cos(5*2*np.pi*t)
line, = plt.plot(x, y, lw=1)

lengths = np.cumsum(np.hypot(np.diff(x), np.diff(y)))
length = lengths[-1]
arrow_locations = np.linspace(0, length, n, endpoint=False)
index = np.searchsorted(lengths, arrow_locations)
dx = x[index + 1] - x[index]
dy = y[index + 1] - y[index]
ds = np.hypot(dx, dy)
dx /= ds
dy /= ds
plt.quiver(x[index], y[index], dx, dy, t[index],
          units="dots", scale_units="dots", 
          angles="xy", scale=1.0/arrow_size, pivot="middle",
          edgecolors="black", linewidths=1,
          width=1, headwidth=arrow_size*0.5, 
          headlength=arrow_size, headaxislength=arrow_size, 
          zorder=100)
plt.colorbar()
plt.xlim([-1.5, 1.5])
plt.ylim([-1.5, 1.5])

show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
#使用quiver()繪制神經網路結構示意圖
levels = [4, 5, 3, 2]
x = np.linspace(0, 1, len(levels))

for i in range(len(levels) - 1):
    j = i + 1
    n1, n2 = levels[i], levels[j]
    y1, y2 = np.mgrid[0:1:n1*1j, 0:1:n2*1j]
    x1 = np.full_like(y1, x[i])
    x2 = np.full_like(y2, x[j])
    plt.quiver(x1, y1, x2-x1, y2-y1, 
              angles="xy", units="dots", scale_units="xy", 
              scale=1, width=2, headlength=10,
              headaxislength=10, headwidth=4)
    
yp = np.concatenate([np.linspace(0, 1, n) for n in levels])
xp = np.repeat(x, levels)
plt.plot(xp, yp, "o", ms=12)
plt.gca().axis("off")
plt.margins(0.1, 0.1)

show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("plt響應滑鼠與鍵碟事件")

# 鍵碟事件

# scpy2.matplotlib.key_event_show_key：顯示觸發鍵碟按鍵事件的按鍵名稱。

fig, ax = plt.subplots()


def on_key_press(event):
    print(event.key)
    sys.stdout.flush()


fig.canvas.mpl_connect("key_press_event", on_key_press)

""" NG
for key, funcs in fig.canvas.callbacks.callbacks.iteritems():
    print(key)
    for cid, wrap in sorted(funcs.items()):
        func = wrap.func
        print("    {0}:{1}.{2}".format(cid, func.__module__, func))
"""
show()

print("------------------------------------------------------------")  # 60個

# scpy2.matplotlib.key_event_change_color：透過按鍵修改曲線的彩色。

fig, ax = plt.subplots()
x = np.linspace(0, 10, 1000)
(line,) = ax.plot(x, np.sin(x))


def on_key_press(event):
    if event.key in "rgbcmyk":
        line.set_color(event.key)
    fig.canvas.draw_idle()


fig.canvas.mpl_disconnect(fig.canvas.manager.key_press_handler_id)
fig.canvas.mpl_connect("key_press_event", on_key_press)

show()

print("------------------------------------------------------------")  # 60個

# 滑鼠事件

# scpy2.matplotlib.mouse_event_show_info：顯示子圖中的滑鼠事件的各種訊息。

fig, ax = plt.subplots()
text = ax.text(0.5, 0.5, "event", ha="center", va="center", fontdict={"size": 20})


def on_mouse(event):
    global e
    e = event
    info = "{}\nButton:{}\nFig x,y:{}, {}\nData x,y:{:3.2f}, {:3.2f}".format(
        event.name, event.button, event.x, event.y, event.xdata, event.ydata
    )
    text.set_text(info)
    fig.canvas.draw()


fig.canvas.mpl_connect("button_press_event", on_mouse)
fig.canvas.mpl_connect("button_release_event", on_mouse)
fig.canvas.mpl_connect("motion_notify_event", on_mouse)

show()

print("------------------------------------------------------------")  # 60個

# scpy2.matplotlib.mouse_event_move_polygon：示範透過滑鼠搬移Patch物件。

from numpy.random import rand, randint
from matplotlib.patches import RegularPolygon


class PatchMover(object):
    def __init__(self, ax):
        self.ax = ax
        self.selected_patch = None
        self.start_mouse_pos = None
        self.start_patch_pos = None

        fig = ax.figure
        fig.canvas.mpl_connect("button_press_event", self.on_press)
        fig.canvas.mpl_connect("button_release_event", self.on_release)
        fig.canvas.mpl_connect("motion_notify_event", self.on_motion)

    def on_press(self, event):
        patches = self.ax.patches[:]
        patches.sort(key=lambda patch: patch.get_zorder())
        for patch in reversed(patches):
            if patch.contains_point((event.x, event.y)):
                self.selected_patch = patch
                self.start_mouse_pos = np.array([event.xdata, event.ydata])
                self.start_patch_pos = patch.xy
                break

    def on_motion(self, event):
        if self.selected_patch is not None:
            pos = np.array([event.xdata, event.ydata])
            self.selected_patch.xy = self.start_patch_pos + pos - self.start_mouse_pos
            self.ax.figure.canvas.draw_idle()

    def on_release(self, event):
        self.selected_patch = None


fig, ax = plt.subplots()
ax.set_aspect("equal")
for i in range(10):
    poly = RegularPolygon(
        rand(2),
        randint(3, 10),
        rand() * 0.1 + 0.1,
        facecolor=rand(3),
        zorder=randint(10, 100),
    )
    ax.add_patch(poly)
ax.relim()
ax.autoscale()
pm = PatchMover(ax)

show()

print("------------------------------------------------------------")  # 60個

# 點選事件

# scpy2.matplotlib.pick_event_demo：示範繪圖物件的點選事件。


fig, ax = plt.subplots()
rect = plt.Rectangle((np.pi, -0.5), 1, 1, fc=np.random.random(3), picker=True)
ax.add_patch(rect)
x = np.linspace(0, np.pi * 2, 100)
y = np.sin(x)
(line,) = plt.plot(x, y, picker=8.0)


def on_pick(event):
    artist = event.artist
    if isinstance(artist, plt.Line2D):
        lw = artist.get_linewidth()
        artist.set_linewidth(lw % 5 + 1)
    else:
        artist.set_fc(np.random.random(3))
    fig.canvas.draw_idle()


fig.canvas.mpl_connect("pick_event", on_pick)

show()

print("------------------------------------------------------------")  # 60個

# 實時反白顯示曲線

# scpy2.matplotlib.mouse_event_highlight_curve：滑鼠搬移到曲線之上時反白顯示該曲線。


class CurveHighLighter(object):
    def __init__(self, ax, alpha=0.3, linewidth=3):
        self.ax = ax
        self.alpha = alpha
        self.linewidth = 3

        ax.figure.canvas.mpl_connect("motion_notify_event", self.on_move)

    def highlight(self, target):
        need_redraw = False
        if target is None:
            for line in self.ax.lines:
                line.set_alpha(1.0)
                if line.get_linewidth() != 1.0:
                    line.set_linewidth(1.0)
                    need_redraw = True
        else:
            for line in self.ax.lines:
                lw = self.linewidth if line is target else 1
                if line.get_linewidth() != lw:
                    line.set_linewidth(lw)
                    need_redraw = True
                alpha = 1.0 if lw == self.linewidth else self.alpha
                line.set_alpha(alpha)

        if need_redraw:
            self.ax.figure.canvas.draw_idle()

    def on_move(self, evt):
        ax = self.ax
        for line in ax.lines:
            if line.contains(evt)[0]:
                self.highlight(line)
                break
        else:
            self.highlight(None)


fig, ax = plt.subplots()
x = np.linspace(0, 50, 300)

from scipy.special import jn

for i in range(1, 10):
    ax.plot(x, jn(i, x))

ch = CurveHighLighter(ax)
show()

print("------------------------------------------------------------")  # 60個

# 動畫

fig, ax = plt.subplots()
x = np.linspace(0, 10, 1000)
(line,) = ax.plot(x, np.sin(x), lw=2)


def update_data(line):
    x[:] += 0.1
    line.set_ydata(np.sin(x))
    fig.canvas.draw()


timer = fig.canvas.new_timer(interval=50)
timer.add_callback(update_data, line)
timer.start()

print("------------------------------------------------------------")  # 60個

# 使用快取快速重繪圖表

fig, ax = plt.subplots()
x = np.linspace(0, 10, 1000)
(line,) = ax.plot(x, np.sin(x), lw=2, animated=True)

fig.canvas.draw()
background = fig.canvas.copy_from_bbox(ax.bbox)


def update_data(line):
    x[:] += 0.1
    line.set_ydata(np.sin(x))
    fig.canvas.restore_region(background)
    ax.draw_artist(line)
    fig.canvas.blit(ax.bbox)


timer = fig.canvas.new_timer(interval=50)
timer.add_callback(update_data, line)
timer.start()

# animation模組

from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

x = np.linspace(0, 4 * np.pi, 200)
y = np.sin(x)
(line,) = ax.plot(x, y, lw=2, animated=True)


def update_line(i):
    y = np.sin(x + i * 2 * np.pi / 100)
    line.set_ydata(y)
    return [line]


ani = FuncAnimation(fig, update_line, blit=True, interval=25, frames=100)

# matplotlib會使用系統中安裝的視訊壓縮軟體（如ffmpeg.exe）產生視訊檔案。
# 請讀者確認視訊壓縮軟體的可執行檔案的路徑是否在PATH環境變數中。

ani.save("tmp_sin_wave.mp4", fps=25)

# 加入GUI面板

# scpy2.matplotlib.gui_panel：提供了TK與QT界面庫的滑標控制項面板類別TkSliderPanel和QtSliderPanel。
# tk_panel_demo.py和qt_panel_demo.py為其示範程式。

import matplotlib

matplotlib.use("TkAgg")

import pylab as pl


def exp_sin(x, A, f, z, p):
    return A * np.sin(2 * np.pi * f * x + p) * np.exp(z * x)


fig, ax = pl.subplots()

x = np.linspace(1e-6, 1, 500)
pars = {"A": 1.0, "f": 2, "z": -0.2, "p": 0}
y = exp_sin(x, **pars)

(line,) = pl.plot(x, y)


def update(**kw):
    y = exp_sin(x, **kw)
    line.set_data(x, y)
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw_idle()


from scpy2.matplotlib.gui_panel import TkSliderPanel

panel = TkSliderPanel(
    fig,
    [("A", 0, 10), ("f", 0, 10), ("z", -3, 0), ("p", 0, 2 * np.pi)],
    update,
    cols=2,
    min_value_width=80,
)
panel.set_parameters(**pars)
fig.show()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from mpl_toolkits import mplot3d
from matplotlib import cm
import matplotlib	

feature_x = np.linspace(-5.0, 5.0, 1000)
feature_y = np.linspace(-5.0, 5.0, 1000)
  
# Creating 2-D grid of features
[X, Y] = np.meshgrid(feature_x, feature_y)
z=(X+Y*1j)
  
fig, ax = plt.subplots(1, 1)
Z = np.sqrt(X ** 2 + Y ** 2)
ax.set_aspect('equal', adjustable='box')

# plots filled contour plot

ax.pcolormesh(X, Y, Z, cmap="hsv", vmin=-(np.pi), vmax=(np.pi))
ax.pcolormesh(X, Y, Z, cmap="viridis", norm=matplotlib.colors.LogNorm())

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

def binary_step(x):
    return 0 if x < 0 else 1


def logistic(x):
    return 1 / (1 + math.exp(-x))


def tanh(x):
    return math.tanh(x)


def relu(x):
    return 0 if x < 0 else x


x = np.linspace(-5, 5, 100)

bs = [binary_step(x_) for x_ in x]
lf = [logistic(x_) for x_ in x]
th = [tanh(x_) for x_ in x]
re = [relu(x_) for x_ in x]

_, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 10))

ax1.set_title("Binary step")
ax2.set_title("TanH")
ax3.set_title("Logistic")
ax4.set_title("ReLU")

ax1.plot(x, bs)
ax2.plot(x, lf)
ax3.plot(x, th)
ax4.plot(x, re)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# AND, OR vs XOR

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
Y_and = [0, 0, 0, 1]
Y_or = [0, 1, 1, 1]
Y_xor = [0, 1, 1, 0]

titles = ("AND", "OR", "XOR")

for i, Y in enumerate([Y_and, Y_or, Y_xor]):
    ax = plt.subplot(131 + i)

    ax.set_xlim([-0.5, 1.5])
    ax.set_ylim([-0.5, 1.5])

    ax.set_aspect("equal")

    plt.title(titles[i])
    plt.scatter(*zip(*X), c=Y)

    if i == 0:
        plt.plot([0, 1.5], [1.5, 0])
    elif i == 1:
        plt.plot([-0.5, 1], [1, -0.5])
    else:
        plt.text(0.5, 0.5, s="?", ha="center", va="center")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

def dice_roll():
    v = random.randint(1, 6)
    return v

num_of_trials = range(100, 10000, 10)
avgs = []
for num_of_trial in num_of_trials:  
    trials = []    
    for trial in range(num_of_trial):
        trials.append(dice_roll())
    avgs.append(sum(trials)/float(num_of_trial))

plt.plot(num_of_trials, avgs)
plt.xlabel("試驗次數")
plt.ylabel("平均")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def normal_pdf(x, mu, sigma):
    pi = 3.1415926
    e = 2.718281
    f = (1./np.sqrt(2*pi*sigma**2))*e**(-(x-mu)**2/(2.*sigma**2))
    return f

ax = np.linspace(-5, 5, 100)
ay = [normal_pdf(x, 0, 1) for x in ax]  
plt.plot(ax, ay)
show()

print("------------------------------------------------------------")  # 60個

x = range(1, 11)  # 1 2 3 ... 10
y = range(1, 11)  # 1 2 3 ... 10
X, Y = np.meshgrid(x, y)

size = [i * 80 for i in Y]  # 放大資料點數據 N 倍，比較容易觀察尺寸
plt.scatter(X, Y, s=size, c=size, cmap="Set1")  # 使用 Set1 的 colormap
show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots()
ax.plot(np.linspace(0, 2 * np.pi, 10), np.sin(np.linspace(0, 2 * np.pi, 10)))
show()

print("------------------------------------------------------------")  # 60個

# Momentum

# Online learning may help to escape local minima

x = np.linspace(-2, 2, 100)
y1 = x**2
y2 = np.array([a**2 + np.sin(5 * a) for a in x])

plt.subplot(121)
plt.plot(x, y1)
plt.scatter([-1.5], [3], c="k", s=300)

plt.subplot(122)
plt.plot(x, y2)
plt.scatter([-1.45], [1.75], c="k", s=300)
show()

print("------------------------------------------------------------")  # 60個

N = 50
A = 100
spread = np.random.rand(N) * A  # 放大 A 倍 原本0~1 後來 0~1*A
print(spread)

print()
center = np.ones(N//2) * N
print(center)

flier_high = np.random.rand(N//5) * A + A
flier_low = np.random.rand(N//5) * -A
data = np.concatenate((spread, center, flier_high, flier_low), 0)

plt.boxplot(data)
#plt.hist(data)

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
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

""" 新進

plt.plot(x, y, '-p', color='gray',
         markersize=15, linewidth=4,
         markerfacecolor='white',
         markeredgecolor='gray',
         markeredgewidth=2)
plt.ylim(-1.2, 1.2)



plt.hist(data, bins=30, normed=True, alpha=0.5,
         histtype='stepfilled', color='steelblue',
         edgecolor='none')




legend 無邊框 兩欄
ax.legend(frameon=False, loc='lower center', ncol=2)


ax.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1)

plt.legend(framealpha=1, frameon=True)


"""


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

"""

plt.savefig("test.png", dpi=120)
    TIP
    若果關閉了圖表視窗，則無法使用savefig()儲存圖形。實際上不需要呼叫show()顯示圖表，可以直接用savefig()將圖表儲存成圖形檔案。使用這種方法可以很容易撰寫批次輸出圖表的程式。

print xxxx
print(

b'\n\n\n

show()

print("------------------------------------------------------------")  # 60個

with open(filename, "r", encoding='UTF-8-sig') as f:

"""

plt.close("all")







cx, cy = 100, 100
R = 100
for i in range(5):
    angle = -90 + 72 * i;
    X = int(R * np.cos(angle * np.pi / 180))+cx
    Y = int(R * np.sin(angle * np.pi / 180))+cy
    print(X, Y, end=" ")
print()

cx, cy = 300, 100
R = 100
for i in range(5):
    angle = -90 + 72 * i;
    X = int(R * np.cos(angle * np.pi / 180))+cx
    Y = int(R * np.sin(angle * np.pi / 180))+cy
    print(X, Y, end=" ")
print()

cx, cy = 200, 300
R = 100
for i in range(5):
    angle = -90 + 72 * i;
    X = int(R * np.cos(angle * np.pi / 180))+cx
    Y = int(R * np.sin(angle * np.pi / 180))+cy
    print(X, Y, end=" ")
print()



