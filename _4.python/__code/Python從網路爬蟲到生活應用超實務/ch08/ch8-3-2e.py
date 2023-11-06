from pytrends.request import TrendReq

pytrend = TrendReq(hl="zh-TW", tz=-480)
pytrend.build_payload(kw_list=["Python"])

dic = pytrend.related_topics()
df = dic["Python"]["rising"]
df = df.drop(["link","topic_mid"], axis=1)
print(df.head(10))
