# ch20_16.py
import matplotlib.pyplot as plt

xpt = list(range(1,101))        # 建立1-100序列x座標點
ypt = [x**2 for x in xpt]       # 以x平方方式建立y座標點
plt.scatter(xpt, ypt, color='y')
plt.show()



