"""
演算法_最強彩色圖鑑_Python程式實作_王者歸來(第二版)


"""

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


import itertools

x = ['1', '2', '3']
perm = itertools.permutations(x)
for i in perm:
    print(i)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\演算法_最強彩色圖鑑\ch01\ch1_4.py

# ch1_4.py
import matplotlib.pyplot as plt
import numpy as np

xpt = np.linspace(1, 10, 10)                # 建立含10個元素的陣列
ypt1 = xpt / xpt                            # 時間複雜度是 O(1)
ypt2 = np.log2(xpt)                         # 時間複雜度是 O(logn)               
ypt3 = xpt                                  # 時間複雜度是 O(n)
plt.plot(xpt, ypt1, '-o', label="O(1)")                  
plt.plot(xpt, ypt2, '-o', label="O(logn)")                  
plt.plot(xpt, ypt3, '-o', label="O(n)")
plt.legend(loc="best")                      # 建立圖例
plt.show()





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\演算法_最強彩色圖鑑\ch01\ch1_5.py

# ch1_5.py
import matplotlib.pyplot as plt
import numpy as np

xpt = np.linspace(1, 10, 10)                # 建立含10個元素的陣列
ypt1 = xpt / xpt                            # 時間複雜度是 O(1)
ypt2 = np.log2(xpt)                         # 時間複雜度是 O(logn)               
ypt3 = xpt                                  # 時間複雜度是 O(n)
ypt4 = xpt * np.log2(xpt)                   # 時間複雜度是 O(nlogn)
ypt5 = xpt * xpt                            # 時間複雜度是 O(n*n)
plt.plot(xpt, ypt1, '-o', label="O(1)")                  
plt.plot(xpt, ypt2, '-o', label="O(logn)")                  
plt.plot(xpt, ypt3, '-o', label="O(n)")
plt.plot(xpt, ypt4, '-o', label="O(nlogn)")
plt.plot(xpt, ypt5, '-o', label="O(n*n)")
plt.legend(loc="best")                      # 建立圖例
plt.show()



print("------------------------------------------------------------")  # 60個
btree = [0] * 16
print(type(btree))
print(btree)

            


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


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

#檔案 : C:\_git\vcs\_4.python\__code\演算法_最強彩色圖鑑\ch07\ch7_3.py

# ch7_3.py
import heapq

h = [10, 21, 5, 9, 13, 28, 3]
heapq.heapify(h)
print("取出前 h = ", h)
val = heapq.heappop(h)
print("取出元素 = ", val) 
print("取出後 h = ", h)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\演算法_最強彩色圖鑑\ch07\ch7_4.py

# ch7_4.py
import heapq

h = [10, 21, 5, 9, 13, 28, 3]
heapq.heapify(h)
print("堆入和取出前 h = ", h)
val = heapq.heappushpop(h, 11)
print("取出元素 = ", val) 
print("堆入和取出後 h = ", h)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\演算法_最強彩色圖鑑\ch07\ch7_5.py

# ch7_5.py
import heapq

h = [10, 21, 5, 9, 13, 28, 3]
print("最大 3 個  : ", heapq.nlargest(3, h))
print("最小 3 個  : ", heapq.nsmallest(3, h))
print("原先資料集 : ",h)





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\演算法_最強彩色圖鑑\ch07\ch7_6.py

# ch7_6.py
import heapq

h = [10, 21, 5, 9, 13, 28, 3]
heapq.heapify(h)
print("執行前 h = ", h)
x = heapq.heapreplace(h, 7)
print("取出值   = ", x)
print("執行後 h = ", h)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\演算法_最強彩色圖鑑\ch07\ch7_7.py

# ch7_7.py
import heapq

h = []
heapq.heappush(h, (100, '牛肉麵'))
heapq.heappush(h, (60, '陽春麵'))
heapq.heappush(h, (80, '肉絲麵'))
heapq.heappush(h, (90, '大滷麵'))
heapq.heappush(h, (70, '家常麵'))
print(h)
print(heapq.heappop(h))











print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\演算法_最強彩色圖鑑\ch07\ch7_8.py

# ch7_8.py
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

def bubble_sort(nLst):
    length = len(nLst)
    for i in range(length-1):
        print("第 %d 次外圈排序" % (i+1))
        for j in range(length-1-i):
            if nLst[j] > nLst[j+1]:
                nLst[j],nLst[j+1] = nLst[j+1],nLst[j]
            print("第 %d 次內圈排序 : " % (j+1), nLst)
    return nLst

data = [6, 1, 5, 7, 3]
print("原始串列 : ", data)
print("排序結果 : ", bubble_sort(data))




print("------------------------------------------------------------")  # 60個


import random

def quick_sort(nLst):
    ''' 快速排序法 '''
    if len(nLst) <= 1:
        return nLst

    left = []                           # 左邊串列
    right= []                           # 右邊串列
    piv = []                            # 基準串列
    pivot = random.choice(nLst)         # 隨機設定基準
    for val in nLst:                    # 分類
        if val == pivot:
            piv.append(val)             # 加入基準串列
        elif val < pivot:               # 如果小於基準
            left.append(val)            # 加入左邊串列
        else:
            right.append(val)           # 加入右邊串列
    return quick_sort(left) + piv + quick_sort(right)
        
data = [6, 1, 5, 7, 3, 9, 4, 2, 8] 
print("原始串列 : ", data)
print("排序結果 : ", quick_sort(data))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\演算法_最強彩色圖鑑\ch09\ch9_12.py

# ch9_12.py    
def merge(left, right):
    ''' 兩數列合併 '''
    output = []
    while left and right:
        if left[0] <= right[0]:
            output.append(left.pop(0))
        else:
            output.append(right.pop(0))
    if left:
        output += left
    if right:
        output += right
    return output

def merge_sort(nLst):
    ''' 合併排序 '''
    if len(nLst) <= 1:                      # 剩下一個或0個元素直接返回
        return nLst    
    mid = len(nLst) // 2                    # 取中間索引
    # 切割(divide)數列
    left = nLst[:mid]                       # 取左半段
    right = nLst[mid:]                      # 取右半段
    # 處理左序列和右邊序列
    left = merge_sort(left)                 # 左邊排序
    right = merge_sort(right)               # 右邊排序
    # 遞迴執行合併
    return merge(left, right)               # 傳回合併

data = [6, 1, 5, 7, 3, 9, 4] 
print("原始串列 : ", data)
print("排序結果 : ", merge_sort(data))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\演算法_最強彩色圖鑑\ch09\ch9_2.py

# ch9_2.py
cars = ['honda','bmw','toyota','ford']     
print("目前串列內容 = ",cars)
print("使用sort( )由小排到大")
cars.sort( )            
print("排序串列結果 = ",cars)
nums = [5, 3, 9, 2]
print("目前串列內容 = ",nums)
print("使用sort( )由小排到大")
nums.sort( )            
print("排序串列結果 = ",nums)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\演算法_最強彩色圖鑑\ch09\ch9_3.py

# ch9_3.py
cars = ['honda','bmw','toyota','ford']     
print("目前串列內容 = ",cars)
print("使用sort( )由大排到小")
cars.sort(reverse=True)            
print("排序串列結果 = ",cars)
nums = [5, 3, 9, 2]
print("目前串列內容 = ",nums)
print("使用sort( )由大排到小")
nums.sort(reverse=True)            
print("排序串列結果 = ",nums)

    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\演算法_最強彩色圖鑑\ch09\ch9_4.py

# ch9_4.py    
def cocktail_sort(nLst):
    ''' 雞尾酒排序 '''
    n = len(nLst) 
    is_sorted = True
    start = 0                                       # 前端索引
    end = n-1                                       # 末端索引
    while is_sorted: 
        is_sorted = False                           # 重置是否排序完成
        for i in range (start, end):                # 往右比較
            if (nLst[i] > nLst[i + 1]) : 
                nLst[i], nLst[i + 1]= nLst[i + 1], nLst[i] 
                is_sorted = True
        print("往後排序過程 : ", nLst)
        if not is_sorted:                           # 如果沒有交換就結束
            break

        end = end-1                                 # 末端索引左移一個索引
        for i in range(end-1, start-1, -1):         # 往左比較
            if (nLst[i] > nLst[i + 1]): 
                nLst[i], nLst[i + 1] = nLst[i + 1], nLst[i] 
                is_sorted = True
        start = start + 1                           # 前端索引右移一個索引
        print("往前排序過程 : ", nLst)
    return nLst
         
data = [6, 1, 5, 7, 3] 
print("原始串列 : ", data)
print("排序結果 : ", cocktail_sort(data))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\演算法_最強彩色圖鑑\ch09\ch9_5.py

# ch9_5.py    
def selection_sort(nLst):
    for i in range(len(nLst)-1):        
        index = i                           # 最小值的索引
        for j in range(i+1, len(nLst)):     # 找最小值的索引
            if nLst[index] > nLst[j]:
                index = j
        if i == index:                      # 如果目前索引是最小值索引
            pass                            # 不更動
        else:
            nLst[i],nLst[index] = nLst[index],nLst[i]   # 資料對調
        print("第 %d 次迴圈排序" % (i+1), nLst)
    return nLst

data = [6, 1, 5, 7, 3]
print("原始串列 : ", data)
print("排序結果 : ", selection_sort(data))


    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\演算法_最強彩色圖鑑\ch09\ch9_6.py

# ch9_6.py
def selection_sort(nLst):
    ''' 選擇排序 '''
    for i in range(len(nLst)-1):        
        index = i                           # 最小值的索引
        for j in range(i+1, len(nLst)):     # 找最小值的索引
            if nLst[index] > nLst[j]:
                index = j
        if i == index:                      # 如果目前索引是最小值索引
            pass                            # 不更動
        else:
            nLst[i],nLst[index] = nLst[index],nLst[i]   # 資料對調
    return nLst

cars = ['honda','bmw','toyota','ford']     
print("目前串列內容 = ",cars)
print("使用selection_sort( )由小排到大")
selection_sort(cars)           
print("排序串列結果 = ",cars)



    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\演算法_最強彩色圖鑑\ch09\ch9_7.py

# ch9_7.py
def selection_sort(nLst):
    ''' 選擇排序 '''
    for i in range(len(nLst)-1):        
        index = i                           # 最小值的索引
        for j in range(i+1, len(nLst)):     # 找最小值的索引
            if nLst[index][2] < nLst[j][2]:
                index = j
        if i == index:                      # 如果目前索引是最小值索引
            pass                            # 不更動
        else:
            nLst[i],nLst[index] = nLst[index],nLst[i]   # 資料對調
    return nLst

music = [('李宗盛', '山丘', 24740000),
         ('趙傳', '我是一隻小小鳥', 8310000),
         ('五佰', '挪威的森林', 34130000),
         ('林憶蓮', '聽說愛情回來過', 12710000)
         ]
         
print("YouTube點播排行")
selection_sort(music)
for i in range(len(music)):
    print("{}:{}{} -- 點播次數 {}".format(i+1,music[i][0], music[i][1], music[i][2]))




    

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\演算法_最強彩色圖鑑\ch09\ch9_8.py

# ch9_8.py    
def insertion_sort(nLst):
    ''' 插入排序 '''
    n = len(nLst)
    if n == 1:                          # 只有1筆資料
        print("第 %d 次迴圈排序" % n, nLst)
        return nLst
    print("第 1 次迴圈排序", nLst)
    for i in range(1,n):                # 迴圈
        for j in range(i, 0, -1):
            if nLst[j] < nLst[j-1]: 
                nLst[j], nLst[j-1] = nLst[j-1], nLst[j]
            else:
                break
        print("第 %d 次迴圈排序" % (i+1), nLst)
    return nLst

data = [6, 1, 5, 7, 3]
print("原始串列 : ", data)
print("排序結果 : ", insertion_sort(data))

print("------------------------------------------------------------")  # 60個

def sequential_search(nLst):
    for i in range(len(nLst)):
        if nLst[i] == key:      # 找到了
            return i            # 傳回索引值
    return -1                   # 找不到傳回-1

data = [6, 1, 5, 7, 3, 9, 4, 2, 8]

#key = eval(input("請輸入搜尋值 : "))
key = 5
index = sequential_search(data)
if index != -1:
    print("在 %d 索引位置找到了共找了 %d 次" % (index, (index + 1)))
else:
    print("查無此搜尋號碼")

print("------------------------------------------------------------")  # 60個

def binary_search(nLst):
    print("列印搜尋串列 : ",nLst)
    low = 0                     # 串列的最小索引
    high = len(nLst) - 1        # 串列的最大索引
    middle = int((high + low) / 2)  # 中間索引
    times = 0                   # 搜尋次數
    while True:
        times += 1
        if key == nLst[middle]: # 表示找到了
            rtn = middle
            break
        elif key > nLst[middle]:
            low = middle + 1    # 下一次往右邊搜尋
        else:
            high = middle - 1   # 下依次往左邊搜尋
        middle = int((high + low) / 2)  # 更新中間索引
        if low > high:          # 所有元素比較結束
            rtn = -1
            break
    return rtn, times

data = [19, 32, 28, 99, 10, 88, 62, 8, 6, 3]
sorted_data = sorted(data)      # 排序串列
#key = int(input("請輸入搜尋值 : "))
key = 62
index, times = binary_search(sorted_data)
if index != -1:
    print("在索引 %d 位置找到了,共找了 %d 次" % (index, times))
else:
    print("查無此搜尋號碼")

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\演算法_最強彩色圖鑑\ch10\ch10_3.py

# ch10_3.py
data = [10, 30, 90, 77, 65]
max = data[0]
for num in data:
    if num > max:
        max = num
print("最大值 : ", max)









print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
