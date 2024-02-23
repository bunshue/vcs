# ex7_2.py
class Heaptree():
    def __init__(self):
        self.heap = []                              # 堆積樹串列
        self.size = 0                               # 堆積樹串列元素個數

    def data_down(self,i):
        ''' 如果節點值大於子節點值則資料與較小的子節點值對調 '''
        while (i * 2 + 2) <= self.size:             # 如果有子節點則繼續
            mi = self.get_min_index(i)              # 取得較小值得子節點
            if self.heap[i] > self.heap[mi]:        # 如果目前節點大於子節點
                self.heap[i], self.heap[mi] = self.heap[mi], self.heap[i]  
            i = mi

    def get_min_index(self,i):
        ''' 傳回較小值的子節點索引 '''
        if i * 2 + 2 >= self.size:                  # 只有一個左子節點
            return i * 2 + 1                        # 傳回左子節點索引
        else:           
            if self.heap[i*2+1] < self.heap[i*2+2]: # 如果左子節點小於右子節點
                return i * 2 + 1                    # True傳回左子節點索引
            else:
                return i * 2 + 2                    # False傳回右子節點索引

    def build_heap(self, mylist):                       
        ''' 建立堆積樹 '''
        i = (len(mylist) // 2) - 1                  # 從有子節點的節點開始處理
        self.size = len(mylist)                     # 得到串列元素個數
        self.heap = mylist                          # 初步建立堆積樹串列
        while (i >= 0):                             # 從下層往上處理
            self.data_down(i)
            i = i - 1

    def get_min(self):
        min_ret = self.heap[0]
        self.size -= 1
        self.heap[0] = self.heap[self.size]
        self.heap.pop()
        self.data_down(0)
        return min_ret

h = [10, 21, 5, 9, 13, 28, 3]
print("執行前普通串列   = ", h)
obj = Heaptree()
obj.build_heap(h)                                   # 建立堆積樹串列
print("執行後堆積樹串列 = ", obj.heap)
min = obj.get_min()
print("所獲得的最小值   = ", min)
print("執行後堆積樹串列 = ", obj.heap)





  





