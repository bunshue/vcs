"""

公開資訊觀測站
https://mops.twse.com.tw/mops/web/index

"""


import pandas as pd
import requests
from fake_useragent import UserAgent
from io import StringIO
import time

def get_monthly_report(s_type, year, month, delay=5):    
    if year > 1990:
        year -= 1911  
    URL = "https://mops.twse.com.tw/nas/t21/{}/" 
    stock_type = ["sii", "otc", "rotc"]
    URL = URL.format(stock_type[s_type])    
    url = URL + "t21sc03_{0}_{1}.html".format(str(year),str(month))
    ua = UserAgent()
    user_agent = ua.random
    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers=headers)
    r.encoding = "big5"
    dfs = pd.read_html(StringIO(r.text), encoding="big5")
    items = []    
    for item in dfs:
        if item.shape[1] <= 11 and item.shape[1] >= 10:
            items.append(item)
    df = pd.concat(items)
    if "levels" in dir(df.columns):
        df.columns = df.columns.get_level_values(1)
    df["當月營收"] = pd.to_numeric(df["當月營收"], "coerce")
    df = df[~df["當月營收"].isnull()]
    df = df[df["公司代號"] != "合計"]    
    time.sleep(delay)

    return df
    
df = get_monthly_report(0, 109, 1)
print(df.shape)
print(df.head())



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

