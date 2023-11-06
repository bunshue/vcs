from pytrends.request import TrendReq

pytrend = TrendReq()
df = pytrend.trending_searches(pn='taiwan')
print(df.head(10))