# ch20_17.py
import matplotlib.pyplot as plt

xpt = list(range(1,101))        # 建立1-100序列x座標點
ypt = [x**2 for x in xpt]       # 以x平方方式建立y座標點
plt.axis([0, 100, 0, 10000])    # 留意參數是串列
plt.scatter(xpt, ypt, c=(0, 1, 0))  # 綠色
plt.show()



