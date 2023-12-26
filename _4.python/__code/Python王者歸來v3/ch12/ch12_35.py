# ch12_35.py
# 定義 Inventory 類別來管理商品庫存
class Inventory:
    # 初始化方法，建立一個空的商品字典
    def __init__(self):
        self.items = {}         # 商品字典，鍵是商品名，值是商品數量

    # 庫存中添加商品,如果商品存在則更新其數量；如果不存在則添加到字典中 
    def add_item(self, item, quantity):
        self.items[item] = self.items.get(item, 0) + quantity

    # 庫存中移除商品
    def remove_item(self, item, quantity):
        # 檢查商品是否存在且數量充足，然後從庫存中移除指定數量的商品
        if item in self.items and self.items[item] >= quantity:
            self.items[item] -= quantity
            # 如果商品數量為0，從字典中移除該商品
            if self.items[item] == 0:
                del self.items[item]

# 使用 Inventory 類別來管理庫存
inventory = Inventory()                 # 建立 Inventory 物件
inventory.add_item('apple', 10)         # 向庫存中添加10個蘋果
inventory.remove_item('apple', 3)       # 從庫存中移除3個蘋果

# 查看庫存的目前狀態
print(inventory.items)                  # 輸出：{'apple': 7}




