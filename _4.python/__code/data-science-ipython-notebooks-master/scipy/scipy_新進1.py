"""
scipy_新進1

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
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Random Sampling

#from __future__ import print_function, division

import numpy
import scipy.stats

#from IPython.html.widgets import interact, fixed
#from IPython.html import widgets

COLOR1 = '#7fc97f'
COLOR2 = '#beaed4'
COLOR3 = '#fdc086'
COLOR4 = '#ffff99'
COLOR5 = '#386cb0'

#Part One

weight = scipy.stats.lognorm(0.23, 0, 70.8)
weight.mean(), weight.std()

#(72.697645732966876, 16.944043048498038)

#Here's what that distribution looks like:

xs = np.linspace(20, 160, 100)
ys = weight.pdf(xs)
plt.plot(xs, ys, linewidth=4, color=COLOR1)
plt.xlabel('weight (kg)')
plt.ylabel('PDF')
show()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#from __future__ import print_function, division

import numpy
import scipy.stats

import matplotlib.pyplot as pyplot

#from IPython.html.widgets import interact, fixed
#from IPython.html import widgets

# some nice colors from http://colorbrewer2.org/
COLOR1 = '#7fc97f'
COLOR2 = '#beaed4'
COLOR3 = '#fdc086'
COLOR4 = '#ffff99'
COLOR5 = '#386cb0'

# use scipy.stats.norm to represent the distributions

mu1, sig1 = 178, 7.7
male_height = scipy.stats.norm(mu1, sig1)

mu2, sig2 = 163, 7.3
female_height = scipy.stats.norm(mu2, sig2)

#The following function evaluates the normal (Gaussian) probability density function (PDF) within 4 standard deviations of the mean. It takes and rv object and returns a pair of NumPy arrays.

def eval_pdf(rv, num=4):
    mean, std = rv.mean(), rv.std()
    xs = np.linspace(mean - num*std, mean + num*std, 100)
    ys = rv.pdf(xs)
    return xs, ys

xs, ys = eval_pdf(male_height)
plt.plot(xs, ys, label='male', linewidth=4, color=COLOR2)

xs, ys = eval_pdf(female_height)
plt.plot(xs, ys, label='female', linewidth=4, color=COLOR3)
plt.xlabel('height (cm)')
show()

male_sample = male_height.rvs(1000)

female_sample = female_height.rvs(1000)

# Both samples are NumPy arrays. Now we can compute sample statistics like the mean and standard deviation.

mean1, std1 = male_sample.mean(), male_sample.std()
cc = mean1, std1
print(cc)

#(178.16511665818112, 7.8419961712899502)

#The sample mean is close to the population mean, but not exact, as expected.

mean2, std2 = female_sample.mean(), female_sample.std()
cc = mean2, std2
print(cc)

#(163.48610226651135, 7.382384919896662)

#And the results are similar for the female sample.

#Now, there are many ways to describe the magnitude of the difference between these distributions. An obvious one is the difference in the means:

difference_in_means = male_sample.mean() - female_sample.mean()
print(difference_in_means) # in cm

#14.679014391669767

# Exercise: what is the relative difference in means, expressed as a percentage?

relative_difference = difference_in_means / male_sample.mean()
print(relative_difference * 100)   # percent

#8.2389946286916569

#But a problem with relative differences is that you have to choose which mean to express them relative to.

relative_difference = difference_in_means / female_sample.mean()
print(relative_difference * 100)    # percent

#8.9787536605040401

#An alternative way to express the difference between distributions is to see how much they overlap. To define overlap, we choose a threshold between the two means. The simple threshold is the midpoint between the means:

simple_thresh = (mean1 + mean2) / 2
print(simple_thresh)

#170.82560946234622

#A better, but slightly more complicated threshold is the place where the PDFs cross.

thresh = (std1 * mean2 + std2 * mean1) / (std1 + std2)
print(thresh)

#170.6040359174722

#In this example, there's not much difference between the two thresholds.

#Now we can count how many men are below the threshold:

male_below_thresh = sum(male_sample < thresh)
print(male_below_thresh)

#164

#And how many women are above it:

female_above_thresh = sum(female_sample > thresh)
print(female_above_thresh)

#174

#The "overlap" is the total area under the curves that ends up on the wrong side of the threshold.

overlap = male_below_thresh / len(male_sample) + female_above_thresh / len(female_sample)
print(overlap)

#0.33799999999999997

#Or in more practical terms, you might report the fraction of people who would be misclassified if you tried to use height to guess sex:

misclassification_rate = overlap / 2
print(misclassification_rate)

#0.16899999999999998

#Another way to quantify the difference between distributions is what's called "probability of superiority", which is a problematic term, but in this context it's the probability that a randomly-chosen man is taller than a randomly-chosen woman.

# Exercise: suppose I choose a man and a woman at random.
# What is the probability that the man is taller?
cc = sum(x > y for x, y in zip(male_sample, female_sample)) / len(male_sample)
print(cc)

#0.91100000000000003


def CohenEffectSize(group1, group2):
    """Compute Cohen's d.

    group1: Series or NumPy array
    group2: Series or NumPy array

    returns: float
    """
    diff = group1.mean() - group2.mean()

    n1, n2 = len(group1), len(group2)
    var1 = group1.var()
    var2 = group2.var()

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / np.sqrt(pooled_var)
    return d


cc = CohenEffectSize(male_sample, female_sample)
print(cc)

# 1.9274780043619493


def overlap_superiority(control, treatment, n=1000):
    """Estimates overlap and superiority based on a sample.
    
    control: scipy.stats rv object
    treatment: scipy.stats rv object
    n: sample size
    """
    control_sample = control.rvs(n)
    treatment_sample = treatment.rvs(n)
    thresh = (control.mean() + treatment.mean()) / 2
    
    control_above = sum(control_sample > thresh)
    treatment_below = sum(treatment_sample < thresh)
    overlap = (control_above + treatment_below) / n
    
    superiority = sum(x > y for x, y in zip(treatment_sample, control_sample)) / n
    return overlap, superiority


def plot_pdfs(cohen_d=2):
    """Plot PDFs for distributions that differ by some number of stds.
    
    cohen_d: number of standard deviations between the means
    """
    control = scipy.stats.norm(0, 1)
    treatment = scipy.stats.norm(cohen_d, 1)
    xs, ys = eval_pdf(control)
    plt.fill_between(xs, ys, label='control', color=COLOR3, alpha=0.7)

    xs, ys = eval_pdf(treatment)
    plt.fill_between(xs, ys, label='treatment', color=COLOR2, alpha=0.7)
    
    o, s = overlap_superiority(control, treatment)
    print('overlap', o)
    print('superiority', s)

#Here's an example that demonstrates the function:

plot_pdfs(2)
show()

#overlap 0.278
#superiority 0.932

"""
slider = widgets.FloatSliderWidget(min=0, max=4, value=2)
interact(plot_pdfs, cohen_d=slider)
show()
"""
#overlap 0.305
#superiority 0.931

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
