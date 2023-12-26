# ch6_29.py
# 在串列中使用 count()
fruits = ["apple", "banana", "cherry", "apple", "cherry"]
apple_count = fruits.count("apple")
print(apple_count)                  # 輸出：2

# 在字串中使用 count()
text = "Hello, how are you? How can I help you?"
how_count = text.count("how")
print(how_count)                    # 輸出：1

# 在字串中指定搜索範圍
how_count_range = text.count("how", 0, 15)
print(how_count_range)              # 輸出：1


