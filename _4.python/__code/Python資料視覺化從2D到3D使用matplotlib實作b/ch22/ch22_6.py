# ch22_6.py
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
# 建立測試資料
np.random.seed(10)
data = [sorted(np.random.normal(0, std, 100)) for std in range(1, 5)]
# 建立子圖
fig, axes = plt.subplots()
axes.set_title('設計小提琴圖',fontsize=16,color='b')
parts = axes.violinplot(
        data, showmeans=False, showmedians=False)
# 建立小提琴圖
for p in parts['bodies']:
    p.set_facecolor('red')
    p.set_edgecolor('black')
    p.set_alpha(1)
# 獲得小提琴圖最大值
wseg = parts['cmaxes'].get_segments()       # 小提琴圖最大值線段
w_max = []                                  # 設定最大值串列
for i in range(len(wseg)):
    upper_array = wseg[i]
    for j in range(0,len(upper_array),2):
        w_max.append(upper_array[j][1])     # 取得最大值 y 軸值
# 獲得小提琴圖最小值
wseg = parts['cmins'].get_segments()        # 小提琴圖最大值線段
c_min = []                                  # 設定最大值串列
for i in range(len(wseg)):
    lower_array = wseg[i]
    for j in range(0,len(lower_array),2):
        c_min.append(lower_array[j][1])     # 取得最小值 y 軸值
# 繪製小提琴內部
quartile1,medians,quartile3=np.percentile(data,[25,50,75],axis=1)
inds = np.arange(1, len(medians) + 1)
axes.scatter(inds,medians,marker='*',color='white',s=30,zorder=3)
axes.vlines(inds,quartile1,quartile3,color='b', linestyle='-',lw=5)
axes.vlines(inds,c_min,w_max,color='b',linestyle='-',lw=1)
# 設定 x 軸
labels = ['A', 'B', 'C', 'D']
axes.set_xticks(np.arange(1, len(labels) + 1))
axes.set_xticklabels(labels=labels)
axes.set_xlim(0.25, len(labels) + 0.75)
axes.set_xlabel('數據樣本',fontsize=12,color='b')
plt.show()


      
