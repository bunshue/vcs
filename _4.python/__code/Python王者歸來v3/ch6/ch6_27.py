# ch6_27.py
# 在串列中使用 index()
fruits = ["apple", "banana", "cherry", "date"]
index = fruits.index("cherry")
print(index)                    # 輸出：2

# 指定搜索範圍, 搜尋的起始索引是 1
fruits = ["apple", "banana", "cherry", "date", "apple"]
index_range = fruits.index("apple", 1)
print(index_range)              # 輸出：4


