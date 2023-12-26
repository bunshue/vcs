# ex20_10.py
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"]        # 使用黑體

country = [u"美國",u"澳洲",u"日本",u"歐洲",u"英國"]
pou = [10543, 2105, 1190, 3346, 980]
          
plt.pie(pou,labels=country,explode=(0,0,0.2,0,0),
        autopct="%1.2f%%")                          # 繪製圓餅圖
plt.show()

