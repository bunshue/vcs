#!/usr/bin/env python
# author: Powen Ko      www.powenko.com
import matplotlib.pyplot as plt # 繪圖函示庫
plt.plot([1, 2, 3, 4], [0, 0.3, 0.6, 0.9], 'gx')  # 在x=1,y=0 四個位置繪製(g)色x 標記
plt.plot([1, 2, 3, 4], [0, 0.3, 0.6, 0.9], 'r--') # 繪製(r)紅色- 標記也就是線（趨勢線）
plt.axis([0, 5, 0, 1])  # 圖表大小範圍，寬度由0到5 ,高度由0到1
plt.ylabel('Y')  # 設定顯示Y 文字
plt.xlabel('X')  # 設定顯示X 文字
plt.legend(('price','passenger'),loc='upper right')
plt.show()   # 繪製圖表

