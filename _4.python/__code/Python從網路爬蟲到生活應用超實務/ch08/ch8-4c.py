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
