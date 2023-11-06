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

