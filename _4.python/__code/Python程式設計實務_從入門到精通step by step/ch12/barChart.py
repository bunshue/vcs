# -*- coding: utf-8 -*- 

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'

x = ['第1學期', '第2學期', '第3學期', '第4學期','第5學期', '第6學期', '第7學期', '第8學期']
s = [95.3, 94.2,91.4,96.2,92.3, 93.6,89.4,91.2]
plt.bar(x, s)
plt.ylabel('平均分數')
plt.title('大學四年各學期的平均分數')
plt.show()
