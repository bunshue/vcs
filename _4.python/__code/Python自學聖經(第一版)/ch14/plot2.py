import pandas as pd
import matplotlib.pyplot as plt
# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" #也可設mingliu或DFKai-SB
plt.rcParams["axes.unicode_minus"] = False 

df = pd.DataFrame([[250,320,300,312,280],
                   [280,300,280,290,310],
                   [220,280,250,305,250]],
                   index=['北部','中部','南部'],
                   columns=[2015,2016,2017,2018,2019])
g1 = df.iloc[0].plot(kind='line', legend=True, xticks=range(2015,2020), title='公司分區年度銷售表', figsize=[10,5])
g1 = df.iloc[1].plot(kind='line', legend=True, xticks=range(2015,2020))
g1 = df.iloc[2].plot(kind='line', legend=True, xticks=range(2015,2020))