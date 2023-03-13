import matplotlib.pyplot as plt
import numpy as np

filename = 'data\popu.txt'
with open(filename, 'r') as fp:
	populations = fp.readlines()

city = list()
popu = list()

for p in populations:
	cc, pp = p.split(',')
	city.append(cc)
	popu.append(int(pp))

ind = np.arange(len(city))

plt.bar(ind, popu)
plt.xticks(ind+0.5, city)
#plt.title('台灣各縣市人口統計')
plt.show()
