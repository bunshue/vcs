# ex20_12.py
import matplotlib.pyplot as plt
from pylab import mpl
import twstock

mpl.rcParams["font.sans-serif"] = ["SimHei"]        # 使用黑體
seq = list(range(0, 31))

stock2892 = twstock.Stock("2892")
stock5880 = twstock.Stock("5880")
stock2886 = twstock.Stock("2886")

line2892, = plt.plot(seq, stock2892.price, '-*', label='第一金')
line5880, = plt.plot(seq, stock5880.price, '-o', label='合庫金')
line2886, = plt.plot(seq, stock2886.price, '-^', label='兆豐金')

plt.legend(handles=[line2892, line5880, line2886], loc='best')
plt.title(u"金融三雄", fontsize=24)
plt.xlabel("近31個交易日", fontsize=14)
plt.ylabel("價格", fontsize=14)
plt.show()

