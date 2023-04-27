# Python 測試 twse 2

#4.5 台灣證券交易所API
#這個API長得大概像這樣:
#http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20160501&stockNo=2330
#比較重要的地方是date這個參數, 基本上你給的值一定要是yyyyMMdd的形式, 但是真正作用的只有yyyy與MM, 因為他會把這段request解讀成你想要看stockNo股票在yyyy年MM月的紀錄, 所以dd基本上沒有太大意義, 但卻是不可少的部分.
import requests
import time

TWSE_URL = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json'

def get_web_content(search_stock, current_date):
    resp = requests.get(TWSE_URL + '&date=' + current_date + '&stockNo=' + search_stock)
    if resp.status_code != 200:
        return None
    else:
        return resp.json()

def get_data(search_stock, current_date):
    info = list()
    resp = get_web_content(search_stock, current_date)
    if resp is None:
        return None
    else:
        if resp['data']:
            for data in resp['data']:
                record = {
                    '日期': data[0],
                    '開盤價': data[3],
                    '收盤價': data[6],
                    '成交筆數': data[8]
                }
                info.append(record)
        return info

def get_stock_data_twse(search_stock):
    current_date = time.strftime('%Y%m%d')
    current_year = time.strftime('%Y')
    current_month = time.strftime('%m')
    print('Processing data for %s %s...' % (current_year, current_month))
    get_data(search_stock, current_date)
    collected_info = get_data(search_stock, current_date)
    for info in collected_info:
        print(info)

search_stock = '2330'
get_stock_data_twse(search_stock)


