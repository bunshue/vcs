"""
statistics

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
print("------------------------------------------------------------")  # 60個

# Munivariate statistics exercises

# Dot product and Euclidean norm

a = np.array([2, 1])
b = np.array([1, 1])


def euclidian(x):
    return np.sqrt(np.dot(x, x))


euclidian(a)

euclidian(a - b)

np.dot(b, a / euclidian(a))

X = np.random.randn(100, 2)
np.dot(X, a / euclidian(a))

# Covariance matrix and Mahalanobis norm

N = 100
mu = np.array([1, 1])
Cov = np.array([[1, 0.8], [0.8, 1]])

X = np.random.multivariate_normal(mu, Cov, N)

xbar = np.mean(X, axis=0)
print(xbar)

Xc = X - xbar

np.mean(Xc, axis=0)

S = 1 / (N - 1) * np.dot(Xc.T, Xc)
print(S)

# import scipy

Sinv = np.linalg.inv(S)


def mahalanobis(x, xbar, Sinv):
    xc = x - xbar
    return np.sqrt(np.dot(np.dot(xc, Sinv), xc))


dists = pd.DataFrame(
    [
        [mahalanobis(X[i, :], xbar, Sinv), euclidian(X[i, :] - xbar)]
        for i in range(X.shape[0])
    ],
    columns=["Mahalanobis", "Euclidean"],
)

print(dists[:10])

x = X[0, :]

import scipy.spatial

assert mahalanobis(X[0, :], xbar, Sinv) == scipy.spatial.distance.mahalanobis(
    xbar, X[0, :], Sinv
)
assert mahalanobis(X[1, :], xbar, Sinv) == scipy.spatial.distance.mahalanobis(
    xbar, X[1, :], Sinv
)

print("------------------------------------------------------------")  # 60個

n = 10
x = np.random.normal(loc=1.78, scale=0.1, size=n)
y = np.random.normal(loc=1.66, scale=0.1, size=n)

xbar = np.mean(x)
assert xbar == np.sum(x) / x.shape[0]

xvar = np.var(x, ddof=1)
assert xvar == np.sum((x - xbar) ** 2) / (n - 1)

xycov = np.cov(x, y)
print(xycov)

ybar = np.sum(y) / n
assert np.allclose(xycov[0, 1], np.sum((x - xbar) * (y - ybar)) / (n - 1))
assert np.allclose(xycov[0, 0], xvar)
assert np.allclose(xycov[1, 1], np.var(y, ddof=1))

print("------------------------------------------------------------")  # 60個

from scipy.stats import norm

mu = 0  # mean
variance = 2  # variance
sigma = np.sqrt(variance)  # standard deviation",
x = np.linspace(mu - 3 * variance, mu + 3 * variance, 100)
plt.plot(x, norm.pdf(x, mu, sigma))
plt.show()

print("------------------------------------------------------------")  # 60個

from scipy.stats import f

fvalues = np.linspace(0.1, 5, 100)

# pdf(x, df1, df2): Probability density function at x of F.
plt.plot(fvalues, f.pdf(fvalues, 1, 30), "b-", label="F(1, 30)")
plt.plot(fvalues, f.pdf(fvalues, 5, 30), "r-", label="F(5, 30)")
plt.legend()

# cdf(x, df1, df2): Cumulative distribution function of F.
# ie.
proba_at_f_inf_3 = f.cdf(3, 1, 30)  # P(F(1,30) < 3)

# ppf(q, df1, df2): Percent point function (inverse of cdf) at q of F.
f_at_proba_inf_95 = f.ppf(0.95, 1, 30)  # q such P(F(1,30) < .95)
# assert f.cdf(f_at_proba_inf_95, 1, 30) == .95

# sf(x, df1, df2): Survival function (1 - cdf) at x of F.
proba_at_f_sup_3 = f.sf(3, 1, 30)  # P(F(1,30) > 3)
assert proba_at_f_inf_3 + proba_at_f_sup_3 == 1

# p-value: P(F(1, 30)) < 0.05
low_proba_fvalues = fvalues[fvalues > f_at_proba_inf_95]
plt.fill_between(
    low_proba_fvalues, 0, f.pdf(low_proba_fvalues, 1, 30), alpha=0.8, label="P < 0.05"
)
plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(5, 3))
plt.bar([0, 1, 2, 3], [1 / 8, 3 / 8, 3 / 8, 1 / 8], width=0.9)
_ = plt.xticks([0, 1, 2, 3], [0, 1, 2, 3])
plt.xlabel("Distribution of the number of head over 3 flip under the null hypothesis")
plt.show()

print("------------------------------------------------------------")  # 60個

import scipy.stats

# tobs = 2.39687663116 # assume the t-value
succes = np.linspace(30, 70, 41)
plt.plot(
    succes, scipy.stats.binom.pmf(succes, 100, 0.5), "b-", label="Binomial(100, 0.5)"
)
upper_succes_tvalues = succes[succes > 60]
plt.fill_between(
    upper_succes_tvalues,
    0,
    scipy.stats.binom.pmf(upper_succes_tvalues, 100, 0.5),
    alpha=0.8,
    label="p-value",
)
_ = plt.legend()


pval = 1 - scipy.stats.binom.cdf(60, 100, 0.5)
print(pval)

plt.show()

print("------------------------------------------------------------")  # 60個


# Random sampling of the Binomial distribution under the null hypothesis

sccess_h0 = scipy.stats.binom.rvs(100, 0.5, size=10000, random_state=4)
print(sccess_h0)

pval_rnd = np.sum(sccess_h0 >= 60) / (len(sccess_h0) + 1)
print(
    "P-value using monte-carlo sampling of the Binomial distribution under H0=",
    pval_rnd,
)

print("------------------------------------------------------------")  # 60個

x = [1.83, 1.83, 1.73, 1.82, 1.83, 1.73, 1.99, 1.85, 1.68, 1.87]

xbar = np.mean(x)  # sample mean
mu0 = 1.75  # hypothesized value
s = np.std(x, ddof=1)  # sample standard deviation
n = len(x)  # sample size

print(xbar)

tobs = (xbar - mu0) / (s / np.sqrt(n))
print(tobs)

print("------------------------------------------------------------")  # 60個

import scipy.stats as stats

# tobs = 2.39687663116 # assume the t-value
tvalues = np.linspace(-10, 10, 100)
plt.plot(tvalues, stats.t.pdf(tvalues, n - 1), "b-", label="T(n-1)")
upper_tval_tvalues = tvalues[tvalues > tobs]
plt.fill_between(
    upper_tval_tvalues,
    0,
    stats.t.pdf(upper_tval_tvalues, n - 1),
    alpha=0.8,
    label="p-value",
)
_ = plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個

import scipy.stats as stats

n = 50
x = np.random.normal(size=n)
y = 2 * x + np.random.normal(size=n)

# Compute with scipy
cor, pval = stats.pearsonr(x, y)
print(cor, pval)


print("------------------------------------------------------------")  # 60個

import scipy.stats as stats

height = np.array(
    [
        1.83,
        1.83,
        1.73,
        1.82,
        1.83,
        1.73,
        1.99,
        1.85,
        1.68,
        1.87,
        1.66,
        1.71,
        1.73,
        1.64,
        1.70,
        1.60,
        1.79,
        1.73,
        1.62,
        1.77,
    ]
)

grp = np.array(["M"] * 10 + ["F"] * 10)

# Compute with scipy
print(stats.ttest_ind(height[grp == "M"], height[grp == "F"], equal_var=True))

print("------------------------------------------------------------")  # 60個

import statsmodels.api as sm
from statsmodels.formula.api import ols

# Load iris datset
iris = sm.datasets.get_rdataset("iris").data
iris.columns = [s.replace(".", "") for s in iris.columns]

# Group means
means = iris.groupby("Species").mean().reset_index()
print(means)

# Group Stds (equal variances ?)
stds = iris.groupby("Species").std(ddof=1).reset_index()
print(stds)

# Plot groups
ax = sns.violinplot(x="Species", y="SepalLength", data=iris)
ax = sns.swarmplot(x="Species", y="SepalLength", data=iris, color="white")
ax = sns.swarmplot(x="Species", y="SepalLength", color="black", data=means, size=10)

# ANOVA
lm = ols("SepalLength ~ Species", data=iris).fit()
sm.stats.anova_lm(lm, typ=2)  # Type 2 ANOVA DataFrame

plt.show()

print("------------------------------------------------------------")  # 60個

import scipy.stats as stats

# Dataset:
# 15 samples:
# 10 first exposed
exposed = np.array([1] * 10 + [0] * 10)
# 8 first with cancer, 10 without, the last two with.
cancer = np.array([1] * 8 + [0] * 10 + [1] * 2)

crosstab = pd.crosstab(exposed, cancer, rownames=["exposed"], colnames=["cancer"])
print("Observed table:")
print("---------------")
print(crosstab)

chi2, pval, dof, expected = stats.chi2_contingency(crosstab)
print("Statistics:")
print("-----------")
print("Chi2 = %f, pval = %f" % (chi2, pval))
print("Expected table:")
print("---------------")
print(expected)

print("------------------------------------------------------------")  # 60個

# Computing expected cross-table

# Compute expected cross-table based on proportion
exposed_marg = crosstab.sum(axis=0)
exposed_freq = exposed_marg / exposed_marg.sum()

cancer_marg = crosstab.sum(axis=1)
cancer_freq = cancer_marg / cancer_marg.sum()

print("Exposed frequency? Yes: %.2f" % exposed_freq[0], "No: %.2f" % exposed_freq[1])
print("Cancer frequency? Yes: %.2f" % cancer_freq[0], "No: %.2f" % cancer_freq[1])

print("Expected frequencies:")
print(np.outer(exposed_freq, cancer_freq))

print("Expected cross-table (frequencies * N): ")
print(np.outer(exposed_freq, cancer_freq) * len(exposed))

print("------------------------------------------------------------")  # 60個

import scipy.stats as stats

# Age uniform distribution between 20 and 40
age = np.random.uniform(20, 60, 40)

# Systolic blood presure, 2 groups:
# - 15 subjects at 0.05 * age + 6
# - 25 subjects at 0.15 * age + 10
sbp = np.concatenate(
    (0.05 * age[:15] + 6, 0.15 * age[15:] + 10)
) + 0.5 * np.random.normal(size=40)

sns.regplot(x=age, y=sbp)

# Non-Parametric Spearman
cor, pval = stats.spearmanr(age, sbp)
print("Non-Parametric Spearman cor test, cor: %.4f, pval: %.4f" % (cor, pval))

# "Parametric Pearson cor test
cor, pval = stats.pearsonr(age, sbp)
print("Parametric Pearson cor test: cor: %.4f, pval: %.4f" % (cor, pval))

plt.show()

print("------------------------------------------------------------")  # 60個

import scipy.stats as stats

n = 20
# Buisness Volume time 0
bv0 = np.random.normal(loc=3, scale=0.1, size=n)
# Buisness Volume time 1
bv1 = bv0 + 0.1 + np.random.normal(loc=0, scale=0.1, size=n)

# create an outlier
bv1[0] -= 10

# Paired t-test
print(stats.ttest_rel(bv0, bv1))

# Wilcoxon
print(stats.wilcoxon(bv0, bv1))

print("------------------------------------------------------------")  # 60個


import scipy.stats as stats

n = 20
# Buismess Volume group 0
bv0 = np.random.normal(loc=1, scale=0.1, size=n)

# Buismess Volume group 1
bv1 = np.random.normal(loc=1.2, scale=0.1, size=n)

# create an outlier
bv1[0] -= 10

# Two-samples t-test
print(stats.ttest_ind(bv0, bv1))

# Wilcoxon
print(stats.mannwhitneyu(bv0, bv1))

print("------------------------------------------------------------")  # 60個

url = "https://github.com/duchesnay/pystatsml/raw/master/datasets/salary_table.csv"
salary = pd.read_csv(url)
salary = salary[salary.management == "N"]

print("------------------------------------------------------------")  # 60個

from scipy import stats

y, x = salary.salary, salary.experience
beta, beta0, r_value, p_value, std_err = stats.linregress(x, y)
print(
    "y = %f x + %f,  r: %f, r-squared: %f,\np-value: %f, std_err: %f"
    % (beta, beta0, r_value, r_value**2, p_value, std_err)
)

print("Regression line with the scatterplot")
yhat = beta * x + beta0  # regression line
plt.plot(x, yhat, "r-", x, y, "o")
plt.xlabel("Experience (years)")
plt.ylabel("Salary")
plt.show()

ax = sns.regplot(x="experience", y="salary", data=salary)

print("------------------------------------------------------------")  # 60個

from scipy import linalg

# Dataset
N, P = 50, 4
X = np.random.normal(size=N * P).reshape((N, P))
## Our model needs an intercept so we add a column of 1s:
X[:, 0] = 1
print(X[:5, :])

betastar = np.array([10, 1.0, 0.5, 0.1])
e = np.random.normal(size=N)
y = np.dot(X, betastar) + e

# Estimate the parameters
Xpinv = linalg.pinv(X)
betahat = np.dot(Xpinv, y)
print("Estimated beta:\n", betahat)

print("------------------------------------------------------------")  # 60個

# Multiple regression

import statsmodels.api as sm

## Fit and summary:
model = sm.OLS(y, X).fit()
print(model.summary())

# prediction of new values
ypred = model.predict(X)

# residuals + prediction == true values
assert np.all(ypred + model.resid == y)


print("------------------------------------------------------------")  # 60個

import statsmodels.formula.api as smf

df = pd.DataFrame(np.column_stack([X, y]), columns=["inter", "x1", "x2", "x3", "y"])
print(df.columns, df.shape)
# Build a model excluding the intercept, it is implicit
model = smf.ols("y~x1 + x2 + x3", df).fit()
print(model.summary())

print("------------------------------------------------------------")  # 60個

url = "https://github.com/duchesnay/pystatsml/raw/master/datasets/salary_table.csv"
df = pd.read_csv(url)

print(df.head())

print("------------------------------------------------------------")  # 60個
""" NG
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms

lm = smf.ols('salary ~ experience', df).fit()
df["residuals"] = lm.resid

print("Jarque-Bera normality test p-value %.5f" % sms.jarque_bera(lm.resid)[1])

ax = sns.displot(df, x='residuals', kind="kde", fill=True)
ax = sns.displot(df, x='residuals', kind="kde", hue='management', fill=True)

print("------------------------------------------------------------")  # 60個

oneway = smf.ols('salary ~ management + experience', df).fit()
df["residuals"] = oneway.resid
sns.displot(df, x='residuals', kind="kde", fill=True)
print(sm.stats.anova_lm(oneway, typ=2))
print("Jarque-Bera normality test p-value %.3f" % sms.jarque_bera(oneway.resid)[1])

print("------------------------------------------------------------")  # 60個

twoway = smf.ols('salary ~ education + management + experience', df).fit()

df["residuals"] = twoway.resid
sns.displot(df, x='residuals', kind="kde", fill=True)
print(sm.stats.anova_lm(twoway, typ=2))

print("Jarque-Bera normality test p-value %.3f" % sms.jarque_bera(twoway.resid)[1])

print(twoway.compare_f_test(oneway))  # return F, pval, df

print(twoway.model.data.param_names)
print(twoway.model.data.exog[:10, :])

#Contrasts and post-hoc tests

# t-test of the specific contribution of experience:
ttest_exp = twoway.t_test([0, 0, 0, 0, 1])
ttest_exp.pvalue, ttest_exp.tvalue
print(ttest_exp)

# Alternatively, you can specify the hypothesis tests using a string
twoway.t_test('experience')

# Post-hoc is salary of Master different salary of Ph.D? 
# ie. t-test salary of Master = salary of Ph.D.
print(twoway.t_test('education[T.Master] = education[T.Ph.D]'))
"""
# Multiple comparisons

# Dataset
n_samples, n_features = 100, 1000
n_info = int(n_features / 10)  # number of features with information
n1, n2 = int(n_samples / 2), n_samples - int(n_samples / 2)
snr = 0.5
Y = np.random.randn(n_samples, n_features)
grp = np.array(["g1"] * n1 + ["g2"] * n2)

# Add some group effect for Pinfo features
Y[grp == "g1", :n_info] += snr

#
import scipy.stats as stats

tvals, pvals = np.full(n_features, np.NAN), np.full(n_features, np.NAN)
for j in range(n_features):
    tvals[j], pvals[j] = stats.ttest_ind(
        Y[grp == "g1", j], Y[grp == "g2", j], equal_var=True
    )

fig, axis = plt.subplots(3, 1, figsize=(9, 9))  # , sharex='col')

axis[0].plot(range(n_features), tvals, "o")
axis[0].set_ylabel("t-value")

axis[1].plot(range(n_features), pvals, "o")
axis[1].axhline(y=0.05, color="red", linewidth=3, label="p-value=0.05")
# axis[1].axhline(y=0.05, label="toto", color='red')
axis[1].set_ylabel("p-value")
axis[1].legend()

axis[2].hist(
    [pvals[n_info:], pvals[:n_info]],
    stacked=True,
    bins=100,
    label=["Negatives", "Positives"],
)
axis[2].set_xlabel("p-value histogram")
axis[2].set_ylabel("density")
axis[2].legend()

plt.tight_layout()

plt.show()

print("------------------------------------------------------------")  # 60個

P, N = n_info, n_features - n_info  # Positives, Negatives
TP = np.sum(pvals[:n_info] < 0.05)  # True Positives
FP = np.sum(pvals[n_info:] < 0.05)  # False Positives
print("No correction, FP: %i (expected: %.2f), TP: %i" % (FP, N * 0.05, TP))


print("------------------------------------------------------------")  # 60個


import statsmodels.sandbox.stats.multicomp as multicomp

_, pvals_fwer, _, _ = multicomp.multipletests(pvals, alpha=0.05, method="bonferroni")
TP = np.sum(pvals_fwer[:n_info] < 0.05)  # True Positives
FP = np.sum(pvals_fwer[n_info:] < 0.05)  # False Positives
print("FWER correction, FP: %i, TP: %i" % (FP, TP))


print("------------------------------------------------------------")  # 60個

import statsmodels.sandbox.stats.multicomp as multicomp

_, pvals_fdr, _, _ = multicomp.multipletests(pvals, alpha=0.05, method="fdr_bh")
TP = np.sum(pvals_fdr[:n_info] < 0.05)  # True Positives
FP = np.sum(pvals_fdr[n_info:] < 0.05)  # False Positives

print("FDR correction, FP: %i, TP: %i" % (FP, TP))

print("------------------------------------------------------------")  # 60個

from scipy import linalg

# Dataset
N, P = 50, 4
X = np.random.normal(size=N * P).reshape((N, P))
## Our model needs an intercept so we add a column of 1s:
X[:, 0] = 1
print(X[:5, :])

betastar = np.array([10, 1.0, 0.5, 0.1])
e = np.random.normal(size=N)
y = np.dot(X, betastar) + e

# Estimate the parameters
Xpinv = linalg.pinv(X)
betahat = np.dot(Xpinv, y)
print("Estimated beta:\n", betahat)

print("------------------------------------------------------------")  # 60個

# dataset
mu_k = np.array([1, 2, 3])  # means of 3 samples
sd_k = np.array([1, 1, 1])  # sd of 3 samples
n_k = np.array([10, 20, 30])  # sizes of 3 samples
grp = [0, 1, 2]  # group labels
n = np.sum(n_k)
label = np.hstack([[k] * n_k[k] for k in [0, 1, 2]])

y = np.zeros(n)
for k in grp:
    y[label == k] = np.random.normal(mu_k[k], sd_k[k], n_k[k])

# Compute with scipy
fval, pval = stats.f_oneway(y[label == 0], y[label == 1], y[label == 2])

print("------------------------------------------------------------")  # 60個

import scipy.stats as stats

n = 10
x = np.random.normal(loc=1.76, scale=0.1, size=n)
print(x)

print("------------------------------------------------------------")  # 60個

(
    xbar,
    s,
    xmu,
) = (
    np.mean(x),
    np.std(x, ddof=1),
    1.75,
)

tval = (xbar - xmu) / (s / np.sqrt(n))

# Survival function (1 - `cdf`)
pval = stats.t.sf(tval, n - 1)

pval2sided = pval * 2
# do it with sicpy
assert np.allclose((tval, pval2sided), stats.ttest_1samp(x, xmu))

print(tval, pval)

tvalues = np.linspace(-10, 10, 100)
plt.plot(tvalues, stats.t.pdf(tvalues, n - 1), "b-", label="T(n-1)")
upper_tval_tvalues = tvalues[tvalues > tval]
plt.fill_between(
    upper_tval_tvalues, 0, stats.t.pdf(upper_tval_tvalues, n - 1), alpha=0.8
)
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個

import scipy.stats as stats

url = "https://github.com/duchesnay/pystatsml/raw/master/datasets/birthwt.csv"
df = pd.read_csv(url)

print(df.head())

print(stats.pearsonr(df.age, df.bwt))
print(stats.pearsonr(df.bwt, df.lwt))

plt.plot(df.bwt, df.lwt, "o")
plt.show()

print("------------------------------------------------------------")  # 60個

import scipy.stats as stats

url = "https://github.com/duchesnay/pystatsml/raw/master/datasets/salary_table.csv"
salary = pd.read_csv(url)

y, x = salary.salary, salary.experience

# Model parameters
beta, beta0, r_value, p_value, std_err = stats.linregress(x, y)

print(
    "y=%f x + %f  r:%f, r-squared:%f, p-value:%f, std_err:%f"
    % (beta, beta0, r_value, r_value**2, p_value, std_err)
)

# plotting the line
yhat = beta * x + beta0  # regression line
plt.plot(x, yhat, "r-", x, y, "o")
plt.xlabel("Experience (years)")
plt.ylabel("Salary")

plt.show()

## $\bar{y}$ `y_mu`

y_mu = np.mean(y)

## $SS_\text{tot}$: `ss_tot`

ss_tot = np.sum((y - y_mu) ** 2)

## $SS_\text{reg}$: `ss_reg`
ss_reg = np.sum((yhat - y_mu) ** 2)

## $SS_\text{res}$: `ss_res`
ss_res = np.sum((y - yhat) ** 2)

## Check partition of variance formula based on SS using `assert np.allclose(val1, val2, atol=1e-05)`
assert np.allclose(ss_tot - (ss_reg + ss_res), 0, atol=1e-05)

## What np.allclose does ?

## What assert does

## What is it worth for ?

## Compute $R^2$ and compare with `r_value` above
r2 = ss_reg / ss_tot

assert np.sqrt(r2) == r_value

## Compute F score
n = y.size
fval = ss_reg / (ss_res / (n - 2))


# Compute the p-value:
#  * Plot the F(1,n) distribution for 100 f values within [10, 25]. Draw P(F(1,n)>F) ie. color the surface defined by x values larger than F below the F(1,n).
#  * P(F(1,n)>F) is the p-value, compute it.

fvalues = np.linspace(10, 25, 100)

plt.plot(fvalues, stats.f.pdf(fvalues, 1, 30), "b-", label="F(1, 30)")

upper_fval_fvalues = fvalues[fvalues > fval]
plt.fill_between(
    upper_fval_fvalues, 0, stats.f.pdf(upper_fval_fvalues, 1, 30), alpha=0.8
)

# pdf(x, df1, df2): Probability density function at x of the given RV.
plt.legend()

# Survival function (1 - `cdf`)
pval = stats.f.sf(fval, 1, n - 2)


## With statmodels

from statsmodels.formula.api import ols

model = ols("salary ~ experience", salary)
results = model.fit()
print(results.summary())

## With sklearn

import sklearn.feature_selection

# sklearn.feature_selection.f_regression??
sklearn.feature_selection.f_regression(x.reshape((n, 1)), y)

print("------------------------------------------------------------")  # 60個

import scipy

# Dataset
N, P = 50, 4
X = np.random.normal(size=N * P).reshape((N, P))
## Our model needs an intercept so we add a column of 1s:
X[:, 0] = 1
print(X[:5, :])

betastar = np.array([10, 1.0, 0.5, 0.1])
e = np.random.normal(size=N)
y = np.dot(X, betastar) + e

# Estimate the parameters
Xpinv = scipy.linalg.pinv2(X)
betahat = np.dot(Xpinv, y)
print("Estimated beta:\n", betahat)


print("------------------------------------------------------------")  # 60個

# 1. What are the dimensions of pinv$(X)$ ?

# ((P x N) (N x P))^1 (P x N)
# P x N

print(Xpinv.shape)

# 2. Compute the MSE between the predicted values and the true values.


yhat = np.dot(X, betahat)

mse = np.sum((y - yhat) ** 2) / N
print("MSE =", mse)


print("------------------------------------------------------------")  # 60個

height = np.array(
    [
        1.83,
        1.83,
        1.73,
        1.82,
        1.83,
        1.73,
        1.99,
        1.85,
        1.68,
        1.87,
        1.66,
        1.71,
        1.73,
        1.64,
        1.70,
        1.60,
        1.79,
        1.73,
        1.62,
        1.77,
    ]
)
grp = np.array(["M"] * 10 + ["F"] * 10)

x = height[grp == "M"]
y = height[grp == "F"]

nx, ny = len(x), len(y)

# mean/std
xbar, ybar = np.mean(x), np.mean(y)
xvar, yvar = np.var(x, ddof=1), np.var(y, ddof=1)

print("------------------------------------------------------------")  # 60個

# se
sigma = np.sqrt((xvar * (nx - 1) + yvar * (ny - 1)) / (nx + ny - 2))
se = sigma * np.sqrt(1 / nx + 1 / ny)

# tval
tval = (xbar - ybar) / se

print("tval=%.2f, pval=%.4f" % (tval, pval))

# df
df = nx + ny - 2
pval = stats.t.sf(tval, df)
pval2sided = pval * 2

# With scipy
import scipy.stats as stats

assert np.allclose((tval, pval2sided), stats.ttest_ind(x, y, equal_var=True))

print("------------------------------------------------------------")  # 60個

se = np.sqrt(xvar / nx + yvar / ny)

tval = (xbar - ybar) / se

# Use the following function to approximate the df needed for the p-value


def unequal_var_ttest_df(v1, n1, v2, n2):
    vn1 = v1 / n1
    vn2 = v2 / n2
    df = (vn1 + vn2) ** 2 / (vn1**2 / (n1 - 1) + vn2**2 / (n2 - 1))
    return df


df = unequal_var_ttest_df(xvar, nx, yvar, ny)

# Compute the p-value.
#
# The p-value is one-sided: a two-sided test would test P(T > tval)
# and P(T < -tval). What would be the two sided p-value ?

pval = stats.t.sf(tval, df)
pval2sided = pval * 2

# Compare the two-sided p-value with the one obtained by `stats.ttest_ind` using `assert np.allclose(arr1, arr2)`

# do it with scipy
assert np.allclose((tval, pval2sided), stats.ttest_ind(x, y, equal_var=False))


# Plot of the two sample t-test

xjitter = np.random.normal(loc=-1, size=len(x), scale=0.01)
yjitter = np.random.normal(loc=+1, size=len(y), scale=0.01)
plt.plot(xjitter, x, "ob", alpha=0.5)
plt.plot(yjitter, y, "ob", alpha=0.5)
plt.plot([-1, +1], [xbar, ybar], "or", markersize=15)

# left, left + width, bottom, bottom + height
# plt.bar(left=0, height=se, width=0.1, bottom=ybar-se/2)
## effect size error bar
plt.errorbar(
    -0.1,
    ybar + (xbar - ybar) / 2,
    yerr=(xbar - ybar) / 2,
    elinewidth=3,
    capsize=5,
    markeredgewidth=3,
    color="r",
)

plt.errorbar(
    [-0.8, 0.8],
    [xbar, ybar],
    yerr=np.sqrt([xvar, yvar]) / 2,
    elinewidth=3,
    capsize=5,
    markeredgewidth=3,
    color="b",
)

plt.errorbar(
    0.1, ybar, yerr=se / 2, elinewidth=3, capsize=5, markeredgewidth=3, color="b"
)
print("------------------------------------------------------------")  # 60個

# Model data
eps = np.random.normal(loc=0, scale=1, size=100)
g = np.concatenate([np.zeros(50), np.ones(50)])

y = g + eps


def tstat(y, g):
    ys = [y[g == l] for l in np.unique(g)]
    means = [np.mean(vals) for vals in ys]
    sse = [np.sum((vals - means[i]) ** 2) for i, vals in enumerate(ys)]
    counts = [len(vals) for vals in ys]
    s = np.sqrt(np.sum(sse) / (len(y) - 2))
    tval = (means[1] - means[0]) / (s * np.sqrt(1 / counts[0] + 1 / counts[0]))
    return tval


# Permutation: simulate the null hypothesis
nperm = 10000
perms = np.zeros(nperm + 1)
perms[0] = tstat(y, g)

for i in range(1, nperm):
    perms[i] = tstat(y, np.random.permutation(g))

pval = np.sum(perms >= perms[0]) / len(perms)
print(pval)

print("------------------------------------------------------------")  # 60個

url = "https://github.com/duchesnay/pystatsml/raw/master/datasets/birthwt.csv"
df = pd.read_csv(url)

df.describe()

df.smoke.describe()

df.smoke = df.smoke.map({1: "y", 0: "n"})

df.smoke.describe()

print(df[["smoke", "bwt"]].groupby("smoke").mean())
print(df[["smoke", "bwt"]].groupby("smoke").std())

ax = sns.violinplot(x="smoke", y="bwt", data=df, inner=None)
ax = sns.swarmplot(x="smoke", y="bwt", data=df, color="white", edgecolor="gray")

import scipy.stats as stats

print(stats.ttest_ind(df.bwt[df.smoke == "y"], df.bwt[df.smoke == "n"]))

print("------------------------------------------------------------")  # 60個

# dataset
mu_k = np.array([1, 2, 3])  # means of 3 samples
sd_k = np.array([1, 1, 1])  # sd of 3 samples
n_k = np.array([10, 20, 30])  # sizes of 3 samples
grp = [0, 1, 2]  # group labels
n = np.sum(n_k)
label = np.hstack([[k] * n_k[k] for k in [0, 1, 2]])

y = np.zeros(n)
for k in grp:
    y[label == k] = np.random.normal(mu_k[k], sd_k[k], n_k[k])


print("------------------------------------------------------------")  # 60個

import scipy.stats as stats

# estimate parameters
ybar_k = np.zeros(3)

ybar = y.mean()
for k in grp:
    ybar_k[k] = np.mean(y[label == k])


betweenvar = np.sum([n_k[k] * (ybar_k[k] - ybar) ** 2 for k in grp]) / (len(grp) - 1)
withinvar = np.sum([np.sum((y[label == k] - ybar_k[k]) ** 2) for k in grp]) / (
    n - len(grp)
)

fval = betweenvar / withinvar
# Survival function (1 - `cdf`)
pval = stats.f.sf(fval, (len(grp) - 1), n - len(grp))

# Compute with scipy
fval, pval = stats.f_oneway(y[label == 0], y[label == 1], y[label == 2])


assert np.allclose(
    (fval, pval), stats.f_oneway(y[label == 0], y[label == 1], y[label == 2])
)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

"""

time_series

"""

# Pandas time series data structure

# Create a Series from a list
ser = pd.Series([1, 3])
print(ser)

# String as index
prices = {"apple": 4.99, "banana": 1.99, "orange": 3.99}
ser = pd.Series(prices)
print(ser)

x = pd.Series(np.arange(1, 3), index=[x for x in "ab"])
print(x)
print(x["b"])


print("------------------------------------------------------------")  # 60個

# Time series analysis of Google trends

df = pd.read_csv("data/multiTimeline.csv", skiprows=2)

print(df.head())


# Rename columns
df.columns = ["month", "diet", "gym", "finance"]

# Describe
print(df.describe())


df.month = pd.to_datetime(df.month)
df.set_index("month", inplace=True)

print(df.head())


df.plot()
plt.xlabel("Year")
plt.show()

# change figure parameters
# df.plot(figsize=(20,10), linewidth=5, fontsize=20)

# Plot single column
# df[['diet']].plot(figsize=(20,10), linewidth=5, fontsize=20)
# plt.xlabel('Year', fontsize=20)
# plt.show()

diet = df["diet"]

diet_resamp_yr = diet.resample("YE").mean()
diet_roll_yr = diet.rolling(12).mean()

ax = diet.plot(alpha=0.5, style="-")  # store axis (ax) for latter plots
diet_resamp_yr.plot(style=":", label="Resample at year frequency", ax=ax)
diet_roll_yr.plot(style="--", label="Rolling average (smooth), window size=12", ax=ax)
ax.legend()
plt.show()

# Rolling average (smoothing) with Numpy

x = np.asarray(df[["diet"]])
win = 12
win_half = int(win / 2)
# print([((idx-win_half), (idx+win_half)) for idx in np.arange(win_half, len(x))])

diet_smooth = np.array(
    [
        x[(idx - win_half) : (idx + win_half)].mean()
        for idx in np.arange(win_half, len(x))
    ]
)
plt.plot(diet_smooth)
plt.show()

gym = df["gym"]

df_avg = pd.concat([diet.rolling(12).mean(), gym.rolling(12).mean()], axis=1)
df_avg.plot()
plt.xlabel("Year")
plt.show()

# Detrending

df_dtrend = df[["diet", "gym"]] - df_avg
df_dtrend.plot()
plt.xlabel("Year")
plt.show()

# First-order differencing: seasonal patterns

# diff = original - shiftted data
# (exclude first term for some implementation details)
assert np.all((diet.diff() == diet - diet.shift())[1:])

df.diff().plot()
plt.xlabel("Year")
plt.show()


# Periodicity and correlation

df.plot()
plt.xlabel("Year")
plt.show()

print(df.corr())

# Plot correlation matrix

print(df.corr())

df.diff().plot()
plt.xlabel("Year")
plt.show()

print(df.diff().corr())

# Plot correlation matrix

print(df.diff().corr())

print("------------------------------")  # 30個

from statsmodels.tsa.seasonal import seasonal_decompose

x = gym

x = x.astype(float)  # force float
decomposition = seasonal_decompose(x)
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

plt.subplot(411)
plt.plot(x, label="Original")
plt.legend(loc="best")
plt.subplot(412)
plt.plot(trend, label="Trend")
plt.legend(loc="best")
plt.subplot(413)
plt.plot(seasonal, label="Seasonality")
plt.legend(loc="best")
plt.subplot(414)
plt.plot(residual, label="Residuals")
plt.legend(loc="best")
plt.tight_layout()
plt.show()

print("------------------------------")  # 30個

from pandas.plotting import autocorrelation_plot

x = df["diet"].astype(float)
autocorrelation_plot(x)

print("------------------------------")  # 30個

from statsmodels.tsa.stattools import acf

x_diff = x.diff().dropna()  # first item is NA
lag_acf = acf(x_diff, nlags=36, fft=True)
plt.plot(lag_acf)
plt.title("Autocorrelation Function")


print("------------------------------")  # 30個

from statsmodels.tsa.stattools import acf
from statsmodels.tsa.stattools import pacf

x = df["gym"].astype(float)

x_diff = x.diff().dropna()  # first item is NA
# ACF and PACF plots:

lag_acf = acf(x_diff, nlags=20, fft=True)
lag_pacf = pacf(x_diff, nlags=20, method="ols")

# Plot ACF:
plt.subplot(121)
plt.plot(lag_acf)
plt.axhline(y=0, linestyle="--", color="gray")
plt.axhline(y=-1.96 / np.sqrt(len(x_diff)), linestyle="--", color="gray")
plt.axhline(y=1.96 / np.sqrt(len(x_diff)), linestyle="--", color="gray")
plt.title("Autocorrelation Function  (q=1)")

# Plot PACF:
plt.subplot(122)
plt.plot(lag_pacf)
plt.axhline(y=0, linestyle="--", color="gray")
plt.axhline(y=-1.96 / np.sqrt(len(x_diff)), linestyle="--", color="gray")
plt.axhline(y=1.96 / np.sqrt(len(x_diff)), linestyle="--", color="gray")
plt.title("Partial Autocorrelation Function (p=1)")
plt.tight_layout()
plt.show()

print("------------------------------")  # 30個

import statsmodels.api as smapi

model = smapi.tsa.arima.ARIMA(x, order=(2, 1, 2))

results_ARIMA = model.fit()

plt.plot(x, "r")
plt.plot(results_ARIMA.fittedvalues, color="g")

plt.title("ARIMA")
plt.show()

cc = sum((results_ARIMA.fittedvalues - x) ** 2)
print("RSS: %.4f" % cc)


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
