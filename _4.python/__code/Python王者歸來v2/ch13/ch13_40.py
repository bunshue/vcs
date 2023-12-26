# ch13_40.py
from collections import Counter

fruits1 = ["apple","orange","apple"]
fruitsdictA = Counter(fruits1)
fruits2 = ["grape","orange","orange", "grape"]
fruitsdictB = Counter(fruits2)
# 加法
fruitsdictAdd = fruitsdictA + fruitsdictB
print(fruitsdictAdd)
# 減法
fruitsdictSub = fruitsdictA - fruitsdictB
print(fruitsdictSub)

















