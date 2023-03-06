import matplotlib.pyplot as plt
import twstock
companys = ['2330','2912','3293']
plt.figure(figsize=[10,5])
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