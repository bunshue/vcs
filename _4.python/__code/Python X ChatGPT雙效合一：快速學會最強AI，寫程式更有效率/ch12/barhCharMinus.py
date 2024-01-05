# -*- coding: utf-8 -*- 

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'
plt.rcParams['axes.unicode_minus']=False

x = ['第一季', '第二季', '第三季', '第四季']
s = [20000,15000,17000, -8000]
plt.barh(x, s,color='red')
plt.ylabel('季別')
plt.xlabel('損益金額')
plt.title('今年度營業獲利的概況')
plt.show()
