# ch18_2.py
import math
    
def knn(record, target, k):
    ''' 計算k組近鄰值, 以list回傳數量和距離 '''
    distances = []                              # 儲存紀錄與目標的距離  
    record_number = []                          # 儲存紀錄的烤香腸數量
    
    for r in record:                            # 計算過往紀錄與目標的距離
        tmp = 0
        for i in range(len(target)-1):
            tmp += (target[i] - r[i]) ** 2
        dist = math.sqrt(tmp)
        distances.append(dist)                  # 儲存距離
        record_number.append(r[len(target)-1])  # 儲存烤香腸數量
   
    knn_number = []                             # 儲存k組烤香腸數量
    knn_distances = []                          # 儲存k組距離值
    for i in range(k):                          # k代表取k組近鄰值
        min_value = min(distances)              # 計算最小值
        min_index = distances.index(min_value)  # 計算最小值索引
        # 將香腸數量分別儲存至knn_number串列
        knn_number.append(record_number.pop(min_index))
        # 將距離分別儲存至knn_distances
        knn_distances.append(distances.pop(min_index))
    return knn_number,knn_distances
        
def regression(knn_num):
    ''' 計算迴歸值 '''
    return int(sum(knn_num)/len(knn_num))

target = [1, 5, 2, 'value']         # value是需計算的值
# 過往紀錄
record = [
    [0, 3, 3, 100],
    [2, 4, 3, 250],
    [2, 5, 6, 350],
    [1, 4, 2, 180],
    [2, 3, 1, 170],
    [1, 5, 4, 300],
    [0, 1, 1, 50],
    [2, 4, 3, 275],
    [2, 2, 4, 230],
    [1, 3, 5, 165],
    [1, 5, 5, 320],
    [2, 5, 1, 210],
]

k = 5                               # 設定k組最相鄰的值
k_nn = knn(record, target, k)
print("需準備 %d 條烤香腸" % regression(k_nn[0]))
for i in range(k):
    print("k組近鄰的距離 %6.4f, 銷售數量 %d" % (k_nn[1][i], k_nn[0][i]))






