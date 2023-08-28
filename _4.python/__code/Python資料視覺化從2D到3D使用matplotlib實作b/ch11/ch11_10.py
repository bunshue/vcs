# ch11_10.py
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False

colName = ['sepal_len','sepal_wd','petal_len','petal_wd','species']
iris = pd.read_csv('iris.csv', names = colName)
x = iris['petal_len'].values        # 花瓣長度
y = iris['sepal_len'].values        # 花萼長度

fig, ax = plt.subplots()
mycmap = mpl.colors.ListedColormap(['b','g','r'])
norm = mpl.colors.BoundaryNorm([0,2,5,7], mycmap.N)
plt.scatter(x, y, c=x, cmap=mycmap, norm=norm)
fig.colorbar(mpl.cm.ScalarMappable(norm=norm,cmap=mycmap),ax=ax)
plt.show()










