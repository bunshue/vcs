# ch18_4.py
import numpy as np
import matplotlib.pyplot as plt

def length(x1, y1, x2, y2):
    ''' 計算2點之間的距離 '''
    return int(((x1-x2)**2 + (y1-y2)**2)**0.5)

def clustering(x, y, cx, cy):
    ''' 對元素執行分群 '''
    clusters = []
    for i in range(cluster_number):                 # 建立群集
        clusters.append([])                              
    for i in range(seeds):                          # 為每個點找群集
        distance = INF                              # 設定最初距離
        for j in range(cluster_number):             # 計算每個點與群集中心的距離    
            dist = length(x[i], y[i], cx[j], cy[j])
            if dist < distance:
                distance = dist
                cluster_index = j                   # 分群的索引
        clusters[cluster_index].append([x[i], y[i]])    # 此點加入此索引的群集
    return clusters

def kmeans(x, y, cx, cy):
    ''' 建立群集和繪製各群集點和線條'''
    clusters = clustering(x, y, cx, cy) 
    plt.scatter(x, y, color='b')                        # 繪製元素點
    plt.scatter(cx, cy, color='r')                      # 用紅色繪群集中心

    c = ['r', 'g', 'y']                                 # 群集的線條顏色
    for index, node in enumerate(clusters):             # 為每個群集中心建立線條
        linex = []                                      # 線條的 x 座標
        liney = []                                      # 線條的 y 座標
        for n in node:
            linex.append([n[0], cx[index]])             # 建立線條x座標串列
            liney.append([n[1], cy[index]])             # 建立線條y座標串列
        color_c = c[index]                              # 選擇顏色
        for i in range(len(linex)):
            plt.plot(linex[i], liney[i], color=color_c) # 為第i群集繪線條
    plt.show()
    
# 群集中心, 元素的數量, 數據最大範圍
INF = 999                                               # 假設最大距離
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






