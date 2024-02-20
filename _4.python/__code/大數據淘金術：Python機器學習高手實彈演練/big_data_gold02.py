import sys

import pandas as pd

print('------------------------------------------------------------')	#60個


import sys
import numpy as np
import matplotlib.pyplot as plt

# 4.2.1 準備工作
import numpy as np
import seaborn as sns
import statsmodels.api as sm # 示例使用了statsmodels庫中的自帶的數據
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

sns.set(style='darkgrid',color_codes=True) # 帶灰色網格的背景風格
tips=sns.load_dataset('tips')  # 示例中的基本數據

# 4.2.2 連續變量相關圖
# Relplot關係類型圖表
sns.relplot(x="total_bill", y="tip", hue="day",col="time", row="sex", data=tips)

plt.show()

print('------------------------------------------------------------')	#60個



# 點圖
sns.scatterplot(x="total_bill", y="tip", hue="size", size="size", data=tips)

plt.show()

print('------------------------------------------------------------')	#60個

# 線圖
sns.lineplot(x="tip", y="total_bill", hue="sex", style="sex", data=tips)

plt.show()

print('------------------------------------------------------------')	#60個

# 4.2.3 分類變量圖
# stripplot散點圖
sns.stripplot(x='day', y='total_bill', data=tips, jitter=True)

plt.show()

print('------------------------------------------------------------')	#60個

# swarmplot散點圖
sns.swarmplot(x='day',y='total_bill',data=tips)

plt.show()

print('------------------------------------------------------------')	#60個

# violinplot小提琴圖
sns.violinplot(x="day", y="total_bill", hue="sex", split=True, data=tips)

plt.show()

print('------------------------------------------------------------')	#60個

# boxplot箱式圖
sns.boxplot(x="day", y="total_bill", hue="sex", data=tips);

plt.show()

print('------------------------------------------------------------')	#60個

# boxenplot變種箱式圖
sns.boxenplot(x="day", y="total_bill", hue="sex", data=tips)

plt.show()

print('------------------------------------------------------------')	#60個

# pointplot分類統計圖
sns.pointplot(x="sex", y="total_bill", hue="smoker", data=tips,
palette={"Yes": "g", "No": "m"},
markers=["^", "o"], linestyles=["-", "--"]);

plt.show()

print('------------------------------------------------------------')	#60個

# barplot柱對比圖
sns.barplot(x='smoker',y='total_bill',hue='sex',data=tips)

plt.show()

print('------------------------------------------------------------')	#60個


# 4.2.4 迴歸圖
# 連續變量回歸圖
sns.lmplot(x="total_bill", y="tip", data=tips)

plt.show()

print('------------------------------------------------------------')	#60個


# 分類變量回歸圖
sns.lmplot(x="size", y="total_bill", data=tips, x_estimator=np.mean)

plt.show()

print('------------------------------------------------------------')	#60個


""" fail
# 4.2.5 多圖組合
# jointplot兩變量圖
import statsmodels.api as sm
import seaborn as sns
sns.set(style="darkgrid")
data = sm.datasets.ccard.load_pandas().data
g = sns.jointplot('AVGEXP', 'AGE', data=data, kind="reg",
                 xlim=(0, 1000), ylim=(0, 50), color="m")
plt.show()

print('------------------------------------------------------------')	#60個

"""

# pairplot多變量圖
data = sm.datasets.ccard.load_pandas().data
sns.pairplot(data, vars=['AGE','INCOME', 'INCOMESQ','OWNRENT'])

plt.show()


print('------------------------------------------------------------')	#60個

""" fail
# factorplot兩變量關係圖
data = sm.datasets.fair.load_pandas().data
sns.factorplot(x='occupation', y='affairs', hue='religious', data=data)

plt.show()
"""

print('------------------------------------------------------------')	#60個

""" fail
# FacetGrid結構化繪圖網格
g = sns.FacetGrid(tips, col = 'time', row = 'smoker') # 按行和列的分類做N個圖
g.map(plt.hist, 'total_bill', bins = 10) # 指定做圖方式

plt.show()
"""

print('------------------------------------------------------------')	#60個


# 4.2.6 熱力圖
data = sns.load_dataset('planets')
corr=data[['number','orbital_period','mass','distance']].corr(method='pearson')
sns.heatmap(corr, cmap="YlGnBu") 

plt.show()

print('------------------------------------------------------------')	#60個


""" fail
# 印刷品作圖

sns.set_style("whitegrid")

with sns.cubehelix_palette(start=2.7, rot=0, dark=.5, light=.8, 
          reverse=True, n_colors=5):
    # 此處放置具體繪圖函數
    sns.stripplot(x='day', y='total_bill', data=tips, jitter=True)

plt.show()
"""

print('------------------------------------------------------------')	#60個

""" fail
import numpy as np
import matplotlib.pyplot as plt

# 4.3.2 準備工作

import pyecharts
attr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]

# 4.3.3 繪製交互圖
# 柱圖
bar = pyecharts.Bar("Title1", "Title2")
bar.add("v1", attr, v1, mark_line=["average"], mark_point=["max", "min"])
bar.add("v2", attr, v2, mark_line=["average"], mark_point=["max", "min"])
bar.render('test.html')
bar

"""




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




