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

from scipy.stats import norm

sigma = 1
mu = 0
x = np.linspace(-10, 10, 1000)
dist = norm(mu, sigma)
plt.plot(x, dist.pdf(x), ls="-", c="black",
            label="mu=0,sigma=1")
plt.xlim(-5, 5)
plt.ylim(0, 0.45)
plt.xlabel("x")
plt.ylabel("P(x)")
plt.title("標準常態分配(Standard Normal Distribution)")
plt.legend()
plt.show()

print("------------------------------------------------------------")  # 60個

friends = [110, 1017, 1127, 417, 624, 957, 89, 
           951, 947, 797, 981, 125, 455, 731, 
           1641, 486, 1307, 472, 1131, 1771, 905,
           532, 742, 622]

s_friends = pd.Series(friends)
print(s_friends.describe())

print("------------------------------------------------------------")  # 60個

friends = [110, 1017, 1127, 417, 624, 957, 89, 
           951, 947, 797, 981, 125, 455, 731, 
           1641, 486, 1307, 472, 1131, 1771, 905,
           532, 742, 622]

s_friends = pd.Series(friends)
m = s_friends.mean()
print("平均數: ", m)
s = s_friends.std()
print("標準差: ", s)

z_scores = []
for x in friends:
    z = (x - m)/s   # 公式
    z_scores.append(z)
print(z_scores)

print("------------------------------------------------------------")  # 60個

friends = [110, 1017, 1127, 417, 624, 957, 89, 
           951, 947, 797, 981, 125, 455, 731, 
           1641, 486, 1307, 472, 1131, 1771, 905,
           532, 742, 622]

s_friends = pd.Series(friends)
m = s_friends.mean()
s = s_friends.std()
z_scores = []
for x in friends:
    z = (x - m)/s   # 公式
    z_scores.append(z)
index = np.arange(len(friends))
plt.bar(index, z_scores)
plt.show()

print("------------------------------------------------------------")  # 60個

dice = [1, 2, 3, 4, 5, 6]
sample_means = []
for x in range(100):
    sample = np.random.choice(a=dice, size=1)
    sample_means.append(sample.mean())

df = pd.DataFrame(sample_means)
df.plot(kind="density")
plt.show()

print("------------------------------------------------------------")  # 60個

dice = [1, 2, 3, 4, 5, 6]
sample_means = []
for x in range(100):
    sample = np.random.choice(a=dice, size=10)
    sample_means.append(sample.mean())

df = pd.DataFrame(sample_means)
df.plot(kind="density")
plt.show()

print("------------------------------------------------------------")  # 60個

dice = [1, 2, 3, 4, 5, 6]
sample_means = []
for x in range(100):
    sample = np.random.choice(a=dice, size=100)
    sample_means.append(sample.mean())

df = pd.DataFrame(sample_means)
df.plot(kind="density")
plt.show()

print("------------------------------------------------------------")  # 60個

dice = [1, 2, 3, 4, 5, 6]
population = []
for x in range(10000):
    sample = np.random.choice(a=dice, size=100)
    population.append(sample.mean())
print("母體平均數:", sum(population)/10000.0)
  
size_range = [10, 100, 1000]
for sample_size in size_range:
    sample = np.random.choice(a=population, size=sample_size)    
    sample_mean = sample.mean()
    print(sample_size, "樣本平均數:", sample_mean)

print("------------------------------------------------------------")  # 60個

population = (["臺灣閩南語"]*7330) + (["臺灣客家語"]*1200) + \
             (["其他漢語方言"]*1300) + (["原住民語"]*170) 
sample_size = 1000    
sample = random.sample(population, sample_size)
for lang in set(sample):
    print(lang+"比例估計:", sample.count(lang)/sample_size)
    
print("------------------------------------------------------------")  # 60個

from scipy import stats

dice = [1, 2, 3, 4, 5, 6]
population = []
for x in range(10000):
    sample = np.random.choice(a=dice, size=100)
    population.append(sample.mean())
print("母體平均:", sum(population)/10000.0)
  
sample_size = 100
sample = np.random.choice(a=population, size=sample_size)    

sample_mean = sample.mean()
print("樣本平均:", sample_mean)
sample_stdev = sample.std()
print("樣本標準差:", sample_stdev)
sigma = sample_stdev/math.sqrt(sample_size-1)
print("樣本計算出的母體標準差:", sigma)
z_critical = stats.norm.ppf(q=0.975)
print("Z分數:", z_critical)
margin_of_error = z_critical * sigma
confidence_interval = (sample_mean - margin_of_error,
                       sample_mean + margin_of_error)
print(confidence_interval)
conf_int = stats.norm.interval(alpha=0.95,                 
                               loc=sample_mean, 
                               scale=sigma)
print(conf_int[0], conf_int[1])

print("------------------------------------------------------------")  # 60個

from scipy import stats

dice = [1, 2, 3, 4, 5, 6]
population = []
for x in range(10000):
    sample = np.random.choice(a=dice, size=100)
    population.append(sample.mean())
population_mean = sum(population)/10000.0
  
sample_size = 1000
intervals = []
sample_means = []

for sample in range(25):
    sample = np.random.choice(a=population, size=sample_size)    
    sample_mean = sample.mean()
    sample_means.append(sample_mean)
    sample_stdev = sample.std()
    sigma = sample_stdev/math.sqrt(sample_size-1)
    z_critical = stats.norm.ppf(q=0.975)
    margin_of_error = z_critical * sigma
    confidence_interval = (sample_mean - margin_of_error,
                           sample_mean + margin_of_error)
    intervals.append(confidence_interval)

plt.figure(figsize=(9,9))
plt.errorbar(x=np.arange(0.1,25,1),
             y=sample_means,
             yerr=[(top-bot)/2 for top,bot in intervals],
             fmt="o")
plt.hlines(xmin=0, xmax=25,
           y=population_mean,linewidth=2.0,color="red")
plt.show()

print("------------------------------------------------------------")  # 60個

from scipy import stats

dice = [1, 2, 3, 4, 5, 6]
population = []
for x in range(10000):
    sample = np.random.choice(a=dice, size=100)
    population.append(sample.mean())
print("母體平均:", sum(population)/10000.0)
  
sample_size = 20
sample = np.random.choice(a=population, size=sample_size)    

sample_mean = sample.mean()
print("樣本平均:", sample_mean)
sample_stdev = sample.std()
print("樣本標準差:", sample_stdev)
sigma = sample_stdev/math.sqrt(sample_size-1)
print("樣本計算出的母體標準差:", sigma)
t_critical = stats.t.ppf(q=0.975, df=sample_size-1)
print("t分數:", t_critical)
margin_of_error = t_critical * sigma
confidence_interval = (sample_mean - margin_of_error,
                       sample_mean + margin_of_error)
print(confidence_interval)
conf_int = stats.t.interval(alpha=0.95,
                            df=sample_size-1,
                            loc=sample_mean, 
                            scale=sigma)
print(conf_int[0], conf_int[1])

print("------------------------------------------------------------")  # 60個

from scipy import stats

population_mean = 70
sample_size = 100
sample_mean = 71.5
print("樣本平均:", sample_mean)
sigma = 2.5
print("母體標準差:", sigma)
z_obtained = (sample_mean-population_mean)/(sigma/math.sqrt(sample_size))
print("Z檢定統計量:", z_obtained)
z_critical = stats.norm.ppf(q=0.975)
print("Z分數:", z_critical)
 

print("------------------------------------------------------------")  # 60個

from scipy import stats

population_mean = 500
sample = np.array([502.2, 501.6, 499.8, 502.8,
                   498.6, 502.2, 499.2, 503.4,
                   499.2])  
sample_size = len(sample)
sample_mean = sample.mean()
print("樣本平均:", sample_mean)
sample_stdev = sample.std()
print("樣本標準差:", sample_stdev)
sigma = sample_stdev/math.sqrt(sample_size-1)
print("樣本計算出的母體標準差:", sigma)
t_obtained = (sample_mean-population_mean)/sigma
print("檢定統計量:", t_obtained)
print(stats.ttest_1samp(a=sample, popmean=population_mean))

t_critical = stats.t.ppf(q=0.975, df=sample_size-1)
print("t分數:", t_critical)
 
print("------------------------------------------------------------")  # 60個

from scipy import stats

observed = np.array([20, 16, 34, 40, 38, 32])
expected = np.array([30, 30, 30, 30, 30, 30])

df = len(observed) - 1
print("自由度:", df)
chi_squared_stat = (((observed-expected)**2)/expected).sum()
print("卡方檢定統計量:", chi_squared_stat)

chi_squared, p_value = stats.chisquare(f_obs=observed, f_exp=expected)
print(chi_squared, p_value)

crit = stats.chi2.ppf(q = 0.95, df=df)
print("臨界區: ", crit)

print("------------------------------------------------------------")  # 60個

voter_gender = np.array((["男"]*352)+(["男"]*315)+ \
                        (["女"]*217)+(["女"]*331))
voter_favorite = np.array((["喜歡"]*352)+(["不喜歡"]*315)+ \
                          (["喜歡"]*217)+(["不喜歡"]*331))
voters = pd.DataFrame({"gender":voter_gender,
                       "favorite":voter_favorite})
voter_tab = pd.crosstab(voters.gender, voters.favorite, margins=True)
voter_tab.columns = ["喜歡", "不喜歡", "小計"]
voter_tab.index = ["男", "女", "小計"]
observed = voter_tab.iloc[0:3, 0:3]
print(observed)

print("------------------------------------------------------------")  # 60個

voter_gender = np.array((["男"]*352)+(["男"]*315)+ \
                        (["女"]*217)+(["女"]*331))
voter_favorite = np.array((["喜歡"]*352)+(["不喜歡"]*315)+ \
                          (["喜歡"]*217)+(["不喜歡"]*331))
voters = pd.DataFrame({"gender":voter_gender,
                       "favorite":voter_favorite})
voter_tab = pd.crosstab(voters.gender, voters.favorite, margins=True)
voter_tab.columns = ["喜歡", "不喜歡", "小計"]
voter_tab.index = ["男", "女", "小計"]
observed = voter_tab.iloc[0:3, 0:3]
print(observed)
print("---------------------------")
expected = np.outer(voter_tab["小計"][0:2],
                    voter_tab.loc["小計"][0:2]) / 1215
expected = pd.DataFrame(expected)
expected.columns = ["喜歡", "不喜歡"]
expected.index = ["男", "女"]                   
print(expected)

print("------------------------------------------------------------")  # 60個

from scipy import stats

voter_gender = np.array((["男"]*352)+(["男"]*315)+ \
                        (["女"]*217)+(["女"]*331))
voter_favorite = np.array((["喜歡"]*352)+(["不喜歡"]*315)+ \
                          (["喜歡"]*217)+(["不喜歡"]*331))
voters = pd.DataFrame({"gender":voter_gender,
                       "favorite":voter_favorite})
voter_tab = pd.crosstab(voters.gender, voters.favorite, margins=True)
voter_tab.columns = ["喜歡", "不喜歡", "小計"]
voter_tab.index = ["男", "女", "小計"]
observed = voter_tab.iloc[0:3, 0:3]
print(observed)
print("---------------------------")
expected = np.outer(voter_tab["小計"][0:2],
                    voter_tab.loc["小計"][0:2]) / 1215
expected = pd.DataFrame(expected)
expected.columns = ["喜歡", "不喜歡"]
expected.index = ["男", "女"]                   
print(expected)
print("---------------------------")
rows = 2
columns =2
df = (rows-1)*(columns-1)
print("自由度:", df)
chi_squared_stat = (((observed-expected)**2)/expected).sum().sum()
print("卡方檢定統計量:",chi_squared_stat)

chi_squared, p_value, degree_of_freedom, matrix = \
           stats.chi2_contingency(observed=observed)
print(chi_squared, p_value)

crit = stats.chi2.ppf(q = 0.95, df=df)
print("臨界區: ", crit)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




