# ch12_9.py
import matplotlib.pyplot as plt
from pylab import mpl
import twstock

mpl.rcParams["font.sans-serif"] = ["SimHei"]        # 使用黑體

stock2330 = twstock.Stock("2330")
stock2330.fetch_from(2018,1)
plt.title(u"台積電", fontsize=24)
plt.xlabel(u"2018年1月以來的交易天數", fontsize=14)
plt.ylabel(u"價格", fontsize=14)
plt.plot(stock2330.price)
plt.show()

