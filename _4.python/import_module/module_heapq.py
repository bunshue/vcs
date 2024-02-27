
import heapq

h = [10, 21, 5, 9, 13, 28, 3]
print("執行前 h = ", h)
heapq.heapify(h)
print("執行後 h = ", h)

print("------------------------------------------------------------")  # 60個

import heapq

h = [10, 21, 5, 9, 13, 28, 3]
heapq.heapify(h)
print("插入前 h = ", h)
heapq.heappush(h, 11)
print("第一次插入後 h = ", h)
heapq.heappush(h, 2)
print("第二次插入後 h = ", h)

print("------------------------------------------------------------")  # 60個

import heapq

h = [10, 21, 5, 9, 13, 28, 3]
heapq.heapify(h)
print("取出前 h = ", h)
val = heapq.heappop(h)
print("取出元素 = ", val)
print("取出後 h = ", h)


print("------------------------------------------------------------")  # 60個

import heapq

h = [10, 21, 5, 9, 13, 28, 3]
heapq.heapify(h)
print("堆入和取出前 h = ", h)
val = heapq.heappushpop(h, 11)
print("取出元素 = ", val)
print("堆入和取出後 h = ", h)

print("------------------------------------------------------------")  # 60個

import heapq

h = [10, 21, 5, 9, 13, 28, 3]
print("最大 3 個  : ", heapq.nlargest(3, h))
print("最小 3 個  : ", heapq.nsmallest(3, h))
print("原先資料集 : ", h)

print("------------------------------------------------------------")  # 60個

import heapq

h = [10, 21, 5, 9, 13, 28, 3]
heapq.heapify(h)
print("執行前 h = ", h)
x = heapq.heapreplace(h, 7)
print("取出值   = ", x)
print("執行後 h = ", h)

print("------------------------------------------------------------")  # 60個

import heapq

h = []
heapq.heappush(h, (100, "牛肉麵"))
heapq.heappush(h, (60, "陽春麵"))
heapq.heappush(h, (80, "肉絲麵"))
heapq.heappush(h, (90, "大滷麵"))
heapq.heappush(h, (70, "家常麵"))
print(h)
print(heapq.heappop(h))

print("------------------------------------------------------------")  # 60個

import heapq

def heapsort(iterable):
    h = []
    for data in iterable:
        heapq.heappush(h, data)
    return [heapq.heappop(h) for i in range(len(h))]


h = [10, 21, 5, 9, 13, 28, 3]
print("排序前 ", h)
print("排序後 ", heapsort(h))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
