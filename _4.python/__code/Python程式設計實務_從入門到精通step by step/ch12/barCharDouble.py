# -*- coding: utf-8 -*- 

import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'

x=['上學期', '下學期']
s1,s2,s3,s4 = [96.2, 87.1], [88.9, 95.2], [85.1, 91.5], [95.2, 96.7]

index = np.arange(len(x)) 
width=0.15
plt.bar(index - 1.5*width, s1, width, color='b')
plt.bar(index - 0.5*width, s2, width, color='r')
plt.bar(index + 0.5*width, s3, width, color='y')
plt.bar(index + 1.5*width, s4, width, color='g')

plt.xticks(index, x)
plt.legend(['2017年','2018年','2019年','2020年'])

plt.ylabel('平均分數,取到小數點第一位')
plt.title('大學四年各學期平均成績比較表')
plt.show()
