# python import module : matplotlib plot 畫折線圖 twstock 抓取股票資訊做分析

#導入模組
import matplotlib.pyplot as plt
import twstock

#股票代碼 stock_code

stock_code = str(2330)
stock = twstock.Stock(stock_code) # 建立 Stock 物件

#使用語法：（查詢某年某月的股票資料）
#stock.fetch(year, month)

stocklist1 = stock.fetch(2023, 1)    #查詢 2023年1月的資料
stocklist2 = stock.fetch(2023, 2)    #查詢 2023年2月的資料

stocklist = stocklist1+stocklist2;


#建立 x, y 軸串列，x 軸為日期時間(date)，y 軸為收盤價(close)
#印出 stock.data[0]，可以觀察到「close」就是收盤價的價位資料

print(stock.data[0])


listx = []
listy = []
for value in stocklist:
    listx.append(value.date.strftime('%Y-%m-%d'))
    listy.append(value.close)

plt.figure(num = '股票分析', figsize=(10,10)) # 設定圖表區寬高

plt.xlabel('日期', fontsize="16") # 設定 x 軸標題內容及大小
plt.ylabel('股價', fontsize="16") # 設定 y 軸標題標題內容及大小
plt.title('台積電(2330)', fontsize="18") # 設定圖表標題內容及大小

plt.plot(listx, listy, color='red', markersize="16", marker=".") # 紅色，實線，標記大小 16，標記為「點」

plt.xticks(rotation = 45) # 讓 x 坐標軸標題旋轉 45 度, 使得文字不會重疊

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

plt.show()  #將圖表呈現出來


