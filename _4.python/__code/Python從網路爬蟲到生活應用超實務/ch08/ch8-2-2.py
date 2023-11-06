import re
import json
import requests
import pandas as pd

date = "20200813"
URL = "https://trends.google.com.tw/trends/api/dailytrends?hl=zh-TW&tz=-480&ed={}&geo=TW&ns=15"
url = URL.format(date)
r = requests.get(url)
json_str = re.sub("\)\]\}\',\n", "", r.text)
data = json.loads(json_str)
results = data["default"]["trendingSearchesDays"][0]["trendingSearches"]
items = []
for item in results:
    items.append(item["title"])
df = pd.DataFrame(items)

print(df.head())

