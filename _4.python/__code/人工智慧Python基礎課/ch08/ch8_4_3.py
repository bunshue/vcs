# coding: utf-8
d1 = {1:1, 2:4, "name":"joe", "age":20, 5:22}
del d1[2]
print(d1)
del d1["age"]
print(d1)
e1 = d1.pop(5)
print(e1, d1)
e2 = d1.popitem()
print(e2, d1)
d1.clear()
print(d1)
