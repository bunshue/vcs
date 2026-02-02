# ch12_8.py
import matplotlib.pyplot as plt
from pylab import mpl
import twstock

mpl.rcParams["font.sans-serif"] = ["SimHei"]        # 使用黑體

stock2330 = twstock.Stock("2330")
plt.title(u"台積電", fontsize=24)
plt.plot(stock2330.price)
plt.show()

