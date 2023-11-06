from pytrends.request import TrendReq

pytrend = TrendReq()
df = pytrend.top_charts(2019, hl="zh-tw", tz=-480, geo="TW")
print(df)