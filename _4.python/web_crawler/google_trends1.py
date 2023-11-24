"""
Google搜尋趨勢（Google Trends），舊稱Google搜尋解析（Google Insights for Search）

該索引顯示了與不同語言和地區在Google的搜尋查詢的頻率。

"""

import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq(hl = 'en-US', tz = 360)
keywords = ['Python', 'R']
pytrend.build_payload(
    kw_list = keywords,
    cat = 0,
    timeframe = 'today 3-m',
    geo = 'TW',
    gprop = '')

data = pytrend.interest_over_time()
data= data.drop(labels = ['isPartial'], axis = 'columns')
image = data.plot(title = 'Python V.S. R in last 3 months on Google Trends ')
fig = image.get_figure()

fig.savefig('figure.png')
data.to_csv('Py_VS_R.csv', encoding='utf_8_sig')

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個



from pytrends.request import TrendReq

pytrend = TrendReq(hl="zh-TW", tz=-480)
keywords = ["Python", "Java", "C++"]
pytrend.build_payload(
     kw_list=keywords,
     cat=0,
     timeframe="2020-07-01 2020-07-31",
     geo="TW",
     gprop="")

print(pytrend.interest_over_time())

print('------------------------------------------------------------')	#60個

from pytrends.request import TrendReq

pytrend = TrendReq()
df = pytrend.trending_searches(pn='taiwan')
print(df.head(10))

print('------------------------------------------------------------')	#60個

from pytrends.request import TrendReq

pytrend = TrendReq()
df = pytrend.top_charts(2019, hl="zh-tw", tz=-480, geo="TW")
print(df)

print('------------------------------------------------------------')	#60個

import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq()
dic = pytrend.suggestions(keyword="python")
print(pd.DataFrame(dic).drop("mid", axis=1))

print('------------------------------------------------------------')	#60個

from pytrends.request import TrendReq

pytrend = TrendReq(hl="zh-TW", tz=-480)
pytrend.build_payload(kw_list=["Python"])

df = pytrend.interest_by_region()
print(df.sort_values(["Python"], ascending=False).head(10))

print('------------------------------------------------------------')	#60個

from pytrends.request import TrendReq

pytrend = TrendReq(hl="zh-TW", tz=-480)
pytrend.build_payload(kw_list=["Python"])

dic = pytrend.related_queries()
print(dic["Python"]["top"].head(10))
print(dic["Python"]["rising"].head(10))

print('------------------------------------------------------------')	#60個

from pytrends.request import TrendReq

pytrend = TrendReq(hl="zh-TW", tz=-480)
pytrend.build_payload(kw_list=["Python"])

dic = pytrend.related_topics()
df = dic["Python"]["rising"]
df = df.drop(["link","topic_mid"], axis=1)
print(df.head(10))

print('------------------------------------------------------------')	#60個

from pytrends.request import TrendReq

pytrend = TrendReq(hl="zh-TW", tz=-480)
pytrend.build_payload(
     kw_list=["Python", "R"],
     timeframe="today 3-m",
     geo="TW")

df = pytrend.interest_over_time()
df = df.drop(["isPartial"], axis=1)
df.plot(kind="line", title="Python vs R")


print('------------------------------------------------------------')	#60個

from pytrends.request import TrendReq

pytrend = TrendReq(hl="zh-TW", tz=-480)
pytrend.build_payload(kw_list=["Python"])

df = pytrend.interest_by_region()
df = df.sort_values(["Python"], ascending=False).head(10)
df.plot(kind="bar")

print('------------------------------------------------------------')	#60個

import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq(hl="en-US", tz=360)
pytrend.build_payload(
     kw_list=["Coronavirus"],
     timeframe="2020-02-01 2020-03-31",
     geo="US-NY")

df = pytrend.interest_over_time()
df = df.drop(["isPartial"], axis=1)
df["timestamp"] = pd.to_datetime(df.index)
print(df.head())
df.plot(kind="line", x="timestamp", y="Coronavirus", 
        title="Searches for Coronavirus in NY")

print('------------------------------------------------------------')	#60個

import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq(hl="en-US", tz=360)

def get_trends(keywords, state): 
    pytrend.build_payload(
         kw_list=keywords,
         timeframe="2020-02-01 2020-03-31",
         geo=state)
    df = pytrend.interest_over_time()
    df = df.drop(["isPartial"], axis=1)
    df.columns = [state]
    return df

df = get_trends(["Coronavirus"], "US-NY")
df2 = get_trends(["Coronavirus"], "US-CA")
 
df3 = pd.concat([df, df2], axis=1)
print(df3.head())

df3["timestamp"] = pd.to_datetime(df.index)
print(df3.head())
df3.plot(kind="line", x="timestamp", y=["US-NY","US-CA"], 
        title="Searches for Coronavirus in NY/CA")

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


