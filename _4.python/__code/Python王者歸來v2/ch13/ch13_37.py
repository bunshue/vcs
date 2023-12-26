# ch13_37.py

fruits = {}
for fruit in ["apple","orange","apple"]:
    if not fruit in fruits:
        fruits[fruit] = 0
    fruits[fruit] += 1

for fruit, count in fruits.items():
    print(fruit, count)


















