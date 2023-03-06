# python import module : matplotlib plot 畫折線圖 twstock 抓取股票資訊做分析

#導入模組
import matplotlib.pyplot as plt
import twstock
import datetime

# 詢問使用者股票代碼
#stock_code = input("請輸入將要查詢的股票代碼:")

stock_code = str(2330)
stock = twstock.Stock(stock_code) # 建立 Stock 物件

#取得查詢當年年份及上個月月份

now_date = datetime.datetime.now() # 取得查詢當下的時間
now_year = now_date.year # 取得查詢當下當年年份

# 取得查詢當下上個月月份
if(now_date.month != 1):
    last_month = now_date.month - 1
else:
    last_month = 12

'''
取得「查詢年/查詢時間前一個月」的股票資料
使用語法：（查詢某年某月的股票資料）
stock.fetch(year, month)
此次需求的「查詢年/查詢時間前一個月」的股票資料：
'''

stocklist = stock.fetch(now_year, last_month)

#建立 x, y 軸串列，x 軸為日期時間(date)，y 軸為收盤價(close)
#印出 stock.data[0]，可以觀察到「close」就是收盤價的價位資料

print(stock.data[0])


listx = []
listy = []
for value in stocklist:
    listx.append(value.date.strftime('%Y-%m-%d'))
    listy.append(value.close)

plt.figure(figsize=(10,10)) # 設定圖表區寬高

plt.xlabel('日期', fontsize="16") # 設定 x 軸標題內容及大小
plt.ylabel('股價', fontsize="16") # 設定 y 軸標題標題內容及大小
plt.title('Taiwan Stock', fontsize="18") # 設定圖表標題內容及大小

plt.plot(listx, listy, color='red', markersize="16", marker=".") # 紅色，實線，標記大小 16，標記為「點」

plt.xticks(rotation = 45) # 讓 x 坐標軸標題旋轉 45 度, 使得文字不會重疊

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

#將圖表呈現出來

plt.show()








