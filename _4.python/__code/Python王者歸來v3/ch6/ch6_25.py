# ch6_25.py
# 基本排序
numbers = [3, 5, 1, 4, 2]
numbers.sort()
print(numbers)          # 輸出：[1, 2, 3, 4, 5]

# 降序排序
numbers = [3, 5, 1, 4, 2]
numbers.sort(reverse=True)
print(numbers)          # 輸出：[5, 4, 3, 2, 1]

# 使用函數定義排序
words = ["banana", "apple", "strawberry"]
words.sort(key=len)
print(words)            # 輸出：['apple', 'banana', 'strawberry]



