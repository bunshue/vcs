import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'

name = ['鼠', '牛', '虎', '兔', '龍']
weight = [3, 48, 33, 8, 38]
plt.bar(name, weight)

plt.ylabel('體重(單位:公斤)')
plt.title('動物體重 使用中文')

plt.show()
