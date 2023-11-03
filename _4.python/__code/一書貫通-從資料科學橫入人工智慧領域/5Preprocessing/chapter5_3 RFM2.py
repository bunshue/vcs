
# coding: utf-8

# # 第5章3 RFM
# - pandas学习参考： [十分钟搞定pandas](http://www.cnblogs.com/chaosimple/p/4153083.html)

# ### 1. 导入数据
import os 
os.chdir(r"D:\Python_book\5Preprocessing")
# In[1]:

import pandas as pd
import numpy as np
trad_flow = pd.read_csv('RFM_TRAD_FLOW.csv', encoding='gbk')
trad_flow.head()


# ### 2.计算 RFM

# In[2]:

import time

# 先将非标准字符串时间格式化为时间数组，再转换为时间戳便于计算
trad_flow['time'] = trad_flow['time'].map(lambda x: time.mktime(time.strptime(x, '%d%b%y:%H:%M:%S')))

# 查找每个购物ID每个销售类型下的最近时间
R=trad_flow.groupby(['cumid','type'])[['time']].max()

# 转化为透视表
R_trans=pd.pivot_table(R,index='cumid',columns='type',values='time')

# 用最久远的购物时间替换缺失值
R_trans[['Special_offer','returned_goods']] = R_trans[['Special_offer','returned_goods']].apply(lambda x: x.replace(np.nan, min(x)), 
                                                                                                axis = 0)
R_trans['R_max'] = R_trans[['Normal','Presented','Special_offer']].apply(lambda x: max(x), axis =1)

R_trans.head()


# In[3]:

# 对购物频率按照购物ID和购物类型进行汇总统计
F=trad_flow.groupby(['cumid','type'])[['transID']].count()

# 转化为透视表
F_trans=pd.pivot_table(F,index='cumid',columns='type',values='transID')

# 用0填补缺失值
F_trans[['Special_offer','returned_goods']] = F_trans[['Special_offer','returned_goods']].fillna(0)

# 将退货的频数转化为负数
F_trans['returned_goods'] = F_trans['returned_goods'].map(lambda x: -x)

# 求每个购物ID的购物总次数
F_trans["F_total"] = F_trans.apply(lambda x: sum(x), axis = 1)

F_trans.head()


# In[4]:

# 对购物金额按照购物ID和购物类型进行汇总统计
M=trad_flow.groupby(['cumid','type'])[['amount']].sum()

# 转化为透视表
M_trans=pd.pivot_table(M,index='cumid',columns='type',values='amount')

# 用0填补缺失值
M_trans[['Special_offer','returned_goods']] = M_trans[['Special_offer','returned_goods']].fillna(0)

# 求每个购物ID的购物总金额
M_trans["M_total"] = M_trans.apply(lambda x: sum(x), axis = 1)

M_trans.head()


# In[5]:

# 合并表
RFM = pd.concat([R_trans['R_max'],F_trans['F_total'],M_trans['M_total']], axis = 1)
# RFM三个维度等宽分箱打分
RFM['R_score'] = pd.cut(RFM.R_max,3,labels = [1,2,3], precision = 2)
RFM['F_score'] = pd.cut(RFM.F_total,3,labels = [1,2,3], precision = 2)
RFM['M_score'] = pd.cut(RFM.M_total,3,labels = [1,2,3], precision = 2)

# RFM各三类，总共有27种组合，为方便营销简化分类为8种
def score_label(a,b,c):
    '''
    a: 'R_score'
    b: 'F_score'
    c: 'M_score'
    '''
    if a == 3 and b == 3 and c == 3:
        return '重要价值客户'
    elif a == 3 and (b in [1,2]) and c == 3:
        return '重要发展客户'
    elif (a in [1,2]) and b == 3 and c == 3:
        return '重要保持客户'
    elif (a in [1,2]) and (b in [1,2]) and c == 3:
        return '重要挽留客户'
    elif a == 3 and b == 3 and (c in [1,2]):
        return '一般价值客户'
    elif a == 3 and (b in [1,2]) and (c in [1,2]):
        return '一般发展客户'
    elif (a in [1,2]) and b == 3 and (c in [1,2]):
        return '一般保持客户'
    elif (a in [1,2]) and (b in [1,2]) and (c in [1,2]):
        return '一般挽留客户'    
# 为每个购物ID贴标签
RFM['Label'] = RFM[['R_score', 'F_score', 'M_score']].apply(lambda x: score_label(x[0],x[1],x[2]), axis = 1)

RFM.head()


# - '重要价值客户'：消费额度高，购物频率高，最近购物时间也较近——该类客户是重要且忠实的大客户，要细心维护。
# 
# 
# - '重要发展客户'：消费额度高，购物频率不高，最近购物时间较近——该类客户只是购物频率不高，有巨大的挖掘潜力，可根据该客户以往购物信息，进行个性                                                              化推荐，并发放购物优惠券刺激消费，增加客户粘性。
# 
# 
# - '重要保持客户'：消费额度高，购物频率高，但最近购物时间较远——该类客户最近一次购物时间较久远，可能是快要流失的重要客户，可以让客户沟通了解其                                                              是不是哪项环节不够人性化体验不好，导致购物频率过低。
# 
# 
# - '重要挽留客户'：消费额度高，购物频率不高，最近购物时间也较远——该类客户可能是已经流失的重要客户，如果还能联系上，可跟进了解其流失原因，对有                                                              相似客户特征的群体进行预警，针对性改进。
# 
# 
# - '一般价值客户'：消费额度不高，购物频率高，最近购物时间也较近——该类客户对我们的产品感兴趣，很活跃，但购物金额过低，可能是价格敏感性客户，可                                                              对其组合金融产品增加其购买力。
# 
# 
# - '一般发展客户'：消费额度不高，购物频率不高，最近购物时间较近——该类客户可能是我们的新晋客户，对我们的服务和产品进行试探性体验，可多留意此类                                                              客户，进行邮件短信关怀及时发送优惠信息。
# 
# 
# - '一般保持客户'：消费额度不高，购物频率高，最近购物时间较远——该类客户可能是快要流失的一般客户，可进行一般性低成本营销。
# 
# 
# - '一般挽留客户'：消费额度不高，购物频率不高，最近购物时间也较远——该类客户不是我们的目标客户，经费有限可忽略此类客户。



# In[ ]:




