"""


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

print("讀取一個資料夾內的所有csv檔, 用區域變數存起來")
foldername = "D:/_git/vcs/_big_files/Bankcredit"
os.chdir(foldername)
print('目前目錄 :', os.getcwd())

loanfile = os.listdir()
createVar = locals()  # 字典
print(type(createVar))
for i in loanfile:
    # print(i)
    if i.endswith("csv"):
        print("csv檔  :", i)
        createVar[i.split(".")[0]] = pd.read_csv(i, encoding="gbk")
        print("前檔名 :", i.split(".")[0])

print(createVar)
print(type(createVar))

print("------------------------------------------------------------")  # 60個

# 生成被解释变量bad_good

bad_good = {"A": 0, "B": 1, "C": 2, "D": 1}

cc = loans.head()
# print(cc)
print(type(loans))

print("df loans 來自 loans.csv")
print("df loans 加一欄 bad_good, 由 loans的status欄對應")
loans["bad_good"] = loans.status.map(bad_good)

cc = loans.head()
print(cc)
print()
print()

# ## 1.3、借款人的年龄、性别

# 表征信息：

print("df合併")

print("loans :\n", loans.head(), sep="")
print("shape :", loans.shape)
print()
print("disp :\n", disp.head(), sep="")
print("shape :", disp.shape)
print()

print("依據account_id合併, 以左df為準")
data2 = pd.merge(loans, disp, on="account_id", how="left")

cc = data2.head()
print(cc)
print("shape :", data2.shape)
print(data2.columns)

data2 = pd.merge(data2, clients, on="client_id", how="left")
cc = data2.head()
print(cc)

data2 = data2[data2.type == "所有者"]

cc = data2.head()
print(cc)

# ## 1.4、借款人居住地的经济状况

# 状态信息：
data3 = pd.merge(data2, district, left_on="district_id", right_on="A1", how="left")
cc = data3.head()
print(cc)

# ## 1.5、贷款前一年内的账户平均余额、余额的标准差、变异系数、平均收入和平均支出的比例
# 行为信息：
data_4temp1 = pd.merge(
    loans[["account_id", "date"]],
    trans[["account_id", "type", "amount", "balance", "date"]],
    on="account_id",
)
data_4temp1.columns = ["account_id", "date", "type", "amount", "balance", "t_date"]
data_4temp1 = data_4temp1.sort_values(by=["account_id", "t_date"])

data_4temp1["date"] = pd.to_datetime(data_4temp1["date"])
data_4temp1["t_date"] = pd.to_datetime(data_4temp1["t_date"])
cc = data_4temp1.head()
print(cc)

# ## 将对账户余额进行清洗

data_4temp1["balance2"] = data_4temp1["balance"].map(
    lambda x: int("".join(x[1:].split(",")))
)
data_4temp1["amount2"] = data_4temp1["amount"].map(
    lambda x: int("".join(x[1:].split(",")))
)

cc = data_4temp1.head()
print(cc)

# ## 根据取数窗口提取交易数据

import datetime

data_4temp2 = data_4temp1[data_4temp1.date > data_4temp1.t_date][
    data_4temp1.date < data_4temp1.t_date + datetime.timedelta(days=365)
]

cc = data_4temp2.head()
print(cc)

# ### 1.5.1账户平均余额、余额的标准差、变异系数

data_4temp3 = data_4temp2.groupby("account_id")["balance2"].agg(
    [("avg_balance", "mean"), ("stdev_balance", "std")]
)
data_4temp3["cv_balance"] = data_4temp3[["avg_balance", "stdev_balance"]].apply(
    lambda x: x[1] / x[0], axis=1
)

cc = data_4temp3.head()
print(cc)

# ### 1.5.2 平均支出和平均收入的比例

type_dict = {"借": "out", "贷": "income"}
data_4temp2["type1"] = data_4temp2.type.map(type_dict)
data_4temp4 = data_4temp2.groupby(["account_id", "type1"])[["amount2"]].sum()
cc = data_4temp4.head()
print(cc)

data_4temp5 = pd.pivot_table(
    data_4temp4, values="amount2", index="account_id", columns="type1"
)
data_4temp5.fillna(0, inplace=True)
data_4temp5["r_out_in"] = data_4temp5[["out", "income"]].apply(
    lambda x: x[0] / x[1], axis=1
)
cc = data_4temp5.head()
print(cc)

data4 = pd.merge(data3, data_4temp3, left_on="account_id", right_index=True, how="left")
data4 = pd.merge(data4, data_4temp5, left_on="account_id", right_index=True, how="left")

cc = data4.head()
print(cc)

# ## 1.6、计算贷存比，贷收比

data4["r_lb"] = data4[["amount", "avg_balance"]].apply(lambda x: x[0] / x[1], axis=1)
data4["r_lincome"] = data4[["amount", "income"]].apply(lambda x: x[0] / x[1], axis=1)

cc = data4.head()
print(cc)

# 建立分析模型：
# 样本随机抽样，建立训练集与测试集：

# 构建Logistic模型
# data4.columns
# 提取状态为C的用于预测。其它样本随机抽样，建立训练集与测试集

data_model = data4[data4.status != "C"]
for_predict = data4[data4.status == "C"]

train = data_model.sample(frac=0.7, random_state=1235).copy()
test = data_model[~data_model.index.isin(train.index)].copy()
print(" 训练集样本量: %i \n 测试集样本量: %i" % (len(train), len(test)))
print("训练集样本量：%i\n测试集样本量：%i" % (len(train), len(test)))

# 训练集样本量：195
# 测试集样本量：84

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

'''
"""
个人贷款违约预测模型

本数据为一家银行的个人金融业务数据集，可以作为银行场景下进行个人客户业务分析和数据挖掘的示例。这份数据中涉及到5300个银行客户的100万笔交易，而且涉及700份贷款信息与近900张信用卡的数据。通过分析这份数据可以获取与银行服务相关的业务知识。例如，提供增值服务的银行客户经理，希望明确哪些客户有更多的业务需求，而风险管理的业务人员可以及早发现贷款的潜在损失。
确认问题：可否根据客户贷款前的属性、状态信息和交易行为预测其贷款违约行为？
"""

"""
第一部分：分析数据
贷款表：loans
账户表：accounts
客户信息表：clients
权限分配表：Disp（描述了客户和账户之间的关系以及客户操作账户的权限）
支付命令表：Orders（每条记录描述了一个支付命令）
交易表：Trans
信用卡：Cards
人口地区统计表：Dinstrict
建立数据的实体-关系图，一般数据库都会有，也可以自己根据表的关系建立一个。
"""

"""
第二部分：业务理解
目的：预测贷款违约的可能性
分析：什么指标具有预测能力？

属性：性别、年龄……
状态：资产总量、居住地失业率……
行为：支出太大……
客户为什么会不还钱？——违约收益大于违约成本
违约收益是固定的，即所贷款项，违约成本是动态的，因此主要指标为：违约成本
得到的收益高于成本，会导致还款意愿不足——【贷前审批】
经济条件恶化，导致还款能力不足——【贷后监控】
导致还款能力不足的原因有多种：欲望大于能力、生活状态不稳定……

思路整理
有预测价值的变量基本都是衍生变量：
一级衍生：资产余额；
二级衍生：资产余额波动率、平均资产余额；
三级衍生，资产余额的变异系数；（波动/均值）
开始数据提取：
相关与因果之间的关系。
注意构建模型时数据选取的标准。
建立因果关系模型：
将分析的变量按照时间变化情况可以分为动态变量和静态变量；
属性变量一般是静态变量，行为、状态和利益变量均属于动态变量。
动态变量还分为时点变量和区间变量，状态变量和利益变量均属于时点变量，行为变量为区间变量。

"""

#第三部分：数据提取

print("讀取一個資料夾內的所有csv檔, 用區域變數存起來")
foldername = "D:/_git/vcs/_big_files/Bankcredit"
os.chdir(foldername)

loanfile = os.listdir()
createVar = locals()
for i in loanfile:
        if i.endswith("csv"):
                createVar[i.split('.')[0]] = pd.read_csv(i,encoding = 'gbk')
                print(i.split('.')[0])
#确认预测值y

bad_good = {'B':1,'D':1,'A':0,'C':2}
loans['bad_good'] = loans.status.map(bad_good)
cc = loans.head()

print(cc)


#确认x

data2 = pd.merge(loans,disp,on = 'account_id',how = 'left')
data2 = pd.merge(data2,clients,on = 'client_id',how = 'left')
data2.head() #借款人的年龄、性别等


data3 = pd.merge(data2,district,left_on = 'district_id',right_on ='A1',how = 'left')
data3.head() #借款人居住地的经济状况

data_4temp1 = pd.merge(loans[['account_id','date']],trans[['account_id','type','amount','balance','date']],on = 'account_id')
data_4temp1.columns = ['account_id','date','type','amount','balance','t_date']
data_4temp1 = data_4temp1.sort_values(by =['account_id','t_date'])

data_4temp1['date'] = pd.to_datetime(data_4temp1['date'])
data_4temp1['t_date'] = pd.to_datetime(data_4temp1['t_date'])
data_4temp1.head() #借款人一年内的账户平均余额、余额的标准差、变异系数、平均收入和平均支出的比例

data_4temp1['balance2'] = data_4temp1['balance'].map(lambda x:int('',join(x[1:].split(','))))
data_4temp1['amount2'] = data_4temp1['amount'].map(lambda x:int('',join(x(x[1:].split(','))))
data_4temp1.head() #对账户余额进行清洗

#根据取数窗口提取交易数据

import datetime
data_4temp2 = data_4temp1[data_4temp1.date > data_4temp1.t_date][data_4temp1.date < data_4temp1.t_date + datetime.timedelta(days = 365)]
data_4temp2.tail() #取贷款时间前一年的交易数据

data_4temp3 = data_4temp2.groupby('account_id')['balance2'].agg([('avg_balance','mean'),('stdev_balance','std')])
data_4temp3['cv_balance'] = data_4temp3[['avg_balance','stdev_balance']].apply(lambda x:x[1]/x[0],axis =1)
data_4temp3.head() #计算账户平均余额、余额的标准差、变异系数

type_dict = {'借':'out','贷':'income'}
data_4temp2['type1'] = data_4temp2.type.map(type_dict)
data_4temp4 = data_4temp2.groupby(['account_id','type1'])[['amount2']].sum()
data_4temp4.head()  #计算平均支出和平均收入的比例
#转置
data_4temp5 = pd.pivot_table(
        data_4temp4,values = 'amount2',
        index = 'account_id',columns = 'type1')
data_4temp5.fillna(0,inplace = True)
data_4temp5['r_out_in'] = data_4temp5[['out','income']].apply(lambda x:x[0]/x[1],axis =1)
data_4temp5.head()

#
data4 = pd.merge(data3,data_4temp3,left_on = 'account_id',right_index = True,how = 'left')
data4 = pd.merge(data4,data_4temp5,left_on = 'account_id',right_index = True,how = 'left')
data4.head()

data4['r_lb'] = data4[['amount','avg_balance']].apply(lambda x:x[0]/x[1],axis = 1)
data4['r_lincome'] data4[['amount','income']].apply(lambda x:x[0]/x[1],axis =1)
data4.head() #计算贷存比（贷款金额/平均账户余额），贷收比（贷款金额/收入金额）
#data4就是用于建模的数据
data4.columns
第四部分 选择模型
选择预测模型，排序类
使用逻辑回归算法
评估指标：ROC曲线、K-S曲线

建立模型

data_model = data4[data4.status!='C']
for_predict = data4[data4.status == 'C']
train = data_model.sample(frac=0.7,random_state=1235).copy()
test = data_model[~data_model.index.isin(train.index)].copy()
print('训练集样本量：%i \n 测试集样本量：%i'%

由于python没有实现变量筛选功能，需要手动编写向前逐步算法
向前逐步算法
以aic作为筛选模型的标准
此处使用statsmodels，当然用sklearn也是可以。

def forward_select(data,response):
        import statsmodels.api as sm
        import statsmodels.formula.api as smf
        remaining = set(data.columns)
        remaining.remove(response)
        selected =[]
        current_score,best_new_score = float('inf'),float('inf')
        while remaining:
                aic_with_candidates = []
                for candidate indef forward_select(data, response):
    import statsmodels.api as sm
    import statsmodels.formula.api as smf
    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score = float('inf'), float('inf')
    while remaining:
        aic_with_candidates=[]
        for candidate in remaining:
            formula = "{} ~ {}".format(
                response,' + '.join(selected + [candidate]))
            aic = smf.glm(
                formula=formula, data=data, 
                family=sm.families.Binomial(sm.families.links.logit)
            ).fit().aic
            aic_with_candidates.append((aic, candidate))
        aic_with_candidates.sort(reverse=True)
        best_new_score, best_candidate=aic_with_candidates.pop()
        if current_score > best_new_score: 
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
            print ('aic is {},continuing!'.format(current_score))
        else:        
            print ('forward selection over!')
            break
            
    formula = "{} ~ {} ".format(response,' + '.join(selected))
    print('final formula is {}'.format(formula))
    model = smf.glm(
        formula=formula, data=data, 
        family=sm.families.Binomial(sm.families.links.logit)
    ).fit()
    return(model)

candidates = ['bad_good', 'A1', 'GDP', 'A4', 'A10', 'A11', 'A12','amount', 'duration',
       'A13', 'A14', 'A15', 'a16', 'avg_balance', 'stdev_balance',
       'cv_balance', 'income', 'out', 'r_out_in', 'r_lb', 'r_lincome']
data_for_select = train[candidates]

lg_m1 = forward_select(data=data_for_select, response='bad_good')
lg_m1.summary().tables[1]

第五部分：评估模型

验证ROC指数

import sklearn.metrics as metrics
import matplotlib.pyplot as plt
fpr, tpr, th = metrics.roc_curve(test.bad_good, lg_m1.predict(test))
plt.figure(figsize=[6, 6])
plt.plot(fpr, tpr, 'b--')
plt.title('ROC curve')
plt.show()
计算AUC值

print('AUC = %.4f' %metrics.auc(fpr, tpr))
结果


训练集样本量: 195 
测试集样本量: 84
aic is 167.4331143250464,continuing!
aic is 135.8243585604184,continuing!
forward selection over!
final formula is bad_good ~ r_lb + cv_balance 
AUC = 0.8846
结果可以看到r_lb及cv_balance 两个因素是影响最大的，采用这两个因素评估出的模型AUC可以达到0.88，证明这个模型的能力还是很强的，也许加入更多的因素后效果会更好。

第六部分 输出预测结果
预测并输出到xls文件

print(for_predict.head())
test_predict = lg_m1.predict(for_predict)
for_predict['prob'] = test_predict
print(for_predict[['account_id','prob']].head())

df5 = for_predict
df5.to_excel(r'test.xls',sheet_name='1')
预测的样本数据输出到 test.xls 文件，最后一列就是每条记录的违约预测值。


'''

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個
