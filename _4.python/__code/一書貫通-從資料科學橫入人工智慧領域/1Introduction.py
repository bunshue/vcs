# # 第5章3 RFM

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

# ### 1. 导入数据

trad_flow = pd.read_csv(r'data/RFM_TRAD_FLOW.csv', encoding='gbk')
cc = trad_flow.head(10)

print(cc)

sys.exit()

# ### 2.通过 RFM方法 建立 模型

# In[6]:
#2.1 通过计算F反应客户对打折产品的偏好
F=trad_flow.groupby(['cumid','type'])[['transID']].count()
F.head()
# In[9]:
F_trans=pd.pivot_table(F,index='cumid',columns='type',values='transID')
F_trans.head()
# In[9]:
F_trans['Special_offer']= F_trans['Special_offer'].fillna(0)
F_trans.head()
# In[9]:
F_trans["interest"]=F_trans['Special_offer']/(F_trans['Special_offer']+F_trans['Normal'])
F_trans.head()
# In[9]:
#2.2 通过计算M反应客户的价值信息
M=trad_flow.groupby(['cumid','type'])[['amount']].sum()
M.head()

# In[7]:
M_trans=pd.pivot_table(M,index='cumid',columns='type',values='amount')
M_trans['Special_offer']= M_trans['Special_offer'].fillna(0)
M_trans['returned_goods']= M_trans['returned_goods'].fillna(0)
M_trans["value"]=M_trans['Normal']+M_trans['Special_offer']+M_trans['returned_goods']
M_trans.head()

##########
#2.3 通过计算R反应客户是否为沉默客户
# In[8] 定义一个从文本转化为时间的函数
from datetime import datetime

def to_time(t):
    out_t=time.mktime(time.strptime(t, '%d%b%y:%H:%M:%S'))   ########此处修改为时间戳方便后面qcut函数分箱
    return out_t
a="14JUN09:17:58:34"
print(to_time(a))
# In[8]
trad_flow["time_new"]= trad_flow.time.apply(to_time)
trad_flow.head()
# In[7]:
R=trad_flow.groupby(['cumid'])[['time_new']].max()
R.head()


# ### 3.构建模型，筛选目标客户
# In[12]
from sklearn import preprocessing

threshold = pd.qcut(F_trans['interest'], 2, retbins=True)[1][1]
binarizer = preprocessing.Binarizer(threshold=threshold)
interest_q = pd.DataFrame(binarizer.transform(F_trans['interest'].values.reshape(-1, 1)))
interest_q.index=F_trans.index
interest_q.columns=["interest"]
# In[12]
threshold = pd.qcut(M_trans['value'], 2, retbins=True)[1][1]
binarizer = preprocessing.Binarizer(threshold=threshold)
value_q = pd.DataFrame(binarizer.transform(M_trans['value'].values.reshape(-1, 1)))
value_q.index=M_trans.index
value_q.columns=["value"]
# In[12]
threshold = pd.qcut(R["time_new"], 2, retbins=True)[1][1]
binarizer = preprocessing.Binarizer(threshold=threshold)
time_new_q = pd.DataFrame(binarizer.transform(R["time_new"].values.reshape(-1, 1)))
time_new_q.index=R.index
time_new_q.columns=["time"]
# In[12]
analysis=pd.concat([interest_q, value_q,time_new_q], axis=1)
# In[12]
#analysis['rank']=analysis.interest_q+analysis.interest_q
analysis = analysis[['interest','value','time']]
analysis.head()

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
analysis['label'] = analysis[['interest','value','time']].apply(lambda x: label[(x[0],x[1],x[2])], axis = 1)
analysis.head()
# In[12]



