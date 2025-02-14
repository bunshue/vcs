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
print("------------------------------------------------------------")  # 60個

# Association

#第十三讲关联规则介绍

from apriori import *

#数据载入

#原数据为倒排表数据

inverted=pd.read_csv('Prod.csv',encoding='gbk')
inverted.head()

#数据转换

#倒排表数据转换为相应的二维列表数据

idataset=dataconvert(inverted,tidvar='ID',itemvar='PROD',data_type = 'inverted')
idataset[:5]

"""
关联规则

参数说明:

    minSupport:最小支持度阈值
    minConf:最小置信度阈值
    minlen:规则最小长度
    maxlen:规则最大长度

这里，minSupport或minConf设定越低，产生的规则越多，计算量也就越大

设定参数为:minSupport=0.05,minConf=0.5,minlen=1,maxlen=10
"""

res = arules(idataset,minSupport=0.05,minConf=0.5,minlen=1,maxlen=10)


#产生关联规则
#规定提升度要大于1,并按照置信度进行排序

res.loc[res.lift>1,:].sort_values('support',ascending=False).head(20)

#关联规则结果汇总

res.plot.scatter(3,4,c=5,figsize=(4,4))
plt.xlabel('support')
plt.ylabel('confidence')
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

