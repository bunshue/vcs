# ch6_26.py
# 基本排序
numbers = [3, 5, 1, 4, 2]
sorted_numbers = sorted(numbers)
print(sorted_numbers)       # 輸出：[1, 2, 3, 4, 5]

# 按降序排序
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc)  # 輸出：[5, 4, 3, 2, 1]

# 使用 key 函數排序
words = ["banana", "apple", "strawberry"]
sorted_words = sorted(words, key=len)
print(sorted_words)         # 輸出：['apple', 'banana', 'strawberry]

# 對字串排序
string = "hello"
sorted_chars = sorted(string)
print(sorted_chars)         # 輸出：['e', 'h', 'l', 'l', 'o']


