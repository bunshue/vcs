import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'

x = ['第1學期', '第2學期', '第3學期', '第4學期','第5學期', '第6學期', '第7學期', '第8學期']
s = [95.3, 94.2,91.4,96.2,92.3, 93.6,89.4,91.2]
plt.barh(x, s)
plt.ylabel('平均分數')
plt.title('大學四年各學期的平均分數')

plt.show()


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


import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'

x = ['第1學期', '第2學期', '第3學期', '第4學期','第5學期', '第6學期', '第7學期', '第8學期']
s = [95.3, 94.2,91.4,96.2,92.3, 93.6,89.4,91.2]
plt.bar(x, s,width=0.5, align='edge', color='r', ec='y',lw=2)
plt.ylabel('平均分數')
plt.title('大學四年各學期的平均分數')
plt.show()




