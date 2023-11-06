import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq()
dic = pytrend.suggestions(keyword="python")
print(pd.DataFrame(dic).drop("mid", axis=1))