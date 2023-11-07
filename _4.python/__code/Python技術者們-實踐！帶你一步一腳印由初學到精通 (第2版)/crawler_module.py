import requests
from io import StringIO
import pandas as pd
import datetime


def get_setting():  # ←將「讀取設定檔」寫成函式, 可讓程式易讀易用
    res = []  # ←準備一個空串列來存放讀取及解析的結果
    try:              # 使用 try 來預防開檔或讀檔錯誤
        with open('stock.txt') as f:  # 用 with 以讀取模式開啟檔案
            slist = f.readlines()     # 以行為單位讀取所有資料
            print('讀入：', slist)    # 輸出讀到的資料以供確認
            a, b, c = slist[0].split(',')  # ←將股票字串以逗號切割為串列
            res = [a, b, c]
    except:
        print('stock.txt 讀取錯誤')
    return res  # ←傳回解析的結果, 但如果開檔或讀檔錯誤則會傳回 []


def get_data():
    data = get_setting()
    dates = []
    start_date = datetime.datetime.strptime(data[1], '%Y%m%d')
    end_date = datetime.datetime.strptime(data[2], '%Y%m%d')
    for daynumber in range((end_date - start_date).days + 1):
        date = (start_date + datetime.timedelta(days=daynumber))
        if date.weekday() < 6:
            dates.append(date.strftime('%Y%m%d'))
    return data[0], dates


def crawl_data(date, symbol):
    # 下載股價
    r = requests.get(
        'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + date + '&type=ALL')

    r_text = [i for i in r.text.split('\n') if len(
        i.split('",')) == 17 and i[0] != '=']
    df = pd.read_csv(StringIO("\n".join(r_text)), header=0)

    df = df.drop(columns=['Unnamed: 16'])
    filter_df = df[df["證券代號"] == symbol]
    filter_df.insert(0, "日期", date)
    df_columns = filter_df.columns
    return list(filter_df.iloc[0]), filter_df.columns
