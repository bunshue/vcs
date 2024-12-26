"""
CH02網路爬蟲資料收集

!pip install scraparazzie


"""

import sys

print("------------------------------------------------------------")  # 60個

"""

print('爬取 google news')
from scraparazzie import scraparazzie

client = scraparazzie.NewsClient(language='chinese traditional', location='Taiwan', topic='Business', max_results=8)
client.print_news()

print(client.languages)

print(client.locations)

print(client.topics)

client = scraparazzie.NewsClient(language = 'chinese traditional', location = 'Taiwan', query = '口罩', max_results = 10)
items = client.export_news()
print(len(items))
for i, item in enumerate(items):
  print('第 ' + str(i+1) + ' 則新聞：')
  print('新聞標題：' + item['title'])
  print('新聞機構：' + item['source'])
  print('新聞連結：' + item['link'])
  print('新聞時間：' + item['publish_date'])
  print('========================================================================================')

print(client.get_config())

print('------------------------------------------------------------')	#60個

print('Newspaper3k：擷取全世界新聞')

# !pip install newspaper3k

import newspaper
print(newspaper.popular_urls())

newspaper.languages()

paper = newspaper.build('http://www.ltn.com.tw/', language='zh')
print('新聞連結：')
for i, article in enumerate(paper.articles):
    print(i+1, article.url)


from newspaper import Article
url = 'https://news.ltn.com.tw/news/life/breakingnews/3649202'
article = Article(url)
article.download()
print(article.html)


article.parse()
print('新聞標題：')
print(article.title)
print('新聞內容：')
print(article.text)
print('新聞日期：')
print(article.publish_date)


from newspaper import fulltext
url = 'https://www.cnbc.com/2020/10/27/trump-biden-foreign-policy-iran-china.html'
article = Article(url)
article.download()
print(fulltext(article.html))

"""
print("------------------------------------------------------------")  # 60個

"""
# fail
print('technews_tw：擷取台灣科技新聞')

# !pip install technews-tw

from technews import TechNews

news = TechNews("business").get_today_news()

# news = TechNews("orange").get_today_news()
# news = TechNews("ithome").get_today_news()
# news = TechNews("inside").get_today_news()
print(news)

news3 = TechNews("business").get_news_by_page(3)
# news3 = TechNews("orange").get_news_by_page(3)
# news3 = TechNews("ithome").get_news_by_page(3)
# news3 = TechNews("inside").get_news_by_page(3)
print(news3)

from datetime import datetime
now = datetime.now()
strTime = now.strftime("%Y-%m-%d %H:%M:%S")
date1 = strTime[:10]  #目前日期
content = news3['news_contents']
for key in content:
  mononews = content[key]
  print('新聞標題：', mononews['title'])
  print('新聞連結：', mononews['link'])
  if 'ago' in mononews['date']: mononews['date'] = date1
  print('發布日期：', mononews['date'])
  print('========================================================================')
"""

print("------------------------------------------------------------")  # 60個

print("HistoricalWeatherTW：取得氣象測站資料")


#!pip install carson-tool.HistoricalWeatherTW

#!wget https://raw.githubusercontent.com/CarsonSlovoka/HistoricalWeatherTW/master/Carson/Tool/HistoricalWeatherTW/config/CSV/station.csv

import pandas as pd

df = pd.read_csv("station.csv")
df1 = df[1:6]
df1.to_csv("station5.csv", index=False)
print(df1)

from Carson.Tool.HistoricalWeatherTW import collect_weather_tw, QueryFormat
from pathlib import Path
import datetime

STATION_CSV = "station5.csv"
OUTPUT_PATH = Path("result5.csv")
BEGIN_DATE = datetime.date(2020, 10, 1)
END_DATE = datetime.date(2020, 10, 2)
QUERY_FORMAT = QueryFormat.DAY
CONVERT2NUM = True

""" #fail
collect_weather_tw(STATION_CSV, OUTPUT_PATH, BEGIN_DATE, END_DATE, QUERY_FORMAT, CONVERT2NUM)

import pandas as pd
df = pd.read_csv('result5.csv')
print(df)
      

"""


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
