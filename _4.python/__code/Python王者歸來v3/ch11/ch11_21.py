# ch11_21.py
def kitchen(unserved, served):
    """ 將未服務的餐點轉為已經服務 """
    print("\n廚房處理顧客所點的餐點")
    while unserved:
        current_meal = unserved.pop( )
        # 模擬出餐點過程
        print(f"菜單: {current_meal}")
        # 將已出餐點轉入已經服務串列
        served.append(current_meal)
    print()

def show_unserved_meal(unserved):
    """ 顯示尚未服務的餐點 """
    print("=== 下列是尚未服務的餐點 ===")
    if not unserved:
        print("*** 沒有餐點 ***")
    for unserved_meal in unserved:
        print(unserved_meal)
        
def show_served_meal(served):
    """ 顯示已經服務的餐點 """
    print("=== 下列是已經服務的餐點 ===")
    if not served:
        print("*** 沒有餐點 ***")
    for served_meal in served:
        print(served_meal)

order_list = ['大麥克', '可樂', '麥克雞塊']  # 所點餐點
served_list = []                           # 已服務餐點
# 列出餐廳處理前的點餐內容
show_unserved_meal(order_list)             # 列出未服務餐點
show_served_meal(served_list)              # 列出已服務餐點
# 餐廳服務過程
kitchen(order_list, served_list)           # 餐廳處理過程
# 列出餐廳處理後的點餐內容
show_unserved_meal(order_list)             # 列出未服務餐點
show_served_meal(served_list)              # 列出已服務餐點

