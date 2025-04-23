"""
ch04

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

# 数据获取

DataAPI.MktEqudGet(tradeDate=u"20150513",secID=["000001.XSHE","600000.XSHG"],
                   ticker=u"",field=u"secID,secShortName,tradeDate,closePrice,marketValue",pandas="1")
     
DataAPI.MktEqudGet(tradeDate=u"",secID=u"",ticker=["000001","600000"],
                   beginDate='20180117',endDate='20180121',
                   field=u"secID,secShortName,tradeDate,closePrice,marketValue",pandas="1")
     
DataAPI.MktStockFactorsOneDayGet(tradeDate=u"20150227",secID=["000001.XSHE","600000.XSHG"],ticker=u"",
                                 field=u"secID,tradeDate,PS,PB,NetProfitGrowRate",pandas="1")
     
df = pd.DataFrame()
for ticker in ["600000",'000001']:
    tmp_df = DataAPI.MktStockFactorsDateRangeGet(secID=u"",ticker=ticker,beginDate=u"20170612",endDate=u"20170616",
                                    field=u"secID,tradeDate,PS,PB,NetProfitGrowRate",pandas="1")
    df = pd.concat([df,tmp_df],axis=0)
cc = df.reset_index(drop=True)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 数据整理

# 合并 追加

df_quotation = DataAPI.MktEqudAdjGet(tradeDate=u"",secID=u"600000.XSHG",ticker=u"",beginDate=u"20180101",endDate=u"20180121",
                                     isOpen="",field=u"secID,tradeDate,closePrice",pandas="1")
df_factor = DataAPI.MktStockFactorsDateRangeGet(secID=u"600000.XSHG",ticker=u"",beginDate=u"20180101",endDate=u"20180121",
                                                field=u"secID,tradeDate,MA10,MA5",pandas="1")
df_quotation = df_quotation.merge(df_factor,on=['tradeDate'])
     

df_quotation[(df_quotation.closePrice > df_quotation.MA10) & (df_quotation.closePrice> df_quotation.MA5)]
     
# 数据透视

df_quotation = DataAPI.MktEqudAdjGet(tradeDate=u"",secID=["600000.XSHG",'000001.XSHE'],ticker=u"",beginDate=u"20180118",endDate=u"20180121",
                                     isOpen="",field=u"secID,tradeDate,marketValue",pandas="1")
print(df_quotation)
     
df_quotation = df_quotation.pivot_table(index='tradeDate',columns='secID',values='marketValue')
print(df_quotation)
     
cc = df_quotation.sum(axis=1)
print(cc)

print("数据过滤")

df = DataAPI.MktStockFactorsOneDayGet(tradeDate=u"20180119",secID=set_universe('A'),ticker=u"",               field=u"secID,tradeDate,PE",pandas="1")
cc = df[df.PE>0].head(10)
print(cc)
     
print("数据探索与数据清洗")

df = DataAPI.MktStockFactorsOneDayGet(tradeDate=u"20180119",secID=set_universe("A"),ticker=u"",
                                      field=u"secID,tradeDate,ROE",pandas="1")
df.plot.hist(bins=100)
show()

_ = df.boxplot(sym='rs')
show()

df_ = df.copy()
     

df_.loc[df.ROE-df.ROE.mean()<-3*df.ROE.std(),'ROE'] = df.ROE.mean()-3*df.ROE.std()
df_.loc[df.ROE-df.ROE.mean()>3*df.ROE.std(),'ROE'] = df.ROE.mean()+3*df.ROE.std()
     

df_.plot.hist(bins=100)
show()

# 数据转化

((df_['ROE'] - df_['ROE'].min()) / (df_['ROE'].max() - df_['ROE'].min())).plot.hist(bins=100)
     

show()


((df_['ROE'] - df_['ROE'].mean()) / df_['ROE'].std()).plot.hist(bins=100)
     

show()

# 哑变量

df_industry = DataAPI.EquIndustryGet(industryVersionCD=u"010303",industry=u"",
                                     secID=df_['secID'].tolist(),ticker=u"",intoDate=u"20180101",field=u"secID,industryName1",pandas="1")
industry_list = df_industry['industryName1'].drop_duplicates().tolist()
     

def get(x):
    ind_s = pd.Series([0]*len(industry_list),index = industry_list)
    if len(df_industry[df_industry['secID']==x]) > 0:
        ind = df_industry[df_industry['secID']==x]['industryName1'].values[0]
        ind_s.loc[ind] = 1
    # print ind_s
    return ind_s
     

df_[industry_list] = df_['secID'].apply(lambda x: get(x))
     

cc = df_.head()
print(cc)
     
cc = len(df_['secID'])
print(cc)


_ = df.boxplot(sym='rs')
     

df.ROE.describe()
     

df_ = df.copy()
     

df_3sigma = df[((df.ROE-df.ROE.mean()).abs()>3*df.ROE.std())]
     

df_[(df.ROE-df.ROE.mean()>3*df.ROE.std())]['ROE'] = df.ROE.mean()+3*df.ROE.std()
     

df_[(df.ROE-df.ROE.mean()<-3*df.ROE.std())]['ROE'] = df.ROE.mean()-3*df.ROE.std()
     

df_.hist(bins=100)
show()

cc = df_[(df.ROE-df.ROE.mean()<-3*df.ROE.std())]['ROE']
print(cc)

df_.loc[df.ROE-df.ROE.mean()<-3*df.ROE.std()]['ROE'] = df.ROE.mean()-3*df.ROE.std()
     

df_.loc[df.ROE-df.ROE.mean()<-3*df.ROE.std(),'ROE'] = df.ROE.mean()-3*df.ROE.std()
     

cc = df_.loc[df.ROE-df.ROE.mean()<-3*df.ROE.std(),'ROE']
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


