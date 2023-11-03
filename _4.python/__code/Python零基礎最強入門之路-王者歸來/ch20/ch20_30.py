# ch20_30.py
import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"]        # 使用黑體
mpl.rcParams["axes.unicode_minus"] = False          # 讓可以顯示負號

sorts = [u"交通",u"娛樂",u"教育",u"交通",u"餐費"]
fee = [8000,2000,3000,5000,6000]
          
plt.pie(fee,labels=sorts,explode=(0,0.2,0,0,0),
        autopct="%1.2f%%")      # 繪製圓餅圖
plt.show()

