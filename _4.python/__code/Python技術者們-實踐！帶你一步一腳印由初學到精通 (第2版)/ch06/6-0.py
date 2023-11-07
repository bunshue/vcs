import requests

datestr = "20210201"

# 下載股價
r = requests.get(
    'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALLBUT0999')

print(r.text)
