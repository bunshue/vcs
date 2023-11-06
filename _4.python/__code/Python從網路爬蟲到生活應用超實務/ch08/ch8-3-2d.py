from pytrends.request import TrendReq

pytrend = TrendReq(hl="zh-TW", tz=-480)
pytrend.build_payload(kw_list=["Python"])

dic = pytrend.related_queries()
print(dic["Python"]["top"].head(10))
print(dic["Python"]["rising"].head(10))
