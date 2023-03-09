import matplotlib.pyplot as plt

#在同一張圖 畫 兩條曲線

year = [2015,2016,2017,2018,2019]

city1 = [128,150,199,180,150]
plt.plot(year, city1, 'r-.s', lw=2, ms=10, label="台北")

city2 = [120,145,180,170,120]
plt.plot(year, city2, 'g--*', lw=2, ms=10, label="台中")

plt.legend()
plt.ylim(50, 250)
plt.xticks(year)
plt.title("銷售報表", fontsize=18)
plt.xlabel("年度", fontsize=12)
plt.ylabel("百萬", fontsize=12)

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

plt.show()  #將圖表呈現出來
