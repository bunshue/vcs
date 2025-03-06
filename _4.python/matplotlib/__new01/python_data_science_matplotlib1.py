"""
python_data_science_matplotlib1

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
    # plt.show()
    pass


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


def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)


x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 40)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.contour(X, Y, Z, colors="black")
show()

plt.contour(X, Y, Z, 20, cmap="RdGy")
show()

plt.contourf(X, Y, Z, 20, cmap="RdGy")
plt.colorbar()
show()


plt.imshow(Z, extent=[0, 5, 0, 5], origin="lower", cmap="RdGy")
plt.colorbar()
# plt.axis(aspect='image')
show()


contours = plt.contour(X, Y, Z, 3, colors="black")
plt.clabel(contours, inline=True, fontsize=8)

plt.imshow(Z, extent=[0, 5, 0, 5], origin="lower", cmap="RdGy", alpha=0.5)
plt.colorbar()
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
    """Return a grayscale version of the given colormap"""
    cmap = plt.cm.get_cmap(cmap)
    colors = cmap(np.arange(cmap.N))

    # convert RGBA to perceived grayscale luminance
    # cf. http://alienryderflex.com/hsp.html
    RGB_weight = [0.299, 0.587, 0.114]
    luminance = np.sqrt(np.dot(colors[:, :3] ** 2, RGB_weight))
    colors[:, :3] = luminance[:, np.newaxis]

    return LinearSegmentedColormap.from_list(cmap.name + "_gray", colors, cmap.N)


def view_colormap(cmap):
    """Plot a colormap with its grayscale equivalent"""
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

plt.figure(figsize=(10, 3.5))

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
plt.rc("figure", figsize=(10, 5))

# Set seaborn aesthetic parameters to defaults
sns.set()

# Basic Plots

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
plt.rc('figure', figsize=(10, 5))

# Set seaborn aesthetic parameters to defaults
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



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Text and Annotation

import matplotlib as mpl

plt.style.use("seaborn-whitegrid")

# Example: Effect of Holidays on US Births

"""
births.csv 15547筆資料 5欄位
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

fig, ax = plt.subplots(figsize=(12, 4))
births_by_date.plot(ax=ax)
show()


# 畫上一些註解

fig, ax = plt.subplots(figsize=(12, 4))
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

fig, ax = plt.subplots(figsize=(12, 4))
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

fig, ax = plt.subplots(5, 5, figsize=(5, 5))
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
    fig, ax = plt.subplots(1, 2, figsize=(11, 4))
    ax[0].hist(np.random.randn(1000))
    for i in range(3):
        ax[1].plot(np.random.rand(10))
    ax[1].legend(["a", "b", "c"], loc="lower left")
    plt.show()


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

# Seaborn style

import seaborn

hist_and_lines()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


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

# Three-dimensional Contour Plots


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
show()

ax.view_init(60, 35)
fig.show()


#Wireframes and Surface Plots

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_wireframe(X, Y, Z, color='black')
ax.set_title('wireframe')
show()


ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('surface')
show()

r = np.linspace(0, 6, 20)
theta = np.linspace(-0.9 * np.pi, 0.8 * np.pi, 40)
r, theta = np.meshgrid(r, theta)

X = r * np.sin(theta)
Y = r * np.cos(theta)
Z = f(X, Y)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
show()

#Surface Triangulations

theta = 2 * np.pi * np.random.random(1000)
r = 6 * np.random.random(1000)
x = np.ravel(r * np.sin(theta))
y = np.ravel(r * np.cos(theta))
z = f(x, y)

ax = plt.axes(projection='3d')
ax.scatter(x, y, z, c=z, cmap='viridis', linewidth=0.5)
show()


ax = plt.axes(projection='3d')
ax.plot_trisurf(x, y, z, cmap='viridis', edgecolor='none')
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#Example: Visualizing a Möbius strip

theta = np.linspace(0, 2 * np.pi, 30)
w = np.linspace(-0.25, 0.25, 8)
w, theta = np.meshgrid(w, theta)

phi = 0.5 * theta

# radius in x-y plane
r = 1 + w * np.cos(phi)

x = np.ravel(r * np.cos(theta))
y = np.ravel(r * np.sin(theta))
z = np.ravel(w * np.sin(phi))

# triangulate in the underlying parametrization
from matplotlib.tri import Triangulation
                                                                
tri = Triangulation(np.ravel(w), np.ravel(theta))

ax = plt.axes(projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles,
                cmap='viridis', linewidths=0.2)

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)

show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Geographic Data With Basemap
# pip install basemap
# pip install basemap-data-hires

from mpl_toolkits.basemap import Basemap

"""
plt.figure(figsize=(8, 8))
m = Basemap(projection='ortho', resolution=None, lat_0=50, lon_0=-100)
m.bluemarble(scale=0.5)
show()



fig = plt.figure(figsize=(8, 8))
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

fig = plt.figure(figsize=(8, 6), edgecolor='w')
m = Basemap(projection='cyl', resolution=None,
            llcrnrlat=-90, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180, )
draw_map(m)
show()

#Pseudo-cylindrical projections

fig = plt.figure(figsize=(8, 6), edgecolor='w')
m = Basemap(projection='moll', resolution=None,
            lat_0=0, lon_0=0)
draw_map(m)
show()

# Perspective projections

fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='ortho', resolution=None,
            lat_0=50, lon_0=0)
draw_map(m)
show()

# Conic projections

fig = plt.figure(figsize=(8, 8))
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
fig = plt.figure(figsize=(8, 8))
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
"""
print("------------------------------------------------------------")  # 60個

# Example: Surface Temperature Data
# https://data.giss.nasa.gov/pub/gistemp/
# !curl -O http://data.giss.nasa.gov/pub/gistemp/gistemp250.nc.gz
# !gunzip gistemp250.nc.gz
# pip install netcdf4

from netCDF4 import Dataset
from mpl_toolkits.basemap import Basemap

data = Dataset("C:/_git/vcs/_big_files/gistemp250_GHCNv4.nc")

from netCDF4 import date2index
from datetime import datetime

timeindex = date2index(datetime(2014, 1, 15), data.variables["time"])

lat = data.variables["lat"][:]
lon = data.variables["lon"][:]
lon, lat = np.meshgrid(lon, lat)
temp_anomaly = data.variables["tempanomaly"][timeindex]

fig = plt.figure(figsize=(10, 8))
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


print("------------------------------------------------------------")  # 60個


"""

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
