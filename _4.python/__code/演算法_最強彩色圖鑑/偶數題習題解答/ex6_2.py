# ex6_2.py
class Node():
    def __init__(self, data=None):
        ''' 建立二元樹的節點 '''
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        ''' 建立二元樹 '''
        if self.data:                           # 如果根節點存在
            if data < self.data:                # 插入值小於目前節點值
                if self.left:
                    self.left.insert(data)      # 遞迴呼叫往下一層
                else:
                    self.left = Node(data)      # 建立新節點存放資料
            else:                               # 插入值大於目前節點值
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)                
        else:                                   # 如果根節點不存在
            self.data = data                    # 建立根節點
            
    def postorder(self):
        ''' 後序列印 '''                      
        if self.left:                           # 如果左子節點存在
            self.left.postorder()               # 遞迴呼叫下一層        
        if self.right:                          # 如果右子節點存在
            self.right.postorder()              # 遞迴呼叫下一層
        print(self.data)                        # 列印        

    def depth(self):
        current_depth = 0
        if self.left:
            current_depth = max(current_depth, self.left.depth())
        if self.right:
            current_depth = max(current_depth, self.right.depth())
        return current_depth + 1
        
num = 0        
tree = Node()                                   # 建立二元樹物件
datas = [10, 5, 21, 9, 13, 28, 3, 4, 1, 17, 32] # 建立二元樹數據
for d in datas:
    tree.insert(d)                              # 分別插入數據
print("所建的二元樹後序列印如下 : ")
tree.postorder()                                # 後序列印
print("二元樹的深度 = ", tree.depth())





    















