import matplotlib.pyplot as plt
import twstock
# 以鴻海的股票代號建立 Stock 物件
stock = twstock.Stock('2317')  
# 取得 2019 年 12 月的資料
stocklist = stock.fetch(2019,12)   
listx = []
listy = []
for s in stocklist:
    listx.append(s.date.strftime('%Y-%m-%d'))
    listy.append(s.close)

plt.figure(figsize=[10,5])
plt.title('鴻海2019年12月股價',fontsize=18)
plt.xlabel("日期",fontsize=14)
plt.ylabel("股價",fontsize=14)
plt.plot(listx, listy, 'r:s')
plt.xticks(rotation=45)
plt.grid('k:', alpha=0.5)
plt.ylim(88,93)
plt.yticks([88,89,90,91,92,93])
plt.rcParams["font.sans-serif"] = "mingliu" 
plt.rcParams["axes.unicode_minus"] = False

plt.show() 