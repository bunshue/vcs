# ch10_22.py
# 創建一個集合
myset = {5, 3, 8, 1, 2}

print(f"集合元素數量   : {len(myset)}")
print(f"集合元素最大值 : {max(myset)}")
print(f"集合元素最小值 : {min(myset)}")
print(f"集合元素總和   : {sum(myset)}")

# 使用 sorted() 函數對集合進行排序
sorted_list = sorted(myset)
print(f"小到大排序 : {sorted_list}")         # 輸出: [1, 2, 3, 5, 8]
sorted_list_desc = sorted(myset, reverse=True)
print(f"大到小排序 : {sorted_list_desc}")    # 輸出: [8, 5, 3, 2, 1]



    
