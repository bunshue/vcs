from pytrends.request import TrendReq

pytrend = TrendReq(hl="zh-TW", tz=-480)
pytrend.build_payload(kw_list=["Python"])

df = pytrend.interest_by_region()
df = df.sort_values(["Python"], ascending=False).head(10)
df.plot(kind="bar")