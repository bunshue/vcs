"""
Google搜尋趨勢（Google Trends），舊稱Google搜尋解析（Google Insights for Search）

該索引顯示了與不同語言和地區在Google的搜尋查詢的頻率。

"""

import sys
import time
import random

import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

import pandas as pd
from pytrends.request import TrendReq
'''
pytrend = TrendReq()

pytrend.build_payload(kw_list=['taiwan'])

related_queries = pytrend.related_queries()
keywords = related_queries.values()

print(keywords)

print('------------------------------------------------------------')	#60個

import pandas as pd                        
from pytrends.request import TrendReq

pytrend = TrendReq()
keywords = pytrend.suggestions(keyword='Mercedes Benz')
df = pd.DataFrame(keywords)
df.drop(columns= 'mid')   # This column makes no sense
print(df)

print('------------------------------------------------------------')	#60個

import pandas as pd                        
from pytrends.request import TrendReq

def get_google_keywords(keyword):
    pytrend = TrendReq()
    keywords = pytrend.suggestions(keyword=keyword)
    df = pd.DataFrame(keywords)
    if len(df)>0:
        df1 = df.title
        return df1
    else:
        return None
'''
print('------------------------------------------------------------')	#60個

import pandas as pd
from pytrends.request import TrendReq
pytrend = TrendReq()
     

pytrend.build_payload(kw_list=['Taylor Swift'])
# Interest by Region
df = pytrend.interest_by_region()
cc = df.head(10)

print(cc)
     



df.reset_index().plot(x='geoName', y='Taylor Swift', figsize=(120, 10), kind ='bar')
     


plt.show()


print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


