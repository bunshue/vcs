# Python 測試 twstock 1

import twstock
import matplotlib.pyplot as plt
import time

# 以鴻海的股票代號建立 Stock 物件
stock = twstock.Stock('2317')
print('最新資料')
print(stock.price)
print('日期：',stock.date[-1])
print('開盤價：',stock.open[-1])
print('最高價：',stock.high[-1])
print('最低價：',stock.low[-1])
print('收盤價：',stock.price[-1])

# 以鴻海的股票代號建立 Stock 物件
stock = twstock.Stock('2317')
# 取得 2019 年 12 月的資料
stocklist = stock.fetch(2019,12)
for s in stocklist:
    print(s.date.strftime('%Y-%m-%d'), end='\t')
    print(s.open, end='\t')
    print(s.high, end='\t')
    print(s.low, end='\t')
    print(s.close)


# 鴻海股票即時交易資訊
real = twstock.realtime.get('2317') 
if real['success']:  #如果讀取成功
    print('即時股票資料：',real['info']['name'])     
    print('開盤價：',real['realtime']['open'], end=', ')
    print('最高價：',real['realtime']['high'], end=', ')  
    print('最低價：',real['realtime']['low'], end=', ')
    print('目前股價：',real['realtime']['latest_trade_price'])   
else:
    print('錯誤：' + real['rtmessage'])


# 以鴻海的股票代號建立 Stock 物件
stock = twstock.Stock('2317')  
# 取得 2019 年 12 月的資料
stocklist = stock.fetch(2019,12)   
listx = []
listy = []
for s in stocklist:
    listx.append(s.date.strftime('%Y-%m-%d'))
    listy.append(s.close)

plt.figure(figsize=[10,5])	#圖像大小[英吋]
plt.title('鴻海2019年12月股價',fontsize=18)
plt.xlabel("日期",fontsize=14)
plt.ylabel("股價",fontsize=14)
plt.plot(listx, listy, 'r:s')

plt.xticks(rotation=45)
plt.grid('k:', alpha=0.5)
plt.ylim(88,93)
plt.yticks([88,89,90,91,92,93])

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

plt.show() 


companys = ['2330','2912','3293']
plt.figure(figsize=[10,5])	#圖像大小[英吋]
for company in companys:
    stock = twstock.Stock(company)  
    # 取得 2019 年 12 月的資料
    stocklist = stock.fetch(2019,12)   
    listx = []
    listy = []
    for s in stocklist:
        listx.append(s.date.strftime('%Y-%m-%d'))
        listy.append(s.close)
    
    plt.plot(listx, listy)
    plt.xticks(rotation=45)
plt.show()



#plt.figure(figsize=[12,30])	#圖像大小[英吋]
stock = twstock.Stock('2317') 
slist = []
for i in range(1,13):
    stocklist = stock.fetch(2019,i)
    [slist.append(s) for s in stocklist]
#    listx = [s.date.strftime('%d') for s in stocklist]
#    listy = [s.close for s in stocklist]
#    plt.subplot('62{}'.format(i))
#    plt.xticks(rotation=45)
#    plt.title(label="{}月".format(i))

#    plt.plot(listx, listy)
    print(len(slist))
    time.sleep(5)
    if i == 6:
        time.sleep(20)
    
#plt.show()

#lista = []
#list1 = [1,2,3,4,5]
#list2 = [7,8,9,10,11]
#list1.append(list2)
#list1
#%%


#將資料寫出到csv檔        
import csv

#比較看看
#filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/stock_data_2019_2330.csv'

with open('2019_2330.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(slist)

