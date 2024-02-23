# ch18_3.py
import numpy as np
import matplotlib.pyplot as plt

def kmeans(x, y, cx, cy):
    ''' 目前功能只是繪群集元素點 '''
    plt.scatter(x, y, color='b')                        # 繪製元素點
    plt.scatter(cx, cy, color='r')                      # 用紅色繪群集中心
    plt.show()
    
# 群集中心, 元素的數量, 數據最大範圍
cluster_number = 3                                      # 群集中心數量
seeds = 50                                              # 元素數量
limits = 100                                            # 值在(100, 100)內
# 使用隨機數建立seeds數量的種子元素
x = np.random.randint(0, limits, seeds)
y = np.random.randint(0, limits, seeds)
# 使用隨機數建立cluster_number數量的群集中心
cluster_x = np.random.randint(0, limits, cluster_number)
cluster_y = np.random.randint(0, limits, cluster_number)

kmeans(x, y, cluster_x, cluster_y)






