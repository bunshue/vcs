# ch13_34.py
from collections import defaultdict
def price():
    return 10

fruits = defaultdict(price)
fruits["apple"] = 20
fruits["orange"]            # 使用自行設計的price()
print(fruits["apple"])
print(fruits["orange"])
print(fruits)
















