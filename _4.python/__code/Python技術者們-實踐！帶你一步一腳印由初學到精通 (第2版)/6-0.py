import requests

datestr = "20210201"

# 下載股價
r = requests.get(
    'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALLBUT0999')

print(r.text)




#檔案 : C:\_git\vcs\_4.python\__code\Python技術者們-實踐！帶你一步一腳印由初學到精通 (第2版)\ch06\6-0.py

import requests

datestr = "20210201"

# 下載股價
r = requests.get(
    'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date=' + datestr + '&type=ALLBUT0999')

print(r.text)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python技術者們-實踐！帶你一步一腳印由初學到精通 (第2版)\ch06\6-1.py

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

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python技術者們-實踐！帶你一步一腳印由初學到精通 (第2版)\ch06\6-2.py

import datetime

date = '20210311'
date = datetime.datetime.strptime(date, '%Y%m%d')
print(date.weekday())

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python技術者們-實踐！帶你一步一腳印由初學到精通 (第2版)\ch06\6-3.py

import datetime

start_date_str = "20210125"
end_date_str = "20210201"

start_date = datetime.datetime.strptime(start_date_str, '%Y%m%d')
end_date = datetime.datetime.strptime(end_date_str, '%Y%m%d')

totaldays = (end_date - start_date).days + 1
dates = []
for daynumber in range(totaldays):
    date = (start_date + datetime.timedelta(days=daynumber))
    if date.weekday() < 6:
        dates.append(date.strftime('%Y%m%d'))
print(dates)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python技術者們-實踐！帶你一步一腳印由初學到精通 (第2版)\ch06\6-4.py

def get_setting():    #←將「讀取設定檔」寫成函式, 可讓程式易讀易用
	res = []     #←準備一個空串列來存放讀取及解析的結果
	try:              # 使用 try 來預防開檔或讀檔錯誤
		with open('stock.txt') as f:  # 用 with 以讀取模式開啟檔案
			slist = f.readlines()     # 以行為單位讀取所有資料
			print('讀入：', slist)    # 輸出讀到的資料以供確認
			a, b, c = slist[0].split(',')   #←將股票字串以逗號切割為串列
			res = [a, b, c]
	except:
		print('stock.txt 讀取錯誤')
	return res   #←傳回解析的結果, 但如果開檔或讀檔錯誤則會傳回 []

stock = get_setting()     # 呼叫上面的函式
print('傳回：', stock)    # 輸出傳回的結果

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python技術者們-實踐！帶你一步一腳印由初學到精通 (第2版)\ch06\6-5.py

import matplotlib.pyplot as plt
import crawler_module as m
from time import sleep
import pandas as pd

all_list = []
stock_symbol, dates = m.get_data()

for date in dates:
    sleep(5)
    try:
        crawler_data = m.crawl_data(date, stock_symbol)
        all_list.append(crawler_data[0])
        df_columns = crawler_data[1]
        print("  OK!  date = " + date + " ,stock symbol = " + stock_symbol)
    except:
        print("error! date = " + date + " ,stock symbol = " + stock_symbol)

all_df = pd.DataFrame(all_list, columns=df_columns)
print(all_df)

# step 1 prepare data
day = all_df["日期"].astype(str)
close = all_df["收盤價"].astype(float)

# step 2 create plot
plt.figure(figsize=(20, 10), dpi=100)

# step 3 plot
plt.plot(day, close, 's-', color='r', label="Close Price")
plt.title("TSMC Line chart")
plt.xticks(fontsize=10, rotation=45)
plt.yticks(fontsize=10)
plt.legend(loc="best", fontsize=20)


plt.show()

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python技術者們-實踐！帶你一步一腳印由初學到精通 (第2版)\ch06\6-6.py

import matplotlib.pyplot as plt
import crawler_module as m
from time import sleep
import pandas as pd

all_list = []
stock_symbol, dates = m.get_data()

for date in dates:
    sleep(5)
    try:
        crawler_data = m.crawl_data(date, stock_symbol)
        all_list.append(crawler_data[0])
        df_columns = crawler_data[1]
        print("  OK!  date = " + date + " ,stock symbol = " + stock_symbol)
    except:
        print("error! date = " + date + " ,stock symbol = " + stock_symbol)

all_df = pd.DataFrame(all_list, columns=df_columns)

# step 1 prepare data
day = all_df["日期"].astype(str)
openprice = all_df["開盤價"].astype(float)
close = all_df["收盤價"].astype(float)

# step 2 create plot
fig, (ax, ax2) = plt.subplots(2, 1, sharex=True, figsize=(24, 15), dpi=100)
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
ax.set_title(stock_symbol+"  開盤價、收盤價 ( " +
             dates[0] + " ~ " + dates[-1] + " )")

# step 3 plot 子圖(ax)
ax.plot(day, openprice, 's-', color='r', label="Open Price")
ax.legend(loc="best", fontsize=10)

# step 3 plot 子圖(ax2)
ax2.plot(day, close, 'o-', color='b', label="Close Price")
ax2.legend(loc="best", fontsize=10)
ax2.set_xticks(range(0, len(day), 5))
ax2.set_xticklabels(day[::5])

# step 4 show plot
plt.show()

print('------------------------------------------------------------')	#60個

