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

