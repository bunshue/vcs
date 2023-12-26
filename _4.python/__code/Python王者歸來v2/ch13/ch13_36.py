# ch13_36.py
from collections import defaultdict

fruits = defaultdict(int)
for fruit in ["apple","orange","apple"]:
    fruits[fruit] += 1

for fruit, count in fruits.items():
    print(fruit, count)


















