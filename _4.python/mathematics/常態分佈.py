"""
常態分佈

normal distribution / Gaussian distribution


"""


print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
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

"""
#Standard Normal Distribution

mu = 0
sd = 1

x = np.linspace(-2.0, 2.0, 50)
#y = np.exp((x-mu)**2/(2*sd)**2) / np.sqrt(2*np.pi*(sd**2))

y = np.exp((-x)**2) / np.sqrt(2*np.pi)


plt.plot(x,y)
plt.show()
"""

"""
x = np.linspace(-2 * np.pi, 2 * np.pi, 100) #共100個點
x = np.linspace(-2 * np.pi, 2 * np.pi)   #預設為50個點
r = np.sqrt(np.power(x,2) + np.power(y, 2))
return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)
"""

print("------------------------------------------------------------")  # 60個

from scipy.stats import norm
import statistics

# Plot between -10 and 10 with .001 steps.
x_axis = np.arange(-20, 20, 0.01)

# Calculating mean and standard deviation
mean = statistics.mean(x_axis)
sd = statistics.stdev(x_axis)

plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
plt.show()


print("------------------------------------------------------------")  # 60個

import scipy.stats as stats

mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()

print("------------------------------------------------------------")  # 60個

from scipy.stats import norm

# Plot between -10 and 10 with .001 steps.
x_axis = np.arange(-10, 10, 0.001)
# Mean = 0, SD = 2.
plt.plot(x_axis, norm.pdf(x_axis, 0, 2))
plt.show()

print("------------------------------------------------------------")  # 60個

mean = 0
std = 1
variance = np.square(std)

x = np.arange(-5, 5, 0.01)
f = np.exp(-np.square(x - mean) / 2 * variance) / (np.sqrt(2 * np.pi * variance))

plt.plot(x, f)
plt.ylabel("gaussian distribution")
plt.show()

print("------------------------------------------------------------")  # 60個
"""
import scipy as sp
from scipy import stats
## generate the data and plot it for an ideal normal curve

## x-axis for the plot
x_data = np.arange(-5, 5, 0.001)

## y-axis as the gaussian
y_data = stats.norm.pdf(x_axis, 0, 1)

## plot data
plt.plot(x_data, y_data)

plt.show()
"""
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

print("------------------------------------------------------------")  # 60個

