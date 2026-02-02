# ch4_19.py
import pandas as pd
import matplotlib.pyplot as plt

cities = {'population':[10000000,8500000,8000000,15000000,6000000,8000000],
          'area':[400, 500, 850, 300, 200, 320],
          'town':['New York','Chicago','Bangkok','Tokyo',
                   'Singapore','HongKong']}
tw = pd.DataFrame(cities, columns=['population','area'],index=cities['town'])

fig, ax = plt.subplots()
fig.suptitle("City Statistics")
ax.set_ylabel("Population")
ax.set_xlabel("City")

ax2 = ax.twinx()
ax2.set_ylabel("Area")
tw['population'].plot(ax=ax,rot=90)     # 繪製人口數線
tw['area'].plot(ax=ax2, style='g-')     # 繪製面積線
ax.legend(loc=1)                        # 圖例位置在右上
ax2.legend(loc=2)                       # 圖例位置在左上
plt.show()








