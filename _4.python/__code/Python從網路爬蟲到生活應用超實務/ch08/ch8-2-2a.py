import re
import json
import requests
import pandas as pd
import datetime
from fake_useragent import UserAgent

URL = "https://trends.google.com.tw/trends/api/dailytrends?hl=zh-TW&tz=-480&ed={}&geo=TW&ns=15"

ua = UserAgent()
enddate = datetime.datetime.today()
startdate = enddate - datetime.timedelta(days=29)
all_items = []
start = datetime.datetime.strftime(startdate,'%Y%m%d')
end = datetime.datetime.strftime(enddate,'%Y%m%d')
for i in pd.date_range(start=start, end=end, freq='1D'):
    url = URL.format(datetime.datetime.strftime(i, '%Y%m%d'))
    print(url)
    headers = {'user-agent' : ua.random}
    r = requests.get(url, headers=headers)
    json_str = re.sub("\)\]\}\',\n", "", r.text)
    data = json.loads(json_str)
    results = data["default"]["trendingSearchesDays"][0]["trendingSearches"]
    items = []
    rank = 1
    for item in results:
        dic = item["title"]
        dic["rank"] = rank        
        items.append(dic)
        rank = rank + 1
    df = pd.DataFrame(items)
    df['date'] = datetime.datetime.strftime(i, '%Y-%m-%d')
    print(df.head())
    all_items.append(df)
   
df = pd.concat(all_items, ignore_index=True)
df.to_csv("trends.csv",index=False)