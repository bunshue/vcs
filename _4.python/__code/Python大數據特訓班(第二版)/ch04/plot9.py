import matplotlib.pyplot as plt
year = [2016,2017,2018,2019,2020]
city1 = [100,180,90,220,150]
plt.plot(year, city1, 'r-.s', lw=2, ms=10, label="台北")
city2 = [160,50,120,140,110]
plt.plot(year, city2, 'g--*', lw=2, ms=10, label="高雄")
plt.legend()
plt.ylim(0, 250)
plt.xticks(year)
plt.title("銷售報表", fontsize=18)
plt.xlabel("年度", fontsize=12)
plt.ylabel("百萬", fontsize=12)
plt.grid(color='k', ls=':', lw=1, alpha=0.5)
# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" #也可設mingliu或DFKai-SB
plt.rcParams["axes.unicode_minus"] = False
plt.show()