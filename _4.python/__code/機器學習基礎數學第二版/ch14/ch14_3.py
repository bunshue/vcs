import matplotlib.pyplot as plt
import numpy as np

import seaborn as sns #海生, 自動把圖畫得比較好看

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.title('二項式分布 Binomial')
plt.xlabel("銷售張數", fontsize=14)
plt.ylabel("成功次數", fontsize=14)
sns.histplot(np.random.binomial(n=5, p=0.75, size=1000), kde=False)

plt.show()












