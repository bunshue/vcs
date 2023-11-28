"""
Google搜尋趨勢（Google Trends），舊稱Google搜尋解析（Google Insights for Search）

該索引顯示了與不同語言和地區在Google的搜尋查詢的頻率。

build_payload 完整參數

pytrend.build_payload(
     kw_list = keywords,       關鍵字串列
     cat = 0,                  類別碼 0是所有類別  人文與社會是14
     timeframe = 'today 1-m',  時間範圍
     geo = 'TW',               2個字元的國碼 美國是US 英國是GB 紐約是US_NY
    gprop = ''                 搜尋結果的過濾類型 例如: image news youtube
    )



timeframe

'today 3-m',  #從今天至前3個月
'now 7-d',    #從現在至前7天
'now 1-H',    #從現在至前1小時


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

from pytrends.request import TrendReq
from pprint import pprint

pytrend = TrendReq(hl = 'en-US', tz = 360)

keywords = ['Python', 'Java', 'C++']
pytrend.build_payload(
     kw_list = keywords,
     cat = 0,
     timeframe = 'today 1-m',
     geo = 'TW',
    gprop = ''
    )

cc = pytrend.interest_over_time()   #探索
pprint(cc)

print('------------------------------------------------------------')	#60個

import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq(hl = 'en-US', tz = 360)

keywords = ['Python', 'Java', 'C++']
pytrend.build_payload(
    kw_list = keywords,
    cat = 0,
    timeframe = 'today 3-m',    #從今天至前3個月
    geo = 'TW',
    gprop = ''
    )

data = pytrend.interest_over_time()
data = data.drop(labels = ['isPartial'], axis = 'columns')
image = data.plot(title = 'Python V.S. R in last 3 months on Google Trends ')
fig = image.get_figure()

fig.savefig('figure.png')
data.to_csv('Py_VS_R.csv', encoding = 'utf_8_sig')

print('------------------------------------------------------------')	#60個

from pytrends.request import TrendReq

pytrend = TrendReq(hl = "zh-TW", tz = -480)

keywords = ['Python', 'Java', 'C++']
pytrend.build_payload(
     kw_list = keywords,
     cat = 0,
     timeframe = "2020-07-01 2020-07-31",
     geo = "TW",
    gprop = ''
    )

print(pytrend.interest_over_time())

print('------------------------------------------------------------')	#60個

from pytrends.request import TrendReq

pytrend = TrendReq()

#trending_searches 查詢每日搜尋趨勢項目的熱搜資料
#pn參數是國家或地區 taiwan/japan/united_states
df = pytrend.trending_searches(pn = 'taiwan')
print(df.head(10))


print('------------------------------------------------------------')	#60個

from pytrends.request import TrendReq

pytrend = TrendReq()
#top_charts 年度排行榜的網路趨勢資料
df = pytrend.top_charts(2022, hl = "zh-tw", tz = -480, geo = "TW")
print(df)

print('------------------------------------------------------------')	#60個

import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq()

#suggestions 爬取查詢建議的關鍵字清單
dic = pytrend.suggestions(keyword = "python")
print(pd.DataFrame(dic).drop("mid", axis = 1))  #刪除mid欄位

sys.exit()

print('------------------------------------------------------------')	#60個

#interest_by_region 爬取關鍵字的熱搜區域

from pytrends.request import TrendReq

pytrend = TrendReq(hl = "zh-TW", tz = -480)

keywords = ['Python', 'Java', 'C++']
pytrend.build_payload(
    kw_list = ["Python"]
    )


df = pytrend.interest_by_region()
print(df.sort_values(["Python"], ascending = False).head(10))

print('------------------------------------------------------------')	#60個

#related_queries 爬取關鍵字的關聯查詢
from pytrends.request import TrendReq

pytrend = TrendReq(hl = "zh-TW", tz = -480)

keywords = ['Python', 'Java', 'C++']
pytrend.build_payload(
    kw_list = ["Python"]
    )

dic = pytrend.related_queries()
print(dic["Python"]["top"].head(10))
print(dic["Python"]["rising"].head(10))

print('------------------------------------------------------------')	#60個

#related_topics 爬取關鍵字的關聯主題

from pytrends.request import TrendReq

pytrend = TrendReq(hl = "zh-TW", tz = -480)

keywords = ['Python', 'Java', 'C++']
pytrend.build_payload(
    kw_list = ["Python"]
    )

dic = pytrend.related_topics()
df = dic["Python"]["rising"]    #取上升值
df = df.drop(["link", "topic_mid"], axis = 1) #刪除link和top_mid兩個欄位
print(df.head(10))  #取前10名

print('------------------------------------------------------------')	#60個

from pytrends.request import TrendReq

pytrend = TrendReq(hl = "zh-TW", tz = -480)

keywords = ['Python', 'Java', 'C++']
pytrend.build_payload(
     kw_list = ["Python", "R"],
     timeframe = "today 3-m",
    geo = "TW"
    )

df = pytrend.interest_over_time()
df = df.drop(["isPartial"], axis = 1)   #刪除isPartial欄位
df.plot(kind = "line", title = "Python vs R")#df畫折線圖

plt.show()

print('------------------------------------------------------------')	#60個

#取得Python關鍵字熱搜地區的資料

from pytrends.request import TrendReq

pytrend = TrendReq(hl = "zh-TW", tz = -480)

keywords = ['Python', 'Java', 'C++']
pytrend.build_payload(
    kw_list = ["Python"]
    )

df = pytrend.interest_by_region()
df = df.sort_values(["Python"], ascending = False).head(10)
df.plot(kind = "bar")   #df畫bar圖

plt.show()

print('------------------------------------------------------------')	#60個

#美國紐約州 2020-02-01 ~ 2020-03-31之間搜尋Coronavirus關鍵字的網路趨勢
import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq(hl = "en-US", tz = 360)

keywords = ["Coronavirus"]
pytrend.build_payload(
    kw_list = keywords,
    timeframe = "2020-02-01 2020-03-31",
    geo = "US-NY"
    )

df = pytrend.interest_over_time()
df = df.drop(["isPartial"], axis = 1)   #刪除isPartial欄位
df["timestamp"] = pd.to_datetime(df.index)#新增timestamp日期資料
print(df.head())
df.plot(kind = "line", x = "timestamp", y = "Coronavirus", title = "Searches for Coronavirus in NY")    #df畫折線圖

plt.show()

print('------------------------------------------------------------')	#60個

import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq(hl = "en-US", tz = 360)

#get_trends 取得美國各州搜尋關鍵字的網路趨勢資料
def get_trends(keywords, state): 
    pytrend.build_payload(
         kw_list = keywords,
         timeframe = "2020-02-01 2020-03-31",
        geo = state
        )
    df = pytrend.interest_over_time()
    df = df.drop(["isPartial"], axis = 1)
    df.columns = [state]
    return df

keywords = ['Python', 'Java', 'C++']

df = get_trends(["Coronavirus"], "US-NY")
df2 = get_trends(["Coronavirus"], "US-CA")
 
df3 = pd.concat([df, df2], axis = 1)    #concat合併欄位
print(df3.head())

df3["timestamp"] = pd.to_datetime(df.index)
print(df3.head())
df3.plot(kind = "line", x = "timestamp", y = ["US-NY","US-CA"],
         title = "Searches for Coronavirus in NY/CA")   #df畫折線圖

plt.show()


sys.exit()


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


