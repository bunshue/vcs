"""
scipy

SciPy是一個開源的Python演算法庫和數學工具包。
SciPy包含的模組有最佳化、線性代數、積分、插值、特殊函數、快速傅立葉轉換、
訊號處理和圖像處理、常微分方程式求解和其他科學與工程中常用的計算。

scipy.integrate
scipy.special
scipy.interpolate
scipy.optimize
scipy.stats
scipy.signal

scipy.stats.norm

"""

import scipy

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
'''
print(
    "---- scipy.integrate 積分 --------------------------------------------------------"
)  # 60個


print("積分")


def my_funciton1(x):
    # return math.sin(x)
    # return (1 - x**2) ** 0.5    #上半圓
    return x**2 + 2 * x + 5  # f(x) = x**2 + 2x + 5


area, err = scipy.integrate.quad(my_funciton1, -3, 3)
print("積分結果 :", area)
print("誤差 :", err)

print("------------------------------------------------------------")  # 60個


# 計算半徑為r的圓的圓周
def calc_area(r):
    return 2 * math.pi * r


# 半徑2～5範圍的圓周總和
s = scipy.integrate.quad(calc_area, 2, 5)
print(s)

# 廁所衛生紙長度 若厚度為0.011
x = s[0] / 0.011
print(x)

print("------------------------------------------------------------")  # 60個

print(
    "---- scipy.special --------------------------------------------------------"
)  # 60個

a = scipy.special.exp10(3)
print("10^3 =", a)

b = scipy.special.exp2(3)
print("2^3 =", b)

c = scipy.special.sindg(90)
print("sind(90) =", c)

d = scipy.special.cosdg(45)
print("cosd(45) =", d)

print(
    "---- scipy.interpolate --------------------------------------------------------"
)  # 60個

print("內插法1")

x = np.arange(5, 20)
y = scipy.special.exp2(x / 3.0)
plt.plot(x, y, "o")

plt.show()

f = scipy.interpolate.interp1d(x, y)
x1 = np.arange(5, 20)
y1 = f(x1)
plt.plot(x, y, "o", x1, y1, "--")

plt.show()

print("內插法2")

x = [1, 2, 3, 4, 5]
y = [5, 8, 7, 4, 3]
plt.plot(x, y, "o")

plt.show()

f = scipy.interpolate.interp1d(x, y)
x1 = [1, 2, 3, 4, 5]
y1 = f(x1)
plt.plot(x, y, "o", x1, y1, "--")

xx = 1.5
yy = f(xx)
print("xx =", xx)
print("yy =", yy)

plt.grid()

plt.show()

print("------------------------------------------------------------")  # 60個

print(
    "---- scipy.optimize --------------------------------------------------------"
)  # 60個


def f(x):
    return x**2 + 15 * np.sin(x)


x = np.arange(-10, 10, 0.1)
plt.plot(x, f(x))

# plt.show()

print("------------------------------------------------------------")  # 60個

result = scipy.optimize.minimize(f, x0=0)
print(result.x)

plt.plot(x, f(x))
plt.plot(result.x, f(result.x), "o")

# plt.show()

print("------------------------------------------------------------")  # 60個


def fmax(x):
    """計算最大值"""
    return -(-3 * x**2 + 12 * x - 9)


def f(x):
    """求解方程式"""
    return -3 * x**2 + 12 * x - 9


a = -3
b = 12
c = -9
r1 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)  # r1
r1_y = f(r1)  # f(r1)
plt.text(r1 + 0.1, r1_y + -0.2, "(" + str(round(r1, 2)) + "," + str(0) + ")")
plt.plot(r1, r1_y, "-o")  # 標記
print("root1 = ", r1)  # print(r1)
r2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)  # r2
r2_y = f(r2)  # f(r2)
plt.text(r2 - 0.5, r2_y - 0.2, "(" + str(round(r2, 2)) + "," + str(0) + ")")
plt.plot(r2, r2_y, "-o")  # 標記
print("root2 = ", r2)  # print(r2)

# 計算最大值
r = scipy.optimize.minimize_scalar(fmax)
print("當x是 %4.2f 時, 有函數最大值 %4.2f" % (r.x, f(r.x)))
plt.text(
    r.x - 0.25,
    f(r.x) - 0.7,
    "(" + str(round(r.x, 2)) + "," + str(round(f(r.x), 2)) + ")",
)
plt.plot(r.x, f(r.x), "-o")  # 標記

# 繪製此函數圖形
x = np.linspace(0, 4, 50)
y = -3 * x**2 + 12 * x - 9
plt.plot(x, y, color="b")
plt.grid()

# plt.show()

print("------------------------------------------------------------")  # 60個


def f(x):
    """求解方程式"""
    return 3 * x**2 - 12 * x + 10


a = 3
b = -12
c = 10
r1 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)  # r1
r1_y = f(r1)  # f(r1)
plt.text(r1 + 0.1, r1_y - 0.2, "(" + str(round(r1, 2)) + "," + str(0) + ")")
plt.plot(r1, r1_y, "-o")  # 標記
print("root1 = ", r1)  # print(r1)
r2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)  # r2
r2_y = f(r2)  # f(r2)
plt.text(r2 - 0.6, r2_y - 0.2, "(" + str(round(r2, 2)) + "," + str(0) + ")")
plt.plot(r2, r2_y, "-o")  # 標記
print("root2 = ", r2)  # print(r2)

# 計算最小值
r = scipy.optimize.minimize_scalar(f)
print("當x是 %4.2f 時, 有函數最小值 %4.2f" % (r.x, f(r.x)))
plt.text(
    r.x - 0.25,
    f(r.x) + 0.3,
    "(" + str(round(r.x, 2)) + "," + str(round(f(r.x), 2)) + ")",
)
plt.plot(r.x, f(r.x), "-o")  # 標記

# 繪製此函數圖形
x = np.linspace(0, 4, 50)
y = 3 * x**2 - 12 * x + 10
plt.plot(x, y, color="b")

# plt.show()

print("------------------------------------------------------------")  # 60個


def fmax(x):
    """計算最大值"""
    return -(-3 * x**2 + 12 * x - 9)


def f(x):
    """求解方程式"""
    return -3 * x**2 + 12 * x - 9


a = -3
b = 12
c = -9
r1 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)  # r1
r1_y = f(r1)  # f(r1)
plt.text(r1 + 0.1, r1_y + -0.2, "(" + str(round(r1, 2)) + "," + str(0) + ")")
plt.plot(r1, r1_y, "-o")  # 標記
print("root1 = ", r1)  # print(r1)
r2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)  # r2
r2_y = f(r2)  # f(r2)
plt.text(r2 - 0.5, r2_y - 0.2, "(" + str(round(r2, 2)) + "," + str(0) + ")")
plt.plot(r2, r2_y, "-o")  # 標記
print("root2 = ", r2)  # print(r2)

# 計算最大值
r = scipy.optimize.minimize_scalar(fmax)
print("當x是 %4.2f 時, 有函數最大值 %4.2f" % (r.x, f(r.x)))
plt.text(
    r.x - 0.25,
    f(r.x) - 0.7,
    "(" + str(round(r.x, 2)) + "," + str(round(f(r.x), 2)) + ")",
)
plt.plot(r.x, f(r.x), "-o")  # 標記

print("------------------------------------------------------------")  # 60個

print(
    "---- scipy.stats --------------------------------------------------------"
)  # 60個


def normal_pdf(x, mu, sigma):
    pi = 3.1415926
    e = 2.718281
    f = (1.0 / np.sqrt(2 * pi * sigma**2)) * e ** (
        -((x - mu) ** 2) / (2.0 * sigma**2)
    )
    return f


ax = np.linspace(-5, 5, 100)
ay = [normal_pdf(x, 0, 1) for x in ax]
plt.plot(ax, ay)

# plt.show()

x = [x / 10.0 for x in range(-50, 60)]
plt.plot(x, scipy.stats.norm.pdf(x, 0, 1), "r-", lw=1, alpha=0.6, label="mu=0,sigma=1")
plt.plot(x, scipy.stats.norm.pdf(x, 0, 2), "b--", lw=1, alpha=0.6, label="mu=0,sigma=2")
plt.plot(x, scipy.stats.norm.pdf(x, 2, 1), "g-.", lw=1, alpha=0.6, label="mu=2,sigma=1")
plt.legend()
plt.title("Various Normal PDF")

# plt.show()

samples = [9, 3, 27]

desc = scipy.stats.describe(samples)
print(desc)

samples2 = [[1, 3, 27], [3, 4, 6], [7, 6, 3], [3, 6, 8]]

desc = scipy.stats.describe(samples2, axis=0)
print(desc)


desc = scipy.stats.describe(samples2, axis=1)
print(desc)

print(
    "---- scipy.signal --------------------------------------------------------"
)  # 60個

t = np.linspace(6, 10, 500)
w = scipy.signal.chirp(t, f0=4, f1=2, t1=5, method="linear")
plt.plot(t, w)
plt.title("Linear Chirp")
plt.xlabel("time in sec)")

# plt.show()

img = np.load("data/digit8.npy")

plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")

# plt.show()

print("------------------------------------------------------------")  # 60個

edge = [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("original image")
plt.subplot(1, 2, 2)
c_digit = scipy.signal.convolve2d(img, edge, boundary="symm", mode="same")
plt.imshow(c_digit, cmap="gray")
plt.axis("off")
plt.title("edge-detection image")

# plt.show()

print("------------------------------------------------------------")  # 60個

sharpen = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
plt.figure()
plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("original image")
plt.subplot(1, 2, 2)
c_digit = scipy.signal.convolve2d(img, sharpen, boundary="symm", mode="same")
plt.imshow(c_digit, cmap="gray")
plt.axis("off")
plt.title("sharpen image")

# plt.show()

print("------------------------------------------------------------")  # 60個

img = np.load("data/digit3.npy")
filters = [
    [[-1, -1, -1], [1, 1, 1], [0, 0, 0]],
    [[-1, 1, 0], [-1, 1, 0], [-1, 1, 0]],
    [[0, 0, 0], [1, 1, 1], [-1, -1, -1]],
    [[0, 1, -1], [0, 1, -1], [0, 1, -1]],
]

plt.figure()
plt.subplot(1, 5, 1)
plt.imshow(img, cmap="gray")
plt.axis("off")
plt.title("original")

for i in range(2, 6):
    plt.subplot(1, 5, i)
    c = scipy.signal.convolve2d(img, filters[i - 2], boundary="symm", mode="same")
    plt.imshow(c, cmap="gray")
    plt.axis("off")
    plt.title("filter" + str(i - 1))

# plt.show()

print("------------------------------------------------------------")  # 60個

A = np.array([[2, 3], [5, 7]])
B = scipy.linalg.inv(A)
print(B)

A = np.array([[3, 8], [4, 6]])
B = scipy.linalg.det(A)
print(B)

a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
b = np.array([2, 4, -1])

x = scipy.linalg.solve(a, b)
print(x)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("傑卡德相似係數 Jaccard Similarity Coefficient")

mat1 = [1, 1, 0, 1, 0, 1, 0, 0, 1]
mat2 = [0, 1, 1, 0, 0, 0, 1, 1, 1]
mat3 = [1, 1, 0, 1, 0, 1, 0, 0, 1]  # the same as mat1
mat4 = [0, 0, 1, 0, 1, 0, 1, 1, 0]  # invert of mat1

matV = np.mat([mat1, mat4])
print(type(matV))
print(matV)
print("傑卡德相似係數 : ")
print(scipy.spatial.distance.pdist(matV, "jaccard"))

print("------------------------------------------------------------")  # 60個


print(
    "---- scipy.stats.norm --------------------------------------------------------"
)  # 60個

# MH采样

data = np.random.randn(200)
print("平均 :", np.mean(data))


def sampler(
    data,
    samples=100,
    mu_init=0.2,
    proposal_width=0.1,
    plot=False,
    mu_prior_mu=0,
    mu_prior_sd=1.0,
):
    mu_current = mu_init
    posterior = [mu_current]
    for i in range(samples):
        mu_proposal = scipy.stats.norm(mu_current, proposal_width).rvs()

        likelihood_current = scipy.stats.norm(mu_current, 1).pdf(data).prod()
        likelihood_proposal = scipy.stats.norm(mu_proposal, 1).pdf(data).prod()

        prior_current = scipy.stats.norm(mu_prior_mu, mu_prior_sd).pdf(mu_current)
        prior_proposal = scipy.stats.norm(mu_prior_mu, mu_prior_sd).pdf(mu_proposal)

        p_current = likelihood_current * prior_current
        p_proposal = likelihood_proposal * prior_proposal

        p_accept = p_proposal / p_current

        accept = np.random.rand() < p_accept

        if accept:
            # Update position
            mu_current = mu_proposal
            posterior.append(mu_current)

    return posterior


tt = sampler(data, samples=5)
print(tt)

print("------------------------------------------------------------")  # 60個

import scipy.spatial.distance as dist

Vector1 = np.array([1, 1, 0, 1, 0, 1, 0, 0, 1])
Vector2 = np.array([0, 1, 1, 0, 0, 0, 1, 1, 1])
matV = np.mat([Vector1, Vector2])
print(matV)
print("dist.jaccard:", dist.pdist(matV, "jaccard"))

print("------------------------------------------------------------")  # 60個

print("關鍵字特徵")

from scipy import stats
import jieba
import re


def do_split(test_text):
    pattern = r',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|？|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】03   |·|！| |…|（|）'
    return re.split(pattern, test_text)


def get_keywords(data, feat):
    ret = []
    data[feat] = data[feat].apply(lambda x: x.strip())
    for i in data[feat].unique():
        # 將短句作爲關鍵字
        if len(i) <= 50 and i not in ret:
            ret.append(i)
        # 將子句作爲關鍵字
        for sentence in do_split(i):
            if len(sentence) <= 50 and sentence not in ret:
                ret.append(sentence)
        # 將詞作爲關鍵字
        for word in jieba.cut(i, cut_all=True):
            if len(word) > 1 and word not in ret:
                ret.append(word)
    return ret


def check_freq(data, feat, keywords, limit):
    ret = []
    for key in keywords:
        try:
            if len(data[data[feat].str.contains(key)]) > limit:
                ret.append(key)
        except:
            pass
    return ret


def do_test(data, feat, key, y, debug=False):
    arr1 = data[data[feat].str.contains(key) == True][y]
    arr2 = data[data[feat].str.contains(key) == False][y]
    ret1 = stats.ttest_ind(arr1, arr2, equal_var=False)
    ret2 = stats.levene(arr1, arr2)
    if ret1.pvalue < 0.05 or ret2.pvalue < 0.05:
        return True
    return False


def check(data, feat, y):
    ret = []
    keywords = get_keywords(data, feat)
    arr = check_freq(data, feat, keywords, 5)
    for word in arr:
        if do_test(data, feat, word, y):
            ret.append(word)
    return ret


# 讀取數據文件的前500條數據，其中第6個字段是微博內容，第5個字段爲點贊次數。
data = pd.read_csv("data/weibo_train_data.txt", sep="\t", header=None, nrows=500)
print(check(data, 6, 5))

print("------------------------------------------------------------")  # 60個

from scipy import stats

arr1 = [
    96,
    95,
    95,
    95,
    95,
    95,
    95,
    95,
    95,
    95,
    95,
    95,
    95,
    95,
    95,
    95,
    95,
    95,
    95,
    95,
    95,
    95,
    95,
    95,
    95,
    95,
    95,
    95,
    95,
    95,
]
arr2 = [
    90,
    91,
    92,
    93,
    94,
    90,
    91,
    92,
    93,
    94,
    90,
    91,
    92,
    93,
    94,
    90,
    91,
    92,
    93,
    94,
    90,
    91,
    92,
    93,
    94,
    90,
    91,
    92,
    93,
    94,
]
print(stats.ttest_1samp(arr1, 92))
print(stats.ttest_1samp(arr2, 92))
print((np.mean(arr1) - 92) / (np.std(arr1) / np.sqrt(len(arr1) - 1)))
print((np.mean(arr2) - 92) / (np.std(arr2) / np.sqrt(len(arr2) - 1)))

print("------------------------------------------------------------")  # 60個

from scipy import stats


print("正態性檢驗")

# 檢驗樣本是否服從某一分佈
np.random.seed(12345678)
x = stats.norm.rvs(loc=0, scale=1, size=300)  # loc爲均值，scale爲方差
print(stats.kstest(x, "norm"))

# 數據的正態性檢驗
np.random.seed(12345678)
x = stats.norm.rvs(loc=10, scale=2, size=70)
print(stats.shapiro(x))

# 作圖法檢驗正態分佈
np.random.seed(12345678)
x = stats.norm.rvs(loc=10, scale=2, size=300)
plt.hist(x)
plt.show()

print("------------------------------------------------------------")  # 60個

print("方差齊性檢驗")
np.random.seed(12345678)
rvs1 = stats.norm.rvs(loc=5, scale=10, size=500)
rvs2 = stats.norm.rvs(loc=25, scale=9, size=500)
print(stats.levene(rvs1, rvs2))


print("------------------------------------------------------------")  # 60個

from scipy import stats

print("兩獨立樣本T檢驗")
np.random.seed(12345678)
rvs1 = stats.norm.rvs(loc=5, scale=10, size=500)
rvs2 = stats.norm.rvs(loc=6, scale=10, size=500)
print(stats.ttest_ind(rvs1, rvs2))


print("配對樣本T檢驗")
np.random.seed(12345678)
rvs1 = stats.norm.rvs(loc=5, scale=10, size=500)
rvs2 = stats.norm.rvs(loc=5, scale=10, size=500) + stats.norm.rvs(scale=0.2, size=500)
print(stats.ttest_rel(rvs1, rvs2))

print("------------------------------------------------------------")  # 60個

from scipy import stats

a = [47, 56, 46, 56, 48, 48, 57, 56, 45, 57]  # 分組1
b = [87, 85, 99, 85, 79, 81, 82, 78, 85, 91]  # 分組2
c = [29, 31, 36, 27, 29, 30, 29, 36, 36, 33]  # 分組3
print(stats.f_oneway(a, b, c))


print("------------------------------------------------------------")  # 60個

from scipy import stats

A = [6, 15, 22, 36, 40, 48, 53]
B = [3, 4, 5, 12, 17, 18, 21]
print(stats.ranksums(A, B))

C = [1, 2, 3, 4, 5, 6, 7]
print(stats.kruskal(A, B, C))


print("------------------------------------------------------------")  # 60個

import statsmodels.api as sm
import scipy.stats as stats

data = sm.datasets.anes96.load_pandas().data
contingency = pd.crosstab(data["vote"], [data["educ"]])
print(stats.chi2_contingency(contingency))  # 卡方檢驗

print("------------------------------------------------------------")  # 60個

from scipy import stats

print("圖形描述相關性")
import statsmodels.api as sm

data = sm.datasets.ccard.load_pandas().data
plt.scatter(data["INCOMESQ"], data["INCOME"])

plt.show()

print("正態資料的相關分析")
np.random.seed(12345678)
a = np.random.normal(0, 1, 100)
b = np.random.normal(2, 2, 100)
print(stats.pearsonr(a, b))


print("非正態資料的相關分析")
print(stats.spearmanr([1, 2, 3, 4, 5], [1, 6, 7, 8, 20]))


print("------------------------------------------------------------")  # 60個

print("多元線性迴歸")
import statsmodels.api as sm

data = sm.datasets.ccard.load_pandas().data
model = sm.OLS(
    endog=data["AVGEXP"], exog=data[["AGE", "INCOME", "INCOMESQ", "OWNRENT"]]
).fit()

print("多元線性迴歸 總結")
print(model.summary())

print("------------------------------------------------------------")  # 60個

# 邏輯迴歸

import statsmodels.api as sm

data = sm.datasets.ccard.load_pandas().data
data["OWNRENT"] = data["OWNRENT"].astype(int)
model = sm.Logit(
    endog=data["OWNRENT"], exog=data[["AVGEXP", "AGE", "INCOME", "INCOMESQ"]]
).fit()

print("邏輯迴歸 總結")
print(model.summary())

print("------------------------------------------------------------")  # 60個

import statsmodels as sm
import tableone

data = sm.datasets.anes96.load_pandas().data
categorical = ["TVnews", "selfLR", "ClinLR", "educ", "income"]
groupby = "vote"
mytable = tableone.TableOne(data, categorical=categorical, groupby=groupby, pval=True)
print()
print()
print()
print()
print()
print(mytable)
mytable.to_excel("tmp_b.xlsx")

print("------------------------------------------------------------")  # 60個

print("方差、協方差、協方差矩陣")

# 數據準備
df = pd.DataFrame({"身高": [1.7, 1.8, 1.65, 1.75, 1.8], "體重": [140, 170, 135, 150, 200]})
print(df)

print("均值")
print(df["身高"].mean())

print("方差")
print(df["身高"].var())
print((sum((df["身高"] - df["身高"].mean()) ** 2)) / (len(df) - 1))

print("標準差")
print(df["身高"].std())

print("協方差")
print(
    (sum((df["體重"] - df["體重"].mean()) * (df["身高"] - df["身高"].mean())) / (len(df) - 1))
)

print("協方差矩陣")
print(df.cov())

print("相關係數和相關係數矩陣")
print(df.corr())

print("------------------------------------------------------------")  # 60個

print("距離與範數")

from scipy.spatial.distance import pdist  # 導入科學計算庫中的距離計算工具

df = pd.DataFrame({"身高": [1.7, 1.8, 1.65, 1.75, 1.8], "體重": [140, 170, 135, 150, 200]})
x = df.loc[0, :]  # 取第一條實例x
print(x)
y = df.loc[1, :]  # 取第二條實例y
print(y)

print("歐氏距離")
d1 = np.sqrt(np.sum(np.square(x - y)))  # 公式計算
d2 = pdist([x, y])  # 調用距離函數
print(d1, d2)

print("曼哈頓距離")
d1 = np.sum(np.abs(x - y))
d2 = pdist([x, y], "cityblock")
print(d1, d2)

print("海明距離")
d1 = pdist([x, y], "hamming")
d2 = pdist([[0, 0, 0, 1], [0, 0, 0, 8]], "hamming")  # 對比兩數組的海明距離
print(d1, d2)

print("閔氏距離")
d1 = np.sqrt(np.sum(np.square(x - y)))
d2 = pdist([x, y], "minkowski", p=2)  # 求取p=2時的閔氏距離
print(d1, d2)

print("切比雪夫距離")
d1 = np.max(np.abs(x - y))
d2 = pdist([x, y], "chebyshev")
print(d1, d2)

print("馬氏距離")
delta = x - y
S = df.cov()  # 協方差矩陣
SI = np.linalg.inv(S)  # 協方差矩陣的逆矩陣
d1 = np.sqrt(np.dot(np.dot(delta, SI), delta.T))
d2 = pdist([x, y], "mahalanobis", VI=SI)
print(d1, d2)

print("------------------------------------------------------------")  # 60個

from scipy.stats import loguniform

fig, ax = plt.subplots(1, 1)

a, b = 0.01, 1.25

r = loguniform.rvs(a, b, size=1000)  # Random variates

ax.hist(
    r,
    density=True,
    bins="auto",
    histtype="stepfilled",
    alpha=0.2,
    label="Random variates",
)
ax.legend(loc="best", frameon=False)

plt.show()

fig, ax = plt.subplots(1, 1)

ax.hist(np.log10(r))

ax.set_ylabel("Frequency")
ax.set_xlabel("Value of random variable")

ax.xaxis.set_major_locator(plt.FixedLocator([-2, -1, 0]))

ticks = ["$10^{{ {} }}$".format(i) for i in [-2, -1, 0]]
ax.set_xticklabels(ticks)

plt.show()

rvs = loguniform(2**-2, 2**0).rvs(size=1000)
fig, ax = plt.subplots(1, 1)

ax.hist(np.log2(rvs))

ax.set_ylabel("Frequency")
ax.set_xlabel("Value of random variable")

ax.xaxis.set_major_locator(plt.FixedLocator([-2, -1, 0]))
ticks = ["$2^{{ {} }}$".format(i) for i in [-2, -1, 0]]
ax.set_xticklabels(ticks)

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
'''
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
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
