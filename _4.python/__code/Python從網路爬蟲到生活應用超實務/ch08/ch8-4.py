from pytrends.request import TrendReq

pytrend = TrendReq(hl="zh-TW", tz=-480)
pytrend.build_payload(
     kw_list=["Python", "R"],
     timeframe="today 3-m",
     geo="TW")

df = pytrend.interest_over_time()
df = df.drop(["isPartial"], axis=1)
df.plot(kind="line", title="Python vs R")

