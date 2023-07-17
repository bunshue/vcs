import requests,json

# 官網 https://trends.google.com/trends/trendingsearches/daily?geo=TW
# Google熱搜關鍵字，預設會取得最近兩天的關鍵字
url = 'https://trends.google.com/trends/api/dailytrends'

# 以 payload 設定 params，ed 可以設定日期 
payload = {
            "hl": "zh-TW",
            "tz": "-480",
            # 如果要指定日期可以加上 ed 參數
            # "ed": "20200401",
            "geo": "TW",
            "ns": "15",
          }
html = requests.get(url,params=payload)
html.encoding='utf-8'

_,datas=html.text.split(',',1)
jsondata=json.loads(datas) #將下載資料轉換為字典
trendingSearchesDays=jsondata['default']['trendingSearchesDays']

for trendingSearchesDay in trendingSearchesDays:
    news=""
    formattedDate=trendingSearchesDay['formattedDate']
    news += '日期:' + formattedDate + '\n\n'
    
    for data in trendingSearchesDay['trendingSearches']:
        news += '【主題關鍵字:' + data['title']['query'] + '】' + '\n\n'
        for content in data['articles']:
            news += '標題:' + content['title'] + '\n'
            news += '媒體:' + content['source'] + '\n'
            news += '發佈時間:' + content['timeAgo'] + '\n'
            news += '內容:' + content['snippet'] + '\n'
            news += '相關連結:' + content['url'] + '\n\n'            
 
    filename= trendingSearchesDay['date'] + '.txt'    
    with open(filename,'w',encoding='utf-8') as f:
        f.write(news)
    print(filename + " 已存檔!") 