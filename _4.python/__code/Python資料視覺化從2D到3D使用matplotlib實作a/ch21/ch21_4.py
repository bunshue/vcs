# ch21_4.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
fig, ax = plt.subplots()
ax.broken_barh([(60, 40), (130, 20)],
               (7, 10),
               facecolors='cyan')
ax.broken_barh([(10, 40), (90, 20), (120, 20)],
               (20, 10),
               facecolors=('m','g','b'))
ax.annotate('學習中斷', (50, 25),
            xytext=(0.6, 0.92), textcoords='axes fraction',
            arrowprops=dict(fc='r', ec='r', shrink=0.05),
            fontsize=14, color='r',
            horizontalalignment='right', verticalalignment='top')
ax.set_ylim(5, 35)
ax.set_xlim(0, 160)
ax.set_xlabel('時間 : 單位秒',color='b')
ax.set_yticks([12, 25])
ax.set_yticklabels(labels=['雨星', '冰雨'],color='b')
ax.grid(True)
ax.set_title('學習觀察表',fontsize=16,color='b')
plt.show()



      
