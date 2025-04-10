"""
RFM 是一種客戶分析模型，根據客戶的消費行為以進行客戶區分的一種方法。

RFM
Recency (最近一次交易)
Frequency (交易頻率)
Monetary (交易金額)

通過這三個消費行為的維度，對客戶進行分類，找出最有價值、最活躍的顧客，
同時也能對不同層級的客戶進行相對應的行銷活動，進而實現精準分群行銷。

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
'''
trad_flow = pd.read_csv("data/RFM_TRAD_FLOW.csv", encoding="gbk")
cc = trad_flow.head(10)
print(cc)

# 通过 RFM方法 建立 模型

# 通过计算F反应客户对打折产品的偏好
F = trad_flow.groupby(["cumid", "type"])[["transID"]].count()
cc = F.head()
print(cc)

F_trans = pd.pivot_table(F, index="cumid", columns="type", values="transID")
cc = F_trans.head()
print(cc)

F_trans["Special_offer"] = F_trans["Special_offer"].fillna(0)
cc = F_trans.head()
print(cc)

F_trans["interest"] = F_trans["Special_offer"] / (
    F_trans["Special_offer"] + F_trans["Normal"]
)
cc = F_trans.head()
print(cc)

# 通过计算M反应客户的价值信息
M = trad_flow.groupby(["cumid", "type"])[["amount"]].sum()
cc = M.head()
print(cc)

M_trans = pd.pivot_table(M, index="cumid", columns="type", values="amount")
M_trans["Special_offer"] = M_trans["Special_offer"].fillna(0)
M_trans["returned_goods"] = M_trans["returned_goods"].fillna(0)
M_trans["value"] = (
    M_trans["Normal"] + M_trans["Special_offer"] + M_trans["returned_goods"]
)
cc = M_trans.head()
print(cc)

# 通过计算R反应客户是否为沉默客户
# 定义一个从文本转化为时间的函数
from datetime import datetime


def to_time(t):
    out_t = time.mktime(
        time.strptime(t, "%d%b%y:%H:%M:%S")
    )  ########此处修改为时间戳方便后面qcut函数分箱
    return out_t


a = "14JUN09:17:58:34"
print(to_time(a))

trad_flow["time_new"] = trad_flow.time.apply(to_time)
cc = trad_flow.head()
print(cc)

R = trad_flow.groupby(["cumid"])[["time_new"]].max()
cc = R.head()
print(cc)

# 构建模型，筛选目标客户

from sklearn import preprocessing

threshold = pd.qcut(F_trans["interest"], 2, retbins=True)[1][1]
binarizer = preprocessing.Binarizer(threshold=threshold)
interest_q = pd.DataFrame(
    binarizer.transform(F_trans["interest"].values.reshape(-1, 1))
)
interest_q.index = F_trans.index
interest_q.columns = ["interest"]

threshold = pd.qcut(M_trans["value"], 2, retbins=True)[1][1]
binarizer = preprocessing.Binarizer(threshold=threshold)
value_q = pd.DataFrame(binarizer.transform(M_trans["value"].values.reshape(-1, 1)))
value_q.index = M_trans.index
value_q.columns = ["value"]

threshold = pd.qcut(R["time_new"], 2, retbins=True)[1][1]
binarizer = preprocessing.Binarizer(threshold=threshold)
time_new_q = pd.DataFrame(binarizer.transform(R["time_new"].values.reshape(-1, 1)))
time_new_q.index = R.index
time_new_q.columns = ["time"]

analysis = pd.concat([interest_q, value_q, time_new_q], axis=1)

# analysis['rank']=analysis.interest_q+analysis.interest_q
analysis = analysis[["interest", "value", "time"]]
cc = analysis.head()
print(cc)

label = {
    (0, 0, 0): "无兴趣-低价值-沉默",
    (1, 0, 0): "有兴趣-低价值-沉默",
    (1, 0, 1): "有兴趣-低价值-活跃",
    (0, 0, 1): "无兴趣-低价值-活跃",
    (0, 1, 0): "无兴趣-高价值-沉默",
    (1, 1, 0): "有兴趣-高价值-沉默",
    (1, 1, 1): "有兴趣-高价值-活跃",
    (0, 1, 1): "无兴趣-高价值-活跃",
}
analysis["label"] = analysis[["interest", "value", "time"]].apply(
    lambda x: label[(x[0], x[1], x[2])], axis=1
)
cc = analysis.head()
print(cc)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# reshape
print("------------------------------------------------------------")  # 60個

# # 第5章 数据整合和数据清洗
# pandas学习参考： [十分钟搞定pandas](http://www.cnblogs.com/chaosimple/p/4153083.html)

# ## 5.1　数据整合

# 行列操作

# 1. 单列

# 拆分、堆叠列

table = pd.DataFrame(
    {
        "cust_id": [10001, 10001, 10002, 10002, 10003],
        "type": ["Normal", "Special_offer", "Normal", "Special_offer", "Special_offer"],
        "Monetary": [3608, 420, 1894, 3503, 4567],
    }
)


table

result = pd.pivot_table(table, index="cust_id", columns="type", values="Monetary")

pd.pivot_table(
    table,
    index="cust_id",
    columns="type",
    values="Monetary",
    fill_value=0,
    aggfunc="sum",
)

table1 = pd.pivot_table(
    table,
    index="cust_id",
    columns="type",
    values="Monetary",
    fill_value=0,
    aggfunc=np.sum,
).reset_index()
table1

pd.melt(
    table1,
    id_vars="cust_id",
    value_vars=["Normal", "Special_offer"],
    value_name="Monetary",
    var_name="TYPE",
)

# -------------------

# # 第5章3 RFM
# pandas学习参考： [十分钟搞定pandas](http://www.cnblogs.com/chaosimple/p/4153083.html)

# 無檔案??
trad_flow = pd.read_csv("data/RFM_TRAD_FLOW.csv", encoding="gbk")
cc = trad_flow.head(10)
print(cc)

# 2.计算 RFM

M = trad_flow.groupby(["cumid", "type"])[["amount"]].sum()

M_trans = pd.pivot_table(M, index="cumid", columns="type", values="amount")

F = trad_flow.groupby(["cumid", "type"])[["transID"]].count()
cc = F.head()
print(cc)

F_trans = pd.pivot_table(F, index="cumid", columns="type", values="transID")
cc = F_trans.head()
print(cc)

R = trad_flow.groupby(["cumid", "type"])[["time"]].max()
cc = R.head()
print(cc)

# R_trans=pd.pivot_table(R,index='cumid',columns='type',values='time')
# cc = R_trans.head()
# print(cc)

# 3.衡量客户对打折商品的偏好

M_trans["Special_offer"] = M_trans["Special_offer"].fillna(0)

M_trans["spe_ratio"] = M_trans["Special_offer"] / (
    M_trans["Special_offer"] + M_trans["Normal"]
)
cc = M_rank = M_trans.sort_values(
    "spe_ratio", ascending=False, na_position="last"
).head()
print(cc)

M_rank["spe_ratio_group"] = pd.qcut(M_rank["spe_ratio"], 4)  # 这里以age_oldest_tr字段等宽分为4段
cc = M_rank.head()
print(cc)

print("------------------------------------------------------------")  # 60個
# sampling
print("------------------------------------------------------------")  # 60個


def get_sample(df, sampling="simple_random", k=1, stratified_col=None):
    """
    对输入的 dataframe 进行抽样的函数

    参数:
        - df: 输入的数据框 pandas.dataframe 对象

        - sampling:抽样方法 str
            可选值有 ["simple_random", "stratified", "systematic"]
            按顺序分别为: 简单随机抽样、分层抽样、系统抽样

        - k: 抽样个数或抽样比例 int or float
            (int, 则必须大于0; float, 则必须在区间(0,1)中)
            如果 0 < k < 1 , 则 k 表示抽样对于总体的比例
            如果 k >= 1 , 则 k 表示抽样的个数；当为分层抽样时，代表每层的样本量

        - stratified_col: 需要分层的列名的列表 list
            只有在分层抽样时才生效

    返回值:
        pandas.dataframe 对象, 抽样结果
    """
    from functools import reduce

    len_df = len(df)
    if k <= 0:
        raise AssertionError("k不能为负数")
    elif k >= 1:
        assert isinstance(k, int), "选择抽样个数时, k必须为正整数"
        sample_by_n = True
        if sampling == "stratified":
            alln = (
                k * df.groupby(by=stratified_col)[stratified_col[0]].count().count()
            )  # 有问题的
            # alln=k*df[stratified_col].value_counts().count()
            if alln >= len_df:
                raise AssertionError("请确认k乘以层数不能超过总样本量")
    else:
        sample_by_n = False
        if sampling in ("simple_random", "systematic"):
            k = math.ceil(len_df * k)

    # print(k)

    if sampling == "simple_random":
        print("使用简单随机抽样")
        idx = random.sample(range(len_df), k)
        res_df = df.iloc[idx, :].copy()
        return res_df

    elif sampling == "systematic":
        print("使用系统抽样")
        step = len_df // k + 1  # step=len_df//k-1
        start = 0  # start=0
        idx = range(len_df)[start::step]  # idx=range(len_df+1)[start::step]
        res_df = df.iloc[idx, :].copy()
        # print("k=%d,step=%d,idx=%d"%(k,step,len(idx)))
        return res_df

    elif sampling == "stratified":
        assert stratified_col is not None, "请传入包含需要分层的列名的列表"
        assert all(np.in1d(stratified_col, df.columns)), "请检查输入的列名"

        grouped = df.groupby(by=stratified_col)[stratified_col[0]].count()
        if sample_by_n == True:
            group_k = grouped.map(lambda x: k)
        else:
            group_k = grouped.map(lambda x: math.ceil(x * k))

        res_df = pd.DataFrame(columns=df.columns)
        for df_idx in group_k.index:
            df1 = df
            if len(stratified_col) == 1:
                df1 = df1[df1[stratified_col[0]] == df_idx]
            else:
                for i in range(len(df_idx)):
                    df1 = df1[df1[stratified_col[i]] == df_idx[i]]
            idx = random.sample(range(len(df1)), group_k[df_idx])
            group_df = df1.iloc[idx, :].copy()
            res_df = pd.concat([res_df, group_df], axis=0, ignore_index=True)
        return res_df

    else:
        raise AssertionError("sampling is illegal")


clients = pd.read_csv("data/rfm_clients.csv", encoding="gbk")
# clients["district_id_c"]=clients["district_id"].map(lambda x:"id"+str(x))

# 在每个地区分别用简单随机抽样、分层抽样、系统抽样，三种方式抽取样本

# 简单随机抽样
# 简单随机抽样-按数量取
srn = get_sample(clients, sampling="simple_random", k=22, stratified_col=None)
# 简单随机抽样-按百分比取
srp = get_sample(clients, sampling="simple_random", k=0.1, stratified_col=None)

# 分层抽样
# 分层抽样-按每层数量取
strn = get_sample(clients, sampling="stratified", k=2, stratified_col=["district_id"])
# 分层抽样-按每层百分比取
strp = get_sample(clients, sampling="stratified", k=0.1, stratified_col=["district_id"])

# 系统抽样
# 系统抽样-按数量取
sysn = get_sample(clients, sampling="systematic", k=4, stratified_col=None)
# 系统抽样-按百分比取
sysp = get_sample(clients, sampling="systematic", k=0.1, stratified_col=None)

print("------------------------------------------------------------")  # 60個
# RFM2
print("------------------------------------------------------------")  # 60個

# # 第5章3 RFM
# pandas学习参考： [十分钟搞定pandas](http://www.cnblogs.com/chaosimple/p/4153083.html)

trad_flow = pd.read_csv("data/RFM_TRAD_FLOW.csv", encoding="gbk")
cc = trad_flow.head()
print(cc)

# 2.计算 RFM

# 先将非标准字符串时间格式化为时间数组，再转换为时间戳便于计算
trad_flow["time"] = trad_flow["time"].map(
    lambda x: time.mktime(time.strptime(x, "%d%b%y:%H:%M:%S"))
)

# 查找每个购物ID每个销售类型下的最近时间
R = trad_flow.groupby(["cumid", "type"])[["time"]].max()

# 转化为透视表
R_trans = pd.pivot_table(R, index="cumid", columns="type", values="time")

# 用最久远的购物时间替换缺失值
R_trans[["Special_offer", "returned_goods"]] = R_trans[
    ["Special_offer", "returned_goods"]
].apply(lambda x: x.replace(np.nan, min(x)), axis=0)
R_trans["R_max"] = R_trans[["Normal", "Presented", "Special_offer"]].apply(
    lambda x: max(x), axis=1
)

cc = R_trans.head()
print(cc)

# 对购物频率按照购物ID和购物类型进行汇总统计
F = trad_flow.groupby(["cumid", "type"])[["transID"]].count()

# 转化为透视表
F_trans = pd.pivot_table(F, index="cumid", columns="type", values="transID")

# 用0填补缺失值
F_trans[["Special_offer", "returned_goods"]] = F_trans[
    ["Special_offer", "returned_goods"]
].fillna(0)

# 将退货的频数转化为负数
F_trans["returned_goods"] = F_trans["returned_goods"].map(lambda x: -x)

# 求每个购物ID的购物总次数
F_trans["F_total"] = F_trans.apply(lambda x: sum(x), axis=1)

cc = F_trans.head()
print(cc)

# 对购物金额按照购物ID和购物类型进行汇总统计
M = trad_flow.groupby(["cumid", "type"])[["amount"]].sum()

# 转化为透视表
M_trans = pd.pivot_table(M, index="cumid", columns="type", values="amount")

# 用0填补缺失值
M_trans[["Special_offer", "returned_goods"]] = M_trans[
    ["Special_offer", "returned_goods"]
].fillna(0)

# 求每个购物ID的购物总金额
M_trans["M_total"] = M_trans.apply(lambda x: sum(x), axis=1)

cc = M_trans.head()
print(cc)

# 合并表
RFM = pd.concat([R_trans["R_max"], F_trans["F_total"], M_trans["M_total"]], axis=1)
# RFM三个维度等宽分箱打分
RFM["R_score"] = pd.cut(RFM.R_max, 3, labels=[1, 2, 3], precision=2)
RFM["F_score"] = pd.cut(RFM.F_total, 3, labels=[1, 2, 3], precision=2)
RFM["M_score"] = pd.cut(RFM.M_total, 3, labels=[1, 2, 3], precision=2)

print("依據 R_score F_score M_score 三欄位, 建立 Label 欄位")


# RFM各三类，总共有27种组合，为方便营销简化分类为8种
def score_label(a, b, c):
    """
    a: 'R_score'
    b: 'F_score'
    c: 'M_score'
    """
    if a == 3 and b == 3 and c == 3:
        return "重要价值客户"
    elif a == 3 and (b in [1, 2]) and c == 3:
        return "重要发展客户"
    elif (a in [1, 2]) and b == 3 and c == 3:
        return "重要保持客户"
    elif (a in [1, 2]) and (b in [1, 2]) and c == 3:
        return "重要挽留客户"
    elif a == 3 and b == 3 and (c in [1, 2]):
        return "一般价值客户"
    elif a == 3 and (b in [1, 2]) and (c in [1, 2]):
        return "一般发展客户"
    elif (a in [1, 2]) and b == 3 and (c in [1, 2]):
        return "一般保持客户"
    elif (a in [1, 2]) and (b in [1, 2]) and (c in [1, 2]):
        return "一般挽留客户"


cc = RFM.head()
print("貼標籤前 :\n", cc, sep="")

# 为每个购物ID贴标签
RFM["Label"] = RFM[["R_score", "F_score", "M_score"]].apply(
    lambda x: score_label(x[0], x[1], x[2]), axis=1
)

cc = RFM.head()
print("貼標籤後 :\n", cc, sep="")

# '重要价值客户'：消费额度高，购物频率高，最近购物时间也较近——该类客户是重要且忠实的大客户，要细心维护。
# '重要发展客户'：消费额度高，购物频率不高，最近购物时间较近——该类客户只是购物频率不高，有巨大的挖掘潜力，可根据该客户以往购物信息，进行个性
#                 化推荐，并发放购物优惠券刺激消费，增加客户粘性。
# '重要保持客户'：消费额度高，购物频率高，但最近购物时间较远——该类客户最近一次购物时间较久远，可能是快要流失的重要客户，可以让客户沟通了解其
#                 是不是哪项环节不够人性化体验不好，导致购物频率过低。
# '重要挽留客户'：消费额度高，购物频率不高，最近购物时间也较远——该类客户可能是已经流失的重要客户，如果还能联系上，可跟进了解其流失原因，对有
#                 相似客户特征的群体进行预警，针对性改进。
# '一般价值客户'：消费额度不高，购物频率高，最近购物时间也较近——该类客户对我们的产品感兴趣，很活跃，但购物金额过低，可能是价格敏感性客户，可
#                 对其组合金融产品增加其购买力。
# '一般发展客户'：消费额度不高，购物频率不高，最近购物时间较近——该类客户可能是我们的新晋客户，对我们的服务和产品进行试探性体验，可多留意此类
#                 客户，进行邮件短信关怀及时发送优惠信息。
# '一般保持客户'：消费额度不高，购物频率高，最近购物时间较远——该类客户可能是快要流失的一般客户，可进行一般性低成本营销。
# '一般挽留客户'：消费额度不高，购物频率不高，最近购物时间也较远——该类客户不是我们的目标客户，经费有限可忽略此类客户。
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# RFM 模型

data = pd.read_csv("data/RFM_TRAD_FLOW.csv", encoding="gbk")

cc = data.head()
print(cc)

# 查看数据的基本信息
data.info()

#查看数据缺失值
cc = data.isnull().sum()   #缺失数量
print(cc)

cc = data.isnull().mean()   #缺失比例
print(cc)

cc = data.time
print(cc)


# 特征工程

#封装成一个函数，对整理数据进行格式化
def to_time(t):
    out_t=pd.to_datetime(time.mktime(time.strptime(t,'%d%b%y:%H:%M:%S')),unit='s') 
    return out_t

#调用函数
data["time_new"]= data.time.apply(to_time)
cc = data.head()
print(cc)

# RFM模型计算
# R计算

# 最近一次消费时间
data.time_new.max()  #定义2010-09-26为取数时间
# Timestamp('2010-09-25 13:17:30')

R_trans = pd.DataFrame(data.groupby(['cumid'])['time_new'].max())
R_trans.columns=['time']
cc = R_trans.head()
print(cc)

R_trans['R'] = (data.time_new.max() - R_trans.time).dt.days
cc = R_trans
print(cc)

# F计算

# 消费频率
F = data.groupby(['cumid', 'type'])[['transID']].count()
cc = F.head(10)
print(cc)

# 取消堆叠
F_trans = F.unstack()
cc = F_trans.head()
print(cc)

cc = F_trans.columns
print(cc)

F_trans.columns = F_trans.columns.droplevel(0)
cc = F_trans.head()
print(cc)

cc = F_trans.isnull().sum()
print(cc)

F_trans['Special_offer'] = F_trans['Special_offer'].fillna(0)
cc = F_trans.head(10)
print(cc)

#填补缺失，因为退回、赠送商品不计入客户价值，不填充
#特价商品用0填充
F_trans["F"]=F_trans['Special_offer']/(F_trans['Special_offer']+F_trans['Normal'])
cc = F_trans.head()
print(cc)

cc = F_trans.isnull().sum()
print(cc)

# M计算

# 消费金额
M = data.groupby(['cumid', 'type'])[['amount']].count()
cc = M.head(10)
print(cc)

# 取消堆叠
M_trans = M.unstack()
cc = M_trans.head()
print(cc)

M_trans.columns = M_trans.columns.droplevel(0)
cc = M_trans.head()
print(cc)

# 填补缺失值
M_trans['Special_offer'] = M_trans['Special_offer'].fillna(0)
M_trans['returned_goods'] = M_trans['returned_goods'].fillna(0)
cc = M_trans.head()

M_trans["M"]=M_trans['Normal']+M_trans['Special_offer']+M_trans['returned_goods']
cc = M_trans.head()

# 模型整合
#拼接
analysis=pd.concat([R_trans["R"],F_trans["F"],M_trans["M"]],axis=1)
cc = analysis.head()

# RFM分段打分
# 5.1 F1 函数映射

#等频分箱
cc = pd.qcut(R_trans['R'],2,retbins=True)[0].value_counts()
print(cc)

#获取分箱阈值
cc = pd.qcut(R_trans['R'],2,retbins=True)[1][1]
print(cc)

#定义分段函数
def R_cut(x):
    if x<=12:
        return 1 
    else:
        return 0
analysis.R = analysis.R.apply(R_cut)
print(analysis)

# F 同理 
pd.qcut(F_trans['F'],2,retbins=True)[1][1]

# 定义F分段函数
def F_cut(x):
    if x<=pd.qcut(F_trans['F'],2,retbins=True)[1][1]:
        return 0
    else:
        return 1

analysis.F = analysis.F.apply(F_cut)
print(analysis)

# M同理
pd.qcut(M_trans['M'],2,retbins=True)[1][1]

def M_cut(x):
    if x<=pd.qcut(M_trans['M'],2,retbins=True)[1][1]:
        return 0
    else:
        return 1

analysis.M = analysis.M.apply(M_cut)
print(analysis)

# 5.2 算法库

# 3.构建模型，筛选目标客户：进行分段打分
# 导入sklearn中的预处理库：主要有编码、分箱、数值化转换……
from sklearn import preprocessing
cc = pd.qcut(F_trans['F'], 2, retbins=True)
print(cc)

threshold = pd.qcut(F_trans['F'], 2, retbins=True)[1][1]
preprocessing.Binarizer(threshold=threshold)

# Binarizer
# Binarizer(threshold=0.08333333333333333)

cc = F_trans['F'].values.reshape(-1, 1)
print(cc)

#通过等频分箱 取出阈值
threshold = pd.qcut(R_trans["R"], q=2, retbins=True)[1][1]
#用取出的阈值通过Binarizer进行二值化 01转换，相当于01编码
binarizer = preprocessing.Binarizer(threshold=threshold) #实例化
R_q = pd.DataFrame(binarizer.transform(R_trans["R"].values.reshape(-1, 1)))
R_q.index=R_trans.index
R_q.columns=["R"]
print(R_q)

# F同理
threshold = pd.qcut(F_trans['F'], 2, retbins=True)[1][1]
binarizer = preprocessing.Binarizer(threshold=threshold)
F_q = pd.DataFrame(binarizer.transform(F_trans['F'].values.reshape(-1, 1))) 
F_q.index=F_trans.index
F_q.columns=["F"]
print(F_q)

# M同理
threshold = pd.qcut(M_trans['M'], 2, retbins=True)[1][1]
binarizer = preprocessing.Binarizer(threshold=threshold)
M_q = pd.DataFrame(binarizer.transform(M_trans['M'].values.reshape(-1, 1)))
M_q.index=M_trans.index
M_q.columns=["M"]
print(M_q)

analysis1=pd.concat([F_q, M_q,R_q], axis=1)
analysis1 = analysis1[['F','M','R']]
cc = analysis1.head()
print(cc)

# RFM定性输出
label = {
    (0,0,0):'无兴趣-低价值-沉默',
    (1,0,0):'有兴趣-低价值-沉默',
    (1,0,1):'有兴趣-低价值-活跃',
    (0,0,1):'无兴趣-低价值-活跃',
    (0,1,0):'无兴趣-高价值-沉默',
    (1,1,0):'有兴趣-高价值-沉默',
    (1,1,1):'有兴趣-高价值-活跃',
    (0,1,1):'无兴趣-高价值-活跃'
}
analysis['label'] = analysis[['F','M','R']].apply(lambda x: label[(x[0],x[1],x[2])], axis = 1) 
cc = analysis.head()
print(cc)

analysis1['label'] = analysis1[['F','M','R']].apply(lambda x: label[(x[0],x[1],x[2])], axis = 1) 
cc = analysis1.head()
print(cc)

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
