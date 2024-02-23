# ex3_2.py
class Node():
    ''' 節點 '''
    def __init__(self, data=None):
        self.data = data            # 資料
        self.next = None            # 指標

class Linked_list():
    ''' 鏈結串列 '''
    def __init__(self): 
        self.head = None            # 鏈結串列第 1 個節點

    def print_list(self):
        ''' 列印鏈結串列 '''   
        ptr = self.head             # 指標指向鏈結串列第 1 個節點
        while ptr:
            print(ptr.data)         # 列印節點
            ptr = ptr.next          # 移動指標到下一個節點

    def search(self, val):
        ptr = self.head
        count = 0
        while ptr:
            if ptr.data == val:
                count += 1
            ptr = ptr.next
        return count
    
link = Linked_list()
link.head = Node(5)
n2 = Node(15)                       # 節點 2
n3 = Node(5)                        # 節點 3
link.head.next = n2                 # 節點 1 指向節點 2
n2.next = n3                        # 節點 2 指向節點 3
print("所建的鏈結串列")
link.print_list()                   # 列印鏈結串列 link
print("分別列出數值5, 15, 20的出現次數")
print("5  出現 %d 次" % link.search(5))
print("15 出現 %d 次" % link.search(15))
print("20 出現 %d 次" % link.search(20))









