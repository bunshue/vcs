import requests
import pandas as pd

def get_price(url):
    data = requests.get(url)   #GET請求
    data_prices = data.json()['stats']   #解析json格式，並取出'status'對應到的值
    df = pd.DataFrame(data_prices)   #將list轉為dataframe
    df.columns = ['datetime', 'twd']   #設定欄索引名稱
    df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')   #將毫秒轉為時間日期格式
    df.index = df['datetime']   #設定列索引
    return df

def strategy(df, total, ma_num, stop_earn):
    df['ma'] = df['twd'].rolling(window = ma_num).mean()
    df=df[ma_num-1:]
    entry_price=0
    max_price=0
    min_price=0
    state='wait_long'
    for i in range(len(df)):
        if state=='wait_long':
            if df['twd'][i]>df['ma'][i]:
                #print(df['datetime'][i], "  entry_long  ", df['twd'][i])
                max_price=df['twd'][i]
                entry_price = df['twd'][i]
                state='entry_long'
        elif state=='wait_short':
            if df['twd'][i]<df['ma'][i]:
                #print(df['datetime'][i], "  entry_short  ", df['twd'][i])
                min_price=df['twd'][i]
                entry_price = df['twd'][i]
                state='entry_short'
        elif state=='entry_long':
            if df['twd'][i]>max_price:
                max_price=df['twd'][i]
                #print("up  ",max_price)
            if df['twd'][i]<max_price:
                #print(df['datetime'][i], "  out  ", df['twd'][i])
                total+=df['twd'][i]-entry_price
                state='wait_short'
            elif df['twd'][i]-entry_price > stop_earn and stop_earn !=0:
                #print(df['datetime'][i], "  out  ", df['twd'][i])
                total+=df['twd'][i]-entry_price
                state='wait_short'
        elif state=='entry_short':
            if df['twd'][i]<min_price:
                min_price=df['twd'][i]
                #print("down  ",min_price)
            if df['twd'][i]>min_price:
                #print(df['datetime'][i], "  out  ", df['twd'][i])
                total+=entry_price-df['twd'][i]
                state='wait_long'
            elif entry_price-df['twd'][i] > stop_earn and stop_earn !=0:
                #print(df['datetime'][i], "  out  ", df['twd'][i])
                total+=entry_price-df['twd'][i]
                state='wait_long'
    return total