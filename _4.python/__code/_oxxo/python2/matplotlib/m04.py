import numpy as np
from matplotlib import pyplot as plt

ax = np.linspace(0, 20, 100)
ay = ax*0.5
by = np.sin(ax)

# 產生子圖表，第一個數值為縱軸要有幾張圖，第二個數值為橫軸，第三個數值為排在哪裡
# label 可以設定圖例標籤
#  '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
plt.plot(ax, ay, color='red', linewidth=8.0, linestyle='dotted', label='x0.5')
plt.plot(ax, by, color='blue', linewidth=2.0, linestyle='-', label='sin')
plt.title('demo')
# 設定圖例標籤位置 ( best, upper, lower, right,left,center )
plt.legend(loc='lower center')
plt.xlabel("ax")
plt.ylabel("ay")
plt.ylim((-5, 10))  # y 軸上下最大和最小區間
plt.xlim((0, 20))  # y 軸上下最大和最小區間
plt.yticks([-5, 0, 10], ['min(-5)', '0', 'max(10)'])  # 可以設置座標軸上特定文字

xx = plt.gca()
xx.spines['right'].set_color('none')  # 設置邊框樣式
xx.spines['top'].set_color('none')
xx.spines['bottom'].set_position(('data', 0))  # 設置邊框位置

plt.show()
