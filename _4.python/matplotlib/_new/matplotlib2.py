
print("------------------------------------------------------------")  # 60個




import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'

name = ['鼠', '牛', '虎', '兔', '龍']
weight = [3, 48, 33, 8, 38]
plt.bar(name, weight)

plt.ylabel('體重(單位:公斤)')
plt.title('動物體重 使用中文')

plt.show()


import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='DFKai-SB'
plt.rcParams['font.size'] = 15  #預設值10.0

name = ['鼠', '牛', '虎', '兔', '龍']
weight = [3, 48, 33, 8, 38]

plt.bar(name, weight, width = 0.8, align = 'edge', color = 'r', ec = 'y', lw = 2)

plt.ylabel('體重(單位:公斤)')
plt.title('動物體重 使用中文')

plt.show()


import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'

name = ['鼠', '牛', '虎', '兔', '龍']
weight = [3, 48, 33, 8, 38]

plt.bar(name, weight, width = 0.8, align = 'edge', color = 'r', ec = 'y', lw = 2)

plt.ylabel('體重(單位:公斤)')
plt.title('動物體重 使用中文')

plt.show()




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

