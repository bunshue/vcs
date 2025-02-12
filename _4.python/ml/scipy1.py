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
print("scipy.integrate 積分")
print("------------------------------------------------------------")  # 60個


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
print("scipy.special")
print("------------------------------------------------------------")  # 60個

a = scipy.special.exp10(3)
print("10^3 =", a)

b = scipy.special.exp2(3)
print("2^3 =", b)

c = scipy.special.sindg(90)
print("sind(90) =", c)

d = scipy.special.cosdg(45)
print("cosd(45) =", d)


print("------------------------------------------------------------")  # 60個
print("scipy.interpolate")
print("------------------------------------------------------------")  # 60個

print("內插法1")

x = np.arange(5, 20)
y = scipy.special.exp2(x / 3.0)
plt.plot(x, y, "o")

show()

f = scipy.interpolate.interp1d(x, y)
x1 = np.arange(5, 20)
y1 = f(x1)
plt.plot(x, y, "o", x1, y1, "--")

show()

print("內插法2")

x = [1, 2, 3, 4, 5]
y = [5, 8, 7, 4, 3]
plt.plot(x, y, "o")

show()

f = scipy.interpolate.interp1d(x, y)
x1 = [1, 2, 3, 4, 5]
y1 = f(x1)
plt.plot(x, y, "o", x1, y1, "--")

xx = 1.5
yy = f(xx)
print("xx =", xx)
print("yy =", yy)

plt.grid()

show()

print("------------------------------------------------------------")  # 60個
print("scipy.optimize")
print("------------------------------------------------------------")  # 60個


def f(x):
    return x**2 + 15 * np.sin(x)


x = np.arange(-10, 10, 0.1)
plt.plot(x, f(x))

show()

print("------------------------------------------------------------")  # 60個

result = scipy.optimize.minimize(f, x0=0)
print(result.x)

plt.plot(x, f(x))
plt.plot(result.x, f(result.x), "o")

show()

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

show()

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

show()

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
print("scipy.stats")
print("------------------------------------------------------------")  # 60個


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

show()

x = [x / 10.0 for x in range(-50, 60)]
plt.plot(x, scipy.stats.norm.pdf(x, 0, 1), "r-", lw=1, alpha=0.6, label="mu=0,sigma=1")
plt.plot(x, scipy.stats.norm.pdf(x, 0, 2), "b--", lw=1, alpha=0.6, label="mu=0,sigma=2")
plt.plot(x, scipy.stats.norm.pdf(x, 2, 1), "g-.", lw=1, alpha=0.6, label="mu=2,sigma=1")
plt.legend()
plt.title("Various Normal PDF")

show()

samples = [9, 3, 27]

desc = scipy.stats.describe(samples)
print(desc)

samples2 = [[1, 3, 27], [3, 4, 6], [7, 6, 3], [3, 6, 8]]

desc = scipy.stats.describe(samples2, axis=0)
print(desc)


desc = scipy.stats.describe(samples2, axis=1)
print(desc)

print("------------------------------------------------------------")  # 60個
print("scipy.signal")
print("------------------------------------------------------------")  # 60個

t = np.linspace(6, 10, 500)
w = scipy.signal.chirp(t, f0=4, f1=2, t1=5, method="linear")
plt.plot(t, w)
plt.title("Linear Chirp")
plt.xlabel("time in sec)")

show()

img = np.load("data/digit8.npy")

plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")

show()

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

show()

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

show()

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

show()

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

print("------------------------------------------------------------")  # 60個
print("scipy.stats.norm")
print("------------------------------------------------------------")  # 60個

# MH採樣

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

print("------------------------------------------------------------")  # 60個
print("from scipy import stats")
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
show()

print("------------------------------------------------------------")  # 60個

from scipy import stats

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

# 目前kilo只能用 pip install statsmodels==0.13.2
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

show()

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

show()

fig, ax = plt.subplots(1, 1)

ax.hist(np.log10(r))

ax.set_ylabel("Frequency")
ax.set_xlabel("Value of random variable")

ax.xaxis.set_major_locator(plt.FixedLocator([-2, -1, 0]))

ticks = ["$10^{{ {} }}$".format(i) for i in [-2, -1, 0]]
ax.set_xticklabels(ticks)

show()

rvs = loguniform(2**-2, 2**0).rvs(size=1000)
fig, ax = plt.subplots(1, 1)

ax.hist(np.log2(rvs))

ax.set_ylabel("Frequency")
ax.set_xlabel("Value of random variable")

ax.xaxis.set_major_locator(plt.FixedLocator([-2, -1, 0]))
ticks = ["$2^{{ {} }}$".format(i) for i in [-2, -1, 0]]
ax.set_xticklabels(ticks)

show()

print("------------------------------------------------------------")  # 60個

from scipy import stats

n = 5
p = 1 / 6
for k in range(n + 1):
    v = stats.binom.pmf(k, n, p)
    print(k, v)

print("------------------------------------------------------------")  # 60個

from scipy import stats

fair_dice_rolls = stats.binom.rvs(n=5, p=1 / 6, size=10000)
print(fair_dice_rolls)
df = pd.DataFrame(fair_dice_rolls)
df.hist(range=(-0.5, 5.5), bins=6)
show()

print("------------------------------------------------------------")  # 60個

from scipy import stats

fair_dice_rolls = stats.binom.rvs(n=10, p=0.5, size=10000)
print(fair_dice_rolls)
df = pd.DataFrame(fair_dice_rolls)
df.hist(range=(-0.5, 10.5), bins=11)
show()

print("------------------------------------------------------------")  # 60個

from scipy import stats

n = 10
p = 1 / 2
for k in range(n + 1):
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

x = [x / 10.0 for x in range(-50, 60)]
plt.plot(x, stats.norm.pdf(x, 0, 1), "r-", lw=1, alpha=0.6, label="mu=0,sigma=1")
plt.plot(x, stats.norm.pdf(x, 0, 2), "b--", lw=1, alpha=0.6, label="mu=0,sigma=2")
plt.plot(x, stats.norm.pdf(x, 2, 1), "g-.", lw=1, alpha=0.6, label="mu=2,sigma=1")
plt.legend()
plt.title("常態分配PDF的機率")
show()

print("------------------------------------------------------------")  # 60個

from scipy.stats import norm

sigma = 1
mu = 0
x = np.linspace(-10, 10, 1000)
dist = norm(mu, sigma)
plt.plot(x, dist.pdf(x), ls="-", c="black", label="mu=0,sigma=1")
plt.xlim(-5, 5)
plt.ylim(0, 0.45)
plt.xlabel("x")
plt.ylabel("P(x)")
plt.title("標準常態分配(Standard Normal Distribution)")
plt.legend()
show()

print("------------------------------------------------------------")  # 60個

from scipy import stats

dice = [1, 2, 3, 4, 5, 6]
population = []
for x in range(10000):
    sample = np.random.choice(a=dice, size=100)
    population.append(sample.mean())
print("母體平均:", sum(population) / 10000.0)

sample_size = 100
sample = np.random.choice(a=population, size=sample_size)

sample_mean = sample.mean()
print("樣本平均:", sample_mean)
sample_stdev = sample.std()
print("樣本標準差:", sample_stdev)
sigma = sample_stdev / math.sqrt(sample_size - 1)
print("樣本計算出的母體標準差:", sigma)
z_critical = stats.norm.ppf(q=0.975)
print("Z分數:", z_critical)
margin_of_error = z_critical * sigma
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
print(confidence_interval)
conf_int = stats.norm.interval(alpha=0.95, loc=sample_mean, scale=sigma)
print(conf_int[0], conf_int[1])

print("------------------------------------------------------------")  # 60個

from scipy import stats

dice = [1, 2, 3, 4, 5, 6]
population = []
for x in range(10000):
    sample = np.random.choice(a=dice, size=100)
    population.append(sample.mean())
print("母體平均:", sum(population) / 10000.0)

sample_size = 20
sample = np.random.choice(a=population, size=sample_size)

sample_mean = sample.mean()
print("樣本平均:", sample_mean)
sample_stdev = sample.std()
print("樣本標準差:", sample_stdev)
sigma = sample_stdev / math.sqrt(sample_size - 1)
print("樣本計算出的母體標準差:", sigma)
t_critical = stats.t.ppf(q=0.975, df=sample_size - 1)
print("t分數:", t_critical)
margin_of_error = t_critical * sigma
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
print(confidence_interval)
""" NG
conf_int = stats.t.interval(
    alpha=0.95, df=sample_size - 1, loc=sample_mean, scale=sigma
)
print(conf_int[0], conf_int[1])
"""
print("------------------------------------------------------------")  # 60個

from scipy import stats

population_mean = 70
sample_size = 100
sample_mean = 71.5
print("樣本平均:", sample_mean)
sigma = 2.5
print("母體標準差:", sigma)
z_obtained = (sample_mean - population_mean) / (sigma / math.sqrt(sample_size))
print("Z檢定統計量:", z_obtained)
z_critical = stats.norm.ppf(q=0.975)
print("Z分數:", z_critical)

print("------------------------------------------------------------")  # 60個

from scipy import stats

population_mean = 500
sample = np.array([502.2, 501.6, 499.8, 502.8, 498.6, 502.2, 499.2, 503.4, 499.2])
sample_size = len(sample)
sample_mean = sample.mean()
print("樣本平均:", sample_mean)
sample_stdev = sample.std()
print("樣本標準差:", sample_stdev)
sigma = sample_stdev / math.sqrt(sample_size - 1)
print("樣本計算出的母體標準差:", sigma)
t_obtained = (sample_mean - population_mean) / sigma
print("檢定統計量:", t_obtained)
print(stats.ttest_1samp(a=sample, popmean=population_mean))

t_critical = stats.t.ppf(q=0.975, df=sample_size - 1)
print("t分數:", t_critical)

print("------------------------------------------------------------")  # 60個

from scipy import stats

observed = np.array([20, 16, 34, 40, 38, 32])
expected = np.array([30, 30, 30, 30, 30, 30])

df = len(observed) - 1
print("自由度:", df)
chi_squared_stat = (((observed - expected) ** 2) / expected).sum()
print("卡方檢定統計量:", chi_squared_stat)

chi_squared, p_value = stats.chisquare(f_obs=observed, f_exp=expected)
print(chi_squared, p_value)

crit = stats.chi2.ppf(q=0.95, df=df)
print("臨界區: ", crit)

print("------------------------------------------------------------")  # 60個

from scipy import stats

voter_gender = np.array((["男"] * 352) + (["男"] * 315) + (["女"] * 217) + (["女"] * 331))
voter_favorite = np.array(
    (["喜歡"] * 352) + (["不喜歡"] * 315) + (["喜歡"] * 217) + (["不喜歡"] * 331)
)
voters = pd.DataFrame({"gender": voter_gender, "favorite": voter_favorite})
voter_tab = pd.crosstab(voters.gender, voters.favorite, margins=True)
voter_tab.columns = ["喜歡", "不喜歡", "小計"]
voter_tab.index = ["男", "女", "小計"]
observed = voter_tab.iloc[0:3, 0:3]
print(observed)
print("---------------------------")
expected = np.outer(voter_tab["小計"][0:2], voter_tab.loc["小計"][0:2]) / 1215
expected = pd.DataFrame(expected)
expected.columns = ["喜歡", "不喜歡"]
expected.index = ["男", "女"]
print(expected)
print("---------------------------")
rows = 2
columns = 2
df = (rows - 1) * (columns - 1)
print("自由度:", df)
chi_squared_stat = (((observed - expected) ** 2) / expected).sum().sum()
print("卡方檢定統計量:", chi_squared_stat)

chi_squared, p_value, degree_of_freedom, matrix = stats.chi2_contingency(
    observed=observed
)
print(chi_squared, p_value)

crit = stats.chi2.ppf(q=0.95, df=df)
print("臨界區: ", crit)

print("------------------------------------------------------------")  # 60個

"""
【Python笔记】Scipy.stats.norm函数解析
scipy.stats.norm函数 可以实现正态分布（也就是高斯分布）
pdf ——概率密度函数
norm.pdf(x, loc, scale)等同于norm.pdf(y) / scale ，其中 y = (x - loc) / scale
"""

from scipy import stats

plt.figure(figsize=(12, 8))
x = np.linspace(-5, 5, num=20)

plt.subplot(2, 2, 1)
# 第1种调用方式
gauss1 = stats.norm(loc=0, scale=2)  # loc: mean 均值， scale: standard deviation 标准差
gauss2 = stats.norm(loc=1, scale=3)
y1 = gauss1.pdf(x)
y2 = gauss2.pdf(x)

plt.plot(x, y1, color="orange", label="u=0,sigma=2")
plt.plot(x, y2, color="green", label="u=1,sigma=3")
plt.legend(loc="upper right")

plt.subplot(2, 2, 2)
# 第2种调用方式
y1 = stats.norm.pdf(x, loc=0, scale=2)
y2 = stats.norm.pdf(x, loc=1, scale=3)

plt.plot(x, y1, color="r", label="u=0,sigma=2")
plt.plot(x, y2, color="b", label="u=1,sigma=3")
plt.legend(loc="upper right")


# stats.norm.pdf 和 stats.norm.rvs的区别
plt.subplot(2, 2, 3)
y1 = stats.norm.rvs(loc=0, scale=2, size=20)
y2 = stats.norm.rvs(loc=1, scale=3, size=20)

plt.plot(x, y1, color="black", linestyle=":", label="u=0,sigma=2")
plt.plot(x, y2, color="purple", label="u=1,sigma=3")
plt.legend(loc="upper right")

plt.subplot(2, 2, 4)
y1 = sorted(stats.norm.rvs(loc=0, scale=2, size=20))
y2 = sorted(stats.norm.rvs(loc=1, scale=3, size=20))

plt.plot(x, y1, color="black", linestyle=":", label="u=0,sigma=2")
plt.plot(x, y2, color="purple", label="u=1,sigma=3")
plt.legend(loc="upper right")

show()

"""
图221 和 图222 是代表调用stats.norm.pdf方法，画出均值为u，方差为sigma的概率密度分布图。

图223 和 图224 是代表调用stats.norm.rvs方法，rvs:随机变量（就是从这个分布中抽一些样本），而不是概率密度分布哦！
"""

print(gauss1)
# <scipy.stats._distn_infrastructure.rv_frozen object at 0x121F7DB0>

print(stats.norm.rvs(loc=0, scale=2, size=10))
# [ 4.04968057 -0.85376074  4.62058049  1.25731984 -0.11082284 -2.63972507 0.81014329 -0.37101067 -0.20334414  2.65743079]

"""
stats.norm主要公共方法如下：

rvs:随机变量（就是从这个分布中抽一些样本）
pdf：概率密度函数。
cdf：累计分布函数
sf：残存函数（1-CDF）
ppf：分位点函数（CDF的逆）
isf：逆残存函数（sf的逆）
stats:返回均值，方差，（费舍尔）偏态，（费舍尔）峰度。
moment:分布的非中心矩。
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


# 以下新進


# 馬哈拉諾比斯距離

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

# 馬哈拉諾比斯距離
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
show()

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
show()

print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(5, 3))
plt.bar([0, 1, 2, 3], [1 / 8, 3 / 8, 3 / 8, 1 / 8], width=0.9)
_ = plt.xticks([0, 1, 2, 3], [0, 1, 2, 3])
plt.xlabel("Distribution of the number of head over 3 flip under the null hypothesis")
show()

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

show()

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

show()

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

show()

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

show()

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
plt.xlabel("年資")
plt.ylabel("薪水")
plt.title("線性迴歸")
show()

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

show()

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

show()

print("------------------------------------------------------------")  # 60個

import scipy.stats as stats

url = "data/birthwt.csv"

df = pd.read_csv(url)

print(df.head())

print(stats.pearsonr(df.age, df.bwt))
print(stats.pearsonr(df.bwt, df.lwt))

plt.plot(df.bwt, df.lwt, "o")
show()

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
plt.xlabel("年資")
plt.ylabel("薪水")

show()

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
show()

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
# NG sklearn.feature_selection.f_regression(x.reshape((n, 1)), y)

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
Xpinv = scipy.linalg.pinv(X)
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
show()

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

url = "data/birthwt.csv"
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

# time_series

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
show()

# change figure parameters
# df.plot(figsize=(20,10), linewidth=5, fontsize=20)

# Plot single column
# df[['diet']].plot(figsize=(20,10), linewidth=5, fontsize=20)
# plt.xlabel('Year', fontsize=20)
show()

diet = df["diet"]

diet_resamp_yr = diet.resample("YE").mean()
diet_roll_yr = diet.rolling(12).mean()

ax = diet.plot(alpha=0.5, style="-")  # store axis (ax) for latter plots
diet_resamp_yr.plot(style=":", label="Resample at year frequency", ax=ax)
diet_roll_yr.plot(style="--", label="Rolling average (smooth), window size=12", ax=ax)
ax.legend()
show()

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
show()

gym = df["gym"]

df_avg = pd.concat([diet.rolling(12).mean(), gym.rolling(12).mean()], axis=1)
df_avg.plot()
plt.xlabel("Year")
show()

# Detrending

df_dtrend = df[["diet", "gym"]] - df_avg
df_dtrend.plot()
plt.xlabel("Year")
show()

# First-order differencing: seasonal patterns

# diff = original - shiftted data
# (exclude first term for some implementation details)
assert np.all((diet.diff() == diet - diet.shift())[1:])

df.diff().plot()
plt.xlabel("Year")
show()


# Periodicity and correlation

df.plot()
plt.xlabel("Year")
show()

print(df.corr())

# Plot correlation matrix

print(df.corr())

df.diff().plot()
plt.xlabel("Year")
show()

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
show()

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
show()

print("------------------------------")  # 30個

import statsmodels.api as smapi

model = smapi.tsa.arima.ARIMA(x, order=(2, 1, 2))

results_ARIMA = model.fit()

plt.plot(x, "r")
plt.plot(results_ARIMA.fittedvalues, color="g")

plt.title("ARIMA")
show()

cc = sum((results_ARIMA.fittedvalues - x) ** 2)
print("RSS: %.4f" % cc)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
