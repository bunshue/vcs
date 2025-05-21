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
'''
df = pd.read_csv('./data/winequality-red.csv', sep=';')
cc = df.head()
print(cc)

new_df = df.rename(columns={'fixed acidity': 'fixed_acidity',
                             'volatile acidity': 'volatile_acidity',
                             'citric acid': 'citric_acid',
                             'residual sugar': 'residual_sugar',
                             'free sulfur dioxide': 'free_sulfur_dioxide',
                             'total sulfur dioxide': 'total_sulfur_dioxide'
                            })
cc = new_df.head() 
print(cc)


def replace_labels(columns):
    labels = list(columns)
    
    for i in range(len(labels)):
        labels[i] = labels[i].replace(' ', '_')
    return labels

df.columns = replace_labels(df.columns)

cc = df.head()
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = pd.read_csv('./data/iris.csv')
renamed_columns = ['sepal length (cm)', 'sepal width (cm)', 
                   'petal length (cm)', 'petal width (cm)', 'species']
df.columns = renamed_columns
versicolor_petal_length = df[df['species'] == 'Versicolor']['petal length (cm)']
setosa_petal_length = df[df['species'] == 'Setosa']['petal length (cm)']
virginica_petal_length = df[df['species'] == 'Virginica']['petal length (cm)']


# Create bee swarm plot with Seaborn's default settings
_ = sns.swarmplot(x='species', y='petal length (cm)', data=df)

# Label the axes
_ = plt.xlabel('species')
_ = plt.ylabel('petal length (cm)')

show()

# plt.savefig('../images/iris-swarmplot.png')



# Create box plot with Seaborn`s default settings
_ = sns.boxplot(x='species', y='petal length (cm)', data=df)

# Label the axes
_ = plt.xlabel('species')
_ = plt.ylabel('petal length (cm)')

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = pd.read_csv('./data/frog_tongue.csv', skiprows=14)
df.head()

# Make bee swarm plot
_ = sns.swarmplot(x='ID', y='impact force (mN)', data=df)

# Label axes
_ = plt.xlabel('frog')
_ = plt.ylabel('impact force (mN)')

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
_ = plt.hist(samples_std1, histtype='step', density=True, bins=100)
_ = plt.hist(samples_std3, histtype='step', density=True, bins=100)
_ = plt.hist(samples_std10, histtype='step', density=True,bins=100)

# Make a legend, set limits
_ = plt.legend(('std = 1', 'std = 3', 'std = 10'))
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
_ = plt.hist(waiting_times, bins=100, density=True, histtype='step')

# Label axes
_ = plt.xlabel('waiting times')
_ = plt.ylabel('PDF')


show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = pd.read_csv('./data/female_literacy_fertility.csv')
fertility = np.array(df['fertility'])
illiteracy = np.array(100 - df['female literacy'])


# Plot the illiteracy rate versus fertility
_ = plt.plot(illiteracy, fertility, marker='.', linestyle='none')

# Set the margins and label axes
plt.margins(0.02)
_ = plt.xlabel('percent illiterate')
_ = plt.ylabel('fertility')

# Show the Pearson correlation coefficient
# xxx print(pearson_r(illiteracy, fertility))




# Plot the illiteracy rate versus fertility
_ = plt.plot(illiteracy, fertility, marker='.', linestyle='none')
plt.margins(0.02)
_ = plt.xlabel('percent illiterate')
_ = plt.ylabel('fertility')

# Perform a linear regression using np.polyfit(): a, b
a, b = np.polyfit(illiteracy, fertility, deg=1)

# Print the results to the screen
print('slope =', a, 'children per woman / percent illiterate')
print('intercept =', b, 'children per woman')

# Make theoretical line to plot
x = np.array([0, 100])
y = a * x + b

# Add regression line to your plot
_ = plt.plot(x, y)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = pd.read_csv('./data/anscombe.csv')
x = np.array(df.iloc[1:, 1].astype('float'))
y = np.array(df.iloc[1:, 2].astype('float'))

# Perform linear regression: a, b
a, b = np.polyfit(x, y, deg=1)

# Print the slope and intercept
print(a, b)

# Generate theoretical x and y data: x_theor, y_theor
x_theor = np.array([3, 15])
y_theor = a * x_theor + b

# Plot the Anscombe data and theoretical line
_ = plt.plot(x, y, marker='.', linestyle='none')
_ = plt.plot(x_theor, y_theor)

# Label the axes
plt.xlabel('x')
plt.ylabel('y')

show()
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df_1 = pd.read_csv('./data/finch_beaks_1975.csv')
df_2 = pd.read_csv('./data/finch_beaks_2012.csv')

df_1['year'] = 1975
df_2['year'] = 2012

df_1.columns = ['band', 'species', 'beak_length', 'beak_depth', 'year']
df_2.columns = ['band', 'species', 'beak_length', 'beak_depth', 'year']

df = pd.concat([df_1, df_2])
df.head()




# Create bee swarm plot
_ = sns.swarmplot(x='year', y='beak_depth', data=df)

# Label the axes
_ = plt.xlabel('year')
_ = plt.ylabel('beak depth (mm)')

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



bd_1975 = np.array(df[(df['year'] == 1975) & (df['species'] == 'scandens')]['beak_depth'])
bd_2012 = np.array(df[(df['year'] == 2012) & (df['species'] == 'scandens')]['beak_depth'])

# Compute ECDFs
x_1975, y_1975 = ecdf(bd_1975)
x_2012, y_2012 = ecdf(bd_2012)

# Plot the ECDFs
_ = plt.plot(x_1975, y_1975, marker='.', linestyle='none')
_ = plt.plot(x_2012, y_2012, marker='.', linestyle='none')

# Set margins
plt.margins(0.02)

# Add axis labels and legend
_ = plt.xlabel('beak depth (mm)')
_ = plt.ylabel('ECDF')
_ = plt.legend(('1975', '2012'), loc='lower right')

show()

bl_1975 = np.array(df[(df['year'] == 1975) & (df['species'] == 'scandens')]['beak_length'])
bl_2012 = np.array(df[(df['year'] == 2012) & (df['species'] == 'scandens')]['beak_length'])

# Make scatter plot of 1975 data
_ = plt.plot(bl_1975, bd_1975, marker='.', linestyle='None', color='blue', alpha=0.5)

# Make scatter plot of 2012 data
_ = plt.plot(bl_2012, bd_2012, marker='.', linestyle='None', color='red', alpha=0.5)

# Label axes and make legend
_ = plt.xlabel('beak length (mm)')
_ = plt.ylabel('beak depth (mm)')
_ = plt.legend(('1975', '2012'), loc='upper left')


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
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

