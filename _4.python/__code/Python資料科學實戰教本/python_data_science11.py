"""
Python資料科學實戰教本

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

results = []
for num_throws in range(1, 10001):
    throws = np.random.randint(low=0, high=2, size=num_throws)
    probability_of_throws = throws.sum()/num_throws
    results.append(probability_of_throws)

df = pd.DataFrame({"投擲" : results})

df.plot(color="b")
plt.title("大數法則(Law of Large Numbers)")
plt.xlabel("投擲次數")
plt.ylabel("平均機率")
plt.show()

print("------------------------------------------------------------")  # 60個

results = []
for num_throws in range(1, 10001):
    throws = np.random.randint(low=1, high=7, size=num_throws)
    mask = (throws == 1)
    probability_of_throws = len(throws[mask])/num_throws    
    results.append(probability_of_throws)

df = pd.DataFrame({"投擲" : results})

df.plot(color="r")
plt.title("大數法則(Law of Large Numbers)")
plt.xlabel("投擲次數")
plt.ylabel("平均機率")
plt.show()

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/titanic.csv")
s =  pd.Series([30,1,5,10,30,50,30,15,40,45,30])

print(df["Age"].mode())
print(s.mode())

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/titanic.csv")
s =  pd.Series([30,1,5,10,30,50,30,15,40,45,30])

print(df["Age"].median())
print(s.median())

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/titanic.csv")
s =  pd.Series([30,1,5,10,30,50,30,15,40,45,30])

print(df["Age"].quantile(q=0.25))
print(df["Age"].quantile(q=0.5))
print(df["Age"].quantile(q=0.75))
print(s.quantile(q=0.25))
print(s.quantile(q=0.5))
print(s.quantile(q=0.75))

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/titanic.csv")
s =  pd.Series([30,1,5,10,30,50,30,15,40,45,30])

print(df["Age"].mean())
print(s.mean())

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/titanic.csv")
s =  pd.Series([30,1,5,10,30,50,30,15,40,45,30])

print(df["Age"].max() - df["Age"].min())
print(s.max() - s.min())

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/titanic.csv")
s =  pd.Series([30,1,5,10,30,50,30,15,40,45,30])

print(df["Age"].quantile(0.75) - df["Age"].quantile(0.25))
print(s.quantile(0.75) - s.quantile(0.25))

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/titanic.csv")
s =  pd.Series([30,1,5,10,30,50,30,15,40,45,30])

print(df["Age"].var())
print(s.var())

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/titanic.csv")
s =  pd.Series([30,1,5,10,30,50,30,15,40,45,30])

print(df["Age"].std())
print(s.std())

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/titanic.csv")
s =  pd.Series([30,1,5,10,30,50,30,15,40,45,30])

print(df["Age"].describe())
print("---------------------------")
print(s.describe())

print("------------------------------------------------------------")  # 60個

def dice_roll():
    v = random.randint(1, 6)
    return v
    
trials = []    
num_of_trials = 100
for trial in range(num_of_trials):
    trials.append(dice_roll())
print(sum(trials)/float(num_of_trials))

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
plt.show()

print("------------------------------------------------------------")  # 60個

from scipy import stats

n = 5
p = 1/6
for k in range(n+1):
    v = stats.binom.pmf(k, n, p)
    print(k, v)

print("------------------------------------------------------------")  # 60個

from scipy import stats

fair_dice_rolls = stats.binom.rvs(n=5, 
                                  p=1/6,
                                  size=10000)
print(fair_dice_rolls)
df = pd.DataFrame(fair_dice_rolls)
df.hist(range=(-0.5, 5.5), bins=6)
plt.show()

print("------------------------------------------------------------")  # 60個

from scipy import stats

fair_dice_rolls = stats.binom.rvs(n=10, 
                                  p=0.5,
                                  size=10000)
print(fair_dice_rolls)
df = pd.DataFrame(fair_dice_rolls)
df.hist(range=(-0.5, 10.5), bins=11)
plt.show()

print("------------------------------------------------------------")  # 60個

from scipy import stats

n = 10
p = 1/2
for k in range(n+1):
    v = stats.binom.pmf(k, n, p)
    print(k, v)


print("------------------------------------------------------------")  # 60個

from scipy import stats

n = 14
p = 0.2
k = 3
v = stats.binom.pmf(k, n, p)
print(k, v)

print("------------------------------------------------------------")  # 60個


def normal_pdf(x, mu, sigma):
    pi = 3.1415926
    e = 2.718281
    f = (1./np.sqrt(2*pi*sigma**2))*e**(-(x-mu)**2/(2.*sigma**2))
    return f

ax = np.linspace(-5, 5, 100)
ay = [normal_pdf(x, 0, 1) for x in ax]  
plt.plot(ax, ay)
plt.show()

print("------------------------------------------------------------")  # 60個

from scipy import stats

x = [x/10.0 for x in range(-50, 60)]
plt.plot(x, stats.norm.pdf(x, 0, 1),
       'r-', lw=1, alpha=0.6, label='mu=0,sigma=1')
plt.plot(x, stats.norm.pdf(x, 0, 2),
       'b--', lw=1, alpha=0.6, label='mu=0,sigma=2')
plt.plot(x, stats.norm.pdf(x, 2, 1),
       'g-.', lw=1, alpha=0.6, label='mu=2,sigma=1')
plt.legend()
plt.title("常態分配PDF的機率")
plt.show()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




