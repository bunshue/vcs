"""
pandas一大堆



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


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

# 多圖組合
# jointplot兩變量圖

import statsmodels.api as sm

sns.set(style="darkgrid")
data = sm.datasets.ccard.load_pandas().data
sns.jointplot(
    x="AVGEXP", y="AGE", data=data, kind="reg", xlim=(0, 1000), ylim=(0, 50), color="m"
)
show()

print("------------------------------------------------------------")  # 60個

import statsmodels.api as sm

# pairplot多變量圖
data = sm.datasets.ccard.load_pandas().data
sns.pairplot(data, vars=["AGE", "INCOME", "INCOMESQ", "OWNRENT"])

show()

print("------------------------------------------------------------")  # 60個

# catplot兩變量關係圖
data = sm.datasets.fair.load_pandas().data
sns.catplot(x="occupation", y="affairs", hue="religious", data=data)

show()

print("------------------------------------------------------------")  # 60個

print("讀寫XML文件")

from xml.dom import minidom

dom = minidom.Document()
root_node = dom.createElement("root")  # 創建根節點
dom.appendChild(root_node)  # 添加根節點

book_node = dom.createElement("blog")  # 創建第一個子節點
book_node.setAttribute("level", "3")  # 添加屬性
root_node.appendChild(book_node)  # 爲root添加子節點

name_node = dom.createElement("addr")  # 創建第二個子節點
name_text = dom.createTextNode("https://blog.csdn.net/xieyan0811")  # 添加文字
name_node.appendChild(name_text)
root_node.appendChild(name_node)

# toxml() 轉換成字符串, toprettyxml()轉換成樹形縮進版式
print(dom.toprettyxml())
with open("tmp_test_dom.xml", "w") as fh:
    dom.writexml(fh, indent="", addindent="\t", newl="\n", encoding="UTF-8")

print("------------------------------")  # 30個

from xml.dom import minidom

with open("tmp_test_dom.xml", "r") as fh:
    dom = minidom.parse(fh)  # 獲取dom對象
    root = dom.documentElement  # 獲取根節點
    print("node name", root.nodeName)  # 顯示節點名: root
    print("node type", root.nodeType)  # 顯示節點類型
    print("child nodes", root.childNodes)  # 列出所有子節點
    blog = root.getElementsByTagName("blog")[0]  # 根據標籤名獲取元素列表
    print(blog.getAttribute("level"))  # 獲取屬性值
    addr = root.getElementsByTagName("addr")[0]
    print("addr's child nodes", addr.childNodes)
    text_node = addr.childNodes[0]  # 獲取文本節點內容
    print("text data", text_node.data)
    print("parent", addr.parentNode.nodeName)  # 顯示name的父節點名稱

print("------------------------------------------------------------")  # 60個

print("抓取網站數據")
""" NG
import urllib.request
from bs4 import BeautifulSoup

response = urllib.request.urlopen("https://blog.csdn.net/xieyan0811")
html = response.read().decode("utf-8","ignore") # 返回網頁爲utf-8編碼，解碼時忽略錯誤
reg = r'http://'  
soup = BeautifulSoup(html, 'html.parser')
for link in soup.find_all('a'):
    addr = link.get('href')
    # 顯示包含關鍵字的所有地址
    if addr != None and addr.find('xieyan0811/article') != -1: 
        print(addr)
"""
print("------------------------------------------------------------")  # 60個

print("簡單隨機抽樣")

import statsmodels.api as sm

data = sm.datasets.anes96.load_pandas().data
df = data.sample(50)
print(df.head())

print("系統抽樣")

index_list = [i for i in range(len(data)) if i % 10 == 0]
df = data.iloc[index_list]
print(df.head())

print("分層抽樣")


def typicalSampling(grp, typicalFracDict):
    name = grp.name
    frac = typicalFracDict[name]
    return grp.sample(frac=frac)


typicalFracDict = {
    0.0: 0.35,
    1.0: 0.5,
}
df = data.groupby("vote").apply(typicalSampling, typicalFracDict)
print(df.head())

print("整羣抽樣")
unique = np.unique(data["income"])
sample = random.sample(list(unique), 2)
df = pd.DataFrame()
for label in sample:
    tmp = data[data["income"] == label]
    df = pd.concat([df, tmp])
print(df.head())

print("------------------------------------------------------------")  # 60個

# sklearn

print("------------------------------------------------------------")  # 60個

print("線性迴歸")


def train(xArr, yArr):  # 訓練模型
    m, n = np.shape(xArr)
    xMat = np.mat(np.ones((m, n + 1)))  # 加第一列設爲1，用於計算截距
    x = np.mat(xArr)
    xMat[:, 1 : n + 1] = x[:, 0:n]
    yMat = np.mat(yArr).T
    xTx = xMat.T * xMat
    if np.linalg.det(xTx) == 0.0:  # 行列式的值爲0，無逆矩陣
        print("This matrix is sigular, cannot do inverse")
        return None
    ws = xTx.I * (xMat.T * yMat)
    return ws


def predict(xArr, ws):  # 預測
    m, n = np.shape(xArr)
    xMat = np.mat(np.ones((m, n + 1)))  # 加第一列設爲1, 爲計算截距
    x = np.mat(xArr)
    xMat[:, 1 : n + 1] = x[:, 0:n]
    return xMat * ws


if __name__ == "__main__":
    x = [[1], [2], [3], [4]]
    y = [4.1, 5.9, 8.1, 10.1]
    ws = train(x, y)
    if isinstance(ws, np.ndarray):
        print(ws)  # 返回結果：[[2.  ] [2.02]]
        print(predict([[5]], ws))  # 返回結果：[[12.1]]
        plt.scatter(x, y, s=20)  # 繪圖
        yHat = predict(x, ws)
        plt.plot(x, yHat, linewidth=2.0)
        show()

print("------------------------------------------------------------")  # 60個

print("邏輯迴歸")


def sigmoid(x):  # S函數實現
    return 1.0 / (1.0 + np.exp(-x))


x = np.arange(-10, 10, 0.2)  # 生成從-10, 10， 間隔爲0.2的數組
y = [sigmoid(i) for i in x]
plt.grid(True)  # 顯示網格
plt.plot(x, y)

show()

print("------------------------------------------------------------")  # 60個

print("信息量和熵")


def entropy(*c):
    if len(c) <= 0:
        return -1
    result = 0
    for x in c:
        result += (-x) * math.log(x, 2)
    return result


print(entropy(0.99, 0.01))
print(entropy(0.5, 0.5))
print(entropy(0.333, 0.333, 0.333))

print("------------------------------------------------------------")  # 60個

print("Apriori關聯規則")

from numpy import *


def load1():
    return [
        ["香蕉", "蘋果", "梨", "葡萄", "櫻桃", "西瓜", "芒果", "枇杷"],
        ["蘋果", "菠蘿", "梨", "香蕉", "荔枝", "芒果", "橙子"],
        ["菠蘿", "香蕉", "桔子", "橙子"],
        ["菠蘿", "梨", "枇杷"],
        ["蘋果", "香蕉", "梨", "荔枝", "枇杷", "芒果", "香瓜"],
    ]


# 建立所有物品集合
def create_collection_1(data):
    c = []
    for item in data:
        for g in item:
            if not [g] in c:
                c.append([g])
    c.sort()
    return list(map(frozenset, c))


def check_support(d_list, c_list, min_support):
    # d_list是購物數據，c_list是物品集合，support是支持度
    c_dic = {}  # 組合計數
    for d in d_list:  # 每次購物
        for c in c_list:  # 每個組
            if c.issubset(d):
                if c in c_dic:
                    c_dic[c] += 1  # 組合計數加1
                else:
                    c_dic[c] = 1  # 將組合加入字典
    d_count = float(len(d_list))  # 購物次數
    ret = []
    support_dic = {}
    for key in c_dic:
        support = c_dic[key] / d_count
        if support >= min_support:  # 判斷支持度
            ret.append(key)
        support_dic[key] = support  # 記錄支持度
    return ret, support_dic  # 返回滿足支持率的組和支持度字典


def create_collection_n(lk, k):
    ret = []
    for i in range(len(lk)):
        for j in range(i + 1, len(lk)):
            l1 = list(lk[i])[: k - 2]
            l1.sort()
            l2 = list(lk[j])[: k - 2]
            l2.sort()
            if l1 == l2:
                ret.append(lk[i] | lk[j])
    return ret


def apriori(data, min_support=0.5):
    c1 = create_collection_1(data)
    d_list = list(map(set, data))  # 將購物列表轉換成集合列表
    l1, support_dic = check_support(d_list, c1, min_support)
    l = [l1]
    k = 2
    while len(l[k - 2]) > 0:
        ck = create_collection_n(l[k - 2], k)  # 建立新組合
        lk, support = check_support(d_list, ck, min_support)  # 判斷新組是否適合支持率
        support_dic.update(support)
        l.append(lk)  # 將本次結果加入整體
        k += 1
    return l, support_dic


data = load1()
l, support_dic = apriori(data)
print(l)
print()
print(support_dic)

print("------------------------------------------------------------")  # 60個

print("樸素貝葉斯")

import jieba


def load2():
    arr = [
        "不知道該說什麼, 這麼爛的抄襲片也能上映, 我感到很尷尬",
        "天吶。一個大寫的滑稽。",
        "劇情太狗血，演技太浮誇，結局太無語。總體太渣了。這一個半小時廢了。",
        "畫面很美，音樂很好聽，主角演的很到位，很值得一看的電影，男主角很帥很帥，贊贊贊",
        "超級喜歡的一部愛情影片",
        "故事情節吸引人，演員演的也很好，電影裏的歌也好聽，總之值得一看，看了之後也會很感動的。",
    ]
    ret = []
    for i in arr:
        words = jieba.cut(i)  # 將句子切分成詞
        ret.append(words)
    return ret, [0, 0, 0, 1, 1, 1]


def create_vocab(data):
    vocab_set = set([])  # 使用set集合操作去掉重複出現的詞彙
    for document in data:
        vocab_set = vocab_set | set(document)
    return list(vocab_set)


def words_to_vec(vocab_list, vocab_set):  # 將句轉換成詞表格式
    ret = np.zeros(len(vocab_list))  # 創建數據表中的一行，並置初值爲0（不存在）
    for word in vocab_set:
        if word in vocab_list:
            ret[vocab_list.index(word)] = 1  # 若該詞在本句中出現，則設置爲1
    return ret


def train(X, y):
    rows = X.shape[0]
    cols = X.shape[1]
    percent = sum(y) / float(rows)  # 正例佔比
    p0_arr = np.ones(cols)  # 設置初值爲1，後作爲分子
    p1_arr = np.ones(cols)
    p0_count = 2.0  # 設初值爲2，後作爲分母
    p1_count = 2.0
    for i in range(rows):  # 按每句遍歷
        if y[i] == 1:
            p1_arr += X[i]  # 數組按每個值相加
            p1_count += sum(X[i])  # 句子所有詞個數相加(只計詞彙表中詞)
        else:
            p0_arr += X[i]
            p0_count += sum(X[i])
    p1_vec = np.log(p1_arr / p1_count)  # 正例時，每個詞出現概率
    p0_vec = np.log(p0_arr / p0_count)
    return p0_vec, p1_vec, percent


def predict(X, p0_vec, p1_vec, percent):
    p1 = sum(X * p1_vec) + np.log(percent)  # 爲1的概率
    p0 = sum(X * p0_vec) + np.log(1.0 - percent)  # 爲0的概率
    if p1 > p0:
        return 1
    else:
        return 0


sentences, y = load2()
vocab_list = create_vocab(sentences)
X = []
for sentence in sentences:
    X.append(words_to_vec(vocab_list, sentence))
p0_vec, p1_vec, percent = train(np.array(X), np.array(y))
test = jieba.cut("抄襲得那麼明顯也是醉了！")
print(test)
test_X = np.array(words_to_vec(vocab_list, test))
print(test_X)
print(test, "分類", predict(test_X, p0_vec, p1_vec, percent))

print("------------------------------------------------------------")  # 60個

print("Hyperopt")

# pip install hyperopt
from hyperopt import fmin, tpe, hp, Trials

trials = Trials()
best = fmin(
    fn=lambda x: (x - 1) ** 2,  # 最小化目標，如誤差函數
    space=hp.uniform("x", -10, 10),  # 定義搜索空間, 名稱爲x，範圍-10~10
    algo=tpe.suggest,  # 指定搜索算法
    trials=trials,  # 保存每次迭代的具體信息
    max_evals=50,
)  # 評估次數
print(best)  # 返回結果：{'x': 0.980859461591201}
for t in trials.trials:
    print(t["result"])

print("------------------------------------------------------------")  # 60個

# 做時序圖觀察基本的趨勢和週期
data = pd.read_csv("AirPassengers.csv")
ts = data["#Passengers"]
plt.plot(ts)

show()

print("------------------------------")  # 30個

# 分析平穩性，正態性，週期性；並對數據進行轉換
ts_log = np.log(ts)
ts_diff = ts_log.diff(1)
ts_diff = ts_diff.dropna()
plt.plot(ts_diff)

show()

print("------------------------------")  # 30個

# 做自相關和偏自相關圖，確定模型階次
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf

f = plot_acf(ts_diff)
show()

f = plot_pacf(ts_diff, method="ols")
show()

print("------------------------------")  # 30個

# 訓練模型
import statsmodels.api as smapi

model = smapi.tsa.arima.ARIMA(ts_log, order=(2, 1, 2))

results_ARIMA = model.fit()

plt.plot(ts_diff, color="r")
plt.plot(results_ARIMA.fittedvalues, color="g")

plt.title("ARIMA")
show()

cc = sum((results_ARIMA.fittedvalues - ts_log) ** 2)
print("RSS: %.4f" % cc)

print("------------------------------")  # 30個

# 轉換回原始波形
pred_diff = pd.Series(results_ARIMA.fittedvalues, copy=True)
pred_diff_cumsum = pred_diff.cumsum()
pred_log = pd.Series(ts_log, index=ts_log.index)
pred_log = pred_log.add(pred_diff_cumsum, fill_value=0)
pred = np.exp(pred_log)
plt.plot(ts)
plt.plot(pred)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("小波變換")

import pywt

data = pd.read_csv("AirPassengers.csv")
ts = data["#Passengers"]
ts_log = np.log(ts)
ts_diff = ts_log.diff(1)
ts_diff = ts_diff.dropna()

cA, cD = pywt.dwt(ts_diff, "db2")
cD = np.zeros(len(cD))
new_data = pywt.idwt(cA, cD, "db2")

plt.plot(ts_diff)
plt.plot(new_data - 0.5)
show()

print("------------------------------------------------------------")  # 60個

""" pip 失敗
import warnings
warnings.filterwarnings('ignore')

import tushare as ts
from fbprophet import Prophet
import datetime

# 數據準備
base = ts.get_hist_data('000002')
df = pd.DataFrame()
df['y'] = base['volume']
df['ds'] = base.index

# 日期插補
ds = df['ds'].min()
arr = []
while ds < df['ds'].max():
    ds = str(pd.to_datetime(ds) + datetime.timedelta(days=1))[:10]
    if ds not in np.array(df['ds']):
        arr.append({'ds':ds, 'y':0}) # 以字典方式加入數組
tmp = pd.DataFrame(arr)
df = pd.concat([tmp, df])
df = df.reset_index(drop=True)
df = df.sort_values(['ds'])


holidays = pd.read_csv('holiday.csv')

prophet = Prophet(holidays=holidays) 
prophet.fit(df)  
future = prophet.make_future_dataframe(freq='D',periods=30)  # 測試之後三十天
forecasts = prophet.predict(future)  

prophet.plot(forecasts).show() 
prophet.plot_components(forecasts).show() 
show()
"""
print("------------------------------------------------------------")  # 60個

# SnowNLP用法

from snownlp import SnowNLP

s = SnowNLP("跟框架學代碼設計，跟應用學功能設計")
print(s.words)  # 分詞
print(s.sentiments)  # 消極or積極，結果在0-1之間
print(s.tags)  # 詞性標註
print(s.keywords(3))  # 　關鍵詞
print(s.summary(3))  # 摘要
print(s.tf)  # tf
print(s.idf)  # idf

print("------------------------------------------------------------")  # 60個

from sklearn.model_selection import train_test_split
import warnings
import re
import tools  # 工具實現在tools.py文件中

warnings.filterwarnings("ignore")

# 讀訓練數據
data = pd.read_csv("data/weibo_train_data.txt", sep="\t", header=None)
data = tools.prepare(data)
data = tools.add_features(data)

# 切分訓練集和驗證集
train, val = train_test_split(data, test_size=0.2, random_state=0)
val = val.reset_index(drop=True)

# 按用戶分組
if True:
    grp = train.groupby("uid")
    user_data = pd.DataFrame()
    user_data["f"] = grp["f"].mean()
    user_data["c"] = grp["c"].mean()
    user_data["l"] = grp["l"].mean()
else:
    user_data = pd.read_csv("train_user.csv")
user_data_2 = user_data.rename(columns={"l": "avg_l", "c": "avg_c", "f": "avg_f"})
print(user_data.head())

print("------------------------------------------------------------")  # 60個

# 模型訓練
import xgboost as xgb


def testme_f(preds, dtrain):
    labels = pd.Series(dtrain.get_label())
    tmp = pd.DataFrame()
    d = ((preds - labels) / (labels + 5.0)).apply(lambda x: abs(x))
    count_i = labels
    precision = 1 - d
    sign = np.sign(precision - 0.8).apply(lambda x: 0 if x == -1 else 1)
    count_i[count_i > 50] = 50
    count_1 = sum((count_i + 1) * sign)
    count_2 = sum(count_i + 1)
    return "testme", 1 - count_1 / count_2


def testme_lc(preds, dtrain):
    labels = pd.Series(dtrain.get_label())
    tmp = pd.DataFrame()
    d = ((preds - labels) / (labels + 3.0)).apply(lambda x: abs(x))
    count_i = labels
    precision = 1 - d
    sign = np.sign(precision - 0.8).apply(lambda x: 0 if x == -1 else 1)
    count_i[count_i > 25] = 25
    count_1 = sum((count_i + 1) * sign)
    count_2 = sum(count_i + 1)
    return "testme", 1 - count_1 / count_2


def calc(grp1, grp2, features, key, params, feval):
    train_X = grp1[features]
    train_Y = grp1[key]
    val_X = grp2[features]
    val_Y = grp2[key]
    dtrain = xgb.DMatrix(train_X, train_Y)
    dval = xgb.DMatrix(val_X, val_Y)
    watchlist = [(dtrain, "train"), (dval, "val")]
    model = xgb.train(
        params,
        dtrain,
        evals=watchlist,
        feval=feval,
        num_boost_round=200,
        early_stopping_rounds=10,
    )
    model.save_model("tmp_model_" + key)
    dic = model.get_fscore()
    dic2 = sorted(dic.items(), key=lambda d: d[1], reverse=True)
    print("feature importance", dic2)
    return model


params = {
    "max_depth": 7,
    "subsample": 0.7,
    "eta": 0.05,
    "seed": 5,
    "objective": "reg:linear",
}

print("------------------------------------------------------------")  # 60個

# 提取關鍵詞
import jieba

# tmp=data.sample(n = 100000) # adjust
tmp = data.sample(n=1000)
arr = tmp["content"].unique()
print(len(arr))
arr_all = []
for i in arr:
    arr = jieba.cut(i, cut_all=True)
    arr_zh = [
        i
        for i in arr
        if len(re.findall(r"^[#\+a-z0-9A-Z\\-_]+$", i, re.M)) == 0 and len(i) > 1
    ]
    arr_all.extend(arr_zh)
print(len(arr_all))

result = pd.value_counts(arr_all)
arr_word = []
for key, value in result.items():
    if value > 5:
        arr_word.append(key)
print(arr_word)

print("------------------------------------------------------------")  # 60個

# 從文字中提取特徵
from scipy import stats


def get_dic(arr_word, dst, count, data):
    print(len(arr_word))
    dic_key = {}
    for idx, i in enumerate(arr_word):
        df1 = data[data["content"].str.contains(i) == False]
        df2 = data[data["content"].str.contains(i) == True]
        ret2 = stats.levene(df1[dst], df2[dst])
        if ret2[1] < 0.05:
            dic_key[i] = [ret2[1], df2[dst].mean(), len(df2)]
            print(idx, i, dic_key[i], len(dic_key))
            if len(dic_key) > count:
                break
    return dic_key


dic_key_f = get_dic(arr_word, "f", 100, data[:100000])
dic_key_c = get_dic(arr_word, "c", 50, data[:100000])
dic_key_l = get_dic(arr_word, "l", 100, data[:100000])

print("------------------------------------------------------------")  # 60個

val = pd.merge(val, user_data_2, on="uid", how="left")
train = pd.merge(train, user_data_2, on="uid", how="left")


# 生成新模型
def calc_dic(train, val, dst, dic):
    train_new = train.copy()
    for key in dic.keys():
        # print(key)
        train_new[key] = (
            train["content"].str.contains(key).apply(lambda x: 1 if x else 0)
        )
    val_new = val.copy()
    for key in dic.keys():
        val_new[key] = val["content"].str.contains(key).apply(lambda x: 1 if x else 0)
    features = [
        "weekday",
        "hour",
        "c_has_link",
        "c_has_at",
        "c_has_ex",
        "c_has_video",
        "c_has_ads",
        "c_has_share",
        "c_has_it",
        "avg_l",
        "avg_c",
        "avg_f",
        "c_has_topic",
    ]
    features_new = features + list(dic.keys())
    model = calc(train_new, val_new, features_new, dst, params, testme_f)
    return model


model_f = calc_dic(train, val, "f", dic_key_f)
model_c = calc_dic(train, val, "c", dic_key_c)
model_l = calc_dic(train, val, "l", dic_key_l)

print("------------------------------")  # 30個

# 保存模型
dic = {}
dic["model_f"] = model_f
dic["model_c"] = model_c
dic["model_l"] = model_l
dic["dic_key_f"] = dic_key_f
dic["dic_key_c"] = dic_key_c
dic["dic_key_l"] = dic_key_l
dic["user_data_2"] = user_data_2

""" import fail
from sklearn.externals import joblib
joblib.dump(dic, 'model.pkl')
"""

print("------------------------------")  # 30個


def do_pred(model, val, dic):
    val_new = val.copy()
    for key in dic.keys():
        val_new[key] = val["content"].str.contains(key).apply(lambda x: 1 if x else 0)
    features = [
        "weekday",
        "hour",
        "c_has_link",
        "c_has_at",
        "c_has_ex",
        "c_has_video",
        "c_has_ads",
        "c_has_share",
        "c_has_it",
        "avg_l",
        "avg_c",
        "avg_f",
        "c_has_topic",
    ]
    features_new = features + list(dic.keys())
    tmp = val_new[features_new]
    dtest = xgb.DMatrix(tmp)
    out = model.predict(dtest)
    out = pd.Series(out).apply(lambda x: int(x))
    return out


def do_pred_all(df):
    out = df.copy()
    out["f"] = do_pred(model_f, df, dic_key_f)
    out["l"] = do_pred(model_l, df, dic_key_l)
    out["c"] = do_pred(model_c, df, dic_key_c)
    return out


# 對驗證集預測
out = do_pred_all(val)
print(tools.do_score(val, out))

# 預測並生成提交數據
test = pd.read_csv("data/weibo_predict_data.txt", sep="\t", header=None)
test = tools.prepare(test)
test = tools.add_features(test)
test = pd.merge(test, user_data_2, on="uid", how="left")
test = test.fillna(0)
out = do_pred_all(test)
out["ss"] = (
    out["f"].astype(str) + "," + out["c"].astype(str) + "," + out["l"].astype(str)
)
out = out[["uid", "mid", "ss"]]
print(out.shape)
print(out.head())
out.to_csv("tmp_result_190624.txt", index=False, header=None, sep="\t")

print("------------------------------------------------------------")  # 60個

""" some fail
df = pd.read_csv('data/weibo_train_data.txt',sep='\t',header=None)
df = df.rename(columns={0:'uid',1:'m',2:'datetime',3:'f',4:'c',5:'l'})
print(df.shape)

print(df[5:10])
df[6:10].to_csv('weibo.csv',index=False, encoding='gbk',header=None)

print('------------------------------------------------------------')	#60個

counts = df[3].value_counts()
print(type(counts))
plt.plot(counts)

show()

df[3].value_counts()
print(len(df[df[3] == 0])/len(df))
print(len(df[df[3] < 50])/len(df))


grp = df.groupby(0)
print(len(grp))

df['feed_back'] = df[3]+df[4]+df[5]


counts = grp['feed_back'].count()
#plt.hist(counts, 200)

means = grp['feed_back'].mean()
count = 0
for i in means:
    print(i)
    if i == 0:
        count += 1
print(count)


means[means>500]
#print(df[df[0]=='6a989f414896b3ecec9ec9571d2489c5'])

"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import tensorflow as tf

print("------------------------------------------------------------")  # 60個

"""
手動下載
https://storage.googleapis.com/tensorflow/keras-applications/resnet/resnet50_weights_tf_dim_ordering_tf_kernels.h5
https://storage.googleapis.com/tensorflow/keras-applications/resnet/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5
https://storage.googleapis.com/tensorflow/keras-applications/inception_v3/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5
https://storage.googleapis.com/tensorflow/keras-applications/xception/xception_weights_tf_dim_ordering_tf_kernels_notop.h5
放在
~/.keras/models/
或
C:/Users/070601/.keras/models/
之下
"""

# from keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.resnet50 import ResNet50

# from keras.preprocessing import image
# from keras.utils import image_utils

# from keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions

model = ResNet50(weights="imagenet")
print(model.summary())  # 顯示模型基本信息

img_path = "elephant.jpg"
# img = image.load_img(img_path, target_size=(224, 224))
img = tf.keras.utils.load_img(img_path, target_size=(224, 224))
# x = image.img_to_array(img)
x = tf.keras.utils.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

preds = model.predict(x)
print("Predicted:", decode_predictions(preds, top=3)[0])

print("------------------------------------------------------------")  # 60個

"""
使用keras下載訓練好的模型（下載每個模型幾十分鐘）, 並用模型對提取圖片的特徵。
訓練集25000張圖式片， 測試集12500張圖片，用三個模型, 如果不使用GPU，約8小時以上。
本例中只使用了幾百張圖片, 花十幾分鍾跑一遍整體流程。 想訓練所有， 只需增加圖片數據即可。
"""

from keras.models import *
from keras.layers import *
from keras.applications import *
from keras.preprocessing.image import *
import h5py
import warnings

warnings.filterwarnings("ignore")


def get_features(MODEL, width, height, lambda_func=None):
    input_tensor = Input((height, width, 3))
    x = input_tensor
    if lambda_func:
        x = Lambda(lambda_func)(x)

    base_model = MODEL(input_tensor=x, weights="imagenet", include_top=False)
    model = Model(base_model.input, GlobalAveragePooling2D()(base_model.output))

    gen = ImageDataGenerator()
    # 注意 train 和 test 是圖片存儲路徑
    train_generator = gen.flow_from_directory(
        "train", (width, height), shuffle=False, batch_size=16
    )
    test_generator = gen.flow_from_directory(
        "test", (width, height), shuffle=False, batch_size=16, class_mode=None
    )
    # 不同的keras版本變量名略有不同，如: train_generator.samples train_generator.samples...
    train = model.predict_generator(train_generator, train_generator.samples)
    test = model.predict_generator(test_generator, test_generator.samples)

    """ some error
    with h5py.File("data_%s.h5"%MODEL.func_name) as h:
        h.create_dataset("train", data=train)
        h.create_dataset("test", data=test)
        h.create_dataset("label", data=train_generator.classes)
    """


get_features(ResNet50, 224, 224)
get_features(InceptionV3, 299, 299, inception_v3.preprocess_input)
get_features(Xception, 299, 299, xception.preprocess_input)

print("------------------------------------------------------------")  # 60個

# 訓練模型並預測，此處使用了深度學習模型，也可以換成機器學習模型

import h5py
from sklearn.utils import shuffle
from keras.models import *
from keras.layers import *

np.random.seed(12345678)
X_train = []
X_test = []

"""
for filename in ["data_ResNet50.h5", "data_Xception.h5", "data_InceptionV3.h5"]:
    with h5py.File(filename, 'r') as h:
        X_train.append(np.array(h['train']))
        X_test.append(np.array(h['test']))
        y_train = np.array(h['label'])

X_train = np.concatenate(X_train, axis=1)
X_test = np.concatenate(X_test, axis=1)
X_train, y_train = shuffle(X_train, y_train)

input_tensor = Input(X_train.shape[1:])
x = Dropout(0.5)(input_tensor)
x = Dense(1, activation='sigmoid')(x)
model = Model(input_tensor, x)

model.compile(optimizer='adadelta',
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(X_train, y_train, batch_size=128, nb_epoch=8, validation_split=0.2)
y_pred = model.predict(X_test, verbose=1)
y_pred = y_pred.clip(min=0.005, max=0.995)

print('------------------------------------------------------------')	#60個

# 用迭代訓練過程中的錯誤率做圖

import matplotlib.pyplot as plt

def plot_training(history):
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    epochs = range(len(acc))
    plt.plot(epochs, acc, 'b')
    plt.plot(epochs, val_acc, 'r')
    plt.legend(["acc", "val_acc"], loc='best')
    plt.title('Training and validation accuracy')
    show()
    loss = history.history['loss']
    val_loss = history.history['val_loss']   
    plt.plot(epochs, loss, 'b')
    plt.plot(epochs, val_loss, 'r')
    plt.legend(["loss", "val_loss"], loc='best')
    plt.title('Training and validation loss')
    show()

plot_training(history)
"""
print("------------------------------------------------------------")  # 60個

# should be the same
print("提取特徵")

from keras.models import *
from keras.layers import *
from keras.applications import *
from keras.preprocessing.image import *
import h5py
import warnings

warnings.filterwarnings("ignore")


def get_features(MODEL, width, height, lambda_func=None):
    input_tensor = Input((height, width, 3))
    x = input_tensor
    if lambda_func:
        x = Lambda(lambda_func)(x)

    base_model = MODEL(input_tensor=x, weights="imagenet", include_top=False)
    model = Model(base_model.input, GlobalAveragePooling2D()(base_model.output))

    gen = ImageDataGenerator()
    # 注意 train 和 test 是圖片存儲路徑
    train_generator = gen.flow_from_directory(
        "train", (width, height), shuffle=False, batch_size=16
    )
    test_generator = gen.flow_from_directory(
        "test", (width, height), shuffle=False, batch_size=16, class_mode=None
    )
    train = model.predict_generator(train_generator, train_generator.samples)
    test = model.predict_generator(test_generator, test_generator.samples)
    """ maybe the same
    with h5py.File("data_%s.h5"%MODEL.func_name) as h:
        h.create_dataset("train", data=train)
        h.create_dataset("test", data=test)
        h.create_dataset("label", data=train_generator.classes)
    """


get_features(ResNet50, 224, 224)
get_features(InceptionV3, 299, 299, inception_v3.preprocess_input)
get_features(Xception, 299, 299, xception.preprocess_input)

print("------------------------------------------------------------")  # 60個

print("訓練模型和預測")
""" NG
import h5py
from sklearn.utils import shuffle
from keras.models import *
from keras.layers import *

np.random.seed(12345678)
X_train = []
X_test = []

for filename in ["data_ResNet50.h5", "data_Xception.h5", "data_InceptionV3.h5"]:
    with h5py.File(filename, 'r') as h:
        X_train.append(np.array(h['train']))
        X_test.append(np.array(h['test']))
        y_train = np.array(h['label'])

X_train = np.concatenate(X_train, axis=1)
X_test = np.concatenate(X_test, axis=1)
X_train, y_train = shuffle(X_train, y_train)

input_tensor = Input(X_train.shape[1:])
x = Dropout(0.5)(input_tensor)
x = Dense(1, activation='sigmoid')(x)
model = Model(input_tensor, x)

model.compile(optimizer='adadelta',
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(X_train, y_train, batch_size=128, nb_epoch=8, validation_split=0.2)
y_pred = model.predict(X_test, verbose=1)
y_pred = y_pred.clip(min=0.005, max=0.995)

print('------------------------------')	#30個

#訓練結果分析

import matplotlib.pyplot as plt

def plot_training(history):
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    epochs = range(len(acc))
    plt.plot(epochs, acc, 'b')
    plt.plot(epochs, val_acc, 'r')
    plt.legend(["acc", "val_acc"], loc='best')
    plt.title('Training and validation accuracy')
    show()
    
loss = history.history['loss']
val_loss = history.history['val_loss']   
plt.plot(epochs, loss, 'b')
plt.plot(epochs, val_loss, 'r')
plt.legend(["loss", "val_loss"], loc='best')
plt.title('Training and validation loss')
show()

plot_training(history)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個
