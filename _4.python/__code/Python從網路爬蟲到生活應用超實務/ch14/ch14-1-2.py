import requests
import pandas as pd
import time
from fake_useragent import UserAgent

dates = [20200601, 20200701, 20200801]
stockNo = 2330
url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date={}&stockNo={}"
ua = UserAgent()

for date in dates :
    print(date, stockNo)
    headers = {"User-Agent": ua.random}
    r = requests.get(url.format(date, stockNo), headers=headers)
    csvfile = "{}_{}.csv".format(stockNo, date)    

    data = pd.read_html(r.text)[0]
    data.columns = data.columns.droplevel(0)
    data.to_csv(csvfile, index=False)
    time.sleep(5)
