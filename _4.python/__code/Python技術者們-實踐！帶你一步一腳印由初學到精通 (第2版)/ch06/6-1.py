import requests
from io import StringIO
import pandas as pd

datestr = "20210201"
stock_symbol = "2330"

# 下載股價
r = requests.get(
    'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALLBUT0999')

r_text = r.text.split('\n')

r_text = [i for i in r_text if len(
    i.split('",')) == 17 and i[0] != '=']

data = "\n".join(r_text)
df = pd.read_csv(StringIO(data), header=0)

df = df.drop(columns=['Unnamed: 16'])
filter_df = df[df["證券代號"] == stock_symbol]
print(filter_df)
