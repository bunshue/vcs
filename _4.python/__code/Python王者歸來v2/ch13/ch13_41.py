# ch13_41.py
from collections import Counter

fruits1 = ["apple","orange","apple"]
fruitsdictA = Counter(fruits1)
fruits2 = ["grape","orange","orange", "grape"]
fruitsdictB = Counter(fruits2)
# 交集
fruitsdictInter = fruitsdictA & fruitsdictB
print(fruitsdictInter)
# 聯集
fruitsdictUnion = fruitsdictA | fruitsdictB
print(fruitsdictUnion)

















